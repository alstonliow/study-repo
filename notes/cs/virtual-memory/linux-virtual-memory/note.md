---
title: "Linux Virtual Memory and Memory Mapping"
sources: [cmu15213-18]
requires: [cs/virtual-memory/address-translation, cs/exceptional-control-flow/process-control]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 18 "Virtual Memory: Systems", in our own wording. -->

::: {#def-x86-64-paging .definition name="Four-level paging on x86-64"}

Current x86-64 processors use $48$-bit virtual addresses, $4$ KiB pages and $8$-byte PTEs. A page-sized table therefore holds $512=2^9$ entries, and the $36$-bit VPN splits into four $9$-bit fields $\text{VPN}_1,\dots,\text{VPN}_4$, one per level of the page table (@def-multi-level-page-table). Besides the address, each entry holds the valid (present) bit, the permission bits (@def-page-permission-bits), a *reference* bit set by hardware on every access and a *dirty* bit set on every write, which the kernel's replacement policy uses.

:::

::: {#fig-linux-virtual-memory-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \f/\w [count=\i from 0] in {VPN 1/9,VPN 2/9,VPN 3/9,VPN 4/9,VPO/12} {
  \draw[cell frame] (\i*1.8,0) rectangle (\i*1.8+1.8,0.55); \node[tick] at (\i*1.8+0.9,0.275) {\f\ (\w)};
}
\node[box] (c) at (-1.4,-1.4) {CR3};
\foreach \i in {0,...,3} {
  \pgfmathtruncatemacro{\l}{\i+1}
  \node[box] (t\i) at (\i*1.8+0.9,-1.4) {L\l\ table};
  \draw[->] (\i*1.8+0.9,0) -- (t\i);
}
\draw[->] (c) -- (t0); \draw[->] (t0) -- (t1); \draw[->] (t1) -- (t2); \draw[->] (t2) -- (t3);
\node[hl box] (pa) at (7.2,-2.8) {PPN | PPO};
\draw[->] (t3) -- (pa); \draw[->] (8.1,0) -- (8.1,-2.45);
\end{tikzpicture}
\end{center}
```

A page walk on x86-64: CR3 points to the level-1 table, each 9-bit field indexes one level, and the level-4 entry gives the physical page number

:::

::: {#def-linux-areas .definition name="Areas of a Linux process"}

Linux describes a process's virtual memory as a list of *areas* (segments): contiguous ranges of allocated pages such as code, data, heap, a shared library or the user stack. Each area has a start, an end, permissions, and a flag saying whether it is private or shared. Pages outside every area are unallocated. The kernel keeps one structure (`mm_struct`) per process, pointing to the level-1 table and to the list of areas.

:::

::: {#def-linux-page-fault-handling .definition name="Linux page fault handling"}

On a page fault at address $A$ the kernel checks, in order:

1. Is $A$ inside some area? If not, the reference is to an unallocated page: send `SIGSEGV`.
2. Is the access allowed by the area's permissions (a write to a read-only area, user access to a kernel area)? If not: send `SIGSEGV`, a protection fault.
3. Otherwise the fault is legal: choose a victim page, load the page for $A$, update the page table and restart the instruction.

:::

::: {#fig-linux-virtual-memory-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.6cm]
\foreach \a/\y in {stack/4,shared libraries/2.5,heap/1,data/0,text/-1} { \draw[regionA] (0,\y) rectangle (3,\y+0.8); \node[tick] at (1.5,\y+0.4) {\a}; }
\node[hl dot] at (3.6,3.3) {}; \node[tick, anchor=west] at (3.8,3.3) {1: outside every area, \texttt{SIGSEGV}};
\node[hl dot] at (3.6,-0.6) {}; \node[tick, anchor=west] at (3.8,-0.6) {2: write to read-only text, \texttt{SIGSEGV}};
\node[dot] at (3.6,1.4) {}; \node[tick, anchor=west] at (3.8,1.4) {3: legal, load the page};
\end{tikzpicture}
\end{center}
```

Three kinds of page fault, distinguished by the list of areas

:::

::: {#def-memory-mapping .definition name="Memory mapping"}

Linux initialises an area by *mapping* it to an object on disk:

- a *regular file*: the area's pages are taken from consecutive pages of the file, loaded on demand;
- an *anonymous file*: pages are created full of zeros on first touch (*demand-zero* pages), used for the heap, the stack and `.bss`.

Once a page has been modified it is backed by *swap space* on disk. `void *mmap(void *start, size_t len, int prot, int flags, int fd, off_t off)` asks the kernel for such a mapping; `munmap` removes it.

:::

::: {#def-shared-object .definition name="Shared and private objects"}

An object mapped as *shared* is seen by every process that maps it: a write by one is visible to all, and is written back to the file. An object mapped as *private* is seen only by the process: its writes are not visible to others or to the file. Many processes can map the same shared object, such as the code of the C library, and only one copy exists in physical memory.

:::

::: {#def-copy-on-write .definition name="Copy-on-write"}

Two processes that map the same private object initially share its physical pages, which are marked read-only in both page tables with the area flagged *private copy-on-write*. When one of them writes to such a page, the protection fault handler copies the page, maps the copy writable into the writer's page table, and restarts the write. Pages are copied only if and when they are written.

:::

::: {#fig-linux-virtual-memory-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0) rectangle (1.6,2); \node[tick] at (0.8,2.25) {process 1};
\draw[regionA] (5,0) rectangle (6.6,2); \node[tick] at (5.8,2.25) {process 2};
\draw[cell frame] (2.5,1.3) rectangle (4.1,1.8); \node[tick] at (3.3,1.55) {page (read-only)};
\draw[hl cell] (2.5,0.2) rectangle (4.1,0.7); \node[tick] at (3.3,0.45) {copy};
\draw[map] (1.6,1.6) -- (2.5,1.55); \draw[map] (5,1.6) -- (4.1,1.55);
\draw[map, draw=accent] (5,0.5) -- (4.1,0.45);
\node[tick, anchor=west] at (6.8,0.5) {after process 2 writes};
\end{tikzpicture}
\end{center}
```

Copy-on-write: both processes share a read-only page until process 2 writes it; the fault handler gives process 2 its own copy

:::

::: {#exm-fork-execve-vm .example name="`fork` and `execve` revisited"}

`fork` creates the child's `mm_struct`, areas and page tables as copies of the parent's, marks every page read-only in both and flags every private area copy-on-write. So `fork` is fast, and each process later gets its own copy of exactly the pages it writes. `execve` deletes the old areas and creates new ones: private copy-on-write areas mapped to the code and data of the executable file, demand-zero areas for `.bss`, heap and stack, and shared areas for the shared libraries; then it sets the program counter to the entry point. No page is read from disk until it is touched.

:::
