---
title: "C Pointers, Arrays and Memory Management"
sources: [cmu15213r-cboot, cmu15213r-6]
requires: [cs/data-representation/byte-ordering]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), C Boot Camp and Recitation 6 (C review), in our own wording. -->

C exposes memory almost directly: a pointer is an address together with the type of what lives there. This note collects the rules the rest of the systems notes rely on.

::: {#def-c-pointer .definition name="Pointer, address-of, dereference"}

For an object `x` of type `T`, the expression `&x` is its address, of type `T *` (*pointer to `T`*). For a pointer `p` of type `T *`, `*p` is the object of type `T` stored at address `p`. The null pointer `NULL` points to no object; dereferencing it, or any pointer that does not point to a live object, is undefined behaviour.

:::

::: {#def-pointer-arithmetic .definition name="Pointer arithmetic"}

For `p` of type `T *` and an integer `i`, `p + i` is the address `p` $+\ i\cdot$`sizeof(T)`. For pointers `p`, `q` into the same array, `q - p` is the number of elements between them. Array indexing is defined by it: `a[i]` means `*(a + i)`.

:::

::: {#exm-pointer-scaling .example name="The same `+ 1` on different types"}

Suppose `int a1` lives at `0x100` and `long long a2` at `0x200`. Then `&a1 + 1` is `0x104` and `&a2 + 1` is `0x208`: the step is the size of the pointed-to type. Casting first changes the step: `(char *) &a2 + 1` is `0x201`. A macro written `#define NEXT(a) ((char *)(a + 1))` adds before it casts, so `NEXT(&a2)` is `0x208`, not the next byte.

:::

::: {#fig-c-pointers-and-memory-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,11} { \draw[cell frame] (\i*0.7,0) rectangle (\i*0.7+0.7,0.55); }
\foreach \i/\a in {0/0x200,4/0x204,8/0x208} { \node[tick] at (\i*0.7+0.35,-0.25) {\texttt{\a}}; }
\draw[regionA] (0.05,0.05) rectangle (5.55,0.5); \node[lab] at (2.8,0.275) {\texttt{long long a2}};
\draw[hl cell] (5.6,0) rectangle (6.3,0.55);
\draw[map] (0.35,1.3) -- (0.35,0.6); \node[lab, anchor=south] at (0.35,1.3) {\texttt{\&a2}};
\draw[map] (1.05,1.3) -- (1.05,0.6); \node[lab, anchor=south west] at (0.8,1.3) {\texttt{(char *)\&a2 + 1}};
\draw[map, draw=accent] (5.95,1.3) -- (5.95,0.6); \node[lab, anchor=south] at (5.95,1.3) {\texttt{\&a2 + 1}};
\end{tikzpicture}
\end{center}
```

Adding $1$ to a `long long *` moves 8 bytes; adding $1$ to a `char *` moves one byte

:::

::: {#def-array-decay .definition name="Arrays and strings"}

An array `T a[n]` is $n$ objects of type `T` at consecutive addresses. In most expressions the name `a` *decays* to a pointer `&a[0]`; the exceptions are `sizeof a` (which gives $n\cdot$`sizeof(T)`) and `&a`. A *string* is a `char` array whose contents end with the null byte `'\0'`; `strlen` counts the characters before it, so a copy needs `strlen(s) + 1` bytes.

:::

::: {#def-storage-duration .definition name="Stack and heap allocation"}

A local variable is allocated on the *stack* when its function is called and is freed automatically when the function returns. A block obtained from `malloc(n)` (uninitialised bytes) or `calloc(k, n)` (zeroed) lives on the *heap* until the program passes its address to `free`. The rules: free exactly what was allocated, exactly once; never use a block after freeing it; never return the address of a local variable.

:::

::: {#fig-c-pointers-and-memory-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,2.2) rectangle (3.2,3.4); \node[lab, lbl bold] at (1.6,3.65) {stack};
\draw[box] (0.3,2.4) rectangle (2.9,3.0); \node[lab] at (1.6,2.7) {\texttt{int *p}};
\draw[regionC] (0,0) rectangle (3.2,1.4); \node[lab, lbl bold] at (1.6,-0.3) {heap};
\draw[box] (0.3,0.4) rectangle (2.9,1.0); \node[lab] at (1.6,0.7) {\texttt{malloc(40)}};
\draw[map, draw=accent] (2.5,2.4) to[bend left=20] (2.5,1.0);
\node[lab, anchor=west] at (3.5,2.7) {freed when the function returns};
\node[lab, anchor=west] at (3.5,0.7) {freed only by \texttt{free(p)}};
\end{tikzpicture}
\end{center}
```

The pointer variable lives on the stack; the block it points to lives on the heap and outlives the function unless it is freed

:::

::: {#exm-c-memory-bugs .example name="Five classic mistakes"}

1. `char w[strlen(s)]; strcpy(w, s);` writes the terminating `'\0'` one byte past the end of `w`: the buffer needs `strlen(s) + 1` bytes.

2. With `typedef struct node *node_t;`, the call `malloc(sizeof(node_t))` allocates the size of a *pointer* (8 bytes), not of the structure; write `malloc(sizeof(struct node))` or `malloc(sizeof *p)`.

3. A function that fills a local array `char buf[n + 1]` and returns `buf` returns a dangling pointer: the array dies with the stack frame.

4. `int *a = malloc(100 * sizeof(int));` followed by reading `a[i]` before writing it reads uninitialised memory; use `calloc` or initialise first.

5. `#define GREATER(a, b) a > b` makes `GREATER(1, 0) + 1` expand to `1 > 0 + 1`, which is $0$. Parenthesise macro bodies and arguments, or use an `inline` function.

:::

::: {#def-struct-typedef .definition name="Structures and typedef"}

A `struct` groups named fields of possibly different types into one object; `s.f` selects a field of a structure and `p->f` abbreviates `(*p).f` for a pointer to one. `typedef T name;` introduces `name` as another name for the type `T`. How the fields are laid out in memory is described in @def-struct-layout.

:::

::: {#rmk-c-pointers-and-memory-1 name="Tools that catch these bugs"}

Compile with warnings (`-Wall -Werror`), run under a memory checker such as Valgrind, which reports reads of uninitialised memory, invalid reads and writes, double frees and leaks, and step through the program with a debugger (gdb) to watch values change. All of these are needed in the labs that follow.

:::
