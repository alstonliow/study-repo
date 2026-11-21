---
title: "Convexity and Accelerated Gradient Descent"
sources: [mit18065-21, mit18065-22, mit18065-23]
requires: [ai/machine-learning/gradient-descent, math/optimization/convex-functions/convex-functions]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lectures 21–23 (video lectures and problem sets; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->
<!-- Merged 2026-11-21 (owner approval): the definitions def-convex-set and def-convex-function moved to @sec-math-optimization-convex-sets-affine-and-convex-sets and @sec-math-optimization-convex-functions-convex-functions, combined there with the EE364A versions. -->

Convex sets (@def-convex-set) and convex functions (@def-convex-function) are defined in the optimization notes. Convex problems are the ones gradient descent solves reliably: every local minimum is global, and projections onto convex constraint sets never push points apart. On a quadratic, the speed of gradient descent is set by the condition number of the Hessian, and a momentum term improves it from $\kappa$ to $\sqrt\kappa$.

::: {#prp-convex-second-derivative .proposition name="Second derivative test for convexity"}

Let $f$ be twice continuously differentiable on an open convex set $K$. Then $f$ is convex if and only if its Hessian $H(\mathbf{x})=\big[\partial^2f/\partial x_i\partial x_j\big]$ is positive semidefinite at every $\mathbf{x}\in K$. For example $f(\mathbf{x})=\frac12\mathbf{x}^{\mathsf T}S\mathbf{x}-\mathbf{b}^{\mathsf T}\mathbf{x}$ is convex exactly when $S$ is positive semidefinite.

:::

::: {.proof}

1. $f$ is convex if and only if every restriction $g(t)=f(\mathbf{x}+t\mathbf{d})$ to a line is convex, because the definition only involves points on one segment. By the chain rule $g''(t)=\mathbf{d}^{\mathsf T}H(\mathbf{x}+t\mathbf{d})\mathbf{d}$.

2. One variable, $g''\ge0\Rightarrow g$ convex: for $a<c<b$ with $c=(1-t)a+tb$, the mean value theorem gives slopes $\frac{g(c)-g(a)}{c-a}=g'(\xi_1)\le g'(\xi_2)=\frac{g(b)-g(c)}{b-c}$ with $\xi_1<c<\xi_2$, since $g'$ is increasing. Rearranging gives $g(c)\le(1-t)g(a)+tg(b)$.

3. One variable, $g$ convex $\Rightarrow g''\ge0$: convexity makes difference quotients increase, so $g'$ is increasing and $g''\ge0$.

4. Combining: $f$ is convex iff $\mathbf{d}^{\mathsf T}H\mathbf{d}\ge0$ for all points and directions, which is positive semidefiniteness (@def-positive-definite).

:::

::: {#fig-convex-optimization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.6,0) node[lab, right] {$x$};
\draw[emph, domain=0:5.3, samples=80, smooth, variable=\x] plot ({\x}, {0.18*(\x-2.6)^2+0.4});
\draw[hl] (0.8,0.983) -- (4.6,1.12);
\node[hl dot] at (0.8,0.983) {};
\node[hl dot] at (4.6,1.12) {};
\draw (0.8,0) -- (0.8,-0.08) node[tick, below] {$x$};
\draw (4.6,0) -- (4.6,-0.08) node[tick, below] {$y$};
\end{tikzpicture}
\end{center}
```

A function with $f''\ge0$ is convex: every chord lies on or above the graph

:::

::: {#prp-convex-local-is-global .proposition name="Local minima of convex functions are global"}

If $f$ is convex on $K$ and $\mathbf{x}^*$ is a local minimum, then $f(\mathbf{x}^*)\le f(\mathbf{y})$ for every $\mathbf{y}\in K$.

:::

::: {.proof}

1. Suppose $f(\mathbf{y})<f(\mathbf{x}^*)$. For small $t>0$ the point $\mathbf{z}=(1-t)\mathbf{x}^*+t\mathbf{y}$ is in $K$ and close to $\mathbf{x}^*$.

2. Convexity gives $f(\mathbf{z})\le(1-t)f(\mathbf{x}^*)+tf(\mathbf{y})<f(\mathbf{x}^*)$, contradicting the local minimum.

:::

::: {#fig-convex-optimization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.4,0) node[lab, right] {};
\draw[emph] (0.100,1.784) -- (0.152,1.785) -- (0.204,1.787) -- (0.256,1.787) -- (0.308,1.786) -- (0.359,1.784) -- (0.411,1.781) -- (0.463,1.775) -- (0.515,1.767) -- (0.567,1.757) -- (0.619,1.745) -- (0.671,1.729) -- (0.723,1.712) -- (0.775,1.692) -- (0.827,1.669) -- (0.878,1.643) -- (0.930,1.616) -- (0.982,1.586) -- (1.034,1.554) -- (1.086,1.520) -- (1.138,1.484) -- (1.190,1.448) -- (1.242,1.410) -- (1.294,1.371) -- (1.346,1.333) -- (1.397,1.294) -- (1.449,1.256) -- (1.501,1.218) -- (1.553,1.182) -- (1.605,1.148) -- (1.657,1.115) -- (1.709,1.084) -- (1.761,1.056) -- (1.813,1.031) -- (1.865,1.009) -- (1.916,0.990) -- (1.968,0.974) -- (2.020,0.963) -- (2.072,0.955) -- (2.124,0.951) -- (2.176,0.951) -- (2.228,0.955) -- (2.280,0.962) -- (2.332,0.974) -- (2.384,0.989) -- (2.435,1.007) -- (2.487,1.029) -- (2.539,1.053) -- (2.591,1.081) -- (2.643,1.111) -- (2.695,1.143) -- (2.747,1.176) -- (2.799,1.212) -- (2.851,1.248) -- (2.903,1.285) -- (2.954,1.322) -- (3.006,1.359) -- (3.058,1.396) -- (3.110,1.432) -- (3.162,1.467) -- (3.214,1.501) -- (3.266,1.532) -- (3.318,1.562) -- (3.370,1.590) -- (3.422,1.616) -- (3.473,1.639) -- (3.525,1.660) -- (3.577,1.678) -- (3.629,1.693) -- (3.681,1.706) -- (3.733,1.716) -- (3.785,1.724) -- (3.837,1.730) -- (3.889,1.733) -- (3.941,1.735) -- (3.992,1.735) -- (4.044,1.734) -- (4.096,1.732) -- (4.148,1.729) -- (4.200,1.726);
\node[tick, below] at (2.2,0) {non-convex};
\begin{scope}[xshift=5.4cm]
\draw[->] (0,0) -- (4.4,0) node[lab, right] {};
\draw[emph, domain=0.1:4.2, samples=80, smooth, variable=\x] plot ({\x}, {0.25*(\x-2.2)^2+0.4});
\node[hl dot] at (2.2,0.4) {};
\node[tick, below] at (2.2,0) {convex};
\end{scope}
\node[hl dot] at (2.18,0.95) {};
\end{tikzpicture}
\end{center}
```

Left: a non-convex function with several local minima (dots). Right: for a convex function every local minimum is global, so descent cannot get stuck

:::

::: {#thm-projection-convex-nonexpansive .theorem name="Projection onto a convex set is a contraction"}

Let $K$ be a nonempty closed convex set and $\Pi(\mathbf{x})$ the point of $K$ closest to $\mathbf{x}$. Then $\Pi(\mathbf{x})$ is unique, it is characterised by
$$(\mathbf{z}-\Pi(\mathbf{x}))^{\mathsf T}(\mathbf{x}-\Pi(\mathbf{x}))\le0\quad\text{for all }\mathbf{z}\in K,$$
and $\lVert\Pi(\mathbf{x})-\Pi(\mathbf{y})\rVert\le\lVert\mathbf{x}-\mathbf{y}\rVert$.

:::

::: {.proof}

1. A closest point exists: minimise the continuous distance over the closed bounded set $K\cap\{\mathbf{z}:\lVert\mathbf{z}-\mathbf{x}\rVert\le\lVert\mathbf{k}-\mathbf{x}\rVert\}$ for any fixed $\mathbf{k}\in K$.

2. Let $\mathbf{p}=\Pi(\mathbf{x})$ and $\mathbf{z}\in K$. For $0<t\le1$, $\mathbf{p}+t(\mathbf{z}-\mathbf{p})\in K$, so $\lVert\mathbf{x}-\mathbf{p}-t(\mathbf{z}-\mathbf{p})\rVert^2\ge\lVert\mathbf{x}-\mathbf{p}\rVert^2$. Expanding, $-2t(\mathbf{z}-\mathbf{p})^{\mathsf T}(\mathbf{x}-\mathbf{p})+t^2\lVert\mathbf{z}-\mathbf{p}\rVert^2\ge0$; divide by $t$ and let $t\to0$ to get the inequality.

3. Uniqueness: if $\mathbf{p}$ and $\mathbf{p}'$ are both closest, apply step 2 to each with $\mathbf{z}$ the other one and add: $\lVert\mathbf{p}-\mathbf{p}'\rVert^2\le0$.

4. Contraction: with $\mathbf{p}=\Pi(\mathbf{x})$, $\mathbf{q}=\Pi(\mathbf{y})$, step 2 gives $(\mathbf{q}-\mathbf{p})^{\mathsf T}(\mathbf{x}-\mathbf{p})\le0$ and $(\mathbf{p}-\mathbf{q})^{\mathsf T}(\mathbf{y}-\mathbf{q})\le0$. Adding, $\lVert\mathbf{p}-\mathbf{q}\rVert^2\le(\mathbf{p}-\mathbf{q})^{\mathsf T}(\mathbf{x}-\mathbf{y})\le\lVert\mathbf{p}-\mathbf{q}\rVert\,\lVert\mathbf{x}-\mathbf{y}\rVert$ by Cauchy–Schwarz.

:::

::: {#fig-convex-optimization-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0) ellipse (1.6 and 1.0);
\node[lab] at (-0.6,0.2) {$C$};
\node[dot] (x) at (3.0,1.3) {};
\node[dot] (y) at (3.2,-1.2) {};
\node[hl dot] (px) at (1.32,0.56) {};
\node[hl dot] (py) at (1.25,-0.62) {};
\draw[faint] (x) -- (px) (y) -- (py);
\draw[hl] (px) -- (py);
\draw[dashed] (x) -- (y);
\node[tick, right] at (x) {$x$};
\node[tick, right] at (y) {$y$};
\node[tick, left] at (px) {$P_C x$};
\node[tick, left] at (py) {$P_C y$};
\end{tikzpicture}
\end{center}
```

Projection onto a closed convex set $C$ never increases distances: $\lVert P_Cx-P_Cy\rVert\le\lVert x-y\rVert$

:::

::: {#thm-gradient-descent-quadratic-rate .theorem name="Gradient descent on a quadratic"}

Let $f(\mathbf{x})=\frac12\mathbf{x}^{\mathsf T}S\mathbf{x}-\mathbf{b}^{\mathsf T}\mathbf{x}$ with $S$ positive definite, eigenvalues between $m=\lambda_{\min}$ and $M=\lambda_{\max}$, and minimiser $\mathbf{x}^*=S^{-1}\mathbf{b}$. Gradient descent $\mathbf{x}_{k+1}=\mathbf{x}_k-s\nabla f(\mathbf{x}_k)$ with step $s=2/(m+M)$ satisfies
$$\lVert\mathbf{x}_{k+1}-\mathbf{x}^*\rVert\le\frac{M-m}{M+m}\,\lVert\mathbf{x}_k-\mathbf{x}^*\rVert=\frac{\kappa-1}{\kappa+1}\,\lVert\mathbf{x}_k-\mathbf{x}^*\rVert,\qquad\kappa=\frac Mm .$$

:::

::: {.proof}

1. $\nabla f(\mathbf{x})=S\mathbf{x}-\mathbf{b}=S(\mathbf{x}-\mathbf{x}^*)$, so the error $\mathbf{e}_k=\mathbf{x}_k-\mathbf{x}^*$ obeys $\mathbf{e}_{k+1}=(I-sS)\mathbf{e}_k$.

2. $I-sS$ is symmetric with eigenvalues $1-s\lambda$ for the eigenvalues $\lambda\in[m,M]$ of $S$, so its spectral norm is $\max_\lambda\lvert1-s\lambda\rvert$ (@thm-matrix-norms-singular-values).

3. With $s=2/(m+M)$, $1-sm=\frac{M-m}{M+m}$ and $1-sM=-\frac{M-m}{M+m}$; every other $1-s\lambda$ lies in between.

4. Any other step makes one of the two ends larger in absolute value, so this $s$ is the best fixed step.

:::

::: {#rmk-convex-optimization-1 .remark name="Zigzag"}

For $f=\frac12(x^2+10y^2)$ ($\kappa=10$) the error shrinks by at most $9/11\approx0.82$ per step: the iterates zigzag across the narrow valley, because the gradient points mostly across the valley rather than along it. Exact line search does no better in the worst case.

:::

::: {#def-heavy-ball-momentum .definition name="Gradient descent with momentum (heavy ball)"}

Momentum adds a multiple of the previous step:
$$\mathbf{x}_{k+1}=\mathbf{x}_k-s\nabla f(\mathbf{x}_k)+\beta(\mathbf{x}_k-\mathbf{x}_{k-1}),\qquad0\le\beta<1 .$$
Nesterov's variant evaluates the gradient at the look-ahead point $\mathbf{x}_k+\beta(\mathbf{x}_k-\mathbf{x}_{k-1})$.

:::

::: {#rmk-convex-optimization-2 .remark name="What momentum gains"}

On the quadratic of @thm-gradient-descent-quadratic-rate the heavy ball is a linear recurrence for the pair $(\mathbf{e}_k,\mathbf{e}_{k-1})$. Choosing $s=4/(\sqrt M+\sqrt m)^2$ and $\beta=\big(\frac{\sqrt M-\sqrt m}{\sqrt M+\sqrt m}\big)^2$ makes its eigenvalues have modulus $\frac{\sqrt\kappa-1}{\sqrt\kappa+1}$ (Polyak). For $\kappa=10$ the factor drops from $0.82$ to $0.52$; for $\kappa=10^4$ the number of steps to gain a digit drops from about $11500$ to about $115$.

:::
