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

::: {#fig-equivalent-problems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.5,0) -- (3.4,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,2.9) node[lab, above] {$t$};
\fill[tintA] (-1.2,2.43) -- (-1.13,2.31) -- (-1.06,2.19) -- (-0.99,2.08) -- (-0.92,1.97) -- (-0.84,1.86) -- (-0.77,1.75) -- (-0.7,1.65) -- (-0.63,1.55) -- (-0.56,1.45) -- (-0.49,1.36) -- (-0.42,1.27) -- (-0.35,1.18) -- (-0.27,1.1) -- (-0.2,1.02) -- (-0.13,0.94) -- (-0.06,0.86) -- (0.01,0.79) -- (0.08,0.72) -- (0.15,0.65) -- (0.22,0.59) -- (0.29,0.53) -- (0.37,0.47) -- (0.44,0.42) -- (0.51,0.38) -- (0.58,0.38) -- (0.65,0.4) -- (0.72,0.41) -- (0.79,0.43) -- (0.86,0.45) -- (0.94,0.48) -- (1.01,0.5) -- (1.08,0.53) -- (1.15,0.57) -- (1.22,0.6) -- (1.29,0.64) -- (1.36,0.68) -- (1.43,0.73) -- (1.51,0.78) -- (1.58,0.83) -- (1.65,0.88) -- (1.72,0.94) -- (1.79,1) -- (1.86,1.07) -- (1.93,1.13) -- (2,1.2) -- (2.07,1.28) -- (2.15,1.35) -- (2.22,1.43) -- (2.29,1.51) -- (2.36,1.6) -- (2.43,1.69) -- (2.5,1.78) -- (2.57,1.87) -- (2.64,1.97) -- (2.72,2.07) -- (2.79,2.17) -- (2.86,2.28) -- (2.93,2.39) -- (3,2.5) -- (3,2.6) -- (-1.2,2.6) -- cycle;
\draw[emph] (-1.2,2.43) -- (-1.13,2.31) -- (-1.06,2.2) -- (-0.99,2.08) -- (-0.92,1.97) -- (-0.85,1.87) -- (-0.78,1.76) -- (-0.71,1.66) -- (-0.64,1.56) -- (-0.57,1.47) -- (-0.5,1.38) -- (-0.43,1.29) -- (-0.36,1.2) -- (-0.29,1.12) -- (-0.22,1.03) -- (-0.15,0.96) -- (-0.08,0.88) -- (-0.01,0.81) -- (0.06,0.74) -- (0.13,0.68) -- (0.2,0.61) -- (0.27,0.55) -- (0.34,0.49) -- (0.41,0.44) -- (0.48,0.39) -- (0.55,0.38) -- (0.62,0.39) -- (0.69,0.4) -- (0.76,0.42) -- (0.83,0.44) -- (0.9,0.46) -- (0.97,0.49) -- (1.04,0.52) -- (1.11,0.55) -- (1.18,0.58) -- (1.25,0.62) -- (1.32,0.66) -- (1.39,0.7) -- (1.46,0.75) -- (1.53,0.8) -- (1.6,0.85) -- (1.67,0.9) -- (1.74,0.96) -- (1.81,1.02) -- (1.88,1.08) -- (1.95,1.15) -- (2.02,1.22) -- (2.09,1.29) -- (2.16,1.37) -- (2.23,1.45) -- (2.3,1.53) -- (2.37,1.61) -- (2.44,1.7) -- (2.51,1.79) -- (2.58,1.88) -- (2.65,1.98) -- (2.72,2.08) -- (2.79,2.18) -- (2.86,2.28) -- (2.93,2.39) -- (3,2.5);
\fill[accent] (0.51,0.38) circle[pt] node[lab, below right] {$(x^\star,t^\star)$};
\draw[->] (2.2,2.3) -- (2.2,1.6) node[lab, right] {minimize $t$};
\node[lab] at (-0.4,2.3) {$f_0(x)\le t$};
\end{tikzpicture}
\end{center}
```

Epigraph form: minimizing $f_0(x)$ is the same as minimizing $t$ over the epigraph $f_0(x)\le t$. The new objective is linear, and the solution is the lowest point of the (convex) epigraph.

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

::: {#fig-equivalent-problems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.7,0) -- (3.8,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,2.2) node[lab, above] {$y$};
\draw[emph] (-1.42,2.05) -- (-1.33,1.93) -- (-1.25,1.82) -- (-1.17,1.71) -- (-1.08,1.6) -- (-1,1.5) -- (-0.92,1.4) -- (-0.83,1.31) -- (-0.75,1.22) -- (-0.67,1.13) -- (-0.58,1.05) -- (-0.5,0.97) -- (-0.42,0.9) -- (-0.33,0.83) -- (-0.25,0.77) -- (-0.17,0.71) -- (-0.08,0.65) -- (0,0.6) -- (0.08,0.55) -- (0.17,0.51) -- (0.25,0.47) -- (0.33,0.43) -- (0.42,0.4) -- (0.5,0.38) -- (0.58,0.35) -- (0.67,0.33) -- (0.75,0.32) -- (0.83,0.31) -- (0.92,0.3) -- (1,0.3) -- (1.08,0.3) -- (1.17,0.31) -- (1.25,0.32) -- (1.33,0.33) -- (1.42,0.35) -- (1.5,0.38) -- (1.58,0.4) -- (1.67,0.43) -- (1.75,0.47) -- (1.83,0.51) -- (1.92,0.55) -- (2,0.6) -- (2.08,0.65) -- (2.17,0.71) -- (2.25,0.77) -- (2.33,0.83) -- (2.42,0.9) -- (2.5,0.97) -- (2.58,1.05) -- (2.67,1.13) -- (2.75,1.22) -- (2.83,1.31) -- (2.92,1.4) -- (3,1.5) -- (3.08,1.6) -- (3.17,1.71) -- (3.25,1.82) -- (3.33,1.93) -- (3.42,2.05);
\draw[hl] (-1.5,0.34) -- (-1.42,0.37) -- (-1.33,0.39) -- (-1.25,0.42) -- (-1.17,0.44) -- (-1.08,0.46) -- (-1,0.48) -- (-0.92,0.5) -- (-0.83,0.52) -- (-0.75,0.54) -- (-0.67,0.55) -- (-0.58,0.57) -- (-0.5,0.58) -- (-0.42,0.6) -- (-0.33,0.61) -- (-0.25,0.63) -- (-0.17,0.64) -- (-0.08,0.65) -- (0,0.66) -- (0.08,0.67) -- (0.17,0.68) -- (0.25,0.69) -- (0.33,0.69) -- (0.42,0.7) -- (0.5,0.7) -- (0.58,0.71) -- (0.67,0.71) -- (0.75,0.72) -- (0.83,0.72) -- (0.92,0.72) -- (1,0.72) -- (1.08,0.72) -- (1.17,0.72) -- (1.25,0.72) -- (1.33,0.71) -- (1.42,0.71) -- (1.5,0.7) -- (1.58,0.7) -- (1.67,0.69) -- (1.75,0.69) -- (1.83,0.68) -- (1.92,0.67) -- (2,0.66) -- (2.08,0.65) -- (2.17,0.64) -- (2.25,0.63) -- (2.33,0.61) -- (2.42,0.6) -- (2.5,0.58) -- (2.58,0.57) -- (2.67,0.55) -- (2.75,0.54) -- (2.83,0.52) -- (2.92,0.5) -- (3,0.48) -- (3.08,0.46) -- (3.17,0.44) -- (3.25,0.42) -- (3.33,0.39) -- (3.42,0.37) -- (3.5,0.34);
\draw[faint] (-1.5,0.11) -- (-1.42,0.12) -- (-1.33,0.13) -- (-1.25,0.14) -- (-1.17,0.15) -- (-1.08,0.15) -- (-1,0.16) -- (-0.92,0.17) -- (-0.83,0.17) -- (-0.75,0.18) -- (-0.67,0.18) -- (-0.58,0.19) -- (-0.5,0.2) -- (-0.42,0.2) -- (-0.33,0.2) -- (-0.25,0.21) -- (-0.17,0.21) -- (-0.08,0.22) -- (0,0.22) -- (0.08,0.22) -- (0.17,0.23) -- (0.25,0.23) -- (0.33,0.23) -- (0.42,0.23) -- (0.5,0.24) -- (0.58,0.24) -- (0.67,0.24) -- (0.75,0.24) -- (0.83,0.24) -- (0.92,0.24) -- (1,0.24) -- (1.08,0.24) -- (1.17,0.24) -- (1.25,0.24) -- (1.33,0.24) -- (1.42,0.24) -- (1.5,0.24) -- (1.58,0.23) -- (1.67,0.23) -- (1.75,0.23) -- (1.83,0.23) -- (1.92,0.22) -- (2,0.22) -- (2.08,0.22) -- (2.17,0.21) -- (2.25,0.21) -- (2.33,0.2) -- (2.42,0.2) -- (2.5,0.2) -- (2.58,0.19) -- (2.67,0.18) -- (2.75,0.18) -- (2.83,0.17) -- (2.92,0.17) -- (3,0.16) -- (3.08,0.15) -- (3.17,0.15) -- (3.25,0.14) -- (3.33,0.13) -- (3.42,0.12) -- (3.5,0.11);
\draw[hl] (-0.08,0) -- (2.08,0);
\draw[faint, dashed] (-0.08,0) -- (-0.08,0.65) (2.08,0) -- (2.08,0.65);
\node[lab, right] at (-1.4,1.9) {$p$};
\node[lab, right] at (3.6,0.45) {$0.6\,q$};
\node[lab, left] at (-1.5,0.08) {$0.2\,q$};
\end{tikzpicture}
\end{center}
```

Sublevel sets of $f_0=p/q$ through $\phi_t=p-tq$: for $t=0.6$ the set $\{p\le tq\}$ is the thick interval, so $p^\star\le0.6$; for $t=0.2$ the curve $tq$ never reaches $p$, the feasibility problem is infeasible, and $p^\star>0.2$.

:::

::: {#rmk-equivalent-problems-1 .remark name="Equivalent is not identical"}

Equivalent problems can differ greatly for algorithms: eliminating equality constraints may destroy sparsity, and introducing variables can make a problem larger but more structured. Duals of equivalent problems can also look quite different (@sec-math-optimization-duality-duality-and-reformulations).

:::

::: {#rmk-equivalent-problems-2 .remark editor="No figure: bisection only halves an interval of candidate values, and the iteration count of the theorem already says everything a picture would."}

The feasibility problems solved by bisection are convex even though $f_0$ is not, so each can be handled by any convex solver; only about $\log_2((u_0-l_0)/\epsilon)$ of them are needed.

:::
