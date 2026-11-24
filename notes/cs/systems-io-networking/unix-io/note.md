---
title: "Unix I/O"
sources: [cmu15213-16, cmu15213lab-7]
requires: [cs/exceptional-control-flow/exceptions]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 16 "System-Level I/O" (Unix I/O, robust reading, metadata, standard I/O) and the Proxy Lab handout (reading requests from a socket), in our own wording; code examples are our own. -->

*Input/output* (I/O) copies data between main memory and external devices: disks, terminals, networks. Every language runtime builds its I/O library (C's `printf`, Java's streams) on a small set of system calls (@def-system-call) that the kernel provides. Using them directly is necessary for network programming and helps explain the behaviour of the higher-level libraries.

::: {#def-unix-file .definition name="Unix file"}

A *Unix file* is a sequence of $m$ bytes
$$B_0,\ B_1,\ \dots,\ B_k,\ \dots,\ B_{m-1}.$$
All I/O devices are modelled as files, so one interface serves them all. Each file has a *type*:

- a *regular file* holds arbitrary data (a *text file* holds only ASCII or Unicode characters, every other file is *binary*; the kernel does not distinguish them);
- a *directory* holds an array of *links*, each mapping a file name to a file;
- a *socket* is used to communicate with a process on another machine (@def-socket-address).

Other types include named pipes, symbolic links, and character and block devices such as `/dev/tty` and `/dev/sda2`.

:::

::: {#fig-unix-io-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r) at (0,0) {\texttt{/}};
\foreach \n/\x/\l in {bin/-3.6/bin,dev/-1.8/dev,etc/0/etc,home/1.8/home,usr/3.6/usr} { \node[box] (\n) at (\x,-1.2) {\texttt{\l/}}; \draw[->] (r) -- (\n); }
\node[box] (bash) at (-3.6,-2.4) {\texttt{bash}};
\node[box] (tty) at (-1.8,-2.4) {\texttt{tty1}};
\node[box] (hosts) at (0,-2.4) {\texttt{hosts}};
\node[box] (al) at (1.8,-2.4) {\texttt{alice/}};
\node[box] (inc) at (3.6,-2.4) {\texttt{include/}};
\node[hl box] (hello) at (1.8,-3.6) {\texttt{hello.c}};
\node[box] (stdio) at (3.6,-3.6) {\texttt{stdio.h}};
\draw[->] (bin) -- (bash); \draw[->] (dev) -- (tty); \draw[->] (etc) -- (hosts); \draw[->] (home) -- (al); \draw[->] (usr) -- (inc); \draw[->] (al) -- (hello); \draw[->] (inc) -- (stdio);
\node[tick, anchor=north] at (-1.8,-2.75) {device file};
\node[tick, anchor=north] at (1.8,-3.95) {absolute path \texttt{/home/alice/hello.c}};
\end{tikzpicture}
\end{center}
```

The directory hierarchy: every file has an absolute path from the root `/`; a relative path such as `../alice/hello.c` starts at the process's current working directory instead. Devices appear as files too

:::

::: {#def-file-descriptor .definition name="File descriptor"}

A process asks the kernel to *open* a file with
$$\texttt{fd = open(filename, flags, mode)},$$
and the kernel returns a small nonnegative integer, the *descriptor*, which identifies the open file in all later calls; it is always the smallest descriptor not currently open in the process. Every process created by a shell starts with three open descriptors: $0$ standard input, $1$ standard output and $2$ standard error (`STDIN_FILENO`, `STDOUT_FILENO`, `STDERR_FILENO`). For each open file the kernel keeps a *file position* $k$, initially $0$, the byte offset where the next read or write starts. `close(fd)` tells the kernel the process is finished with the file.

:::

::: {#fig-unix-io-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-0.4,-3.2) rectangle (2.0,0.6); \node[lab] at (0.8,0.85) {process};
\foreach \d/\n in {0/{stdin},1/{stdout},2/{stderr},3/{\texttt{fd = open(...)}}} {
  \draw[cell frame] (0,-\d*0.8) rectangle (0.6,-\d*0.8+0.5); \node[tick] at (0.3,-\d*0.8+0.25) {\d};
}
\draw[hl cell] (0,-2.4) rectangle (0.6,-1.9); \node[tick] at (0.3,-2.15) {3};
\node[box] (t) at (5.0,-0.4) {terminal \texttt{/dev/tty1}};
\node[hl box] (f) at (5.0,-2.15) {regular file \texttt{data.txt}};
\draw[->] (0.65,0.25) -- (t.west); \draw[->] (0.65,-0.55) -- (t.west); \draw[->] (0.65,-1.35) -- (t.west);
\draw[->, draw=accent, emph] (0.65,-2.15) -- (f.west);
\node[tick] at (5.0,-2.75) {file position $k$};
\end{tikzpicture}
\end{center}
```

A process started from a shell: descriptors $0$, $1$, $2$ refer to the terminal, and the first `open` returns $3$, the smallest unused descriptor

:::

::: {#def-unix-read-write .definition name="Reading and writing"}

- `n = read(fd, buf, size)` copies at most `size` bytes, starting at the current file position $k$, into memory at `buf`, and advances $k$ by the number $n$ copied. It returns $n>0$, or $0$ when $k$ is already at the end of the file (*end of file*, EOF), or $-1$ on an error.
- `n = write(fd, buf, size)` copies at most `size` bytes from `buf` to the file, starting at position $k$, and advances $k$. It returns the number written, or $-1$.
- `lseek(fd, offset, whence)` sets $k$ explicitly (not possible on sockets and terminals).

There is no "EOF character": end of file is the condition $k\ge m$, which `read` reports by returning $0$.

:::

::: {#fig-unix-io-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm]
\foreach \i/\c in {0/H,1/e,2/l,3/l,4/o,5/{\textbackslash n},6/b,7/y,8/e,9/{\textbackslash n}} { \draw[cell frame] (\i,0) rectangle (\i+1,0.55); \node[tick] at (\i+0.5,0.27) {\texttt{\c}}; \node[tick] at (\i+0.5,-0.25) {\i}; }
\path[tintA] (0,0) rectangle (4,0.55);
\path[tintB] (4,0) rectangle (8,0.55);
\path[tintC] (8,0) rectangle (10,0.55);
\foreach \i/\c in {0/H,1/e,2/l,3/l,4/o,5/{\textbackslash n},6/b,7/y,8/e,9/{\textbackslash n}} { \node[tick] at (\i+0.5,0.27) {\texttt{\c}}; }
\draw[->, draw=accent] (0,1.4) -- (0,0.6); \node[tick] at (0,1.6) {$k=0$};
\draw[->, draw=accent] (4,1.4) -- (4,0.6); \node[tick] at (4,1.6) {$k=4$};
\draw[->, draw=accent] (8,1.4) -- (8,0.6); \node[tick] at (8,1.6) {$k=8$};
\draw[->, draw=accent] (10,1.4) -- (10,0.6); \node[tick] at (10,1.6) {$k=m=10$};
\node[lab, anchor=west] at (11,1.0) {\texttt{read(fd, buf, 4)}:};
\node[tick, anchor=west] at (11,0.5) {returns 4, 4, 2, then 0 (EOF)};
\end{tikzpicture}
\end{center}
```

Four calls `read(fd, buf, 4)` on a 10-byte file: each advances the file position by the number of bytes read; the third returns a short count of $2$ and the fourth returns $0$

:::

::: {#exm-copy-stdin .example name="Copying standard input, one byte at a time"}

```c
#include <unistd.h>

int main(void) {
    char c;
    while (read(STDIN_FILENO, &c, 1) == 1)   /* 0 at EOF, -1 on error */
        write(STDOUT_FILENO, &c, 1);
    return 0;
}
```

The program is correct but makes two system calls per byte. Each costs a trap into the kernel (@def-exception-classes), thousands of cycles, so copying a megabyte this way takes about two million traps; reading into a larger buffer cuts that by the buffer size.

:::

::: {#def-short-count .definition name="Short count"}

A `read` or `write` that transfers fewer bytes than requested returns a *short count*. Short counts are not errors. They happen

- at end of file, on any file;
- when reading text lines from a terminal (each `read` returns at most one line);
- when reading or writing pipes and network sockets, where the bytes arrive in pieces as the other side sends them.

On a disk file a `read` returns a short count only at end of file, and a `write` never does.

:::

::: {#fig-unix-io-4}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm]
\draw[->] (0,-2.6) -- (10,-2.6) node[lab, right] {time};
\node[lab, anchor=east] at (-0.2,1.3) {sender};
\node[lab, anchor=east] at (-0.2,-1.3) {receiver};
\draw[emph] (0.5,1.3) -- (9.5,1.3); \draw[emph] (0.5,-1.3) -- (9.5,-1.3);
\draw[hl box] (1,1.05) rectangle (4,1.55); \node[tick] at (2.5,1.3) {packet 1: 40 bytes};
\draw[box] (6,1.05) rectangle (9,1.55); \node[tick] at (7.5,1.3) {packet 2: 60 bytes};
\draw[->, draw=accent] (4,1.0) -- (4.6,-1.0);
\draw[->] (9,1.0) -- (9.4,-1.0);
\node[dot] at (4.6,-1.3) {}; \node[tick, anchor=north] at (4.6,-1.45) {\texttt{read(fd,buf,100)} returns 40};
\node[dot] at (9.4,-1.3) {}; \node[tick, anchor=north] at (8.7,-1.9) {next \texttt{read(fd,buf+40,60)} returns 60};
\end{tikzpicture}
\end{center}
```

A short count on a socket: the receiver asks for $100$ bytes, but only the first packet has arrived, so `read` returns $40$ at once instead of waiting

:::

::: {#def-robust-read .definition name="Robust reading: read exactly $n$ bytes"}

To read $n$ bytes from a descriptor that may return short counts, call `read` in a loop until $n$ bytes have arrived or EOF is reached, and restart a call that was interrupted by a signal handler (it returns $-1$ with `errno == EINTR`, @def-signal-handler-guidelines):

```c
ssize_t readn(int fd, void *buf, size_t n) {
    size_t left = n;
    char *p = buf;
    while (left > 0) {
        ssize_t r = read(fd, p, left);
        if (r < 0) {
            if (errno == EINTR) continue;    /* interrupted: call read again */
            return -1;
        }
        if (r == 0) break;                   /* EOF */
        left -= r;
        p += r;
    }
    return n - left;                         /* n, or fewer only at EOF */
}
```

The matching `writen` loops in the same way until all $n$ bytes are written.

:::

::: {#prp-readn-correct .proposition name="What `readn` returns"}

`readn(fd, buf, n)` returns $n$ unless it meets end of file or an error first; in the first case it returns the number of bytes before EOF, in the second $-1$. On return the bytes read are stored at `buf` in order.

:::

::: {.proof}
1. Invariant at the top of the loop: the first $n-\mathit{left}$ bytes read are at `buf[0..n-left)` and `p == buf + (n - left)`. It holds initially with $\mathit{left}=n$.

2. A call returning $r>0$ appends $r\le\mathit{left}$ bytes at `p`; decreasing $\mathit{left}$ by $r$ and advancing `p` by $r$ restores the invariant.

3. A call interrupted by a signal transfers nothing and changes no variable, so the invariant still holds when it is repeated.

4. Each successful iteration decreases $\mathit{left}$ by at least $1$, so the loop ends: with $\mathit{left}=0$ (return $n$), at EOF (return the $n-\mathit{left}$ bytes stored), or on an error (return $-1$).
:::

::: {#def-buffered-reading .definition name="Buffered reading"}

To read text lines efficiently, a *read buffer* sits between the program and the descriptor. A buffer record holds the descriptor, an array of a few kilobytes, the number $c$ of unread bytes in it, and a pointer to the next unread byte. A request for bytes is served from the buffer; only when $c=0$ is the buffer refilled with one `read` call of the full buffer size. A function `readline(rp, usrbuf, maxlen)` copies bytes from the buffer up to and including the next newline, so a line costs one system call per buffer, not one per byte.

:::

::: {#fig-unix-io-5}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm]
\node[lab, anchor=east] at (-0.3,0.27) {file};
\foreach \i in {0,...,17} { \draw[cell frame] (\i,0) rectangle (\i+1,0.55); }
\path[tintA] (0,0) rectangle (5,0.55); \node[tick] at (2.5,-0.3) {already read};
\path[tintB] (5,0) rectangle (13,0.55); \node[tick] at (9,-0.3) {copied into the buffer};
\draw[->, draw=accent] (13,1.2) -- (13,0.6); \node[tick] at (13,1.4) {file position $k$};
\node[lab, anchor=east] at (-0.3,-1.73) {buffer};
\foreach \i in {0,...,7} { \draw[cell frame] (\i+5,-2) rectangle (\i+6,-1.45); }
\path[tintA] (5,-2) rectangle (8,-1.45);
\path[tintC] (8,-2) rectangle (13,-1.45);
\draw[->, draw=accent] (8,-2.7) -- (8,-2.05); \node[tick] at (8,-2.9) {next unread byte};
\draw[decorate, decoration={brace, mirror}] (8,-3.2) -- (13,-3.2) node[midway, below=2pt, tick] {$c=5$ unread};
\draw[map] (5,-0.6) -- (5,-1.4); \draw[map] (13,-0.6) -- (13,-1.4);
\end{tikzpicture}
\end{center}
```

A read buffer over a file: one `read` call copied $8$ bytes into the buffer; the program has used $3$ of them, and the next $5$ requests are served from memory without a system call

:::

::: {#def-file-metadata .definition name="File metadata"}

`stat(filename, &st)` and `fstat(fd, &st)` fill a `struct stat` with the *metadata* the kernel keeps about a file: among others its size in bytes `st_size`, its owner, its access times, and `st_mode`, which encodes the file type (tested with the macros `S_ISREG`, `S_ISDIR`, `S_ISSOCK`) and the permission bits (`S_IRUSR` and so on).

:::

::: {#def-standard-io .definition name="Standard I/O"}

The C standard library offers *streams*: a `FILE *` is a descriptor together with a buffer. `fopen`/`fclose`, `fread`/`fwrite`, `fgets`/`fputs`, `scanf`/`printf` work on streams; every program starts with `stdin`, `stdout` and `stderr`. Output to a terminal is *line buffered*: `printf` copies characters into the buffer, and the buffer is written with one `write` call when a newline is printed, when it is full, at `fflush`, or at `exit`. Output to a file is *fully buffered* (only when full), and `stderr` is unbuffered.

:::

::: {#fig-unix-io-6}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=west] at (0,2.4) {program};
\foreach \y/\s in {1.9/{printf("h")},1.4/{printf("e")},0.9/{printf("y")},0.4/{printf("\textbackslash n")}} { \node[tick, anchor=west] at (0,\y) {\texttt{\s}}; }
\node[lab] at (5.0,2.4) {\texttt{stdout} buffer};
\foreach \i/\c in {0/h,1/e,2/y,3/{\textbackslash n}} { \draw[cell frame] (3.8+\i*0.6,1.15) rectangle (4.4+\i*0.6,1.65); \node[tick] at (4.1+\i*0.6,1.4) {\texttt{\c}}; }
\foreach \y in {1.9,1.4,0.9,0.4} { \draw[->, faint] (2.3,\y) -- (3.7,1.4); }
\draw[->, draw=accent, emph] (5.0,1.1) -- (5.0,0.0) node[midway, right, tick] {one \texttt{write(1, buf, 4)}};
\node[box] at (5.0,-0.4) {terminal};
\end{tikzpicture}
\end{center}
```

Line buffering: four `printf` calls only copy bytes into the stream's buffer; the newline triggers a single `write` system call (visible with `strace`)

:::

::: {#fig-unix-io-7}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-4.2,1.2) rectangle (4.2,2.0); \node[lab] at (0,1.6) {C application program};
\draw[box] (-4.0,0.2) rectangle (-0.2,1.0); \node[tick] at (-2.1,0.6) {standard I/O (\texttt{printf}, \texttt{fgets})};
\draw[box] (0.2,0.2) rectangle (4.0,1.0); \node[tick] at (2.1,0.6) {robust I/O (\texttt{readn}, \texttt{readline})};
\draw[hl box] (-4.2,-0.8) rectangle (4.2,0.0); \node[tick] at (0,-0.4) {Unix I/O system calls: \texttt{open read write lseek stat close}};
\draw[regionC] (-4.2,-1.8) rectangle (4.2,-1.0); \node[lab] at (0,-1.4) {kernel and devices};
\end{tikzpicture}
\end{center}
```

The I/O libraries are layered on Unix I/O: both the standard library and a robust-I/O package call `read` and `write` underneath

:::

::: {#rmk-unix-io-1 name="Which I/O functions to use"}

Use standard I/O for disk and terminal files whenever possible, and Unix I/O in signal handlers (it is async-signal-safe, @def-async-signal-safe) and when performance matters most. Standard I/O is a poor fit for network sockets: its streams cannot read and write a socket in an interleaved way without careful flushing, so network programs read sockets with a robust buffered reader and write with a `writen` loop. Never mix two buffered libraries on one descriptor, and do not use line-oriented functions (`fgets`, `scanf`, `readline`, `strlen`) on binary data, which may contain zero bytes and no newlines.

:::
