---
title: "Virtual Memory for Memory Management and Protection"
sources: [cmu15213-17]
requires: [cs/virtual-memory/address-spaces-and-paging]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 17 "Virtual Memory: Concepts", middle part, in our own wording. -->

Besides caching disk pages in DRAM, virtual memory gives each process its own page table, and with it its own address space. This one mechanism simplifies linking, loading, sharing and allocation, and it enforces protection.

::: {#def-per-process-address-space .definition name="One address space per process"}

The operating system keeps a separate page table for each process. The same virtual address in two processes can therefore map to different physical pages, and each process sees the uniform layout of @def-x86-64-linux-layout regardless of where its pages really are.

:::

::: {#fig-vm-memory-management-and-protection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.55cm]
\foreach \n/\x in {1/0,2/7.2} {
  \node[tick] at (\x+0.8,1.1) {process \n};
  \foreach \i in {1,2,3} { \draw[cell frame] (\x,-\i+1) rectangle (\x+1.6,-\i+1.9); \node[tick] at (\x+0.8,-\i+1.45) {VP \i}; }
}
\node[tick] at (4.4,1.1) {physical memory};
\foreach \i in {0,...,6} { \draw[cell frame] (3.6,-\i+0.4) rectangle (5.2,-\i+1.3); \node[tick] at (4.4,-\i+0.85) {PP \i}; }
\draw[regionC] (3.6,-6+0.4) rectangle (5.2,-6+1.3); \node[tick] at (4.4,-6+0.85) {PP 6: shared};
\draw[map] (1.6,0.45) -- (3.6,-0.15); \draw[map] (1.6,-0.55) -- (3.6,-2.15); \draw[map, draw=secondary] (1.6,-1.55) -- (3.6,-5.15);
\draw[map] (7.2,0.45) -- (5.2,-1.15); \draw[map] (7.2,-0.55) -- (5.2,-4.15); \draw[map, draw=secondary] (7.2,-1.55) -- (5.2,-5.15);
\end{tikzpicture}
\end{center}
```

Two processes with their own page tables: their pages go to different physical pages, except a shared page (green), such as library code, that both map

:::

::: {#prp-vm-simplifies .proposition name="What per-process address spaces simplify"}

1. *Linking*: every program can be linked to the same fixed addresses (code at `0x400000`, stack at the top), whatever physical memory it gets.
2. *Loading*: the loader only creates PTEs for the code and data segments, marked uncached; the pages are brought in by page faults when first used (@def-page-fault).
3. *Sharing*: mapping a virtual page of several processes to one physical page shares it, for example the code of the C library (@def-shared-object).
4. *Allocation*: a contiguous range of $k$ virtual pages can be backed by any $k$ physical pages, so a process can grow its heap without the physical pages being contiguous.

:::

::: {.proof}
Each item is a consequence of translating every address through a table that the kernel controls. The program's addresses never change; only the table entries do, and the kernel chooses them independently for each page and each process.
:::

::: {#def-page-permission-bits .definition name="Page permission bits"}

Each PTE also carries permission bits that the MMU checks on every access: *SUP* (the page may be accessed only in kernel mode), *READ*, *WRITE*, and on x86-64 *XD* (execute disable). An access that violates them raises a fault, and the kernel normally sends the process `SIGSEGV`, reported as a "segmentation fault".

:::

::: {#exm-permissions .example name="Using the permission bits"}

The code segment is mapped READ and not WRITE, so a stray store into the program's own instructions is caught. The stack and heap are mapped XD, so the code-injection attack of @def-code-injection faults instead of running. Kernel memory is mapped SUP in every process, so user code cannot read or change it, yet a system call needs no change of page table to reach it.

:::

::: {#fig-vm-memory-management-and-protection-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.55cm]
\foreach \h [count=\j from 0] in {SUP,READ,WRITE,XD,address} { \node[tick] at (\j*1.1+0.55,0.6) {\h}; }
\foreach \r/\a/\b/\c/\d/\e [count=\i from 0] in {VP 0/no/yes/no/no/PP 6,VP 1/no/yes/yes/yes/PP 4,VP 2/yes/yes/yes/yes/PP 2} {
  \node[tick, anchor=east] at (-0.1,-\i-0.45) {\r};
  \foreach \v [count=\j from 0] in {\a,\b,\c,\d,\e} { \draw[cell frame] (\j*1.1,-\i) rectangle (\j*1.1+1.1,-\i-0.9); \node[tick] at (\j*1.1+0.55,-\i-0.45) {\v}; }
}
\node[tick, anchor=west] at (5.8,-0.45) {code: read-only, executable};
\node[tick, anchor=west] at (5.8,-1.45) {data: read/write, not executable};
\node[tick, anchor=west] at (5.8,-2.45) {kernel only};
\end{tikzpicture}
\end{center}
```

Page table entries with permission bits; the MMU checks them on every access

:::
