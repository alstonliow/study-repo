---
title: "The Sockets Interface"
sources: [cmu15213-21, cmu15213-22, cmu15213lab-7]
requires: [cs/systems-io-networking/network-basics, cs/systems-io-networking/unix-io]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lectures 21 and 22 "Network Programming" (socket addresses, getaddrinfo, the socket functions, helper functions, an echo client and server) and the Proxy Lab handout, in our own wording; the code is our own. -->

The *sockets interface* is a set of functions that, together with Unix I/O (@def-unix-read-write), let programs build network applications. To the kernel a socket is an endpoint of a connection (@def-internet-connection); to a program it is an open file with a descriptor, read and written like any other.

::: {#def-socket-address .definition name="Socket address structure"}

An Internet socket address is stored in a 16-byte structure
```c
struct sockaddr_in {
    uint16_t       sin_family;   /* AF_INET for IPv4 */
    uint16_t       sin_port;     /* port number, network byte order */
    struct in_addr sin_addr;     /* IP address, network byte order */
    unsigned char  sin_zero[8];  /* padding to the size of struct sockaddr */
};
```
Functions such as `connect`, `bind` and `accept` work with many kinds of addresses, so they take a pointer to a *generic* `struct sockaddr` (a 2-byte family followed by 14 bytes of address data) and the caller casts its specific structure to it. Port and address are always in network byte order, big endian; the functions `htons`, `htonl` convert a 16-bit or 32-bit value from host to network order and `ntohs`, `ntohl` back (@def-endianness).

:::

::: {#fig-sockets-interface-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm]
\foreach \i in {0,...,15} { \node[tick] at (\i+0.5,0.85) {\i}; }
\draw[cell frame] (0,0) rectangle (2,0.6); \node[tick] at (1,0.3) {family};
\draw[hl cell] (2,0) rectangle (4,0.6); \node[tick] at (3,0.3) {port};
\path[tintB] (4,0) rectangle (8,0.6); \draw[cell frame] (4,0) rectangle (8,0.6); \node[tick] at (6,0.3) {IP address};
\path[tintD] (8,0) rectangle (16,0.6); \draw[cell frame] (8,0) rectangle (16,0.6); \node[tick] at (12,0.3) {zero padding};
\node[lab, anchor=east] at (-0.2,0.3) {\texttt{sockaddr\_in}};
\draw[cell frame] (0,-1.2) rectangle (2,-0.6); \node[tick] at (1,-0.9) {family};
\path[tintC] (2,-1.2) rectangle (16,-0.6); \draw[cell frame] (2,-1.2) rectangle (16,-0.6); \node[tick] at (9,-0.9) {address data (14 bytes)};
\node[lab, anchor=east] at (-0.2,-0.9) {\texttt{sockaddr}};
\node[tick] at (3,-1.55) {\texttt{00 50}};
\node[tick] at (6,-1.55) {\texttt{80 02 C2 F2}};
\end{tikzpicture}
\end{center}
```

The 16 bytes of an IPv4 socket address and the generic structure it is cast to. For port $80$ at `128.2.194.242` the bytes are stored most significant first

:::

::: {#def-socket-functions .definition name="The socket functions"}

- `socket(domain, type, protocol)` creates a socket and returns its descriptor, not yet usable for I/O.
- A client calls `connect(fd, addr, addrlen)`, which blocks until a connection to the server at socket address `addr` is established or an error occurs; then `fd` is ready for reading and writing.
- A server calls `bind(fd, addr, addrlen)` to associate its socket address with `fd`, then `listen(fd, backlog)` to turn `fd` from an active socket into a *listening socket* that accepts connection requests.
- `accept(listenfd, addr, addrlen)` waits for a connection request on the listening descriptor, fills `addr` with the client's socket address, and returns a new *connected descriptor* for the connection.

:::

::: {#fig-sockets-interface-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.75cm]
\node[lab] at (0,0.8) {client}; \node[lab] at (6,0.8) {server};
\node[box] (ga1) at (0,0) {\texttt{getaddrinfo}};
\node[box] (s1) at (0,-1) {\texttt{socket}};
\node[box] (ga2) at (6,0) {\texttt{getaddrinfo}};
\node[box] (s2) at (6,-1) {\texttt{socket}};
\node[box] (b) at (6,-2) {\texttt{bind}};
\node[box] (l) at (6,-3) {\texttt{listen}};
\node[hl box] (c) at (0,-4) {\texttt{connect}};
\node[hl box] (a) at (6,-4) {\texttt{accept}};
\node[box] (w1) at (0,-5.2) {\texttt{write}}; \node[box] (r2) at (6,-5.2) {\texttt{read}};
\node[box] (r1) at (0,-6.4) {\texttt{read}}; \node[box] (w2) at (6,-6.4) {\texttt{write}};
\node[box] (cl1) at (0,-7.6) {\texttt{close}}; \node[box] (r3) at (6,-7.6) {\texttt{read} returns 0};
\node[box] (cl2) at (6,-8.8) {\texttt{close}};
\draw[->] (ga1) -- (s1); \draw[->] (s1) -- (c); \draw[->] (c) -- (w1); \draw[->] (w1) -- (r1); \draw[->] (r1) -- (cl1);
\draw[->] (ga2) -- (s2); \draw[->] (s2) -- (b); \draw[->] (b) -- (l); \draw[->] (l) -- (a); \draw[->] (a) -- (r2); \draw[->] (r2) -- (w2); \draw[->] (w2) -- (r3); \draw[->] (r3) -- (cl2);
\draw[->, dashed, draw=accent] (c) -- node[edge label, above] {connection request} (a);
\draw[->, draw=accent] (w1) -- node[edge label, above] {request} (r2);
\draw[->, draw=accent] (w2) -- node[edge label, above] {response} (r1);
\draw[->, dashed, draw=accent] (cl1) -- node[edge label, above] {EOF} (r3);
\draw[->] (cl2.east) -- ++(1.0,0) |- (a.east) node[pos=0.25, right, tick] {next client};
\draw[decorate, decoration={brace}] (-1.6,-7.9) -- (-1.6,-4.9) node[midway, left=3pt, tick] {session};
\end{tikzpicture}
\end{center}
```

The order of socket calls in a client and an iterative server. The dashed arrows are connection setup and teardown; after a session the server accepts the next client

:::

::: {#def-listening-connected .definition name="Listening and connected descriptors"}

A server uses two kinds of descriptors. The *listening descriptor* is created once and exists for the lifetime of the server; it is only an endpoint for connection requests. Each `accept` returns a fresh *connected descriptor*, the server's endpoint of one connection with one client; it is closed when that client has been served. Keeping them apart lets a server serve many clients at once: it can hand each connected descriptor to a separate process or thread while it keeps accepting on the listening descriptor (@sec-cs-concurrency-concurrent-servers).

:::

::: {#fig-sockets-interface-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r/\t in {0/{1. server blocks in \texttt{accept}, waiting on \texttt{listenfd}},1/{2. client calls \texttt{connect}: a request arrives at \texttt{listenfd}},2/{3. \texttt{accept} returns \texttt{connfd}; client and server exchange data}} {
  \begin{scope}[yshift=-\r*2.0cm]
  \node[tick, anchor=west] at (-0.6,0.9) {\t};
  \node[box] (c) at (0.4,0) {client};
  \node[box] (s) at (5.8,0) {server};
  \node[dot] at (1.4,0) {}; \node[tick, anchor=west] at (1.3,-0.3) {\texttt{clientfd}};
  \node[hl dot] at (4.6,0.2) {}; \node[tick] at (4.6,0.5) {\texttt{listenfd(3)}};
  \end{scope}
}
\draw[->, dashed, draw=accent] (1.5,-2.0) -- (4.5,-1.82);
\node[dot] at (4.6,-4.25) {}; \node[tick] at (4.6,-4.55) {\texttt{connfd(4)}};
\draw[<->, emph, draw=accent] (1.5,-4.0) -- (4.5,-4.22);
\end{tikzpicture}
\end{center}
```

`accept` in three steps: the listening descriptor (shaded) only receives connection requests; data flows through the new connected descriptor

:::

::: {#def-getaddrinfo .definition name="`getaddrinfo` and `getnameinfo`"}

`getaddrinfo(host, service, hints, &result)` converts a host name or dotted-decimal address and a service name or port number into socket address structures. It returns, in `result`, a linked list of `struct addrinfo` records, one for each address and socket type that match; each record holds the arguments for `socket` (`ai_family`, `ai_socktype`, `ai_protocol`) and a pointer `ai_addr` to a socket address ready for `connect` or `bind`. `hints` restricts the list, for example to connection sockets or to numeric ports, and asks for a listening address (`AI_PASSIVE`). The list is freed with `freeaddrinfo`. The inverse, `getnameinfo`, turns a socket address into host and service strings. Both are reentrant and independent of the protocol version, so the same code serves IPv4 and IPv6.

:::

::: {#fig-sockets-interface-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (-0.3,0) {\texttt{result}};
\foreach \i/\x in {1/1.4,2/4.6,3/7.8} {
  \draw[box] (\x,-0.6) rectangle (\x+2.4,0.6);
  \node[tick] at (\x+1.2,0.35) {\texttt{addrinfo}};
  \node[tick] at (\x+1.2,0.0) {\texttt{ai\_addr}};
  \node[tick] at (\x+1.2,-0.35) {\texttt{ai\_next}};
  \draw[hl cell] (\x+0.3,-2.2) rectangle (\x+2.1,-1.4); \node[tick] at (\x+1.2,-1.8) {socket addr \i};
  \draw[->] (\x+1.2,-0.6) -- (\x+1.2,-1.4);
}
\draw[->] (0.3,0) -- (1.4,0);
\draw[->] (3.8,-0.35) -- (4.6,-0.35);
\draw[->] (7.0,-0.35) -- (7.8,-0.35);
\node[tick] at (10.8,-0.35) {\texttt{NULL}}; \draw[->] (10.2,-0.35) -- (10.4,-0.35);
\end{tikzpicture}
\end{center}
```

The list returned by `getaddrinfo`: a client tries each address in turn until a `socket` and `connect` succeed

:::

::: {#exm-open-clientfd .example name="A helper that connects to a server"}

```c
/* Connect to host:port; return a connected descriptor, or -1. */
int open_clientfd(const char *host, const char *port) {
    struct addrinfo hints = {0}, *list, *p;
    int fd = -1;
    hints.ai_socktype = SOCK_STREAM;                 /* a connection */
    hints.ai_flags = AI_NUMERICSERV | AI_ADDRCONFIG; /* numeric port */
    if (getaddrinfo(host, port, &hints, &list) != 0)
        return -1;
    for (p = list; p != NULL; p = p->ai_next) {
        fd = socket(p->ai_family, p->ai_socktype, p->ai_protocol);
        if (fd < 0)
            continue;                                /* try the next address */
        if (connect(fd, p->ai_addr, p->ai_addrlen) == 0)
            break;                                   /* success */
        close(fd);
        fd = -1;
    }
    freeaddrinfo(list);
    return fd;
}
```

The matching `open_listenfd(port)` asks for addresses with `AI_PASSIVE` (any local address), and for the first one that works calls `socket`, sets the option `SO_REUSEADDR` (so the server can restart at once on the same port), `bind` and `listen`.

:::

::: {#exm-echo-server .example name="An iterative echo server"}

```c
void echo(int connfd) {                     /* send each line back */
    char line[MAXLINE];
    ssize_t n;
    while ((n = read_line(connfd, line, MAXLINE)) > 0)
        writen(connfd, line, n);
}

int main(int argc, char **argv) {
    int listenfd = open_listenfd(argv[1]);
    for (;;) {
        struct sockaddr_storage client;     /* large enough for any address */
        socklen_t len = sizeof client;
        int connfd = accept(listenfd, (struct sockaddr *)&client, &len);
        echo(connfd);
        close(connfd);
    }
}
```

The server is *iterative*: it serves one client at a time, from `accept` until the client closes its end, which makes `read_line` return $0$ (EOF). A client is symmetric: `open_clientfd`, then a loop that reads a line from standard input, writes it to the socket and prints the line that comes back. A second client that connects meanwhile waits in `accept`'s queue until the first one finishes.

:::

::: {#fig-sockets-interface-5}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.8cm]
\node[lab] at (0,0.6) {client 1}; \node[lab] at (4,0.6) {server}; \node[lab] at (8,0.6) {client 2};
\draw[faint] (0,0.2) -- (0,-6.2); \draw[faint] (4,0.2) -- (4,-6.2); \draw[faint] (8,0.2) -- (8,-6.2);
\draw[->, draw=accent] (0,0) -- node[edge label, above] {connect} (4,-0.4);
\draw[->] (0,-1.0) -- node[edge label, above] {\texttt{hello}} (4,-1.4);
\draw[->] (4,-1.6) -- node[edge label, below] {\texttt{hello}} (0,-2.0);
\draw[->, dashed, draw=accent] (8,-1.2) -- node[edge label, above] {connect: waits} (4.1,-1.6);
\draw[hl] (8,-1.2) -- (8,-4.4);
\draw[->] (0,-3.0) -- node[edge label, above] {close (EOF)} (4,-3.4);
\draw[->] (4,-4.4) -- node[edge label, above] {accepted} (8,-4.4);
\draw[->] (8,-5.2) -- node[edge label, above] {\texttt{bye}} (4,-5.6);
\draw[->] (4,-5.8) -- node[edge label, below] {\texttt{bye}} (8,-6.2);
\node[tick, anchor=west] at (8.1,-2.8) {blocked};
\end{tikzpicture}
\end{center}
```

An iterative echo server: client 2's connection request is queued until the server has finished with client 1

:::

::: {#rmk-sockets-interface-1 name="Testing servers with `telnet`"}

`telnet host port` opens a connection and copies lines between the terminal and the socket, so any server that speaks a text protocol can be tested by hand: type a line and see what comes back. The same works for a Web server, by typing an HTTP request (@sec-cs-systems-io-networking-http-and-web-servers). Tools such as `nc` (netcat) do the same.

:::
