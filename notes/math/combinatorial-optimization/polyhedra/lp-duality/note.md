---
title: "Linear Programming Duality"
sources: [mit18433-3]
requires: [math/combinatorial-optimization/polyhedra/farkas-lemma]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on polyhedral theory and linear programming (Section 3.2), in our own wording; example our own (checked by computation); proofs written out in steps. The same theorems appear for the standard form, without proof of strong duality, in @thm-weak-duality and @thm-strong-duality, and as a special case of Lagrange duality in @thm-weak-strong-duality and @prp-complementary-slackness; merge proposed to the owner (best-version rule). -->

::: {#def-lp-primal-dual .definition name="Primal and dual linear programs" related="def-dual-lp"}

For $A\in\mathbb R^{m\times n}$, $b\in\mathbb R^m$ and $c\in\mathbb R^n$, the *primal* and *dual* linear programs are
$$(P)\quad\max\{c^{\mathsf T}x: Ax\le b\},\qquad\qquad (D)\quad\min\{b^{\mathsf T}y: A^{\mathsf T}y=c,\ y\ge0\}.$$
A point satisfying the constraints is *feasible*. The optimum value of (P) is $-\infty$ if (P) is *infeasible* and $+\infty$ if it is *unbounded* (its objective takes arbitrarily large values); for (D) the conventions are reversed. The primal has $n$ variables, the dual has $m$, one per primal constraint.

:::

Other forms, such as $\min\{c^{\mathsf T}x:Ax=b,\ x\ge0\}$, reduce to this one by writing equalities as two inequalities and sign constraints as rows of $A$.

::: {#thm-lp-weak-duality .theorem name="Weak duality" related="thm-weak-duality"}

If $x$ is feasible for (P) and $y$ for (D), then
$$c^{\mathsf T}x\le b^{\mathsf T}y .$$
In particular, if (P) is unbounded then (D) is infeasible.

:::

::: {.proof}

$c^{\mathsf T}x=(A^{\mathsf T}y)^{\mathsf T}x=y^{\mathsf T}(Ax)\le y^{\mathsf T}b$, where the inequality uses $y\ge0$ and $Ax\le b$.

:::

::: {#thm-lp-strong-duality .theorem name="Strong duality" related="thm-strong-duality"}

If (P) and (D) are both feasible, then both have optimal solutions and
$$\max\{c^{\mathsf T}x:Ax\le b\}=\min\{b^{\mathsf T}y:A^{\mathsf T}y=c,\ y\ge0\}.$$

:::

::: {.proof}

1. Fix feasible $x^*$ for (P) and $y^*$ for (D). It suffices to find feasible $x,y$ with $c^{\mathsf T}x\ge b^{\mathsf T}y$: by weak duality they are then equal and both optimal. Suppose, for a contradiction, that the system
$$Ax\le b,\qquad A^{\mathsf T}y=c,\qquad -y\le0,\qquad -c^{\mathsf T}x+b^{\mathsf T}y\le0$$
in the unknowns $(x,y)$ has no solution.

2. By the theorem of the alternatives for mixed systems (@thm-theorem-of-alternatives with free multipliers for equalities, @sec-math-combinatorial-optimization-polyhedra-farkas-lemma) there are multipliers $s\ge0$ (for $Ax\le b$), $t\in\mathbb R^n$ free (for the equalities), $u\ge0$ (for $-y\le0$) and $v\ge0$ (for the last row) with
$$A^{\mathsf T}s-vc=0,\qquad At-u+vb=0,\qquad b^{\mathsf T}s+c^{\mathsf T}t<0 .$$
(The first two say the coefficients of $x$ and of $y$ vanish; the last says the right-hand side is negative.)

3. *Case $v=0$.* Then $A^{\mathsf T}s=0$ with $s\ge0$, so $y^*+\alpha s$ is dual feasible for every $\alpha\ge0$. Also $At=u\ge0$, so $A(x^*-\alpha t)\le b$ and $x^*-\alpha t$ is primal feasible. Weak duality gives $c^{\mathsf T}(x^*-\alpha t)\le b^{\mathsf T}(y^*+\alpha s)$, that is,
$$c^{\mathsf T}x^*-b^{\mathsf T}y^*\le\alpha\,(b^{\mathsf T}s+c^{\mathsf T}t).$$
The right side tends to $-\infty$ as $\alpha\to\infty$ while the left side is fixed: a contradiction.

4. *Case $v>0$.* Divide everything by $v$. Then $A^{\mathsf T}(s/v)=c$ with $s/v\ge0$, so $s/v$ is dual feasible; and $A(-t/v)=b-u/v\le b$, so $-t/v$ is primal feasible. Weak duality gives $c^{\mathsf T}(-t/v)\le b^{\mathsf T}(s/v)$, that is $b^{\mathsf T}s+c^{\mathsf T}t\ge0$: a contradiction.

5. So the system has a solution, and the two optimal values are attained and equal.

:::

If only one of (P), (D) is feasible, the other is infeasible and the feasible one is unbounded (exercise), so the equality of optimal values still holds with the conventions $\pm\infty$. If neither is feasible, the values are $-\infty$ and $+\infty$.

::: {#thm-lp-complementary-slackness .theorem name="Complementary slackness" related="prp-complementary-slackness"}

Let $x$ be feasible for (P) and $y$ for (D). Then both are optimal if and only if, for every row $i$,
$$y_i=0\quad\text{or}\quad a_i^{\mathsf T}x=b_i\qquad(\text{or both}).$$

:::

::: {.proof}

1. As in weak duality, $b^{\mathsf T}y-c^{\mathsf T}x=y^{\mathsf T}(b-Ax)=\sum_iy_i(b_i-a_i^{\mathsf T}x)$, a sum of nonnegative terms.

2. By weak and strong duality, $x$ and $y$ are both optimal exactly when this gap is $0$, that is, when every term $y_i(b_i-a_i^{\mathsf T}x)$ is $0$.

:::

::: {#exm-lp-duality-small .example name="Certifying an optimum"}

Maximise $x_1+x_2$ subject to $x_1+2x_2\le4$, $3x_1+x_2\le6$, $-x_1\le0$, $-x_2\le0$. The point $x=(\frac85,\frac65)$ makes the first two rows tight and has value $\frac{14}5$. The dual asks for $y\ge0$ with $y_1+3y_2-y_3=1$ and $2y_1+y_2-y_4=1$; complementary slackness forces $y_3=y_4=0$ (rows $3$ and $4$ are slack), and then $y=(\frac25,\frac15,0,0)$. Its value $4\cdot\frac25+6\cdot\frac15=\frac{14}5$ equals the primal value, which proves both optimal.

:::

::: {#fig-lp-duality-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2.8,0) -- (2.24,1.68) -- (0,2.8) -- cycle;
\draw[emph] (0,0) -- (2.8,0) -- (2.24,1.68) -- (0,2.8) -- cycle;
\draw[->, faint] (-0.2,0) -- (3.92,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-0.2) -- (0,3.64) node[lab, above] {$x_2$};
\node[hl dot] (v) at (2.24,1.68) {};
\draw[->, hl] (v) -- ++(0.7,0.7) node[lab, above right] {$c$};
\draw[->, emph] (v) -- ++(0.35,0.7) node[lab, above left] {$a_1$};
\draw[->, emph] (v) -- ++(0.95,0.32) node[lab, right] {$a_2$};
\node[lab, below left] at (v) {$(\tfrac85,\tfrac65)$};
\node[lab] at (0.98,0.98) {feasible};
\end{tikzpicture}
\end{center}
```

The example: the objective $c=(1,1)$ at the optimal vertex lies in the cone of the normals $a_1=(1,2)$ and $a_2=(3,1)$ of the two tight rows, $c=\frac25a_1+\frac15a_2$; these weights are the optimal dual solution.

:::

::: {#rmk-lp-duality-1 .remark name="Algorithms"}

The simplex method walks along vertices of the feasible region (@sec-math-combinatorial-optimization-polyhedra-vertices-of-polyhedra); no variant is known to run in polynomial time. The ellipsoid method (@sec-math-combinatorial-optimization-polyhedra-ellipsoid-method) and interior-point methods (@sec-math-optimization-algorithms-barrier-method) do.

:::
