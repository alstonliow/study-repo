---
title: "Generalized Linear Models"
sources: [cs229-2, cs229-3, mit18650-10]
requires: [math/probability/distributions/exponential-family, ai/machine-learning/logistic-regression, math/optimization/algorithms/newtons-method-for-minimization, math/statistics/inference/fisher-information, math/statistics/frequentist/multiple-linear-regression]
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

::: {#rmk-glm-2 .remark name="Softmax as a GLM" editor="The Newton iterates of a small logistic regression are drawn in the IRLS example below (IRLS is Newton's method for the canonical link); the general Newton picture is in the convex optimization notes."}

The categorical distribution on $K$ classes is also an exponential family: take $T(y)$ to be the one-hot vector of $y$ without its last entry and $\eta_k=\log(\phi_k/\phi_{K-1})$. Its canonical response is the softmax, and making each $\eta_k$ linear in $\mathbf{x}$ gives the multiclass linear model of @def-softmax. Newton's method on logistic regression is usually much faster than gradient ascent in iterations (quadratic convergence near the optimum, @thm-newton-classical-convergence), but each step solves a $d\times d$ system, so it is preferred when $d$ is small.

:::

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 10 (GLMs with a dispersion parameter and an arbitrary link: link functions, canonical link, log-likelihood, Fisher scoring, iteratively reweighted least squares), in our own wording; derivations written out in steps, the numerical example is our own. Overlap with def-glm, thm-glm-likelihood and prp-glm-newton-step (the canonical case): owner approved 2026-11-21 to keep both levels, linked by generalizes, since CS229 covers only the canonical blocks; the canonical link points to def-glm instead of being defined twice. -->

The model of @def-glm ties the natural parameter to the input directly, $\eta=\boldsymbol\theta^{\mathsf T}\mathbf x$, which is the *canonical* choice. Statistics often needs other ways of linking the mean to the covariates, for instance a probit instead of a logistic curve, or a log link for Gamma responses. In this part we use the statistical notation: covariates $X_i\in\mathbb{R}^p$, coefficients $\beta$ (the $\boldsymbol\theta$ of @def-glm), and responses $Y_i$ with density $f_{\theta_i}(y)=\exp\bigl((y\theta_i-b(\theta_i))/\phi+c(y,\phi)\bigr)$ in a dispersion family (@def-exponential-dispersion-family) with known $\phi$, so $\mu_i=E[Y_i\mid X_i]=b'(\theta_i)$ and $V_i=b''(\theta_i)$ (@prp-dispersion-family-moments).

::: {#def-link-function .definition name="Link function, canonical link" generalizes="def-glm"}

A *link function* is a strictly increasing, differentiable function $g$ from the range of the mean to $\mathbb{R}$; the GLM with link $g$ assumes
$$g(\mu_i)=X_i^{\mathsf T}\beta,\qquad\text{that is}\qquad \mu_i=g^{-1}(X_i^{\mathsf T}\beta).$$
The *canonical link* is $g=(b')^{-1}$, the link for which $\theta_i=X_i^{\mathsf T}\beta$, which is the model of @def-glm (there with $\phi=1$); it is strictly increasing because $b''>0$. In general $\theta_i=h(X_i^{\mathsf T}\beta)$ with $h=(b')^{-1}\circ g^{-1}=(g\circ b')^{-1}$, and $h$ is the identity exactly for the canonical link.

:::

::: {#fig-generalized-linear-models-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (x) at (0,0) {$\mathbf x$};
\node[box] (e) at (2.4,0) {$\eta=\boldsymbol\theta^{\mathsf T}\mathbf x$};
\node[hl box] (m) at (6.2,0) {$\mu=g^{-1}(\eta)$};
\node[box] (y) at (9.4,0) {$y\sim$ family$(\mu)$};
\draw[map] (x) -- (e);
\draw[map] (e) -- node[edge label] {inverse link} (m);
\draw[map] (m) -- (y);
\end{tikzpicture}
\end{center}
```

The three parts of a generalized linear model: a linear predictor $\eta$, an inverse link mapping it to the mean $\mu$, and an exponential-family distribution with that mean

:::

::: {#exm-link-functions .example name="Common links"}

1. *Normal responses:* identity link $g(\mu)=\mu$ (canonical), the linear model.
2. *Counts (Poisson):* the mean is positive, and the log link $g(\mu)=\log\mu$ (canonical) maps $(0,\infty)$ onto $\mathbb{R}$. A count growing exponentially in time, $\mu_t=\gamma e^{\delta t}$, becomes $\log\mu_t=\log\gamma+\delta t$.
3. *Binary responses:* $g$ must map $(0,1)$ onto $\mathbb{R}$. Choices are the *logit* $\log\frac\mu{1-\mu}$ (canonical: logistic regression), the *probit* $\Phi^{-1}(\mu)$, and the *complementary log-log* $\log(-\log(1-\mu))$.
4. *Positive continuous responses (Gamma):* the canonical link is $-1/\mu$; the reciprocal link $1/\mu$ (the same up to sign) makes a saturating mean such as $\mu=\alpha x/(h+x)$ linear in $1/x$: $1/\mu=1/\alpha+(h/\alpha)(1/x)$. The log link is also common.

:::

::: {#fig-generalized-linear-models-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-3.4,0) -- (3.4,0) node[lab, right] {$\eta$};
\draw[->] (0,0) -- (0,3.0) node[lab, above] {$\mu$};
\draw[emph, domain=-3.2:3.2, samples=80, smooth, variable=\x] plot ({\x}, {2/(1+exp(-\x))});
\draw[hl, domain=-3.2:2.2, samples=80, smooth, variable=\x] plot ({\x}, {0.3*exp(\x)});
\draw[faint, domain=-3.2:3.2, samples=80, smooth, variable=\x] plot ({\x}, {1+0.4*\x});
\node[tick] at (2.9,1.75) {logistic};
\node[tick, text=accent] at (1.6,2.8) {$e^\eta$};
\node[tick] at (-2.7,0.2) {identity};
\end{tikzpicture}
\end{center}
```

Inverse links of three canonical GLMs: identity (normal, $\mu\in\mathbb R$, rescaled), exponential (Poisson, $\mu>0$) and logistic (Bernoulli, $\mu\in(0,1)$, scaled to height $2$)

:::

::: {#thm-glm-score-information .theorem name="Score and Fisher information of a GLM" generalizes="thm-glm-likelihood"}

Let $Y_1,\dots,Y_n$ be independent given the fixed covariates, following the GLM with link $g$. Write $\eta_i=X_i^{\mathsf T}\beta$, $\mu_i=g^{-1}(\eta_i)$ and
$$W_i=\frac1{\phi\,V_i\,g'(\mu_i)^2},\qquad W=\operatorname{diag}(W_1,\dots,W_n).$$
The log-likelihood $\ell_n(\beta)=\sum_i\bigl(Y_i\theta_i-b(\theta_i)\bigr)/\phi+\text{const}$, with $\theta_i=h(\eta_i)$, has score and Fisher information

$$
\nabla\ell_n(\beta)=\sum_{i=1}^nW_i\,g'(\mu_i)\,(Y_i-\mu_i)\,X_i,\qquad I(\beta)=-E\bigl[\nabla^2\ell_n(\beta)\bigr]=\mathbb X^{\mathsf T}W\mathbb X,
$$

where $\mathbb X$ has rows $X_i^{\mathsf T}$. For the canonical link the Hessian itself equals $-\mathbb X^{\mathsf T}W\mathbb X$ and does not involve the $Y_i$.

:::

::: {.proof}

1. Since $g^{-1}=b'\circ h$, differentiating gives $(g^{-1})'(\eta)=b''(h(\eta))\,h'(\eta)$, and $(g^{-1})'(\eta_i)=1/g'(\mu_i)$. Hence $V_i\,h'(\eta_i)=1/g'(\mu_i)$.

2. *Score.* The $i$th term $\ell_i=(Y_i\theta_i-b(\theta_i))/\phi$ has $\partial\ell_i/\partial\theta_i=(Y_i-b'(\theta_i))/\phi=(Y_i-\mu_i)/\phi$, and $\nabla_\beta\theta_i=h'(\eta_i)X_i$. So $\nabla\ell_i=(Y_i-\mu_i)h'(\eta_i)X_i/\phi$, and by step 1, $h'(\eta_i)/\phi=1/(\phi V_ig'(\mu_i))=W_ig'(\mu_i)$.

3. *Hessian.* Differentiate $\nabla\ell_i=(Y_i-\mu_i)h'(\eta_i)X_i/\phi$ again. Using $\nabla_\beta\mu_i=b''(\theta_i)h'(\eta_i)X_i$,
   $$\nabla^2\ell_i=\frac1\phi\Bigl[(Y_i-\mu_i)h''(\eta_i)-V_i\,h'(\eta_i)^2\Bigr]X_iX_i^{\mathsf T}.$$

4. *Information.* $E[Y_i]=\mu_i$ removes the first term, so $-E[\nabla^2\ell_i]=V_ih'(\eta_i)^2X_iX_i^{\mathsf T}/\phi$. By step 1, $V_ih'(\eta_i)^2/\phi=1/(\phi V_ig'(\mu_i)^2)=W_i$. Summing gives $\mathbb X^{\mathsf T}W\mathbb X$.

5. For the canonical link $h$ is the identity, so $h''=0$ and the Hessian in step 3 equals its expectation.

:::

With the canonical link the log-likelihood is therefore concave (strictly so if $\mathbb X$ has rank $p$, since then $\mathbb X^{\mathsf T}W\mathbb X$ is positive definite), and the MLE is unique if it exists. With other links the log-likelihood need not be concave.

::: {#def-fisher-scoring .definition name="Fisher scoring"}

*Fisher scoring* maximises a log-likelihood $\ell_n$ by Newton's method with the Hessian replaced by its expectation $-I(\beta)$:
$$\beta^{(k+1)}=\beta^{(k)}+I\bigl(\beta^{(k)}\bigr)^{-1}\nabla\ell_n\bigl(\beta^{(k)}\bigr).$$

:::

The information matrix is positive semidefinite, often easier to compute than the Hessian, and the method has essentially the same convergence behaviour as Newton's method. For a GLM with the canonical link the two coincide by @thm-glm-score-information, and Fisher scoring is the Newton step of @prp-glm-newton-step.

::: {#prp-irls .proposition name="Fisher scoring is iteratively reweighted least squares" generalizes="prp-glm-newton-step"}

For a GLM, with $\mu_i,W_i$ evaluated at $\beta^{(k)}$ and $\mathbb X^{\mathsf T}W\mathbb X$ invertible, the Fisher scoring step is

$$
\beta^{(k+1)}=(\mathbb X^{\mathsf T}W\mathbb X)^{-1}\mathbb X^{\mathsf T}W\mathbf Z,\qquad Z_i=X_i^{\mathsf T}\beta^{(k)}+g'(\mu_i)\,(Y_i-\mu_i),
$$

the weighted least squares fit (@def-generalized-least-squares) of the *adjusted responses* $Z_i$ on $\mathbb X$ with weights $W_i$.

:::

::: {.proof}

1. By @thm-glm-score-information, $\nabla\ell_n=\mathbb X^{\mathsf T}W\mathbf r$ with $r_i=g'(\mu_i)(Y_i-\mu_i)$, and $I=\mathbb X^{\mathsf T}W\mathbb X$.

2. Then $\beta^{(k)}+I^{-1}\nabla\ell_n=(\mathbb X^{\mathsf T}W\mathbb X)^{-1}\bigl(\mathbb X^{\mathsf T}W\mathbb X\beta^{(k)}+\mathbb X^{\mathsf T}W\mathbf r\bigr)=(\mathbb X^{\mathsf T}W\mathbb X)^{-1}\mathbb X^{\mathsf T}W\bigl(\mathbb X\beta^{(k)}+\mathbf r\bigr)$.

3. $\mathbb X\beta^{(k)}+\mathbf r=\mathbf Z$, and $(\mathbb X^{\mathsf T}W\mathbb X)^{-1}\mathbb X^{\mathsf T}W\mathbf Z$ minimises $\sum_iW_i(Z_i-X_i^{\mathsf T}t)^2$ (its weighted normal equations).

:::

```{=latex}
\begin{algorithm}
\caption{Iteratively reweighted least squares (IRLS) for a GLM}
\begin{algorithmic}
\INPUT design $\mathbb X$ with rows $X_i^{\mathsf T}$; responses $Y_i$; link $g$; variance function $V(\mu)$; dispersion $\phi$
\STATE choose a start $\beta^{(0)}$ \COMMENT{for example from $\mu_i=Y_i$, adjusted away from the boundary}
\FOR{$k=0,1,2,\dots$ until $\beta^{(k)}$ stops changing}
    \STATE $\eta_i\gets X_i^{\mathsf T}\beta^{(k)}$, \quad $\mu_i\gets g^{-1}(\eta_i)$
    \STATE $Z_i\gets\eta_i+g'(\mu_i)(Y_i-\mu_i)$, \quad $W_i\gets1/\bigl(\phi\,V(\mu_i)\,g'(\mu_i)^2\bigr)$
    \STATE $\beta^{(k+1)}\gets\operatorname{argmin}_t\sum_iW_i(Z_i-X_i^{\mathsf T}t)^2$
\ENDFOR
\STATE \textbf{return} $\beta^{(k)}$
\end{algorithmic}
\end{algorithm}
```

IRLS needs only the link $g$ and the variance function, and each step is a weighted least squares fit, which any regression software can do.

::: {#exm-irls-logistic .example name="IRLS for a small logistic regression"}

Fit the logistic model $\operatorname{logit}\mu_i=\beta_1+\beta_2x_i$ to $x=-2,-1,0,1,2,3$ with responses $Y=0,0,1,0,1,1$. Here $\phi=1$, $V(\mu)=\mu(1-\mu)$ and $g'(\mu)=1/(\mu(1-\mu))$, so $W_i=\mu_i(1-\mu_i)$ and $Z_i=\eta_i+(Y_i-\mu_i)/(\mu_i(1-\mu_i))$. Starting from $\beta^{(0)}=(0,0)$, every $\mu_i=1/2$, $W_i=1/4$ and $Z_i=\pm2$, and the iterates are

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $\beta_1^{(k)}$ | $0$ | $-0.400$ | $-0.555$ | $-0.603$ | $-0.607$ |
| $\beta_2^{(k)}$ | $0$ | $0.800$ | $1.110$ | $1.206$ | $1.214$ |
| $\ell_n(\beta^{(k)})$ | $-4.159$ | $-2.607$ | $-2.485$ | $-2.478$ | $-2.478$ |

After four steps the estimate is stable to three decimals, as expected from Newton's quadratic convergence (the link is canonical, so IRLS is Newton's method here).

:::

::: {#fig-generalized-linear-models-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.90,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,3.30) node[lab, above] {$\mu$};
\draw (1.000,0) -- (1.000,-0.07) node[lab, tick, below] {-2};
\draw (3.000,0) -- (3.000,-0.07) node[lab, tick, below] {0};
\draw (5.000,0) -- (5.000,-0.07) node[lab, tick, below] {2};
\draw (0,0.000) -- (-0.07,0.000) node[lab, tick, left] {0};
\draw (0,3.000) -- (-0.07,3.000) node[lab, tick, left] {1};
\draw (0,1.500) -- (-0.07,1.500) node[lab, tick, left] {0.5};
\node[dot] at (1.000,0.000) {};
\node[dot] at (2.000,0.000) {};
\node[dot] at (3.000,3.000) {};
\node[dot] at (4.000,0.000) {};
\node[dot] at (5.000,3.000) {};
\node[dot] at (6.000,3.000) {};
\draw[faint] (0.000,0.172) -- (0.055,0.179) -- (0.111,0.187) -- (0.166,0.195) -- (0.222,0.203) -- (0.277,0.212) -- (0.333,0.221) -- (0.388,0.230) -- (0.444,0.239) -- (0.499,0.249) -- (0.555,0.260) -- (0.610,0.270) -- (0.666,0.282) -- (0.721,0.293) -- (0.776,0.305) -- (0.832,0.317) -- (0.887,0.330) -- (0.943,0.343) -- (0.998,0.357) -- (1.054,0.371) -- (1.109,0.386) -- (1.165,0.401) -- (1.220,0.417) -- (1.276,0.433) -- (1.331,0.450) -- (1.387,0.467) -- (1.442,0.485) -- (1.497,0.503) -- (1.553,0.522) -- (1.608,0.541) -- (1.664,0.561) -- (1.719,0.582) -- (1.775,0.603) -- (1.830,0.625) -- (1.886,0.647) -- (1.941,0.670) -- (1.997,0.693) -- (2.052,0.717) -- (2.108,0.741) -- (2.163,0.766) -- (2.218,0.792) -- (2.274,0.818) -- (2.329,0.845) -- (2.385,0.872) -- (2.440,0.900) -- (2.496,0.928) -- (2.551,0.957) -- (2.607,0.986) -- (2.662,1.015) -- (2.718,1.045) -- (2.773,1.076) -- (2.829,1.107) -- (2.884,1.138) -- (2.939,1.169) -- (2.995,1.201) -- (3.050,1.233) -- (3.106,1.265) -- (3.161,1.298) -- (3.217,1.331) -- (3.272,1.364) -- (3.328,1.397) -- (3.383,1.430) -- (3.439,1.463) -- (3.494,1.496) -- (3.550,1.530) -- (3.605,1.563) -- (3.661,1.596) -- (3.716,1.629) -- (3.771,1.662) -- (3.827,1.695) -- (3.882,1.728) -- (3.938,1.760) -- (3.993,1.792) -- (4.049,1.824) -- (4.104,1.856) -- (4.160,1.887) -- (4.215,1.918) -- (4.271,1.948) -- (4.326,1.978) -- (4.382,2.008) -- (4.437,2.037) -- (4.492,2.066) -- (4.548,2.094) -- (4.603,2.122) -- (4.659,2.149) -- (4.714,2.176) -- (4.770,2.202) -- (4.825,2.228) -- (4.881,2.253) -- (4.936,2.278) -- (4.992,2.302) -- (5.047,2.325) -- (5.103,2.348) -- (5.158,2.371) -- (5.213,2.393) -- (5.269,2.414) -- (5.324,2.434) -- (5.380,2.454) -- (5.435,2.474) -- (5.491,2.493) -- (5.546,2.511) -- (5.602,2.529) -- (5.657,2.547) -- (5.713,2.563) -- (5.768,2.580) -- (5.824,2.595) -- (5.879,2.611) -- (5.934,2.626) -- (5.990,2.640) -- (6.045,2.654) -- (6.101,2.667) -- (6.156,2.680) -- (6.212,2.692) -- (6.267,2.704) -- (6.323,2.716) -- (6.378,2.727) -- (6.434,2.738) -- (6.489,2.748) -- (6.545,2.759) -- (6.600,2.768);
\draw[faint] (0.3,2.85) -- (0.9,2.85) node[lab, right] {$k=1$};
\draw[emph, primaryMid] (0.000,0.060) -- (0.055,0.064) -- (0.111,0.068) -- (0.166,0.072) -- (0.222,0.077) -- (0.277,0.082) -- (0.333,0.087) -- (0.388,0.092) -- (0.444,0.098) -- (0.499,0.104) -- (0.555,0.110) -- (0.610,0.117) -- (0.666,0.124) -- (0.721,0.131) -- (0.776,0.139) -- (0.832,0.148) -- (0.887,0.157) -- (0.943,0.166) -- (0.998,0.176) -- (1.054,0.186) -- (1.109,0.197) -- (1.165,0.209) -- (1.220,0.221) -- (1.276,0.234) -- (1.331,0.248) -- (1.387,0.262) -- (1.442,0.277) -- (1.497,0.293) -- (1.553,0.310) -- (1.608,0.328) -- (1.664,0.346) -- (1.719,0.365) -- (1.775,0.385) -- (1.830,0.407) -- (1.886,0.429) -- (1.941,0.452) -- (1.997,0.476) -- (2.052,0.501) -- (2.108,0.527) -- (2.163,0.555) -- (2.218,0.583) -- (2.274,0.612) -- (2.329,0.643) -- (2.385,0.675) -- (2.440,0.707) -- (2.496,0.741) -- (2.551,0.776) -- (2.607,0.812) -- (2.662,0.849) -- (2.718,0.887) -- (2.773,0.926) -- (2.829,0.966) -- (2.884,1.006) -- (2.939,1.048) -- (2.995,1.090) -- (3.050,1.133) -- (3.106,1.177) -- (3.161,1.221) -- (3.217,1.266) -- (3.272,1.311) -- (3.328,1.357) -- (3.383,1.403) -- (3.439,1.449) -- (3.494,1.495) -- (3.550,1.541) -- (3.605,1.587) -- (3.661,1.633) -- (3.716,1.679) -- (3.771,1.724) -- (3.827,1.769) -- (3.882,1.814) -- (3.938,1.857) -- (3.993,1.901) -- (4.049,1.943) -- (4.104,1.985) -- (4.160,2.026) -- (4.215,2.066) -- (4.271,2.105) -- (4.326,2.143) -- (4.382,2.180) -- (4.437,2.216) -- (4.492,2.252) -- (4.548,2.286) -- (4.603,2.319) -- (4.659,2.350) -- (4.714,2.381) -- (4.770,2.411) -- (4.825,2.439) -- (4.881,2.467) -- (4.936,2.493) -- (4.992,2.519) -- (5.047,2.543) -- (5.103,2.567) -- (5.158,2.589) -- (5.213,2.610) -- (5.269,2.631) -- (5.324,2.650) -- (5.380,2.669) -- (5.435,2.686) -- (5.491,2.703) -- (5.546,2.719) -- (5.602,2.735) -- (5.657,2.749) -- (5.713,2.763) -- (5.768,2.776) -- (5.824,2.788) -- (5.879,2.800) -- (5.934,2.811) -- (5.990,2.822) -- (6.045,2.832) -- (6.101,2.842) -- (6.156,2.850) -- (6.212,2.859) -- (6.267,2.867) -- (6.323,2.875) -- (6.378,2.882) -- (6.434,2.889) -- (6.489,2.895) -- (6.545,2.901) -- (6.600,2.907);
\draw[emph, primaryMid] (0.3,2.34) -- (0.9,2.34) node[lab, right] {$k=2$};
\draw[emph, accent] (0.000,0.042) -- (0.055,0.045) -- (0.111,0.048) -- (0.166,0.052) -- (0.222,0.055) -- (0.277,0.059) -- (0.333,0.063) -- (0.388,0.067) -- (0.444,0.072) -- (0.499,0.077) -- (0.555,0.082) -- (0.610,0.087) -- (0.666,0.093) -- (0.721,0.099) -- (0.776,0.106) -- (0.832,0.113) -- (0.887,0.121) -- (0.943,0.129) -- (0.998,0.137) -- (1.054,0.146) -- (1.109,0.156) -- (1.165,0.166) -- (1.220,0.177) -- (1.276,0.189) -- (1.331,0.201) -- (1.387,0.214) -- (1.442,0.228) -- (1.497,0.243) -- (1.553,0.258) -- (1.608,0.274) -- (1.664,0.292) -- (1.719,0.310) -- (1.775,0.329) -- (1.830,0.349) -- (1.886,0.370) -- (1.941,0.393) -- (1.997,0.416) -- (2.052,0.441) -- (2.108,0.467) -- (2.163,0.494) -- (2.218,0.523) -- (2.274,0.552) -- (2.329,0.583) -- (2.385,0.616) -- (2.440,0.649) -- (2.496,0.684) -- (2.551,0.721) -- (2.607,0.758) -- (2.662,0.797) -- (2.718,0.837) -- (2.773,0.878) -- (2.829,0.920) -- (2.884,0.964) -- (2.939,1.008) -- (2.995,1.054) -- (3.050,1.101) -- (3.106,1.148) -- (3.161,1.196) -- (3.217,1.245) -- (3.272,1.294) -- (3.328,1.344) -- (3.383,1.394) -- (3.439,1.444) -- (3.494,1.495) -- (3.550,1.545) -- (3.605,1.596) -- (3.661,1.646) -- (3.716,1.696) -- (3.771,1.745) -- (3.827,1.794) -- (3.882,1.842) -- (3.938,1.889) -- (3.993,1.936) -- (4.049,1.982) -- (4.104,2.027) -- (4.160,2.070) -- (4.215,2.113) -- (4.271,2.155) -- (4.326,2.195) -- (4.382,2.234) -- (4.437,2.272) -- (4.492,2.308) -- (4.548,2.343) -- (4.603,2.377) -- (4.659,2.410) -- (4.714,2.441) -- (4.770,2.471) -- (4.825,2.500) -- (4.881,2.527) -- (4.936,2.553) -- (4.992,2.578) -- (5.047,2.602) -- (5.103,2.625) -- (5.158,2.646) -- (5.213,2.667) -- (5.269,2.686) -- (5.324,2.705) -- (5.380,2.722) -- (5.435,2.739) -- (5.491,2.754) -- (5.546,2.769) -- (5.602,2.783) -- (5.657,2.796) -- (5.713,2.809) -- (5.768,2.820) -- (5.824,2.831) -- (5.879,2.842) -- (5.934,2.852) -- (5.990,2.861) -- (6.045,2.869) -- (6.101,2.878) -- (6.156,2.885) -- (6.212,2.892) -- (6.267,2.899) -- (6.323,2.906) -- (6.378,2.912) -- (6.434,2.917) -- (6.489,2.922) -- (6.545,2.927) -- (6.600,2.932);
\draw[emph, accent] (0.3,1.83) -- (0.9,1.83) node[lab, right] {$k=4$};
\end{tikzpicture}
\end{center}
```

The six observations and the fitted response curves $\mu(x)=1/(1+e^{-(\beta_1+\beta_2x)})$ after IRLS steps $k=1$, $2$ and $4$ (from the flat start $\mu\equiv1/2$). The curve steepens towards the maximum likelihood fit $\hat\beta\approx(-0.607,1.214)$, which it has essentially reached after two steps.

:::

