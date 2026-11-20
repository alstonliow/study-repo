<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-5-q6" status="draft"}
The answer is $\frac{(X+Y)+(X+Z)}{3}$.

1. $Y-Z=(X+Y)-(X+Z)$ is a function of the other two observations, so conditioning on all three is the same as conditioning on $U=X+Y$ and $V=X+Z$.
2. $(X,U,V)$ is jointly Gaussian, so $E[X\mid U,V]=L[X\mid U,V]$ (@thm-jointly-gaussian-conditional).
3. $\Sigma_{(U,V)}=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ and $\operatorname{Cov}(X,(U,V))=(1,1)$, so the coefficients are $(1,1)\Sigma^{-1}=(1,1)\cdot\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}=(\tfrac13,\tfrac13)$ (@thm-llse).
:::

::: {.solution for="prob-eecs126hw-12-q4" status="draft"}
(a) Independent variables are uncorrelated (@thm-expectation-of-product). Conversely, if they are pairwise uncorrelated, $C=\operatorname{diag}(\sigma_1^2,\dots,\sigma_n^2)$, so $\det C=\prod_i\sigma_i^2$ and $(x-\mu)^TC^{-1}(x-\mu)=\sum_i(x_i-\mu_i)^2/\sigma_i^2$. The density factorises,
$$f(x)=\prod_{i=1}^{n}\frac{1}{\sqrt{2\pi\sigma_i^2}}e^{-(x_i-\mu_i)^2/(2\sigma_i^2)},$$
into the marginal normal densities, so the $X_i$ are independent.

(b) $C$ is symmetric positive definite, so $C=AA^T$ with $A=C^{1/2}$ invertible, and by change of variables (@thm-change-of-variables-density) $Z=A^{-1}(X-\mu)$ has density $(2\pi)^{-n/2}e^{-\|z\|^2/2}$: its entries are independent $N(0,1)$. Then $a^TX=a^T\mu+(A^Ta)^TZ$ is a constant plus a combination of independent normals, which is normal (@cor-sum-of-normals).
:::

::: {.solution for="prob-eecs126hw-12-q5" status="draft"}
Take $U=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, so $X'=X+Y$ and $Y'=X-Y$.

1. $(X',Y')$ is jointly Gaussian with covariance $U\Sigma U^T$ (@thm-jointly-gaussian-properties).
2. $\operatorname{Cov}(X+Y,X-Y)=\operatorname{Var}X-\operatorname{Var}Y=0$, and $U\Sigma U^T=\operatorname{diag}(6,2)$.
3. Uncorrelated jointly Gaussian variables are independent. (The rows of $U$ are the eigenvectors $(1,1)$ and $(1,-1)$ of $\Sigma$; any $U$ whose rows are orthogonal eigenvectors works.)
:::

::: {.solution for="prob-eecs126hw-13-q3" status="draft"}
Yes, with $a=\frac12$ and $Z\sim N(-1,2)$.

1. Choose $a$ so that $Z=U-aV$ is uncorrelated with $V$: $\operatorname{Cov}(U-aV,V)=1-2a=0$, $a=\frac12$.
2. $(Z,V)$ is a linear function of $(U,V)$, hence jointly Gaussian, so uncorrelated means independent (@thm-jointly-gaussian-properties).
3. $E[Z]=1-\frac12\cdot4=-1$ and $\operatorname{Var}Z=2.5-2\cdot\frac12\cdot1+\frac14\cdot2=2$.
:::

::: {.solution for="prob-eecs126hw-14-q4" status="draft"}
1. $W$ is a function of $Y$, so $E[WX\mid Y]=W\,E[X\mid Y]$, and by @thm-jointly-gaussian-conditional $E[X\mid Y]=1+\frac12Y$. Hence
$$E[WX\mid Y]=\operatorname{sign}(Y)\Bigl(1+\frac Y2\Bigr)=\operatorname{sign}(Y)+\frac{|Y|}2.$$
2. This is not linear in $Y$ (it jumps by $2$ at $0$), so the LLSE differs. Explicitly, with $Y\sim N(0,2)$ and $E|Y|=\frac2{\sqrt\pi}$: $E[WX]=E[\operatorname{sign}Y]+\frac12E|Y|=\frac1{\sqrt\pi}$ and $\operatorname{Cov}(WX,Y)=E[|Y|]+\frac12E[|Y|Y]=\frac2{\sqrt\pi}$, so $L[WX\mid Y]=\frac{1+Y}{\sqrt\pi}$.
:::

::: {.solution for="prob-eecs126hw-14-q5" status="draft"}
The answer is $0$.

1. By @thm-jointly-gaussian-conditional, $E[Y\mid X,Z]=2+(1,1)\begin{pmatrix}4&0\\0&4\end{pmatrix}^{-1}\begin{pmatrix}X\\Z\end{pmatrix}=2+\frac{X+Z}4$.
2. By the tower property, $E[\sin X\,Y\sin Z]=E\bigl[\sin X\sin Z\,(2+\tfrac{X+Z}4)\bigr]$.
3. $X$ and $Z$ are uncorrelated and jointly Gaussian, hence independent, and each is symmetric about $0$, so $E[\sin X]=E[\sin Z]=0$. Every term factors with one of these: $E[\sin X]E[\sin Z]$, $E[X\sin X]E[\sin Z]$, $E[\sin X]E[Z\sin Z]$.
:::

::: {.solution for="prob-gaussian-fusion-code" status="draft"}
```{.python}
import numpy as np


def fuse(x1, S1, x2, S2):
    """X has prior N(x1, S1); we observe Y = X + W with W ~ N(0, S2) independent of X,
    and Y = x2. Return (mean, covariance) of X given Y = x2."""
    x1, S1, x2, S2 = (np.atleast_1d(np.asarray(a, dtype=float)) for a in (x1, S1, x2, S2))
    S1, S2 = np.atleast_2d(S1), np.atleast_2d(S2)
    K = np.linalg.solve(S1 + S2, S1).T          # K = S1 (S1 + S2)^{-1}; both are symmetric
    return x1 + K @ (x2 - x1), S1 - K @ S1
```

1. $(X,Y)$ is jointly Gaussian with $\mu_Y=\hat x_1$, $\Sigma_Y=\Sigma_1+\Sigma_2$ and $\Sigma_{XY}=\operatorname{Cov}(X,X+W)=\Sigma_1$.
2. By @thm-jointly-gaussian-conditional, with the gain $K=\Sigma_1(\Sigma_1+\Sigma_2)^{-1}$,
$$E[X\mid Y=\hat x_2]=\hat x_1+K(\hat x_2-\hat x_1),\qquad\operatorname{Cov}(X\mid Y)=\Sigma_1-K\Sigma_1.$$
3. `np.linalg.solve(S1 + S2, S1)` is $(\Sigma_1+\Sigma_2)^{-1}\Sigma_1$, whose transpose is $K$, since both matrices are symmetric; solving is more accurate than inverting.
:::
