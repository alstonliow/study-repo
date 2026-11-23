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

::: {#fig-experiment-design-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.49,-0.38) -- (-0.44,-0.44) -- (-0.39,-0.5) -- (-0.33,-0.55) -- (-0.27,-0.6) -- (-0.21,-0.64) -- (-0.15,-0.68) -- (-0.09,-0.72) -- (-0.02,-0.75) -- (0.04,-0.77) -- (0.11,-0.79) -- (0.17,-0.8) -- (0.23,-0.8) -- (0.29,-0.8) -- (0.35,-0.8) -- (0.4,-0.78) -- (0.46,-0.77) -- (0.51,-0.74) -- (0.55,-0.71) -- (0.59,-0.67) -- (0.63,-0.63) -- (0.66,-0.59) -- (0.68,-0.54) -- (0.71,-0.48) -- (0.72,-0.43) -- (0.73,-0.36) -- (0.74,-0.3) -- (0.74,-0.23) -- (0.73,-0.17) -- (0.72,-0.1) -- (0.7,-0.03) -- (0.68,0.04) -- (0.65,0.11) -- (0.62,0.18) -- (0.58,0.25) -- (0.54,0.32) -- (0.49,0.38) -- (0.44,0.44) -- (0.39,0.5) -- (0.33,0.55) -- (0.27,0.6) -- (0.21,0.64) -- (0.15,0.68) -- (0.09,0.72) -- (0.02,0.75) -- (-0.04,0.77) -- (-0.11,0.79) -- (-0.17,0.8) -- (-0.23,0.8) -- (-0.29,0.8) -- (-0.35,0.8) -- (-0.4,0.78) -- (-0.46,0.77) -- (-0.51,0.74) -- (-0.55,0.71) -- (-0.59,0.67) -- (-0.63,0.63) -- (-0.66,0.59) -- (-0.68,0.54) -- (-0.71,0.48) -- (-0.72,0.43) -- (-0.73,0.36) -- (-0.74,0.3) -- (-0.74,0.23) -- (-0.73,0.17) -- (-0.72,0.1) -- (-0.7,0.03) -- (-0.68,-0.04) -- (-0.65,-0.11) -- (-0.62,-0.18) -- (-0.58,-0.25) -- (-0.54,-0.32) -- (-0.49,-0.38) -- cycle;
\draw[hl] (-0.44,-0.39) -- (-0.38,-0.45) -- (-0.33,-0.5) -- (-0.27,-0.55) -- (-0.21,-0.59) -- (-0.15,-0.63) -- (-0.08,-0.67) -- (-0.02,-0.7) -- (0.05,-0.72) -- (0.11,-0.74) -- (0.17,-0.75) -- (0.23,-0.76) -- (0.29,-0.76) -- (0.35,-0.76) -- (0.41,-0.75) -- (0.46,-0.73) -- (0.5,-0.71) -- (0.55,-0.68) -- (0.59,-0.65) -- (0.63,-0.61) -- (0.66,-0.57) -- (0.68,-0.53) -- (0.7,-0.48) -- (0.72,-0.42) -- (0.73,-0.37) -- (0.73,-0.31) -- (0.73,-0.25) -- (0.72,-0.18) -- (0.71,-0.12) -- (0.69,-0.05) -- (0.67,0.02) -- (0.64,0.08) -- (0.61,0.15) -- (0.57,0.21) -- (0.53,0.27) -- (0.48,0.34) -- (0.44,0.39) -- (0.38,0.45) -- (0.33,0.5) -- (0.27,0.55) -- (0.21,0.59) -- (0.15,0.63) -- (0.08,0.67) -- (0.02,0.7) -- (-0.05,0.72) -- (-0.11,0.74) -- (-0.17,0.75) -- (-0.23,0.76) -- (-0.29,0.76) -- (-0.35,0.76) -- (-0.41,0.75) -- (-0.46,0.73) -- (-0.5,0.71) -- (-0.55,0.68) -- (-0.59,0.65) -- (-0.63,0.61) -- (-0.66,0.57) -- (-0.68,0.53) -- (-0.7,0.48) -- (-0.72,0.42) -- (-0.73,0.37) -- (-0.73,0.31) -- (-0.73,0.25) -- (-0.72,0.18) -- (-0.71,0.12) -- (-0.69,0.05) -- (-0.67,-0.02) -- (-0.64,-0.08) -- (-0.61,-0.15) -- (-0.57,-0.21) -- (-0.53,-0.27) -- (-0.48,-0.34) -- (-0.44,-0.39) -- cycle;
\draw[->] (0,0) -- (1.3,0.13) node[lab, right] {$v_1$};
\draw[->] (0,0) -- (0.39,1.3) node[lab, right] {$v_2$};
\draw[->] (0,0) -- (1.04,0.91) node[lab, right] {$v_3$};
\draw[->] (0,0) -- (-0.78,0.65) node[lab, left] {$v_4$};
\end{tikzpicture}
\end{center}
```

Confidence ellipsoids $\{x\mid x^{\mathsf T}E^{-1}x\le\text{const}\}$ of the estimation error for four test vectors $v_j$: the uniform design $\lambda_j=\tfrac14$ (thin) and the D-optimal design (thick), which has the smaller area. The D-optimal design here puts weight 0.50, 0.50, 0.00, 0.00 on $v_1,\dots,v_4$; the vectors with zero weight are not used.

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

::: {#fig-experiment-design-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl] (0.54,-0.6) -- (0.62,-0.52) -- (0.69,-0.45) -- (0.75,-0.37) -- (0.81,-0.28) -- (0.87,-0.2) -- (0.91,-0.11) -- (0.95,-0.03) -- (0.99,0.06) -- (1.01,0.15) -- (1.03,0.24) -- (1.04,0.32) -- (1.04,0.4) -- (1.04,0.48) -- (1.02,0.56) -- (1,0.63) -- (0.97,0.69) -- (0.94,0.75) -- (0.89,0.81) -- (0.84,0.86) -- (0.79,0.9) -- (0.72,0.94) -- (0.65,0.96) -- (0.58,0.99) -- (0.5,1) -- (0.42,1) -- (0.34,1) -- (0.25,0.99) -- (0.16,0.98) -- (0.07,0.95) -- (-0.02,0.92) -- (-0.11,0.88) -- (-0.2,0.84) -- (-0.29,0.79) -- (-0.38,0.73) -- (-0.46,0.67) -- (-0.54,0.6) -- (-0.62,0.52) -- (-0.69,0.45) -- (-0.75,0.37) -- (-0.81,0.28) -- (-0.87,0.2) -- (-0.91,0.11) -- (-0.95,0.03) -- (-0.99,-0.06) -- (-1.01,-0.15) -- (-1.03,-0.24) -- (-1.04,-0.32) -- (-1.04,-0.4) -- (-1.04,-0.48) -- (-1.02,-0.56) -- (-1,-0.63) -- (-0.97,-0.69) -- (-0.94,-0.75) -- (-0.89,-0.81) -- (-0.84,-0.86) -- (-0.79,-0.9) -- (-0.72,-0.94) -- (-0.65,-0.96) -- (-0.58,-0.99) -- (-0.5,-1) -- (-0.42,-1) -- (-0.34,-1) -- (-0.25,-0.99) -- (-0.16,-0.98) -- (-0.07,-0.95) -- (0.02,-0.92) -- (0.11,-0.88) -- (0.2,-0.84) -- (0.29,-0.79) -- (0.38,-0.73) -- (0.46,-0.67) -- (0.54,-0.6) -- cycle;
\fill[accent] (1,0.1) circle[pt] node[lab, right] {$v_1$};
\fill[accent] (-1,-0.1) circle[pt];
\fill[accent] (0.3,1) circle[pt] node[lab, right] {$v_2$};
\fill[accent] (-0.3,-1) circle[pt];
\fill[ink] (0.8,0.7) circle[pt] node[lab, right] {$v_3$};
\fill[ink] (-0.8,-0.7) circle[pt];
\fill[ink] (-0.6,0.5) circle[pt] node[lab, left] {$v_4$};
\fill[ink] (0.6,-0.5) circle[pt];
\fill[ink] (0,0) circle[pt];
\end{tikzpicture}
\end{center}
```

The dual of D-optimal design: the minimum-area ellipse centred at the origin containing all $\pm v_j$. It touches exactly the test vectors used by the optimal design (highlighted); complementary slackness forces $\lambda_j=0$ for points strictly inside.

:::

::: {#exm-design-two-vectors .example name="Two test vectors"}

In $\mathbb{R}^2$ with $v_1=e_1$, $v_2=e_2$, the D-optimal design maximizes $\log(\lambda_1\lambda_2)$ over the simplex, so $\lambda=(\frac12,\frac12)$: split the measurements equally. The dual maximizes $\log\det W$ subject to $W_{11}\le1$, $W_{22}\le1$, giving $W^\star=I$ (by Hadamard's inequality $\det W\le W_{11}W_{22}$); both constraints are tight, consistent with complementary slackness.

:::

::: {#fig-experiment-design-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.8]
\draw[->, faint] (-0.2,0) -- (1.4,0) node[lab, right] {$\lambda_1$};
\draw[->, faint] (0,-0.2) -- (0,1.4) node[lab, above] {$\lambda_2$};
\draw[faint] (1,0) -- (0,1);
\draw[faint] (0.05,1.3) -- (0.07,0.89) -- (0.09,0.68) -- (0.11,0.55) -- (0.13,0.46) -- (0.15,0.4) -- (0.17,0.35) -- (0.19,0.31) -- (0.21,0.28) -- (0.23,0.26) -- (0.26,0.24) -- (0.28,0.22) -- (0.3,0.2) -- (0.32,0.19) -- (0.34,0.18) -- (0.36,0.17) -- (0.38,0.16) -- (0.4,0.15) -- (0.42,0.14) -- (0.44,0.14) -- (0.46,0.13) -- (0.48,0.12) -- (0.51,0.12) -- (0.53,0.11) -- (0.55,0.11) -- (0.57,0.11) -- (0.59,0.1) -- (0.61,0.1) -- (0.63,0.1) -- (0.65,0.09) -- (0.67,0.09) -- (0.69,0.09) -- (0.71,0.08) -- (0.74,0.08) -- (0.76,0.08) -- (0.78,0.08) -- (0.8,0.08) -- (0.82,0.07) -- (0.84,0.07) -- (0.86,0.07) -- (0.88,0.07) -- (0.9,0.07) -- (0.92,0.06) -- (0.94,0.06) -- (0.97,0.06) -- (0.99,0.06) -- (1.01,0.06) -- (1.03,0.06) -- (1.05,0.06) -- (1.07,0.06) -- (1.09,0.05) -- (1.11,0.05) -- (1.13,0.05) -- (1.15,0.05) -- (1.17,0.05) -- (1.2,0.05) -- (1.22,0.05) -- (1.24,0.05) -- (1.26,0.05) -- (1.28,0.05) -- (1.3,0.05);
\draw[faint] (0.12,1.3) -- (0.14,1.11) -- (0.15,0.97) -- (0.17,0.86) -- (0.19,0.77) -- (0.21,0.7) -- (0.23,0.64) -- (0.25,0.59) -- (0.27,0.55) -- (0.29,0.51) -- (0.31,0.48) -- (0.33,0.45) -- (0.35,0.43) -- (0.37,0.4) -- (0.39,0.38) -- (0.41,0.36) -- (0.43,0.35) -- (0.45,0.33) -- (0.47,0.32) -- (0.49,0.31) -- (0.51,0.29) -- (0.53,0.28) -- (0.55,0.27) -- (0.57,0.26) -- (0.59,0.25) -- (0.61,0.25) -- (0.63,0.24) -- (0.65,0.23) -- (0.67,0.22) -- (0.69,0.22) -- (0.71,0.21) -- (0.73,0.21) -- (0.75,0.2) -- (0.77,0.2) -- (0.79,0.19) -- (0.81,0.19) -- (0.83,0.18) -- (0.85,0.18) -- (0.87,0.17) -- (0.89,0.17) -- (0.91,0.17) -- (0.92,0.16) -- (0.94,0.16) -- (0.96,0.16) -- (0.98,0.15) -- (1,0.15) -- (1.02,0.15) -- (1.04,0.14) -- (1.06,0.14) -- (1.08,0.14) -- (1.1,0.14) -- (1.12,0.13) -- (1.14,0.13) -- (1.16,0.13) -- (1.18,0.13) -- (1.2,0.12) -- (1.22,0.12) -- (1.24,0.12) -- (1.26,0.12) -- (1.28,0.12) -- (1.3,0.12);
\draw[faint] (0.19,1.3) -- (0.21,1.19) -- (0.23,1.09) -- (0.25,1.01) -- (0.27,0.94) -- (0.28,0.88) -- (0.3,0.82) -- (0.32,0.78) -- (0.34,0.74) -- (0.36,0.7) -- (0.38,0.66) -- (0.4,0.63) -- (0.41,0.6) -- (0.43,0.58) -- (0.45,0.55) -- (0.47,0.53) -- (0.49,0.51) -- (0.51,0.49) -- (0.52,0.48) -- (0.54,0.46) -- (0.56,0.45) -- (0.58,0.43) -- (0.6,0.42) -- (0.62,0.41) -- (0.64,0.39) -- (0.65,0.38) -- (0.67,0.37) -- (0.69,0.36) -- (0.71,0.35) -- (0.73,0.34) -- (0.75,0.34) -- (0.76,0.33) -- (0.78,0.32) -- (0.8,0.31) -- (0.82,0.3) -- (0.84,0.3) -- (0.86,0.29) -- (0.88,0.29) -- (0.89,0.28) -- (0.91,0.27) -- (0.93,0.27) -- (0.95,0.26) -- (0.97,0.26) -- (0.99,0.25) -- (1,0.25) -- (1.02,0.24) -- (1.04,0.24) -- (1.06,0.24) -- (1.08,0.23) -- (1.1,0.23) -- (1.12,0.22) -- (1.13,0.22) -- (1.15,0.22) -- (1.17,0.21) -- (1.19,0.21) -- (1.21,0.21) -- (1.23,0.2) -- (1.24,0.2) -- (1.26,0.2) -- (1.28,0.2) -- (1.3,0.19);
\fill[accent] (0.5,0.5) circle[pt] node[lab, above right] {$(\tfrac12,\tfrac12)$};
\node[lab] at (1,-0.25) {$1$};
\node[lab] at (-0.25,1) {$1$};
\end{tikzpicture}
\end{center}
```

Two test vectors $e_1,e_2$: the design $\lambda$ lies on the segment $\lambda_1+\lambda_2=1$, and the level curves $\lambda_1\lambda_2=\text{const}$ of the D-optimal objective are hyperbolas. The best one touches the segment at $(\tfrac12,\tfrac12)$.

:::

::: {#rmk-experiment-design-1 .remark name="Rounding"}

The relaxed solution $\lambda^\star$ gives a lower bound on the integer problem; rounding $m\lambda_j^\star$ to integers gives a design whose objective is close to the bound when $m$ is large.

:::
