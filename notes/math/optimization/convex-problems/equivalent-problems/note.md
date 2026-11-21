---
title: "Equivalent Problems and Quasiconvex Optimization"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/optimization-problems, math/optimization/convex-functions/quasiconvex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. -->

Two problems are *equivalent* if a solution of one is readily obtained from a solution of the other. Standard transformations keep a problem convex while changing its form, and a quasiconvex problem reduces to a sequence of convex feasibility problems.

::: {#prp-standard-transformations .proposition name="Transformations that preserve convexity"}

Each of the following turns a convex problem into an equivalent convex problem.

1. *Eliminating equality constraints*: write $\{x\mid Ax=b\}=\{Fz+x_0\mid z\in\mathbb{R}^k\}$ and minimize $f_0(Fz+x_0)$ subject to $f_i(Fz+x_0)\le0$ over $z$.

2. *Introducing equality constraints*: replace $f_i(A_ix+b_i)$ by $f_i(y_i)$ and add $y_i=A_ix+b_i$.

3. *Slack variables*: replace $a_i^{\mathsf T}x\le b_i$ by $a_i^{\mathsf T}x+s_i=b_i$, $s_i\ge0$.

4. *Epigraph form*: minimize $t$ subject to $f_0(x)-t\le0$ and the original constraints, over $(x,t)$.

5. *Minimizing over some variables*: if $f_0(x_1,x_2)$ is jointly convex and only $x_1$ appears in the constraints, replace $f_0$ by $\tilde f_0(x_1)=\inf_{x_2}f_0(x_1,x_2)$, which is convex (@prp-partial-minimization).

:::

::: {.proof}

1. In each case the new constraint functions are convex or affine by the composition rules (@prp-nonnegative-sum-affine-composition): $f_i(Fz+x_0)$ is a convex function composed with an affine map, $f_0(x)-t$ is convex in $(x,t)$, and equality constraints added are affine.

2. Equivalence: feasible points correspond through the stated maps ($x=Fz+x_0$; $y_i=A_ix+b_i$; $s_i=b_i-a_i^{\mathsf T}x$; $t=f_0(x)$ at the optimum) with the same objective value.

:::

::: {#def-quasiconvex-problem .definition name="Quasiconvex optimization problem"}

A *quasiconvex optimization problem* has the form of @def-convex-optimization-problem with $f_0$ quasiconvex instead of convex. Its locally optimal points need not be globally optimal.

:::

::: {#def-quasiconvex-bisection .definition name="Bisection for quasiconvex problems"}

Represent the sublevel sets of $f_0$ by convex functions $\phi_t$, nonincreasing in $t$, with $f_0(x)\le t\iff\phi_t(x)\le0$. For fixed $t$ the *convex feasibility problem*
$$\text{find }x\quad\text{with}\quad\phi_t(x)\le0,\quad f_i(x)\le0,\quad Ax=b$$
is feasible iff $p^\star\le t$. Bisection: given $l\le p^\star\le u$ and $\epsilon>0$, repeat: $t:=(l+u)/2$; solve the feasibility problem; if it is feasible set $u:=t$, else $l:=t$; until $u-l\le\epsilon$.

:::

::: {#thm-bisection-iterations .theorem name="Bisection terminates"}

Bisection returns an interval $[l,u]$ of length at most $\epsilon$ containing $p^\star$ after exactly $\lceil\log_2((u_0-l_0)/\epsilon)\rceil$ feasibility problems, where $[l_0,u_0]$ is the starting interval.

:::

::: {.proof}

1. Invariant: $l\le p^\star\le u$. It holds initially; if the problem at $t$ is feasible then $p^\star\le t$ and setting $u=t$ keeps it; if infeasible then $p^\star>t$ and setting $l=t$ keeps it.

2. Each step halves $u-l$, so after $k$ steps $u-l=(u_0-l_0)2^{-k}$, which is at most $\epsilon$ once $k\ge\log_2((u_0-l_0)/\epsilon)$.

:::

```{=latex}
\begin{algorithm}
\caption{Bisection for a quasiconvex problem}
\begin{algorithmic}
\INPUT $l\le p^\star\le u$, tolerance $\epsilon>0$
\WHILE{$u-l>\epsilon$}
  \STATE $t\gets(l+u)/2$
  \IF{the convex feasibility problem at $t$ is feasible}
    \STATE $u\gets t$
  \ELSE
    \STATE $l\gets t$
  \ENDIF
\ENDWHILE
\RETURN $[l,u]$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-linear-fractional-bisection .example name="Sublevel sets of a ratio"}

For $f_0(x)=p(x)/q(x)$ with $p$ convex, $q$ concave and $p\ge0$, $q>0$ on the domain, take $\phi_t(x)=p(x)-tq(x)$. For $t\ge0$ it is convex in $x$, and $f_0(x)\le t\iff\phi_t(x)\le0$.

:::

::: {#rmk-equivalent-problems-1 .remark name="Equivalent is not identical"}

Equivalent problems can differ greatly for algorithms: eliminating equality constraints may destroy sparsity, and introducing variables can make a problem larger but more structured. Duals of equivalent problems can also look quite different (@sec-math-optimization-duality-duality-and-reformulations).

:::

::: {#rmk-equivalent-problems-2 .remark editor="No figure: bisection only halves an interval of candidate values, and the iteration count of the theorem already says everything a picture would."}

The feasibility problems solved by bisection are convex even though $f_0$ is not, so each can be handled by any convex solver; only about $\log_2((u_0-l_0)/\epsilon)$ of them are needed.

:::
