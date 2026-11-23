---
title: "Implicit Free Lists and Coalescing"
sources: [cmu15213-19, cmu15213lab-6]
requires: [cs/virtual-memory/dynamic-memory-allocation]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 19 "Dynamic Memory Allocation: Basic Concepts" and the Malloc Lab handout, in our own wording; the example trace is our own. -->

::: {#def-implicit-free-list .definition name="Implicit free list"}

In an *implicit free list* every block, allocated or free, starts with a one-word *header* holding the block size (including the header) and an *allocated bit*. Because block sizes are multiples of the alignment (8 or 16 bytes), the low bits of the size are always $0$ and the allocated bit can share the word. The blocks form a list *implicitly*: the next block starts at the current block's address plus its size. A final header of size $0$, marked allocated, ends the list.

:::

::: {#fig-implicit-free-lists-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,0) rectangle (3.0,0.5); \node[tick] at (1.5,0.25) {size};
\draw[hl cell] (3.0,0) rectangle (3.8,0.5); \node[tick] at (3.4,0.25) {a};
\path[tintA] (0,-1.2) rectangle (3.8,-0.05); \draw[emph] (0,-1.2) rectangle (3.8,-0.05); \node[tick] at (1.9,-0.62) {payload and padding};
\draw[hl cell] (0,-1.75) rectangle (3.0,-1.25); \node[tick] at (1.5,-1.5) {size};
\draw[hl cell] (3.0,-1.75) rectangle (3.8,-1.25); \node[tick] at (3.4,-1.5) {a};
\node[lab, anchor=west] at (4.0,0.25) {header};
\node[lab, anchor=west] at (4.0,-1.5) {footer (boundary tag): a copy of the header};
\node[lab, anchor=west] at (4.0,-0.62) {pointer returned by \texttt{malloc}};
\draw[->] (4.0,-0.5) -- (3.85,-0.1);
\node[tick, anchor=west] at (4.0,0.7) {$a=1$: allocated, $a=0$: free; sizes are multiples of 8, so the low bits are free for $a$};
\end{tikzpicture}
\end{center}
```

Format of a block: a one-word header with the block size and the allocated bit, the payload, and (with boundary tags) a footer that repeats the header

:::


::: {#fig-implicit-free-lists-2}

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
\path[tintC] (2.20,0.00) rectangle (4.40,0.50);
\draw[emph] (2.20,0.00) rectangle (4.40,0.50);
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
\path[tintC] (7.70,0.00) rectangle (8.80,0.50);
\draw[emph] (7.70,0.00) rectangle (8.80,0.50);
\draw[faint] (8.25,0.00) -- (8.25,0.50);
\node[tick] at (7.98,0.25) {\tiny 2/0};
\node[tick] at (8.53,0.25) {\tiny 2/0};
\draw[->, draw=accent] (0.28,0.55) to[out=60,in=120] (2.48,0.55);
\draw[->, draw=accent] (2.48,0.55) to[out=60,in=120] (4.68,0.55);
\draw[->, draw=accent] (4.68,0.55) to[out=60,in=120] (7.98,0.55);
\draw[hl cell] (8.80,0) rectangle (9.35,0.5); \node[tick] at (9.08,-0.25) {end 0/1};
\node[tick, anchor=west] at (0,-0.35) {header labels: size in words / allocated bit};
\end{tikzpicture}
\end{center}
```

A heap as an implicit free list: each header gives the size of its block, so adding the size to a block's address finds the next block (arrows); an allocated header of size 0 ends the list

:::


::: {#def-placement-policies .definition name="Placement policies"}

To serve a request for a block of $k$ words, the allocator searches the list for a free block of at least $k$ words:

- *first fit*: the first suitable block from the start of the list;
- *next fit*: the first suitable block after the place where the previous search stopped;
- *best fit*: the smallest suitable block in the whole list.

If no free block is large enough, the allocator asks the kernel for more heap with `sbrk` and makes a new free block at the end.

:::

::: {#fig-implicit-free-lists-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,0.25) {request 3 words};
\path[tintA] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/1};
\node[tick] at (1.93,0.25) {\tiny 4/1};
\path[tintC] (2.20,0.00) rectangle (4.40,0.50);
\draw[emph] (2.20,0.00) rectangle (4.40,0.50);
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
\path[tintC] (7.70,0.00) rectangle (8.80,0.50);
\draw[emph] (7.70,0.00) rectangle (8.80,0.50);
\draw[faint] (8.25,0.00) -- (8.25,0.50);
\node[tick] at (7.98,0.25) {\tiny 2/0};
\node[tick] at (8.53,0.25) {\tiny 2/0};
\node[tick] at (1.10,-0.3) {allocated: skip};
\node[tick, text=accent] at (3.30,-0.6) {first free block big enough};
\draw[hl] (2.20,0) rectangle (4.40,0.5);
\end{tikzpicture}
\end{center}
```

First fit: scan the list from the start and take the first free block that is large enough (here the 4-word block at word 4)

:::


::: {#rmk-implicit-free-lists-1 name="Comparing the policies"}

All three take time linear in the total number of blocks, allocated ones included, which is the main weakness of implicit lists. First fit tends to leave many small fragments ("splinters") near the start of the heap; next fit is faster but has been observed to fragment more; best fit fragments least but must scan the whole list.

:::

::: {#def-splitting .definition name="Splitting"}

If the chosen free block has $f$ words and the request needs $k<f$ words, the allocator may *split* it: the first $k$ words become the allocated block and the remaining $f-k$ words a new free block with its own header. Splitting is done only if $f-k$ is at least the minimum block size; otherwise the whole block is allocated and the extra words are internal fragmentation (@def-fragmentation).

:::

::: {#fig-implicit-free-lists-4}

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
\path[tintC] (2.20,1.00) rectangle (4.40,1.50);
\draw[emph] (2.20,1.00) rectangle (4.40,1.50);
\draw[faint] (2.75,1.00) -- (2.75,1.50);
\draw[faint] (3.30,1.00) -- (3.30,1.50);
\draw[faint] (3.85,1.00) -- (3.85,1.50);
\node[tick] at (2.48,1.25) {\tiny 4/0};
\node[tick] at (4.12,1.25) {\tiny 4/0};
\path[tintA] (4.40,1.00) rectangle (7.70,1.50);
\draw[emph] (4.40,1.00) rectangle (7.70,1.50);
\draw[faint] (4.95,1.00) -- (4.95,1.50);
\draw[faint] (5.50,1.00) -- (5.50,1.50);
\draw[faint] (6.05,1.00) -- (6.05,1.50);
\draw[faint] (6.60,1.00) -- (6.60,1.50);
\draw[faint] (7.15,1.00) -- (7.15,1.50);
\node[tick] at (4.68,1.25) {\tiny 6/1};
\node[tick] at (7.43,1.25) {\tiny 6/1};
\path[tintC] (7.70,1.00) rectangle (8.80,1.50);
\draw[emph] (7.70,1.00) rectangle (8.80,1.50);
\draw[faint] (8.25,1.00) -- (8.25,1.50);
\node[tick] at (7.98,1.25) {\tiny 2/0};
\node[tick] at (8.53,1.25) {\tiny 2/0};
\node[lab, anchor=east] at (-0.2,0.25) {after split};
\path[tintA] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/1};
\node[tick] at (1.93,0.25) {\tiny 4/1};
\path[tintA] (2.20,0.00) rectangle (3.30,0.50);
\draw[hl] (2.20,0.00) rectangle (3.30,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\node[tick] at (2.48,0.25) {\tiny 2/1};
\node[tick] at (3.03,0.25) {\tiny 2/1};
\path[tintC] (3.30,0.00) rectangle (4.40,0.50);
\draw[hl] (3.30,0.00) rectangle (4.40,0.50);
\draw[faint] (3.85,0.00) -- (3.85,0.50);
\node[tick] at (3.58,0.25) {\tiny 2/0};
\node[tick] at (4.12,0.25) {\tiny 2/0};
\path[tintA] (4.40,0.00) rectangle (7.70,0.50);
\draw[emph] (4.40,0.00) rectangle (7.70,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\draw[faint] (5.50,0.00) -- (5.50,0.50);
\draw[faint] (6.05,0.00) -- (6.05,0.50);
\draw[faint] (6.60,0.00) -- (6.60,0.50);
\draw[faint] (7.15,0.00) -- (7.15,0.50);
\node[tick] at (4.68,0.25) {\tiny 6/1};
\node[tick] at (7.43,0.25) {\tiny 6/1};
\path[tintC] (7.70,0.00) rectangle (8.80,0.50);
\draw[emph] (7.70,0.00) rectangle (8.80,0.50);
\draw[faint] (8.25,0.00) -- (8.25,0.50);
\node[tick] at (7.98,0.25) {\tiny 2/0};
\node[tick] at (8.53,0.25) {\tiny 2/0};
\end{tikzpicture}
\end{center}
```

Splitting: a request that needs 2 of the 4 words of a free block takes the first part, and the rest becomes a new free block with its own header and footer

:::


::: {#def-coalescing .definition name="Coalescing"}

When a block is freed, it may lie next to other free blocks. *Coalescing* merges adjacent free blocks into one. Without it, the heap fills with small adjacent free blocks that together could satisfy a request but individually cannot (*false fragmentation*).

:::

::: {#fig-implicit-free-lists-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,1.25) {free the 2-word block};
\path[tintA] (0.00,1.00) rectangle (2.20,1.50);
\draw[emph] (0.00,1.00) rectangle (2.20,1.50);
\draw[faint] (0.55,1.00) -- (0.55,1.50);
\draw[faint] (1.10,1.00) -- (1.10,1.50);
\draw[faint] (1.65,1.00) -- (1.65,1.50);
\node[tick] at (0.28,1.25) {\tiny 4/1};
\node[tick] at (1.93,1.25) {\tiny 4/1};
\path[tintA] (2.20,1.00) rectangle (3.30,1.50);
\draw[emph] (2.20,1.00) rectangle (3.30,1.50);
\draw[faint] (2.75,1.00) -- (2.75,1.50);
\node[tick] at (2.48,1.25) {\tiny 2/1};
\node[tick] at (3.03,1.25) {\tiny 2/1};
\path[tintC] (3.30,1.00) rectangle (4.40,1.50);
\draw[emph] (3.30,1.00) rectangle (4.40,1.50);
\draw[faint] (3.85,1.00) -- (3.85,1.50);
\node[tick] at (3.58,1.25) {\tiny 2/0};
\node[tick] at (4.12,1.25) {\tiny 2/0};
\path[tintA] (4.40,1.00) rectangle (7.70,1.50);
\draw[emph] (4.40,1.00) rectangle (7.70,1.50);
\draw[faint] (4.95,1.00) -- (4.95,1.50);
\draw[faint] (5.50,1.00) -- (5.50,1.50);
\draw[faint] (6.05,1.00) -- (6.05,1.50);
\draw[faint] (6.60,1.00) -- (6.60,1.50);
\draw[faint] (7.15,1.00) -- (7.15,1.50);
\node[tick] at (4.68,1.25) {\tiny 6/1};
\node[tick] at (7.43,1.25) {\tiny 6/1};
\path[tintC] (7.70,1.00) rectangle (8.80,1.50);
\draw[emph] (7.70,1.00) rectangle (8.80,1.50);
\draw[faint] (8.25,1.00) -- (8.25,1.50);
\node[tick] at (7.98,1.25) {\tiny 2/0};
\node[tick] at (8.53,1.25) {\tiny 2/0};
\node[lab, anchor=east] at (-0.2,0.25) {without coalescing};
\path[tintA] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/1};
\node[tick] at (1.93,0.25) {\tiny 4/1};
\path[tintC] (2.20,0.00) rectangle (3.30,0.50);
\draw[hl] (2.20,0.00) rectangle (3.30,0.50);
\draw[faint] (2.75,0.00) -- (2.75,0.50);
\node[tick] at (2.48,0.25) {\tiny 2/0};
\node[tick] at (3.03,0.25) {\tiny 2/0};
\path[tintC] (3.30,0.00) rectangle (4.40,0.50);
\draw[hl] (3.30,0.00) rectangle (4.40,0.50);
\draw[faint] (3.85,0.00) -- (3.85,0.50);
\node[tick] at (3.58,0.25) {\tiny 2/0};
\node[tick] at (4.12,0.25) {\tiny 2/0};
\path[tintA] (4.40,0.00) rectangle (7.70,0.50);
\draw[emph] (4.40,0.00) rectangle (7.70,0.50);
\draw[faint] (4.95,0.00) -- (4.95,0.50);
\draw[faint] (5.50,0.00) -- (5.50,0.50);
\draw[faint] (6.05,0.00) -- (6.05,0.50);
\draw[faint] (6.60,0.00) -- (6.60,0.50);
\draw[faint] (7.15,0.00) -- (7.15,0.50);
\node[tick] at (4.68,0.25) {\tiny 6/1};
\node[tick] at (7.43,0.25) {\tiny 6/1};
\path[tintC] (7.70,0.00) rectangle (8.80,0.50);
\draw[emph] (7.70,0.00) rectangle (8.80,0.50);
\draw[faint] (8.25,0.00) -- (8.25,0.50);
\node[tick] at (7.98,0.25) {\tiny 2/0};
\node[tick] at (8.53,0.25) {\tiny 2/0};
\node[tick, text=accent, anchor=west] at (9.00,0.25) {a 4-word request fails};
\end{tikzpicture}
\end{center}
```

Freeing without coalescing leaves two adjacent free blocks of 2 words: a 4-word request fails although 4 adjacent words are free (false fragmentation)

:::


::: {#def-boundary-tags .definition name="Boundary tags"}

A header lets the allocator find the *next* block in constant time, but not the previous one. *Boundary tags* add a *footer*, a copy of the header, at the end of every block. The footer of the previous block lies in the word just before the current header, so both neighbours of a block can be examined in constant time.

:::

::: {#thm-constant-time-coalescing .theorem name="Constant-time coalescing"}

With boundary tags, freeing a block and merging it with every free neighbour takes $O(1)$ time, by four cases on whether the previous and the next block are allocated.

:::

::: {.proof}
1. The next block's header is at the freed block's address plus its size; the previous block's footer is the word before the freed block's header. Reading both takes constant time.

2. *Both allocated*: only the freed block's header and footer change ($a\gets0$).

3. *Next free*: the new block runs from the freed block's header to the next block's footer; write the sum of the two sizes into both.

4. *Previous free*: the new block runs from the previous block's header (found through its footer, which gives its size) to the freed block's footer; write the sum into both.

5. *Both free*: the new block runs from the previous block's header to the next block's footer, with the sum of three sizes.

6. Each case reads and writes a constant number of words. Afterwards no two free blocks are adjacent: by induction over all operations there were none before the free, and the merged block absorbed every free neighbour.
:::

::: {#fig-implicit-free-lists-6}

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
\end{tikzpicture}
\end{center}
```

Constant-time coalescing, case 1: both neighbours allocated: the block in the middle is freed; only its allocated bits change

:::


::: {#fig-implicit-free-lists-7}

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
\end{tikzpicture}
\end{center}
```

Constant-time coalescing, case 2: next block free: the block in the middle is freed; it merges with the next block, whose footer gets the new size

:::


::: {#fig-implicit-free-lists-8}

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
\end{tikzpicture}
\end{center}
```

Constant-time coalescing, case 3: previous block free: the block in the middle is freed; it merges with the previous block, found through the footer just before the freed header

:::


::: {#fig-implicit-free-lists-9}

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
\end{tikzpicture}
\end{center}
```

Constant-time coalescing, case 4: both neighbours free: the block in the middle is freed; all three merge into one free block

:::


::: {#exm-implicit-list-trace .example name="A trace of requests"}

Take 8-byte words, 16-byte alignment, a header and a footer of one word each, and a minimum block of 4 words. A request for $n$ bytes needs a block of $\max\bigl(4,\,2\lceil(n+16)/16\rceil\bigr)$ words. The requests `a = malloc(10)`, `b = malloc(20)`, `c = malloc(5)`, `free(b)`, `d = malloc(8)`, `free(a)`, `free(d)`, served with first fit, splitting and coalescing, give the heaps of the figure below.

:::

::: {#fig-implicit-free-lists-10}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,0.25) {\texttt{a = malloc(10)}};
\path[tintA] (0.00,0.00) rectangle (2.20,0.50);
\draw[emph] (0.00,0.00) rectangle (2.20,0.50);
\draw[faint] (0.55,0.00) -- (0.55,0.50);
\draw[faint] (1.10,0.00) -- (1.10,0.50);
\draw[faint] (1.65,0.00) -- (1.65,0.50);
\node[tick] at (0.28,0.25) {\tiny 4/1};
\node[tick] at (1.93,0.25) {\tiny 4/1};
\node[tick] at (1.10,0.75) {\texttt{a}};
\node[lab, anchor=east] at (-0.2,-0.95) {\texttt{b = malloc(20)}};
\path[tintA] (0.00,-1.20) rectangle (2.20,-0.70);
\draw[emph] (0.00,-1.20) rectangle (2.20,-0.70);
\draw[faint] (0.55,-1.20) -- (0.55,-0.70);
\draw[faint] (1.10,-1.20) -- (1.10,-0.70);
\draw[faint] (1.65,-1.20) -- (1.65,-0.70);
\node[tick] at (0.28,-0.95) {\tiny 4/1};
\node[tick] at (1.93,-0.95) {\tiny 4/1};
\node[tick] at (1.10,-0.45) {\texttt{a}};
\path[tintA] (2.20,-1.20) rectangle (5.50,-0.70);
\draw[emph] (2.20,-1.20) rectangle (5.50,-0.70);
\draw[faint] (2.75,-1.20) -- (2.75,-0.70);
\draw[faint] (3.30,-1.20) -- (3.30,-0.70);
\draw[faint] (3.85,-1.20) -- (3.85,-0.70);
\draw[faint] (4.40,-1.20) -- (4.40,-0.70);
\draw[faint] (4.95,-1.20) -- (4.95,-0.70);
\node[tick] at (2.48,-0.95) {\tiny 6/1};
\node[tick] at (5.22,-0.95) {\tiny 6/1};
\node[tick] at (3.85,-0.45) {\texttt{b}};
\node[lab, anchor=east] at (-0.2,-2.15) {\texttt{c = malloc(5)}};
\path[tintA] (0.00,-2.40) rectangle (2.20,-1.90);
\draw[emph] (0.00,-2.40) rectangle (2.20,-1.90);
\draw[faint] (0.55,-2.40) -- (0.55,-1.90);
\draw[faint] (1.10,-2.40) -- (1.10,-1.90);
\draw[faint] (1.65,-2.40) -- (1.65,-1.90);
\node[tick] at (0.28,-2.15) {\tiny 4/1};
\node[tick] at (1.93,-2.15) {\tiny 4/1};
\node[tick] at (1.10,-1.65) {\texttt{a}};
\path[tintA] (2.20,-2.40) rectangle (5.50,-1.90);
\draw[emph] (2.20,-2.40) rectangle (5.50,-1.90);
\draw[faint] (2.75,-2.40) -- (2.75,-1.90);
\draw[faint] (3.30,-2.40) -- (3.30,-1.90);
\draw[faint] (3.85,-2.40) -- (3.85,-1.90);
\draw[faint] (4.40,-2.40) -- (4.40,-1.90);
\draw[faint] (4.95,-2.40) -- (4.95,-1.90);
\node[tick] at (2.48,-2.15) {\tiny 6/1};
\node[tick] at (5.22,-2.15) {\tiny 6/1};
\node[tick] at (3.85,-1.65) {\texttt{b}};
\path[tintA] (5.50,-2.40) rectangle (7.70,-1.90);
\draw[emph] (5.50,-2.40) rectangle (7.70,-1.90);
\draw[faint] (6.05,-2.40) -- (6.05,-1.90);
\draw[faint] (6.60,-2.40) -- (6.60,-1.90);
\draw[faint] (7.15,-2.40) -- (7.15,-1.90);
\node[tick] at (5.78,-2.15) {\tiny 4/1};
\node[tick] at (7.42,-2.15) {\tiny 4/1};
\node[tick] at (6.60,-1.65) {\texttt{c}};
\node[lab, anchor=east] at (-0.2,-3.35) {\texttt{free(b)}};
\path[tintA] (0.00,-3.60) rectangle (2.20,-3.10);
\draw[emph] (0.00,-3.60) rectangle (2.20,-3.10);
\draw[faint] (0.55,-3.60) -- (0.55,-3.10);
\draw[faint] (1.10,-3.60) -- (1.10,-3.10);
\draw[faint] (1.65,-3.60) -- (1.65,-3.10);
\node[tick] at (0.28,-3.35) {\tiny 4/1};
\node[tick] at (1.93,-3.35) {\tiny 4/1};
\node[tick] at (1.10,-2.85) {\texttt{a}};
\path[tintC] (2.20,-3.60) rectangle (5.50,-3.10);
\draw[emph] (2.20,-3.60) rectangle (5.50,-3.10);
\draw[faint] (2.75,-3.60) -- (2.75,-3.10);
\draw[faint] (3.30,-3.60) -- (3.30,-3.10);
\draw[faint] (3.85,-3.60) -- (3.85,-3.10);
\draw[faint] (4.40,-3.60) -- (4.40,-3.10);
\draw[faint] (4.95,-3.60) -- (4.95,-3.10);
\node[tick] at (2.48,-3.35) {\tiny 6/0};
\node[tick] at (5.22,-3.35) {\tiny 6/0};
\path[tintA] (5.50,-3.60) rectangle (7.70,-3.10);
\draw[emph] (5.50,-3.60) rectangle (7.70,-3.10);
\draw[faint] (6.05,-3.60) -- (6.05,-3.10);
\draw[faint] (6.60,-3.60) -- (6.60,-3.10);
\draw[faint] (7.15,-3.60) -- (7.15,-3.10);
\node[tick] at (5.78,-3.35) {\tiny 4/1};
\node[tick] at (7.42,-3.35) {\tiny 4/1};
\node[tick] at (6.60,-2.85) {\texttt{c}};
\node[lab, anchor=east] at (-0.2,-4.55) {\texttt{d = malloc(8)}};
\path[tintA] (0.00,-4.80) rectangle (2.20,-4.30);
\draw[emph] (0.00,-4.80) rectangle (2.20,-4.30);
\draw[faint] (0.55,-4.80) -- (0.55,-4.30);
\draw[faint] (1.10,-4.80) -- (1.10,-4.30);
\draw[faint] (1.65,-4.80) -- (1.65,-4.30);
\node[tick] at (0.28,-4.55) {\tiny 4/1};
\node[tick] at (1.93,-4.55) {\tiny 4/1};
\node[tick] at (1.10,-4.05) {\texttt{a}};
\path[tintA] (2.20,-4.80) rectangle (5.50,-4.30);
\draw[emph] (2.20,-4.80) rectangle (5.50,-4.30);
\draw[faint] (2.75,-4.80) -- (2.75,-4.30);
\draw[faint] (3.30,-4.80) -- (3.30,-4.30);
\draw[faint] (3.85,-4.80) -- (3.85,-4.30);
\draw[faint] (4.40,-4.80) -- (4.40,-4.30);
\draw[faint] (4.95,-4.80) -- (4.95,-4.30);
\node[tick] at (2.48,-4.55) {\tiny 6/1};
\node[tick] at (5.22,-4.55) {\tiny 6/1};
\node[tick] at (3.85,-4.05) {\texttt{d}};
\path[tintA] (5.50,-4.80) rectangle (7.70,-4.30);
\draw[emph] (5.50,-4.80) rectangle (7.70,-4.30);
\draw[faint] (6.05,-4.80) -- (6.05,-4.30);
\draw[faint] (6.60,-4.80) -- (6.60,-4.30);
\draw[faint] (7.15,-4.80) -- (7.15,-4.30);
\node[tick] at (5.78,-4.55) {\tiny 4/1};
\node[tick] at (7.42,-4.55) {\tiny 4/1};
\node[tick] at (6.60,-4.05) {\texttt{c}};
\node[lab, anchor=east] at (-0.2,-5.75) {\texttt{free(a)}};
\path[tintC] (0.00,-6.00) rectangle (2.20,-5.50);
\draw[emph] (0.00,-6.00) rectangle (2.20,-5.50);
\draw[faint] (0.55,-6.00) -- (0.55,-5.50);
\draw[faint] (1.10,-6.00) -- (1.10,-5.50);
\draw[faint] (1.65,-6.00) -- (1.65,-5.50);
\node[tick] at (0.28,-5.75) {\tiny 4/0};
\node[tick] at (1.93,-5.75) {\tiny 4/0};
\path[tintA] (2.20,-6.00) rectangle (5.50,-5.50);
\draw[emph] (2.20,-6.00) rectangle (5.50,-5.50);
\draw[faint] (2.75,-6.00) -- (2.75,-5.50);
\draw[faint] (3.30,-6.00) -- (3.30,-5.50);
\draw[faint] (3.85,-6.00) -- (3.85,-5.50);
\draw[faint] (4.40,-6.00) -- (4.40,-5.50);
\draw[faint] (4.95,-6.00) -- (4.95,-5.50);
\node[tick] at (2.48,-5.75) {\tiny 6/1};
\node[tick] at (5.22,-5.75) {\tiny 6/1};
\node[tick] at (3.85,-5.25) {\texttt{d}};
\path[tintA] (5.50,-6.00) rectangle (7.70,-5.50);
\draw[emph] (5.50,-6.00) rectangle (7.70,-5.50);
\draw[faint] (6.05,-6.00) -- (6.05,-5.50);
\draw[faint] (6.60,-6.00) -- (6.60,-5.50);
\draw[faint] (7.15,-6.00) -- (7.15,-5.50);
\node[tick] at (5.78,-5.75) {\tiny 4/1};
\node[tick] at (7.42,-5.75) {\tiny 4/1};
\node[tick] at (6.60,-5.25) {\texttt{c}};
\node[lab, anchor=east] at (-0.2,-6.95) {\texttt{free(d)}};
\path[tintC] (0.00,-7.20) rectangle (5.50,-6.70);
\draw[emph] (0.00,-7.20) rectangle (5.50,-6.70);
\draw[faint] (0.55,-7.20) -- (0.55,-6.70);
\draw[faint] (1.10,-7.20) -- (1.10,-6.70);
\draw[faint] (1.65,-7.20) -- (1.65,-6.70);
\draw[faint] (2.20,-7.20) -- (2.20,-6.70);
\draw[faint] (2.75,-7.20) -- (2.75,-6.70);
\draw[faint] (3.30,-7.20) -- (3.30,-6.70);
\draw[faint] (3.85,-7.20) -- (3.85,-6.70);
\draw[faint] (4.40,-7.20) -- (4.40,-6.70);
\draw[faint] (4.95,-7.20) -- (4.95,-6.70);
\node[tick] at (0.28,-6.95) {\tiny 10/0};
\node[tick] at (5.22,-6.95) {\tiny 10/0};
\path[tintA] (5.50,-7.20) rectangle (7.70,-6.70);
\draw[emph] (5.50,-7.20) rectangle (7.70,-6.70);
\draw[faint] (6.05,-7.20) -- (6.05,-6.70);
\draw[faint] (6.60,-7.20) -- (6.60,-6.70);
\draw[faint] (7.15,-7.20) -- (7.15,-6.70);
\node[tick] at (5.78,-6.95) {\tiny 4/1};
\node[tick] at (7.42,-6.95) {\tiny 4/1};
\node[tick] at (6.60,-6.45) {\texttt{c}};
\end{tikzpicture}
\end{center}
```

Running the requests of @exm-implicit-list-trace (sizes in 8-byte words; the header and footer labels show size/allocated). `d` takes a whole 6-word block because the 2-word remainder would be below the minimum block size, and the last `free` merges `d` with the free block before it

:::


::: {#rmk-implicit-free-lists-2 name="Cost of boundary tags"}

Footers cost one word per block, a large overhead for small blocks. Only free blocks need footers, though: an allocated block can record in a spare low bit of its own header whether the *previous* block is allocated, and then a footer is needed only when that bit says "free". Allocated blocks then carry no footer at all.

:::
