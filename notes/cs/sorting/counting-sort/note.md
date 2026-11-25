---
title: "Counting Sort"
sources: [mit6006-5, mit6006r-5]
requires: [cs/sorting/linear-sorting]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 5 and Recitation 5, in our own wording; proofs written out in steps. Split from cs/sorting/linear-sorting on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Direct access array sort (@def-direct-access-sort) needs distinct keys. To allow equal keys, each slot holds a sequence of items instead of a single item, as in chaining.

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
