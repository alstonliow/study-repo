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

::: {#fig-kkt-conditions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (-0.54,1.4) -- (-0.62,1.37) -- (-0.69,1.33) -- (-0.77,1.29) -- (-0.84,1.25) -- (-0.9,1.2) -- (-0.97,1.14) -- (-1.03,1.09) -- (-1.09,1.03) -- (-1.15,0.97) -- (-1.2,0.9) -- (-1.25,0.83) -- (-1.29,0.76) -- (-1.33,0.69) -- (-1.37,0.61) -- (-1.4,0.53) -- (-1.43,0.45) -- (-1.45,0.37) -- (-1.47,0.29) -- (-1.49,0.21) -- (-1.49,0.12) -- (-1.5,0.04) -- (-1.5,-0.04) -- (-1.49,-0.13) -- (-1.48,-0.21) -- (-1.47,-0.29) -- (-1.45,-0.38) -- (-1.43,-0.46) -- (-1.4,-0.54) -- (-1.37,-0.61) -- (-1.33,-0.69) -- (-1.29,-0.76) -- (-1.25,-0.83) -- (-1.2,-0.9) -- (-1.15,-0.97) -- (-1.09,-1.03) -- (-1.03,-1.09) -- (-0.97,-1.15) -- (-0.9,-1.2) -- (-0.83,-1.25) -- (-0.76,-1.29) -- (-0.69,-1.33) -- (-0.61,-1.37) -- (-0.53,-1.4) -- (-0.46,-1.43) -- (-0.37,-1.45) -- (-0.29,-1.47) -- (-0.21,-1.49) -- (-0.13,-1.49) -- (-0.04,-1.5) -- (0.04,-1.5) -- (0.13,-1.49) -- (0.21,-1.49) -- (0.29,-1.47) -- (0.37,-1.45) -- (0.46,-1.43) -- (0.53,-1.4) -- (0.61,-1.37) -- (0.69,-1.33) -- (0.76,-1.29) -- (0.83,-1.25) -- (0.9,-1.2) -- (0.97,-1.15) -- (1.03,-1.09) -- (1.09,-1.03) -- (1.15,-0.97) -- (1.2,-0.9) -- (1.25,-0.83) -- (1.29,-0.76) -- (1.33,-0.69) -- (1.37,-0.61) -- (1.4,-0.54) -- (1.43,-0.46) -- (1.45,-0.38) -- (1.47,-0.29) -- (1.48,-0.21) -- (1.49,-0.13) -- (1.5,-0.04) -- (1.5,0.04) -- (1.49,0.12) -- (1.49,0.21) -- (1.47,0.29) -- (1.45,0.37) -- (1.43,0.45) -- (1.4,0.53) -- (1.37,0.61) -- (1.33,0.69) -- (1.29,0.76) -- (1.25,0.83) -- (1.2,0.9) -- (1.15,0.97) -- (1.09,1.03) -- (1.03,1.09) -- (0.97,1.14) -- (0.9,1.2) -- (0.84,1.25) -- (0.77,1.29) -- (0.69,1.33) -- (0.62,1.37) -- (0.54,1.4) -- cycle;
\draw[emph] (-0.54,1.4) -- (-0.62,1.37) -- (-0.69,1.33) -- (-0.77,1.29) -- (-0.84,1.25) -- (-0.9,1.2) -- (-0.97,1.14) -- (-1.03,1.09) -- (-1.09,1.03) -- (-1.15,0.97) -- (-1.2,0.9) -- (-1.25,0.83) -- (-1.29,0.76) -- (-1.33,0.69) -- (-1.37,0.61) -- (-1.4,0.53) -- (-1.43,0.45) -- (-1.45,0.37) -- (-1.47,0.29) -- (-1.49,0.21) -- (-1.49,0.12) -- (-1.5,0.04) -- (-1.5,-0.04) -- (-1.49,-0.13) -- (-1.48,-0.21) -- (-1.47,-0.29) -- (-1.45,-0.38) -- (-1.43,-0.46) -- (-1.4,-0.54) -- (-1.37,-0.61) -- (-1.33,-0.69) -- (-1.29,-0.76) -- (-1.25,-0.83) -- (-1.2,-0.9) -- (-1.15,-0.97) -- (-1.09,-1.03) -- (-1.03,-1.09) -- (-0.97,-1.15) -- (-0.9,-1.2) -- (-0.83,-1.25) -- (-0.76,-1.29) -- (-0.69,-1.33) -- (-0.61,-1.37) -- (-0.53,-1.4) -- (-0.46,-1.43) -- (-0.37,-1.45) -- (-0.29,-1.47) -- (-0.21,-1.49) -- (-0.13,-1.49) -- (-0.04,-1.5) -- (0.04,-1.5) -- (0.13,-1.49) -- (0.21,-1.49) -- (0.29,-1.47) -- (0.37,-1.45) -- (0.46,-1.43) -- (0.53,-1.4) -- (0.61,-1.37) -- (0.69,-1.33) -- (0.76,-1.29) -- (0.83,-1.25) -- (0.9,-1.2) -- (0.97,-1.15) -- (1.03,-1.09) -- (1.09,-1.03) -- (1.15,-0.97) -- (1.2,-0.9) -- (1.25,-0.83) -- (1.29,-0.76) -- (1.33,-0.69) -- (1.37,-0.61) -- (1.4,-0.54) -- (1.43,-0.46) -- (1.45,-0.38) -- (1.47,-0.29) -- (1.48,-0.21) -- (1.49,-0.13) -- (1.5,-0.04) -- (1.5,0.04) -- (1.49,0.12) -- (1.49,0.21) -- (1.47,0.29) -- (1.45,0.37) -- (1.43,0.45) -- (1.4,0.53) -- (1.37,0.61) -- (1.33,0.69) -- (1.29,0.76) -- (1.25,0.83) -- (1.2,0.9) -- (1.15,0.97) -- (1.09,1.03) -- (1.03,1.09) -- (0.97,1.14) -- (0.9,1.2) -- (0.84,1.25) -- (0.77,1.29) -- (0.69,1.33) -- (0.62,1.37) -- (0.54,1.4) -- cycle;
\draw[faint, dashed] (-2,1.4) -- (2.4,1.4) node[lab, right] {$f_2=0$};
\begin{scope}\clip (-2,-1.8) rectangle (4,3.2); \draw[faint] (3,2.5) circle (2.41); \end{scope}
\begin{scope}\clip (-2,-1.8) rectangle (4,3.2); \draw[faint] (3,2.5) circle (3.01); \end{scope}
\fill[accent] (1.15,0.96) circle[pt] node[lab, below right] {$x^\star$};
\fill[ink] (3,2.5) circle[pt];
\draw[->, hl] (1.15,0.96) -- (1.69,1.41) node[lab, above left] {$-\nabla f_0$};
\node[lab] at (-0.3,-0.4) {$f_1\le0,\ f_2\le0$};
\node[lab] at (-0.9,1.65) {$\lambda_2^\star=0$};
\end{tikzpicture}
\end{center}
```

Complementary slackness: the optimum $x^\star$ lies on the circle $f_1=0$ but not on the line $f_2=0$. The inactive constraint gets $\lambda_2^\star=0$; only $f_1$ pushes back, with $-\nabla f_0(x^\star)=\lambda_1^\star\nabla f_1(x^\star)$.

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

::: {#fig-kkt-conditions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (-1.2,0.9) -- (-1.24,0.85) -- (-1.28,0.79) -- (-1.31,0.73) -- (-1.34,0.67) -- (-1.37,0.61) -- (-1.4,0.55) -- (-1.42,0.49) -- (-1.44,0.42) -- (-1.46,0.36) -- (-1.47,0.29) -- (-1.48,0.23) -- (-1.49,0.16) -- (-1.5,0.09) -- (-1.5,0.03) -- (-1.5,-0.04) -- (-1.5,-0.11) -- (-1.49,-0.18) -- (-1.48,-0.24) -- (-1.47,-0.31) -- (-1.45,-0.37) -- (-1.43,-0.44) -- (-1.41,-0.5) -- (-1.39,-0.56) -- (-1.36,-0.63) -- (-1.33,-0.69) -- (-1.3,-0.74) -- (-1.27,-0.8) -- (-1.23,-0.86) -- (-1.19,-0.91) -- (-1.15,-0.96) -- (-1.1,-1.02) -- (-1.06,-1.06) -- (-1.01,-1.11) -- (-0.96,-1.15) -- (-0.91,-1.2) -- (-0.85,-1.23) -- (-0.8,-1.27) -- (-0.74,-1.31) -- (-0.68,-1.34) -- (-0.62,-1.37) -- (-0.56,-1.39) -- (-0.49,-1.42) -- (-0.43,-1.44) -- (-0.37,-1.45) -- (-0.3,-1.47) -- (-0.23,-1.48) -- (-0.17,-1.49) -- (-0.1,-1.5) -- (-0.03,-1.5) -- (0.03,-1.5) -- (0.1,-1.5) -- (0.17,-1.49) -- (0.23,-1.48) -- (0.3,-1.47) -- (0.37,-1.45) -- (0.43,-1.44) -- (0.49,-1.42) -- (0.56,-1.39) -- (0.62,-1.37) -- (0.68,-1.34) -- (0.74,-1.31) -- (0.8,-1.27) -- (0.85,-1.23) -- (0.91,-1.2) -- (0.96,-1.15) -- (1.01,-1.11) -- (1.06,-1.06) -- (1.1,-1.02) -- (1.15,-0.96) -- (1.19,-0.91) -- (1.23,-0.86) -- (1.27,-0.8) -- (1.3,-0.74) -- (1.33,-0.69) -- (1.36,-0.63) -- (1.39,-0.56) -- (1.41,-0.5) -- (1.43,-0.44) -- (1.45,-0.37) -- (1.47,-0.31) -- (1.48,-0.24) -- (1.49,-0.18) -- (1.5,-0.11) -- (1.5,-0.04) -- (1.5,0.03) -- (1.5,0.09) -- (1.49,0.16) -- (1.48,0.23) -- (1.47,0.29) -- (1.46,0.36) -- (1.44,0.42) -- (1.42,0.49) -- (1.4,0.55) -- (1.37,0.61) -- (1.34,0.67) -- (1.31,0.73) -- (1.28,0.79) -- (1.24,0.85) -- (1.2,0.9) -- cycle;
\draw[emph] (-1.2,0.9) -- (-1.24,0.85) -- (-1.28,0.79) -- (-1.31,0.73) -- (-1.34,0.67) -- (-1.37,0.61) -- (-1.4,0.55) -- (-1.42,0.49) -- (-1.44,0.42) -- (-1.46,0.36) -- (-1.47,0.29) -- (-1.48,0.23) -- (-1.49,0.16) -- (-1.5,0.09) -- (-1.5,0.03) -- (-1.5,-0.04) -- (-1.5,-0.11) -- (-1.49,-0.18) -- (-1.48,-0.24) -- (-1.47,-0.31) -- (-1.45,-0.37) -- (-1.43,-0.44) -- (-1.41,-0.5) -- (-1.39,-0.56) -- (-1.36,-0.63) -- (-1.33,-0.69) -- (-1.3,-0.74) -- (-1.27,-0.8) -- (-1.23,-0.86) -- (-1.19,-0.91) -- (-1.15,-0.96) -- (-1.1,-1.02) -- (-1.06,-1.06) -- (-1.01,-1.11) -- (-0.96,-1.15) -- (-0.91,-1.2) -- (-0.85,-1.23) -- (-0.8,-1.27) -- (-0.74,-1.31) -- (-0.68,-1.34) -- (-0.62,-1.37) -- (-0.56,-1.39) -- (-0.49,-1.42) -- (-0.43,-1.44) -- (-0.37,-1.45) -- (-0.3,-1.47) -- (-0.23,-1.48) -- (-0.17,-1.49) -- (-0.1,-1.5) -- (-0.03,-1.5) -- (0.03,-1.5) -- (0.1,-1.5) -- (0.17,-1.49) -- (0.23,-1.48) -- (0.3,-1.47) -- (0.37,-1.45) -- (0.43,-1.44) -- (0.49,-1.42) -- (0.56,-1.39) -- (0.62,-1.37) -- (0.68,-1.34) -- (0.74,-1.31) -- (0.8,-1.27) -- (0.85,-1.23) -- (0.91,-1.2) -- (0.96,-1.15) -- (1.01,-1.11) -- (1.06,-1.06) -- (1.1,-1.02) -- (1.15,-0.96) -- (1.19,-0.91) -- (1.23,-0.86) -- (1.27,-0.8) -- (1.3,-0.74) -- (1.33,-0.69) -- (1.36,-0.63) -- (1.39,-0.56) -- (1.41,-0.5) -- (1.43,-0.44) -- (1.45,-0.37) -- (1.47,-0.31) -- (1.48,-0.24) -- (1.49,-0.18) -- (1.5,-0.11) -- (1.5,-0.04) -- (1.5,0.03) -- (1.5,0.09) -- (1.49,0.16) -- (1.48,0.23) -- (1.47,0.29) -- (1.46,0.36) -- (1.44,0.42) -- (1.42,0.49) -- (1.4,0.55) -- (1.37,0.61) -- (1.34,0.67) -- (1.31,0.73) -- (1.28,0.79) -- (1.24,0.85) -- (1.2,0.9) -- cycle;
\fill[tintB] (1.2,0.9) -- (2.24,1.68) -- (1.2,2.2) -- cycle;
\draw[->] (1.2,0.9) -- (1.92,1.44) node[lab, right] {$\nabla f_1$};
\draw[->] (1.2,0.9) -- (1.2,1.8) node[lab, above left] {$\nabla f_2$};
\draw[->, hl] (1.2,0.9) -- (1.87,1.77) node[lab, above] {$-\nabla f_0$};
\fill[accent] (1.2,0.9) circle[pt] node[lab, below left] {$x^\star$};
\end{tikzpicture}
\end{center}
```

KKT at a corner where both constraints are active: stationarity $-\nabla f_0=\lambda_1\nabla f_1+\lambda_2\nabla f_2$ with $\lambda\succeq0$ says $-\nabla f_0(x^\star)$ lies in the cone spanned by the active constraint gradients (shaded).

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
