---
title: "Vertices and Basic Feasible Solutions"
sources: [mit18433-3]
requires: [math/combinatorial-optimization/polyhedra/faces-of-polyhedra]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on polyhedral theory and linear programming (Section 3.3, vertices, basic feasible solutions, and polytopes as convex hulls), in our own wording; example our own (checked by computation); proofs written out in steps. -->

As in @sec-math-combinatorial-optimization-polyhedra-faces-of-polyhedra, $P=\{x\in\mathbb R^n:Ax\le b\}$ with rows $a_i^{\mathsf T}x\le b_i$. A vertex (@def-polyhedron-face) is the same as an *extreme point*: a point of $P$ that is not $\lambda y+(1-\lambda)z$ for distinct $y,z\in P$ and $0<\lambda<1$.

::: {#thm-vertex-unique-solution .theorem name="A vertex is fixed by its tight rows"}

If $x^*$ is a vertex of $P$ and $I=\{i:a_i^{\mathsf T}x^*=b_i\}$, then $x^*$ is the unique solution of the equations $a_i^{\mathsf T}x=b_i$ ($i\in I$).

:::

::: {.proof}

1. By @thm-faces-tight-rows, the face $\{x^*\}$ is $F_J$ for some $J$; the rows of $J$ are tight at $x^*$, so $J\subseteq I$ and $F_I\subseteq F_J=\{x^*\}$. Thus $x^*$ is the only point of $P$ satisfying the rows of $I$ with equality.

2. Suppose $\hat x\ne x^*$ also solves $a_i^{\mathsf T}x=b_i$ for $i\in I$. For $i\notin I$ we have $a_i^{\mathsf T}x^*<b_i$, so for small $\varepsilon>0$ the point $(1-\varepsilon)x^*+\varepsilon\hat x$ still satisfies these rows strictly.

3. That point satisfies the rows of $I$ with equality, so it lies in $F_I=\{x^*\}$; but it differs from $x^*$. This contradiction proves uniqueness.

:::

In particular, a vertex satisfies $n$ linearly independent rows with equality, and $P$ has finitely many vertices.

::: {#def-basic-feasible-solution .definition name="Basic feasible solution"}

Let $Q=\{x\in\mathbb R^n:Ax=b,\ x\ge0\}$ with $A\in\mathbb R^{m\times n}$ of rank $m$. A *basis* is a set $B$ of $m$ column indices with $A_B$ invertible; the other indices $N$ are *non-basic*. The *basic solution* of $B$ is $x_B=A_B^{-1}b$, $x_N=0$; it is a *basic feasible solution* (bfs) if moreover $x_B\ge0$.

:::

::: {#prp-vertices-are-bfs .proposition name="Vertices are basic feasible solutions"}

The vertices of $Q$ are exactly its basic feasible solutions.

:::

::: {.proof}

1. Let $x^*$ be a vertex of $Q$ (viewed as a polyhedron with rows $Ax\le b$, $-Ax\le-b$, $-x\le0$). By @thm-vertex-unique-solution, $x^*$ is the unique solution of $Ax=b$ together with $x_j=0$ for $j$ in the set $N_0=\{j:x^*_j=0\}$.

2. With $B_0$ the remaining indices, uniqueness says $A_{B_0}x_{B_0}=b$ has only one solution, so the columns of $A_{B_0}$ are linearly independent.

3. As $\operatorname{rank}A=m$, these columns can be extended by further columns to a basis $B\supseteq B_0$ of $m$ columns. The basic solution of $B$ solves $Ax=b$ with zeros outside $B\supseteq B_0$, so it is $x^*$. Hence $x^*$ is a bfs.

4. Conversely, a bfs $x$ of basis $B$ is the unique solution of $Ax=b$, $x_j=0$ ($j\in N$), because $A_B$ is invertible. If $x=\lambda y+(1-\lambda)z$ with $y,z\in Q$ and $0<\lambda<1$, then $y_j=z_j=0$ for $j\in N$ (they are $\ge0$ and average to $0$), so $y=z=x$ by uniqueness. Thus $x$ is an extreme point.

:::

Different bases can give the same vertex, when the vertex has more than $n-m$ zero coordinates.

::: {#exm-bfs-small .example name="Basic feasible solutions of a small system"}

Take $Q=\{x\in\mathbb R^3: x_1+x_2+x_3=2,\ x_1-x_2=0,\ x\ge0\}$, so $m=2$. The bases are $\{1,2\}$, $\{1,3\}$, $\{2,3\}$. Basis $\{1,2\}$ gives $x=(1,1,0)$; bases $\{1,3\}$ and $\{2,3\}$ both give $x=(0,0,2)$ (a degenerate vertex). So $Q$ is the segment between its two vertices $(1,1,0)$ and $(0,0,2)$.

:::

::: {#fig-vertices-of-polyhedra-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0.0,0.0) -- (-2.34,-1.56) node[lab, below left] {$x_1$};
\draw[->, faint] (0.0,0.0) -- (3.90,0.00) node[lab, right] {$x_2$};
\draw[->, faint] (0.0,0.0) -- (0.00,3.90) node[lab, above] {$x_3$};
\fill[tintA] (-1.80,-1.20) -- (3.00,0.00) -- (0.00,3.00) -- cycle;
\draw[faint] (-1.80,-1.20) -- (3.00,0.00) -- (0.00,3.00) -- cycle;
\draw[hl] (0.60,-0.60) -- (0.00,3.00);
\node[hl dot] at (0.60,-0.60) {}; \node[hl dot] at (0.00,3.00) {};
\node[lab, below] at (0.60,-0.60) {$(1,1,0)$}; \node[lab, right] at (0.00,3.00) {$(0,0,2)$};
\end{tikzpicture}
\end{center}
```

The example: the plane $x_1+x_2+x_3=2$ meets $x\ge0$ in a triangle (shaded); the second equation $x_1=x_2$ cuts it down to the segment $Q$ between its two basic feasible solutions.

:::

::: {#cor-minimal-faces-are-vertices .corollary name="Minimal faces are vertices"}

If $\operatorname{rank}A=n$, the inclusion-wise minimal non-trivial faces of a non-empty polyhedron $P=\{x:Ax\le b\}$ are its vertices. Hence an LP $\max\{c^{\mathsf T}x:x\in P\}$ that is feasible and bounded has an optimal solution at a vertex.

:::

::: {.proof}

1. Let $F$ be a minimal non-trivial face. By @thm-faces-tight-rows, $F=F_I$ for some $I$, and we may take $I$ maximal; then adding any row to $I$ makes $F_I$ empty.

2. *Case $F=\{x:a_i^{\mathsf T}x=b_i,\ i\in I\}$.* For $j\notin I$, the row $a_j$ must be a linear combination of the rows $a_i$, $i\in I$: otherwise some solution of the equations of $I$ would also satisfy $a_j^{\mathsf T}x=b_j+1$, and it would lie in $F$ while violating row $j$. So the rows of $I$ span all rows, they have rank $n$, and the equations have a unique solution. So $F$ is a point, a vertex.

3. *Otherwise* some $j\notin I$ and some $\tilde x$ satisfy the equations of $I$ but $a_j^{\mathsf T}\tilde x>b_j$. Take any $\hat x\in F$ and move from $\hat x$ towards $\tilde x$, keeping the equations of $I$. At the largest $\lambda\in[0,1)$ for which $\lambda\tilde x+(1-\lambda)\hat x$ is still in $P$, some row $k\notin I$ becomes tight, so $F_{I\cup\{k\}}\ne\varnothing$, contradicting the maximality of $I$.

4. Steps 2 and 3 used only that $F_I\ne\varnothing$ and that adding any row to $I$ empties it. For the LP, the optimal set is a non-empty face $F_I$ (@thm-faces-tight-rows); enlarge $I$ to a maximal $I'\supseteq I$ with $F_{I'}\ne\varnothing$. Then $F_{I'}\subseteq F_I$ is a single point, a vertex, and it is optimal.

:::

The rank condition is needed: if $\operatorname{rank}A<n$, then $P$ has no vertices at all (exercise), for example a halfplane in $\mathbb R^2$.

::: {#thm-minkowski-polytope .theorem name="A bounded polyhedron is the convex hull of its vertices"}

If $P=\{x:Ax\le b\}$ is bounded and $X$ is its set of vertices, then $P=\operatorname{conv}(X)$.

:::

::: {.proof}

1. $X\subseteq P$ and $P$ is convex, so $\operatorname{conv}(X)\subseteq P$. Suppose some $\tilde x\in P$ is not in $\operatorname{conv}(X)$. Then the system $\sum_{v\in X}\lambda_vv=\tilde x$, $\sum_v\lambda_v=1$, $\lambda\ge0$ in the unknowns $\lambda$ has no solution.

2. By the theorem of the alternatives (@thm-theorem-of-alternatives, with free multipliers $c\in\mathbb R^n$ and $t\in\mathbb R$ for the equalities) there are $c,t$ with
$$t+c^{\mathsf T}v\ge0\ \text{ for all } v\in X,\qquad t+c^{\mathsf T}\tilde x<0 .$$

3. $P$ is bounded, so $\operatorname{rank}A=n$ (otherwise a non-zero $y$ with $Ay=0$ would give the unbounded line $\tilde x+\mathbb Ry$ in $P$), and $z^*=\min\{c^{\mathsf T}x:x\in P\}$ is finite.

4. By @cor-minimal-faces-are-vertices, the optimal face $\{x\in P:c^{\mathsf T}x=z^*\}$ contains a vertex $v$. But $c^{\mathsf T}v\ge-t>c^{\mathsf T}\tilde x\ge z^*$, so $v$ is not optimal: a contradiction.

:::

With @cor-polytope-hull-is-polyhedron this shows that polytopes, defined either way, are the same objects.
