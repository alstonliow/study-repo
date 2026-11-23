---
title: "Storage Technologies"
sources: [cmu15213-11, cmu15213r-7]
requires: [cs/data-representation/byte-ordering]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 11 "The Memory Hierarchy" and Recitation 7 (SRAM versus DRAM), in our own wording. -->

A program sees memory as one flat array of bytes (@def-byte-addressable-memory). Physically, the bytes live in devices whose speeds differ by factors of a million. This note describes the devices; @sec-cs-memory-hierarchy-caching-in-the-hierarchy explains how a system hides the differences.

::: {#def-sram-dram .definition name="SRAM and DRAM"}

*Random-access memory* (RAM) loses its contents without power and reads any location in about the same time.

- *SRAM* (static RAM) stores each bit in a cell of about six transistors that holds its value as long as power is on. It is fast (around a nanosecond) but large per bit and expensive; it is used for caches.
- *DRAM* (dynamic RAM) stores each bit as charge in a capacitor with one transistor. It is dense and cheap but slower (tens of nanoseconds), and its cells leak, so they must be *refreshed* every few tens of milliseconds; it is used for main memory.

:::

::: {#def-dram-organization .definition name="DRAM organization"}

A DRAM chip is a grid of *supercells*, each holding a few bits (often 8), addressed by a row and a column. A read sends the row address (the whole row is copied into an internal *row buffer*), then the column address (the supercell is taken from the buffer). A *memory module* combines eight chips: to read the 8-byte word at one address, each chip supplies one byte of the same supercell position, and the memory controller assembles the bytes.

:::

::: {#fig-storage-technologies-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.55]
\foreach \r in {0,...,3} { \foreach \c in {0,...,3} { \draw[cell frame] (\c,-\r) rectangle (\c+1,-\r-1); } }
\path[tintB] (0,-2) rectangle (4,-3);
\draw[hl cell] (1,-2) rectangle (2,-3);
\node[tick] at (2,0.5) {columns 0--3};
\node[tick, anchor=east] at (-0.2,-2.5) {row 2};
\foreach \c in {0,...,3} { \draw[cell frame] (\c,-5) rectangle (\c+1,-6); }
\path[tintB] (0,-5) rectangle (4,-6);
\node[tick, anchor=east] at (-0.2,-5.5) {row buffer};
\draw[map] (2,-4.1) -- (2,-4.9);
\draw[map, draw=accent] (1.5,-6.1) -- (1.5,-7.2);
\node[tick] at (1.5,-7.6) {supercell (2,1) to the controller};
\node[lab, anchor=west] at (5,-1) {1. row address: copy row 2};
\node[lab, anchor=west] at (5,-2.2) {2. column address: pick column 1};
\end{tikzpicture}
\end{center}
```

Reading supercell $(2,1)$ of a $4\times4$ DRAM: the row address copies a whole row into the row buffer, the column address selects one supercell from it

:::

::: {#def-memory-bus .definition name="Buses and the memory read"}

The CPU reaches main memory through a chain of *buses*: the *system bus* from the CPU chip to an *I/O bridge*, and the *memory bus* from the bridge to main memory. A load `movq A, %rax` that misses the caches puts address $A$ on the bus, main memory returns the word at $A$ on the bus, and the CPU copies it into `%rax`. One such transaction takes on the order of $50$–$100$ ns, hundreds of clock cycles.

:::

::: {#def-disk-geometry .definition name="Rotating disk"}

A *disk* stores bits magnetically on *platters* that spin at a constant rate (typically $5\,400$–$15\,000$ revolutions per minute). Each surface is divided into concentric *tracks*, and each track into *sectors* of typically $512$ bytes separated by gaps. An *arm* moves the read/write head to a track. The *access time* of a sector is
$$T_{\text{access}}=T_{\text{seek}}+T_{\text{rotation}}+T_{\text{transfer}},$$
the time to move the arm to the track, to wait for the sector to come under the head (on average half a revolution), and to read it.

:::

::: {#fig-storage-technologies-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r in {0.6,1.0,1.4,1.8} { \draw[faint] (0,0) circle (\r); }
\draw[regionA] (0,0) circle (0.25);
\draw[hl] (1.4,0) arc (0:30:1.4);
\foreach \a in {0,30,...,330} { \draw[faint] ({0.6*cos(\a)},{0.6*sin(\a)}) -- ({1.8*cos(\a)},{1.8*sin(\a)}); }
\draw[emph] (3.6,-1.4) -- (1.45,0.45); \node[dot] at (1.45,0.45) {};
\node[lab, anchor=west] at (3.6,-1.4) {arm and head};
\node[lab, anchor=west] at (2.2,1.6) {track};
\draw[->, faint] (2.2,1.6) -- (1.75,0.9);
\node[lab, anchor=west] at (2.4,0.6) {sector};
\draw[->] (2.4,0.6) -- (1.35,0.35);
\draw[->] (-1.2,1.9) arc (120:150:2.2); \node[tick] at (-1.7,2.0) {spin};
\end{tikzpicture}
\end{center}
```

One disk surface: concentric tracks divided into sectors; the arm moves the head across tracks while the platter spins

:::

::: {#exm-disk-access-time .example name="Access time of a disk sector"}

Take $7\,200$ RPM, an average seek of $9$ ms, and $400$ sectors per track. One revolution takes $60/7200$ s $=8.33$ ms, so the average rotational latency is $\tfrac12\cdot8.33\approx4.17$ ms and the transfer of one sector is $8.33/400\approx0.02$ ms. The access time is about $9+4.17+0.02\approx13.2$ ms. Seek and rotation dominate; once the head is in place, the bytes of a sector are almost free. Compared with about $50$ ns for DRAM, the first byte of a sector costs some $260\,000$ times as long.

:::

::: {#def-ssd .definition name="Solid-state disk"}

A *solid-state disk* (SSD) stores data in flash memory, organised in *pages* of $512$ bytes to $4$ KiB grouped into *blocks* of $32$–$128$ pages. Data is read and written in pages, but a page can be written only after its whole block has been erased, and a block wears out after about $100\,000$ erasures. A *flash translation layer* in the drive hides this. Reads take tens of microseconds; random writes are slower because they may need a block to be copied and erased.

:::

::: {#fig-storage-technologies-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.15cm]
\draw[->] (0,0) -- (8.6,0) node[lab, right] {access time};
\foreach \e/\l in {0/{1 ns},2/{100 ns},4/{10 $\mu$s},6/{1 ms},8/{100 ms}} { \draw (\e,-0.08) -- (\e,0.08); \node[tick] at (\e,-0.35) {\l}; }
\foreach \x/\n in {0.0/register,0.6/SRAM cache,1.7/DRAM,3.7/SSD read,6.9/disk} { \node[dot] at (\x,0) {}; \node[tick, rotate=40, anchor=south west] at (\x,0.12) {\n}; }
\end{tikzpicture}
\end{center}
```

Typical access times on a logarithmic scale (each tick a factor of $100$): from registers to disk spans about seven orders of magnitude

:::

::: {#rmk-storage-technologies-1 name="The growing gap"}

For decades processor cycle times shrank much faster than DRAM and disk access times, and since about 2005 clock rates have stopped rising while the number of cores per chip grows instead. Either way, the processor can use data far faster than main memory or storage can supply it. Programs are fast only if most of their accesses are served by the small fast memories near the processor, which works because of locality (@def-locality).

:::
