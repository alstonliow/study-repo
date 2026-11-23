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
