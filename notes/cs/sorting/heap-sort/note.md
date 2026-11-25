---
title: "Heap Sort"
sources: [mit6006-8, mit6006r-8]
requires: [cs/sorting/comparison-sorting, cs/data-structures/binary-heaps]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 8 and Recitation 8, in our own wording; proofs written out in steps. Moved from cs/data-structures/binary-heaps on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Priority queue sort with a binary heap (@def-max-heap) kept inside the array being sorted.

::: {#def-heap-sort .definition name="Heap sort"}

*Heap sort* of an array $A$ of length $n$: treat a prefix $A[0..s-1]$ as a max-heap, with $s=0$ at first. Insert $A[s]$ for $s=0,\dots,n-1$ (grow the prefix by one and heapify up). Then $n$ times delete the maximum: swap $A[0]$ with $A[s-1]$, shrink the prefix by one and heapify down. The removed maxima fill the array from the end, so $A$ ends up sorted.

:::

```{=latex}
\begin{algorithm}
\caption{Heap sort}
\begin{algorithmic}
\INPUT Array $A[0..n-1]$
\OUTPUT $A$ sorted in place
\FOR{$s=1$ to $n$}
    \STATE heapify up from $s-1$ in the heap $A[0..s-1]$ \COMMENT{insert $A[s-1]$}
\ENDFOR
\FOR{$s=n$ down to $2$}
    \STATE swap $A[0]$ and $A[s-1]$ \COMMENT{the maximum goes to its final place}
    \STATE heapify down from $0$ in the heap $A[0..s-2]$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#fig-binary-heaps-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$2$};
\node[lab,tick] at (0.275,-0.180) {0};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$9$};
\node[lab,tick] at (0.825,-0.180) {1};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$4$};
\node[lab,tick] at (1.375,-0.180) {2};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$7$};
\node[lab,tick] at (1.925,-0.180) {3};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$1$};
\node[lab,tick] at (2.475,-0.180) {4};
\node[lab,tick,anchor=west] at (3.05,0.28) {input};
\draw[cell frame] (0.000,-0.720) rectangle (0.550,-0.170);
\node[lab] at (0.275,-0.445) {$9$};
\draw[cell frame] (0.550,-0.720) rectangle (1.100,-0.170);
\node[lab] at (0.825,-0.445) {$7$};
\draw[cell frame] (1.100,-0.720) rectangle (1.650,-0.170);
\node[lab] at (1.375,-0.445) {$4$};
\draw[cell frame] (1.650,-0.720) rectangle (2.200,-0.170);
\node[lab] at (1.925,-0.445) {$2$};
\draw[cell frame] (2.200,-0.720) rectangle (2.750,-0.170);
\node[lab] at (2.475,-0.445) {$1$};
\draw[emph] (2.75,-0.80) -- (2.75,-0.09);
\node[lab,tick,anchor=west] at (3.05,-0.44) {after inserting all: a max-heap};
\draw[cell frame] (0.000,-1.440) rectangle (0.550,-0.890);
\node[lab] at (0.275,-1.165) {$7$};
\draw[cell frame] (0.550,-1.440) rectangle (1.100,-0.890);
\node[lab] at (0.825,-1.165) {$2$};
\draw[cell frame] (1.100,-1.440) rectangle (1.650,-0.890);
\node[lab] at (1.375,-1.165) {$4$};
\draw[cell frame] (1.650,-1.440) rectangle (2.200,-0.890);
\node[lab] at (1.925,-1.165) {$1$};
\draw[hl cell] (2.200,-1.440) rectangle (2.750,-0.890);
\node[lab] at (2.475,-1.165) {$9$};
\draw[emph] (2.20,-1.52) -- (2.20,-0.81);
\node[lab,tick,anchor=west] at (3.05,-1.17) {move max to index $4$, heapify down};
\draw[cell frame] (0.000,-2.160) rectangle (0.550,-1.610);
\node[lab] at (0.275,-1.885) {$4$};
\draw[cell frame] (0.550,-2.160) rectangle (1.100,-1.610);
\node[lab] at (0.825,-1.885) {$2$};
\draw[cell frame] (1.100,-2.160) rectangle (1.650,-1.610);
\node[lab] at (1.375,-1.885) {$1$};
\draw[hl cell] (1.650,-2.160) rectangle (2.200,-1.610);
\node[lab] at (1.925,-1.885) {$7$};
\draw[hl cell] (2.200,-2.160) rectangle (2.750,-1.610);
\node[lab] at (2.475,-1.885) {$9$};
\draw[emph] (1.65,-2.24) -- (1.65,-1.53);
\node[lab,tick,anchor=west] at (3.05,-1.89) {move max to index $3$, heapify down};
\draw[cell frame] (0.000,-2.880) rectangle (0.550,-2.330);
\node[lab] at (0.275,-2.605) {$2$};
\draw[cell frame] (0.550,-2.880) rectangle (1.100,-2.330);
\node[lab] at (0.825,-2.605) {$1$};
\draw[hl cell] (1.100,-2.880) rectangle (1.650,-2.330);
\node[lab] at (1.375,-2.605) {$4$};
\draw[hl cell] (1.650,-2.880) rectangle (2.200,-2.330);
\node[lab] at (1.925,-2.605) {$7$};
\draw[hl cell] (2.200,-2.880) rectangle (2.750,-2.330);
\node[lab] at (2.475,-2.605) {$9$};
\draw[emph] (1.10,-2.96) -- (1.10,-2.25);
\node[lab,tick,anchor=west] at (3.05,-2.60) {move max to index $2$, heapify down};
\draw[cell frame] (0.000,-3.600) rectangle (0.550,-3.050);
\node[lab] at (0.275,-3.325) {$1$};
\draw[hl cell] (0.550,-3.600) rectangle (1.100,-3.050);
\node[lab] at (0.825,-3.325) {$2$};
\draw[hl cell] (1.100,-3.600) rectangle (1.650,-3.050);
\node[lab] at (1.375,-3.325) {$4$};
\draw[hl cell] (1.650,-3.600) rectangle (2.200,-3.050);
\node[lab] at (1.925,-3.325) {$7$};
\draw[hl cell] (2.200,-3.600) rectangle (2.750,-3.050);
\node[lab] at (2.475,-3.325) {$9$};
\draw[emph] (0.55,-3.68) -- (0.55,-2.97);
\node[lab,tick,anchor=west] at (3.05,-3.32) {move max to index $1$, heapify down};
\end{tikzpicture}
\end{center}
```

Heap sort of $2,9,4,7,1$ in place. The bold bar separates the heap prefix from the sorted suffix (highlighted). Inserting the items one by one gives the max-heap $9,7,4,2,1$; then each step swaps the maximum $A[0]$ to the end of the heap, shrinks the heap by one and heapifies down. This is priority queue sort with the queue living inside the array.

:::

Heap sort is in place and runs in $O(n\log n)$ time; it is not stable. The first phase can also be done by building the heap in linear time (@thm-build-heap).
