---
title: "Sorted Arrays and Binary Search"
sources: [mit6006-3, mit6006r-3]
requires: [cs/sorting/merge-sort]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 3 and Recitation 3, in our own wording; proofs written out in steps. Algorithms are described in words, not copied code. Split from cs/sorting/comparison-sorting on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Storing the items of a set (@def-set-interface) in an array *sorted by key* makes `find_min` and `find_max` take $O(1)$ time (first and last slot) and `find` take $O(\log n)$ time by binary search.

::: {#prp-binary-search .proposition name="Binary search"}

Let $A[0],\dots,A[n-1]$ be sorted increasingly. To find key $k$, compare $k$ with the middle item $A[m]$, $m=\lfloor n/2\rfloor$: stop if equal, otherwise search $A[0..m-1]$ if $k$ is smaller and $A[m+1..n-1]$ if $k$ is larger, and report "absent" on an empty range. This finds $k$ (or correctly reports it absent) using at most $\lfloor\log_2n\rfloor+1$ comparisons.

:::

::: {.proof}

1. *Correctness*, by strong induction on $n$. For $n=0$ the answer "absent" is right. For $n\ge1$, if $k<A[m]$ then $k$ is not at any position $\ge m$ because the array is sorted, so it suffices to search the left part, which is done correctly by induction; the case $k>A[m]$ is symmetric.

2. *Count.* Each comparison leaves a range of at most $\lfloor n/2\rfloor$ items. After $j$ comparisons at most $\lfloor n/2^j\rfloor$ items remain, which is $0$ once $2^j>n$, that is, after $\lfloor\log_2n\rfloor+1$ comparisons.

:::

```{=latex}
\begin{algorithm}
\caption{Binary search}
\begin{algorithmic}
\INPUT Sorted array $A[0..n-1]$, key $k$
\OUTPUT An index $m$ with $A[m]=k$, or "absent"
\STATE $lo\gets0$; $hi\gets n$ \COMMENT{search $A[lo..hi-1]$}
\WHILE{$lo<hi$}
    \STATE $m\gets lo+\lfloor(hi-lo)/2\rfloor$
    \IF{$k=A[m]$}
        \RETURN $m$
    \ELSIF{$k<A[m]$}
        \STATE $hi\gets m$
    \ELSE
        \STATE $lo\gets m+1$
    \ENDIF
\ENDWHILE
\RETURN "absent"
\end{algorithmic}
\end{algorithm}
```

::: {#fig-comparison-sorting-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\node[lab,tick] at (0.275,-0.180) {0};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$3$};
\node[lab,tick] at (0.825,-0.180) {1};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$4$};
\node[lab,tick] at (1.375,-0.180) {2};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$6$};
\node[lab,tick] at (1.925,-0.180) {3};
\draw[hl cell] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$8$};
\node[lab,tick] at (2.475,-0.180) {4};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$9$};
\node[lab,tick] at (3.025,-0.180) {5};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$11$};
\node[lab,tick] at (3.575,-0.180) {6};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$14$};
\node[lab,tick] at (4.125,-0.180) {7};
\draw[cell frame] (4.400,0.000) rectangle (4.950,0.550);
\node[lab] at (4.675,0.275) {$17$};
\node[lab,tick] at (4.675,-0.180) {8};
\node[lab, anchor=east] at (-0.100,0.275) {step 1};
\draw[cell frame] (0.000,-0.800) rectangle (0.550,-0.250);
\draw[cell frame] (0.550,-0.800) rectangle (1.100,-0.250);
\draw[cell frame] (1.100,-0.800) rectangle (1.650,-0.250);
\draw[cell frame] (1.650,-0.800) rectangle (2.200,-0.250);
\draw[cell frame] (2.200,-0.800) rectangle (2.750,-0.250);
\draw[cell frame] (2.750,-0.800) rectangle (3.300,-0.250);
\node[lab] at (3.025,-0.525) {$9$};
\draw[cell frame] (3.300,-0.800) rectangle (3.850,-0.250);
\node[lab] at (3.575,-0.525) {$11$};
\draw[hl cell] (3.850,-0.800) rectangle (4.400,-0.250);
\node[lab] at (4.125,-0.525) {$14$};
\draw[cell frame] (4.400,-0.800) rectangle (4.950,-0.250);
\node[lab] at (4.675,-0.525) {$17$};
\node[lab, anchor=east] at (-0.100,-0.525) {step 2};
\draw[cell frame] (0.000,-1.600) rectangle (0.550,-1.050);
\draw[cell frame] (0.550,-1.600) rectangle (1.100,-1.050);
\draw[cell frame] (1.100,-1.600) rectangle (1.650,-1.050);
\draw[cell frame] (1.650,-1.600) rectangle (2.200,-1.050);
\draw[cell frame] (2.200,-1.600) rectangle (2.750,-1.050);
\draw[cell frame] (2.750,-1.600) rectangle (3.300,-1.050);
\node[lab] at (3.025,-1.325) {$9$};
\draw[hl cell] (3.300,-1.600) rectangle (3.850,-1.050);
\node[lab] at (3.575,-1.325) {$11$};
\draw[cell frame] (3.850,-1.600) rectangle (4.400,-1.050);
\draw[cell frame] (4.400,-1.600) rectangle (4.950,-1.050);
\node[lab, anchor=east] at (-0.100,-1.325) {step 3};
\end{tikzpicture}
\end{center}
```

Binary search for $11$ in a sorted array. Each step compares $11$ with the middle item of the remaining range (highlighted) and keeps one half, so after $j$ steps at most $n/2^j$ items remain.

:::

But inserting into or deleting from a sorted array shifts items and takes $\Theta(n)$ time, and building one requires sorting.
