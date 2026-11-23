---
title: "Derivative-Free Optimization"
sources: [mit18335-32]
requires: [math/optimization/algorithms/trust-region-methods]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 32 (derivative-free optimization by linear and quadratic approximations), in our own wording; proofs written out in steps; the Nelder–Mead count was measured with scipy. -->

Sometimes the gradient is unavailable: the objective comes from a black-box simulation, an experiment, or noisy code. Derivative-free methods build their models from function values alone. The successful modern ones are trust-region methods whose model is obtained by *interpolation* instead of a Taylor expansion: linear models for COBYLA, quadratic models for NEWUOA and BOBYQA.

::: {#def-interpolation-model .definition name="Interpolation models"}

In $\mathbb{R}^n$, a *linear interpolation model* $m(x)=c+g^{\mathsf T}(x-x_k)$ is determined by the values of $f$ at $n+1$ points $y_0=x_k,y_1,\dots,y_n$ in general position (the vertices of a nondegenerate simplex): $m(y_i)=f(y_i)$. A full quadratic model needs $(n+1)(n+2)/2$ points; NEWUOA uses about $2n+1$ points and fixes the remaining freedom by making the change in the model Hessian as small as possible in the Frobenius norm.

:::

::: {#fig-derivative-free-optimization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.6,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.2) node[lab, above] {$y$};
\draw[emph] (-0.4,1.31) -- (-0.34,1.26) -- (-0.29,1.22) -- (-0.23,1.18) -- (-0.17,1.15) -- (-0.12,1.12) -- (-0.06,1.1) -- (-0,1.08) -- (0.05,1.06) -- (0.11,1.04) -- (0.17,1.03) -- (0.22,1.01) -- (0.28,1) -- (0.34,0.99) -- (0.39,0.97) -- (0.45,0.96) -- (0.51,0.95) -- (0.56,0.93) -- (0.62,0.92) -- (0.68,0.9) -- (0.73,0.89) -- (0.79,0.87) -- (0.85,0.85) -- (0.9,0.83) -- (0.96,0.8) -- (1.02,0.78) -- (1.07,0.76) -- (1.13,0.73) -- (1.19,0.71) -- (1.24,0.68) -- (1.3,0.66) -- (1.36,0.63) -- (1.41,0.61) -- (1.47,0.59) -- (1.53,0.57) -- (1.58,0.55) -- (1.64,0.54) -- (1.7,0.52) -- (1.75,0.52) -- (1.81,0.51) -- (1.87,0.51) -- (1.92,0.51) -- (1.98,0.52) -- (2.04,0.54) -- (2.09,0.56) -- (2.15,0.59) -- (2.21,0.62) -- (2.26,0.66) -- (2.32,0.7) -- (2.38,0.75) -- (2.43,0.81) -- (2.49,0.88) -- (2.55,0.95) -- (2.6,1.02) -- (2.66,1.11) -- (2.72,1.19) -- (2.77,1.29) -- (2.83,1.39) -- (2.89,1.49) -- (2.94,1.6) -- (3,1.71);
\draw[faint] (-0.4,1.19) -- (1.3,0.7) -- (3,0.22);
\draw[hl] (-0.4,1.2) -- (-0.36,1.19) -- (-0.32,1.17) -- (-0.27,1.16) -- (-0.23,1.15) -- (-0.19,1.13) -- (-0.15,1.12) -- (-0.1,1.11) -- (-0.06,1.09) -- (-0.02,1.08) -- (0.02,1.07) -- (0.07,1.06) -- (0.11,1.04) -- (0.15,1.03) -- (0.19,1.02) -- (0.24,1.01) -- (0.28,0.99) -- (0.32,0.98) -- (0.36,0.97) -- (0.41,0.96) -- (0.45,0.94) -- (0.49,0.93) -- (0.53,0.92) -- (0.58,0.91) -- (0.62,0.89) -- (0.66,0.88) -- (0.7,0.87) -- (0.75,0.86) -- (0.79,0.85) -- (0.83,0.84) -- (0.87,0.82) -- (0.92,0.81) -- (0.96,0.8) -- (1,0.79) -- (1.04,0.78) -- (1.09,0.76) -- (1.13,0.75) -- (1.17,0.74) -- (1.21,0.73) -- (1.26,0.72) -- (1.3,0.71) -- (1.34,0.7) -- (1.38,0.69) -- (1.43,0.67) -- (1.47,0.66) -- (1.51,0.65) -- (1.56,0.64) -- (1.6,0.63) -- (1.64,0.62) -- (1.68,0.61) -- (1.73,0.6) -- (1.77,0.59) -- (1.81,0.58) -- (1.85,0.57) -- (1.9,0.55) -- (1.94,0.54) -- (1.98,0.53) -- (2.02,0.52) -- (2.06,0.51) -- (2.11,0.5) -- (2.15,0.49) -- (2.19,0.48) -- (2.23,0.47) -- (2.28,0.46) -- (2.32,0.45) -- (2.36,0.44) -- (2.41,0.43) -- (2.45,0.42) -- (2.49,0.41) -- (2.53,0.4) -- (2.58,0.39) -- (2.62,0.38) -- (2.66,0.37) -- (2.7,0.36) -- (2.75,0.35) -- (2.79,0.34) -- (2.83,0.33) -- (2.87,0.33) -- (2.92,0.32) -- (2.96,0.31) -- (3,0.3);
\fill[ink] (0.2,1.02) circle[pt];
\fill[ink] (1,0.79) circle[pt];
\fill[ink] (2,0.53) circle[pt];
\node[lab, right] at (3,1.71) {$f$};
\node[lab, right] at (3,0.22) {linear};
\node[lab, left] at (-0.4,1.2) {quadratic};
\end{tikzpicture}
\end{center}
```

Interpolation models from function values only: a linear model through two samples and a quadratic model through three (thick). Model-based derivative-free methods minimize such a model inside a trust region instead of using gradients.

:::

::: {#prp-linear-interpolation-gradient .proposition name="Accuracy of the simplex gradient"}

Let $y_i=x_k+\Delta d_i$ with $\lVert d_i\rVert\le1$ and $D=[d_1\cdots d_n]$ invertible, and let $f$ have an $L$-Lipschitz gradient. Then the linear interpolation model satisfies
$$\lVert g-\nabla f(x_k)\rVert\le\tfrac12L\,\Delta\,\sqrt n\,\lVert D^{-1}\rVert .$$

:::

::: {.proof}

1. Interpolation gives $\Delta\,d_i^{\mathsf T}g=f(y_i)-f(x_k)$ for each $i$.

2. By Taylor's theorem with Lipschitz gradient, $f(y_i)-f(x_k)=\Delta\,d_i^{\mathsf T}\nabla f(x_k)+r_i$ with $\lvert r_i\rvert\le\tfrac L2\Delta^2$.

3. Subtracting, $\Delta\,D^{\mathsf T}(g-\nabla f(x_k))=r$, so $\lVert g-\nabla f(x_k)\rVert\le\Delta^{-1}\lVert D^{-\mathsf T}\rVert\,\lVert r\rVert\le\Delta^{-1}\lVert D^{-1}\rVert\sqrt n\,\tfrac L2\Delta^2$.

:::

The error is proportional to $\Delta$ times $\lVert D^{-1}\rVert$, which measures how degenerate the simplex is. So the method must keep its interpolation points *well poised* (not nearly on a hyperplane) and shrink $\Delta$ as it converges.

::: {#def-cobyla .definition name="A model-based trust-region method (COBYLA type)"}

Keep $n+1$ interpolation points around the current best point $x_k$ and a radius $\Delta_k$. At each step: build linear models of the objective and of every constraint; minimise the model objective subject to the linearised constraints and $\lVert x-x_k\rVert\le\Delta_k$ (a small linear program with a trust-region constraint); evaluate $f$ at the result; replace the worst point of the set (keeping it well poised); update $x_k$ if the new point is better; and shrink $\Delta_k$ when no progress is made at the current radius. Stop when $\Delta_k$ falls below a tolerance. BOBYQA and NEWUOA follow the same pattern with quadratic models, which converge much faster on smooth problems.

:::

```{=latex}
\begin{algorithm}
\caption{Derivative-free trust-region method with interpolation models}
\begin{algorithmic}
\INPUT $f$, initial point $x_0$, radius $\Delta_0$, final radius $\Delta_{\text{end}}$
\STATE choose a well-poised set $Y$ of interpolation points around $x_0$ and evaluate $f$ on it
\WHILE{$\Delta>\Delta_{\text{end}}$}
    \STATE build the model $m$ interpolating $f$ on $Y$
    \STATE $x^+\gets\operatorname{argmin}\{m(x):\lVert x-x_k\rVert\le\Delta\}$; evaluate $f(x^+)$
    \STATE replace a point of $Y$ by $x^+$, keeping $Y$ well poised
    \STATE \textbf{if} $f(x^+)<f(x_k)$ \textbf{then} $x_k\gets x^+$ \textbf{else if} the model is accurate at this radius \textbf{then} $\Delta\gets\Delta/2$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#fig-derivative-free-optimization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.3]
\foreach \s in {0.5,1.0,1.5,2.0} {\draw[faint, rotate around={-20:(2.6,1.6)}] (2.6,1.6) ellipse ({1.2*\s} and {0.6*\s});}
\coordinate (a) at (0,0); \coordinate (b) at (0.9,0.15); \coordinate (c) at (0.25,0.85);
\fill[tintA] (a) -- (b) -- (c) -- cycle; \draw (a) -- (b) -- (c) -- cycle;
\foreach \p in {a,b,c} {\fill (\p) circle (1.5pt);}
\node[lab, below left] at (a) {$x_k$};
\draw[faint, dashed] (a) circle (1.2);
\draw[hl, ->] (a) -- (0.98,0.69);
\fill[accent] (0.98,0.69) circle (1.6pt) node[lab, right] {$x^+$};
\node[note] at (-0.2,-1.45) {trust region $\lVert x-x_k\rVert\le\Delta$};
\node[note] at (3.4,0.15) {level curves of $f$};
\end{tikzpicture}
\end{center}
```

One step of a linear-model method in two dimensions: $f$ is evaluated at the three vertices of a simplex (shaded), the plane through these values gives a model gradient, and the model is minimised over the trust region. The new point $x^+$ then replaces a vertex of the simplex.

:::

::: {#rmk-derivative-free-optimization-1 .remark name="Nelder–Mead and the cost of not having gradients"}

The popular *Nelder–Mead* simplex method moves a simplex by reflections, expansions and contractions using only comparisons of function values. It is robust and simple; on the Rosenbrock function from $(-1.2,1)$ scipy's implementation needs $249$ function evaluations to reach $f\approx10^{-21}$. But it has no convergence guarantee (it can stall at non-stationary points), and like all derivative-free methods its cost grows quickly with the dimension, since $n+1$ or more values are needed just to see one gradient. When derivatives can be obtained, by hand, by automatic differentiation or by adjoints (@sec-math-optimization-algorithms-adjoint-methods), gradient-based methods are almost always preferable for more than a handful of variables.

:::
