---
title: "Optimality Conditions: Complementary Slackness and KKT"
sources: [ee364a-5]
requires: [math/optimization/duality/lagrange-dual-problem]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on duality, in our own wording; proofs written out in steps. Numbers in the water-filling example checked in Python. -->

When strong duality holds and both optima are attained, primal and dual optimal points satisfy a short list of equations and inequalities, the KKT conditions. For convex problems the list is also sufficient, so solving it solves the problem.

::: {#prp-complementary-slackness .proposition name="Complementary slackness"}

Suppose strong duality holds, $x^\star$ is primal optimal and $(\lambda^\star,\nu^\star)$ is dual optimal. Then $x^\star$ minimizes $L(x,\lambda^\star,\nu^\star)$ over $x$, and
$$\lambda_i^\star f_i(x^\star)=0,\qquad i=1,\dots,m.$$
So $\lambda_i^\star>0$ implies $f_i(x^\star)=0$, and $f_i(x^\star)<0$ implies $\lambda_i^\star=0$.

:::

::: {.proof}

1. Chain the inequalities:
$$f_0(x^\star)=g(\lambda^\star,\nu^\star)=\inf_xL(x,\lambda^\star,\nu^\star)\le L(x^\star,\lambda^\star,\nu^\star)=f_0(x^\star)+\sum_i\lambda_i^\star f_i(x^\star)+\sum_i\nu_i^\star h_i(x^\star)\le f_0(x^\star).$$

2. The last step uses $h_i(x^\star)=0$ and $\lambda_i^\star f_i(x^\star)\le0$. Since the two ends agree, every inequality is an equality.

3. Equality in the first gives that $x^\star$ minimizes the Lagrangian; equality in the second gives $\sum_i\lambda_i^\star f_i(x^\star)=0$, a sum of nonpositive terms, so each term is $0$.

:::

::: {#def-kkt-conditions .definition name="Karush–Kuhn–Tucker conditions"}

For differentiable $f_i,h_i$, the *KKT conditions* at $(x,\lambda,\nu)$ are
$$\begin{aligned}&f_i(x)\le0,\quad h_i(x)=0&&\text{(primal feasibility)}\\&\lambda\succeq0&&\text{(dual feasibility)}\\&\lambda_if_i(x)=0&&\text{(complementary slackness)}\\&\nabla f_0(x)+\sum_i\lambda_i\nabla f_i(x)+\sum_i\nu_i\nabla h_i(x)=0&&\text{(stationarity of the Lagrangian).}\end{aligned}$$

:::

::: {#thm-kkt .theorem name="KKT conditions"}

1. (Necessity) If strong duality holds and $x^\star$, $(\lambda^\star,\nu^\star)$ are primal and dual optimal, they satisfy the KKT conditions.

2. (Sufficiency) For a convex problem, any $(\tilde x,\tilde\lambda,\tilde\nu)$ satisfying the KKT conditions is primal and dual optimal with zero duality gap.

3. Hence, for a convex problem satisfying Slater's condition, $x$ is optimal if and only if there are $(\lambda,\nu)$ with $(x,\lambda,\nu)$ satisfying the KKT conditions.

:::

::: {.proof}

1. Necessity: feasibility holds by assumption; complementary slackness and minimization of the Lagrangian come from @prp-complementary-slackness, and a minimizer of a differentiable function has zero gradient.

2. Sufficiency: as $\tilde\lambda\succeq0$, $L(x,\tilde\lambda,\tilde\nu)$ is convex in $x$, and its gradient vanishes at $\tilde x$, so $\tilde x$ minimizes it (@cor-convex-stationary-global). Hence
$$g(\tilde\lambda,\tilde\nu)=L(\tilde x,\tilde\lambda,\tilde\nu)=f_0(\tilde x)+\sum_i\tilde\lambda_if_i(\tilde x)+\sum_i\tilde\nu_ih_i(\tilde x)=f_0(\tilde x),$$
using complementary slackness and $h_i(\tilde x)=0$.

3. So a feasible point and a dual feasible point have equal values; by weak duality (@thm-weak-strong-duality) both are optimal.

4. Part 3 combines parts 1 and 2 with Slater's theorem (@thm-slater), which gives strong duality and attainment of the dual.

:::

::: {#exm-water-filling .example name="Water-filling"}

Minimize $-\sum_{i=1}^n\log(x_i+\alpha_i)$ subject to $x\succeq0$, $\mathbf 1^{\mathsf T}x=1$, with $\alpha_i>0$ (allocate power $x_i$ to channels with noise levels $\alpha_i$). KKT: $x\succeq0$, $\mathbf 1^{\mathsf T}x=1$, $\lambda\succeq0$, $\lambda_ix_i=0$ and $-1/(x_i+\alpha_i)-\lambda_i+\nu=0$. Eliminating $\lambda$:

- if $\nu<1/\alpha_i$ then $\lambda_i=0$ and $x_i=1/\nu-\alpha_i$;
- if $\nu\ge1/\alpha_i$ then $x_i=0$.

So $x_i=\max\{0,1/\nu-\alpha_i\}$, with $\nu$ fixed by $\sum_i\max\{0,1/\nu-\alpha_i\}=1$: pour water of total volume $1$ over patches at heights $\alpha_i$; the water level is $1/\nu$. For $\alpha=(0.5,1,2)$ the level is $1.25$ and $x=(0.75,0.25,0)$.

:::

::: {#fig-kkt-conditions-1}

```{=latex}
\begin{tikzpicture}[x=1.1cm,y=1.1cm]
\fill[shade] (0,0.5) rectangle (1,1.25);
\fill[shade] (1,1) rectangle (2,1.25);
\fill[bar] (0,0) rectangle (1,0.5);
\fill[bar] (1,0) rectangle (2,1);
\fill[bar] (2,0) rectangle (3,2);
\draw[faint] (0,0) rectangle (1,1.25) (1,0) rectangle (2,1.25) (2,0) rectangle (3,2);
\draw[hl] (-0.2,1.25) -- (3.2,1.25) node[right,lab] {level $1/\nu=1.25$};
\node[lab] at (0.5,-0.25) {$\alpha_1=0.5$};
\node[lab] at (1.5,-0.25) {$\alpha_2=1$};
\node[lab] at (2.5,-0.25) {$\alpha_3=2$};
\node[lab] at (0.5,0.875) {$x_1$};
\node[lab] at (1.5,1.125) {$x_2$};
\end{tikzpicture}
```

Water-filling for $\alpha=(0.5,1,2)$: channels 1 and 2 are filled up to the level $1.25$ (heights $x_1=0.75$, $x_2=0.25$); channel 3 sits above the level and gets nothing.

:::

::: {#rmk-kkt-conditions-1 .remark name="Relation to Lagrange multipliers"}

With equality constraints only, the KKT conditions are the Lagrange multiplier rule of calculus (@thm-lagrange-multipliers). Inequalities add the sign condition $\lambda\succeq0$ and complementary slackness: an inactive constraint has zero multiplier.

:::
