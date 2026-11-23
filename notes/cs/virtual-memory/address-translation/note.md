---
title: "Address Translation, TLBs and Multi-Level Page Tables"
sources: [cmu15213-17, cmu15213-18]
requires: [cs/virtual-memory/vm-memory-management-and-protection, cs/memory-hierarchy/cache-organization]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 17 "Virtual Memory: Concepts", last part, and Lecture 18 "Virtual Memory: Systems", first part, in our own wording; the small memory system and its translations are our own example; proofs written out in steps. -->

::: {#def-address-translation .definition name="Address translation"}

With $n$-bit virtual addresses, $m$-bit physical addresses and pages of $P=2^p$ bytes, a virtual address splits into a *virtual page number* (VPN, the high $n-p$ bits) and a *virtual page offset* (VPO, the low $p$ bits). The MMU uses the VPN to select a PTE; if it is valid, its *physical page number* (PPN) is concatenated with the offset:
$$\text{VA}=\text{VPN}\,|\,\text{VPO}\ \longmapsto\ \text{PA}=\text{PPN}\,|\,\text{PPO},\qquad \text{PPO}=\text{VPO}.$$

:::

::: {#def-tlb .definition name="Translation lookaside buffer"}

Reading a PTE from memory on every reference would double memory traffic. The *translation lookaside buffer* (TLB) is a small set-associative cache of PTEs inside the MMU, indexed by the VPN: the low bits of the VPN are the *TLB index* (TLBI) and the remaining bits the *TLB tag* (TLBT). A TLB hit translates without touching memory; a TLB miss reads the PTE (from the caches or memory) and stores it in the TLB.

:::

::: {#fig-address-translation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (3.6,0.55); \node[tick] at (1.8,0.275) {VPN};
\draw[cell frame] (3.6,0) rectangle (6,0.55); \node[tick] at (4.8,0.275) {VPO};
\draw[draw=primary] (0,0.65) rectangle (2.4,1.0); \node[tick] at (1.2,0.83) {TLBT};
\draw[draw=accent] (2.4,0.65) rectangle (3.6,1.0); \node[tick] at (3.0,0.83) {TLBI};
\node[lab, anchor=east] at (-0.1,0.275) {virtual address};
\node[hl box] (tlb) at (1.8,-1.3) {TLB / page table:\\VPN $\mapsto$ PPN};
\draw[->] (1.8,0) -- (tlb);
\draw[cell frame] (0.6,-3.0) rectangle (3.6,-2.45); \node[tick] at (2.1,-2.72) {PPN};
\draw[cell frame] (3.6,-3.0) rectangle (6,-2.45); \node[tick] at (4.8,-2.72) {PPO};
\node[lab, anchor=east] at (0.5,-2.72) {physical address};
\draw[->] (tlb) -- (2.1,-2.45);
\draw[->] (4.8,0) -- (4.8,-2.45) node[midway, right, tick] {copied unchanged};
\end{tikzpicture}
\end{center}
```

Translation replaces the virtual page number by a physical page number and keeps the offset; the low bits of the VPN index the TLB

:::

::: {#exm-small-memory-system .example name="Translating in a small memory system"}

Take $n=12$, $m=10$, pages of $32$ bytes ($p=5$): the VPN has $7$ bits and the PPN $5$. The TLB has $4$ sets of $2$ lines (TLBI: low $2$ VPN bits; TLBT: high $5$). Some of its contents, as (tag, PPN, valid):

| set | line 0 | line 1 |
|---|---|---|
| 1 | (`0x09`, `0x07`, 1) | (`0x00`, `0x05`, 1) |
| 2 | (`0x07`, `0x13`, 1) | (`0x0B`, `0x02`, 0) |

and some page table entries: VPN `0x1E` $\mapsto$ PPN `0x13`, VPN `0x26` $\mapsto$ `0x07`, VPN `0x1F` invalid.

1. VA `0x3D4` $=001111\,0\,10100$: VPN `0x1E`, VPO `0x14`; TLBI $=2$, TLBT `0x07`. Set 2 has a valid line with tag `0x07`: TLB hit, PPN `0x13`, so PA $=$ `0x13`$\cdot32+$`0x14` $=$ `0x274`.
2. VA `0x4CA`: VPN `0x26`, VPO `0x0A`; TLBI $=2$, TLBT `0x09`. No match in set 2: TLB miss. The PTE for `0x26` is valid with PPN `0x07`: PA $=$ `0xEA`.
3. VA `0x3E7`: VPN `0x1F`, TLBI $=3$. TLB miss, and the PTE is invalid: a page fault.

:::

::: {#fig-address-translation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \b [count=\i from 0] in {0,0,1,1,1,1,0,1,0,1,0,0} {
  \pgfmathtruncatemacro{\k}{11-\i}
  \draw[cell frame] (\i*0.55,0) rectangle (\i*0.55+0.55,0.55); \node[tick] at (\i*0.55+0.275,0.275) {\b};
  \node[tick] at (\i*0.55+0.275,-0.25) {\k};
}
\draw[draw=primary] (0,0.65) rectangle (5*0.55,1.0); \node[tick] at (2.5*0.55,0.83) {TLBT \texttt{0x07}};
\draw[draw=accent] (5*0.55,0.65) rectangle (7*0.55,1.0); \node[tick] at (6*0.55,0.83) {TLBI 2};
\draw[faint] (7*0.55,-0.1) -- (7*0.55,1.4); \node[tick] at (3.5*0.55,1.3) {VPN \texttt{0x1E}}; \node[tick] at (9.5*0.55,1.3) {VPO \texttt{0x14}};
\node[hl box] at (8.6,0.3) {TLB hit: PPN \texttt{0x13}};
\foreach \b [count=\i from 0] in {1,0,0,1,1,1,0,1,0,0} {
  \draw[cell frame] (\i*0.55+1.1,-1.6) rectangle (\i*0.55+1.65,-1.05); \node[tick] at (\i*0.55+1.375,-1.325) {\b};
}
\node[lab, anchor=east] at (1.0,-1.325) {PA \texttt{0x274}};
\draw[faint] (7*0.55,-1.7) -- (7*0.55,-0.95);
\end{tikzpicture}
\end{center}
```

Translating VA `0x3D4` in @exm-small-memory-system: the VPN's low two bits pick TLB set 2, its tag `0x07` hits, and PPN `0x13` is joined to the unchanged offset

:::

::: {#def-multi-level-page-table .definition name="Multi-level page table"}

A single-level table for a 48-bit address space with 4 KiB pages and 8-byte PTEs needs $2^{36}\cdot8$ bytes $=512$ GiB per process. A *$k$-level page table* splits the VPN into $k$ fields $\text{VPN}_1,\dots,\text{VPN}_k$. A level-$1$ table, one page in size, is always present; entry $\text{VPN}_i$ of a level-$i$ table points to a level-$(i+1)$ table, and the entries of the level-$k$ tables are ordinary PTEs. A null entry at any level means that the whole range below it is unallocated, and the tables below it are not created.

:::

::: {#prp-multi-level-size .proposition name="Multi-level tables are small for sparse address spaces"}

In a two-level table with $2^{a}$ entries per table, a process that uses $u$ contiguous, aligned chunks of $2^{a}$ pages each needs only $1+u$ tables, independent of the size of the address space.

:::

::: {.proof}
1. The level-$1$ table always exists: one table.

2. A level-$2$ table covers exactly one aligned chunk of $2^a$ consecutive virtual pages. It exists only if some page of its chunk is allocated.

3. By assumption exactly $u$ chunks contain allocated pages, so $u$ level-$2$ tables exist. All other level-$1$ entries are null and cost no further memory.
:::

::: {#fig-address-translation-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.45cm]
\node[tick] at (0.8,1.2) {level 1};
\foreach \e/\c [count=\i from 0] in {PT 0/,PT 1/,null/,null/,null/,null/,PT 7/,null/} { \draw[cell frame] (0,-\i) rectangle (1.6,-\i+0.9); \node[tick] at (0.8,-\i+0.45) {\e}; }
\foreach \t/\y [count=\i from 0] in {0/0,1/-3,7/-7} {
  \foreach \k in {0,1,2} { \draw[cell frame] (3.5,\y-\k+0.9) rectangle (5.1,\y-\k); }
  \node[tick] at (4.3,\y+1.3) {level 2, table \t};
  \node[tick] at (4.3,\y-0.55) {PTEs};
}
\draw[map] (1.6,0.45) -- (3.5,0.45); \draw[map] (1.6,-0.55) -- (3.5,-2.55); \draw[map] (1.6,-5.55) -- (3.5,-6.55);
\node[tick, anchor=west] at (5.4,-4.3) {no level-2 tables for the null entries};
\end{tikzpicture}
\end{center}
```

A two-level page table: level-2 tables exist only for the regions of the address space in use

:::

::: {#def-multi-level-translation .definition name="Translation with a $k$-level table"}

The MMU walks the levels: the *page table base register* (CR3 on x86-64) gives the level-$1$ table; field $\text{VPN}_i$ selects an entry of the level-$i$ table, which gives the next table's address; the level-$k$ entry gives the PPN. A TLB hit skips the whole walk, so a deeper table costs extra memory accesses only on TLB misses.

:::

::: {#rmk-address-translation-1 name="Caches see physical addresses"}

The L1 cache is indexed and tagged by physical address, which would seem to put translation before every cache access. x86-64 hides this: an L1 cache of $32$ KiB, $8$-way, $64$-byte blocks has $64$ sets, so its $6$ index and $6$ offset bits are the $12$ low address bits, which are the page offset and need no translation. The cache can select the set while the TLB translates the page number in parallel.

:::
