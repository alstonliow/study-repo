---
title: "Address Spaces and Paging"
sources: [cmu15213-17]
requires: [cs/memory-hierarchy/caching-in-the-hierarchy, cs/exceptional-control-flow/exceptions]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 17 "Virtual Memory: Concepts", first part, in our own wording; proofs written out in steps. -->

::: {#def-address-spaces .definition name="Physical and virtual addressing"}

An *address space* is an ordered set of nonnegative integer addresses. The *physical address space* $\{0,\dots,M-1\}$ numbers the $M$ bytes of main memory. With *virtual addressing*, the CPU generates addresses in a *virtual address space* $\{0,\dots,N-1\}$, $N=2^n$, and a hardware unit on the CPU chip, the *memory management unit* (MMU), *translates* each one to a physical address before main memory sees it.

:::

::: {#fig-address-spaces-and-paging-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (cpu) at (0,0) {CPU};
\node[hl box] (mmu) at (2.6,0) {MMU};
\draw[->] (cpu) -- (mmu) node[midway, above, tick] {VA \texttt{0x4100}};
\foreach \i in {0,...,7} { \draw[cell frame] (6,1.6-\i*0.45) rectangle (7.6,2.0-\i*0.45); \node[tick, anchor=east] at (5.9,1.8-\i*0.45) {\i}; }
\draw[hl cell] (6,1.6-4*0.45) rectangle (7.6,2.0-4*0.45);
\draw[->] (mmu) -- (6,1.8-4*0.45) node[midway, above, tick] {PA \texttt{4}};
\node[tick] at (6.8,2.3) {main memory};
\draw[->, dashed] (6.8,1.6-7*0.45) to[out=180,in=-60] (cpu.south) node[pos=0.2, below, tick] {data word};
\end{tikzpicture}
\end{center}
```

Virtual addressing: the MMU translates the virtual address the CPU issues into the physical address that main memory uses

:::

::: {#def-vm-as-cache .definition name="Virtual memory as a cache"}

The virtual address space is divided into *virtual pages* of $P=2^p$ bytes, physical memory into *physical pages* (page frames) of the same size. The virtual pages of a program live on disk; main memory (DRAM) is a cache for them. At any time each virtual page is either

- *unallocated*: not used by the program, with no data on disk;
- *cached*: allocated and currently in a physical page;
- *uncached*: allocated but only on disk.

:::

::: {#def-page-table .definition name="Page table"}

A *page table* is an array, kept in physical memory by the operating system, with one *page table entry* (PTE) per virtual page. A PTE holds a *valid bit* and an address: if valid is $1$, the physical page number where the virtual page is cached; if valid is $0$, the location of the page on disk, or null if it is unallocated. The MMU reads the page table on every translation.

:::

::: {#fig-address-spaces-and-paging-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.5cm]
\node[tick] at (1,1.2) {page table};
\foreach \v/\a [count=\i from 0] in {0/null,1/PP 1,1/PP 0,0/disk,1/PP 3,0/null,0/disk,1/PP 2} {
  \draw[cell frame] (0,-\i) rectangle (0.5,-\i+0.9); \node[tick] at (0.25,-\i+0.45) {\v};
  \draw[cell frame] (0.5,-\i) rectangle (2,-\i+0.9); \node[tick] at (1.25,-\i+0.45) {\a};
  \node[tick, anchor=east] at (-0.1,-\i+0.45) {VP \i};
}
\node[tick] at (5,1.2) {DRAM};
\foreach \p/\c [count=\i from 0] in {0/VP 2,1/VP 1,2/VP 7,3/VP 4} { \draw[regionA] (4.2,-\i*1.3) rectangle (5.8,-\i*1.3+1.1); \node[tick] at (5,-\i*1.3+0.55) {PP \p: \c}; }
\node[tick] at (8.4,1.2) {disk};
\foreach \c [count=\i from 0] in {VP 1,VP 2,VP 3,VP 4,VP 6,VP 7} { \draw[cell frame] (7.6,-\i*0.95) rectangle (9.2,-\i*0.95+0.85); \node[tick] at (8.4,-\i*0.95+0.42) {\c}; }
\draw[map] (2,-0.55) -- (4.2,-0.75);
\draw[map] (2,-1.55) -- (4.2,0.05);
\draw[map] (2,-3.55) -- (4.2,-3.35);
\draw[map] (2,-6.55) -- (4.2,-2.05);
\draw[map, dashed] (2,-2.55) to[out=-10,in=180] (7.6,-1.48);
\draw[map, dashed] (2,-5.55) to[out=-10,in=180] (7.6,-4.33);
\end{tikzpicture}
\end{center}
```

A page table for eight virtual pages: four are cached in DRAM, two are only on disk (valid $0$, disk address), two are unallocated (null)

:::

::: {#def-page-fault .definition name="Page hit and page fault"}

A reference to a word in a cached virtual page is a *page hit*: the MMU finds a valid PTE and forms the physical address. A reference to an uncached page is a *page fault*: the MMU raises a fault exception (@def-exception-classes), and the kernel's page fault handler picks a *victim* physical page, writes it back to disk if it was modified, loads the requested page in its place, updates both PTEs, and returns; the faulting instruction is restarted and now hits. Loading a page only when it is first referenced is *demand paging*.

:::

::: {#fig-address-spaces-and-paging-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (p) at (0,0) {CPU references\\VP 3 (valid 0)};
\node[hl box] (f) at (3.4,0) {page fault\\exception};
\node[box] (h) at (6.8,0) {handler: evict VP 4,\\load VP 3 into PP 3};
\node[box] (r) at (6.8,-1.6) {update both PTEs,\\return};
\node[box] (a) at (3.4,-1.6) {restart instruction:\\page hit};
\draw[->] (p) -- (f); \draw[->] (f) -- (h); \draw[->] (h) -- (r); \draw[->] (r) -- (a);
\end{tikzpicture}
\end{center}
```

Handling a page fault in the page table above: a victim page is evicted, the missing page is brought in, and the instruction runs again

:::

::: {#rmk-address-spaces-and-paging-1 name="Design forced by the miss penalty"}

A miss in DRAM costs about $10^5$ times a hit (@exm-disk-access-time), so a page cache uses large pages (4–8 KiB), lets any virtual page occupy any physical page (fully associative), chooses victims by an elaborate policy in software, and writes pages back only when they are evicted. Each choice minimises the number or the cost of misses at the price of extra work per miss, and that price is negligible against the disk time. Large pages amortise the seek and rotation time over many bytes (@def-disk-geometry); full associativity removes conflict misses (@def-kinds-of-misses); a software replacement policy can be smarter than a hardware one because it has milliseconds to decide; and writing through to disk on every store would make every store as slow as a disk access.

:::

::: {#def-working-set .definition name="Working set and thrashing"}

The *working set* of a program is the set of pages it references during a phase. If the working set fits in physical memory, after the initial misses the program runs with page hits only. If the combined working sets exceed physical memory, pages are swapped in and out continuously and the program slows by orders of magnitude: this is *thrashing*.

:::
