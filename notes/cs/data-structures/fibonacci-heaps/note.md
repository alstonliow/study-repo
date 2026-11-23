---
title: "Fibonacci Heaps"
sources: [res-clrs-fibonacci-heaps]
requires: [cs/data-structures/binary-heaps, cs/data-structures/amortized-analysis, math/discrete/sequences/fibonacci]
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 19, in our own wording; proofs written out in steps. The example heaps are our own. -->

A binary heap (@sec-cs-data-structures-binary-heaps) does every priority queue operation in $O(\log n)$ time. Dijkstra's and Prim's algorithms call `decrease_key` once per edge but `delete_min` only once per vertex, so they would profit from a heap in which `decrease_key` is cheap even if `delete_min` is not. Fibonacci heaps make `insert`, `union` and `decrease_key` take $O(1)$ amortised time and `delete_min` $O(\log n)$. The trick is laziness: do as little as possible until `delete_min` forces a clean-up.

## Mergeable heaps

::: {#def-mergeable-heap .definition name="Mergeable heap"}

A *mergeable heap* is a min priority queue (@def-priority-queue) that also supports `union(H1, H2)`, which returns one heap holding the items of both and destroys $H_1$ and $H_2$. We also want `decrease_key(x, k)`, which lowers the key of the item $x$ (given by a pointer) to $k$, and `delete(x)`.

:::

| Operation | Binary heap (worst case) | Fibonacci heap (amortised) |
|---|---|---|
| `insert`, `find_min` | $O(\log n)$, $O(1)$ | $O(1)$, $O(1)$ |
| `delete_min`, `delete` | $O(\log n)$ | $O(\log n)$ |
| `union` | $O(n)$ | $O(1)$ |
| `decrease_key` | $O(\log n)$ | $O(1)$ |

## Structure and potential

::: {#def-fibonacci-heap .definition name="Fibonacci heap"}

A *Fibonacci heap* is a collection of rooted trees, each *min-heap ordered* (every node's key is at least its parent's key). The roots are kept in a circular doubly linked list, the *root list*, with a pointer to a root of minimum key. The children of each node are kept in the same kind of list, and every node stores its *degree* (number of children), its parent, and a *mark* bit. A node is *marked* if it has lost a child since it last became the child of another node; roots are unmarked.

:::

Doubly linked circular lists let us remove a node, or splice two lists together, in $O(1)$ time. For a heap $H$ write $t(H)$ for the number of trees and $m(H)$ for the number of marked nodes, and let $D(n)$ be an upper bound on the degree of any node in an $n$-item heap (we show $D(n)=O(\log n)$ at the end). The analysis uses the potential method (@def-potential-method) with
$$
\Phi(H)=t(H)+2\,m(H).
$$
An empty heap has $\Phi=0$ and $\Phi\ge0$ always, so the total amortised cost bounds the total actual cost. We scale one unit of potential to pay for the constant amount of work in $O(1)$ steps.

::: {#fig-fibonacci-heaps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[mk/.style={small vertex, fill=ink, text=white}]
\node[small vertex] (r1) at (0,0) {$23$};
\node[small vertex, fill=accentLight, draw=accent] (r2) at (1.4,0) {$3$};
\node[small vertex] (r3) at (3.4,0) {$17$};
\node[small vertex] (r4) at (4.8,0) {$24$};
\draw[<->, faint] (r1)--(r2); \draw[<->, faint] (r2)--(r3); \draw[<->, faint] (r3)--(r4);
\draw[<->, faint] (r4.north) to[bend right=12] (r1.north);
\node[small vertex] (a1) at (0.7,-1.0) {$18$};
\node[small vertex] (a2) at (1.4,-1.0) {$52$};
\node[small vertex] (a3) at (2.1,-1.0) {$38$};
\draw (r2)--(a1) (r2)--(a2) (r2)--(a3);
\node[mk] (b1) at (0.7,-2.0) {$39$};
\node[small vertex] (b3) at (2.1,-2.0) {$41$};
\draw (a1)--(b1) (a3)--(b3);
\node[small vertex] (c1) at (3.4,-1.0) {$30$};
\draw (r3)--(c1);
\node[mk] (d1) at (4.4,-1.0) {$26$};
\node[small vertex] (d2) at (5.2,-1.0) {$46$};
\draw (r4)--(d1) (r4)--(d2);
\node[small vertex] (e1) at (4.4,-2.0) {$35$};
\draw (d1)--(e1);
\node[lab] (mn) at (1.4,1.0) {min};
\draw[->] (mn)--(r2);
\end{tikzpicture}
\end{center}
```

A Fibonacci heap with $t(H)=4$ trees and $m(H)=2$ marked nodes (dark), so $\Phi(H)=8$. The roots form a circular list (thin arrows) with a pointer to the minimum $3$. Each tree is min-heap ordered; children lists are drawn as plain edges.

:::

## Lazy operations

::: {#prp-fibonacci-heap-lazy .proposition name="Insert, find-min and union"}

1. `insert(x)` adds a one-node tree to the root list and updates the min pointer.
2. `find_min()` returns the item at the min pointer.
3. `union(H1, H2)` splices the two root lists and keeps the smaller of the two minima.

Each takes $O(1)$ actual and amortised time.

:::

::: {.proof}

1. Each operation changes $O(1)$ pointers.

2. `insert` adds one tree and no mark, so $\Delta\Phi=1$. `find_min` changes nothing. For `union`, $t$ and $m$ of the result are the sums of those of $H_1,H_2$, so the potential is unchanged.

:::

Nothing is ever tidied up by these operations: after $n$ inserts the heap is a list of $n$ single nodes.

## Delete-min and consolidation

`delete_min` removes the minimum root $z$, moves each child of $z$ to the root list (unmarking it), and then *consolidates*: while two roots have the same degree, *link* them, making the root with the larger key a child of the other. Then it scans the remaining roots for the new minimum. To find equal degrees fast, use an array $A[0..D(n)]$ in which $A[d]$ holds the root of degree $d$ seen so far.

```{=latex}
\begin{algorithm}
\caption{Consolidate$(H)$}
\begin{algorithmic}
\INPUT a Fibonacci heap $H$ whose root list may contain roots of equal degree
\STATE $A[0..D(n)]\gets$ all empty
\FOR{each root $w$ of $H$}
    \STATE $x\gets w$; $d\gets$ degree$(x)$
    \WHILE{$A[d]$ is not empty}
        \STATE $y\gets A[d]$; if $y.\mathrm{key}<x.\mathrm{key}$, swap $x$ and $y$
        \STATE link: remove $y$ from the root list, make it a child of $x$, unmark $y$
        \STATE $A[d]\gets$ empty; $d\gets d+1$
    \ENDWHILE
    \STATE $A[d]\gets x$
\ENDFOR
\STATE rebuild the root list from the nonempty entries of $A$ and find the minimum
\end{algorithmic}
\end{algorithm}
```

::: {#prp-fibonacci-heap-delete-min .proposition name="Cost of delete-min"}

`delete_min` takes $O(D(n))$ amortised time.

:::

::: {.proof}

Let $H$ be the heap before the operation.

1. *Actual cost.* Moving the at most $D(n)$ children of $z$ takes $O(D(n))$ time. Consolidation starts with at most $t(H)-1+D(n)$ roots. Each link removes one root for good, so there are fewer links than roots, and the work, including the final scan of $A$, is $O(t(H)+D(n))$.

2. *Potential.* Afterwards the roots have distinct degrees in $0..D(n)$, so there are at most $D(n)+1$ of them. No node becomes marked. So $\Phi$ after is at most $D(n)+1+2m(H)$, while before it was $t(H)+2m(H)$.

3. *Amortised cost.* Scaling the potential so that one unit pays for one link or one root step, the amortised cost is at most
$$
O\bigl(t(H)+D(n)\bigr)+\bigl(D(n)+1+2m(H)\bigr)-\bigl(t(H)+2m(H)\bigr)=O(D(n)).
$$
The $t(H)$ term cancels: each tree pays for its own linking with the unit of potential it brought.

:::

::: {#fig-fibonacci-heaps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0,0) {$7$};
\node[small vertex] (b) at (0.8,0) {$21$};
\node[small vertex] (c) at (1.6,0) {$18$};
\node[small vertex] (d) at (2.4,0) {$52$};
\node[small vertex] (e) at (3.2,0) {$38$};
\node[small vertex] (e1) at (3.2,-0.9) {$41$};
\draw (e)--(e1);
\node[lab,tick] at (1.6,0.5) {root list (degrees $0,0,0,0,1$)};
\draw[emph,->] (3.8,-0.4) -- (4.6,-0.4);
\node[small vertex] (A) at (5.4,0) {$7$};
\node[small vertex] (A1) at (5.0,-0.9) {$21$};
\node[small vertex] (A2) at (5.8,-0.9) {$18$};
\node[small vertex] (A3) at (5.8,-1.8) {$52$};
\draw (A)--(A1) (A)--(A2) (A2)--(A3);
\node[small vertex] (E) at (7.0,0) {$38$};
\node[small vertex] (E1) at (7.0,-0.9) {$41$};
\draw (E)--(E1);
\node[lab,tick] at (6.2,0.5) {after linking: degrees $2$ and $1$};
\end{tikzpicture}
\end{center}
```

Consolidation of a root list of five trees, as left after a `delete_min`. $7$ and $21$ have degree $0$ and are linked, giving $7$ degree $1$. Then $18$ and $52$ are linked ($18$ on top), and the two degree-$1$ roots $7$ and $18$ are linked ($7$ on top). The root $38$ of degree $1$ finds $A[1]$ empty and stays. Every root now has a different degree.

:::

## Decrease-key and cascading cuts

To decrease the key of $x$: if $x$ is a root, or its new key is still at least its parent's key, nothing else is needed. Otherwise *cut* $x$: remove it from its parent's child list and add it to the root list, unmarked. Then look at the old parent $y$, and perform a *cascading cut*:

- if $y$ is a root, stop;
- if $y$ is unmarked, mark it and stop (it has lost its first child);
- if $y$ is marked, it has now lost a second child: cut $y$ too, and continue with its parent.

Finally update the min pointer. To `delete(x)`, decrease its key to $-\infty$ and call `delete_min`.

::: {#prp-fibonacci-heap-decrease-key .proposition name="Cost of decrease-key and delete"}

`decrease_key` takes $O(1)$ amortised time, and `delete` takes $O(D(n))$.

:::

::: {.proof}

1. *Actual cost.* Suppose the call makes $c$ cuts in all (the cut of $x$ and $c-1$ cascading cuts). Each takes $O(1)$ time, so the actual cost is $O(c)$.

2. *Trees.* Each cut adds one tree: $t$ grows by $c$.

3. *Marks.* Each cascading cut removes the mark of a marked node, and the cut of $x$ may remove one more. At most one node becomes marked, the place where the cascade stops. So $m$ changes by at most $-(c-1)+1=2-c$.

4. *Amortised cost.* $\Delta\Phi\le c+2(2-c)=4-c$, so the amortised cost is $O(c)+4-c=O(1)$ after scaling. Each marked node pays with its $2$ units for its own cascading cut (one unit for the work, one for the new tree).

5. `delete` is one `decrease_key` and one `delete_min`: $O(1)+O(D(n))$.

:::

::: {#fig-fibonacci-heaps-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[mk/.style={small vertex, fill=ink, text=white}]
\node[small vertex] (r) at (0,0) {$3$};
\node[mk] (y) at (0,-0.9) {$18$};
\node[small vertex] (s) at (-0.6,-1.8) {$25$};
\node[small vertex, fill=accentLight, draw=accent] (x) at (0.6,-1.8) {$39$};
\draw (r)--(y) (y)--(s) (y)--(x);
\node[lab,tick, anchor=north] at (0.6,-2.15) {key $\to5$};
\draw[emph,->] (1.6,-0.7) -- (2.6,-0.7);
\node[small vertex] (R) at (3.4,0) {$3$};
\node[small vertex, fill=accentLight, draw=accent] (X) at (4.3,0) {$5$};
\node[small vertex] (Y) at (5.2,0) {$18$};
\node[small vertex] (S) at (5.2,-0.9) {$25$};
\draw (Y)--(S);
\draw[<->, faint] (R)--(X); \draw[<->, faint] (X)--(Y);
\node[lab,tick] at (4.6,-1.7) {$39$ cut; its marked parent $18$ cut too};
\end{tikzpicture}
\end{center}
```

`decrease_key` of $39$ to $5$. The new key breaks heap order, so $39$ (now $5$) is cut to the root list. Its parent $18$ was already marked, having lost a child before, so it is cut as well and unmarked. The cascade stops at the root $3$.

:::

## Why the degrees stay logarithmic

The cascading cuts are there for one reason: a node may lose at most one child before it is cut itself, which keeps the trees bushy.

::: {#lem-fibonacci-heap-children .lemma name="Degrees of children"}

Let $x$ be a node of degree $k$, and let $y_1,\dots,y_k$ be its children in the order in which they were linked to $x$. Then $\operatorname{degree}(y_1)\ge0$ and $\operatorname{degree}(y_i)\ge i-2$ for $i\ge2$.

:::

::: {.proof}

1. When $y_i$ was linked to $x$, the nodes $y_1,\dots,y_{i-1}$ were already children of $x$, so $x$ had degree at least $i-1$.

2. Nodes are linked only when their degrees are equal, so $y_i$ also had degree at least $i-1$ then.

3. Since then $y_i$ has lost at most one child, since a second loss would have cut it from $x$. So its degree is now at least $i-2$.

:::

::: {#thm-fibonacci-heap-degree .theorem name="Degree bound"}

A node of degree $k$ in a Fibonacci heap has at least $f_{k+2}\ge\varphi^k$ descendants, counting itself, where $f$ is the Fibonacci sequence and $\varphi=(1+\sqrt5)/2$. Hence in an $n$-item heap every degree is at most $D(n)=\lfloor\log_\varphi n\rfloor=O(\log n)$.

:::

::: {.proof}

1. Let $s_k$ be the least number of nodes in a subtree whose root has degree $k$. Then $s_0=1=f_2$ and $s_1=2=f_3$, and $s_k$ is increasing in $k$.

2. For $k\ge2$, a root $x$ of degree $k$ with children as in @lem-fibonacci-heap-children has at least $1$ node for itself, $1$ for $y_1$, and $s_{i-2}$ for each $y_i$ with $i\ge2$. So
$$
s_k\ge2+\sum_{i=2}^{k}s_{i-2}\ge2+\sum_{i=2}^{k}f_i=1+\sum_{i=1}^{k}f_i
$$
by induction on $k$.

3. By induction, $1+\sum_{i=1}^{k}f_i=f_{k+2}$: for $k=0$ both sides are $1$, and adding $f_{k+1}$ to both sides of the case $k$ gives $f_{k+2}+f_{k+1}=f_{k+3}$.

4. So $s_k\ge f_{k+2}\ge\varphi^k$ (@prp-fibonacci-2). A node of degree $k$ in an $n$-item heap has $n\ge\varphi^k$, so $k\le\log_\varphi n$.

:::

So all the $O(D(n))$ bounds above are $O(\log n)$, which completes the table.

::: {#rmk-fibonacci-heaps-1 .remark name="In practice"}

With a Fibonacci heap, Dijkstra's algorithm and Prim's algorithm run in $O(|E|+|V|\log|V|)$ time, which is better than $O(|E|\log|V|)$ with a binary heap when the graph is dense. The constant factors and the pointer-heavy layout make Fibonacci heaps slow in practice, though, and simpler heaps (binary or pairing heaps) usually win for real inputs. The name comes from @thm-fibonacci-heap-degree.

:::
