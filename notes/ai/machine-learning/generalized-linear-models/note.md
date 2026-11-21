---
title: "Generalized Linear Models"
sources: [cs229-2, cs229-3]
requires: [math/probability/continuous/exponential-family, ai/machine-learning/logistic-regression, math/optimization/algorithms/newtons-method-for-minimization]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 3 (constructing GLMs; least squares and logistic regression as GLMs) and Chapter 2.4 (Newton's method for the log-likelihood), in our own wording. The general gradient and Hessian, the Poisson example and the Newton step for any GLM are our own; proofs written out in steps. -->

Linear regression and logistic regression look like separate inventions, but both arise from one recipe: choose an exponential family for the label, let its natural parameter be linear in the input, and fit by maximum likelihood.

::: {#def-glm .definition name="Generalized linear model"}

Fix an exponential family $p(y;\eta)=b(y)\exp\bigl(\eta\,T(y)-a(\eta)\bigr)$ with a scalar natural parameter (@def-exponential-family). A *generalized linear model* (GLM) with parameters $\boldsymbol\theta\in\mathbb{R}^d$ assumes:

1. given the input $\mathbf{x}$, the label has distribution $y\mid\mathbf{x};\boldsymbol\theta\sim p(\,\cdot\,;\eta)$ in this family;
2. the natural parameter is linear in the input: $\eta=\boldsymbol\theta^{\mathsf T}\mathbf{x}$;
3. the prediction is the conditional mean of the sufficient statistic, $h_{\boldsymbol\theta}(\mathbf{x})=E[T(y)\mid\mathbf{x};\boldsymbol\theta]$.

The function $g(\eta)=E[T(y);\eta]$ that turns the natural parameter into the mean is the *canonical response function*; its inverse $g^{-1}$ is the *canonical link function*. With $T(y)=y$, @prp-exponential-family-moments gives $g=a'$, so $h_{\boldsymbol\theta}(\mathbf{x})=a'(\boldsymbol\theta^{\mathsf T}\mathbf{x})$.

:::

::: {#exm-glm-examples .example name="Three GLMs"}

1. *Gaussian labels, $\sigma^2=1$.* Here $a(\eta)=\eta^2/2$, so $g(\eta)=\eta$ and $h_{\boldsymbol\theta}(\mathbf{x})=\boldsymbol\theta^{\mathsf T}\mathbf{x}$: ordinary least squares (@def-linear-predictor).

2. *Bernoulli labels $y\in\{0,1\}$.* Here $a(\eta)=\log(1+e^\eta)$, so $g(\eta)=1/(1+e^{-\eta})$ and $h_{\boldsymbol\theta}(\mathbf{x})=\sigma(\boldsymbol\theta^{\mathsf T}\mathbf{x})$: logistic regression (@def-logistic-regression, written there with labels $\pm1$). The sigmoid is not a design choice; it is the canonical response of the Bernoulli family.

3. *Poisson labels (counts).* Here $a(\eta)=e^\eta$, so $h_{\boldsymbol\theta}(\mathbf{x})=e^{\boldsymbol\theta^{\mathsf T}\mathbf{x}}$: *Poisson regression*, for example to predict the number of visitors to a shop from the weather and the day of the week.

:::

::: {#thm-glm-likelihood .theorem name="Gradient and Hessian of a GLM log-likelihood"}

For a GLM with $T(y)=y$ and training examples $(\mathbf{x}^{(i)},y^{(i)})$, $i=1,\dots,N$, the log-likelihood

$$
\ell(\boldsymbol\theta)=\sum_{i=1}^N\log p\bigl(y^{(i)}\mid\mathbf{x}^{(i)};\boldsymbol\theta\bigr)
$$

has gradient and Hessian

$$
\nabla\ell(\boldsymbol\theta)=\sum_{i=1}^N\bigl(y^{(i)}-h_{\boldsymbol\theta}(\mathbf{x}^{(i)})\bigr)\mathbf{x}^{(i)},\qquad \nabla^2\ell(\boldsymbol\theta)=-\sum_{i=1}^Na''\bigl(\boldsymbol\theta^{\mathsf T}\mathbf{x}^{(i)}\bigr)\,\mathbf{x}^{(i)}\mathbf{x}^{(i)\mathsf T}.
$$

The Hessian is negative semidefinite, so $\ell$ is concave.

:::

::: {.proof}

1. Write $\eta_i=\boldsymbol\theta^{\mathsf T}\mathbf{x}^{(i)}$. Then $\log p(y^{(i)}\mid\mathbf{x}^{(i)};\boldsymbol\theta)=\log b(y^{(i)})+\eta_iy^{(i)}-a(\eta_i)$.

2. Since $\nabla_{\boldsymbol\theta}\eta_i=\mathbf{x}^{(i)}$, the chain rule gives the gradient of the $i$th term as $\bigl(y^{(i)}-a'(\eta_i)\bigr)\mathbf{x}^{(i)}$, and $a'(\eta_i)=h_{\boldsymbol\theta}(\mathbf{x}^{(i)})$ by @def-glm.

3. Differentiating once more, the Hessian of the $i$th term is $-a''(\eta_i)\,\mathbf{x}^{(i)}\mathbf{x}^{(i)\mathsf T}$. Summing proves both formulas.

4. By @prp-exponential-family-moments, $a''(\eta_i)$ is a variance, hence $\ge0$. For any $\mathbf{v}$, $\mathbf{v}^{\mathsf T}\nabla^2\ell\,\mathbf{v}=-\sum_ia''(\eta_i)(\mathbf{v}^{\mathsf T}\mathbf{x}^{(i)})^2\le0$, so $\ell$ is concave.

:::

::: {#rmk-glm-1 .remark name="One update rule for all GLMs"}

By @thm-glm-likelihood, stochastic gradient ascent on the log-likelihood uses the same rule for every GLM,

$$
\boldsymbol\theta\leftarrow\boldsymbol\theta+\alpha\bigl(y^{(i)}-h_{\boldsymbol\theta}(\mathbf{x}^{(i)})\bigr)\mathbf{x}^{(i)},
$$

"prediction error times input"; only $h_{\boldsymbol\theta}$ changes. For least squares this is the LMS (Widrow–Hoff) rule, the stochastic gradient step on the squared loss (@def-stochastic-gradient-descent). Concavity means there are no spurious local maxima.

:::

::: {#prp-glm-newton-step .proposition name="Newton's method for a GLM"}

Let $X$ have rows $\mathbf{x}^{(i)\mathsf T}$, let $\mathbf{h}$ have entries $h_{\boldsymbol\theta}(\mathbf{x}^{(i)})$ and let $S=\operatorname{diag}\bigl(a''(\boldsymbol\theta^{\mathsf T}\mathbf{x}^{(i)})\bigr)$. If $X^{\mathsf T}SX$ is invertible, the Newton step for maximizing $\ell$ (@def-newton-step applied to $-\ell$) is

$$
\boldsymbol\theta\leftarrow\boldsymbol\theta+(X^{\mathsf T}SX)^{-1}X^{\mathsf T}(\mathbf{y}-\mathbf{h}).
$$

For logistic regression $S=\operatorname{diag}\bigl(h_i(1-h_i)\bigr)$. For least squares $S=I$ and $\mathbf{h}=X\boldsymbol\theta$, and one step lands on the solution of the normal equations from any start.

:::

::: {.proof}

1. Newton's method for minimizing $f=-\ell$ moves by $-\bigl(\nabla^2f\bigr)^{-1}\nabla f=-(\nabla^2\ell)^{-1}\nabla\ell$.

2. In matrix form @thm-glm-likelihood reads $\nabla\ell=X^{\mathsf T}(\mathbf{y}-\mathbf{h})$ and $\nabla^2\ell=-X^{\mathsf T}SX$, which gives the step.

3. For the Bernoulli family $a''(\eta)=\phi(1-\phi)$ with $\phi=h$ (@exm-exponential-family-moments).

4. For least squares the step is $\boldsymbol\theta+(X^{\mathsf T}X)^{-1}(X^{\mathsf T}\mathbf{y}-X^{\mathsf T}X\boldsymbol\theta)=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbf{y}$, whatever $\boldsymbol\theta$ was.

:::

::: {#rmk-glm-2 .remark name="Softmax as a GLM" editor="No figure for Newton on a GLM: its iterates are parameter vectors, and the Newton picture is in the convex optimization notes."}

The categorical distribution on $K$ classes is also an exponential family: take $T(y)$ to be the one-hot vector of $y$ without its last entry and $\eta_k=\log(\phi_k/\phi_{K-1})$. Its canonical response is the softmax, and making each $\eta_k$ linear in $\mathbf{x}$ gives the multiclass linear model of @def-softmax. Newton's method on logistic regression is usually much faster than gradient ascent in iterations (quadratic convergence near the optimum, @thm-newton-classical-convergence), but each step solves a $d\times d$ system, so it is preferred when $d$ is small.

:::
