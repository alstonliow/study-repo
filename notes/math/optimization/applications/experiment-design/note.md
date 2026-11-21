---
title: "Experiment Design"
sources: [ee364a-7]
requires: [math/optimization/applications/statistical-estimation, math/optimization/convex-problems/semidefinite-programs]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on statistical estimation, in our own wording; proofs written out in steps. -->

In linear estimation the error covariance depends on which measurements are made. Experiment design chooses how many measurements of each type to take so that this covariance is small in a chosen sense; the relaxed problems are convex.

::: {#def-experiment-design .definition name="Experiment design"}

With $m$ measurements $y_i=a_i^{\mathsf T}x+w_i$, $w_i$ independent $\mathcal N(0,1)$, the least-squares estimate has error covariance
$$E=\Big(\sum_{i=1}^ma_ia_i^{\mathsf T}\Big)^{-1}.$$
If each $a_i$ is chosen from $p$ test vectors $v_1,\dots,v_p$, and $\lambda_j$ is the fraction of measurements using $v_j$, the *relaxed experiment design problem* is
$$\text{minimize (w.r.t. }\mathbb S^n_+)\ \ E=\frac1m\Big(\sum_{j=1}^p\lambda_jv_jv_j^{\mathsf T}\Big)^{-1}\quad\text{s.t. }\lambda\succeq0,\ \mathbf 1^{\mathsf T}\lambda=1,$$
dropping the requirement that $m\lambda_j$ be integers.

:::

::: {#def-d-optimal-design .definition name="D-, E- and A-optimal design"}

Scalarizations of @def-experiment-design:

- *D-optimal*: minimize $\log\det\big(\sum_j\lambda_jv_jv_j^{\mathsf T}\big)^{-1}$ (volume of confidence ellipsoids);
- *E-optimal*: minimize $\lambda_{\max}$ of $E$, an SDP: maximize $t$ subject to $\sum_j\lambda_jv_jv_j^{\mathsf T}\succeq tI$;
- *A-optimal*: minimize $\operatorname{tr}E$ (mean squared error).

Each has constraints $\lambda\succeq0$, $\mathbf 1^{\mathsf T}\lambda=1$ and a convex objective, since $\log\det X^{-1}=-\log\det X$ is convex (@exm-log-det-concave).

:::

::: {#thm-d-optimal-dual .theorem name="Dual of D-optimal design"}

The dual of D-optimal design is, up to constants, the minimum-volume ellipsoid problem
$$\text{maximize }\log\det W+n\log n\quad\text{s.t. }v_j^{\mathsf T}Wv_j\le1,\ j=1,\dots,p,$$
and complementary slackness gives $\lambda_j^\star=0$ unless $v_j^{\mathsf T}W^\star v_j=1$: only test vectors on the boundary of the optimal ellipsoid $\{x\mid x^{\mathsf T}W^\star x\le1\}$ are used.

:::

::: {.proof}

1. Write D-optimal design as minimize $-\log\det X$ subject to $X=\sum_j\lambda_jv_jv_j^{\mathsf T}$, $\lambda\succeq0$, $\mathbf 1^{\mathsf T}\lambda=1$, with multipliers $Z\in\mathbb S^n$ for the equality, $z$ for $\mathbf 1^{\mathsf T}\lambda=1$ and $\mu\succeq0$ for $\lambda\succeq0$.

2. Minimizing $-\log\det X+\operatorname{tr}(ZX)$ over $X\succ0$ gives $X=Z^{-1}$ (requires $Z\succ0$) and value $\log\det Z+n$.

3. Minimizing $\sum_j\lambda_j(z-v_j^{\mathsf T}Zv_j-\mu_j)$ over $\lambda$ is $-\infty$ unless $v_j^{\mathsf T}Zv_j=z-\mu_j\le z$.

4. So the dual is maximize $\log\det Z+n-z$ subject to $v_j^{\mathsf T}Zv_j\le z$. Put $W=Z/z$: the objective is $\log\det W+n\log z+n-z$, maximized over $z$ at $z=n$, giving $\log\det W+n\log n$.

5. Complementary slackness $\lambda_j\mu_j=0$ with $\mu_j=z-v_j^{\mathsf T}Zv_j$ is the last claim.

:::

::: {#exm-design-two-vectors .example name="Two test vectors"}

In $\mathbb{R}^2$ with $v_1=e_1$, $v_2=e_2$, the D-optimal design maximizes $\log(\lambda_1\lambda_2)$ over the simplex, so $\lambda=(\frac12,\frac12)$: split the measurements equally. The dual maximizes $\log\det W$ subject to $W_{11}\le1$, $W_{22}\le1$, giving $W^\star=I$ (by Hadamard's inequality $\det W\le W_{11}W_{22}$); both constraints are tight, consistent with complementary slackness.

:::

::: {#rmk-experiment-design-1 .remark name="Rounding"}

The relaxed solution $\lambda^\star$ gives a lower bound on the integer problem; rounding $m\lambda_j^\star$ to integers gives a design whose objective is close to the bound when $m$ is large.

:::
