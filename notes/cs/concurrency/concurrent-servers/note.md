---
title: "Concurrent Servers"
sources: [cmu15213-23, cmu15213lab-7]
requires: [cs/systems-io-networking/sockets-interface, cs/exceptional-control-flow/signal-handling]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 23 "Concurrent Programming" (iterative servers, process-based and event-based servers) and the Proxy Lab handout (part II: concurrent requests), in our own wording; the code is our own. -->

Logical control flows are *concurrent* if they overlap in time (@def-concurrent-flows). Concurrency at the application level lets a server serve many clients at once, lets a program do useful work while it waits for slow I/O, and lets it use several cores. There are three basic ways to write concurrent programs: processes, I/O multiplexing and threads; this note applies the first two to servers, and @sec-cs-concurrency-threads treats the third.

::: {#prp-iterative-server-flaw .proposition name="An iterative server serves one client at a time"}

In an iterative server (@exm-echo-server), a client that connects while the server is serving another client gets no service until the first client closes its connection, however long that takes.

:::

::: {.proof}
1. The server's only thread of control is in the loop `accept`, `echo(connfd)`, `close(connfd)`.

2. While it runs `echo` for client 1, it does not call `accept`; client 2's `connect` completes (the kernel queues the connection request on the listening socket), so client 2 can even send its first line, but nobody reads it.

3. Client 2's `read` of the reply therefore blocks until `echo` for client 1 returns, which happens only when client 1 closes its end. A client that walks away from an open connection blocks every later client indefinitely.
:::

::: {#fig-concurrent-servers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.8cm]
\node[lab] at (0,0.6) {client 1}; \node[lab] at (4,0.6) {server}; \node[lab] at (8,0.6) {client 2};
\draw[faint] (0,0.2) -- (0,-5.4); \draw[faint] (4,0.2) -- (4,-5.4); \draw[faint] (8,0.2) -- (8,-5.4);
\draw[->] (0,0) -- node[edge label, above] {\texttt{connect}} (4,-0.3);
\draw[->] (0,-0.8) -- node[edge label, above] {\texttt{write}} (4,-1.1);
\draw[->] (4,-1.3) -- node[edge label, below] {reply} (0,-1.6);
\node[tick, anchor=east] at (-0.1,-2.6) {user goes to lunch};
\draw[hl] (0,-2.0) -- (0,-4.6);
\draw[->, draw=accent] (8,-1.4) -- node[edge label, above] {\texttt{connect}} (4.1,-1.7);
\draw[->, draw=accent] (8,-2.2) -- node[edge label, above] {\texttt{write}} (4.1,-2.5);
\node[dot] at (8,-3.0) {}; \node[tick, anchor=west] at (8.1,-3.0) {\texttt{read} blocks};
\draw[hl] (8,-3.0) -- (8,-4.8);
\draw[->] (0,-4.6) -- node[edge label, above] {\texttt{close}} (4,-4.9);
\draw[->] (4,-5.1) -- node[edge label, below] {now served} (8,-5.3);
\end{tikzpicture}
\end{center}
```

The fundamental flaw of an iterative server: client 2's connection is set up by the kernel, but its request is not read until client 1 has finished

:::

::: {#def-process-based-server .definition name="Process-based server"}

A *process-based* concurrent server forks a child for each client (@def-fork). After `accept` returns a connected descriptor, the parent forks; the child closes its copy of the listening descriptor, serves the client, and exits; the parent closes its copy of the connected descriptor and returns to `accept`. A `SIGCHLD` handler reaps the terminated children (@exm-sigchld-reaping-bug shows how to write it correctly).

:::

::: {#exm-process-echo-server .example name="Process-based echo server"}

```c
void sigchld_handler(int sig) {
    int olderrno = errno;
    while (waitpid(-1, NULL, WNOHANG) > 0)
        ;                                    /* reap every terminated child */
    errno = olderrno;
}

int main(int argc, char **argv) {
    signal(SIGCHLD, sigchld_handler);
    int listenfd = open_listenfd(argv[1]);
    for (;;) {
        struct sockaddr_storage client;
        socklen_t len = sizeof client;
        int connfd = accept(listenfd, (struct sockaddr *)&client, &len);
        if (fork() == 0) {
            close(listenfd);                 /* child does not accept */
            echo(connfd);
            close(connfd);
            exit(0);
        }
        close(connfd);                       /* parent: essential */
    }
}
```

The parent's `close(connfd)` matters: the connection's open file entry is shared with the child (@prp-fork-shares-files), and it is released, and the client sees EOF, only when both copies are closed. Without it the parent leaks a descriptor per client and the connection stays open after the child exits.

:::

::: {#fig-concurrent-servers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (c1) at (0,1.6) {client 1};
\node[box] (c2) at (0,-1.6) {client 2};
\node[hl box] (p) at (4.5,0) {parent: \texttt{listenfd}};
\node[box] (ch1) at (8.5,1.6) {child 1: \texttt{connfd}};
\node[box] (ch2) at (8.5,-1.6) {child 2: \texttt{connfd}};
\draw[->, dashed] (c1) -- node[edge label, above] {connect} (p);
\draw[->, dashed] (c2) -- node[edge label, below] {connect} (p);
\draw[->] (p) -- node[edge label, above] {\texttt{fork}} (ch1);
\draw[->] (p) -- node[edge label, below] {\texttt{fork}} (ch2);
\draw[<->, emph, draw=accent] (c1) to[bend left=12] node[edge label, above] {data transfer} (ch1);
\draw[<->, emph, draw=accent] (c2) to[bend right=12] node[edge label, below] {data transfer} (ch2);
\end{tikzpicture}
\end{center}
```

Execution model of a process-based server: the parent only accepts; each client talks to its own child over a connected descriptor

:::

::: {#fig-concurrent-servers-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r/\t in {0/{1. after \texttt{accept}: parent holds \texttt{listenfd(3)} and \texttt{connfd(4)}},1/{2. after \texttt{fork}: both processes hold both descriptors},2/{3. after the \texttt{close} calls: parent keeps 3, child keeps 4}} {
  \node[tick, anchor=west] at (-0.6,-\r*1.9+0.8) {\t};
  \node[box] at (0.3,-\r*1.9) {client};
}
\node[box] at (5.0,0) {parent}; \node[hl dot] at (3.9,0.2) {}; \node[tick] at (3.9,0.45) {3}; \node[dot] at (3.9,-0.2) {}; \node[tick] at (3.9,-0.45) {4};
\draw[<->, draw=accent] (1.1,0) -- (3.8,-0.2);
\node[box] at (5.0,-1.9) {parent}; \node[hl dot] at (3.9,-1.7) {}; \node[dot] at (3.9,-2.1) {};
\node[box] at (5.0,-2.9) {child}; \node[hl dot] at (3.9,-2.7) {}; \node[dot] at (3.9,-3.1) {};
\draw[<->, draw=accent] (1.1,-1.9) -- (3.8,-2.1);
\draw[<->, draw=accent] (1.1,-1.9) -- (3.8,-3.1);
\node[box] at (5.0,-3.8) {parent}; \node[hl dot] at (3.9,-3.8) {}; \node[tick] at (3.6,-3.8) {3};
\node[box] at (5.0,-4.8) {child}; \node[dot] at (3.9,-4.8) {}; \node[tick] at (3.6,-4.6) {4};
\draw[<->, draw=accent] (1.1,-3.8) -- (3.8,-4.8);
\end{tikzpicture}
\end{center}
```

The descriptors of a process-based server: listening descriptors shaded, connected descriptors black. Each process closes the descriptor it does not need

:::

::: {#rmk-concurrent-servers-1 name="Pros and cons of processes"}

Processes handle many clients concurrently with a clean model: each has its own address space, so one client's code cannot corrupt another's state. The same separation is the drawback: sharing data such as a cache between clients needs explicit interprocess communication (pipes, shared memory), and creating and switching processes costs much more than the work of a small request.

:::

::: {#def-event-based-server .definition name="Event-driven server with I/O multiplexing"}

An *event-based* server runs as one process and keeps a set of active descriptors: the listening descriptor and every connected descriptor. In each iteration it calls `select` (or `epoll` on Linux), which blocks until at least one descriptor in the set is *ready*, that is, a read from it would not block, and reports which. The server then handles the ready descriptors: on the listening descriptor it calls `accept` and adds the new descriptor to the set; on a connected descriptor it reads and serves *one* line or request and returns to `select`. Each connection is a little state machine whose transitions are triggered by such input events.

:::

::: {#fig-concurrent-servers-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hl box] (sel) at (0,0) {\texttt{select}: wait until some descriptor is ready};
\node[box] (acc) at (-3.4,-1.8) {\texttt{listenfd} ready: \texttt{accept}, add \texttt{connfd}};
\node[box] (srv) at (3.4,-1.8) {\texttt{connfd} ready: read and echo one line};
\node[box] (cls) at (3.4,-3.2) {EOF: close, remove from set};
\draw[->] (sel) -- (acc); \draw[->] (sel) -- (srv); \draw[->] (srv) -- (cls);
\draw[->] (acc.west) -- ++(-0.4,0) |- (sel.west);
\draw[->] (srv.east) -- ++(0.4,0) |- (sel.east);
\draw[->] (cls.east) -- ++(0.8,0) |- (sel.east);
\foreach \i/\x in {0/-1.5,1/-0.5,2/0.5,3/1.5} { \draw[cell frame] (\x-0.45,1.0) rectangle (\x+0.45,1.5); }
\node[tick] at (-1.5,1.25) {3}; \node[tick] at (-0.5,1.25) {4}; \node[tick] at (0.5,1.25) {5}; \node[tick] at (1.5,1.25) {7};
\draw[hl cell] (0.05,1.0) rectangle (0.95,1.5); \node[tick] at (0.5,1.25) {5};
\node[tick, anchor=west] at (2.1,1.25) {active set; 5 is ready};
\end{tikzpicture}
\end{center}
```

An event-driven echo server: one loop waits for any ready descriptor and does a small, non-blocking step for it

:::

::: {#rmk-concurrent-servers-2 name="Pros and cons of events"}

An event-based server has one logical control flow and one address space, so it shares data freely, is easy to debug, and pays no process or thread switching costs; high-performance Web servers such as nginx are built this way. But it is harder to write: every handler must do only a bounded amount of work, so a slow client that sends half a line must not make the server wait for the rest, which means code must keep per-connection state by hand. And one process cannot use several cores.

:::

::: {#fig-concurrent-servers-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \c/\t in {0/{process-based},1/{event-based},2/{thread-based}} { \node[lab] at (3.2+\c*3.0,0) {\t}; }
\foreach \r/\q in {1/{control flows},2/{address spaces},3/{sharing data},4/{overhead},5/{multiple cores}} { \node[tick, anchor=west] at (-0.6,-\r*0.6) {\q}; }
\foreach \r/\a/\b/\c in {1/{one per client}/{one}/{one per client},2/{one per client}/{one}/{one, shared},3/{hard (IPC)}/{easy}/{easy, but races},4/{high}/{low}/{medium},5/{yes}/{no}/{yes}} {
  \node[tick] at (3.2,-\r*0.6) {\a}; \node[tick] at (6.2,-\r*0.6) {\b}; \node[tick] at (9.2,-\r*0.6) {\c};
}
\draw[faint] (-0.6,-0.3) -- (10.6,-0.3);
\end{tikzpicture}
\end{center}
```

The three approaches to concurrent servers compared

:::
