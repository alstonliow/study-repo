---
title: "Explicit and Segregated Free Lists"
sources: [cmu15213-20, cmu15213lab-6]
requires: [cs/virtual-memory/implicit-free-lists]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 20 "Dynamic Memory Allocation: Advanced Concepts", first part, and the Malloc Lab handout, in our own wording; proofs written out in steps. -->

An implicit list makes every allocation scan all blocks, allocated ones included (@sec-cs-virtual-memory-implicit-free-lists). Better allocators keep the free blocks in their own data structures.

::: {#def-explicit-free-list .definition name="Explicit free list"}

An *explicit free list* links the free blocks into a doubly linked list. Each free block stores, in the first two words of its payload area, a *successor* pointer and a *predecessor* pointer; allocated blocks need no pointers, so the payload is not reduced. Headers and footers stay as in @def-boundary-tags, so coalescing still finds the neighbours in memory. The minimum block now holds a header, two pointers and a footer.

:::

::: {#fig-explicit-and-segregated-lists-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,0) rectangle (3.0,0.5); \node[tick] at (1.5,0.25) {size};
\draw[hl cell] (3.0,0) rectangle (3.8,0.5); \node[tick] at (3.4,0.25) {a};
\draw[regionC] (0,-0.55) rectangle (3.8,-0.05); \node[tick] at (1.9,-0.3) {next (pointer)};
\draw[regionC] (0,-1.1) rectangle (3.8,-0.6); \node[tick] at (1.9,-0.85) {prev (pointer)};
\path[tintC] (0,-1.8) rectangle (3.8,-1.15); \draw[emph] (0,-1.8) rectangle (3.8,-1.15); \node[tick] at (1.9,-1.47) {unused};
\draw[hl cell] (0,-2.35) rectangle (3.0,-1.85); \node[tick] at (1.5,-2.1) {size};
\draw[hl cell] (3.0,-2.35) rectangle (3.8,-1.85); \node[tick] at (3.4,-2.1) {a};
\node[lab] at (1.9,0.8) {free block};
\draw[hl cell] (5.5,0) rectangle (8.5,0.5); \node[tick] at (7.0,0.25) {size};
\draw[hl cell] (8.5,0) rectangle (9.3,0.5); \node[tick] at (8.9,0.25) {a};
\path[tintA] (5.5,-1.8) rectangle (9.3,-0.05); \draw[emph] (5.5,-1.8) rectangle (9.3,-0.05); \node[tick] at (7.4,-0.9) {payload and padding};
\draw[hl cell] (5.5,-2.35) rectangle (8.5,-1.85); \node[tick] at (7.0,-2.1) {size};
\draw[hl cell] (8.5,-2.35) rectangle (9.3,-1.85); \node[tick] at (8.9,-2.1) {a};
\node[lab] at (7.4,0.8) {allocated block (unchanged)};
\end{tikzpicture}
\end{center}
```

Block format of an explicit free list: a free block uses the first two words of its payload area for the successor and predecessor pointers; allocated blocks look as before, so the pointers cost no space in them

:::


::: {#fig-explicit-and-segregated-lists-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\path[tintC] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/0};
\node[tick] at (1.93,0.25) {\tiny 4/0};
\path[tintA] (2.20,0.00) rectangle (5.50,0.50);
\draw[emph] (2.20,0.00) rectangle (5.50,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\draw[faint] (3.30,0.00) -- (3.30,0.50);
\draw[faint] (3.85,0.00) -- (3.85,0.50);
\draw[faint] (4.40,0.00) -- (4.40,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\node[tick] at (2.48,0.25) {\tiny 6/1};
\node[tick] at (5.22,0.25) {\tiny 6/1};
\path[tintC] (5.50,0.00) rectangle (7.70,0.50);
\draw[emph] (5.50,0.00) rectangle (7.70,0.50);
\draw[faint] (6.05,0.00) -- (6.05,0.50);
\draw[faint] (6.60,0.00) -- (6.60,0.50);
\draw[faint] (7.15,0.00) -- (7.15,0.50);
\node[tick] at (5.78,0.25) {\tiny 4/0};
\node[tick] at (7.42,0.25) {\tiny 4/0};
\path[tintA] (7.70,0.00) rectangle (9.90,0.50);
\draw[emph] (7.70,0.00) rectangle (9.90,0.50);
\draw[faint] (8.25,0.00) -- (8.25,0.50);
\draw[faint] (8.80,0.00) -- (8.80,0.50);
\draw[faint] (9.35,0.00) -- (9.35,0.50);
\node[tick] at (7.98,0.25) {\tiny 4/1};
\node[tick] at (9.62,0.25) {\tiny 4/1};
\path[tintC] (9.90,0.00) rectangle (13.20,0.50);
\draw[emph] (9.90,0.00) rectangle (13.20,0.50);
\draw[faint] (10.45,0.00) -- (10.45,0.50);
\draw[faint] (11.00,0.00) -- (11.00,0.50);
\draw[faint] (11.55,0.00) -- (11.55,0.50);
\draw[faint] (12.10,0.00) -- (12.10,0.50);
\draw[faint] (12.65,0.00) -- (12.65,0.50);
\node[tick] at (10.18,0.25) {\tiny 6/0};
\node[tick] at (12.93,0.25) {\tiny 6/0};
\node[box] (root) at (-1.4,0.25) {\texttt{root}};
\draw[->, draw=accent] (root.north) to[bend left=20] (11.55,0.55);
\draw[->, draw=accent] (11.55,0.55) to[bend left=25] (1.10,0.55);
\draw[->, draw=accent] (1.10,0.55) to[bend left=25] (6.60,0.55);
\end{tikzpicture}
\end{center}
```

An explicit free list threads only the free blocks together, in any order: here root $\to$ block 5 $\to$ block 1 $\to$ block 3. The order of the list need not match the order of the addresses

:::


::: {#def-free-list-ordering .definition name="Insertion policies"}

When a block is freed, it is inserted into the free list either

- *LIFO*: at the front of the list, in constant time; or
- *address-ordered*: so that the list order matches the order of addresses, which needs a search for the right place but has been observed to fragment less.

:::

::: {#prp-explicit-list-cost .proposition name="Cost of an explicit list"}

With first fit on an explicit list, allocation takes time linear in the number of *free* blocks, and freeing with the LIFO policy and boundary-tag coalescing takes constant time.

:::

::: {.proof}
1. The search visits only blocks on the free list, that is, free blocks.

2. Splitting a block replaces it in the list by its remainder (or removes it), a constant number of pointer updates.

3. Freeing finds both neighbours in memory through the boundary tags in constant time (@thm-constant-time-coalescing). Each free neighbour is unlinked from the list in constant time, because the list is doubly linked: its own predecessor and successor pointers say which two pointers to change.

4. The merged block is inserted at the front of the list, again a constant number of pointer updates.
:::

::: {#fig-explicit-and-segregated-lists-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,1.15) {before};
\path[tintA] (0.00,0.90) rectangle (1.65,1.40);
\draw[emph] (0.00,0.90) rectangle (1.65,1.40);
\draw[faint] (0.55,0.90) -- (0.55,1.40);
\draw[faint] (1.10,0.90) -- (1.10,1.40);
\node[tick] at (0.28,1.15) {\tiny 3/1};
\node[tick] at (1.38,1.15) {\tiny 3/1};
\path[tintA] (1.65,0.90) rectangle (3.85,1.40);
\draw[hl] (1.65,0.90) rectangle (3.85,1.40);
\draw[faint] (2.20,0.90) -- (2.20,1.40);
\draw[faint] (2.75,0.90) -- (2.75,1.40);
\draw[faint] (3.30,0.90) -- (3.30,1.40);
\node[tick] at (1.93,1.15) {\tiny 4/1};
\node[tick] at (3.58,1.15) {\tiny 4/1};
\path[tintA] (3.85,0.90) rectangle (5.50,1.40);
\draw[emph] (3.85,0.90) rectangle (5.50,1.40);
\draw[faint] (4.40,0.90) -- (4.40,1.40);
\draw[faint] (4.95,0.90) -- (4.95,1.40);
\node[tick] at (4.13,1.15) {\tiny 3/1};
\node[tick] at (5.23,1.15) {\tiny 3/1};
\node[lab, anchor=east] at (-0.2,0.25) {after};
\path[tintA] (0.00,0.00) rectangle (1.65,0.50);
\draw[emph] (0.00,0.00) rectangle (1.65,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\node[tick] at (0.28,0.25) {\tiny 3/1};
\node[tick] at (1.38,0.25) {\tiny 3/1};
\path[tintC] (1.65,0.00) rectangle (3.85,0.50);
\draw[emph] (1.65,0.00) rectangle (3.85,0.50);
\draw[faint] (2.20,0.00) -- (2.20,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\draw[faint] (3.30,0.00) -- (3.30,0.50);
\node[tick] at (1.93,0.25) {\tiny 4/0};
\node[tick] at (3.58,0.25) {\tiny 4/0};
\path[tintA] (3.85,0.00) rectangle (5.50,0.50);
\draw[emph] (3.85,0.00) rectangle (5.50,0.50);
\draw[faint] (4.40,0.00) -- (4.40,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\node[tick] at (4.13,0.25) {\tiny 3/1};
\node[tick] at (5.23,0.25) {\tiny 3/1};
\node[lab] at (2.75,1.75) {case 1: both neighbours allocated};
\node[box] (r) at (7.6,0.25) {\texttt{root}};
\draw[->, draw=accent] (r.west) to[out=180,in=60] (2.75,0.55);
\node[tick, anchor=west] at (6.9,-0.45) {insert the block at the front of the list};
\end{tikzpicture}
\end{center}
```

Freeing with the LIFO policy, case 1: both neighbours allocated: insert the block at the front of the list

:::


::: {#fig-explicit-and-segregated-lists-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,1.15) {before};
\path[tintA] (0.00,0.90) rectangle (1.65,1.40);
\draw[emph] (0.00,0.90) rectangle (1.65,1.40);
\draw[faint] (0.55,0.90) -- (0.55,1.40);
\draw[faint] (1.10,0.90) -- (1.10,1.40);
\node[tick] at (0.28,1.15) {\tiny 3/1};
\node[tick] at (1.38,1.15) {\tiny 3/1};
\path[tintA] (1.65,0.90) rectangle (3.85,1.40);
\draw[hl] (1.65,0.90) rectangle (3.85,1.40);
\draw[faint] (2.20,0.90) -- (2.20,1.40);
\draw[faint] (2.75,0.90) -- (2.75,1.40);
\draw[faint] (3.30,0.90) -- (3.30,1.40);
\node[tick] at (1.93,1.15) {\tiny 4/1};
\node[tick] at (3.58,1.15) {\tiny 4/1};
\path[tintC] (3.85,0.90) rectangle (5.50,1.40);
\draw[emph] (3.85,0.90) rectangle (5.50,1.40);
\draw[faint] (4.40,0.90) -- (4.40,1.40);
\draw[faint] (4.95,0.90) -- (4.95,1.40);
\node[tick] at (4.13,1.15) {\tiny 3/0};
\node[tick] at (5.23,1.15) {\tiny 3/0};
\node[lab, anchor=east] at (-0.2,0.25) {after};
\path[tintA] (0.00,0.00) rectangle (1.65,0.50);
\draw[emph] (0.00,0.00) rectangle (1.65,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\node[tick] at (0.28,0.25) {\tiny 3/1};
\node[tick] at (1.38,0.25) {\tiny 3/1};
\path[tintC] (1.65,0.00) rectangle (5.50,0.50);
\draw[emph] (1.65,0.00) rectangle (5.50,0.50);
\draw[faint] (2.20,0.00) -- (2.20,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\draw[faint] (3.30,0.00) -- (3.30,0.50);
\draw[faint] (3.85,0.00) -- (3.85,0.50);
\draw[faint] (4.40,0.00) -- (4.40,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\node[tick] at (1.93,0.25) {\tiny 7/0};
\node[tick] at (5.23,0.25) {\tiny 7/0};
\node[lab] at (2.75,1.75) {case 2: next block free};
\node[box] (r) at (7.6,0.25) {\texttt{root}};
\draw[->, draw=accent] (r.west) to[out=180,in=60] (3.58,0.55);
\node[tick, anchor=west] at (6.9,-0.45) {unlink the next block, merge, insert at the front};
\end{tikzpicture}
\end{center}
```

Freeing with the LIFO policy, case 2: next block free: unlink the next block, merge, insert at the front

:::


::: {#fig-explicit-and-segregated-lists-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,1.15) {before};
\path[tintC] (0.00,0.90) rectangle (1.65,1.40);
\draw[emph] (0.00,0.90) rectangle (1.65,1.40);
\draw[faint] (0.55,0.90) -- (0.55,1.40);
\draw[faint] (1.10,0.90) -- (1.10,1.40);
\node[tick] at (0.28,1.15) {\tiny 3/0};
\node[tick] at (1.38,1.15) {\tiny 3/0};
\path[tintA] (1.65,0.90) rectangle (3.85,1.40);
\draw[hl] (1.65,0.90) rectangle (3.85,1.40);
\draw[faint] (2.20,0.90) -- (2.20,1.40);
\draw[faint] (2.75,0.90) -- (2.75,1.40);
\draw[faint] (3.30,0.90) -- (3.30,1.40);
\node[tick] at (1.93,1.15) {\tiny 4/1};
\node[tick] at (3.58,1.15) {\tiny 4/1};
\path[tintA] (3.85,0.90) rectangle (5.50,1.40);
\draw[emph] (3.85,0.90) rectangle (5.50,1.40);
\draw[faint] (4.40,0.90) -- (4.40,1.40);
\draw[faint] (4.95,0.90) -- (4.95,1.40);
\node[tick] at (4.13,1.15) {\tiny 3/1};
\node[tick] at (5.23,1.15) {\tiny 3/1};
\node[lab, anchor=east] at (-0.2,0.25) {after};
\path[tintC] (0.00,0.00) rectangle (3.85,0.50);
\draw[emph] (0.00,0.00) rectangle (3.85,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\draw[faint] (2.20,0.00) -- (2.20,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\draw[faint] (3.30,0.00) -- (3.30,0.50);
\node[tick] at (0.28,0.25) {\tiny 7/0};
\node[tick] at (3.58,0.25) {\tiny 7/0};
\path[tintA] (3.85,0.00) rectangle (5.50,0.50);
\draw[emph] (3.85,0.00) rectangle (5.50,0.50);
\draw[faint] (4.40,0.00) -- (4.40,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\node[tick] at (4.13,0.25) {\tiny 3/1};
\node[tick] at (5.23,0.25) {\tiny 3/1};
\node[lab] at (2.75,1.75) {case 3: previous block free};
\node[box] (r) at (7.6,0.25) {\texttt{root}};
\draw[->, draw=accent] (r.west) to[out=180,in=60] (1.93,0.55);
\node[tick, anchor=west] at (6.9,-0.45) {unlink the previous block, merge, insert at the front};
\end{tikzpicture}
\end{center}
```

Freeing with the LIFO policy, case 3: previous block free: unlink the previous block, merge, insert at the front

:::


::: {#fig-explicit-and-segregated-lists-6}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,1.15) {before};
\path[tintC] (0.00,0.90) rectangle (1.65,1.40);
\draw[emph] (0.00,0.90) rectangle (1.65,1.40);
\draw[faint] (0.55,0.90) -- (0.55,1.40);
\draw[faint] (1.10,0.90) -- (1.10,1.40);
\node[tick] at (0.28,1.15) {\tiny 3/0};
\node[tick] at (1.38,1.15) {\tiny 3/0};
\path[tintA] (1.65,0.90) rectangle (3.85,1.40);
\draw[hl] (1.65,0.90) rectangle (3.85,1.40);
\draw[faint] (2.20,0.90) -- (2.20,1.40);
\draw[faint] (2.75,0.90) -- (2.75,1.40);
\draw[faint] (3.30,0.90) -- (3.30,1.40);
\node[tick] at (1.93,1.15) {\tiny 4/1};
\node[tick] at (3.58,1.15) {\tiny 4/1};
\path[tintC] (3.85,0.90) rectangle (5.50,1.40);
\draw[emph] (3.85,0.90) rectangle (5.50,1.40);
\draw[faint] (4.40,0.90) -- (4.40,1.40);
\draw[faint] (4.95,0.90) -- (4.95,1.40);
\node[tick] at (4.13,1.15) {\tiny 3/0};
\node[tick] at (5.23,1.15) {\tiny 3/0};
\node[lab, anchor=east] at (-0.2,0.25) {after};
\path[tintC] (0.00,0.00) rectangle (5.50,0.50);
\draw[emph] (0.00,0.00) rectangle (5.50,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\draw[faint] (2.20,0.00) -- (2.20,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\draw[faint] (3.30,0.00) -- (3.30,0.50);
\draw[faint] (3.85,0.00) -- (3.85,0.50);
\draw[faint] (4.40,0.00) -- (4.40,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\node[tick] at (0.28,0.25) {\tiny 10/0};
\node[tick] at (5.22,0.25) {\tiny 10/0};
\node[lab] at (2.75,1.75) {case 4: both neighbours free};
\node[box] (r) at (7.6,0.25) {\texttt{root}};
\draw[->, draw=accent] (r.west) to[out=180,in=60] (2.75,0.55);
\node[tick, anchor=west] at (6.9,-0.45) {unlink both neighbours, merge all three, insert at the front};
\end{tikzpicture}
\end{center}
```

Freeing with the LIFO policy, case 4: both neighbours free: unlink both neighbours, merge all three, insert at the front

:::


::: {#def-segregated-free-lists .definition name="Segregated free lists"}

A *segregated* allocator keeps an array of free lists, one per *size class*, for example $\{1\},\{2\},\{3,4\},\{5,\dots,8\},\dots$ (powers of two above some size). To allocate $k$ words it searches the list of $k$'s class for a fitting block; if there is none it tries the next larger class, and if all are empty it requests more heap with `sbrk`. A block found is split if useful and the remainder inserted in the list of its own class. A freed block is coalesced and inserted in the list of its class.

:::

::: {#fig-explicit-and-segregated-lists-7}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,0.00) rectangle (1.4,0.55); \node[tick] at (0.7,0.27) {1--2};
\path[tintC] (2.00,0.00) rectangle (2.80,0.55); \draw[emph] (2.00,0.00) rectangle (2.80,0.55); \node[tick] at (2.40,0.27) {2};
\draw[->] (1.40,0.27) -- (2.00,0.27);
\path[tintC] (3.30,0.00) rectangle (4.10,0.55); \draw[emph] (3.30,0.00) rectangle (4.10,0.55); \node[tick] at (3.70,0.27) {2};
\draw[->] (2.80,0.27) -- (3.30,0.27);
\path[tintC] (4.60,0.00) rectangle (5.15,0.55); \draw[emph] (4.60,0.00) rectangle (5.15,0.55); \node[tick] at (4.88,0.27) {1};
\draw[->] (4.10,0.27) -- (4.60,0.27);
\draw[hl cell] (0,-0.75) rectangle (1.4,-0.20); \node[tick] at (0.7,-0.48) {3};
\path[tintC] (2.00,-0.75) rectangle (3.05,-0.20); \draw[emph] (2.00,-0.75) rectangle (3.05,-0.20); \node[tick] at (2.52,-0.48) {3};
\draw[->] (1.40,-0.48) -- (2.00,-0.48);
\draw[hl cell] (0,-1.50) rectangle (1.4,-0.95); \node[tick] at (0.7,-1.23) {4};
\path[tintC] (2.00,-1.50) rectangle (3.30,-0.95); \draw[emph] (2.00,-1.50) rectangle (3.30,-0.95); \node[tick] at (2.65,-1.23) {4};
\draw[->] (1.40,-1.23) -- (2.00,-1.23);
\path[tintC] (3.80,-1.50) rectangle (5.10,-0.95); \draw[emph] (3.80,-1.50) rectangle (5.10,-0.95); \node[tick] at (4.45,-1.23) {4};
\draw[->] (3.30,-1.23) -- (3.80,-1.23);
\draw[hl cell] (0,-2.25) rectangle (1.4,-1.70); \node[tick] at (0.7,-1.98) {5--8};
\path[tintC] (2.00,-2.25) rectangle (3.80,-1.70); \draw[emph] (2.00,-2.25) rectangle (3.80,-1.70); \node[tick] at (2.90,-1.98) {6};
\draw[->] (1.40,-1.98) -- (2.00,-1.98);
\path[tintC] (4.30,-2.25) rectangle (6.60,-1.70); \draw[emph] (4.30,-2.25) rectangle (6.60,-1.70); \node[tick] at (5.45,-1.98) {8};
\draw[->] (3.80,-1.98) -- (4.30,-1.98);
\path[tintC] (7.10,-2.25) rectangle (8.65,-1.70); \draw[emph] (7.10,-2.25) rectangle (8.65,-1.70); \node[tick] at (7.88,-1.98) {5};
\draw[->] (6.60,-1.98) -- (7.10,-1.98);
\path[tintC] (9.15,-2.25) rectangle (11.20,-1.70); \draw[emph] (9.15,-2.25) rectangle (11.20,-1.70); \node[tick] at (10.17,-1.98) {7};
\draw[->] (8.65,-1.98) -- (9.15,-1.98);
\draw[hl cell] (0,-3.00) rectangle (1.4,-2.45); \node[tick] at (0.7,-2.73) {9--$\infty$};
\path[tintC] (2.00,-3.00) rectangle (5.30,-2.45); \draw[emph] (2.00,-3.00) rectangle (5.30,-2.45); \node[tick] at (3.65,-2.73) {12};
\draw[->] (1.40,-2.73) -- (2.00,-2.73);
\node[tick] at (0.7,0.85) {size class (words)};
\end{tikzpicture}
\end{center}
```

Segregated free lists: one free list per size class. A request for $k$ words searches the class of $k$ first, then larger classes; the block found is split and the remainder goes to the list of its own class

:::


::: {#fig-explicit-and-segregated-lists-8}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (1.60,0.8) {request 5 words};
\draw[cell frame] (0.00,0.00) rectangle (0.90,0.45); \node[tick] at (0.45,0.22) {1--2};
\draw[cell frame] (1.10,0.00) rectangle (1.60,0.45); \node[tick] at (1.35,0.22) {2};
\draw[cell frame] (1.70,0.00) rectangle (2.20,0.45); \node[tick] at (1.95,0.22) {1};
\draw[cell frame] (0.00,-0.60) rectangle (0.90,-0.15); \node[tick] at (0.45,-0.38) {3};
\draw[cell frame] (0.00,-1.20) rectangle (0.90,-0.75); \node[tick] at (0.45,-0.98) {4};
\draw[cell frame] (1.10,-1.20) rectangle (1.60,-0.75); \node[tick] at (1.35,-0.98) {4};
\draw[cell frame] (0.00,-1.80) rectangle (0.90,-1.35); \node[tick] at (0.45,-1.58) {5--8};
\draw[hl cell] (1.10,-1.80) rectangle (1.60,-1.35); \node[tick] at (1.35,-1.58) {8};
\draw[cell frame] (1.70,-1.80) rectangle (2.20,-1.35); \node[tick] at (1.95,-1.58) {6};
\draw[cell frame] (0.00,-2.40) rectangle (0.90,-1.95); \node[tick] at (0.45,-2.18) {9--$\infty$};
\draw[cell frame] (1.10,-2.40) rectangle (1.60,-1.95); \node[tick] at (1.35,-2.18) {12};
\node[lab] at (5.90,0.8) {take the 8-word block};
\draw[cell frame] (4.30,0.00) rectangle (5.20,0.45); \node[tick] at (4.75,0.22) {1--2};
\draw[cell frame] (5.40,0.00) rectangle (5.90,0.45); \node[tick] at (5.65,0.22) {2};
\draw[cell frame] (6.00,0.00) rectangle (6.50,0.45); \node[tick] at (6.25,0.22) {1};
\draw[cell frame] (4.30,-0.60) rectangle (5.20,-0.15); \node[tick] at (4.75,-0.38) {3};
\draw[cell frame] (4.30,-1.20) rectangle (5.20,-0.75); \node[tick] at (4.75,-0.98) {4};
\draw[cell frame] (5.40,-1.20) rectangle (5.90,-0.75); \node[tick] at (5.65,-0.98) {4};
\draw[cell frame] (4.30,-1.80) rectangle (5.20,-1.35); \node[tick] at (4.75,-1.58) {5--8};
\draw[cell frame] (5.40,-1.80) rectangle (5.90,-1.35); \node[tick] at (5.65,-1.58) {6};
\draw[cell frame] (4.30,-2.40) rectangle (5.20,-1.95); \node[tick] at (4.75,-2.18) {9--$\infty$};
\draw[cell frame] (5.40,-2.40) rectangle (5.90,-1.95); \node[tick] at (5.65,-2.18) {12};
\node[lab] at (10.20,0.8) {split: 5 used, 3 left};
\draw[cell frame] (8.60,0.00) rectangle (9.50,0.45); \node[tick] at (9.05,0.22) {1--2};
\draw[cell frame] (9.70,0.00) rectangle (10.20,0.45); \node[tick] at (9.95,0.22) {2};
\draw[cell frame] (10.30,0.00) rectangle (10.80,0.45); \node[tick] at (10.55,0.22) {1};
\draw[cell frame] (8.60,-0.60) rectangle (9.50,-0.15); \node[tick] at (9.05,-0.38) {3};
\draw[hl cell] (9.70,-0.60) rectangle (10.20,-0.15); \node[tick] at (9.95,-0.38) {3};
\draw[cell frame] (8.60,-1.20) rectangle (9.50,-0.75); \node[tick] at (9.05,-0.98) {4};
\draw[cell frame] (9.70,-1.20) rectangle (10.20,-0.75); \node[tick] at (9.95,-0.98) {4};
\draw[cell frame] (8.60,-1.80) rectangle (9.50,-1.35); \node[tick] at (9.05,-1.58) {5--8};
\draw[cell frame] (9.70,-1.80) rectangle (10.20,-1.35); \node[tick] at (9.95,-1.58) {6};
\draw[cell frame] (8.60,-2.40) rectangle (9.50,-1.95); \node[tick] at (9.05,-2.18) {9--$\infty$};
\draw[cell frame] (9.70,-2.40) rectangle (10.20,-1.95); \node[tick] at (9.95,-2.18) {12};
\end{tikzpicture}
\end{center}
```

A segregated-fit allocation of 5 words: the class 5--8 holds an 8-word block, which is taken and split; the 3-word remainder is put on the list of class 3

:::


::: {#prp-segregated-best-fit .proposition name="Segregated fit approximates best fit"}

If each size class contains a single size, first fit within the class of the request finds a block of exactly the requested size whenever one exists among the free blocks, so the allocation is a best fit.

:::

::: {.proof}
1. A class with a single size $s$ holds only free blocks of size exactly $s$.

2. If the class of the request size $k$ is nonempty, its first block has size $k$, which is the smallest size that fits.

3. With wider classes the same argument shows that the chosen block is at most the largest size in the class, so the waste is bounded by the width of the class; this is why practical seglists are close to best fit at the speed of first fit.
:::

::: {#rmk-explicit-and-segregated-lists-1 name="Other designs"}

Free blocks can also be kept in a balanced search tree ordered by size, which gives true best fit in logarithmic time. The GNU C library's `malloc` uses segregated lists ("bins"), some holding a single size; Malloc Lab asks students to build an allocator of this kind and to trade throughput against utilization (@def-throughput-utilization).

:::
