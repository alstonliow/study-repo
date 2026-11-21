---
title: "Perturbation and Sensitivity Analysis"
sources: [ee364a-5]
requires: [math/optimization/duality/kkt-conditions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on duality, in our own wording; proofs written out in steps. -->

Optimal dual variables measure how sensitive the optimal value is to changes in the constraints. A large multiplier means tightening that constraint is costly; a zero multiplier means a small change does not matter to first order.

::: {#def-perturbed-problem .definition name="Perturbed problem"}

For $u\in\mathbb{R}^m$, $v\in\mathbb{R}^p$, the *perturbed problem* is
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\le u_i,\quad i=1,\dots,m,\\ &h_i(x)=v_i,\quad i=1,\dots,p,\end{array}$$
with optimal value $p^\star(u,v)$; $p^\star(0,0)=p^\star$. For a convex problem $p^\star(u,v)$ is a convex function of $(u,v)$ (by @prp-partial-minimization applied to the epigraph form).

:::

::: {#thm-global-sensitivity .theorem name="Global sensitivity"}

If strong duality holds for the unperturbed problem and $(\lambda^\star,\nu^\star)$ is dual optimal, then for all $u,v$
$$p^\star(u,v)\ge p^\star(0,0)-\lambda^{\star\mathsf T}u-\nu^{\star\mathsf T}v.$$

:::

::: {.proof}

1. Let $x$ be feasible for the perturbed problem. Then
$$p^\star(0,0)=g(\lambda^\star,\nu^\star)\le f_0(x)+\sum_i\lambda_i^\star f_i(x)+\sum_i\nu_i^\star h_i(x)\le f_0(x)+\lambda^{\star\mathsf T}u+\nu^{\star\mathsf T}v,$$
using $\lambda_i^\star\ge0$, $f_i(x)\le u_i$ and $h_i(x)=v_i$.

2. Take the infimum over feasible $x$.

:::

::: {#cor-local-sensitivity .corollary name="Local sensitivity"}

If in addition $p^\star(u,v)$ is differentiable at $(0,0)$, then
$$\lambda_i^\star=-\frac{\partial p^\star(0,0)}{\partial u_i},\qquad\nu_i^\star=-\frac{\partial p^\star(0,0)}{\partial v_i}.$$

:::

::: {.proof}

1. Take $u=te_i$, $v=0$. By @thm-global-sensitivity, $\frac{p^\star(te_i,0)-p^\star}{t}\ge-\lambda_i^\star$ for $t>0$ and $\le-\lambda_i^\star$ for $t<0$.

2. Letting $t\to0^{\pm}$, the derivative is both $\ge-\lambda_i^\star$ and $\le-\lambda_i^\star$.

3. The same argument with $v=te_i$ gives the formula for $\nu_i^\star$.

:::

::: {#exm-sensitivity-reading .example name="Reading the global bound"}

1. If $\lambda_i^\star$ is large and the constraint is tightened ($u_i<0$), $p^\star$ increases greatly.

2. If $\lambda_i^\star$ is small and the constraint is loosened ($u_i>0$), $p^\star$ does not decrease much.

3. Minimize $x^2$ subject to $1-x\le u$: $p^\star(u)=(1-u)^2$ for $u\le1$, and the dual optimum at $u=0$ is $\lambda^\star=2$; indeed $-\frac{d}{du}(1-u)^2\big|_{u=0}=2$ and $(1-u)^2\ge1-2u$.

:::

::: {#rmk-sensitivity-analysis-1 .remark name="Prices"}

In resource allocation, $u_i$ is extra resource $i$ and $\lambda_i^\star$ is its marginal value, a *shadow price*: the most one should pay per unit of resource $i$ for small changes.

:::
