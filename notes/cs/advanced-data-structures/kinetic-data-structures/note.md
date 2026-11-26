---
title: "Kinetic Data Structures"
sources: [mit6851-4]
requires: [cs/data-structures/binary-heaps]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 4, in our own wording; proofs written out in steps. Only the framework, kinetic sorting and the kinetic heap are covered; the survey of other results is a remark. -->

A kinetic data structure maintains a structure on points that move, such as the sorted order or the minimum, while time advances, by keeping a proof of correctness (certificates) and repairing the structure when a certificate fails.

::: {#def-kinetic .definition name="Kinetic data structure"}

Objects follow *trajectories*: affine $f(t)=a+bt$, bounded-degree polynomial, or pseudo-algebraic (any certificate changes truth value $O(1)$ times). The operations are $\operatorname{advance}(t)$, which moves the current time to $t$, and $\operatorname{change}(x,f)$, which replaces the trajectory of $x$, plus the queries of the underlying structure. A *certificate* is a boolean condition on the objects whose truth guarantees that the stored structure is correct. For each certificate the *failure time* (the first time after now it becomes false) is computed and kept in a priority queue; $\operatorname{advance}(t)$ processes the failures in time order and repairs the structure and its certificates at each.

:::

The quality of a kinetic structure is measured by four numbers:

* *responsiveness*: the time to repair after one certificate failure;
* *locality*: the largest number of certificates one object takes part in;
* *compactness*: the total number of certificates;
* *efficiency*: the ratio of the worst-case number of events (certificate failures) to the number of changes of the answer that are unavoidable for the problem.

::: {#prp-kinetic-sorting .proposition name="Kinetic sorting (predecessor)"}

Keep the objects in a balanced search tree in value order, with the certificates $x_i<x_{i+1}$ for the in-order neighbours. When $x_i<x_{i+1}$ fails, swap the two in the tree, add the new certificate $x_{i+1}\le x_i$, and replace the certificates with the two outer neighbours. Then the structure has responsiveness $O(\log n)$ (a constant number of priority-queue operations), locality $O(1)$ (each object is in at most $2$ certificates), compactness $O(n)$ and efficiency $O(1)$: each pair of objects with affine trajectories swaps at most once, so there are $O(n^2)$ events, each of which is a change of the sorted order that any structure maintaining the order must also process.

:::

::: {#fig-kinetic-data-structures-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm,y=0.8cm]
\draw[->,faint] (0,0) -- (4.4,0) node[right] {$t$};
\draw[hl] (0,0.5) -- (4,3.5);
\draw (0,1.6) -- (4,1.6);
\draw (0,3.4) -- (4,0.2);
\node[lab] at (4.35,3.6) {$x_1$};
\node[lab] at (4.35,1.6) {$x_2$};
\node[lab] at (4.35,0.2) {$x_3$};
\fill[accent] (1.467,1.6) circle (0.06);
\fill[accent] (1.871,1.903) circle (0.06);
\fill[accent] (2.25,1.6) circle (0.06);
\end{tikzpicture}
\end{center}
```

Three affine trajectories. Each crossing of two lines is an event of kinetic sorting: the order of the three values changes at each marked point.

:::

::: {#thm-kinetic-heap .theorem name="Kinetic heap"}

Keep the objects in a binary heap ordered by value with the certificates "node $\le$ child" for every edge. When a child overtakes its parent, swap them (heap-up) and replace the certificates of the nodes around. Then responsiveness is $O(\log n)$, locality $O(1)$, compactness $O(n)$, and for affine trajectories there are at most $O(n\log n)$ events in total, so the efficiency is $O(\log n)$; $\operatorname{find-min}$ is the root.

:::

::: {.proof}

1. *Potential.* For a node $x$ and time $t$ let $\Phi(t,x)$ be the number of descendants of $x$ that overtake $x$ at some time after $t$, and $\Phi(t)=\sum_x\Phi(t,x)$. For a child $y$ of $x$ let $\Phi(t,x,y)$ count the descendants of $y$ (including $y$) that overtake $x$ after $t$, so that $\Phi(t,x)=\Phi(t,x,y)+\Phi(t,x,z)$ for the children $y,z$ of $x$.

2. *Bound.* $\Phi(t)\le\sum_x(\text{number of descendants of }x)=\sum_v(\text{number of ancestors of }v)=O(n\log n)$ in a balanced heap.

3. *Each event lowers $\Phi$ by $1$.* Suppose child $y$ overtakes its parent $x$ at time $t$, and $z$ is the other child of $x$. Only $x$ and $y$ exchange places. Afterwards, $\Phi(t^+,x)=\Phi(t,x,y)-1$ (the node $y$ no longer counts, since it has already overtaken $x$), and $\Phi(t^+,y)=\Phi(t,y)+\Phi(t,y,z)$ (the descendants of $z$ are now descendants of $y$).

4. After time $t$ the node $y$ stays above $x$ (affine trajectories cross once), so a descendant of $z$ that overtakes $y$ later also overtakes $x$ later. Hence $\Phi(t,y,z)\le\Phi(t,x,z)=\Phi(t,x)-\Phi(t,x,y)$.

5. Adding up, $\Phi(t^+,x)+\Phi(t^+,y)\le\Phi(t,x,y)-1+\Phi(t,y)+\Phi(t,x)-\Phi(t,x,y)=\Phi(t,x)+\Phi(t,y)-1$, and no other node's value changes. So $\Phi$ drops by at least $1$ per event and the number of events is at most the initial $\Phi=O(n\log n)$.

:::

::: {#rmk-kinetic-data-structures-1 .remark name="Other results"}

For the convex hull of moving points in the plane (and diameter and minimum-area rectangle) the efficiency is $O(n^{\varepsilon})$ with a lower bound $\Omega(n^2)$ on events; the smallest enclosing disk has $O(n^3)$ events; Delaunay triangulations have $O(1)$ efficiency with between $\Omega(n^2)$ and $O(n^3)$ events; any triangulation needs $\Omega(n^2)$ changes. Several of these are open. These statements are quoted from the lecture.

:::
