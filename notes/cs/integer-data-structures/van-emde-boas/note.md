---
title: "van Emde Boas Trees"
sources: [mit6046-4]
requires: [cs/data-structures/hashing]
aliases: [cs/data-structures/van-emde-boas, cs/advanced-data-structures/van-emde-boas]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 4, in our own wording; proofs written out in steps. -->

Goal: store a set of integers from $\{0,\dots,u-1\}$ and support `insert`, `delete` and `successor` in $O(\log\log u)$ time. For $u=n^{O(1)}$ this is $O(\log\log n)$, exponentially faster than a balanced search tree; an application is routing tables, where $u=2^{32}$ IP addresses.

The bound $\log\log u$ arises from a recurrence that takes a *square root* of the universe at each step:
$$T(u)=T(\sqrt u)+O(1)\quad\Longrightarrow\quad T(u)=O(\log\log u),$$
since with $u=2^{2^k}$ the universe size after $k$ steps is $2$. (Equivalently, $T'(\lg u)=T'(\tfrac12\lg u)+O(1)$.)

## From a bit vector to clusters

A bit vector of length $u$ supports `insert` and `delete` in $O(1)$ but `successor` in $O(u)$. Split the universe into $\sqrt u$ *clusters* of size $\sqrt u$: write $x=i\sqrt u+j$ with
$$\mathrm{high}(x)=\lfloor x/\sqrt u\rfloor=i,\qquad\mathrm{low}(x)=x\bmod\sqrt u=j.$$
A *summary* vector records which clusters are non-empty. Then a successor query looks inside $x$'s cluster, and if that fails, finds the next non-empty cluster in the summary and takes its minimum: $O(\sqrt u)$.

::: {#def-veb .definition name="van Emde Boas structure"}

A vEB structure $V$ for universe size $u$ stores

1. $V.\min$ and $V.\max$ (with $V.\min$ *not* stored anywhere else);
2. $V.\mathrm{cluster}[i]$ for $0\le i<\sqrt u$: a vEB structure for universe size $\sqrt u$ holding $\{\mathrm{low}(x):x\in V,\ x\ne V.\min,\ \mathrm{high}(x)=i\}$;
3. $V.\mathrm{summary}$: a vEB structure for universe size $\sqrt u$ holding the indices of the non-empty clusters.

:::

::: {#fig-van-emde-boas-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.500,0.500);
\node[lab] at (0.250,0.250) {$0$};
\node[lab,tick] at (0.250,-0.180) {0};
\draw[hl cell] (0.500,0.000) rectangle (1.000,0.500);
\node[lab] at (0.750,0.250) {$1$};
\node[lab,tick] at (0.750,-0.180) {1};
\draw[cell frame] (1.000,0.000) rectangle (1.500,0.500);
\node[lab] at (1.250,0.250) {$0$};
\node[lab,tick] at (1.250,-0.180) {2};
\draw[cell frame] (1.500,0.000) rectangle (2.000,0.500);
\node[lab] at (1.750,0.250) {$0$};
\node[lab,tick] at (1.750,-0.180) {3};
\draw[cell frame] (2.000,0.000) rectangle (2.500,0.500);
\node[lab] at (2.250,0.250) {$0$};
\node[lab,tick] at (2.250,-0.180) {4};
\draw[cell frame] (2.500,0.000) rectangle (3.000,0.500);
\node[lab] at (2.750,0.250) {$0$};
\node[lab,tick] at (2.750,-0.180) {5};
\draw[cell frame] (3.000,0.000) rectangle (3.500,0.500);
\node[lab] at (3.250,0.250) {$0$};
\node[lab,tick] at (3.250,-0.180) {6};
\draw[cell frame] (3.500,0.000) rectangle (4.000,0.500);
\node[lab] at (3.750,0.250) {$0$};
\node[lab,tick] at (3.750,-0.180) {7};
\draw[cell frame] (4.000,0.000) rectangle (4.500,0.500);
\node[lab] at (4.250,0.250) {$0$};
\node[lab,tick] at (4.250,-0.180) {8};
\draw[hl cell] (4.500,0.000) rectangle (5.000,0.500);
\node[lab] at (4.750,0.250) {$1$};
\node[lab,tick] at (4.750,-0.180) {9};
\draw[hl cell] (5.000,0.000) rectangle (5.500,0.500);
\node[lab] at (5.250,0.250) {$1$};
\node[lab,tick] at (5.250,-0.180) {10};
\draw[cell frame] (5.500,0.000) rectangle (6.000,0.500);
\node[lab] at (5.750,0.250) {$0$};
\node[lab,tick] at (5.750,-0.180) {11};
\draw[cell frame] (6.000,0.000) rectangle (6.500,0.500);
\node[lab] at (6.250,0.250) {$0$};
\node[lab,tick] at (6.250,-0.180) {12};
\draw[cell frame] (6.500,0.000) rectangle (7.000,0.500);
\node[lab] at (6.750,0.250) {$0$};
\node[lab,tick] at (6.750,-0.180) {13};
\draw[cell frame] (7.000,0.000) rectangle (7.500,0.500);
\node[lab] at (7.250,0.250) {$0$};
\node[lab,tick] at (7.250,-0.180) {14};
\draw[hl cell] (7.500,0.000) rectangle (8.000,0.500);
\node[lab] at (7.750,0.250) {$1$};
\node[lab,tick] at (7.750,-0.180) {15};
\draw[faint] (0.05,-0.45) -- (1.95,-0.45);
\node[lab,tick] at (1.00,-0.7) {cluster 0};
\draw[faint] (2.05,-0.45) -- (3.95,-0.45);
\node[lab,tick] at (3.00,-0.7) {cluster 1};
\draw[faint] (4.05,-0.45) -- (5.95,-0.45);
\node[lab,tick] at (5.00,-0.7) {cluster 2};
\draw[faint] (6.05,-0.45) -- (7.95,-0.45);
\node[lab,tick] at (7.00,-0.7) {cluster 3};
\draw[hl cell] (2.000,1.200) rectangle (2.500,1.700);
\node[lab] at (2.250,1.450) {$1$};
\draw[cell frame] (2.500,1.200) rectangle (3.000,1.700);
\node[lab] at (2.750,1.450) {$0$};
\draw[hl cell] (3.000,1.200) rectangle (3.500,1.700);
\node[lab] at (3.250,1.450) {$1$};
\draw[hl cell] (3.500,1.200) rectangle (4.000,1.700);
\node[lab] at (3.750,1.450) {$1$};
\node[lab, anchor=east] at (1.900,1.450) {summary};
\end{tikzpicture}
\end{center}
```

The set $\{1,9,10,15\}$ in a universe of size $u=16$, split into $\sqrt u=4$ clusters of size $4$. The summary records which clusters are non-empty ($0$, $2$ and $3$). A successor query looks in one cluster, or in the summary and then one cluster: each is a structure of size $\sqrt u$.

:::

::: {#prp-veb-successor .proposition name="Successor in $O(\log\log u)$"}

`successor(V, x)`:

1. if $x<V.\min$, return $V.\min$;
2. let $i=\mathrm{high}(x)$; if $\mathrm{low}(x)<V.\mathrm{cluster}[i].\max$, return $i\sqrt u+$ `successor(V.cluster[i], low(x))`;
3. otherwise let $i'$ = `successor(V.summary, i)` and return $i'\sqrt u+V.\mathrm{cluster}[i'].\min$ (or "none" if $i'$ does not exist).

It makes at most one recursive call, on a universe of size $\sqrt u$, so it runs in $O(\log\log u)$ time.

:::

::: {.proof}

1. If the answer is in $x$'s own cluster, it is there exactly when $\mathrm{low}(x)$ is below that cluster's maximum, which is read in $O(1)$; then the successor within the cluster is the answer.

2. Otherwise the answer is the minimum of the next non-empty cluster, found by one successor query on the summary and an $O(1)$ lookup of a minimum.

3. Either way there is one recursive call on size $\sqrt u$ plus $O(1)$ work: $T(u)=T(\sqrt u)+O(1)=O(\log\log u)$.

:::

```{=latex}
\begin{algorithm}
\caption{vEB successor$(V,x)$}
\begin{algorithmic}
\INPUT vEB structure $V$ for universe size $u$, an integer $x$
\OUTPUT The smallest element of $V$ larger than $x$, or none
\IF{$V$ is empty}
    \RETURN none
\ENDIF
\IF{$x<V.\min$}
    \RETURN $V.\min$
\ENDIF
\STATE $i\gets\mathrm{high}(x)$
\IF{$V.\mathrm{cluster}[i]$ is not empty and $\mathrm{low}(x)<V.\mathrm{cluster}[i].\max$}
    \RETURN $i\sqrt u+$ successor$(V.\mathrm{cluster}[i],\mathrm{low}(x))$
\ENDIF
\STATE $i'\gets$ successor$(V.\mathrm{summary},i)$
\IF{$i'$ is none}
    \RETURN none
\ENDIF
\RETURN $i'\sqrt u+V.\mathrm{cluster}[i'].\min$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-van-emde-boas-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,anchor=west] at (-0.10,1.60) {$V.\min=1$, $V.\max=15$};
\draw[cell frame] (1.600,0.600) rectangle (2.150,1.150);
\node[lab] at (1.875,0.875) {$0$};
\draw[cell frame] (2.150,0.600) rectangle (2.700,1.150);
\node[lab] at (2.425,0.875) {$0$};
\draw[hl cell] (2.700,0.600) rectangle (3.250,1.150);
\node[lab] at (2.975,0.875) {$1$};
\draw[cell frame] (3.250,0.600) rectangle (3.800,1.150);
\node[lab] at (3.525,0.875) {$1$};
\node[lab, anchor=east] at (1.500,0.875) {summary};
\draw[cell frame] (0.000,-0.500) rectangle (0.550,0.050);
\node[lab] at (0.275,-0.225) {$0$};
\draw[cell frame] (0.550,-0.500) rectangle (1.100,0.050);
\node[lab] at (0.825,-0.225) {$0$};
\draw[cell frame] (1.100,-0.500) rectangle (1.650,0.050);
\node[lab] at (1.375,-0.225) {$0$};
\draw[cell frame] (1.650,-0.500) rectangle (2.200,0.050);
\node[lab] at (1.925,-0.225) {$0$};
\node[lab,tick] at (1.10,0.25) {cluster $0$};
\node[lab,tick] at (1.10,-0.80) {empty};
\draw[cell frame] (2.900,-0.500) rectangle (3.450,0.050);
\node[lab] at (3.175,-0.225) {$0$};
\draw[cell frame] (3.450,-0.500) rectangle (4.000,0.050);
\node[lab] at (3.725,-0.225) {$0$};
\draw[cell frame] (4.000,-0.500) rectangle (4.550,0.050);
\node[lab] at (4.275,-0.225) {$0$};
\draw[cell frame] (4.550,-0.500) rectangle (5.100,0.050);
\node[lab] at (4.825,-0.225) {$0$};
\node[lab,tick] at (4.00,0.25) {cluster $1$};
\node[lab,tick] at (4.00,-0.80) {empty};
\draw[cell frame] (5.800,-0.500) rectangle (6.350,0.050);
\node[lab] at (6.075,-0.225) {$0$};
\draw[hl cell] (6.350,-0.500) rectangle (6.900,0.050);
\node[lab] at (6.625,-0.225) {$1$};
\draw[cell frame] (6.900,-0.500) rectangle (7.450,0.050);
\node[lab] at (7.175,-0.225) {$1$};
\draw[cell frame] (7.450,-0.500) rectangle (8.000,0.050);
\node[lab] at (7.725,-0.225) {$0$};
\node[lab,tick] at (6.90,0.25) {cluster $2$};
\node[lab,tick] at (6.90,-0.80) {min $1$, max $2$};
\draw[cell frame] (8.700,-0.500) rectangle (9.250,0.050);
\node[lab] at (8.975,-0.225) {$0$};
\draw[cell frame] (9.250,-0.500) rectangle (9.800,0.050);
\node[lab] at (9.525,-0.225) {$0$};
\draw[cell frame] (9.800,-0.500) rectangle (10.350,0.050);
\node[lab] at (10.075,-0.225) {$0$};
\draw[cell frame] (10.350,-0.500) rectangle (10.900,0.050);
\node[lab] at (10.625,-0.225) {$1$};
\node[lab,tick] at (9.80,0.25) {cluster $3$};
\node[lab,tick] at (9.80,-0.80) {min $3$, max $3$};
\end{tikzpicture}
\end{center}
```

The set $\{1,9,10,15\}$ of @fig-van-emde-boas-1 stored as in @def-veb, with $u=16$: the minimum $1$ is kept only in $V.\min$, so cluster $0$ is empty and the summary holds $2,3$. For `successor(V, 3)` the cluster of $3$ has nothing above $\mathrm{low}(3)=3$, so one recursive call on the summary finds the next non-empty cluster, $2$, and its stored minimum gives $9$ (highlighted).

:::

::: {#prp-veb-insert .proposition name="Insert in $O(\log\log u)$"}

`insert(V, x)`: if $V$ is empty, set $V.\min=V.\max=x$ and stop. If $x<V.\min$, swap $x$ and $V.\min$ (the new minimum stays only at the top). Let $i=\mathrm{high}(x)$; if $V.\mathrm{cluster}[i]$ is empty, insert $i$ into the summary and set the cluster's min and max to $\mathrm{low}(x)$ in $O(1)$; otherwise insert $\mathrm{low}(x)$ into the cluster. Update $V.\max$.

:::

::: {.proof}

The key point is that the minimum is not stored recursively. If the cluster was empty, inserting into the summary is the one recursive call, and filling the empty cluster costs $O(1)$ because a structure holding one element stores it only in its min and max. If the cluster was non-empty, the summary already lists it, and the one recursive call goes into the cluster. Either way $T(u)=T(\sqrt u)+O(1)$.

:::

```{=latex}
\begin{algorithm}
\caption{vEB insert$(V,x)$}
\begin{algorithmic}
\INPUT vEB structure $V$ for universe size $u$, an integer $x\notin V$
\IF{$V$ is empty}
    \STATE $V.\min\gets x$; $V.\max\gets x$
    \RETURN
\ENDIF
\IF{$x<V.\min$}
    \STATE swap $x$ and $V.\min$ \COMMENT{the minimum is stored only here}
\ENDIF
\STATE $i\gets\mathrm{high}(x)$
\IF{$V.\mathrm{cluster}[i]$ is empty}
    \STATE insert$(V.\mathrm{summary},i)$
    \STATE $V.\mathrm{cluster}[i].\min\gets\mathrm{low}(x)$; $V.\mathrm{cluster}[i].\max\gets\mathrm{low}(x)$ \COMMENT{$O(1)$}
\ELSE
    \STATE insert$(V.\mathrm{cluster}[i],\mathrm{low}(x))$
\ENDIF
\STATE $V.\max\gets\max\{V.\max,x\}$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-van-emde-boas-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,anchor=west] at (-0.10,1.60) {$V.\min=1$, $V.\max=15$};
\draw[cell frame] (1.600,0.600) rectangle (2.150,1.150);
\node[lab] at (1.875,0.875) {$0$};
\draw[hl cell] (2.150,0.600) rectangle (2.700,1.150);
\node[lab] at (2.425,0.875) {$1$};
\draw[cell frame] (2.700,0.600) rectangle (3.250,1.150);
\node[lab] at (2.975,0.875) {$1$};
\draw[cell frame] (3.250,0.600) rectangle (3.800,1.150);
\node[lab] at (3.525,0.875) {$1$};
\node[lab, anchor=east] at (1.500,0.875) {summary};
\draw[cell frame] (0.000,-0.500) rectangle (0.550,0.050);
\node[lab] at (0.275,-0.225) {$0$};
\draw[cell frame] (0.550,-0.500) rectangle (1.100,0.050);
\node[lab] at (0.825,-0.225) {$0$};
\draw[cell frame] (1.100,-0.500) rectangle (1.650,0.050);
\node[lab] at (1.375,-0.225) {$0$};
\draw[cell frame] (1.650,-0.500) rectangle (2.200,0.050);
\node[lab] at (1.925,-0.225) {$0$};
\node[lab,tick] at (1.10,0.25) {cluster $0$};
\node[lab,tick] at (1.10,-0.80) {empty};
\draw[hl cell] (2.900,-0.500) rectangle (3.450,0.050);
\node[lab] at (3.175,-0.225) {$1$};
\draw[cell frame] (3.450,-0.500) rectangle (4.000,0.050);
\node[lab] at (3.725,-0.225) {$0$};
\draw[cell frame] (4.000,-0.500) rectangle (4.550,0.050);
\node[lab] at (4.275,-0.225) {$0$};
\draw[cell frame] (4.550,-0.500) rectangle (5.100,0.050);
\node[lab] at (4.825,-0.225) {$0$};
\node[lab,tick] at (4.00,0.25) {cluster $1$};
\node[lab,tick] at (4.00,-0.80) {min $0$, max $0$};
\draw[cell frame] (5.800,-0.500) rectangle (6.350,0.050);
\node[lab] at (6.075,-0.225) {$0$};
\draw[cell frame] (6.350,-0.500) rectangle (6.900,0.050);
\node[lab] at (6.625,-0.225) {$1$};
\draw[cell frame] (6.900,-0.500) rectangle (7.450,0.050);
\node[lab] at (7.175,-0.225) {$1$};
\draw[cell frame] (7.450,-0.500) rectangle (8.000,0.050);
\node[lab] at (7.725,-0.225) {$0$};
\node[lab,tick] at (6.90,0.25) {cluster $2$};
\node[lab,tick] at (6.90,-0.80) {min $1$, max $2$};
\draw[cell frame] (8.700,-0.500) rectangle (9.250,0.050);
\node[lab] at (8.975,-0.225) {$0$};
\draw[cell frame] (9.250,-0.500) rectangle (9.800,0.050);
\node[lab] at (9.525,-0.225) {$0$};
\draw[cell frame] (9.800,-0.500) rectangle (10.350,0.050);
\node[lab] at (10.075,-0.225) {$0$};
\draw[cell frame] (10.350,-0.500) rectangle (10.900,0.050);
\node[lab] at (10.625,-0.225) {$1$};
\node[lab,tick] at (9.80,0.25) {cluster $3$};
\node[lab,tick] at (9.80,-0.80) {min $3$, max $3$};
\end{tikzpicture}
\end{center}
```

Inserting $4$ into the structure of @fig-van-emde-boas-2. Its cluster $1$ was empty, so the only recursive call inserts $1$ into the summary; the new cluster just records $\min=\max=0$ in $O(1)$ (highlighted). Had the cluster been non-empty, the only recursive call would insert into the cluster instead.

:::

Deletion is similar: when the cluster becomes empty, the second recursive call (deleting from the summary) happens only when the first one removed the last element, which was then an $O(1)$ call. So all three operations take $O(\log\log u)$ time.

::: {#rmk-van-emde-boas-space .remark name="Space"}

The plain structure uses $\Theta(u)$ space. Storing only the non-empty clusters, in a hash table keyed by cluster index (@sec-cs-data-structures-hashing), reduces the space to $O(n\log\log u)$, and with further tricks to $O(n)$, at the price of making the time bounds expected.

:::
