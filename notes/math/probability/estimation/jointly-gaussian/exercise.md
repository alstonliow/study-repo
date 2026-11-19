::: {.problem #prob-eecs126hw-5-q6 origin="external" source="eecs126hw-5-q6"}
**Noisy Guessing.** Let $X$, $Y$, and $Z$ be i.i.d. with the standard Gaussian distribution. Find $E[X\mid X+Y,X+Z,Y-Z]$.

Hint: Argue that the observation $Y-Z$ is redundant.
:::

::: {.problem #prob-eecs126hw-12-q4 origin="external" source="eecs126hw-12-q4"}
**Basic Properties of Jointly Gaussian Random Variables.** Let $(X_1,\dots,X_n)$ be a collection of jointly Gaussian random variables. Their joint density is given by (for $x\in\mathbb R^n$)
$$f(x)=\frac{1}{\sqrt{(2\pi)^n\det(C)}}\exp\Bigl(-\frac12(x-\mu)^TC^{-1}(x-\mu)\Bigr),$$
where $\mu$ is the mean vector and $C$ is the covariance matrix.

(a) Show that $X_1,\dots,X_n$ are independent if and only if they are pairwise uncorrelated.

(b) Show that any linear combination of these random variables will also be a Gaussian random variable.

*Note (these notes):* The extracted text of the density lost its square root and the factor $\tfrac12$; they are restored here as in the standard Gaussian density. Owner to check against the handout.
:::

::: {.problem #prob-eecs126hw-12-q5 origin="external" source="eecs126hw-12-q5"}
**Independent Gaussians.** Let $\mathbf X=(X,Y)$ be a jointly Gaussian random vector with mean vector $[0,0]$ and covariance matrix
$$\begin{pmatrix}2&1\\1&2\end{pmatrix}$$
Find a $2\times2$ matrix $U$ such that $U\mathbf X=(X',Y')$ where $X'$ and $Y'$ are independent.
:::

::: {.problem #prob-eecs126hw-13-q3 origin="external" source="eecs126hw-13-q3"}
**Jointly Gaussian Decomposition.** Let $U$ and $V$ be jointly Gaussian random variables with means $\mu_U=1$, $\mu_V=4$, respectively, with variances $\sigma_U^2=2.5$, $\sigma_V^2=2$, respectively, and with covariance $\rho=1$. Can we write $U$ as $U=aV+Z$, where $a$ is a scalar and $Z$ is independent of $V$? If you think we can, find the value of $a$ and the distribution of $Z$; otherwise please explain the reason.
:::

::: {.problem #prob-eecs126hw-14-q4 origin="external" source="eecs126hw-14-q4"}
**Gaussian Random Vector MMSE.** Let
$$\begin{pmatrix}X\\Y\end{pmatrix}\sim N\Bigl(\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}2&1\\1&2\end{pmatrix}\Bigr)$$
be a Gaussian random vector.

Let
$$W=\begin{cases}1,&\text{if }Y>0\\0,&\text{if }Y=0\\-1,&\text{if }Y<0\end{cases}$$
be the sign of $Y$. Find $E[WX\mid Y]$. Is the LLSE the same as the MMSE?
:::

::: {.problem #prob-eecs126hw-14-q5 origin="external" source="eecs126hw-14-q5"}
**Gaussian Sine.** Let $X,Y,Z$ be jointly Gaussian random variables with covariance matrix
$$\begin{pmatrix}4&1&0\\1&4&1\\0&1&4\end{pmatrix}$$
and mean vector $[0,2,0]$. Compute $E[(\sin X)Y(\sin Z)]$. Hint: Condition on $(X,Z)$.
:::
