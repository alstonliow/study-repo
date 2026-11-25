---
title: "Dynamic Arrays"
sources: [mit6006-2, mit6006r-2]
requires: [cs/data-structures/linked-lists-and-dynamic-arrays]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 2 and Recitation 2, in our own wording; proofs written out in steps. Split from cs/data-structures/linked-lists-and-dynamic-arrays on 2026-11-25 (one data structure per note, SPEC §8.6). -->

A dynamic array keeps the fast reads of an array and makes the operations at the end fast as well, by allocating more room than it needs.

::: {#def-dynamic-array .definition name="Dynamic array"}

A *dynamic array* stores the $n$ items in the first $n$ slots of a static array of some length $m\ge n$. `insert_last(x)` writes $x$ into slot $n$ if $n<m$; if the array is full ($n=m$), it first allocates a new array of length $2m$ (length $1$ if $m=0$), copies the items over, and frees the old one. `delete_last()` simply forgets the last item. Python's `list` is a dynamic array.

:::

```{=latex}
\begin{algorithm}
\caption{Dynamic array insert\_last}
\begin{algorithmic}
\INPUT Static array $A$ of length $m$ holding $n$ items; new item $x$
\IF{$n=m$}
    \STATE $B\gets$ new static array of length $\max\{1,2m\}$
    \STATE copy $A[0..n-1]$ to $B[0..n-1]$; $A\gets B$; $m\gets\max\{1,2m\}$
\ENDIF
\STATE $A[n]\gets x$; $n\gets n+1$
\end{algorithmic}
\end{algorithm}
```

A single `insert_last` can take $\Theta(n)$ time, but such expensive steps are rare. To capture this we average over a sequence of operations.

::: {#def-amortized-cost .definition name="Amortized cost"}

An operation has *amortized cost* $T(n)$ if, for every $k$, any sequence of $k$ operations, starting from an empty structure, takes at most $k\,T(n)$ time in total.

:::

::: {#thm-dynamic-array-append .theorem name="Appending is constant amortized time"}

Starting from an empty dynamic array, any sequence of $k$ `insert_last` operations takes $O(k)$ time. So `insert_last` takes $O(1)$ amortized time.

:::

::: {.proof}

1. Each operation does $O(1)$ work besides copying. Copying happens only when the array is full, at sizes $n=1,2,4,\dots,2^j$ with $2^j<k$, and copying $n$ items costs $O(n)$.

2. The total copying cost is at most a constant times $1+2+4+\dots+2^j=2^{j+1}-1<2k$ (geometric sum, @exm-well-ordering-geometric-sum).

3. So the $k$ operations cost $O(k)+O(2k)=O(k)$ in total.

:::

::: {#fig-linked-lists-and-dynamic-arrays-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\node[lab, anchor=east] at (-0.100,0.275) {length 1};
\draw[cell frame] (0.000,-0.850) rectangle (0.550,-0.300);
\node[lab] at (0.275,-0.575) {$1$};
\draw[hl cell] (0.550,-0.850) rectangle (1.100,-0.300);
\node[lab] at (0.825,-0.575) {$2$};
\node[lab, anchor=east] at (-0.100,-0.575) {length 2};
\draw[cell frame] (0.000,-1.700) rectangle (0.550,-1.150);
\node[lab] at (0.275,-1.425) {$1$};
\draw[cell frame] (0.550,-1.700) rectangle (1.100,-1.150);
\node[lab] at (0.825,-1.425) {$2$};
\draw[cell frame] (1.100,-1.700) rectangle (1.650,-1.150);
\node[lab] at (1.375,-1.425) {$3$};
\draw[hl cell] (1.650,-1.700) rectangle (2.200,-1.150);
\node[lab] at (1.925,-1.425) {$4$};
\node[lab, anchor=east] at (-0.100,-1.425) {length 4};
\draw[cell frame] (0.000,-2.550) rectangle (0.550,-2.000);
\node[lab] at (0.275,-2.275) {$1$};
\draw[cell frame] (0.550,-2.550) rectangle (1.100,-2.000);
\node[lab] at (0.825,-2.275) {$2$};
\draw[cell frame] (1.100,-2.550) rectangle (1.650,-2.000);
\node[lab] at (1.375,-2.275) {$3$};
\draw[cell frame] (1.650,-2.550) rectangle (2.200,-2.000);
\node[lab] at (1.925,-2.275) {$4$};
\draw[hl cell] (2.200,-2.550) rectangle (2.750,-2.000);
\node[lab] at (2.475,-2.275) {$5$};
\draw[cell frame] (2.750,-2.550) rectangle (3.300,-2.000);
\draw[cell frame] (3.300,-2.550) rectangle (3.850,-2.000);
\draw[cell frame] (3.850,-2.550) rectangle (4.400,-2.000);
\node[lab, anchor=east] at (-0.100,-2.275) {length 8};
\node[lab, anchor=west] at (4.8,-1.0) {each row is a new array:};
\node[lab, anchor=west] at (4.8,-1.45) {the old items are copied over};
\end{tikzpicture}
\end{center}
```

Appending $1,2,\dots,5$ to a dynamic array. The array is reallocated only when full, at lengths $1,2,4,8$; the highlighted item is the one whose append triggered the copy (or, in the last row, the latest one). The copies cost $1+2+4<2\cdot5$ in total.

:::

::: {#rmk-linked-lists-and-dynamic-arrays-growth .remark name="Any constant factor works"}

Growing by any constant factor $c>1$ instead of $2$ also works: the copying costs form a geometric series with ratio $c$, summing to $O(k)$. Growing by a constant *amount* does not: copies at sizes $d,2d,3d,\dots$ cost $\Theta(k^2/d)$ in total.

:::

To keep the space linear when items are deleted, the array must also shrink, but shrinking as soon as it is half full would let alternating inserts and deletes at the boundary cost $\Theta(n)$ each.

::: {#prp-dynamic-array-shrink .proposition name="Shrinking without thrashing"}

Let a dynamic array double when full and, after a deletion, reallocate to length $2n$ whenever $n<m/4$. Then `insert_last` and `delete_last` take $O(1)$ amortized time and the array always has length $O(n)$ (for $n\ge1$).

:::

::: {.proof}

1. Right after any reallocation, and before the item that triggered a growth is written, the array is exactly half full: $n=m/2$.

2. The next reallocation happens when $n$ reaches $m$ or drops below $m/4$, so at least $m/4$ operations happen between two reallocations.

3. That reallocation copies at most $m$ items, which is $O(m/4)$, so it can be charged at $O(1)$ to each of the at least $m/4$ operations since the previous one. Every operation is charged by at most one reallocation, so $k$ operations cost $O(k)$ in total.

4. Between reallocations $m/4\le n\le m$, so $m\le4n$.

:::

```{=latex}
\begin{algorithm}
\caption{Dynamic array delete\_last with shrinking}
\begin{algorithmic}
\INPUT Static array $A$ of length $m$ holding $n\ge1$ items
\STATE $x\gets A[n-1]$; $n\gets n-1$
\IF{$n<m/4$}
    \STATE reallocate $A$ to length $2n$, copying the $n$ items; $m\gets2n$
\ENDIF
\RETURN $x$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-linked-lists-and-dynamic-arrays-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$x_0$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$x_1$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$x_2$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$x_3$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$x_4$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$x_5$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$x_6$};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$x_7$};
\node[lab,tick,anchor=west] at (4.70,0.28) {start: full};
\draw[cell frame] (0.000,-0.720) rectangle (0.550,-0.170);
\node[lab] at (0.275,-0.445) {$x_0$};
\draw[cell frame] (0.550,-0.720) rectangle (1.100,-0.170);
\node[lab] at (0.825,-0.445) {$x_1$};
\draw[cell frame] (1.100,-0.720) rectangle (1.650,-0.170);
\draw[cell frame] (1.650,-0.720) rectangle (2.200,-0.170);
\draw[cell frame] (2.200,-0.720) rectangle (2.750,-0.170);
\draw[cell frame] (2.750,-0.720) rectangle (3.300,-0.170);
\draw[cell frame] (3.300,-0.720) rectangle (3.850,-0.170);
\draw[cell frame] (3.850,-0.720) rectangle (4.400,-0.170);
\node[lab,tick,anchor=west] at (4.70,-0.44) {after $6$ deletes: $n=2=m/4$, no shrink};
\draw[cell frame] (0.000,-1.440) rectangle (0.550,-0.890);
\node[lab] at (0.275,-1.165) {$x_0$};
\draw[cell frame] (0.550,-1.440) rectangle (1.100,-0.890);
\node[lab,tick,anchor=west] at (4.70,-1.17) {delete: $n=1<m/4$, reallocate to $2n=2$};
\draw[cell frame] (0.000,-2.160) rectangle (0.550,-1.610);
\node[lab] at (0.275,-1.885) {$x_0$};
\draw[cell frame] (0.550,-2.160) rectangle (1.100,-1.610);
\node[lab] at (0.825,-1.885) {$x_1$};
\node[lab,tick,anchor=west] at (4.70,-1.89) {insert: room left};
\draw[cell frame] (0.000,-2.880) rectangle (0.550,-2.330);
\node[lab] at (0.275,-2.605) {$x_0$};
\draw[cell frame] (0.550,-2.880) rectangle (1.100,-2.330);
\node[lab] at (0.825,-2.605) {$x_1$};
\draw[cell frame] (1.100,-2.880) rectangle (1.650,-2.330);
\node[lab] at (1.375,-2.605) {$x_2$};
\draw[cell frame] (1.650,-2.880) rectangle (2.200,-2.330);
\node[lab,tick,anchor=west] at (4.70,-2.60) {insert: full, double to $4$};
\end{tikzpicture}
\end{center}
```

Deleting from a full array of length $8$ (empty cells are unused room). It shrinks only when fewer than a quarter of the slots are used, and then to twice the number of items, so the array is half full afterwards. One more insertion fits without copying, and a later doubling is again far away: inserts and deletes at the boundary cannot cause a copy each time.

:::
