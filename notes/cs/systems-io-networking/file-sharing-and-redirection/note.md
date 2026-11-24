---
title: "File Sharing and I/O Redirection"
sources: [cmu15213-16]
requires: [cs/systems-io-networking/unix-io, cs/exceptional-control-flow/process-control]
status: draft
---

<!-- Added 2026-11-24 from CMU 15-213 (Fall 2015), Lecture 16 "System-Level I/O" (file sharing, fork, I/O redirection and the descriptor puzzles in its extra slides), in our own wording; the examples and their file contents are our own. -->

A file can be open several times, in one process or in several. What the processes share, and what each has for itself, is fixed by three kernel tables; with them the behaviour of `fork`, of repeated `open` calls and of shell redirection follows directly.

::: {#def-descriptor-table .definition name="Descriptor table, open file table, v-node table"}

The kernel represents open files with three data structures:

- each process has its own *descriptor table*, indexed by descriptor number; entry $d$ points to an entry of the open file table (@def-file-descriptor);
- the *open file table* is shared by all processes; each entry holds a *file position* and a *reference count*, the number of descriptor entries that point to it;
- the *v-node table* is shared too; each entry holds the file's metadata (@def-file-metadata), one per file however often it is open.

`open` creates a new open file entry with reference count $1$. `close(d)` clears descriptor entry $d$ and decrements the count of its open file entry; the kernel frees the open file entry only when the count reaches $0$.

:::

::: {#fig-file-sharing-and-redirection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0.4,0.8) {descriptor table};
\node[tick] at (0.4,0.45) {(one per process)};
\foreach \d in {0,...,4} { \draw[cell frame] (0,-\d*0.55) rectangle (0.8,-\d*0.55-0.5); \node[tick, anchor=east] at (-0.1,-\d*0.55-0.25) {fd \d}; }
\node[lab] at (4.0,0.8) {open file table};
\node[tick] at (4.0,0.45) {(shared by all processes)};
\draw[box] (3.0,-0.2) rectangle (5.0,-1.4); \node[tick] at (4.0,-0.5) {file A}; \node[tick] at (4.0,-0.85) {position $k$}; \node[tick] at (4.0,-1.15) {refcnt $=1$};
\draw[box] (3.0,-1.8) rectangle (5.0,-3.0); \node[tick] at (4.0,-2.1) {file B}; \node[tick] at (4.0,-2.45) {position $k$}; \node[tick] at (4.0,-2.75) {refcnt $=1$};
\node[lab] at (7.6,0.8) {v-node table};
\node[tick] at (7.6,0.45) {(shared)};
\draw[regionB] (6.6,-0.2) rectangle (8.6,-1.4); \node[tick] at (7.6,-0.55) {access, size,}; \node[tick] at (7.6,-0.9) {type, \dots};
\draw[regionB] (6.6,-1.8) rectangle (8.6,-3.0); \node[tick] at (7.6,-2.15) {access, size,}; \node[tick] at (7.6,-2.5) {type, \dots};
\draw[->] (0.4,-0.8) -- (3.0,-0.8);
\draw[->] (0.4,-2.45) -- (3.0,-2.4);
\draw[->] (5.0,-0.8) -- (6.6,-0.8);
\draw[->] (5.0,-2.4) -- (6.6,-2.4);
\node[dot] at (0.4,-0.8) {}; \node[dot] at (0.4,-2.45) {};
\end{tikzpicture}
\end{center}
```

The three tables when descriptors $1$ and $4$ refer to two different files: each descriptor has its own open file entry and each file its own v-node

:::

::: {#exm-open-twice .example name="Opening the same file twice"}

Let `data.txt` contain `pqrstuvw`.

```c
char c1, c2;
int fd1 = open("data.txt", O_RDONLY);
int fd2 = open("data.txt", O_RDONLY);
read(fd1, &c1, 1);
read(fd1, &c1, 1);
read(fd2, &c2, 1);
printf("c1 = %c, c2 = %c\n", c1, c2);
```

Each `open` creates its own open file entry, so `fd1` and `fd2` have separate file positions that point to the same v-node. The two reads on `fd1` return `p` and then `q`; the read on `fd2` starts at its own position $0$. The program prints `c1 = q, c2 = p`.

:::

::: {#fig-file-sharing-and-redirection-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \d in {0,...,4} { \draw[cell frame] (0,-\d*0.55) rectangle (0.8,-\d*0.55-0.5); \node[tick, anchor=east] at (-0.1,-\d*0.55-0.25) {fd \d}; }
\draw[hl box] (3.0,-0.9) rectangle (5.0,-1.9); \node[tick] at (4.0,-1.2) {$k=2$}; \node[tick] at (4.0,-1.6) {refcnt $=1$};
\draw[hl box] (3.0,-2.2) rectangle (5.0,-3.2); \node[tick] at (4.0,-2.5) {$k=1$}; \node[tick] at (4.0,-2.9) {refcnt $=1$};
\draw[regionB] (6.6,-1.4) rectangle (8.6,-2.7); \node[tick] at (7.6,-2.05) {\texttt{data.txt}};
\node[dot] at (0.4,-1.9) {}; \node[dot] at (0.4,-2.45) {};
\draw[->] (0.4,-1.9) -- (3.0,-1.4); \node[tick, anchor=south] at (1.7,-1.6) {fd1};
\draw[->] (0.4,-2.45) -- (3.0,-2.7); \node[tick, anchor=north] at (1.7,-2.6) {fd2};
\draw[->] (5.0,-1.4) -- (6.6,-1.8);
\draw[->] (5.0,-2.7) -- (6.6,-2.3);
\node[lab] at (4.0,0.0) {open file table}; \node[lab] at (7.6,-0.8) {v-node};
\end{tikzpicture}
\end{center}
```

@exm-open-twice after the three reads: two open file entries with independent positions share one v-node

:::

::: {#prp-fork-shares-files .proposition name="A child shares its parent's open files"}

After `fork` (@def-fork), the child's descriptor table is a copy of the parent's, and each corresponding pair of descriptors points to the *same* open file entry, whose reference count has increased by one. Hence parent and child share every file position: a read or write by one moves the position seen by the other.

:::

::: {.proof}
1. `fork` gives the child a copy of the parent's context; the descriptor table is part of that context (@def-process), so entry $d$ of the child holds the same pointer as entry $d$ of the parent.

2. The open file table is not copied: it lives in the kernel and is shared by all processes, so both pointers reach one entry, and the kernel adds one to its reference count for the new descriptor.

3. The file position is stored in that one entry, not in the descriptor tables, so every `read`, `write` or `lseek` through either descriptor updates the position seen through the other.
:::

::: {#fig-file-sharing-and-redirection-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0.4,0.45) {parent};
\foreach \d in {0,...,3} { \draw[cell frame] (0,-\d*0.55) rectangle (0.8,-\d*0.55-0.5); \node[tick, anchor=east] at (-0.1,-\d*0.55-0.25) {fd \d}; }
\node[lab] at (0.4,-2.55) {child};
\foreach \d in {0,...,3} { \draw[cell frame] (0,-3.0-\d*0.55) rectangle (0.8,-3.0-\d*0.55-0.5); \node[tick, anchor=east] at (-0.1,-3.0-\d*0.55-0.25) {fd \d}; }
\draw[hl box] (3.2,-1.9) rectangle (5.4,-3.1); \node[tick] at (4.3,-2.2) {file position $k$}; \node[tick] at (4.3,-2.75) {refcnt $=2$};
\draw[regionB] (6.8,-1.9) rectangle (8.6,-3.1); \node[tick] at (7.7,-2.5) {v-node};
\node[dot] at (0.4,-1.9) {}; \node[dot] at (0.4,-4.9) {};
\draw[->] (0.4,-1.9) -- (3.2,-2.3);
\draw[->, draw=accent] (0.4,-4.9) -- (3.2,-2.8);
\draw[->] (5.4,-2.5) -- (6.8,-2.5);
\end{tikzpicture}
\end{center}
```

After `fork`: the child's descriptor $3$ points to the same open file entry as the parent's, so they share the file position, and the reference count is $2$

:::

::: {#exm-fork-read .example name="Reading after `fork`"}

With `data.txt` again containing `pqrstuvw`:

```c
char c;
int fd = open("data.txt", O_RDONLY);
read(fd, &c, 1);                     /* parent reads p */
if (fork() == 0) {
    read(fd, &c, 1);                 /* child */
    printf("child: %c\n", c);
    exit(0);
}
wait(NULL);
read(fd, &c, 1);                     /* parent, after the child has finished */
printf("parent: %c\n", c);
```

The child continues from the shared position $1$ and prints `child: q`. Because the parent waits for the child, the parent's second read starts at position $2$, so it prints `parent: r`. If the two processes did not share the position, both would read `q`.

:::

::: {#def-dup2 .definition name="`dup2` and I/O redirection"}

$$\texttt{dup2(oldfd, newfd)}$$
copies descriptor entry `oldfd` into entry `newfd`, first closing `newfd` if it is open. Afterwards both descriptors point to the same open file entry. A shell implements the *redirection* `ls > out.txt` by opening `out.txt` (say as descriptor $4$) in the child that will run `ls`, calling `dup2(4, 1)` so that standard output refers to the file, closing $4$, and then calling `execve` (@def-execve): `ls` writes to descriptor $1$ as usual, and the bytes go to the file.

:::

::: {#fig-file-sharing-and-redirection-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}
\node[lab] at (1.6,0.7) {before \texttt{dup2(4, 1)}};
\foreach \d in {0,...,4} { \draw[cell frame] (0,-\d*0.55) rectangle (0.8,-\d*0.55-0.5); \node[tick, anchor=east] at (-0.1,-\d*0.55-0.25) {fd \d}; }
\draw[box] (2.2,-0.3) rectangle (3.6,-1.1); \node[tick] at (2.9,-0.5) {terminal}; \node[tick] at (2.9,-0.85) {refcnt 1};
\draw[box] (2.2,-1.9) rectangle (3.6,-2.7); \node[tick] at (2.9,-2.1) {\texttt{out.txt}}; \node[tick] at (2.9,-2.45) {refcnt 1};
\node[dot] at (0.4,-0.8) {}; \node[dot] at (0.4,-2.45) {};
\draw[->] (0.4,-0.8) -- (2.2,-0.7);
\draw[->] (0.4,-2.45) -- (2.2,-2.3);
\end{scope}
\begin{scope}[xshift=6cm]
\node[lab] at (1.6,0.7) {after \texttt{dup2(4, 1)}};
\foreach \d in {0,...,4} { \draw[cell frame] (0,-\d*0.55) rectangle (0.8,-\d*0.55-0.5); \node[tick, anchor=east] at (-0.1,-\d*0.55-0.25) {fd \d}; }
\draw[box, draw=muted] (2.2,-0.3) rectangle (3.6,-1.1); \node[tick, text=muted] at (2.9,-0.5) {terminal}; \node[tick, text=muted] at (2.9,-0.85) {refcnt 0};
\draw[hl box] (2.2,-1.9) rectangle (3.6,-2.7); \node[tick] at (2.9,-2.1) {\texttt{out.txt}}; \node[tick] at (2.9,-2.45) {refcnt 2};
\node[dot] at (0.4,-0.8) {}; \node[dot] at (0.4,-2.45) {};
\draw[->, draw=accent, emph] (0.4,-0.8) -- (2.2,-2.1);
\draw[->] (0.4,-2.45) -- (2.2,-2.4);
\end{scope}
\end{tikzpicture}
\end{center}
```

Redirecting standard output: `dup2(4, 1)` makes descriptor $1$ point to the open file entry of `out.txt`; the terminal's entry loses its last reference (in this process), and `out.txt` now has two

:::

::: {#exm-shell-redirection .example name="A shell runs `ls > out.txt`"}

```c
pid_t pid = fork();
if (pid == 0) {                                   /* child */
    int fd = open("out.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    dup2(fd, STDOUT_FILENO);                      /* standard output -> out.txt */
    close(fd);                                    /* descriptor 1 keeps it open */
    execve("/bin/ls", argv, environ);
}
waitpid(pid, NULL, 0);                            /* the shell's own stdout is unchanged */
```

The redirection happens in the child after `fork` and before `execve`. The descriptor table survives `execve`, so `ls` starts with descriptor $1$ already pointing to the file, while the shell's own table is untouched.

:::

::: {#fig-file-sharing-and-redirection-5}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.5cm]
\node[box] (sh) at (0,0) {shell};
\node[box] (f) at (1.6,0) {\texttt{fork}};
\node[box] (o) at (3.2,0) {\texttt{open}};
\node[hl box] (d) at (4.8,0) {\texttt{dup2(fd,1)}};
\node[box] (c) at (6.4,0) {\texttt{close(fd)}};
\node[box] (e) at (8.0,0) {\texttt{execve ls}};
\draw[->] (sh) -- (f); \draw[->] (f) -- (o); \draw[->] (o) -- (d); \draw[->] (d) -- (c); \draw[->] (c) -- (e);
\draw[decorate, decoration={brace, mirror}] (2.7,-0.5) -- (8.6,-0.5) node[midway, below=3pt, tick] {in the child only};
\node[box] (w) at (1.6,-1.6) {parent: \texttt{waitpid}};
\draw[->] (f) -- (w);
\end{tikzpicture}
\end{center}
```

The order of the calls in a shell for `ls > out.txt`: the descriptor table is changed in the child between `fork` and `execve`

:::

::: {#exm-dup2-puzzle .example name="Reading through a duplicated descriptor"}

Again `data.txt` holds `pqrstuvw`:

```c
char c1, c2, c3;
int fd1 = open("data.txt", O_RDONLY);
int fd2 = open("data.txt", O_RDONLY);
read(fd2, &c1, 1);          /* fd2 at position 1 */
dup2(fd2, fd1);             /* fd1 now shares fd2's entry */
read(fd1, &c2, 1);
read(fd2, &c3, 1);
```

`c1 = p`. After `dup2`, `fd1` no longer refers to its own entry (still at position $0$, now closed) but to `fd2`'s entry at position $1$; so `c2 = q`, and the shared position moves to $2$, giving `c3 = r`.

:::

::: {#rmk-file-sharing-and-redirection-1 name="Standard I/O and `fork`"}

A stream buffer (@def-standard-io) is ordinary user memory, so `fork` copies it too. If a program calls `printf("x")` without a newline and then forks while its output goes to a file (fully buffered), both processes later flush their copy and the file receives `x` twice. Call `fflush(stdout)` before `fork` to avoid this.

:::
