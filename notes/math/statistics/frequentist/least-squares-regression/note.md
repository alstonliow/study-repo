---
title: "Least Squares Regression"
sources: [mit1805-26]
requires: [math/statistics/frequentist/confidence-intervals, math/calculus/multivariable/differentiation/least-squares-fitting]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Class 26, in our own wording; proofs written out in steps. The fitting itself is in @thm-least-squares-line-calculus and @thm-least-squares-normal-equations; this note adds the statistical model. -->

Fitting a line by least squares is a calculation (@thm-least-squares-line-calculus, @thm-least-squares-normal-equations). Statistics adds a model of where the scatter comes from, which explains why least squares is a good choice and how good the fit is.

::: {#def-simple-linear-regression .definition name="Simple linear regression model"}

Data $(x_1,y_1),\dots,(x_n,y_n)$ follow the *simple linear regression model* if
$$y_i=a+bx_i+E_i\qquad(i=1,\dots,n),$$
where the $x_i$ are fixed numbers, $a,b$ are unknown parameters and the errors $E_i$ are independent with mean $0$ and the same variance $\sigma^2$ (*homoscedastic*). For the fitted line $\hat y=\hat a+\hat bx$, the *residuals* are $e_i=y_i-\hat a-\hat bx_i$.

:::

::: {#prp-least-squares-slope .proposition name="Slope and intercept from sample moments" related="thm-least-squares-line-calculus"}

Let the $x_i$ not all be equal and put
$$s_{xx}=\sum_{i=1}^n(x_i-\bar x)^2,\qquad s_{xy}=\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y).$$
The least-squares line has slope and intercept
$$\hat b=\frac{s_{xy}}{s_{xx}},\qquad\hat a=\bar y-\hat b\,\bar x,$$
so it passes through $(\bar x,\bar y)$.

:::

::: {.proof}

1. The second normal equation of @thm-least-squares-line-calculus, divided by $n$, says $\hat b\bar x+\hat a=\bar y$, which is the formula for $\hat a$.

2. Substitute $\hat a=\bar y-\hat b\bar x$ into the first normal equation: $\hat b\sum x_i^2+(\bar y-\hat b\bar x)n\bar x=\sum x_iy_i$, that is $\hat b\bigl(\sum x_i^2-n\bar x^2\bigr)=\sum x_iy_i-n\bar x\bar y$.

3. Expanding the squares shows $\sum x_i^2-n\bar x^2=s_{xx}$ and $\sum x_iy_i-n\bar x\bar y=s_{xy}$. Since $s_{xx}>0$, $\hat b=s_{xy}/s_{xx}$.

:::

::: {#prp-least-squares-is-mle .proposition name="Least squares is maximum likelihood" related="def-maximum-likelihood"}

If in @def-simple-linear-regression the errors are $N(0,\sigma^2)$, the maximum likelihood estimates of $a$ and $b$ are the least-squares estimates, whatever $\sigma$ is.

:::

::: {.proof}

1. The $y_i$ are independent with $y_i\sim N(a+bx_i,\sigma^2)$, so the log-likelihood is
$$-\frac n2\ln(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_{i=1}^n(y_i-a-bx_i)^2 .$$

2. For fixed $\sigma$, only the last sum depends on $(a,b)$, with a negative factor. Maximising the log-likelihood is therefore the same as minimising the sum of squared residuals.

:::

::: {#exm-regression-five-points .example name="Five points"}

For the points $(1,2),(2,3),(3,5),(4,4),(5,6)$: $\bar x=3$, $\bar y=4$, $s_{xx}=10$, $s_{xy}=9$, so $\hat b=0.9$ and $\hat a=4-2.7=1.3$. The residuals are $-0.2,-0.1,1.0,-0.9,0.2$; they sum to $0$, as they always do when the model has an intercept.

:::

::: {#def-coefficient-of-determination .definition name="Coefficient of determination"}

With the total sum of squares $\mathit{TSS}=\sum_i(y_i-\bar y)^2$ and the residual sum of squares $\mathit{RSS}=\sum_ie_i^2$, the *coefficient of determination* is
$$R^2=1-\frac{\mathit{RSS}}{\mathit{TSS}},$$
the fraction of the variation of $y$ that the fitted model accounts for.

:::

::: {#prp-r-squared-correlation .proposition name="$R^2$ is the squared correlation" related="def-correlation"}

For the least-squares line, $R^2=r^2$, where $r=s_{xy}/\sqrt{s_{xx}s_{yy}}$ is the sample correlation and $s_{yy}=\mathit{TSS}$.

:::

::: {.proof}

1. By @prp-least-squares-slope, $e_i=(y_i-\bar y)-\hat b(x_i-\bar x)$.

2. Expand: $\mathit{RSS}=s_{yy}-2\hat bs_{xy}+\hat b^2s_{xx}=s_{yy}-2\frac{s_{xy}^2}{s_{xx}}+\frac{s_{xy}^2}{s_{xx}}=s_{yy}-\frac{s_{xy}^2}{s_{xx}}$.

3. Divide by $\mathit{TSS}=s_{yy}$: $R^2=1-\mathit{RSS}/s_{yy}=\dfrac{s_{xy}^2}{s_{xx}s_{yy}}=r^2$.

:::

In @exm-regression-five-points, $s_{yy}=10$ and $\mathit{RSS}=1.9$, so $R^2=0.81$ and $r=0.9$.

::: {#rmk-polynomial-multiple-regression .remark name="Polynomial and multiple regression" related="thm-least-squares-normal-equations"}

"Linear" refers to the parameters, not to $x$. A model $y_i=\beta_0+\beta_1x_i+\beta_2x_i^2+E_i$, or one with several explanatory variables $y_i=\beta_0+\beta_1u_i+\beta_2v_i+E_i$, is fitted the same way: put the values of the explanatory functions in the columns of a matrix $A$ and solve the normal equations $A^{\mathsf T}A\hat\beta=A^{\mathsf T}y$. With normal errors this is again maximum likelihood.

:::

::: {#rmk-overfitting .remark name="Overfitting"}

A polynomial of degree $n-1$ passes through all $n$ points, so $R^2=1$, yet it follows the noise and predicts new data badly. A good model explains the data with few parameters; plotting the residuals against $x$ shows whether a pattern (curvature, growing spread) remains that the model has missed.

:::

::: {#rmk-regression-to-the-mean .remark name="Regression to the mean"}

If $x$ and $y$ are standardized to mean $0$ and standard deviation $1$, the least-squares line is $\hat y=rx$ with $|r|\le1$. So an individual who is extreme in $x$ is predicted to be less extreme in $y$: children of very tall parents tend to be tall, but less so than their parents. This is a property of imperfect correlation, not of any causal effect.

:::
