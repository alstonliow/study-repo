---
title: "Sorting in Linear Time"
sources: [mit6006-5, mit6006r-5]
requires: [cs/data-structures/hashing]
aliases: [cs/data-structures/linear-sorting]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 5 and Recitation 5, in our own wording; proofs written out in steps. On 2026-11-25 counting sort and radix sort moved to their own notes (one algorithm per note, SPEC §8.6); this note is their overview. -->

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

## The algorithms

Counting sort (@sec-cs-sorting-counting-sort) allows equal keys; radix sort (@sec-cs-sorting-radix-sort) handles keys up to a polynomial in $n$.

| algorithm | keys | time | stable |
|---|---|---|---|
| direct access array sort (@def-direct-access-sort) | distinct, in $\{0,\dots,u-1\}$ | $\Theta(n+u)$ | — |
| counting sort (@prp-counting-sort) | in $\{0,\dots,u-1\}$ | $\Theta(n+u)$ | yes |
| radix sort (@thm-radix-sort) | in $\{0,\dots,u-1\}$ | $O\bigl(n\,(1+\log_nu)\bigr)$ | yes |
