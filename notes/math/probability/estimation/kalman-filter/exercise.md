::: {.problem #prob-eecs126hw-14-q6 origin="external" source="eecs126hw-14-q6"}
**Error of the Kalman Filter for a Linear Stochastic System.** The linear stochastic system
$$\begin{pmatrix}X_{1,k+1}\\X_{2,k+1}\end{pmatrix}=\begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}X_{1,k}\\X_{2,k}\end{pmatrix}+\begin{pmatrix}1\\-1\end{pmatrix}w_k,\qquad k\ge0,$$
starts from an arbitrary (known) initial condition $\begin{pmatrix}x_{1,0}\\x_{2,0}\end{pmatrix}$ and the system noise variables $(w_k,\ k\ge0)$ are i.i.d. normal with mean $0$ and variance $1$.

The state variables are not directly observable. However, we can observe
$$Y_k=X_{1,k}+X_{2,k},\qquad k\ge0.$$
Let $\hat X_{k|k}$ denote the minimum mean square error estimator of $X_k=\begin{pmatrix}X_{1,k}\\X_{2,k}\end{pmatrix}$ given $(Y_0,\dots,Y_k)$.

Determine the asymptotic behavior of the covariance matrix of the estimation error.

Note: This problem needs thought. Note that there is no observation noise, so the assumption used in the derivation of the Kalman filter equations, that the covariance matrix of the observation noise is positive definite, is no longer valid.
:::

::: {.problem #prob-eecs126d-13-q3 origin="external" source="eecs126d-13-q3"}
**Stochastic Linear System MMSE.** Let $(V_n,\ n\in\mathbb N)$ be i.i.d. $N(0,\sigma^2)$ and independent of $X_0=N(0,u^2)$. Let $|a|<1$. Define
$$X_{n+1}=aX_n+V_n,\quad n\in\mathbb N.$$

(a) What is the distribution of $X_n$, where $n$ is a positive integer?

(b) Find $E[X_{n+m}\mid X_n]$ for $m,n\in\mathbb N$, $m\ge1$.

(c) Find $u$ so that the distribution of $X_n$ is the same for all $n\in\mathbb N$.
:::
