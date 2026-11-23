---
title: "Garbage Collection"
sources: [cmu15213-20]
requires: [cs/virtual-memory/implicit-free-lists, cs/graph-algorithms/depth-first-search]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 20 "Dynamic Memory Allocation: Advanced Concepts", garbage collection part, in our own wording; proofs written out in steps. -->

::: {#def-garbage-collector .definition name="Garbage collector"}

A *garbage collector* is a dynamic memory allocator that frees, automatically, the allocated blocks that the program can no longer use. Programs written for it allocate but never call `free`. Languages such as Java, Python, Go and ML rely on garbage collection; for C there are *conservative* collectors (@def-conservative-collector).

:::

::: {#def-reachability-graph .definition name="Memory as a directed graph"}

View memory as a directed graph. Its *root nodes* are locations outside the heap that contain pointers into the heap: registers, variables on the stack, global variables. Its other nodes are the allocated heap blocks. There is an edge $p\to q$ if some word of $p$ points into block $q$. A block is *reachable* if there is a path from some root to it; unreachable blocks are *garbage*.

:::

::: {#prp-garbage-is-safe .proposition name="Unreachable blocks can never be used again"}

If a block is unreachable at some moment, the program can never again read or write it.

:::

::: {.proof}
1. A program can reach heap memory only through an address it holds, in a register, on the stack, in a global, or in a heap block it can itself reach.

2. If no path from a root leads to block $q$, no such address points into $q$, and new addresses inside $q$ cannot be made without one (C programs that hide pointers are the exception, discussed at the end of this note).

3. Instructions only copy or combine values the program already holds, so no later step creates a path to $q$.
:::

::: {#fig-garbage-collection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r1) at (0,2) {root};
\node[box] (r2) at (0,1) {root};
\node[box] (r3) at (0,0) {root};
\node[small vertex] (a) at (2,2) {a};
\node[small vertex] (b) at (3.6,2) {b};
\node[small vertex] (c) at (2,0.8) {c};
\node[small vertex] (d) at (3.6,0.8) {d};
\node[small vertex] (e) at (2,-0.4) {e};
\node[small vertex] (f) at (3.6,-0.4) {f};
\node[small vertex] (g) at (5.2,1.4) {g};
\draw[->] (r1) -- (a);
\draw[->] (a) -- (b);
\draw[->] (r2) -- (c);
\draw[->] (c) -- (a);
\draw[->] (d) -- (b);
\draw[->] (e) -- (f);
\draw[->] (f) -- (e);
\draw[->] (b) -- (g);
\node[tick, anchor=west] at (4.3,-0.4) {\texttt{d}, \texttt{e}, \texttt{f} unreachable};
\end{tikzpicture}
\end{center}
```

Memory as a graph: roots (registers, stack slots, globals) point into the heap. Blocks `a`, `b`, `c`, `g` are reachable from a root; `d`, `e`, `f` are garbage, even though `e` and `f` point to each other and `d` points to a live block

:::


::: {#def-mark-and-sweep .definition name="Mark-and-sweep collection"}

A *mark-and-sweep* collector, called when the allocator runs out of space, works in two phases using one *mark bit* in each block header:

1. *Mark*: from every root, run a depth-first search (@def-dfs) over the heap graph and set the mark bit of every block visited.
2. *Sweep*: scan all blocks in address order (for example along the implicit list); free every allocated block whose mark bit is clear, and clear the mark bit of every marked block.

:::

::: {#fig-garbage-collection-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r1) at (0,2) {root};
\node[box] (r2) at (0,1) {root};
\node[box] (r3) at (0,0) {root};
\node[small vertex, fill=accentLight, draw=accent] (a) at (2,2) {a};
\node[small vertex, fill=accentLight, draw=accent] (b) at (3.6,2) {b};
\node[small vertex, fill=accentLight, draw=accent] (c) at (2,0.8) {c};
\node[small vertex] (d) at (3.6,0.8) {d};
\node[small vertex] (e) at (2,-0.4) {e};
\node[small vertex] (f) at (3.6,-0.4) {f};
\node[small vertex, fill=accentLight, draw=accent] (g) at (5.2,1.4) {g};
\draw[->] (r1) -- (a);
\draw[->] (a) -- (b);
\draw[->] (r2) -- (c);
\draw[->] (c) -- (a);
\draw[->] (d) -- (b);
\draw[->] (e) -- (f);
\draw[->] (f) -- (e);
\draw[->] (b) -- (g);
\end{tikzpicture}
\end{center}
```

Mark phase: a depth-first search from every root sets the mark bit of each reachable block (terracotta)

:::


::: {#fig-garbage-collection-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r1) at (0,2) {root};
\node[box] (r2) at (0,1) {root};
\node[box] (r3) at (0,0) {root};
\node[small vertex, fill=accentLight, draw=accent] (a) at (2,2) {a};
\node[small vertex, fill=accentLight, draw=accent] (b) at (3.6,2) {b};
\node[small vertex, fill=accentLight, draw=accent] (c) at (2,0.8) {c};
\node[small vertex, dashed, fill=white] (d) at (3.6,0.8) {d};
\node[small vertex, dashed, fill=white] (e) at (2,-0.4) {e};
\node[small vertex, dashed, fill=white] (f) at (3.6,-0.4) {f};
\node[small vertex, fill=accentLight, draw=accent] (g) at (5.2,1.4) {g};
\draw[->] (r1) -- (a);
\draw[->] (a) -- (b);
\draw[->] (r2) -- (c);
\draw[->] (c) -- (a);
\draw[->] (d) -- (b);
\draw[->] (e) -- (f);
\draw[->] (f) -- (e);
\draw[->] (b) -- (g);
\end{tikzpicture}
\end{center}
```

Sweep phase: a pass over all blocks frees the unmarked ones (dashed) and clears the marks of the others for the next collection

:::


::: {#fig-garbage-collection-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,1.25) {before};
\path[tintA] (0.00,1.00) rectangle (2.20,1.50);
\draw[emph] (0.00,1.00) rectangle (2.20,1.50);
\draw[faint] (0.55,1.00) -- (0.55,1.50);
\draw[faint] (1.10,1.00) -- (1.10,1.50);
\draw[faint] (1.65,1.00) -- (1.65,1.50);
\node[tick] at (0.28,1.25) {\tiny 4/1};
\node[tick] at (1.93,1.25) {\tiny 4/1};
\node[tick] at (1.10,1.75) {\texttt{a}};
\path[tintA] (2.20,1.00) rectangle (4.40,1.50);
\draw[emph] (2.20,1.00) rectangle (4.40,1.50);
\draw[faint] (2.75,1.00) -- (2.75,1.50);
\draw[faint] (3.30,1.00) -- (3.30,1.50);
\draw[faint] (3.85,1.00) -- (3.85,1.50);
\node[tick] at (2.48,1.25) {\tiny 4/1};
\node[tick] at (4.12,1.25) {\tiny 4/1};
\node[tick] at (3.30,1.75) {\texttt{d}};
\path[tintA] (4.40,1.00) rectangle (7.70,1.50);
\draw[emph] (4.40,1.00) rectangle (7.70,1.50);
\draw[faint] (4.95,1.00) -- (4.95,1.50);
\draw[faint] (5.50,1.00) -- (5.50,1.50);
\draw[faint] (6.05,1.00) -- (6.05,1.50);
\draw[faint] (6.60,1.00) -- (6.60,1.50);
\draw[faint] (7.15,1.00) -- (7.15,1.50);
\node[tick] at (4.68,1.25) {\tiny 6/1};
\node[tick] at (7.43,1.25) {\tiny 6/1};
\node[tick] at (6.05,1.75) {\texttt{b}};
\path[tintA] (7.70,1.00) rectangle (9.90,1.50);
\draw[emph] (7.70,1.00) rectangle (9.90,1.50);
\draw[faint] (8.25,1.00) -- (8.25,1.50);
\draw[faint] (8.80,1.00) -- (8.80,1.50);
\draw[faint] (9.35,1.00) -- (9.35,1.50);
\node[tick] at (7.98,1.25) {\tiny 4/1};
\node[tick] at (9.63,1.25) {\tiny 4/1};
\node[tick] at (8.80,1.75) {\texttt{e}};
\path[tintA] (9.90,1.00) rectangle (13.20,1.50);
\draw[emph] (9.90,1.00) rectangle (13.20,1.50);
\draw[faint] (10.45,1.00) -- (10.45,1.50);
\draw[faint] (11.00,1.00) -- (11.00,1.50);
\draw[faint] (11.55,1.00) -- (11.55,1.50);
\draw[faint] (12.10,1.00) -- (12.10,1.50);
\draw[faint] (12.65,1.00) -- (12.65,1.50);
\node[tick] at (10.18,1.25) {\tiny 6/1};
\node[tick] at (12.93,1.25) {\tiny 6/1};
\node[tick] at (11.55,1.75) {\texttt{c}};
\node[lab, anchor=east] at (-0.2,0.25) {after sweep};
\path[tintA] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/1};
\node[tick] at (1.93,0.25) {\tiny 4/1};
\path[tintC] (2.20,0.00) rectangle (4.40,0.50);
\draw[hl] (2.20,0.00) rectangle (4.40,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\draw[faint] (3.30,0.00) -- (3.30,0.50);
\draw[faint] (3.85,0.00) -- (3.85,0.50);
\node[tick] at (2.48,0.25) {\tiny 4/0};
\node[tick] at (4.12,0.25) {\tiny 4/0};
\path[tintA] (4.40,0.00) rectangle (7.70,0.50);
\draw[emph] (4.40,0.00) rectangle (7.70,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\draw[faint] (5.50,0.00) -- (5.50,0.50);
\draw[faint] (6.05,0.00) -- (6.05,0.50);
\draw[faint] (6.60,0.00) -- (6.60,0.50);
\draw[faint] (7.15,0.00) -- (7.15,0.50);
\node[tick] at (4.68,0.25) {\tiny 6/1};
\node[tick] at (7.43,0.25) {\tiny 6/1};
\path[tintC] (7.70,0.00) rectangle (9.90,0.50);
\draw[hl] (7.70,0.00) rectangle (9.90,0.50);
\draw[faint] (8.25,0.00) -- (8.25,0.50);
\draw[faint] (8.80,0.00) -- (8.80,0.50);
\draw[faint] (9.35,0.00) -- (9.35,0.50);
\node[tick] at (7.98,0.25) {\tiny 4/0};
\node[tick] at (9.63,0.25) {\tiny 4/0};
\path[tintA] (9.90,0.00) rectangle (13.20,0.50);
\draw[emph] (9.90,0.00) rectangle (13.20,0.50);
\draw[faint] (10.45,0.00) -- (10.45,0.50);
\draw[faint] (11.00,0.00) -- (11.00,0.50);
\draw[faint] (11.55,0.00) -- (11.55,0.50);
\draw[faint] (12.10,0.00) -- (12.10,0.50);
\draw[faint] (12.65,0.00) -- (12.65,0.50);
\node[tick] at (10.18,0.25) {\tiny 6/1};
\node[tick] at (12.93,0.25) {\tiny 6/1};
\end{tikzpicture}
\end{center}
```

The same collection seen in the heap: the sweep walks the implicit list (@def-implicit-free-list) and frees the unmarked blocks `d` and `e`

:::


::: {#thm-mark-sweep-correct .theorem name="Mark and sweep frees exactly the garbage"}

After a mark-and-sweep collection, every reachable block is still allocated and every unreachable block has been freed.

:::

::: {.proof}
1. Depth-first search from a root visits exactly the nodes reachable from it (@thm-dfs); running it from every root marks exactly the blocks reachable from some root.

2. The sweep frees exactly the allocated blocks that are unmarked, which by step 1 are the unreachable ones.

3. The sweep also clears every mark, so the next collection starts from the same state.
:::

::: {#def-conservative-collector .definition name="Conservative collection for C"}

A C collector cannot tell pointers from integers, and a C pointer may point into the middle of a block. A *conservative* collector therefore treats every word that *could* be a pointer into the heap as one. To find the block that contains an arbitrary address, it keeps the allocated blocks in a balanced binary tree ordered by start address, using two extra words per header. It never frees a reachable block, but it may keep some garbage alive.

:::

::: {#fig-garbage-collection-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (6,0.5);
\path[tintA] (0.3,0) rectangle (1.5,0.5); \draw[emph] (0.3,0) rectangle (1.5,0.5); \node[tick] at (0.9,0.25) {b1};
\path[tintA] (1.8,0) rectangle (3.6,0.5); \draw[emph] (1.8,0) rectangle (3.6,0.5); \node[tick] at (2.7,0.25) {b2};
\path[tintA] (4.0,0) rectangle (5.4,0.5); \draw[emph] (4.0,0) rectangle (5.4,0.5); \node[tick] at (4.7,0.25) {b3};
\node[dot] at (2.6,-0.9) {}; \node[tick, anchor=north] at (2.6,-1.0) {a word that looks like a pointer};
\draw[->, draw=accent] (2.6,-0.85) -- (2.6,-0.05);
\node[tick, anchor=west] at (6.2,0.25) {balanced tree of block start addresses finds \texttt{b2}};
\end{tikzpicture}
\end{center}
```

Conservative collection in C: any word whose value falls inside a heap block (even into its middle) must be treated as a pointer to that block, so `b2` is kept alive

:::


::: {#rmk-garbage-collection-1 name="Why C needs conservatism"}

An integer whose value happens to equal an address inside a dead block keeps that block alive; that is the price of conservatism and only wastes space. The opposite error is impossible as long as the program stores pointers in ordinary words, but tricks that hide a pointer, for example storing `p ^ q` instead of `p`, defeat any collector. Other classical algorithms are reference counting (which fails on cycles such as `e` and `f` in the figure), copying collection, and generational collection, which collects young blocks more often because most blocks die young.

:::
