---
title: "Multiple Linear Regression"
sources: [mit18650-7, mit18650-10]
requires: [math/statistics/frequentist/least-squares-regression]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 7 (theoretical linear regression of Y on X; least squares in matrix form; deterministic design with Gaussian noise: distribution of the estimator, its risk, the unbiased variance estimate and Cochran's theorem) and Chapter 10 (weighted least squares), in our own wording. The proofs and the numerical example are our own. -->

Simple regression (@sec-math-statistics-frequentist-least-squares-regression) fits a line in one explanatory variable. Here the response depends linearly on $p$ variables, and under Gaussian noise the estimator has an exact distribution, which gives exact tests (@sec-math-statistics-frequentist-regression-inference).

The best approximation of $Y$ in mean square by a linear function $a+bX$ of a random variable $X$ is the linear least squares estimate $L[Y\mid X]$ (@thm-llse): $b=\operatorname{Cov}(X,Y)/\mathrm{Var}(X)$ and $a=E[Y]-bE[X]$. It is called the *theoretical linear regression* of $Y$ on $X$. The residual $\varepsilon=Y-a-bX$ then satisfies $E[\varepsilon]=0$ and $\operatorname{Cov}(X,\varepsilon)=0$, and these two properties characterise it.

::: {#prp-regression-characterisation .proposition name="Uncorrelated noise characterises the regression line" related="thm-llse"}

Let $\mathrm{Var}(X)>0$. If $Y=a+bX+\varepsilon$ with $E[\varepsilon]=0$ and $\operatorname{Cov}(X,\varepsilon)=0$, then $a+bX$ is the theoretical linear regression of $Y$ on $X$. This holds in particular if $\varepsilon$ is independent of $X$, or if $E[\varepsilon\mid X]=0$.

:::

::: {.proof}

1. $\operatorname{Cov}(X,Y)=b\,\mathrm{Var}(X)+\operatorname{Cov}(X,\varepsilon)=b\,\mathrm{Var}(X)$, so $b=\operatorname{Cov}(X,Y)/\mathrm{Var}(X)$.

2. Taking expectations, $E[Y]=a+bE[X]$, so $a=E[Y]-bE[X]$. These are the coefficients of @thm-llse.

3. Independence with $E[\varepsilon]=0$ gives $\operatorname{Cov}(X,\varepsilon)=0$. If $E[\varepsilon\mid X]=0$, then $E[\varepsilon]=0$ and $E[X\varepsilon]=E[X\,E[\varepsilon\mid X]]=0$ by iterated expectations (@thm-iterated-expectations).

:::

Replacing expectations by sample averages gives the least squares line of @prp-least-squares-slope.

::: {#def-linear-model .definition name="Linear model, design matrix, least squares estimator"}

Observations $(X_i,Y_i)$, $i=1,\dots,n$, with $X_i\in\mathbb{R}^p$ (first coordinate $1$ when there is an intercept) and $Y_i\in\mathbb{R}$, follow a *linear model* if
$$Y_i=X_i^{\mathsf T}\beta+\varepsilon_i,\qquad i=1,\dots,n,$$
for an unknown $\beta\in\mathbb{R}^p$ and noise terms $\varepsilon_i$. In matrix form $\mathbf Y=\mathbb X\beta+\boldsymbol\varepsilon$, where $\mathbb X\in\mathbb{R}^{n\times p}$, the *design matrix*, has rows $X_i^{\mathsf T}$. The *least squares estimator* (LSE) is
$$\hat\beta=\operatorname*{argmin}_{t\in\mathbb{R}^p}\|\mathbf Y-\mathbb Xt\|_2^2 .$$

:::

If $\operatorname{rank}\mathbb X=p$, the normal equations (@thm-least-squares-normal-equations) give
$$\hat\beta=(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T}\mathbf Y,\qquad \hat{\mathbf Y}=\mathbb X\hat\beta=P\mathbf Y,\qquad P=\mathbb X(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T},$$
where $P$ is the orthogonal projection onto the column space of $\mathbb X$ (@thm-projection-onto-subspace). The fitted values are the projection of the responses; the *residuals* $\hat{\boldsymbol\varepsilon}=\mathbf Y-\hat{\mathbf Y}=(I_n-P)\mathbf Y$ are orthogonal to every column of $\mathbb X$.

::: {#thm-gaussian-linear-model .theorem name="The Gaussian linear model"}

Let $\mathbb X$ be deterministic with $\operatorname{rank}\mathbb X=p<n$, and let $\boldsymbol\varepsilon\sim N_n(0,\sigma^2I_n)$ (independent, *homoscedastic* Gaussian noise). Then:

1. the LSE is the maximum likelihood estimator of $\beta$;
2. $\hat\beta\sim N_p\bigl(\beta,\ \sigma^2(\mathbb X^{\mathsf T}\mathbb X)^{-1}\bigr)$; in particular $\hat\beta$ is unbiased, with quadratic risk $E\|\hat\beta-\beta\|^2=\sigma^2\operatorname{tr}\bigl((\mathbb X^{\mathsf T}\mathbb X)^{-1}\bigr)$;
3. $E\|\mathbf Y-\mathbb X\hat\beta\|^2=\sigma^2(n-p)$, so
   $$\hat\sigma^2=\frac{\|\mathbf Y-\mathbb X\hat\beta\|^2}{n-p}$$
   is an unbiased estimator of $\sigma^2$;
4. $(n-p)\hat\sigma^2/\sigma^2\sim\chi^2_{n-p}$, and $\hat\sigma^2$ is independent of $\hat\beta$.

:::

::: {.proof}

1. The density of $\mathbf Y$ is $(2\pi\sigma^2)^{-n/2}\exp\bigl(-\|\mathbf Y-\mathbb X\beta\|^2/(2\sigma^2)\bigr)$. For every $\sigma^2$ it is maximised over $\beta$ by minimising $\|\mathbf Y-\mathbb X\beta\|^2$, which is the LSE.

2. $\hat\beta=\beta+A\boldsymbol\varepsilon$ with $A=(\mathbb X^{\mathsf T}\mathbb X)^{-1}\mathbb X^{\mathsf T}$ is an affine function of the Gaussian vector $\boldsymbol\varepsilon$, hence Gaussian (@thm-jointly-gaussian-properties), with mean $\beta$ and covariance $A(\sigma^2I_n)A^{\mathsf T}=\sigma^2(\mathbb X^{\mathsf T}\mathbb X)^{-1}$.

3. The quadratic risk is the sum of the variances of the coordinates of $\hat\beta$, the trace of its covariance matrix.

4. Since $(I_n-P)\mathbb X=0$, the residual vector is $\hat{\boldsymbol\varepsilon}=(I_n-P)\boldsymbol\varepsilon$. Choose an orthonormal basis $u_1,\dots,u_n$ of $\mathbb{R}^n$ whose first $p$ vectors span the column space of $\mathbb X$. Then $Z_j=u_j^{\mathsf T}\boldsymbol\varepsilon/\sigma$ are independent $N(0,1)$ (an orthogonal change of coordinates preserves $N_n(0,I_n)$), and
   $$\|\hat{\boldsymbol\varepsilon}\|^2=\Bigl\|\sum_{j>p}(u_j^{\mathsf T}\boldsymbol\varepsilon)\,u_j\Bigr\|^2=\sigma^2\sum_{j=p+1}^nZ_j^2 .$$
   So $\|\hat{\boldsymbol\varepsilon}\|^2/\sigma^2\sim\chi^2_{n-p}$, whose mean is $n-p$. This proves part 3 and the first half of part 4.

5. $\hat\beta-\beta=A\boldsymbol\varepsilon=AP\boldsymbol\varepsilon$ (as $AP=A$) is a function of $Z_1,\dots,Z_p$ only, while $\hat\sigma^2$ is a function of $Z_{p+1},\dots,Z_n$. These groups are independent, so $\hat\beta$ and $\hat\sigma^2$ are independent.

:::

Part 4 is an instance of *Cochran's theorem*: the squared lengths of the projections of a standard Gaussian vector onto orthogonal subspaces are independent chi-square variables, with degrees of freedom the dimensions. The case $p=1$, $\mathbb X=\mathbf 1$ is @thm-normal-sample-theory.

::: {#exm-linear-model-six-points .example name="Six points"}

Fit $Y=\beta_1+\beta_2x$ to $x=1,\dots,6$ and $Y=1.2,\ 1.9,\ 3.4,\ 3.1,\ 4.6,\ 4.4$. Here
$$\mathbb X^{\mathsf T}\mathbb X=\begin{pmatrix}6&21\\21&91\end{pmatrix},\qquad (\mathbb X^{\mathsf T}\mathbb X)^{-1}=\frac1{105}\begin{pmatrix}91&-21\\-21&6\end{pmatrix},\qquad \mathbb X^{\mathsf T}\mathbf Y=\begin{pmatrix}18.6\\77.0\end{pmatrix},$$
so $\hat\beta=(0.72,\ 0.68)$. The residuals are $-0.20,-0.18,0.64,-0.34,0.48,-0.40$ (they sum to $0$ and are orthogonal to $x$), with $\|\hat{\boldsymbol\varepsilon}\|^2=0.988$ and $\hat\sigma^2=0.988/4=0.247$. The estimated covariance of $\hat\beta$ is $\hat\sigma^2(\mathbb X^{\mathsf T}\mathbb X)^{-1}$, giving standard errors $0.463$ for the intercept and $0.119$ for the slope.

:::

::: {#def-generalized-least-squares .definition name="Weighted and generalised least squares"}

If the noise is Gaussian with a known invertible covariance matrix, $\boldsymbol\varepsilon\sim N_n(0,\Sigma)$, the model is *heteroscedastic* when $\Sigma$ is not a multiple of $I_n$. The *generalised least squares* estimator minimises
$$(\mathbf Y-\mathbb Xt)^{\mathsf T}\Sigma^{-1}(\mathbf Y-\mathbb Xt)$$
over $t\in\mathbb{R}^p$. When $\Sigma=\operatorname{diag}(\sigma_1^2,\dots,\sigma_n^2)$ this is *weighted least squares*, $\sum_iw_i(Y_i-X_i^{\mathsf T}t)^2$ with weights $w_i=1/\sigma_i^2$: precise observations count more.

:::

::: {#rmk-random-design .remark name="Random designs and what regression does not show"}

When the $X_i$ are random, the results above hold *conditionally* on $X_1,\dots,X_n$ provided $\boldsymbol\varepsilon\sim N_n(0,\sigma^2I_n)$ given the $X_i$; a statement whose conditional law does not depend on the $X_i$ (as for $(n-p)\hat\sigma^2/\sigma^2$) holds unconditionally too. Gaussian noise can be checked by a goodness-of-fit test or a normal QQ plot (@def-qq-plot) of the residuals. A fitted coefficient measures association: regression exhibits correlation, not causation.

:::
