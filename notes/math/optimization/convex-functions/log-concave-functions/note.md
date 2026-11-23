---
title: "Log-Concave and Log-Convex Functions"
sources: [ee364a-3]
requires: [math/optimization/convex-functions/operations-preserving-convex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex functions, in our own wording; proofs written out in steps; the integration property is stated without proof. -->

Many probability densities are log-concave, and log-concavity survives multiplication, marginalization and convolution. This makes probabilities of convex events behave well in optimization.

::: {#def-log-concave .definition name="Log-concave function"}

A positive function $f$ with convex domain is *log-concave* if $\log f$ is concave, equivalently
$$f(\theta x+(1-\theta)y)\ge f(x)^\theta f(y)^{1-\theta}\qquad\text{for }0\le\theta\le1.$$
It is *log-convex* if $\log f$ is convex.

:::

::: {#fig-log-concave-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.8,0) -- (2.9,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.1) -- (0,1) node[lab, above] {};
\draw[emph] (-2.6,0.03) -- (-2.51,0.03) -- (-2.43,0.04) -- (-2.34,0.05) -- (-2.25,0.06) -- (-2.17,0.08) -- (-2.08,0.09) -- (-1.99,0.11) -- (-1.91,0.13) -- (-1.82,0.15) -- (-1.73,0.18) -- (-1.65,0.21) -- (-1.56,0.24) -- (-1.47,0.27) -- (-1.39,0.31) -- (-1.3,0.34) -- (-1.21,0.38) -- (-1.13,0.42) -- (-1.04,0.46) -- (-0.95,0.51) -- (-0.87,0.55) -- (-0.78,0.59) -- (-0.69,0.63) -- (-0.61,0.66) -- (-0.52,0.7) -- (-0.43,0.73) -- (-0.35,0.75) -- (-0.26,0.77) -- (-0.17,0.79) -- (-0.09,0.79) -- (0,0.8) -- (0.09,0.79) -- (0.17,0.79) -- (0.26,0.77) -- (0.35,0.75) -- (0.43,0.73) -- (0.52,0.7) -- (0.61,0.66) -- (0.69,0.63) -- (0.78,0.59) -- (0.87,0.55) -- (0.95,0.51) -- (1.04,0.46) -- (1.13,0.42) -- (1.21,0.38) -- (1.3,0.34) -- (1.39,0.31) -- (1.47,0.27) -- (1.56,0.24) -- (1.65,0.21) -- (1.73,0.18) -- (1.82,0.15) -- (1.91,0.13) -- (1.99,0.11) -- (2.08,0.09) -- (2.17,0.08) -- (2.25,0.06) -- (2.34,0.05) -- (2.43,0.04) -- (2.51,0.03) -- (2.6,0.03);
\node[lab] at (1.4,0.7) {$\varphi(x)$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-2.8,0) -- (2.9,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.7) -- (0,0.5) node[lab, above] {};
\draw[hl] (-1.8,-1.54) -- (-1.74,-1.43) -- (-1.68,-1.33) -- (-1.62,-1.23) -- (-1.56,-1.14) -- (-1.5,-1.04) -- (-1.44,-0.96) -- (-1.38,-0.87) -- (-1.32,-0.79) -- (-1.26,-0.71) -- (-1.2,-0.64) -- (-1.14,-0.57) -- (-1.08,-0.5) -- (-1.02,-0.44) -- (-0.96,-0.38) -- (-0.9,-0.32) -- (-0.84,-0.27) -- (-0.78,-0.22) -- (-0.72,-0.18) -- (-0.66,-0.14) -- (-0.6,-0.1) -- (-0.54,-0.06) -- (-0.48,-0.03) -- (-0.42,-0.01) -- (-0.36,0.02) -- (-0.3,0.04) -- (-0.24,0.05) -- (-0.18,0.06) -- (-0.12,0.07) -- (-0.06,0.08) -- (0,0.08) -- (0.06,0.08) -- (0.12,0.07) -- (0.18,0.06) -- (0.24,0.05) -- (0.3,0.04) -- (0.36,0.02) -- (0.42,-0.01) -- (0.48,-0.03) -- (0.54,-0.06) -- (0.6,-0.1) -- (0.66,-0.14) -- (0.72,-0.18) -- (0.78,-0.22) -- (0.84,-0.27) -- (0.9,-0.32) -- (0.96,-0.38) -- (1.02,-0.44) -- (1.08,-0.5) -- (1.14,-0.57) -- (1.2,-0.64) -- (1.26,-0.71) -- (1.32,-0.79) -- (1.38,-0.87) -- (1.44,-0.96) -- (1.5,-1.04) -- (1.56,-1.14) -- (1.62,-1.23) -- (1.68,-1.33) -- (1.74,-1.43) -- (1.8,-1.54);
\node[lab] at (1.6,0.4) {$\log\varphi(x)$};
\end{tikzpicture}
\end{center}
```

The standard normal density $\varphi$ (left, vertically scaled) is not concave, but its logarithm $-\tfrac12x^2-\tfrac12\log(2\pi)$ (right, shifted) is a concave parabola, so $\varphi$ is log-concave.

:::

::: {#exm-log-concave .example name="Log-concave functions"}

1. $x^a$ on $x>0$ is log-concave for $a\ge0$ and log-convex for $a\le0$; $e^{ax}$ is both.

2. The normal density $\frac{1}{\sqrt{(2\pi)^n\det\Sigma}}e^{-\frac12(x-\bar x)^{\mathsf T}\Sigma^{-1}(x-\bar x)}$ is log-concave, as is the indicator of a convex set (with $\log0=-\infty$).

3. The Gaussian cumulative distribution $\Phi(x)=\frac1{\sqrt{2\pi}}\int_{-\infty}^xe^{-u^2/2}\,du$ is log-concave (from the integration property below).

:::

::: {#fig-log-concave-functions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-3,0) -- (3,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.1) -- (0,1.4) node[lab, above] {};
\draw[emph] (-2.8,0) -- (-2.71,0) -- (-2.61,0.01) -- (-2.52,0.01) -- (-2.43,0.01) -- (-2.33,0.01) -- (-2.24,0.02) -- (-2.15,0.02) -- (-2.05,0.02) -- (-1.96,0.03) -- (-1.87,0.04) -- (-1.77,0.05) -- (-1.68,0.06) -- (-1.59,0.07) -- (-1.49,0.08) -- (-1.4,0.1) -- (-1.31,0.11) -- (-1.21,0.14) -- (-1.12,0.16) -- (-1.03,0.18) -- (-0.93,0.21) -- (-0.84,0.24) -- (-0.75,0.27) -- (-0.65,0.31) -- (-0.56,0.35) -- (-0.47,0.38) -- (-0.37,0.43) -- (-0.28,0.47) -- (-0.19,0.51) -- (-0.09,0.56) -- (0,0.6) -- (0.09,0.64) -- (0.19,0.69) -- (0.28,0.73) -- (0.37,0.77) -- (0.47,0.82) -- (0.56,0.85) -- (0.65,0.89) -- (0.75,0.93) -- (0.84,0.96) -- (0.93,0.99) -- (1.03,1.02) -- (1.12,1.04) -- (1.21,1.06) -- (1.31,1.09) -- (1.4,1.1) -- (1.49,1.12) -- (1.59,1.13) -- (1.68,1.14) -- (1.77,1.15) -- (1.87,1.16) -- (1.96,1.17) -- (2.05,1.18) -- (2.15,1.18) -- (2.24,1.18) -- (2.33,1.19) -- (2.43,1.19) -- (2.52,1.19) -- (2.61,1.19) -- (2.71,1.2) -- (2.8,1.2);
\node[lab] at (2,1.4) {$\Phi(x)$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-3,0) -- (3,0) node[lab, right] {$x$};
\draw[->, faint] (0,-2.6) -- (0,0.4) node[lab, above] {};
\draw[hl] (-2.8,-2.39) -- (-2.71,-2.27) -- (-2.61,-2.16) -- (-2.52,-2.06) -- (-2.43,-1.95) -- (-2.33,-1.85) -- (-2.24,-1.75) -- (-2.15,-1.66) -- (-2.05,-1.56) -- (-1.96,-1.48) -- (-1.87,-1.39) -- (-1.77,-1.31) -- (-1.68,-1.23) -- (-1.59,-1.15) -- (-1.49,-1.08) -- (-1.4,-1.01) -- (-1.31,-0.94) -- (-1.21,-0.87) -- (-1.12,-0.81) -- (-1.03,-0.75) -- (-0.93,-0.7) -- (-0.84,-0.64) -- (-0.75,-0.59) -- (-0.65,-0.54) -- (-0.56,-0.5) -- (-0.47,-0.46) -- (-0.37,-0.41) -- (-0.28,-0.38) -- (-0.19,-0.34) -- (-0.09,-0.31) -- (0,-0.28) -- (0.09,-0.25) -- (0.19,-0.22) -- (0.28,-0.2) -- (0.37,-0.18) -- (0.47,-0.15) -- (0.56,-0.14) -- (0.65,-0.12) -- (0.75,-0.1) -- (0.84,-0.09) -- (0.93,-0.08) -- (1.03,-0.07) -- (1.12,-0.06) -- (1.21,-0.05) -- (1.31,-0.04) -- (1.4,-0.03) -- (1.49,-0.03) -- (1.59,-0.02) -- (1.68,-0.02) -- (1.77,-0.02) -- (1.87,-0.01) -- (1.96,-0.01) -- (2.05,-0.01) -- (2.15,-0.01) -- (2.24,-0.01) -- (2.33,-0) -- (2.43,-0) -- (2.52,-0) -- (2.61,-0) -- (2.71,-0) -- (2.8,-0);
\node[lab] at (-1,-1.6) {$\log\Phi(x)$};
\end{tikzpicture}
\end{center}
```

The Gaussian distribution function $\Phi$ (left) is neither convex nor concave, yet $\log\Phi$ (right, scaled) is concave: it tends to $0$ on the right and falls like $-\tfrac12x^2$ on the left.

:::

::: {#prp-log-concave-second-order .proposition name="Second-order condition"}

A twice differentiable positive $f$ with convex domain is log-concave if and only if
$$f(x)\nabla^2f(x)\preceq\nabla f(x)\nabla f(x)^{\mathsf T}\qquad\text{for all }x\in\operatorname{dom}f.$$

:::

::: {.proof}

1. $\nabla^2\log f=\frac{1}{f}\nabla^2f-\frac1{f^2}\nabla f\nabla f^{\mathsf T}$.

2. Multiplying by $f^2>0$, $\nabla^2\log f\preceq0$ is the stated inequality; apply the second-order test (@prp-convex-second-derivative) to $-\log f$.

:::

::: {#prp-log-concave-operations .proposition name="Products, marginals and convolutions"}

1. A product of log-concave functions is log-concave.

2. A sum of log-concave functions need not be log-concave.

3. (Integration) If $f(x,y)$ is log-concave in $(x,y)$, then $g(x)=\int f(x,y)\,dy$ is log-concave.

4. Consequently the convolution $(f*g)(x)=\int f(x-y)g(y)\,dy$ of log-concave functions is log-concave.

:::

::: {.proof}

1. $\log(fg)=\log f+\log g$ is a sum of concave functions.

2. $h(x)=e^{-x^2/2}+e^{-(x-4)^2/2}$ is a sum of log-concave functions, but $h(2)=2e^{-2}\approx0.271$ is less than $\sqrt{h(0)h(4)}=1+e^{-8}\approx1.0003$, violating the defining inequality with $\theta=\frac12$.

3. The integration property is the Prékopa–Leindler theorem; we state it without proof.

4. $f(x-y)g(y)$ is log-concave in $(x,y)$ by part 1 (each factor is a log-concave function composed with a linear map), so part 3 applies.

:::

::: {#fig-log-concave-functions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.6,0) -- (2.8,0) node[lab, right] {};
\draw[->, faint] (0,-0.1) -- (0,1.4) node[lab, above] {};
\draw[emph] (-2.4,0) -- (-1,0) -- (-1,1) -- (1,1) -- (1,0) -- (2.4,0);
\node[lab] at (0,1.25) {$\mathbf 1_{[-1,1]}$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-2.6,0) -- (2.8,0) node[lab, right] {};
\draw[->, faint] (0,-0.1) -- (0,1.4) node[lab, above] {};
\draw[hl] (-2.4,0) -- (-2,0) -- (0,1) -- (2,0) -- (2.4,0);
\node[lab] at (0,1.25) {$\tfrac12\,\mathbf 1_{[-1,1]}*\mathbf 1_{[-1,1]}$};
\end{tikzpicture}
\end{center}
```

The indicator of an interval is log-concave, so its convolution with itself is too: the result is the triangle function on $[-2,2]$, whose logarithm is concave where it is finite.

:::

::: {#exm-yield-function .example name="Manufacturing yield"}

A part is made to target dimensions $x$, but the actual dimensions are $x+w$ with random $w$ of log-concave density $p$. If acceptable parts form a convex set $S$, the yield $Y(x)=\operatorname{P}(x+w\in S)=\int I_S(x+w)p(w)\,dw$ is log-concave in $x$ by @prp-log-concave-operations. So the set of targets with yield at least $\alpha$, $\{x\mid Y(x)\ge\alpha\}$, is convex.

:::

::: {#def-k-convex .definition name="Convexity with respect to a generalized inequality"}

For a proper cone $K$, $f:\mathbb{R}^n\to\mathbb{R}^m$ is *$K$-convex* if
$$f(\theta x+(1-\theta)y)\preceq_K\theta f(x)+(1-\theta)f(y)\qquad\text{for }0\le\theta\le1.$$
 With $K=\mathbb S^m_+$ the map $X\mapsto X^2$ is matrix convex: for any $z$, $z^{\mathsf T}X^2z=\lVert Xz\rVert_2^2$ is a convex function of $X$.

:::
