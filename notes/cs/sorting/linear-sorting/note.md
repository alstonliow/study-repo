---
title: "Sorting in Linear Time"
sources: [mit6006-5, mit6006r-5]
requires: [cs/data-structures/hashing]
aliases: [cs/data-structures/linear-sorting]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 5 and Recitation 5, in our own wording; proofs written out in steps. -->

The $\Omega(n\log n)$ bound (@thm-comparison-sort-lower-bound) applies only to comparison sorts. If the keys are integers in a range $\{0,\dots,u-1\}$, using them as array indices sorts faster. Throughout, $n$ is the number of items.

::: {#def-direct-access-sort .definition name="Direct access array sort"}

If the keys are *distinct* integers in $\{0,\dots,u-1\}$: insert every item into a direct access array of length $u$ (@def-direct-access-array), then read the slots in order $0,1,\dots,u-1$ and output the items found. This takes $\Theta(n+u)$ time.

:::

```{=latex}
\begin{algorithm}
\caption{Direct access array sort}
\begin{algorithmic}
\INPUT Items with distinct integer keys in $\{0,\dots,u-1\}$
\OUTPUT The items sorted by key
\STATE $D\gets$ array of $u$ empty slots
\FOR{each item $x$}
    \STATE $D[x.\mathrm{key}]\gets x$
\ENDFOR
\STATE $B\gets$ empty sequence
\FOR{$k=0$ to $u-1$}
    \IF{$D[k]$ is not empty}
        \STATE append $D[k]$ to $B$
    \ENDIF
\ENDFOR
\RETURN $B$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-linear-sorting-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.800,1.100) rectangle (1.350,1.650);
\node[lab] at (1.075,1.375) {$5$};
\draw[cell frame] (1.350,1.100) rectangle (1.900,1.650);
\node[lab] at (1.625,1.375) {$2$};
\draw[cell frame] (1.900,1.100) rectangle (2.450,1.650);
\node[lab] at (2.175,1.375) {$7$};
\draw[cell frame] (2.450,1.100) rectangle (3.000,1.650);
\node[lab] at (2.725,1.375) {$0$};
\draw[cell frame] (3.000,1.100) rectangle (3.550,1.650);
\node[lab] at (3.275,1.375) {$3$};
\node[lab, anchor=east] at (0.700,1.375) {input};
\draw[hl cell] (0.800,0.000) rectangle (1.350,0.550);
\node[lab] at (1.075,0.275) {$0$};
\node[lab,tick] at (1.075,-0.180) {0};
\draw[cell frame] (1.350,0.000) rectangle (1.900,0.550);
\node[lab,tick] at (1.625,-0.180) {1};
\draw[hl cell] (1.900,0.000) rectangle (2.450,0.550);
\node[lab] at (2.175,0.275) {$2$};
\node[lab,tick] at (2.175,-0.180) {2};
\draw[hl cell] (2.450,0.000) rectangle (3.000,0.550);
\node[lab] at (2.725,0.275) {$3$};
\node[lab,tick] at (2.725,-0.180) {3};
\draw[cell frame] (3.000,0.000) rectangle (3.550,0.550);
\node[lab,tick] at (3.275,-0.180) {4};
\draw[hl cell] (3.550,0.000) rectangle (4.100,0.550);
\node[lab] at (3.825,0.275) {$5$};
\node[lab,tick] at (3.825,-0.180) {5};
\draw[cell frame] (4.100,0.000) rectangle (4.650,0.550);
\node[lab,tick] at (4.375,-0.180) {6};
\draw[hl cell] (4.650,0.000) rectangle (5.200,0.550);
\node[lab] at (4.925,0.275) {$7$};
\node[lab,tick] at (4.925,-0.180) {7};
\node[lab, anchor=east] at (0.700,0.275) {$D$};
\draw[cell frame] (0.800,-1.200) rectangle (1.350,-0.650);
\node[lab] at (1.075,-0.925) {$0$};
\draw[cell frame] (1.350,-1.200) rectangle (1.900,-0.650);
\node[lab] at (1.625,-0.925) {$2$};
\draw[cell frame] (1.900,-1.200) rectangle (2.450,-0.650);
\node[lab] at (2.175,-0.925) {$3$};
\draw[cell frame] (2.450,-1.200) rectangle (3.000,-0.650);
\node[lab] at (2.725,-0.925) {$5$};
\draw[cell frame] (3.000,-1.200) rectangle (3.550,-0.650);
\node[lab] at (3.275,-0.925) {$7$};
\node[lab, anchor=east] at (0.700,-0.925) {output};
\end{tikzpicture}
\end{center}
```

Direct access array sort of the distinct keys $5,2,7,0,3$ with $u=8$. Each item goes to the slot of its key; reading the $u$ slots in order and skipping empty ones gives $0,2,3,5,7$. The time is $\Theta(n+u)$, which is linear only when $u=O(n)$.

:::

## Counting sort

To allow equal keys, each slot holds a sequence of items instead of a single item, as in chaining.

::: {#def-counting-sort .definition name="Counting sort"}

*Counting sort* of items with integer keys in $\{0,\dots,u-1\}$: make an array of $u$ empty sequences; for each item in input order, append it to the sequence at index equal to its key; then output the sequences in order $0,1,\dots,u-1$, each from first to last.

:::

```{=latex}
\begin{algorithm}
\caption{Counting sort}
\begin{algorithmic}
\INPUT Items $A[0..n-1]$ with integer keys in $\{0,\dots,u-1\}$
\OUTPUT The items sorted by key, stably
\STATE $D\gets$ array of $u$ empty sequences
\FOR{$i=0$ to $n-1$}
    \STATE append $A[i]$ to $D[A[i].\mathrm{key}]$
\ENDFOR
\STATE $B\gets$ empty sequence
\FOR{$k=0$ to $u-1$}
    \STATE append the items of $D[k]$, first to last, to $B$
\ENDFOR
\RETURN $B$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-linear-sorting-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.200) rectangle (0.550,1.750);
\node[lab] at (0.275,1.475) {$3a$};
\draw[cell frame] (0.550,1.200) rectangle (1.100,1.750);
\node[lab] at (0.825,1.475) {$1b$};
\draw[cell frame] (1.100,1.200) rectangle (1.650,1.750);
\node[lab] at (1.375,1.475) {$3c$};
\draw[cell frame] (1.650,1.200) rectangle (2.200,1.750);
\node[lab] at (1.925,1.475) {$0d$};
\draw[cell frame] (2.200,1.200) rectangle (2.750,1.750);
\node[lab] at (2.475,1.475) {$1e$};
\node[lab, anchor=east] at (-0.100,1.475) {input};
\draw[cell frame] (0.2,0) rectangle (0.75,0.55);
\node[lab,tick] at (0.47,0.75) {key 0};
\node[lab] at (0.47,-0.35) {$0d$};
\draw[cell frame] (1.3,0) rectangle (1.85,0.55);
\node[lab,tick] at (1.57,0.75) {key 1};
\node[lab] at (1.57,-0.35) {$1b$};
\node[lab] at (1.57,-0.8) {$1e$};
\draw[cell frame] (2.40,0) rectangle (2.95,0.55);
\node[lab,tick] at (2.67,0.75) {key 2};
\draw[cell frame] (3.50,0) rectangle (4.05,0.55);
\node[lab,tick] at (3.77,0.75) {key 3};
\node[lab] at (3.77,-0.35) {$3a$};
\node[lab] at (3.77,-0.8) {$3c$};
\draw[cell frame] (0.000,-1.900) rectangle (0.550,-1.350);
\node[lab] at (0.275,-1.625) {$0d$};
\draw[cell frame] (0.550,-1.900) rectangle (1.100,-1.350);
\node[lab] at (0.825,-1.625) {$1b$};
\draw[cell frame] (1.100,-1.900) rectangle (1.650,-1.350);
\node[lab] at (1.375,-1.625) {$1e$};
\draw[cell frame] (1.650,-1.900) rectangle (2.200,-1.350);
\node[lab] at (1.925,-1.625) {$3a$};
\draw[cell frame] (2.200,-1.900) rectangle (2.750,-1.350);
\node[lab] at (2.475,-1.625) {$3c$};
\node[lab, anchor=east] at (-0.100,-1.625) {output};
\end{tikzpicture}
\end{center}
```

Counting sort of keys $3,1,3,0,1$ (letters tell equal keys apart). Each item is appended to the chain of its key in input order; reading the chains from key $0$ upwards gives $0d,1b,1e,3a,3c$, with equal keys in their input order (stable).

:::

::: {#prp-counting-sort .proposition name="Counting sort"}

Counting sort is a stable sort that runs in $\Theta(n+u)$ time.

:::

::: {.proof}

1. Items are output in non-decreasing order of key, because sequence $k$ is output before sequence $k+1$.

2. Items with equal key $k$ all lie in sequence $k$, in the order they were appended, which is their input order. So the sort is stable.

3. Creating the sequences and reading them out takes $\Theta(u)$, and each item is appended and output once in $O(1)$ (amortized) time, so $\Theta(n+u)$ in total.

:::

::: {#rmk-linear-sorting-counting .remark name="Why it is called counting sort"}

A common implementation avoids sequences: count how many items have each key, turn the counts into prefix sums (the first output position of each key), and place the items in input order at those positions. The bounds are the same.

:::

```{=latex}
\begin{algorithm}
\caption{Counting sort with prefix sums}
\begin{algorithmic}
\INPUT Items $A[0..n-1]$ with integer keys in $\{0,\dots,u-1\}$
\OUTPUT Array $B[0..n-1]$ of the items sorted by key, stably
\STATE $C[k]\gets0$ for $0\le k<u$
\FOR{$i=0$ to $n-1$}
    \STATE $C[A[i].\mathrm{key}]\gets C[A[i].\mathrm{key}]+1$
\ENDFOR
\STATE $s\gets0$
\FOR{$k=0$ to $u-1$}
    \STATE $t\gets C[k]$; $C[k]\gets s$; $s\gets s+t$ \COMMENT{first output position of key $k$}
\ENDFOR
\FOR{$i=0$ to $n-1$}
    \STATE $B[C[A[i].\mathrm{key}]]\gets A[i]$; $C[A[i].\mathrm{key}]\gets C[A[i].\mathrm{key}]+1$
\ENDFOR
\RETURN $B$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-linear-sorting-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (1.200,1.400) rectangle (1.750,1.950);
\node[lab] at (1.475,1.675) {$3\mathrm{a}$};
\draw[cell frame] (1.750,1.400) rectangle (2.300,1.950);
\node[lab] at (2.025,1.675) {$1\mathrm{b}$};
\draw[cell frame] (2.300,1.400) rectangle (2.850,1.950);
\node[lab] at (2.575,1.675) {$3\mathrm{c}$};
\draw[cell frame] (2.850,1.400) rectangle (3.400,1.950);
\node[lab] at (3.125,1.675) {$0\mathrm{d}$};
\draw[cell frame] (3.400,1.400) rectangle (3.950,1.950);
\node[lab] at (3.675,1.675) {$1\mathrm{e}$};
\node[lab, anchor=east] at (1.100,1.675) {input};
\draw[cell frame] (1.200,0.500) rectangle (1.750,1.050);
\node[lab] at (1.475,0.775) {$1$};
\node[lab,tick] at (1.475,0.320) {0};
\draw[cell frame] (1.750,0.500) rectangle (2.300,1.050);
\node[lab] at (2.025,0.775) {$2$};
\node[lab,tick] at (2.025,0.320) {1};
\draw[cell frame] (2.300,0.500) rectangle (2.850,1.050);
\node[lab] at (2.575,0.775) {$0$};
\node[lab,tick] at (2.575,0.320) {2};
\draw[cell frame] (2.850,0.500) rectangle (3.400,1.050);
\node[lab] at (3.125,0.775) {$2$};
\node[lab,tick] at (3.125,0.320) {3};
\node[lab, anchor=east] at (1.100,0.775) {counts $C$};
\draw[cell frame] (1.200,-0.500) rectangle (1.750,0.050);
\node[lab] at (1.475,-0.225) {$0$};
\draw[cell frame] (1.750,-0.500) rectangle (2.300,0.050);
\node[lab] at (2.025,-0.225) {$1$};
\draw[cell frame] (2.300,-0.500) rectangle (2.850,0.050);
\node[lab] at (2.575,-0.225) {$3$};
\draw[cell frame] (2.850,-0.500) rectangle (3.400,0.050);
\node[lab] at (3.125,-0.225) {$3$};
\node[lab, anchor=east] at (1.100,-0.225) {starts};
\draw[cell frame] (1.200,-1.400) rectangle (1.750,-0.850);
\node[lab] at (1.475,-1.125) {$0\mathrm{d}$};
\node[lab,tick] at (1.475,-1.580) {0};
\draw[cell frame] (1.750,-1.400) rectangle (2.300,-0.850);
\node[lab] at (2.025,-1.125) {$1\mathrm{b}$};
\node[lab,tick] at (2.025,-1.580) {1};
\draw[cell frame] (2.300,-1.400) rectangle (2.850,-0.850);
\node[lab] at (2.575,-1.125) {$1\mathrm{e}$};
\node[lab,tick] at (2.575,-1.580) {2};
\draw[cell frame] (2.850,-1.400) rectangle (3.400,-0.850);
\node[lab] at (3.125,-1.125) {$3\mathrm{a}$};
\node[lab,tick] at (3.125,-1.580) {3};
\draw[cell frame] (3.400,-1.400) rectangle (3.950,-0.850);
\node[lab] at (3.675,-1.125) {$3\mathrm{c}$};
\node[lab,tick] at (3.675,-1.580) {4};
\node[lab, anchor=east] at (1.100,-1.125) {output $B$};
\end{tikzpicture}
\end{center}
```

Counting sort of @fig-linear-sorting-1 without sequences. Count the keys ($1,2,0,2$ for keys $0,1,2,3$), turn the counts into starting positions $0,1,3,3$ by prefix sums, then place the items in input order, each at the next free position of its key. The output $0\mathrm d,1\mathrm b,1\mathrm e,3\mathrm a,3\mathrm c$ is the same, and stable.

:::

## Tuple sort and radix sort

::: {#lem-tuple-sort .lemma name="Tuple sort"}

Let each key be a tuple $(k_1,\dots,k_c)$, ordered lexicographically ($k_1$ most significant). Sorting the items by $k_c$, then by $k_{c-1}$, …, then by $k_1$, each time with a *stable* sort, sorts them lexicographically.

:::

::: {.proof}

1. Claim: after the passes on $k_c,k_{c-1},\dots,k_j$, the items are sorted lexicographically by $(k_j,\dots,k_c)$. We prove it by induction on the number of passes.

2. After the first pass the items are sorted by $k_c$.

3. Suppose after the pass on $k_{j+1}$ they are sorted by $(k_{j+1},\dots,k_c)$, and consider the stable pass on $k_j$. Take two items $x$ and $y$ with $(x_j,\dots,x_c)<(y_j,\dots,y_c)$ lexicographically. If $x_j<y_j$, the pass puts $x$ first. If $x_j=y_j$, then $(x_{j+1},\dots,x_c)<(y_{j+1},\dots,y_c)$, so $x$ was before $y$ before the pass, and stability keeps it there.

4. After the pass on $k_1$ the items are sorted by the whole tuple.

:::

```{=latex}
\begin{algorithm}
\caption{Tuple sort}
\begin{algorithmic}
\INPUT Items with keys $(k_1,\dots,k_c)$; a stable sort
\OUTPUT The items in lexicographic order of key
\FOR{$j=c$ down to $1$}
    \STATE sort the items stably by $k_j$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

The order matters: sorting from the most significant entry first would let the later passes destroy the earlier order.

::: {#def-radix-sort .definition name="Radix sort"}

*Radix sort* of items with integer keys in $\{0,\dots,u-1\}$: write each key in base $n$ as a $c$-digit number with $c=\lceil\log_nu\rceil$ (at least $1$), and tuple-sort the digit tuples using counting sort for each digit.

:::

```{=latex}
\begin{algorithm}
\caption{Radix sort}
\begin{algorithmic}
\INPUT Items $A[0..n-1]$ with integer keys in $\{0,\dots,u-1\}$
\OUTPUT The items sorted by key, stably
\STATE $c\gets\max\{1,\lceil\log_nu\rceil\}$
\FOR{each item $x$}
    \STATE write $x.\mathrm{key}$ in base $n$ as digits $(k_1,\dots,k_c)$, $k_1$ most significant
\ENDFOR
\FOR{$j=c$ down to $1$}
    \STATE counting sort the items by digit $k_j$ \COMMENT{keys in $\{0,\dots,n-1\}$}
\ENDFOR
\RETURN the items
\end{algorithmic}
\end{algorithm}
```

::: {#thm-radix-sort .theorem name="Radix sort"}

Radix sort sorts $n$ items with keys in $\{0,\dots,u-1\}$, stably, in $O\bigl(n\,(1+\log_nu)\bigr)$ time. In particular, if $u\le n^c$ for a constant $c$, it runs in $O(n)$ time.

:::

::: {.proof}

1. Correctness follows from @lem-tuple-sort, since counting sort is stable (@prp-counting-sort) and the lexicographic order of the base-$n$ digit tuples is the order of the keys.

2. Computing the digits takes $O(c)$ arithmetic operations per key. Each of the $c$ passes is a counting sort with $n$ items and digit range $n$, costing $\Theta(n+n)=\Theta(n)$.

3. The total is $O(cn)$ with $c=O(1+\log_nu)$.

:::

::: {#fig-linear-sorting-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$32$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$03$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$44$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$42$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$22$};
\node[lab, anchor=east] at (-0.100,0.275) {base $5$};
\draw[cell frame] (0.000,-0.800) rectangle (0.550,-0.250);
\node[lab] at (0.275,-0.525) {$32$};
\draw[cell frame] (0.550,-0.800) rectangle (1.100,-0.250);
\node[lab] at (0.825,-0.525) {$42$};
\draw[cell frame] (1.100,-0.800) rectangle (1.650,-0.250);
\node[lab] at (1.375,-0.525) {$22$};
\draw[cell frame] (1.650,-0.800) rectangle (2.200,-0.250);
\node[lab] at (1.925,-0.525) {$03$};
\draw[cell frame] (2.200,-0.800) rectangle (2.750,-0.250);
\node[lab] at (2.475,-0.525) {$44$};
\node[lab, anchor=east] at (-0.100,-0.525) {by last digit};
\draw[cell frame] (0.000,-1.600) rectangle (0.550,-1.050);
\node[lab] at (0.275,-1.325) {$03$};
\draw[cell frame] (0.550,-1.600) rectangle (1.100,-1.050);
\node[lab] at (0.825,-1.325) {$22$};
\draw[cell frame] (1.100,-1.600) rectangle (1.650,-1.050);
\node[lab] at (1.375,-1.325) {$32$};
\draw[cell frame] (1.650,-1.600) rectangle (2.200,-1.050);
\node[lab] at (1.925,-1.325) {$42$};
\draw[cell frame] (2.200,-1.600) rectangle (2.750,-1.050);
\node[lab] at (2.475,-1.325) {$44$};
\node[lab, anchor=east] at (-0.100,-1.325) {by first digit};
\draw[cell frame] (0.000,-2.400) rectangle (0.550,-1.850);
\node[lab] at (0.275,-2.125) {$3$};
\draw[cell frame] (0.550,-2.400) rectangle (1.100,-1.850);
\node[lab] at (0.825,-2.125) {$12$};
\draw[cell frame] (1.100,-2.400) rectangle (1.650,-1.850);
\node[lab] at (1.375,-2.125) {$17$};
\draw[cell frame] (1.650,-2.400) rectangle (2.200,-1.850);
\node[lab] at (1.925,-2.125) {$22$};
\draw[cell frame] (2.200,-2.400) rectangle (2.750,-1.850);
\node[lab] at (2.475,-2.125) {$24$};
\node[lab, anchor=east] at (-0.100,-2.125) {keys};
\end{tikzpicture}
\end{center}
```

Radix sort of $17,3,24,22,12$ with base $n=5$: write the keys as two base-$5$ digits, sort stably by the last digit, then by the first. Stability keeps $32,42,22$ in order within the first digit's ties, so the result is sorted.

:::

For example, with $n=5$ the keys $17,3,24,22,12$ become the base-$5$ pairs $32,03,44,42,22$; sorting by the last digit gives $32,42,22,03,44$, and then by the first digit $03,22,32,42,44$, that is $3,12,17,22,24$.

| algorithm | time | in place | stable | note |
|---|---|---|---|---|
| insertion sort | $n^2$ | yes | yes | $O(nk)$ if items are at most $k$ places off |
| selection sort | $n^2$ | yes | no | $O(n)$ swaps |
| merge sort | $n\log n$ | no | yes | optimal comparison sort |
| counting sort | $n+u$ | no | yes | $O(n)$ when $u=O(n)$ |
| radix sort | $n+n\log_nu$ | no | yes | $O(n)$ when $u=O(n^c)$ |
