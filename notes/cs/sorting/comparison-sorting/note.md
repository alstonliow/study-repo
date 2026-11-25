---
title: "Sorting by Comparisons"
sources: [mit6006-3, mit6006r-3]
requires: [cs/data-structures/linked-lists-and-dynamic-arrays, math/discrete/sequences/solving-recurrences]
aliases: [cs/data-structures/comparison-sorting]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 3 and Recitation 3, in our own wording; proofs written out in steps. Algorithms are described in words, not copied code. -->

## Sorted arrays as sets

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

## The sorting problem

::: {#def-sorting-problem .definition name="Sorting"}

*Sorting*: given an array $A$ of $n$ items with keys, output a permutation $B$ of $A$ with $B[i-1].\mathrm{key}\le B[i].\mathrm{key}$ for $1\le i<n$. A sorting algorithm is

1. *destructive* if it overwrites $A$ instead of producing a new array,
2. *in place* if it uses only $O(1)$ extra space (so it is destructive), and
3. *stable* if items with equal keys appear in $B$ in the same relative order as in $A$.

:::

Trying all $n!$ permutations and checking each in $\Theta(n)$ time ("permutation sort") is correct by exhaustion but takes $\Omega(n!\cdot n)$ time. The following algorithms do much better.

## Selection sort and insertion sort

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

## Merge sort

::: {#def-merge-sort .definition name="Merge sort"}

*Merge sort* of $A[a..b-1]$: if it has at least two items, let $c=\lceil(a+b)/2\rceil$, merge sort $A[a..c-1]$ and $A[c..b-1]$, copy the two sorted halves to arrays $L$ and $R$, and *merge* them back into $A[a..b-1]$: repeatedly move the smaller of the first remaining items of $L$ and $R$ (the one from $L$ on a tie) to the next slot of $A$, until both are empty.

:::

```{=latex}
\begin{algorithm}
\caption{Merge sort of $A[a..b-1]$}
\begin{algorithmic}
\INPUT Array $A$, indices $a\le b$
\OUTPUT $A[a..b-1]$ sorted
\IF{$b-a\ge2$}
    \STATE $c\gets\lceil(a+b)/2\rceil$
    \STATE merge sort $A[a..c-1]$; merge sort $A[c..b-1]$
    \STATE $L\gets$ copy of $A[a..c-1]$; $R\gets$ copy of $A[c..b-1]$
    \STATE $i\gets0$; $j\gets0$ \COMMENT{merge}
    \FOR{$k=a$ to $b-1$}
        \IF{$j=|R|$ or ($i<|L|$ and $L[i]\le R[j]$)}
            \STATE $A[k]\gets L[i]$; $i\gets i+1$ \COMMENT{ties from $L$: stable}
        \ELSE
            \STATE $A[k]\gets R[j]$; $j\gets j+1$
        \ENDIF
    \ENDFOR
\ENDIF
\end{algorithmic}
\end{algorithm}
```

::: {#thm-merge-sort .theorem name="Merge sort" related="exm-merge-sort-extra"}

Merge sort is a stable sort that runs in $\Theta(n\log n)$ time and uses $\Theta(n)$ extra space.

:::

::: {.proof}

1. *Merging is correct.* At each step the smallest remaining item overall is the smaller of the first remaining items of $L$ and $R$, because both are sorted. So the items are written in non-decreasing order. Taking from $L$ on ties keeps equal items in their original order.

2. *Merge sort is correct*, by strong induction on the length: a range of $0$ or $1$ items is sorted, and a longer range is split into two shorter ones, sorted by induction and then merged correctly by step 1.

3. *Time.* Merging $n$ items costs $\Theta(n)$, so $T(n)=2T(n/2)+\Theta(n)$ (for $n$ a power of $2$; other $n$ only change constants). In the recursion tree, level $i$ has $2^i$ calls on $n/2^i$ items each, $\Theta(n)$ work per level, and there are $\log_2n+1$ levels, so $T(n)=\Theta(n\log n)$; this is case 2 of the master theorem (@thm-master-theorem).

4. *Space.* The copies $L$ and $R$ at the top level have $n$ items; lower levels can reuse one buffer of size $n$.

:::

::: {#fig-comparison-sorting-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$6$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$7$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$1$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$5$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$3$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$8$};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$4$};
\draw[cell frame] (0.000,-0.800) rectangle (0.550,-0.250);
\node[lab] at (0.275,-0.525) {$6$};
\draw[cell frame] (0.550,-0.800) rectangle (1.100,-0.250);
\node[lab] at (0.825,-0.525) {$2$};
\draw[cell frame] (1.100,-0.800) rectangle (1.650,-0.250);
\node[lab] at (1.375,-0.525) {$7$};
\draw[cell frame] (1.650,-0.800) rectangle (2.200,-0.250);
\node[lab] at (1.925,-0.525) {$1$};
\draw[cell frame] (2.550,-0.800) rectangle (3.100,-0.250);
\node[lab] at (2.825,-0.525) {$5$};
\draw[cell frame] (3.100,-0.800) rectangle (3.650,-0.250);
\node[lab] at (3.375,-0.525) {$3$};
\draw[cell frame] (3.650,-0.800) rectangle (4.200,-0.250);
\node[lab] at (3.925,-0.525) {$8$};
\draw[cell frame] (4.200,-0.800) rectangle (4.750,-0.250);
\node[lab] at (4.475,-0.525) {$4$};
\draw[cell frame] (0.000,-1.600) rectangle (0.550,-1.050);
\node[lab] at (0.275,-1.325) {$6$};
\draw[cell frame] (0.550,-1.600) rectangle (1.100,-1.050);
\node[lab] at (0.825,-1.325) {$2$};
\draw[cell frame] (1.450,-1.600) rectangle (2.000,-1.050);
\node[lab] at (1.725,-1.325) {$7$};
\draw[cell frame] (2.000,-1.600) rectangle (2.550,-1.050);
\node[lab] at (2.275,-1.325) {$1$};
\draw[cell frame] (2.900,-1.600) rectangle (3.450,-1.050);
\node[lab] at (3.175,-1.325) {$5$};
\draw[cell frame] (3.450,-1.600) rectangle (4.000,-1.050);
\node[lab] at (3.725,-1.325) {$3$};
\draw[cell frame] (4.350,-1.600) rectangle (4.900,-1.050);
\node[lab] at (4.625,-1.325) {$8$};
\draw[cell frame] (4.900,-1.600) rectangle (5.450,-1.050);
\node[lab] at (5.175,-1.325) {$4$};
\draw[cell frame] (0.000,-2.400) rectangle (0.550,-1.850);
\node[lab] at (0.275,-2.125) {$6$};
\draw[cell frame] (0.900,-2.400) rectangle (1.450,-1.850);
\node[lab] at (1.175,-2.125) {$2$};
\draw[cell frame] (1.800,-2.400) rectangle (2.350,-1.850);
\node[lab] at (2.075,-2.125) {$7$};
\draw[cell frame] (2.700,-2.400) rectangle (3.250,-1.850);
\node[lab] at (2.975,-2.125) {$1$};
\draw[cell frame] (3.600,-2.400) rectangle (4.150,-1.850);
\node[lab] at (3.875,-2.125) {$5$};
\draw[cell frame] (4.500,-2.400) rectangle (5.050,-1.850);
\node[lab] at (4.775,-2.125) {$3$};
\draw[cell frame] (5.400,-2.400) rectangle (5.950,-1.850);
\node[lab] at (5.675,-2.125) {$8$};
\draw[cell frame] (6.300,-2.400) rectangle (6.850,-1.850);
\node[lab] at (6.575,-2.125) {$4$};
\draw[cell frame] (0.000,-3.200) rectangle (0.550,-2.650);
\node[lab] at (0.275,-2.925) {$2$};
\draw[cell frame] (0.550,-3.200) rectangle (1.100,-2.650);
\node[lab] at (0.825,-2.925) {$6$};
\draw[cell frame] (1.450,-3.200) rectangle (2.000,-2.650);
\node[lab] at (1.725,-2.925) {$1$};
\draw[cell frame] (2.000,-3.200) rectangle (2.550,-2.650);
\node[lab] at (2.275,-2.925) {$7$};
\draw[cell frame] (2.900,-3.200) rectangle (3.450,-2.650);
\node[lab] at (3.175,-2.925) {$3$};
\draw[cell frame] (3.450,-3.200) rectangle (4.000,-2.650);
\node[lab] at (3.725,-2.925) {$5$};
\draw[cell frame] (4.350,-3.200) rectangle (4.900,-2.650);
\node[lab] at (4.625,-2.925) {$4$};
\draw[cell frame] (4.900,-3.200) rectangle (5.450,-2.650);
\node[lab] at (5.175,-2.925) {$8$};
\draw[cell frame] (0.000,-4.000) rectangle (0.550,-3.450);
\node[lab] at (0.275,-3.725) {$1$};
\draw[cell frame] (0.550,-4.000) rectangle (1.100,-3.450);
\node[lab] at (0.825,-3.725) {$2$};
\draw[cell frame] (1.100,-4.000) rectangle (1.650,-3.450);
\node[lab] at (1.375,-3.725) {$6$};
\draw[cell frame] (1.650,-4.000) rectangle (2.200,-3.450);
\node[lab] at (1.925,-3.725) {$7$};
\draw[cell frame] (2.550,-4.000) rectangle (3.100,-3.450);
\node[lab] at (2.825,-3.725) {$3$};
\draw[cell frame] (3.100,-4.000) rectangle (3.650,-3.450);
\node[lab] at (3.375,-3.725) {$4$};
\draw[cell frame] (3.650,-4.000) rectangle (4.200,-3.450);
\node[lab] at (3.925,-3.725) {$5$};
\draw[cell frame] (4.200,-4.000) rectangle (4.750,-3.450);
\node[lab] at (4.475,-3.725) {$8$};
\draw[cell frame] (0.000,-4.800) rectangle (0.550,-4.250);
\node[lab] at (0.275,-4.525) {$1$};
\draw[cell frame] (0.550,-4.800) rectangle (1.100,-4.250);
\node[lab] at (0.825,-4.525) {$2$};
\draw[cell frame] (1.100,-4.800) rectangle (1.650,-4.250);
\node[lab] at (1.375,-4.525) {$3$};
\draw[cell frame] (1.650,-4.800) rectangle (2.200,-4.250);
\node[lab] at (1.925,-4.525) {$4$};
\draw[cell frame] (2.200,-4.800) rectangle (2.750,-4.250);
\node[lab] at (2.475,-4.525) {$5$};
\draw[cell frame] (2.750,-4.800) rectangle (3.300,-4.250);
\node[lab] at (3.025,-4.525) {$6$};
\draw[cell frame] (3.300,-4.800) rectangle (3.850,-4.250);
\node[lab] at (3.575,-4.525) {$7$};
\draw[cell frame] (3.850,-4.800) rectangle (4.400,-4.250);
\node[lab] at (4.125,-4.525) {$8$};
\node[lab, anchor=west] at (7.4,-1.2) {split};
\draw[->] (7.3,-0.2) -- (7.3,-2.3);
\node[lab, anchor=west] at (7.4,-4.4) {merge};
\draw[->] (7.3,-3.4) -- (7.3,-5.5);
\end{tikzpicture}
\end{center}
```

Merge sort of $6,2,7,1,5,3,8,4$. The upper rows split the array in halves down to single items; the lower rows merge sorted halves back together. There are $\log_2n$ levels of each kind, and each level does $\Theta(n)$ work.

:::

::: {#rmk-comparison-sorting-solving-recurrences .remark name="Three ways to solve a recurrence"}

The recurrences of this note can be solved by *substitution* (guess the answer and check it by induction), by a *recursion tree* (add up the work at the nodes level by level), or by the *master theorem* (@thm-master-theorem), which packages the recursion-tree computation for $T(n)=aT(n/b)+f(n)$.

:::
