<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-14-q6" status="draft"}
The error covariance is $k\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$: it grows linearly without bound along the direction $(1,-1)$.

1. Change coordinates to $S_k=X_{1,k}+X_{2,k}$ and $D_k=X_{1,k}-X_{2,k}$ (the eigenvectors of the matrix, eigenvalues $3$ and $1$). The noise vector $(1,-1)$ has sum $0$ and difference $2$, so
$$S_{k+1}=3S_k,\qquad D_{k+1}=D_k+2w_k.$$
2. $S_k=3^kS_0$ is deterministic and $Y_k=S_k$ is observed exactly, but the observations carry no information about the $w$'s. So $E[D_k\mid Y_{0:k}]=D_0$, while $D_k-D_0=2\sum_{j<k}w_j$ has variance $4k$.
3. $X_k=\frac12(S_k+D_k,\,S_k-D_k)$, so $\hat X_{k|k}=\frac12(S_k+D_0,\,S_k-D_0)$ and the error is $\frac{D_k-D_0}{2}(1,-1)^T$, with covariance $\frac{4k}{4}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$.

The component along $(1,-1)$ is unobservable (it never reaches $Y$), and the noise drives exactly that component, so no filter can keep the error bounded.
:::

::: {.solution for="prob-eecs126d-13-q3" status="draft"}
(a) Unrolling, $X_n=a^nX_0+\sum_{k=0}^{n-1}a^{n-1-k}V_k$, a linear combination of independent Gaussians, so
$$X_n\sim N\Bigl(0,\ a^{2n}u^2+\sigma^2\frac{1-a^{2n}}{1-a^2}\Bigr).$$

(b) $X_{n+m}=a^mX_n+\sum_{k=n}^{n+m-1}a^{n+m-1-k}V_k$, and the $V_k$ with $k\ge n$ are independent of $X_n$ with mean $0$. So $E[X_{n+m}\mid X_n]=a^mX_n$.

(c) The variance is constant in $n$ iff $a^{2n}\bigl(u^2-\frac{\sigma^2}{1-a^2}\bigr)$ is constant, i.e. $u^2=\frac{\sigma^2}{1-a^2}$, $u=\frac{\sigma}{\sqrt{1-a^2}}$. This is the stationary distribution of the chain, and the variance the Kalman filter's predictions approach when there are no observations.
:::

::: {.solution for="prob-kalman-filter-code" status="draft"}
```{.python}
import numpy as np


def kalman_filter(A, C, SV, SW, x0, S0, ys):
    """Kalman filter for X_n = A X_{n-1} + V_n, Y_n = C X_n + W_n (n >= 1), where
    X_0 ~ N(x0, S0), V_n ~ N(0, SV), W_n ~ N(0, SW), all independent.
    ys = [y_1, ..., y_N]. Return two lists of length N: the estimates
    E[X_n | Y_1..Y_n] and their error covariances."""
    A, C, SV, SW, S = (np.atleast_2d(np.asarray(M, dtype=float)) for M in (A, C, SV, SW, S0))
    x = np.atleast_1d(np.asarray(x0, dtype=float))
    xs, Ss = [], []
    for y in ys:
        x, S = A @ x, A @ S @ A.T + SV                     # predict
        K = S @ C.T @ np.linalg.inv(C @ S @ C.T + SW)      # gain
        x = x + K @ (np.atleast_1d(y) - C @ x)             # update
        S = (np.eye(len(x)) - K @ C) @ S
        xs.append(x)
        Ss.append(S)
    return xs, Ss
```

1. *Predict:* $\hat X_{n\mid n-1}=A\hat X_{n-1\mid n-1}$ and $\Sigma_{n\mid n-1}=A\Sigma_{n-1\mid n-1}A^{\mathsf T}+\Sigma_V$, starting from $\hat X_{0\mid0}=\hat x_0$ and $\Sigma_{0\mid0}=\Sigma_0$.
2. *Gain:* $K_n=\Sigma_{n\mid n-1}C^{\mathsf T}(C\Sigma_{n\mid n-1}C^{\mathsf T}+\Sigma_W)^{-1}$.
3. *Update:* $\hat X_{n\mid n}=\hat X_{n\mid n-1}+K_n(y_n-C\hat X_{n\mid n-1})$ and $\Sigma_{n\mid n}=(I-K_nC)\Sigma_{n\mid n-1}$ (the vector form of @thm-kalman-filter).
4. With a nonzero prior mean the same recursion holds, because the means of all variables are known and the innovations remain uncorrelated (@thm-orthogonal-update).
:::
