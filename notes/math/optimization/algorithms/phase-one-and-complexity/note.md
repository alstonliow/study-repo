---
title: "Phase I, Complexity and Generalized Inequalities"
sources: [ee364a-12]
requires: [math/optimization/algorithms/barrier-method, math/optimization/convex-problems/semidefinite-programs]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on interior-point methods, in our own wording; proofs written out in steps; the per-centering Newton bound is quoted from the self-concordance theorem. -->

The barrier method needs a strictly feasible starting point, found by a phase I problem. Self-concordance gives a bound on the total number of Newton steps that grows like $\sqrt m$, and the method extends to generalized inequalities such as semidefinite constraints.

::: {#def-phase-one .definition name="Basic phase I method"}

To find $x$ with $f_i(x)<0$, $Ax=b$, solve
$$\text{minimize }s\quad\text{subject to }f_i(x)\le s,\ i=1,\dots,m,\quad Ax=b,$$
over $(x,s)$, by the barrier method started from any $x$ with $Ax=b$ and $s>\max_if_i(x)$. If the optimal value $\bar p^\star<0$, a point with $s<0$ is strictly feasible for the original problem; if $\bar p^\star>0$ the inequalities are infeasible; one can stop as soon as a point with $s<0$, or a dual certificate of $\bar p^\star>0$, is found.

:::

::: {#def-sum-of-infeasibilities .definition name="Sum of infeasibilities"}

The variant minimize $\mathbf 1^{\mathsf T}s$ subject to $s\succeq0$, $f_i(x)\le s_i$, $Ax=b$ has optimal value $0$ iff the inequalities are feasible, and when they are infeasible its solution tends to satisfy many of the inequalities exactly ($s_i=0$), showing which ones to drop.

:::

::: {#thm-barrier-complexity .theorem name="Complexity of the barrier method"}

Suppose $tf_0+\phi$ is self-concordant for every $t\ge t^{(0)}$ and the sublevel sets are bounded. Then the total number of Newton steps, excluding the first centering, is at most
$$\Big\lceil\frac{\log(m/(t^{(0)}\epsilon))}{\log\mu}\Big\rceil\Big(\frac{m(\mu-1-\log\mu)}{\gamma}+c\Big),$$
with $\gamma$ and $c$ the constants of @thm-self-concordant-newton. With $\mu=1+1/\sqrt m$ this is $O\big(\sqrt m\log\frac{m}{t^{(0)}\epsilon}\big)$.

:::

::: {.proof}

1. Each centering starts at $x=x^\star(t)$ and computes $x^+=x^\star(\mu t)$. By @thm-self-concordant-newton it takes at most $\frac{\mu tf_0(x)+\phi(x)-\mu tf_0(x^+)-\phi(x^+)}{\gamma}+c$ Newton steps, with $c=\log_2\log_2(1/\epsilon_{\rm nt})$.

2. With $\lambda_i=-1/(tf_i(x))$ the dual point at $x$ (@thm-central-path-duality-gap), $\frac{-f_i(x^+)}{-f_i(x)}=t\lambda_i(-f_i(x^+))$, so
$$\phi(x)-\phi(x^+)=\sum_i\log\big(\mu t\lambda_i(-f_i(x^+))\big)-m\log\mu\le-\mu t\sum_i\lambda_if_i(x^+)-m-m\log\mu,$$
using $\log y\le y-1$.

3. Since $x$ minimizes $L(\cdot,\lambda,\nu)$ over $Ax=b$ with value $f_0(x)-m/t$, and $Ax^+=b$, we have $f_0(x^+)+\sum_i\lambda_if_i(x^+)\ge f_0(x)-m/t$. Hence the numerator is at most
$$\mu tf_0(x)-\mu t\Big(f_0(x^+)+\sum_i\lambda_if_i(x^+)\Big)-m-m\log\mu\le\mu m-m-m\log\mu=m(\mu-1-\log\mu).$$

4. Multiply by the number of centering steps from @prp-barrier-outer-iterations. For $\mu=1+1/\sqrt m$, $m(\mu-1-\log\mu)\le m\cdot\frac{(\mu-1)^2}{2}=\frac12$ and $\log\mu\ge\frac{1}{2\sqrt m}$ (for $m\ge1$), giving the $O(\sqrt m\log\cdot)$ bound.

:::

::: {#def-generalized-log .definition name="Generalized logarithm, barrier for generalized inequalities"}

For a proper cone $K\subseteq\mathbb{R}^q$, a *generalized logarithm* of degree $\theta$ is a concave, closed $\psi:\mathbb{R}^q\to\mathbb{R}$ with $\operatorname{dom}\psi=\operatorname{int}K$, $\nabla^2\psi(y)\prec0$ and $\psi(sy)=\psi(y)+\theta\log s$ for $s>0$. Examples: $\psi(y)=\sum_i\log y_i$ on $\mathbb{R}^n_+$ ($\theta=n$); $\psi(Y)=\log\det Y$ on $\mathbb S^p_+$ ($\theta=p$). For constraints $f_i(x)\preceq_{K_i}0$ the barrier is $\phi(x)=-\sum_i\psi_i(-f_i(x))$, and the central path has duality gap $\sum_i\theta_i/t$.

:::

::: {#exm-sdp-barrier .example name="Barrier for an SDP"}

For the SDP minimize $c^{\mathsf T}x$ subject to $F(x)=\sum_ix_iF_i+G\preceq0$, the barrier is $\phi(x)=-\log\det(-F(x))$ and the central point $x^\star(t)$ satisfies $tc_i=\operatorname{tr}(F_i\,(-F(x^\star))^{-1})$. Then $Z^\star(t)=\frac1t(-F(x^\star(t)))^{-1}$ is dual feasible (@exm-sdp-dual) with gap $p/t$, where $p$ is the size of the matrices.

:::

::: {#rmk-phase-one-and-complexity-1 .remark name="Primal-dual methods"}

Primal-dual interior-point methods update primal and dual variables together, taking one Newton step on the perturbed KKT conditions of the central path (@sec-math-optimization-algorithms-barrier-method) per iteration instead of fully centering. They are often faster than the barrier method, especially when high accuracy is needed, and handle infeasible starting points.

:::
