---
title: "Merge Sort"
sources: [mit6006-3, mit6006r-3]
requires: [cs/sorting/comparison-sorting, math/discrete/sequences/solving-recurrences]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 3 and Recitation 3, in our own wording; proofs written out in steps. Algorithms are described in words, not copied code. Split from cs/sorting/comparison-sorting on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

A divide-and-conquer sort (@def-sorting-problem) in $\Theta(n\log n)$ time.

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
