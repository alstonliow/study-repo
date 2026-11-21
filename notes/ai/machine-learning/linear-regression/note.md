---
title: "Linear Regression"
sources: [cs221-2]
requires: [ai/machine-learning/supervised-learning, math/calculus/multivariable/differentiation/gradient]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 2 (linear regression), in our own wording. The minimizer is the least squares line of @sec-math-linear-algebra-orthogonality-least-squares and @sec-math-calculus-multivariable-differentiation-least-squares-fitting; this note takes the learning view (loss, gradient) and links those notes instead of repeating them. -->

::: {#def-linear-predictor .definition name="Linear predictor"}

For inputs $\mathbf{x}\in\mathbb{R}^d$, the parameters $\theta=(\mathbf{w},b)$ consist of a *weight vector* $\mathbf{w}\in\mathbb{R}^d$ and a *bias* $b\in\mathbb{R}$, and the *linear predictor* is

$$
f_\theta(\mathbf{x})=\mathbf{w}\cdot\mathbf{x}+b.
$$

The hypothesis class of linear regression is $\{f_\theta:\mathbf{w}\in\mathbb{R}^d,\ b\in\mathbb{R}\}$.

:::

::: {#def-squared-loss .definition name="Squared loss"}

The *residual* of $f_\theta$ on an example $(\mathbf{x},y)$ is $f_\theta(\mathbf{x})-y$, and the *squared loss* is its square,

$$
\text{Loss}(\mathbf{x},y,\theta)=(\mathbf{w}\cdot\mathbf{x}+b-y)^2.
$$

Linear regression minimizes the training loss built from it, the mean squared residual.

:::

::: {#fig-linear-regression-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-2.8,0) -- (2.8,0) node[lab, right] {$r$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {};
\draw[emph, domain=-2.2:2.2, samples=80, smooth, variable=\x] plot ({\x}, {0.5*\x*\x});
\draw[faint, domain=-2.2:2.2, samples=80, smooth, variable=\x] plot ({\x}, {abs(\x)});
\node[tick] at (2.4,2.3) {$r^2$};
\node[tick] at (-2.5,1.8) {$|r|$};
\end{tikzpicture}
\end{center}
```

The squared loss as a function of the residual $r=\mathbf w\cdot\phi(x)-y$, scaled by $\tfrac12$, against the absolute loss (faint): the squared loss punishes large residuals much more

:::

::: {#thm-squared-loss-gradient .theorem name="Gradient of the squared loss"}

For one example,

$$
\nabla_{\mathbf{w}}\text{Loss}(\mathbf{x},y,\theta)=2\,(\mathbf{w}\cdot\mathbf{x}+b-y)\,\mathbf{x},\qquad
\frac{\partial}{\partial b}\text{Loss}(\mathbf{x},y,\theta)=2\,(\mathbf{w}\cdot\mathbf{x}+b-y),
$$

and the gradient of the training loss is the average of these over $\mathcal D$.

:::

::: {.proof}

1. Write $r=\mathbf{w}\cdot\mathbf{x}+b-y$, so $\text{Loss}=r^2$ and $\partial\text{Loss}/\partial r=2r$.

2. Since $r$ is linear in the parameters, $\partial r/\partial w_j=x_j$ and $\partial r/\partial b=1$.

3. By the chain rule, $\partial\text{Loss}/\partial w_j=2r\,x_j$ and $\partial\text{Loss}/\partial b=2r$, which are the stated formulas.

4. The training loss is an average of per-example losses and the gradient is linear, so its gradient is the average of the per-example gradients.

:::

::: {#exm-linear-regression-1 .example name="Hours studied and exam score"}

Take $d=1$ and the training data $(1,4)$, $(2,6)$, $(4,7)$ (hours studied, score). For $(w,b)=(0,1)$ the residuals are $-3,-5,-6$, so

$$
\text{TrainLoss}(0,1)=\tfrac{9+25+36}{3}=\tfrac{70}{3}\approx23.33,
$$

and by @thm-squared-loss-gradient the gradient is $\bigl(\tfrac{2}{3}(-3-10-24),\ \tfrac{2}{3}(-3-5-6)\bigr)=\bigl(-\tfrac{74}{3},-\tfrac{28}{3}\bigr)$: both parameters should increase. Setting the gradient to zero gives the minimizer $w=\tfrac{13}{14}\approx0.93$, $b=\tfrac{7}{2}$, with training loss $\tfrac{3}{14}\approx0.21$; it is the least squares line (@thm-least-squares-normal-equations).

:::

::: {#fig-linear-regression-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.32cm]
\draw[->] (0,0) -- (5,0) node[lab,anchor=north east] {hours $x$};
\draw[->] (0,0) -- (0,9) node[lab,anchor=north west] {score $y$};
\foreach \x in {1,2,3,4} { \node[lab,tick] at (\x,-0.7) {\x}; }
\foreach \y in {2,4,6,8} { \node[lab,tick] at (-0.3,\y) {\y}; }
\draw[faint] (0,1) -- (4.8,1) node[lab,anchor=south east] {$w=0,\ b=1$};
\draw[hl] (0,3.5) -- (4.8,{3.5+4.8*13/14}) node[lab,anchor=south east] {$w=\tfrac{13}{14},\ b=\tfrac72$};
\draw[faint,dashed] (1,4) -- (1,{3.5+13/14});
\draw[faint,dashed] (2,6) -- (2,{3.5+26/14});
\draw[faint,dashed] (4,7) -- (4,{3.5+52/14});
\node[dot] at (1,4) {}; \node[dot] at (2,6) {}; \node[dot] at (4,7) {};
\end{tikzpicture}
\end{center}
```

The three training examples of @exm-linear-regression-1, the predictor $w=0$, $b=1$ and the minimizer of the training loss, with its residuals dashed.

:::

::: {#rmk-linear-regression-1 .remark name="Closed form versus gradient descent" related="thm-least-squares-normal-equations"}

For the squared loss the minimizer has a closed form, the solution of the normal equations (@sec-math-linear-algebra-orthogonality-least-squares). Learning uses gradient descent (@sec-ai-machine-learning-gradient-descent) anyway, because it works unchanged for other losses and for hypothesis classes such as neural networks where no closed form exists.

:::
