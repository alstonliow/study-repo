---
title: "Common Memory-Related Bugs in C"
sources: [cmu15213-20, cmu15213r-6]
requires: [cs/virtual-memory/dynamic-memory-allocation]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 20 "Dynamic Memory Allocation: Advanced Concepts", memory-related perils part, and Recitation 6, in our own wording; the code examples are our own. -->

Memory bugs in C are hard to find because the effect often appears far from the cause, in time and in code. This note lists the common kinds; @exm-c-memory-bugs gave some first examples.

::: {#def-c-declarations .definition name="Reading C declarations"}

In a declaration, the postfix operators `[]` (array of) and `()` (function returning) bind tighter than the prefix `*` (pointer to). Read from the name outward, postfix first, then prefix, using parentheses to change the order:

| declaration | meaning |
|---|---|
| `int *p` | pointer to `int` |
| `int *p[13]` | array of 13 pointers to `int` |
| `int (*p)[13]` | pointer to an array of 13 `int`s |
| `int *f()` | function returning a pointer to `int` |
| `int (*f)()` | pointer to a function returning `int` |
| `int (*(*f())[13])()` | function returning a pointer to an array of 13 pointers to functions returning `int` |

:::

::: {#fig-memory-bugs-6}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0,0.8) {\texttt{int *p[13]}}; \node[tick] at (0,0.3) {array of 13 pointers to int};
\node[lab] at (5,0.8) {\texttt{int (*p)[13]}}; \node[tick] at (5,0.3) {pointer to an array of 13 ints};
\foreach \i in {0,...,3} { \draw[cell frame] (-1+\i*0.5,-0.6) rectangle (-0.5+\i*0.5,-0.1); \draw[->] (-0.75+\i*0.5,-0.6) -- (-0.75+\i*0.5,-1.1); }
\draw[cell frame] (4,-0.6) rectangle (4.5,-0.1); \draw[->] (4.25,-0.6) -- (4.25,-1.0);
\foreach \i in {0,...,5} { \draw[cell frame] (3.5+\i*0.4,-1.5) rectangle (3.9+\i*0.4,-1.05); }
\end{tikzpicture}
\end{center}
```

Two declarations that differ only by parentheses: `[]` binds tighter than `*`, so `int *p[13]` is an array of pointers, while `int (*p)[13]` is one pointer to an array

:::


::: {#exm-bad-pointer-deref .example name="Dereferencing bad pointers"}

```c
int val;
scanf("%d", val);      /* should be &val */
```

`scanf` expects an address and receives the integer's (uninitialised) value. If the value happens to be a valid writable address, some unrelated variable is silently overwritten; otherwise the program dies with a segmentation fault.

:::

::: {#fig-memory-bugs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionB] (0,0) rectangle (3,0.6); \node[tick] at (1.5,0.3) {low memory: code, data};
\node[box] (p) at (1.5,2.2) {\texttt{scanf("\%d", val)}};
\draw[->, draw=accent, emph] (p) -- (1.5,0.65) node[midway, right, tick] {writes to address \texttt{val}};
\node[tick, anchor=west] at (3.2,0.3) {a random location is overwritten, or a segmentation fault};
\end{tikzpicture}
\end{center}
```

Passing a value where a pointer is expected: `scanf` treats the integer `val` as an address and writes there

:::


::: {#exm-uninitialised-read .example name="Reading uninitialised heap memory"}

```c
/* y = A x, A is n x n */
int *matvec(int **A, int *x, int n) {
    int *y = malloc(n * sizeof(int));      /* not zeroed */
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            y[i] += A[i][j] * x[j];        /* adds to garbage */
    return y;
}
```

`malloc` does not clear the block, so `y[i]` starts with whatever bytes were there. Use `calloc`, or set `y[i] = 0` first.

:::

::: {#exm-overwriting-memory .example name="Overwriting memory"}

1. Allocating the wrong size: `int **p = malloc(n * sizeof(int));` allocates room for `int`s but stores pointers, which are twice as large on x86-64.

2. Off by one: `for (i = 0; i <= n; i++) p[i] = ...;` writes element $n$ of an $n$-element array.

3. Unbounded string input: `gets(s)` writes as many bytes as the line has (@def-buffer-overflow).

4. Misunderstood pointer arithmetic: in a search `while (*p && *p != val) p += sizeof(int);`, the step is already scaled by the type (@def-pointer-arithmetic), so `p` moves four elements at a time.

5. Precedence: `*size--` decrements the pointer `size`, not the value it points to; write `(*size)--`.

:::

::: {#fig-memory-bugs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0) rectangle (0.9,0.55); \node[tick] at (0.45,0.27) {\texttt{p[0]}};
\draw[cell frame] (0.9,0) rectangle (1.8,0.55); \node[tick] at (1.35,0.27) {\texttt{p[1]}};
\draw[cell frame] (1.8,0) rectangle (2.7,0.55); \node[tick] at (2.25,0.27) {\texttt{p[2]}};
\draw[cell frame] (2.7,0) rectangle (3.6,0.55); \node[tick] at (3.1500000000000004,0.27) {\texttt{p[3]}};
\draw[cell frame] (3.6,0) rectangle (4.5,0.55); \node[tick] at (4.05,0.27) {\texttt{p[4]}};
\draw[hl cell] (4.5,0) rectangle (5.4,0.55); \node[tick] at (4.95,0.27) {\texttt{p[5]}};
\node[tick, text=accent] at (4.95,-0.3) {one past the end};
\node[lab, anchor=west] at (5.6,0.27) {\texttt{for (i = 0; i <= n; i++)} with $n=5$};
\end{tikzpicture}
\end{center}
```

An off-by-one error: the loop condition `i <= n` writes one element past an array of `n` elements

:::


::: {#exm-dangling-pointers .example name="Pointers that outlive their object"}

1. Returning the address of a local variable: `int *f(void) { int val; return &val; }`. The frame is reused by the next call.

2. Freeing a block twice: `free(x); ... free(x);` corrupts the allocator's lists, which may later hand out the same block twice.

3. Using a block after freeing it: after `free(y)` the allocator may store its own pointers in the block (@def-explicit-free-list) or give it to another request; writing through `y` corrupts either.

:::

::: {#fig-memory-bugs-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (s) at (0,1.2) {stack frame of \texttt{f}};
\node[box] (x) at (0,0) {\texttt{int val}};
\node[box, dashed] (c) at (3.6,0.6) {after \texttt{f} returns};
\node[box] (q) at (7.2,0.6) {caller keeps \texttt{\&val}};
\draw[->, draw=accent] (q.west) to[out=180,in=0] (x.east);
\draw[->] (s) -- (c);
\end{tikzpicture}
\end{center}
```

Returning the address of a local variable: the pointer outlives the stack frame it points into, and later calls overwrite that memory

:::


::: {#fig-memory-bugs-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\path[tintA] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/1};
\node[tick] at (1.93,0.25) {\tiny 4/1};
\node[tick] at (1.10,0.75) {\texttt{x}};
\path[tintC] (2.20,0.00) rectangle (5.50,0.50);
\draw[hl] (2.20,0.00) rectangle (5.50,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\draw[faint] (3.30,0.00) -- (3.30,0.50);
\draw[faint] (3.85,0.00) -- (3.85,0.50);
\draw[faint] (4.40,0.00) -- (4.40,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\node[tick] at (2.48,0.25) {\tiny 6/0};
\node[tick] at (5.22,0.25) {\tiny 6/0};
\node[tick] at (3.85,0.75) {\texttt{freed y}};
\path[tintA] (5.50,0.00) rectangle (7.70,0.50);
\draw[emph] (5.50,0.00) rectangle (7.70,0.50);
\draw[faint] (6.05,0.00) -- (6.05,0.50);
\draw[faint] (6.60,0.00) -- (6.60,0.50);
\draw[faint] (7.15,0.00) -- (7.15,0.50);
\node[tick] at (5.78,0.25) {\tiny 4/1};
\node[tick] at (7.42,0.25) {\tiny 4/1};
\node[tick] at (6.60,0.75) {\texttt{z}};
\draw[->, draw=accent] (3.85,-0.6) -- (3.85,-0.05);
\node[tick, anchor=north] at (3.85,-0.6) {\texttt{*y = 0} after \texttt{free(y)}: corrupts the free list};
\end{tikzpicture}
\end{center}
```

Using freed memory: the allocator may already have reused the block, or stored its free-list pointers in it

:::


::: {#exm-memory-leak .example name="Memory leaks"}

```c
void process(int n) {
    int *x = malloc(n * sizeof(int));
    /* ... use x ... */
    return;                       /* x is never freed */
}
```

Each call leaves an unreachable block behind. Freeing only part of a structure (the head node of a list but not the rest) leaks the same way. Short programs survive leaks; servers that run for weeks do not.

:::

::: {#fig-memory-bugs-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\path[tintA] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/1};
\node[tick] at (1.93,0.25) {\tiny 4/1};
\path[tintA] (0.00,-0.60) rectangle (2.20,-0.10);
\draw[emph] (0.00,-0.60) rectangle (2.20,-0.10);
\draw[faint] (0.55,-0.60) -- (0.55,-0.10);
\draw[faint] (1.10,-0.60) -- (1.10,-0.10);
\draw[faint] (1.65,-0.60) -- (1.65,-0.10);
\node[tick] at (0.28,-0.35) {\tiny 4/1};
\node[tick] at (1.93,-0.35) {\tiny 4/1};
\path[tintA] (2.20,-0.60) rectangle (4.40,-0.10);
\draw[emph] (2.20,-0.60) rectangle (4.40,-0.10);
\draw[faint] (2.75,-0.60) -- (2.75,-0.10);
\draw[faint] (3.30,-0.60) -- (3.30,-0.10);
\draw[faint] (3.85,-0.60) -- (3.85,-0.10);
\node[tick] at (2.48,-0.35) {\tiny 4/1};
\node[tick] at (4.12,-0.35) {\tiny 4/1};
\path[tintA] (0.00,-1.20) rectangle (2.20,-0.70);
\draw[emph] (0.00,-1.20) rectangle (2.20,-0.70);
\draw[faint] (0.55,-1.20) -- (0.55,-0.70);
\draw[faint] (1.10,-1.20) -- (1.10,-0.70);
\draw[faint] (1.65,-1.20) -- (1.65,-0.70);
\node[tick] at (0.28,-0.95) {\tiny 4/1};
\node[tick] at (1.93,-0.95) {\tiny 4/1};
\path[tintA] (2.20,-1.20) rectangle (4.40,-0.70);
\draw[emph] (2.20,-1.20) rectangle (4.40,-0.70);
\draw[faint] (2.75,-1.20) -- (2.75,-0.70);
\draw[faint] (3.30,-1.20) -- (3.30,-0.70);
\draw[faint] (3.85,-1.20) -- (3.85,-0.70);
\node[tick] at (2.48,-0.95) {\tiny 4/1};
\node[tick] at (4.12,-0.95) {\tiny 4/1};
\path[tintA] (4.40,-1.20) rectangle (6.60,-0.70);
\draw[emph] (4.40,-1.20) rectangle (6.60,-0.70);
\draw[faint] (4.95,-1.20) -- (4.95,-0.70);
\draw[faint] (5.50,-1.20) -- (5.50,-0.70);
\draw[faint] (6.05,-1.20) -- (6.05,-0.70);
\node[tick] at (4.68,-0.95) {\tiny 4/1};
\node[tick] at (6.33,-0.95) {\tiny 4/1};
\path[tintA] (0.00,-1.80) rectangle (2.20,-1.30);
\draw[emph] (0.00,-1.80) rectangle (2.20,-1.30);
\draw[faint] (0.55,-1.80) -- (0.55,-1.30);
\draw[faint] (1.10,-1.80) -- (1.10,-1.30);
\draw[faint] (1.65,-1.80) -- (1.65,-1.30);
\node[tick] at (0.28,-1.55) {\tiny 4/1};
\node[tick] at (1.93,-1.55) {\tiny 4/1};
\path[tintA] (2.20,-1.80) rectangle (4.40,-1.30);
\draw[emph] (2.20,-1.80) rectangle (4.40,-1.30);
\draw[faint] (2.75,-1.80) -- (2.75,-1.30);
\draw[faint] (3.30,-1.80) -- (3.30,-1.30);
\draw[faint] (3.85,-1.80) -- (3.85,-1.30);
\node[tick] at (2.48,-1.55) {\tiny 4/1};
\node[tick] at (4.12,-1.55) {\tiny 4/1};
\path[tintA] (4.40,-1.80) rectangle (6.60,-1.30);
\draw[emph] (4.40,-1.80) rectangle (6.60,-1.30);
\draw[faint] (4.95,-1.80) -- (4.95,-1.30);
\draw[faint] (5.50,-1.80) -- (5.50,-1.30);
\draw[faint] (6.05,-1.80) -- (6.05,-1.30);
\node[tick] at (4.68,-1.55) {\tiny 4/1};
\node[tick] at (6.33,-1.55) {\tiny 4/1};
\path[tintA] (6.60,-1.80) rectangle (8.80,-1.30);
\draw[emph] (6.60,-1.80) rectangle (8.80,-1.30);
\draw[faint] (7.15,-1.80) -- (7.15,-1.30);
\draw[faint] (7.70,-1.80) -- (7.70,-1.30);
\draw[faint] (8.25,-1.80) -- (8.25,-1.30);
\node[tick] at (6.88,-1.55) {\tiny 4/1};
\node[tick] at (8.53,-1.55) {\tiny 4/1};
\path[tintA] (0.00,-2.40) rectangle (2.20,-1.90);
\draw[emph] (0.00,-2.40) rectangle (2.20,-1.90);
\draw[faint] (0.55,-2.40) -- (0.55,-1.90);
\draw[faint] (1.10,-2.40) -- (1.10,-1.90);
\draw[faint] (1.65,-2.40) -- (1.65,-1.90);
\node[tick] at (0.28,-2.15) {\tiny 4/1};
\node[tick] at (1.93,-2.15) {\tiny 4/1};
\path[tintA] (2.20,-2.40) rectangle (4.40,-1.90);
\draw[emph] (2.20,-2.40) rectangle (4.40,-1.90);
\draw[faint] (2.75,-2.40) -- (2.75,-1.90);
\draw[faint] (3.30,-2.40) -- (3.30,-1.90);
\draw[faint] (3.85,-2.40) -- (3.85,-1.90);
\node[tick] at (2.48,-2.15) {\tiny 4/1};
\node[tick] at (4.12,-2.15) {\tiny 4/1};
\path[tintA] (4.40,-2.40) rectangle (6.60,-1.90);
\draw[emph] (4.40,-2.40) rectangle (6.60,-1.90);
\draw[faint] (4.95,-2.40) -- (4.95,-1.90);
\draw[faint] (5.50,-2.40) -- (5.50,-1.90);
\draw[faint] (6.05,-2.40) -- (6.05,-1.90);
\node[tick] at (4.68,-2.15) {\tiny 4/1};
\node[tick] at (6.33,-2.15) {\tiny 4/1};
\path[tintA] (6.60,-2.40) rectangle (8.80,-1.90);
\draw[emph] (6.60,-2.40) rectangle (8.80,-1.90);
\draw[faint] (7.15,-2.40) -- (7.15,-1.90);
\draw[faint] (7.70,-2.40) -- (7.70,-1.90);
\draw[faint] (8.25,-2.40) -- (8.25,-1.90);
\node[tick] at (6.88,-2.15) {\tiny 4/1};
\node[tick] at (8.53,-2.15) {\tiny 4/1};
\path[tintA] (8.80,-2.40) rectangle (11.00,-1.90);
\draw[emph] (8.80,-2.40) rectangle (11.00,-1.90);
\draw[faint] (9.35,-2.40) -- (9.35,-1.90);
\draw[faint] (9.90,-2.40) -- (9.90,-1.90);
\draw[faint] (10.45,-2.40) -- (10.45,-1.90);
\node[tick] at (9.08,-2.15) {\tiny 4/1};
\node[tick] at (10.72,-2.15) {\tiny 4/1};
\node[tick, anchor=west] at (11.3,-1.2) {each call allocates and never frees};
\end{tikzpicture}
\end{center}
```

A memory leak: a function that allocates on every call and loses the pointer makes the heap grow until the program runs out of memory

:::


::: {#rmk-memory-bugs-1 name="Finding memory bugs"}

A debugger (gdb) finds bad-pointer crashes at the point of the fault. A *heap consistency checker* walks the allocator's data structures and reports corruption (Malloc Lab asks for one). Valgrind runs the program in an instrumented virtual machine and reports, at the faulting instruction, reads of uninitialised memory, accesses outside allocated blocks, double frees and leaks. glibc's `malloc` also checks some of its invariants when the environment variable `MALLOC_CHECK_` is set.

:::
