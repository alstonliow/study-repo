---
title: "Caching in the Memory Hierarchy"
sources: [cmu15213-11, cmu15213r-7]
requires: [cs/memory-hierarchy/storage-technologies, cs/memory-hierarchy/locality]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 11 "The Memory Hierarchy" and Recitation 7 (types of cache misses), in our own wording. -->

::: {#def-memory-hierarchy .definition name="Memory hierarchy"}

A *memory hierarchy* is a sequence of storage levels $L_0,L_1,L_2,\dots$ in which each level is smaller, faster and costlier per byte than the next. Typically: $L_0$ registers, $L_1$–$L_3$ SRAM caches, $L_4$ main memory (DRAM), $L_5$ local disk or SSD, $L_6$ remote storage. Level $k$ serves as a *cache* for level $k+1$.

:::

::: {#fig-caching-in-the-hierarchy-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.7cm]
\foreach \l/\n/\w [count=\i from 0] in {L0/registers/1.0,L1/L1 cache (SRAM)/2.0,L2/L2 cache (SRAM)/3.0,L3/L3 cache (SRAM)/4.0,L4/main memory (DRAM)/5.0,L5/local disk or SSD/6.0,L6/remote storage/7.0} {
  \draw[cell frame] (-\w/2,-\i) rectangle (\w/2,-\i-0.85);
  \node[tick] at (0,-\i-0.42) {\n};
  \node[tick, anchor=east] at (-4,-\i-0.42) {\l};
}
\draw[->] (4.3,-0.2) -- (4.3,-6.6) node[midway, right, tick, align=left] {larger,\\slower,\\cheaper per byte};
\end{tikzpicture}
\end{center}
```

A typical memory hierarchy: each level caches blocks of the level below it

:::

::: {#def-cache-hit-miss .definition name="Blocks, hits and misses"}

Level $k+1$ is divided into *blocks*, the units of transfer; level $k$ holds copies of some of them. A request for a data object that is in a block present at level $k$ is a *hit*. Otherwise it is a *miss*: the block is fetched from level $k+1$, and if level $k$ is full, a *victim* block is *evicted* to make room. The *placement policy* decides where a block may go and the *replacement policy* which block is evicted.

:::

::: {#def-kinds-of-misses .definition name="Kinds of cache misses"}

- *Cold* (compulsory) miss: the first reference to a block; the cache starts empty.
- *Conflict* miss: the cache has room, but the placement policy maps several active blocks to the same place, so they evict one another.
- *Capacity* miss: the set of blocks the program uses during a phase, its *working set*, is larger than the cache.

:::

::: {#exm-conflict-misses .example name="Blocks that collide"}

Let level $k$ have four places and put block $i$ of level $k+1$ in place $i\bmod4$. The reference sequence $0,8,0,8,0,8,\dots$ misses every time: blocks $0$ and $8$ both map to place $0$ and evict each other, although three places stay empty. A cache with the same capacity that let any block go anywhere would have two cold misses and then only hits.

:::

::: {#fig-caching-in-the-hierarchy-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,3} { \draw[cell frame] (\i*0.8,1.6) rectangle (\i*0.8+0.8,2.2); \node[tick] at (\i*0.8+0.4,2.4) {\i}; }
\draw[hl cell] (0,1.6) rectangle (0.8,2.2); \node[lab] at (0.4,1.9) {0/8};
\foreach \i in {0,...,15} { \draw[cell frame] (\i*0.6-1.6,0) rectangle (\i*0.6-1.0,0.5); \node[tick] at (\i*0.6-1.3,0.25) {\i}; }
\draw[hl cell] (-1.6,0) rectangle (-1.0,0.5); \node[tick] at (-1.3,0.25) {0};
\draw[hl cell] (3.2,0) rectangle (3.8,0.5); \node[tick] at (3.5,0.25) {8};
\draw[map, draw=accent] (-1.3,0.55) -- (0.3,1.55);
\draw[map, draw=accent] (3.5,0.55) -- (0.5,1.55);
\node[lab, anchor=west] at (3.6,1.9) {level $k$};
\node[lab, anchor=west] at (8.1,0.25) {level $k+1$};
\end{tikzpicture}
\end{center}
```

With the placement rule "block $i$ goes to place $i \bmod 4$", blocks $0$ and $8$ compete for place $0$ and cause conflict misses

:::

::: {#exm-caches-everywhere .example name="Caches throughout a system"}

| cache | what is cached | where | managed by |
|---|---|---|---|
| registers | 4–8-byte words | CPU core | compiler |
| TLB | address translations | MMU | hardware |
| L1, L2, L3 | 64-byte blocks | on chip | hardware |
| virtual memory | 4 KiB pages | main memory | hardware and OS |
| buffer cache | parts of files | main memory | OS |
| browser cache | web pages | local disk | web browser |

The same idea, keep recently used items close, recurs at every scale; virtual memory (@def-vm-as-cache) and the translation lookaside buffer (@def-tlb) are two of the instances.

:::

::: {#rmk-caching-in-the-hierarchy-1 name="Why hierarchies work"}

Because of locality (@def-locality), a program tends to use a block at level $k$ many times once it is brought in, so the cost of the slow transfer from level $k+1$ is spread over many fast accesses. The whole hierarchy then behaves almost like a memory as large as its bottom level and almost as fast as its top.

:::
