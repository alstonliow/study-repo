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

::: {#fig-sensitivity-analysis-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle (0.71);
\fill[ink] (0.58,0.4) circle[pt];
\draw[emph] (0,0) circle (1);
\fill[accent] (0.82,0.57) circle[pt];
\draw[faint] (0,0) circle (1.34);
\fill[ink] (1.1,0.76) circle[pt];
\fill[ink] (2.6,1.8) circle[pt] node[lab, right] {$\text{argmin}\,f_0$};
\draw[faint, dashed] (0,0) -- (2.6,1.8);
\node[lab, above right] at (-0.5,-0.5) {$-0.5$};
\node[lab, below left] at (-0.71,-0.71) {$0$};
\node[lab, below left] at (-0.95,-0.95) {$u=0.8$};
\end{tikzpicture}
\end{center}
```

Perturbing $f_1(x)=\lVert x\rVert_2^2-1\le u$: loosening ($u>0$) enlarges the feasible disc and the optimum moves toward the unconstrained minimizer of $f_0=\lVert x-q\rVert_2^2$, so $p^\star(u)$ decreases; tightening ($u<0$) does the opposite.

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

::: {#fig-sensitivity-analysis-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.4,0) -- (2,0) node[lab, right] {$u$};
\draw[->, faint] (0,-0.4) -- (0,3.4) node[lab, above] {};
\draw[emph] (-0.8,3.24) -- (-0.77,3.13) -- (-0.74,3.03) -- (-0.71,2.92) -- (-0.68,2.82) -- (-0.65,2.72) -- (-0.62,2.62) -- (-0.59,2.53) -- (-0.56,2.43) -- (-0.53,2.34) -- (-0.5,2.25) -- (-0.47,2.16) -- (-0.44,2.07) -- (-0.41,1.99) -- (-0.38,1.9) -- (-0.35,1.82) -- (-0.32,1.74) -- (-0.29,1.66) -- (-0.26,1.59) -- (-0.23,1.51) -- (-0.2,1.44) -- (-0.17,1.37) -- (-0.14,1.3) -- (-0.11,1.23) -- (-0.08,1.17) -- (-0.05,1.1) -- (-0.02,1.04) -- (0.01,0.98) -- (0.04,0.92) -- (0.07,0.86) -- (0.1,0.81) -- (0.13,0.76) -- (0.16,0.71) -- (0.19,0.66) -- (0.22,0.61) -- (0.25,0.56) -- (0.28,0.52) -- (0.31,0.48) -- (0.34,0.44) -- (0.37,0.4) -- (0.4,0.36) -- (0.43,0.32) -- (0.46,0.29) -- (0.49,0.26) -- (0.52,0.23) -- (0.55,0.2) -- (0.58,0.18) -- (0.61,0.15) -- (0.64,0.13) -- (0.67,0.11) -- (0.7,0.09) -- (0.73,0.07) -- (0.76,0.06) -- (0.79,0.04) -- (0.82,0.03) -- (0.85,0.02) -- (0.88,0.01) -- (0.91,0.01) -- (0.94,0) -- (0.97,0) -- (1,0);
\draw[emph] (1,0) -- (1.8,0);
\draw[hl] (-0.9,2.8) -- (0.25,0.5) -- (1.4,-1.8);
\fill[accent] (0,1) circle[pt];
\node[lab, left] at (-0.75,3.2) {$p^\star(u)$};
\node[lab, right] at (1,-1) {$p^\star(0)-\lambda^\star u$};
\end{tikzpicture}
\end{center}
```

Minimize $x^2$ subject to $1-x\le u$: $p^\star(u)=(1-u)^2$ for $u\le1$ and $0$ after. The line $1-2u$ (thick) through $(0,p^\star(0))$ with slope $-\lambda^\star=-2$ lies below it everywhere, as the global sensitivity bound says.

:::

::: {#rmk-sensitivity-analysis-1 .remark name="Prices"}

In resource allocation, $u_i$ is extra resource $i$ and $\lambda_i^\star$ is its marginal value, a *shadow price*: the most one should pay per unit of resource $i$ for small changes.

:::
