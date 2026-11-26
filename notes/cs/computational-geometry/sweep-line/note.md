---
title: "Sweep Line: Area of a Union of Rectangles"
sources: [cs97si-9]
requires: [cs/sorting/merge-sort]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 9, in our own wording; proofs written out in steps. The example is our own. -->

A *sweep line* turns a two-dimensional problem into a sequence of one-dimensional ones. A vertical line moves from left to right; the answer changes only at finitely many *events*, and between two events the line sees a fixed situation, kept in a data structure. Each problem needs its own events and its own structure; the area of a union of rectangles is the standard first example.

::: {#def-rectangle-union-sweep .definition name="Union of rectangles by a sweep"}

Given $n$ axis-parallel rectangles $[x^-_i,x^+_i]\times[y^-_i,y^+_i]$, sort the $2n$ values $x^\pm_i$ into $x_{(1)}\le\dots\le x_{(2n)}$. Between consecutive events $x_{(k)}<x_{(k+1)}$ the *active* rectangles are those with $x^-_i\le x_{(k)}$ and $x^+_i\ge x_{(k+1)}$; let $L_k$ be the total length of the union of their $y$-intervals. Return

$$
\sum_{k=1}^{2n-1}L_k\,\bigl(x_{(k+1)}-x_{(k)}\bigr).
$$

:::

```{=latex}
\begin{algorithm}
\caption{Area of a union of rectangles}
\begin{algorithmic}
\INPUT Rectangles $[x^-_i,x^+_i]\times[y^-_i,y^+_i]$, $i=1,\dots,n$
\OUTPUT The area of their union
\STATE events $\gets$ the $2n$ pairs $(x^-_i,\text{open }i)$ and $(x^+_i,\text{close }i)$, sorted by $x$
\STATE $Y\gets$ empty list of active $y$-intervals, kept sorted by lower end; $A\gets0$
\FOR{each event $(x,\cdot)$ in order, with $x'$ the previous event's $x$}
    \STATE $A\gets A+(x-x')\cdot\operatorname{length}(\bigcup Y)$ \COMMENT{one pass over $Y$}
    \STATE insert or remove interval $i$ in $Y$
\ENDFOR
\RETURN $A$
\end{algorithmic}
\end{algorithm}
```

The union length of a list of intervals sorted by lower end is found in one pass: keep a current merged interval $[a,b]$; for the next interval $[c,d]$, extend $b$ to $\max(b,d)$ if $c\le b$, otherwise add $b-a$ to the total and start a new merged interval $[c,d]$.

::: {#thm-rectangle-union-sweep .theorem name="Correctness and cost"}

The sweep returns the area of the union in $O(n^2)$ time.

:::

::: {.proof}

1. *Slabs.* The vertical lines $x=x_{(k)}$ cut the plane into slabs. Inside the open slab $x_{(k)}<x<x_{(k+1)}$ no rectangle starts or ends, so a rectangle meets the slab exactly when it is active, and then it covers the whole width of the slab.

2. *One slab.* So the union restricted to the slab is (union of the active $y$-intervals) $\times\,(x_{(k)},x_{(k+1)})$, whose area is $L_k(x_{(k+1)}-x_{(k)})$. Summing over slabs gives the area of the union, since the slab boundaries have area zero.

3. *Merging.* The merged interval $[a,b]$ is always covered by the intervals absorbed so far. When the next interval starts at $c>b$, every later interval starts at a value $\ge c>b$ too, since the list is sorted by lower end. So $[a,b]$ is a maximal piece of the union, and the union length is the sum of the lengths of these pieces.

4. *Cost.* Sorting the events costs $O(n\log n)$. Each of the $2n$ events inserts or removes one interval in a sorted list ($O(n)$) and runs one merging pass ($O(n)$), so the total is $O(n^2)$.

:::

::: {#exm-sweep-line-1 .example name="Three rectangles"}

For $R_1=[0,4]\times[0,3]$, $R_2=[2,6]\times[1,5]$, $R_3=[5,7]\times[0,2]$ the events are $x=0,2,4,5,6,7$. The slabs have widths $2,2,1,1,1$ and union lengths $L=3,5,4,5,2$ (for example on $[2,4]$ the active intervals $[0,3]$ and $[1,5]$ merge to $[0,5]$). The area is $6+10+4+5+2=27$.

:::

::: {#fig-sweep-line-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.7]
\draw[gridline] (-0.3,-0.3) grid (7.3,5.3);
\fill[tintA] (0,0) rectangle (4,3);
\fill[tintB] (2,1) rectangle (6,5);
\fill[tintC] (5,0) rectangle (7,2);
\draw[emph] (0,0) rectangle (4,3); \draw[emph] (2,1) rectangle (6,5); \draw[emph] (5,0) rectangle (7,2);
\node[lab] at (1,1.5) {$R_1$}; \node[lab] at (4,4) {$R_2$}; \node[lab] at (6.5,0.6) {$R_3$};
\draw[hl] (3,-0.6) -- (3,5.6) node[lab,above] {sweep};
\draw[hl] (3.25,0) -- (3.25,5);
\foreach \x/\L/\y in {1/3/-0.8,3/5/-0.8,4.5/4/-1.4,5.5/5/-0.8,6.5/2/-1.4} \node[lab,tick] at (\x,\y) {$L=\L$};
\end{tikzpicture}
\end{center}
```

@exm-sweep-line-1: in the slab $[2,4]$ the sweep line meets $R_1$ and $R_2$, whose $y$-intervals merge into one interval of length $5$ (thick bar). The slab contributes $5\cdot2=10$.

:::

::: {#rmk-sweep-line-1 .remark name="Faster structures and other sweeps"}

Keeping the active intervals in a segment tree over the sorted $y$-values gives the union length in $O(\log n)$ per event and $O(n\log n)$ in total. The same pattern, with other events and structures, computes the perimeter of a union of rectangles, or reports all $k$ intersections among $n$ segments in $O((n+k)\log n)$ time (events at endpoints and crossings, a balanced search tree ordered by height on the sweep line).

:::
