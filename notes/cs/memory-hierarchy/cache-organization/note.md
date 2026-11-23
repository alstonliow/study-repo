---
title: "Cache Memory Organization"
sources: [cmu15213-12, cmu15213r-7, cmu15213lab-4]
requires: [cs/memory-hierarchy/caching-in-the-hierarchy]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 12 "Cache Memories", Recitation 7 and the Cache Lab handout (part A: a cache simulator), in our own wording; the example trace is our own. -->

The SRAM caches between the registers and main memory are managed entirely by hardware. Their organization is described by a few parameters, and it determines which addresses can live in the cache at the same time.

::: {#def-cache-parameters .definition name="Cache organization $(S,E,B,m)$"}

For a machine with $m$-bit addresses, a cache is an array of $S=2^s$ *sets*; each set holds $E$ *lines*; each line holds a *valid bit*, a *tag* of $t=m-s-b$ bits, and a *block* of $B=2^b$ bytes. The *capacity* is $C=S\cdot E\cdot B$ data bytes. An address is split as
$$\underbrace{\text{tag}}_{t\text{ bits}}\ \big|\ \underbrace{\text{set index}}_{s\text{ bits}}\ \big|\ \underbrace{\text{block offset}}_{b\text{ bits}} .$$
A cache with $E=1$ is *direct-mapped*; with $1<E<C/B$ it is *$E$-way set-associative*; with $S=1$ it is *fully associative*.

:::

::: {#fig-cache-organization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \s in {0,1,2} {
  \foreach \e in {0,1} {
    \pgfmathsetmacro{\y}{-\s*1.45-\e*0.6}
    \draw[cell frame] (0,\y) rectangle (0.5,\y+0.5); \node[tick] at (0.25,\y+0.25) {v};
    \draw[cell frame] (0.55,\y) rectangle (1.75,\y+0.5); \node[tick] at (1.15,\y+0.25) {tag};
    \foreach \k in {0,...,7} { \draw[cell frame] (1.8+\k*0.45,\y) rectangle (2.25+\k*0.45,\y+0.5); \node[tick] at (2.025+\k*0.45,\y+0.25) {\k}; }
  }
  \draw[draw=primary] (-0.08,-\s*1.45-0.68) rectangle (5.48,-\s*1.45+0.58);
  \node[tick, anchor=east] at (-0.15,-\s*1.45-0.05) {set \s};
}
\node[tick] at (2.7,-4.2) {\vdots};
\node[tick, anchor=west] at (5.6,0.25) {$E=2$ lines per set};
\node[tick] at (3.6,0.8) {block: $B=8$ bytes};
\draw[cell frame] (1.0,-5.4) rectangle (3.0,-4.85); \node[tick] at (2.0,-5.12) {tag ($t$ bits)};
\draw[hl cell] (3.0,-5.4) rectangle (4.6,-4.85); \node[tick] at (3.8,-5.12) {set ($s$)};
\draw[cell frame] (4.6,-5.4) rectangle (6.2,-4.85); \node[tick] at (5.4,-5.12) {offset ($b$)};
\node[lab, anchor=east] at (0.9,-5.12) {address};
\end{tikzpicture}
\end{center}
```

A 2-way set-associative cache with 8-byte blocks. The middle $s$ bits of an address choose the set, the tag is compared with the tags of that set's lines, and the low $b$ bits choose the byte in the block

:::

::: {#def-cache-lookup .definition name="Cache read"}

To read the word at address $A$:

1. *Set selection*: take the $s$ set-index bits of $A$ and go to that set.
2. *Line matching*: look for a line in the set whose valid bit is $1$ and whose tag equals the tag bits of $A$. If one exists, it is a hit.
3. *Word extraction*: on a hit, the $b$ offset bits give the position of the word within the block.

On a miss, the block containing $A$ is fetched from the next level and stored in the set: in an invalid line if there is one, otherwise in place of a victim chosen by the replacement policy, typically *least recently used* (LRU).

:::

::: {#prp-middle-bits-index .proposition name="Why the set index uses the middle bits"}

With the set index taken from the bits just above the block offset, any $S$ consecutive blocks of memory map to $S$ different sets. If the index came from the high-order bits instead, a run of consecutive blocks would share one set.

:::

::: {.proof}
1. Consecutive blocks have addresses $A, A+B, A+2B,\dots$, so their block numbers $\lfloor A/B\rfloor,\lfloor A/B\rfloor+1,\dots$ are consecutive integers.

2. The middle bits are the block number mod $S$, and $S$ consecutive integers have $S$ different residues mod $S$, so they land in $S$ different sets.

3. The high-order bits, $\lfloor A/2^{m-s}\rfloor$, are the same for every address in an aligned range of $2^{m-s}$ bytes, so all the blocks of such a range would compete for one set, and a program scanning an array sequentially would use only one set of the cache.
:::

::: {#exm-cache-trace .example name="Simulating a small cache"}

Take $m=6$, $B=4$ ($b=2$), $S=4$ ($s=2$), $E=1$: a direct-mapped cache of $16$ bytes. Run the byte addresses $0,4,1,16,0,36,20,4$:

| address | bits (tag, set, offset) | set | result |
|---|---|---|---|
| 0 | 00 00 00 | 0 | miss (cold) |
| 4 | 00 01 00 | 1 | miss (cold) |
| 1 | 00 00 01 | 0 | hit |
| 16 | 01 00 00 | 0 | miss, evicts tag 0 |
| 0 | 00 00 00 | 0 | miss, evicts tag 1 (conflict) |
| 36 | 10 01 00 | 1 | miss, evicts tag 0 |
| 20 | 01 01 00 | 1 | miss, evicts tag 2 |
| 4 | 00 01 00 | 1 | miss, evicts tag 1 (conflict) |

One hit in eight. The same capacity organised as $S=2$ sets of $E=2$ lines with LRU replacement ($s=1$, tags of $3$ bits) gets a second hit, at the second reference to $0$, and evicts only twice: associativity removes the conflict between addresses $0$ and $16$.

:::

::: {#fig-cache-organization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \s/\v/\tg/\bk in {0/1/00/{M[0..3]},1/1/00/{M[4..7]},2/0/{}/{},3/0/{}/{}} {
  \draw[cell frame] (0,-\s*0.6) rectangle (0.5,-\s*0.6+0.5); \node[tick] at (0.25,-\s*0.6+0.25) {\v};
  \draw[cell frame] (0.55,-\s*0.6) rectangle (1.45,-\s*0.6+0.5); \node[tick] at (1.0,-\s*0.6+0.25) {\tg};
  \draw[cell frame] (1.5,-\s*0.6) rectangle (3.5,-\s*0.6+0.5); \node[tick] at (2.5,-\s*0.6+0.25) {\bk};
  \node[tick, anchor=east] at (-0.1,-\s*0.6+0.25) {set \s};
}
\draw[hl cell] (1.5,-0.6) rectangle (3.5,-0.1); \node[tick] at (2.5,-0.35) {M[4..7]};
\node[tick] at (0.25,0.75) {v}; \node[tick] at (1.0,0.75) {tag}; \node[tick] at (2.5,0.75) {block};
\node[lab, anchor=west] at (3.8,-0.35) {last access: 4, a conflict miss};
\node[lab, anchor=west] at (3.8,-1.2) {1 hit, 7 misses, 5 evictions};
\end{tikzpicture}
\end{center}
```

The direct-mapped cache of @exm-cache-trace after the whole trace. Sets 2 and 3 were never used, yet five of the misses evicted a block

:::

::: {#def-write-policies .definition name="Write policies"}

On a write hit, a *write-through* cache updates the next level at once, while a *write-back* cache only updates its own copy and marks the line *dirty*; the block is written to the next level when it is evicted. On a write miss, a *write-allocate* cache loads the block and then writes it, while a *no-write-allocate* cache writes directly to the next level. Lower levels of the hierarchy, where transfers are slow, use write-back with write-allocate.

:::

::: {#exm-core-i7-caches .example name="The caches of a multicore processor"}

A typical Intel Core i7 (Haswell) core has a $32$ KiB 8-way L1 data cache and a separate $32$ KiB L1 instruction cache (access about $4$ cycles), a $256$ KiB 8-way L2 cache (about $10$ cycles), and all cores share an $8$ MiB 16-way L3 cache (about $40$–$75$ cycles). All use $64$-byte blocks. Main memory is a further $200$ cycles or so away.

:::

::: {#rmk-cache-organization-1 name="A simulator counts, it does not store"}

To study a cache's behaviour, it is enough to track for each line its valid bit, its tag and how recently it was used: the data bytes do not affect hits and misses. A cache simulator therefore keeps an array of $S\times E$ such records and, for each address of a trace, reports a hit, a miss, or a miss with an eviction (@prob-cache-simulator-code).

:::
