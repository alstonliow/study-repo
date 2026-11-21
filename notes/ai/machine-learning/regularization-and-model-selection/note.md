---
title: "Regularization and Model Selection"
sources: [cs229-9]
requires: [ai/machine-learning/bias-variance-tradeoff, math/probability/estimation/bayesian-inference, math/linear-algebra/matrix-methods/matrix-derivatives]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 9 (regularization, implicit regularization of the optimizer, cross validation, the Bayesian view of regularization), in our own wording. The ridge closed form, the minimum-norm proposition with its proof and the examples are our own, checked in Python; proofs written out in steps. Choosing hyperparameters on held-out data is introduced in @sec-ai-machine-learning-generalization. -->

The bias-variance tradeoff (@thm-bias-variance-decomposition) is controlled by model complexity. Two tools adjust it: a penalty that pulls the parameters towards simple values, and a data-based procedure for choosing among models.

::: {#def-regularization .definition name="Regularization"}

A *regularized* training objective adds a penalty to the training loss:

$$
J_\lambda(\boldsymbol\theta)=J(\boldsymbol\theta)+\lambda R(\boldsymbol\theta),\qquad\lambda\ge0.
$$

Common choices are $R(\boldsymbol\theta)=\tfrac12\lVert\boldsymbol\theta\rVert_2^2$ (*$\ell_2$ regularization*, also called *weight decay*, since each gradient step first shrinks $\boldsymbol\theta$ by the factor $1-\alpha\lambda$), $R(\boldsymbol\theta)=\lVert\boldsymbol\theta\rVert_1$ (*$\ell_1$*, which tends to make many parameters exactly zero) and the number of nonzero parameters (*$\ell_0$*, the sparsest choice but hard to optimize). Least squares with $\ell_2$ regularization is *ridge regression*. The intercept is usually not penalized.

:::

::: {#fig-regularization-and-model-selection-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-1.8,0) -- (3.6,0) node[lab, right] {$\theta_1$};
\draw[->] (0,-1.6) -- (0,3.0) node[lab, above] {$\theta_2$};
\draw[faint, rotate around={-30:(2.4,1.8)}] (2.4,1.8) ellipse (0.60 and 0.30);
\draw[faint, rotate around={-30:(2.4,1.8)}] (2.4,1.8) ellipse (1.30 and 0.65);
\draw[faint, rotate around={-30:(2.4,1.8)}] (2.4,1.8) ellipse (2.05 and 1.02);
\draw[regionA] (0,0) circle (1.05);
\node[hl dot] at (0.78,0.7) {};
\node[dot] at (2.4,1.8) {};
\node[tick, right] at (2.5,1.8) {unregularized};
\end{tikzpicture}
\end{center}
```

An $\ell_2$ penalty in picture form: the regularized solution (highlighted) is where a contour of the training loss first touches a ball around the origin, so it is pulled towards $\mathbf 0$

:::

::: {#prp-ridge-closed-form .proposition name="Ridge regression in closed form"}

For $J(\boldsymbol\theta)=\tfrac12\lVert X\boldsymbol\theta-\mathbf{y}\rVert^2$ and $\lambda>0$, the ridge objective $J(\boldsymbol\theta)+\tfrac\lambda2\lVert\boldsymbol\theta\rVert^2$ has the unique minimizer

$$
\boldsymbol\theta_\lambda=(X^{\mathsf T}X+\lambda I)^{-1}X^{\mathsf T}\mathbf{y},
$$

and $X^{\mathsf T}X+\lambda I$ is invertible for every $X$.

:::

::: {.proof}

1. By @prp-matrix-gradient-rules the gradient is $X^{\mathsf T}X\boldsymbol\theta-X^{\mathsf T}\mathbf{y}+\lambda\boldsymbol\theta$, which vanishes exactly when $(X^{\mathsf T}X+\lambda I)\boldsymbol\theta=X^{\mathsf T}\mathbf{y}$.

2. For $\mathbf{v}\ne\mathbf{0}$, $\mathbf{v}^{\mathsf T}(X^{\mathsf T}X+\lambda I)\mathbf{v}=\lVert X\mathbf{v}\rVert^2+\lambda\lVert\mathbf{v}\rVert^2>0$. So the matrix is positive definite, hence invertible, and the objective is strictly convex.

3. A strictly convex function has at most one minimizer, and its stationary point is one.

:::

::: {#exm-ridge-one-feature .example name="Shrinkage with one feature"}

With one feature and no intercept, inputs $1,2,3$ and labels $1,2,2$, the formula reads $\theta_\lambda=\sum_ix_iy_i/(\sum_ix_i^2+\lambda)=11/(14+\lambda)$: $\theta_0\approx0.786$ (least squares), $\theta_1\approx0.733$ and $\theta_{10}\approx0.458$. Larger $\lambda$ shrinks the slope towards $0$, trading variance for bias.

:::

::: {#fig-regularization-and-model-selection-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$\lambda$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$\theta_\lambda$};
\draw[emph, domain=0:6, samples=80, smooth, variable=\x] plot ({\x}, {2.6*11/(14+\x*5)});
\draw (0,0) -- (0,-0.08) node[tick, below] {$0$};
\draw (1,0) -- (1,-0.08) node[tick, below] {$5$};
\draw (2,0) -- (2,-0.08) node[tick, below] {$10$};
\draw (6,0) -- (6,-0.08) node[tick, below] {$30$};
\draw (0,2.04) -- (-0.08,2.04) node[tick, left] {$0.79$};
\end{tikzpicture}
\end{center}
```

The ridge estimate $\theta_\lambda=11/(14+\lambda)$ of @exm-ridge-one-feature shrinks from the least squares value $0.79$ towards $0$ as $\lambda$ grows

:::

::: {#prp-gd-min-norm .proposition name="Gradient descent finds the minimum-norm solution"}

Let $X\boldsymbol\theta=\mathbf{y}$ have solutions (as when there are more parameters than examples and $X$ has full row rank). If gradient descent on $J(\boldsymbol\theta)=\tfrac12\lVert X\boldsymbol\theta-\mathbf{y}\rVert^2$ starts at $\boldsymbol\theta=\mathbf{0}$ and converges, its limit is the solution of $X\boldsymbol\theta=\mathbf{y}$ of smallest Euclidean norm.

:::

::: {.proof}

1. Each step subtracts $\alpha X^{\mathsf T}(X\boldsymbol\theta-\mathbf{y})$, a vector in the row space $R=\operatorname{range}(X^{\mathsf T})$. Starting from $\mathbf{0}$, every iterate lies in $R$, and so does the limit $\boldsymbol\theta_\infty$, since $R$ is closed.

2. At the limit the gradient is zero: $X^{\mathsf T}(X\boldsymbol\theta_\infty-\mathbf{y})=\mathbf{0}$. Since $\mathbf{y}=X\boldsymbol\theta_0$ for some solution $\boldsymbol\theta_0$, the vector $X\boldsymbol\theta_\infty-\mathbf{y}=X(\boldsymbol\theta_\infty-\boldsymbol\theta_0)$ lies in the column space of $X$ and in the null space of $X^{\mathsf T}$, which are orthogonal complements. So it is zero and $\boldsymbol\theta_\infty$ is a solution.

3. Every solution has the form $\boldsymbol\theta_\infty+\mathbf{n}$ with $X\mathbf{n}=\mathbf{0}$, and the null space of $X$ is orthogonal to $R$. By Pythagoras $\lVert\boldsymbol\theta_\infty+\mathbf{n}\rVert^2=\lVert\boldsymbol\theta_\infty\rVert^2+\lVert\mathbf{n}\rVert^2$, which is smallest for $\mathbf{n}=\mathbf{0}$.

:::

::: {#exm-gd-min-norm .example name="Two equations, three unknowns"}

The equations $\theta_1+\theta_2=1$ and $\theta_2+\theta_3=2$ have the solutions $(0,1,1)+t(1,-1,1)$. Gradient descent from $\mathbf{0}$ with step $0.1$ converges to $(0,1,1)$, the solution of norm $\sqrt2$, which is orthogonal to the null direction $(1,-1,1)$; for $t\ne0$ the norm is $\sqrt{2+3t^2}$.

:::

::: {#rmk-implicit-regularization .remark name="Implicit regularization"}

When a model can fit the training data in many ways, the optimizer and its settings (initialization, step size, batch size, number of steps) choose which fit is returned. @prp-gd-min-norm is the simplest instance: gradient descent behaves as if it penalized $\lVert\boldsymbol\theta\rVert$ without being told to. In deep networks similar effects are believed to favour solutions that generalize, and stopping early acts like a penalty too.

:::

::: {#def-cross-validation .definition name="Cross validation"}

To choose among candidate models $M_1,\dots,M_m$ (different hypothesis classes, or different values of $\lambda$):

1. *Hold-out validation*: split the training data into a training part (say 70%) and a validation part; train each $M_j$ on the first, evaluate it on the second, and pick the best. Optionally retrain the winner on all the data.
2. *$k$-fold cross validation*: split the data into $k$ disjoint parts of equal size. For each $M_j$ and each part, train on the other $k-1$ parts and measure the error on the held-out part; average the $k$ errors, and pick the model with the smallest average. Then retrain it on all the data.
3. *Leave-one-out cross validation* is $k$-fold with $k=N$.

Larger $k$ wastes less data on validation but costs $k$ trainings per model; $k=10$ is a common default. The test set (@def-test-error) is never used for this choice.

:::

::: {#fig-regularization-and-model-selection-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.0,-0.0) rectangle (1.0,0.45);
\draw[cell frame] (1.0,-0.0) rectangle (2.0,0.45);
\draw[cell frame] (2.0,-0.0) rectangle (3.0,0.45);
\draw[cell frame] (3.0,-0.0) rectangle (4.0,0.45);
\draw[cell frame] (4.0,-0.0) rectangle (5.0,0.45);
\node[tick, left] at (0,0.22) {round $1$};
\draw[cell frame] (0.0,-0.5) rectangle (1.0,-0.05);
\draw[hl cell] (1.0,-0.5) rectangle (2.0,-0.05);
\draw[cell frame] (2.0,-0.5) rectangle (3.0,-0.05);
\draw[cell frame] (3.0,-0.5) rectangle (4.0,-0.05);
\draw[cell frame] (4.0,-0.5) rectangle (5.0,-0.05);
\node[tick, left] at (0,-0.28) {round $2$};
\draw[cell frame] (0.0,-1.0) rectangle (1.0,-0.55);
\draw[cell frame] (1.0,-1.0) rectangle (2.0,-0.55);
\draw[hl cell] (2.0,-1.0) rectangle (3.0,-0.55);
\draw[cell frame] (3.0,-1.0) rectangle (4.0,-0.55);
\draw[cell frame] (4.0,-1.0) rectangle (5.0,-0.55);
\node[tick, left] at (0,-0.78) {round $3$};
\draw[cell frame] (0.0,-1.5) rectangle (1.0,-1.05);
\draw[cell frame] (1.0,-1.5) rectangle (2.0,-1.05);
\draw[cell frame] (2.0,-1.5) rectangle (3.0,-1.05);
\draw[hl cell] (3.0,-1.5) rectangle (4.0,-1.05);
\draw[cell frame] (4.0,-1.5) rectangle (5.0,-1.05);
\node[tick, left] at (0,-1.28) {round $4$};
\draw[cell frame] (0.0,-2.0) rectangle (1.0,-1.55);
\draw[cell frame] (1.0,-2.0) rectangle (2.0,-1.55);
\draw[cell frame] (2.0,-2.0) rectangle (3.0,-1.55);
\draw[cell frame] (3.0,-2.0) rectangle (4.0,-1.55);
\draw[hl cell] (4.0,-2.0) rectangle (5.0,-1.55);
\node[tick, left] at (0,-1.78) {round $5$};
\node[tick, right] at (5.1,-0.8) {highlighted: validation fold};
\end{tikzpicture}
\end{center}
```

Five-fold cross validation: each round trains on four folds and validates on the fifth, and the five validation errors are averaged

:::

::: {#prp-map-ridge .proposition name="Ridge regression is a MAP estimate"}

Assume $y^{(i)}=\boldsymbol\theta^{\mathsf T}\mathbf{x}^{(i)}+\xi^{(i)}$ with independent noise $\xi^{(i)}\sim N(0,\sigma^2)$ and the prior $\boldsymbol\theta\sim N(\mathbf{0},\tau^2I)$. Then the MAP estimate (@def-map-lms-estimates) of $\boldsymbol\theta$ is the ridge solution of @prp-ridge-closed-form with $\lambda=\sigma^2/\tau^2$.

:::

::: {.proof}

1. The posterior is proportional to likelihood times prior, so the MAP estimate maximizes

   $$
   \sum_i\log p(y^{(i)}\mid\mathbf{x}^{(i)},\boldsymbol\theta)+\log p(\boldsymbol\theta)=-\frac1{2\sigma^2}\sum_i\bigl(y^{(i)}-\boldsymbol\theta^{\mathsf T}\mathbf{x}^{(i)}\bigr)^2-\frac1{2\tau^2}\lVert\boldsymbol\theta\rVert^2+\text{const}.
   $$

2. Multiplying by $-\sigma^2$ turns this into minimizing $\tfrac12\lVert X\boldsymbol\theta-\mathbf{y}\rVert^2+\tfrac{\sigma^2}{2\tau^2}\lVert\boldsymbol\theta\rVert^2$, the ridge objective with $\lambda=\sigma^2/\tau^2$.

:::

::: {#rmk-regularization-bayes .remark name="Frequentist and Bayesian views"}

Maximum likelihood treats $\boldsymbol\theta$ as an unknown constant; the Bayesian view treats it as random with a prior (@sec-math-probability-estimation-classical-estimation). A strong prior (small $\tau$) means a large $\lambda$. A Laplace prior gives $\ell_1$ regularization in the same way. The fully Bayesian prediction averages over the posterior, $p(y\mid\mathbf{x},S)=\int p(y\mid\mathbf{x},\boldsymbol\theta)\,p(\boldsymbol\theta\mid S)\,d\boldsymbol\theta$, which is usually intractable; MAP replaces the posterior by its mode.

:::
