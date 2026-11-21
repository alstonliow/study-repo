---
title: "Locally Weighted Linear Regression"
sources: [cs229-1]
requires: [ai/machine-learning/linear-regression, math/linear-algebra/matrix-methods/matrix-derivatives]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 1 (locally weighted linear regression), in our own wording; the closed form and the example are our own. -->

A single straight line fits a curved data set badly everywhere. Locally weighted regression fits a fresh line for every query point, giving the training examples near the query the most say.

::: {#def-locally-weighted-regression .definition name="Locally weighted linear regression"}

Given training examples $(\mathbf{x}^{(i)},y^{(i)})$, $i=1,\dots,N$, a query point $\mathbf{x}$ and a *bandwidth* $\tau>0$, give example $i$ the weight

$$
w^{(i)}=\exp\Bigl(-\frac{\lVert\mathbf{x}^{(i)}-\mathbf{x}\rVert^2}{2\tau^2}\Bigr),
$$

choose $\boldsymbol\theta$ to minimize the weighted squared error

$$
\sum_{i=1}^Nw^{(i)}\bigl(y^{(i)}-\boldsymbol\theta^{\mathsf T}\mathbf{x}^{(i)}\bigr)^2,
$$

and predict $\boldsymbol\theta^{\mathsf T}\mathbf{x}$. (A constant feature $1$ in each $\mathbf{x}^{(i)}$ supplies the intercept.) The weights depend on $\mathbf{x}$, so the fit is repeated for every query.

:::

::: {#fig-locally-weighted-regression-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.2,0) node[lab, right] {$x^{(i)}$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {$w^{(i)}$};
\draw[hl, domain=0:6, samples=100, smooth, variable=\x] plot ({\x}, {2*exp(-(\x-3)^2/(2*0.5^2))});
\draw[emph, domain=0:6, samples=100, smooth, variable=\x] plot ({\x}, {2*exp(-(\x-3)^2/(2*1.5^2))});
\draw (3,0) -- (3,-0.08) node[tick, below] {$x$};
\node[tick, text=accent] at (3.9,1.9) {$\tau=0.5$};
\node[tick] at (5.3,0.9) {$\tau=1.5$};
\draw (0,2) -- (-0.08,2) node[tick, left] {$1$};
\end{tikzpicture}
\end{center}
```

The weights $w^{(i)}=\exp\bigl(-(x^{(i)}-x)^2/(2\tau^2)\bigr)$ as a function of the training input. A small bandwidth $\tau$ fits only the nearby points; a large one approaches ordinary least squares

:::

::: {#prp-locally-weighted-closed-form .proposition name="Weighted normal equations"}

Let $X$ have rows $\mathbf{x}^{(i)\mathsf T}$, let $\mathbf{y}$ collect the targets and let $W=\operatorname{diag}(w^{(1)},\dots,w^{(N)})$. If $X^{\mathsf T}WX$ is invertible, the weighted squared error of @def-locally-weighted-regression has the unique minimizer

$$
\boldsymbol\theta=(X^{\mathsf T}WX)^{-1}X^{\mathsf T}W\mathbf{y}.
$$

:::

::: {.proof}

1. The objective is $J(\boldsymbol\theta)=(X\boldsymbol\theta-\mathbf{y})^{\mathsf T}W(X\boldsymbol\theta-\mathbf{y})=\boldsymbol\theta^{\mathsf T}X^{\mathsf T}WX\boldsymbol\theta-2\,(X^{\mathsf T}W\mathbf{y})^{\mathsf T}\boldsymbol\theta+\mathbf{y}^{\mathsf T}W\mathbf{y}$.

2. By @prp-matrix-gradient-rules, $\nabla J=2X^{\mathsf T}WX\boldsymbol\theta-2X^{\mathsf T}W\mathbf{y}$, which vanishes exactly at the stated $\boldsymbol\theta$.

3. All weights are positive, so $\mathbf{v}^{\mathsf T}X^{\mathsf T}WX\mathbf{v}=\sum_iw^{(i)}(\mathbf{x}^{(i)\mathsf T}\mathbf{v})^2\ge0$; $J$ is a convex quadratic, and with $X^{\mathsf T}WX$ invertible it is strictly convex. Its only stationary point is therefore its unique minimizer.

:::

::: {#exm-locally-weighted-regression-1 .example name="Points on a parabola"}

Take the four points $(0,0),(1,1),(2,4),(3,9)$ on $y=x^2$ and the query $x=1.5$, where the true value is $2.25$.

| bandwidth $\tau$ | weights of $x=0,1,2,3$ | fitted line | prediction at $1.5$ |
|---|---|---|---|
| $0.5$ | $0.011,\ 0.607,\ 0.607,\ 0.011$ | $-1.964+3x$ | $2.536$ |
| $1$ | $0.325,\ 0.883,\ 0.883,\ 0.325$ | $-1.462+3x$ | $3.038$ |
| $100$ | all about $1$ | $-1+3x$ | $3.5$ |

As $\tau\to\infty$ every weight tends to $1$ and the method becomes ordinary least squares. A small bandwidth listens mainly to the two nearest points, whose chord passes closer to the curve. (The slope is $3$ in every row because the weights are symmetric about $1.5$.)

:::

::: {#fig-locally-weighted-regression-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.6cm,y=1cm]
\draw[->] (-0.3,0) -- (3.5,0) node[lab,anchor=west] {$x$};
\draw[->] (0,-0.3) -- (0,3.43) node[lab,anchor=south] {$y$};
\draw[faint] (0.000,0.000) -- (0.100,0.004) -- (0.200,0.014) -- (0.300,0.032) -- (0.400,0.056) -- (0.500,0.087) -- (0.600,0.126) -- (0.700,0.171) -- (0.800,0.224) -- (0.900,0.283) -- (1.000,0.350) -- (1.100,0.424) -- (1.200,0.504) -- (1.300,0.592) -- (1.400,0.686) -- (1.500,0.787) -- (1.600,0.896) -- (1.700,1.011) -- (1.800,1.134) -- (1.900,1.263) -- (2.000,1.400) -- (2.100,1.543) -- (2.200,1.694) -- (2.300,1.851) -- (2.400,2.016) -- (2.500,2.188) -- (2.600,2.366) -- (2.700,2.552) -- (2.800,2.744) -- (2.900,2.943) -- (3.000,3.150) -- (3.100,3.364);
\draw (0.2,-0.140) -- (3.2,3.010) node[lab,anchor=west] {least squares};
\draw[hl] (0.8,0.153) -- (2.2,1.623) node[lab,emph,anchor=north west] {$\tau=0.5$};
\node[dot] at (0.0,0.000) {};
\node[dot] at (1.0,0.350) {};
\node[dot] at (2.0,1.400) {};
\node[dot] at (3.0,3.150) {};
\draw[tick] (1.5,0) -- (1.5,-0.1) node[lab,anchor=north] {$1.5$};
\node[hl dot] at (1.5,0.888) {};
\end{tikzpicture}
\end{center}
```

The four points of @exm-locally-weighted-regression-1 on $y=x^2$ (faint), the least squares line $-1+3x$ and the locally weighted line for the query $1.5$ with $\tau=0.5$, which predicts $2.536$.

:::

::: {#rmk-locally-weighted-regression-1 .remark name="Parametric and non-parametric"}

Ordinary linear regression is *parametric*: after training, the fixed vector $\boldsymbol\theta$ is all that is kept. Locally weighted regression is *non-parametric*: every prediction needs the whole training set, so the amount of stored information grows with $N$. The bandwidth plays the role of a hyperparameter: too small and the fit follows the noise, too large and it misses the curvature (@def-overfitting).

:::
