---
title: "Linear Programming in Fixed Dimension: Seidel's Algorithm"
sources: [mit6854-22]
requires: [cs/computational-geometry/half-plane-intersection, math/combinatorial-optimization/polyhedra/vertices-of-polyhedra]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 22 (Section 1), in our own wording; the correctness proof (given in the preceding lecture, which is not in the published notes) is written out by us; the example is our own (checked by computation); proofs written out in steps. -->

When the number of variables $d$ is a small constant, a linear program with $n$ constraints can be solved in expected time $O(d!\,n)$ by a strikingly simple randomized algorithm (Seidel, 1991). The bound depends on $n$ and $d$ only, so for fixed $d$ the algorithm is strongly polynomial, which no algorithm is known to be for general linear programming. In the plane it gives an expected $O(n)$ algorithm, faster than intersecting all half-planes (@sec-cs-computational-geometry-half-plane-intersection).

## Setting

Let $H$ be a set of $n$ half-spaces $a_h^{\mathsf T}x\le b_h$ in $\mathbb R^d$ and $\mathrm{LP}(H)$ the problem of minimising $c^{\mathsf T}x$ over their intersection. Two assumptions simplify the description:

1. *bounded:* every $\mathrm{LP}(G)$, $G\subseteq H$, is bounded; add a large box $-M\le x_i\le M$, and if a box constraint is tight at the end, the original program is unbounded;
2. *non-degenerate:* no $d+1$ of the bounding hyperplanes meet in a point, and optima are unique (perturb, or break ties lexicographically).

Then each feasible $\mathrm{LP}(G)$ has a unique optimum $x(G)$, a vertex determined by exactly $d$ tight constraints (box faces included). A minimal $B\subseteq G$ with $x(B)=x(G)$ is a *basis*; it has at most $d$ elements of $H$.

::: {#lem-seidel-tight .lemma name="A violated constraint is tight"}

Let $h\in H$ and suppose $x(H\setminus\{h\})$ violates $h$. Then, if $\mathrm{LP}(H)$ is feasible, $h$ is tight at its optimum: $x(H)$ is the optimum of $\mathrm{LP}(H\setminus\{h\})$ restricted to the hyperplane $a_h^{\mathsf T}x=b_h$.

:::

::: {.proof}

1. Let $x'=x(H\setminus\{h\})$ and $x^*=x(H)$, so $c^{\mathsf T}x'\le c^{\mathsf T}x^*$ (fewer constraints), and $a_h^{\mathsf T}x'>b_h\ge a_h^{\mathsf T}x^*$.

2. Suppose $a_h^{\mathsf T}x^*<b_h$. If $c^{\mathsf T}x'<c^{\mathsf T}x^*$, the points $x^*+t(x'-x^*)$ for small $t>0$ satisfy every constraint of $H\setminus\{h\}$ (convexity) and still satisfy $h$ (it is strict at $x^*$), and they are cheaper than $x^*$: a contradiction.

3. If $c^{\mathsf T}x'=c^{\mathsf T}x^*$, then $x^*$ is also optimal for $\mathrm{LP}(H\setminus\{h\})$, and uniqueness gives $x^*=x'$, which violates $h$: again a contradiction. So $h$ is tight at $x^*$.

4. Hence $x^*$ minimises $c^{\mathsf T}x$ over $\{x:a_h^{\mathsf T}x=b_h\}\cap\bigcap_{g\ne h}g$, which is a program in $d-1$ variables after eliminating one variable with the equation.

:::

## The algorithm

::: {#def-seidel-lp .definition name="Seidel's algorithm"}

To solve $\mathrm{LP}(H)$ in dimension $d$:

1. If $d=1$, solve directly in $O(n)$ (an interval). If $H$ has no constraints besides the box, return the best box corner.
2. Choose $h\in H$ uniformly at random and solve $\mathrm{LP}(H\setminus\{h\})$ recursively, giving $x$.
3. If $x$ satisfies $h$, return $x$.
4. Otherwise use the equation $a_h^{\mathsf T}x=b_h$ to eliminate one variable from all other constraints and the objective, solve the resulting problem in dimension $d-1$ with $n-1$ constraints recursively, and lift its solution back.

:::

```{=latex}
\begin{algorithm}
\caption{Seidel's randomized LP}
\begin{algorithmic}
\INPUT half-spaces $H$ in $\mathbb R^d$ (plus a bounding box), objective $c$
\OUTPUT the optimum $x(H)$, or ``infeasible''
\IF{$d=1$ or $H=\varnothing$}
\RETURN the optimum by direct computation
\ENDIF
\STATE choose $h\in H$ uniformly at random
\STATE $x\gets$ \textsc{Seidel}$(H\setminus\{h\},c)$
\IF{$x$ satisfies $h$}
\RETURN $x$
\ENDIF
\STATE eliminate one variable using $a_h^{\mathsf T}x=b_h$
\RETURN \textsc{Seidel}$(H\setminus\{h\}$ restricted to the hyperplane, $c$ restricted$)$
\end{algorithmic}
\end{algorithm}
```

By @lem-seidel-tight the algorithm is correct. The analysis looks *backwards*: instead of asking whether the new constraint is violated, ask how likely the last constraint added is one of the few that determine the final optimum.

::: {#thm-seidel-lp .theorem name="Running time of Seidel's algorithm"}

The expected running time $T(d,n)$ satisfies
$$T(d,n)\le T(d,n-1)+\frac dn\Big(O(dn)+T(d-1,n-1)\Big)+O(d),$$
and $T(d,n)=O(d!\,n)$.

:::

::: {.proof}

1. Step 2 costs $T(d,n-1)$ and the test in step 3 costs $O(d)$.

2. *Backward analysis.* $x(H)$ is determined by at most $d$ constraints of $H$ (its basis). The recursive optimum $x(H\setminus\{h\})$ differs from $x(H)$ only if $h$ belongs to that basis, and $h$ is uniform among $n$ constraints, so step 4 runs with probability at most $d/n$.

3. Step 4 costs $O(dn)$ for the elimination plus $T(d-1,n-1)$. This gives the recurrence.

4. Multiplying out, $T(d,n)\le T(d,n-1)+\tfrac dnT(d-1,n-1)+O(d^2)$. By induction on $d+n$ one checks $T(d,n)\le C\,d!\,n\sum_{i=1}^di^2/i!$: substituting, the main terms give $C\,d!\,(n-1)\sum_{i\le d}\tfrac{i^2}{i!}+C\,d!\,\tfrac{n-1}n\sum_{i\le d-1}\tfrac{i^2}{i!}$, and the deficit $C\,d!\sum_{i\le d}\tfrac{i^2}{i!}-C\,d!\tfrac{n-1}{n}\sum_{i\le d-1}\tfrac{i^2}{i!}\ge C\,d!\,\tfrac{d^2}{d!}=Cd^2$ absorbs the $O(d^2)$ term.

5. As $\sum_{i\ge1}i^2/i!=2e$ is finite, $T(d,n)=O(d!\,n)$.

:::

::: {#exm-seidel-lp .example name="A small planar program"}

Minimise $-2x-y$ subject to $h_1:x\le3$, $h_2:y\le2$, $h_3:x+y\le4$ (and a large box). Suppose $h_3$ is the constraint removed at the top. The optimum of $\{h_1,h_2\}$ is $(3,2)$ with value $-8$; it violates $h_3$. On the line $x+y=4$ the objective is $-x-4$, and $h_1,h_2$ become $2\le x\le3$, a one-dimensional program with optimum $x=3$: the answer is $(3,1)$, value $-7$. Had $h_2$ been removed at the top instead, the optimum $(3,1)$ of $\{h_1,h_3\}$ already satisfies $y\le2$ and is returned at once. Only $h_1$ and $h_3$ form the basis, so the expensive branch is taken with probability $2/3$ at the top level.

:::

::: {#fig-seidel-lp-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[->, faint] (-0.3,0)--(4.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3)--(0,3) node[lab, above] {$y$};
\fill[tintA] (0,0)--(3,0)--(3,1)--(2,2)--(0,2)--cycle;
\draw[emph] (3,-0.3)--(3,2.8) node[lab, above] {$h_1$};
\draw[emph] (-0.3,2)--(4,2) node[lab, right] {$h_2$};
\draw[hl] (0.5,3.5)--(4,0) node[lab, right] {$h_3$};
\node[dot] at (3,2) {};
\node[lab, above right] at (3,2) {$(3,2)$};
\node[hl dot] at (3,1) {};
\node[lab, right] at (3.05,0.9) {$(3,1)$};
\end{tikzpicture}
\end{center}
```

Seidel's algorithm on the example: without $h_3$ the optimum is $(3,2)$; it violates $h_3$, so the optimum lies on the line of $h_3$, found by a one-dimensional program: $(3,1)$.

:::

::: {#rmk-seidel-lp-1 .remark name="Subexponential in the dimension"}

The factor $d!$ grows fast. Matoušek, Sharir and Welzl keep a candidate basis and recurse more cleverly, getting expected $e^{O(\sqrt{d\log n})}$ time, subexponential in $d$; combined with Clarkson's random sampling this gives $O(d^2n+e^{O(\sqrt{d\log d})})$, still the best bound independent of the sizes of the numbers. The same scheme solves other *LP-type problems*, such as the smallest enclosing ball of $n$ points.

:::
