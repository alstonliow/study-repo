---
title: "Dynamic Memory Allocation"
sources: [cmu15213-19, cmu15213lab-6]
requires: [cs/virtual-memory/linux-virtual-memory]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 19 "Dynamic Memory Allocation: Basic Concepts" and the Malloc Lab handout (its goals only), in our own wording; proofs written out in steps. -->

::: {#def-heap-allocator .definition name="Heap and dynamic memory allocator"}

The *heap* is an area of demand-zero memory (@def-memory-mapping) just above the data segment; the kernel keeps a pointer `brk` to its top, which `sbrk(n)` moves up by $n$ bytes. A *dynamic memory allocator* manages the heap as a collection of *blocks*, each either *allocated* (in use by the program) or *free*. An *explicit* allocator, such as C's `malloc` and `free`, requires the program to free its blocks; an *implicit* allocator, a *garbage collector*, frees blocks the program can no longer reach (@def-garbage-collector).

:::

::: {#def-malloc-api .definition name="The `malloc` interface"}

`void *malloc(size_t n)` returns a pointer to a block of at least $n$ bytes, *aligned* to $16$ bytes on x86-64 so that any type can be stored in it, or `NULL` (with `errno` set) if it fails. `void free(void *p)` returns the block at `p`, which must have come from `malloc`, `calloc` or `realloc` and not been freed already. `calloc` returns a zeroed block; `realloc(p, n)` changes the size of a block, moving it if necessary.

:::

::: {#fig-dynamic-memory-allocation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.15,0.25) {\texttt{p1 = malloc(4)}};
\draw[cell frame] (0.00,0.00) rectangle (0.45,0.50);
\draw[cell frame] (0.45,0.00) rectangle (0.90,0.50);
\draw[cell frame] (0.90,0.00) rectangle (1.35,0.50);
\draw[cell frame] (1.35,0.00) rectangle (1.80,0.50);
\draw[cell frame] (1.80,0.00) rectangle (2.25,0.50);
\draw[cell frame] (2.25,0.00) rectangle (2.70,0.50);
\draw[cell frame] (2.70,0.00) rectangle (3.15,0.50);
\draw[cell frame] (3.15,0.00) rectangle (3.60,0.50);
\draw[cell frame] (3.60,0.00) rectangle (4.05,0.50);
\draw[cell frame] (4.05,0.00) rectangle (4.50,0.50);
\draw[cell frame] (4.50,0.00) rectangle (4.95,0.50);
\draw[cell frame] (4.95,0.00) rectangle (5.40,0.50);
\draw[cell frame] (5.40,0.00) rectangle (5.85,0.50);
\draw[cell frame] (5.85,0.00) rectangle (6.30,0.50);
\draw[cell frame] (6.30,0.00) rectangle (6.75,0.50);
\draw[cell frame] (6.75,0.00) rectangle (7.20,0.50);
\draw[regionA] (0.00,0.03) rectangle (1.80,0.47); \node[tick] at (0.90,0.25) {\texttt{p1}};
\node[lab, anchor=east] at (-0.15,-0.55) {\texttt{p2 = malloc(5)}};
\draw[cell frame] (0.00,-0.80) rectangle (0.45,-0.30);
\draw[cell frame] (0.45,-0.80) rectangle (0.90,-0.30);
\draw[cell frame] (0.90,-0.80) rectangle (1.35,-0.30);
\draw[cell frame] (1.35,-0.80) rectangle (1.80,-0.30);
\draw[cell frame] (1.80,-0.80) rectangle (2.25,-0.30);
\draw[cell frame] (2.25,-0.80) rectangle (2.70,-0.30);
\draw[cell frame] (2.70,-0.80) rectangle (3.15,-0.30);
\draw[cell frame] (3.15,-0.80) rectangle (3.60,-0.30);
\draw[cell frame] (3.60,-0.80) rectangle (4.05,-0.30);
\draw[cell frame] (4.05,-0.80) rectangle (4.50,-0.30);
\draw[cell frame] (4.50,-0.80) rectangle (4.95,-0.30);
\draw[cell frame] (4.95,-0.80) rectangle (5.40,-0.30);
\draw[cell frame] (5.40,-0.80) rectangle (5.85,-0.30);
\draw[cell frame] (5.85,-0.80) rectangle (6.30,-0.30);
\draw[cell frame] (6.30,-0.80) rectangle (6.75,-0.30);
\draw[cell frame] (6.75,-0.80) rectangle (7.20,-0.30);
\draw[regionA] (0.00,-0.77) rectangle (1.80,-0.33); \node[tick] at (0.90,-0.55) {\texttt{p1}};
\draw[regionA] (1.80,-0.77) rectangle (4.50,-0.33); \node[tick] at (3.15,-0.55) {\texttt{p2}};
\draw[hl cell] (4.05,-0.80) rectangle (4.50,-0.30); \node[tick, anchor=west] at (7.3,-0.55) {padding word for alignment};
\node[lab, anchor=east] at (-0.15,-1.35) {\texttt{p3 = malloc(6)}};
\draw[cell frame] (0.00,-1.60) rectangle (0.45,-1.10);
\draw[cell frame] (0.45,-1.60) rectangle (0.90,-1.10);
\draw[cell frame] (0.90,-1.60) rectangle (1.35,-1.10);
\draw[cell frame] (1.35,-1.60) rectangle (1.80,-1.10);
\draw[cell frame] (1.80,-1.60) rectangle (2.25,-1.10);
\draw[cell frame] (2.25,-1.60) rectangle (2.70,-1.10);
\draw[cell frame] (2.70,-1.60) rectangle (3.15,-1.10);
\draw[cell frame] (3.15,-1.60) rectangle (3.60,-1.10);
\draw[cell frame] (3.60,-1.60) rectangle (4.05,-1.10);
\draw[cell frame] (4.05,-1.60) rectangle (4.50,-1.10);
\draw[cell frame] (4.50,-1.60) rectangle (4.95,-1.10);
\draw[cell frame] (4.95,-1.60) rectangle (5.40,-1.10);
\draw[cell frame] (5.40,-1.60) rectangle (5.85,-1.10);
\draw[cell frame] (5.85,-1.60) rectangle (6.30,-1.10);
\draw[cell frame] (6.30,-1.60) rectangle (6.75,-1.10);
\draw[cell frame] (6.75,-1.60) rectangle (7.20,-1.10);
\draw[regionA] (0.00,-1.57) rectangle (1.80,-1.13); \node[tick] at (0.90,-1.35) {\texttt{p1}};
\draw[regionA] (1.80,-1.57) rectangle (4.50,-1.13); \node[tick] at (3.15,-1.35) {\texttt{p2}};
\draw[regionA] (4.50,-1.57) rectangle (7.20,-1.13); \node[tick] at (5.85,-1.35) {\texttt{p3}};
\node[lab, anchor=east] at (-0.15,-2.15) {\texttt{free(p2)}};
\draw[cell frame] (0.00,-2.40) rectangle (0.45,-1.90);
\draw[cell frame] (0.45,-2.40) rectangle (0.90,-1.90);
\draw[cell frame] (0.90,-2.40) rectangle (1.35,-1.90);
\draw[cell frame] (1.35,-2.40) rectangle (1.80,-1.90);
\draw[cell frame] (1.80,-2.40) rectangle (2.25,-1.90);
\draw[cell frame] (2.25,-2.40) rectangle (2.70,-1.90);
\draw[cell frame] (2.70,-2.40) rectangle (3.15,-1.90);
\draw[cell frame] (3.15,-2.40) rectangle (3.60,-1.90);
\draw[cell frame] (3.60,-2.40) rectangle (4.05,-1.90);
\draw[cell frame] (4.05,-2.40) rectangle (4.50,-1.90);
\draw[cell frame] (4.50,-2.40) rectangle (4.95,-1.90);
\draw[cell frame] (4.95,-2.40) rectangle (5.40,-1.90);
\draw[cell frame] (5.40,-2.40) rectangle (5.85,-1.90);
\draw[cell frame] (5.85,-2.40) rectangle (6.30,-1.90);
\draw[cell frame] (6.30,-2.40) rectangle (6.75,-1.90);
\draw[cell frame] (6.75,-2.40) rectangle (7.20,-1.90);
\draw[regionA] (0.00,-2.37) rectangle (1.80,-1.93); \node[tick] at (0.90,-2.15) {\texttt{p1}};
\draw[regionA] (4.50,-2.37) rectangle (7.20,-1.93); \node[tick] at (5.85,-2.15) {\texttt{p3}};
\node[lab, anchor=east] at (-0.15,-2.95) {\texttt{p4 = malloc(2)}};
\draw[cell frame] (0.00,-3.20) rectangle (0.45,-2.70);
\draw[cell frame] (0.45,-3.20) rectangle (0.90,-2.70);
\draw[cell frame] (0.90,-3.20) rectangle (1.35,-2.70);
\draw[cell frame] (1.35,-3.20) rectangle (1.80,-2.70);
\draw[cell frame] (1.80,-3.20) rectangle (2.25,-2.70);
\draw[cell frame] (2.25,-3.20) rectangle (2.70,-2.70);
\draw[cell frame] (2.70,-3.20) rectangle (3.15,-2.70);
\draw[cell frame] (3.15,-3.20) rectangle (3.60,-2.70);
\draw[cell frame] (3.60,-3.20) rectangle (4.05,-2.70);
\draw[cell frame] (4.05,-3.20) rectangle (4.50,-2.70);
\draw[cell frame] (4.50,-3.20) rectangle (4.95,-2.70);
\draw[cell frame] (4.95,-3.20) rectangle (5.40,-2.70);
\draw[cell frame] (5.40,-3.20) rectangle (5.85,-2.70);
\draw[cell frame] (5.85,-3.20) rectangle (6.30,-2.70);
\draw[cell frame] (6.30,-3.20) rectangle (6.75,-2.70);
\draw[cell frame] (6.75,-3.20) rectangle (7.20,-2.70);
\draw[regionA] (0.00,-3.17) rectangle (1.80,-2.73); \node[tick] at (0.90,-2.95) {\texttt{p1}};
\draw[regionA] (1.80,-3.17) rectangle (2.70,-2.73); \node[tick] at (2.25,-2.95) {\texttt{p4}};
\draw[regionA] (4.50,-3.17) rectangle (7.20,-2.73); \node[tick] at (5.85,-2.95) {\texttt{p3}};
\end{tikzpicture}
\end{center}
```

A sequence of requests on a heap of 16 words with double-word alignment: `p2` gets 6 words for 5 requested, and `p4` reuses part of the block freed by `p2`

:::

::: {#def-allocator-constraints .definition name="Constraints on an allocator"}

An allocator must handle arbitrary sequences of `malloc` and `free` requests; must respond immediately, without reordering or buffering requests; may use only the heap itself to store its bookkeeping; must align blocks; and may not move or modify allocated blocks.

:::

::: {#def-throughput-utilization .definition name="Throughput and peak memory utilization"}

For a sequence of requests $R_0,\dots,R_{n-1}$, *throughput* is the number of requests completed per unit of time. After request $R_k$, let the *aggregate payload* $P_k$ be the sum of the payloads of the currently allocated blocks and $H_k$ the current heap size (nondecreasing). The *peak utilization* after $k+1$ requests is
$$U_k=\frac{\max_{i\le k}P_i}{H_k}.$$
A good allocator has high throughput and high peak utilization; the two goals conflict.

:::

::: {#def-fragmentation .definition name="Internal and external fragmentation"}

*Internal fragmentation* is space inside an allocated block that is not payload: headers, padding for alignment, or space left because the policy gave a larger block than requested. *External fragmentation* occurs when the free memory in total would satisfy a request, but no single free block is large enough.

:::

::: {#fig-dynamic-memory-allocation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \k in {0,...,11} { \draw[cell frame] (\k*0.6,0) rectangle (\k*0.6+0.6,0.55); }
\path[tintA] (0,0) rectangle (2.4,0.55); \path[tintA] (3.6,0) rectangle (5.4,0.55);
\draw[regionC] (2.4,0.02) rectangle (3.6,0.53); \node[tick] at (3.0,0.275) {free};
\draw[regionC] (5.4,0.02) rectangle (7.2,0.53); \node[tick] at (6.3,0.275) {free};
\node[tick] at (1.2,0.275) {allocated}; \node[tick] at (4.5,0.275) {allocated};
\draw[hl cell] (1.8,0) rectangle (2.4,0.55); \node[tick] at (2.1,-0.25) {padding};
\node[tick, anchor=west] at (7.4,0.275) {\texttt{malloc(4 words)} fails: 5 words free, largest hole 3};
\end{tikzpicture}
\end{center}
```

Internal fragmentation (the shaded padding inside an allocated block) and external fragmentation (free space split into holes too small for the request)

:::

::: {#prp-external-fragmentation-unpredictable .proposition name="External fragmentation depends on the future"}

No allocator that satisfies the constraints of @def-allocator-constraints can avoid external fragmentation for every request sequence.

:::

::: {.proof}
1. Consider requests that allocate $2m$ blocks of one word each, filling the heap, and then free every second block.

2. Allocated blocks cannot be moved, so $m$ free words now lie in $m$ separate holes of one word each, whatever placement was chosen.

3. A following request for two words cannot be placed in any hole, although $m\ge2$ words are free: the heap must grow. Since the allocator must answer each request at once, it cannot know that a two-word request will come.
:::

::: {#def-allocator-design-issues .definition name="Design questions of an allocator"}

Every allocator must answer: how does `free` know the size of the block it is given (a *header* word before the payload stores it)? How are free blocks kept track of (@def-implicit-free-list, @def-explicit-free-list, @def-segregated-free-lists)? Which free block is chosen for a request (*placement*)? What happens to the rest of a block larger than needed (*splitting*)? And what happens to a newly freed block next to other free blocks (*coalescing*)?

:::
