---
title: "Selection Sort and Insertion Sort"
sources: [mit6006-3, mit6006r-3]
requires: [cs/sorting/comparison-sorting]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 3 and Recitation 3, in our own wording; proofs written out in steps. Algorithms are described in words, not copied code. Split from cs/sorting/comparison-sorting on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Two simple sorts that solve the sorting problem (@def-sorting-problem) in quadratic time.

::: {#def-selection-sort .definition name="Selection sort"}

*Selection sort* of $A[0..i]$: if $i>0$, find the index $j$ of a largest item of $A[0..i]$, swap $A[j]$ and $A[i]$, and selection sort $A[0..i-1]$.

:::

```{=latex}
\begin{algorithm}
\caption{Selection sort}
\begin{algorithmic}
\INPUT Array $A[0..n-1]$
\OUTPUT $A$ sorted in place
\FOR{$i=n-1$ down to $1$}
    \STATE $j\gets$ an index of a largest item of $A[0..i]$
    \STATE swap $A[j]$ and $A[i]$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#def-insertion-sort .definition name="Insertion sort"}

*Insertion sort* of $A[0..i]$: if $i>0$, insertion sort $A[0..i-1]$, then *insert* $A[i]$: while it is smaller than its left neighbour, swap it with that neighbour.

:::

```{=latex}
\begin{algorithm}
\caption{Insertion sort}
\begin{algorithmic}
\INPUT Array $A[0..n-1]$
\OUTPUT $A$ sorted in place
\FOR{$i=1$ to $n-1$}
    \STATE $j\gets i$
    \WHILE{$j>0$ and $A[j]<A[j-1]$}
        \STATE swap $A[j]$ and $A[j-1]$; $j\gets j-1$
    \ENDWHILE
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-selection-insertion-sort .theorem name="Selection and insertion sort"}

Both algorithms sort $A$ in place, in $\Theta(n^2)$ time in the worst case. Insertion sort is stable.

:::

::: {.proof}

1. *Selection sort is correct*, by induction on $i$. One item is sorted. For $i>0$, the item moved to position $i$ is a largest one, which is a correct last item of a sorted order of $A[0..i]$, and $A[0..i-1]$ is then sorted by induction.

2. *Insertion sort is correct*, by induction on $i$. After $A[0..i-1]$ is sorted, the swaps move $A[i]$ left past exactly the items larger than it and stop at the first item that is not larger, so $A[0..i]$ is sorted. Equal items are never swapped past each other, so the sort is stable.

3. *Time.* Finding a largest item of $A[0..i]$ takes $\Theta(i)$ comparisons, and inserting $A[i]$ takes up to $i$ swaps (exactly $i$ when the input is in decreasing order). Both satisfy $T(n)=T(n-1)+\Theta(n)$, so $T(n)=\Theta\bigl(\sum_{i=1}^ni\bigr)=\Theta(n^2)$.

4. Both use only a constant number of extra words (written as loops instead of recursion), so they are in place.

:::

::: {#fig-comparison-sorting-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (1.4,0.9) {selection sort};
\node[lab] at (6.4,0.9) {insertion sort};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$7$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$3$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$5$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$1$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$4$};
\draw[cell frame] (0.000,-0.750) rectangle (0.550,-0.200);
\node[lab] at (0.275,-0.475) {$4$};
\draw[cell frame] (0.550,-0.750) rectangle (1.100,-0.200);
\node[lab] at (0.825,-0.475) {$3$};
\draw[cell frame] (1.100,-0.750) rectangle (1.650,-0.200);
\node[lab] at (1.375,-0.475) {$5$};
\draw[cell frame] (1.650,-0.750) rectangle (2.200,-0.200);
\node[lab] at (1.925,-0.475) {$1$};
\draw[hl cell] (2.200,-0.750) rectangle (2.750,-0.200);
\node[lab] at (2.475,-0.475) {$7$};
\draw[faint] (2.20,-0.80) -- (2.20,-0.15);
\draw[cell frame] (0.000,-1.500) rectangle (0.550,-0.950);
\node[lab] at (0.275,-1.225) {$4$};
\draw[cell frame] (0.550,-1.500) rectangle (1.100,-0.950);
\node[lab] at (0.825,-1.225) {$3$};
\draw[cell frame] (1.100,-1.500) rectangle (1.650,-0.950);
\node[lab] at (1.375,-1.225) {$1$};
\draw[hl cell] (1.650,-1.500) rectangle (2.200,-0.950);
\node[lab] at (1.925,-1.225) {$5$};
\draw[cell frame] (2.200,-1.500) rectangle (2.750,-0.950);
\node[lab] at (2.475,-1.225) {$7$};
\draw[faint] (1.65,-1.55) -- (1.65,-0.90);
\draw[cell frame] (0.000,-2.250) rectangle (0.550,-1.700);
\node[lab] at (0.275,-1.975) {$1$};
\draw[cell frame] (0.550,-2.250) rectangle (1.100,-1.700);
\node[lab] at (0.825,-1.975) {$3$};
\draw[hl cell] (1.100,-2.250) rectangle (1.650,-1.700);
\node[lab] at (1.375,-1.975) {$4$};
\draw[cell frame] (1.650,-2.250) rectangle (2.200,-1.700);
\node[lab] at (1.925,-1.975) {$5$};
\draw[cell frame] (2.200,-2.250) rectangle (2.750,-1.700);
\node[lab] at (2.475,-1.975) {$7$};
\draw[faint] (1.10,-2.30) -- (1.10,-1.65);
\draw[cell frame] (0.000,-3.000) rectangle (0.550,-2.450);
\node[lab] at (0.275,-2.725) {$1$};
\draw[hl cell] (0.550,-3.000) rectangle (1.100,-2.450);
\node[lab] at (0.825,-2.725) {$3$};
\draw[cell frame] (1.100,-3.000) rectangle (1.650,-2.450);
\node[lab] at (1.375,-2.725) {$4$};
\draw[cell frame] (1.650,-3.000) rectangle (2.200,-2.450);
\node[lab] at (1.925,-2.725) {$5$};
\draw[cell frame] (2.200,-3.000) rectangle (2.750,-2.450);
\node[lab] at (2.475,-2.725) {$7$};
\draw[faint] (0.55,-3.05) -- (0.55,-2.40);
\draw[cell frame] (5.000,0.000) rectangle (5.550,0.550);
\node[lab] at (5.275,0.275) {$7$};
\draw[cell frame] (5.550,0.000) rectangle (6.100,0.550);
\node[lab] at (5.825,0.275) {$3$};
\draw[cell frame] (6.100,0.000) rectangle (6.650,0.550);
\node[lab] at (6.375,0.275) {$5$};
\draw[cell frame] (6.650,0.000) rectangle (7.200,0.550);
\node[lab] at (6.925,0.275) {$1$};
\draw[cell frame] (7.200,0.000) rectangle (7.750,0.550);
\node[lab] at (7.475,0.275) {$4$};
\draw[hl cell] (5.000,-0.750) rectangle (5.550,-0.200);
\node[lab] at (5.275,-0.475) {$3$};
\draw[cell frame] (5.550,-0.750) rectangle (6.100,-0.200);
\node[lab] at (5.825,-0.475) {$7$};
\draw[cell frame] (6.100,-0.750) rectangle (6.650,-0.200);
\node[lab] at (6.375,-0.475) {$5$};
\draw[cell frame] (6.650,-0.750) rectangle (7.200,-0.200);
\node[lab] at (6.925,-0.475) {$1$};
\draw[cell frame] (7.200,-0.750) rectangle (7.750,-0.200);
\node[lab] at (7.475,-0.475) {$4$};
\draw[cell frame] (5.000,-1.500) rectangle (5.550,-0.950);
\node[lab] at (5.275,-1.225) {$3$};
\draw[hl cell] (5.550,-1.500) rectangle (6.100,-0.950);
\node[lab] at (5.825,-1.225) {$5$};
\draw[cell frame] (6.100,-1.500) rectangle (6.650,-0.950);
\node[lab] at (6.375,-1.225) {$7$};
\draw[cell frame] (6.650,-1.500) rectangle (7.200,-0.950);
\node[lab] at (6.925,-1.225) {$1$};
\draw[cell frame] (7.200,-1.500) rectangle (7.750,-0.950);
\node[lab] at (7.475,-1.225) {$4$};
\draw[hl cell] (5.000,-2.250) rectangle (5.550,-1.700);
\node[lab] at (5.275,-1.975) {$1$};
\draw[cell frame] (5.550,-2.250) rectangle (6.100,-1.700);
\node[lab] at (5.825,-1.975) {$3$};
\draw[cell frame] (6.100,-2.250) rectangle (6.650,-1.700);
\node[lab] at (6.375,-1.975) {$5$};
\draw[cell frame] (6.650,-2.250) rectangle (7.200,-1.700);
\node[lab] at (6.925,-1.975) {$7$};
\draw[cell frame] (7.200,-2.250) rectangle (7.750,-1.700);
\node[lab] at (7.475,-1.975) {$4$};
\draw[cell frame] (5.000,-3.000) rectangle (5.550,-2.450);
\node[lab] at (5.275,-2.725) {$1$};
\draw[cell frame] (5.550,-3.000) rectangle (6.100,-2.450);
\node[lab] at (5.825,-2.725) {$3$};
\draw[hl cell] (6.100,-3.000) rectangle (6.650,-2.450);
\node[lab] at (6.375,-2.725) {$4$};
\draw[cell frame] (6.650,-3.000) rectangle (7.200,-2.450);
\node[lab] at (6.925,-2.725) {$5$};
\draw[cell frame] (7.200,-3.000) rectangle (7.750,-2.450);
\node[lab] at (7.475,-2.725) {$7$};
\end{tikzpicture}
\end{center}
```

Both sorts on $7,3,5,1,4$, one row per step. Selection sort (left) swaps a largest remaining item into the last unsorted position (highlighted), growing a sorted suffix. Insertion sort (right) moves the next item left into its place (highlighted) in the sorted prefix.

:::

::: {#rmk-comparison-sorting-swaps .remark name="Strengths of the two"}

Selection sort makes only $O(n)$ swaps, which matters if moving an item is expensive. Insertion sort does one swap per *inversion* (pair out of order), so on an almost sorted array, with each item at most $k$ places from its final position, it runs in $O(nk)$ time.

:::
