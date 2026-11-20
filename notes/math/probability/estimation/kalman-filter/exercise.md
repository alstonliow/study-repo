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

::: {#prob-kalman-filter-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-kalman" packages="numpy"}
Write `kalman_filter(A, C, SV, SW, x0, S0, ys)` for the vector form of the system of @def-linear-system:
$$X_n=AX_{n-1}+V_n,\qquad Y_n=CX_n+W_n,\qquad n\ge1,$$
with $X_0\sim N(\hat x_0,\Sigma_0)$, $V_n\sim N(0,\Sigma_V)$ and $W_n\sim N(0,\Sigma_W)$, all independent. Given the observations `ys` $=[y_1,\dots,y_N]$, return two lists of length $N$: the estimates $\hat X_{n\mid n}=E[X_n\mid Y_1,\dots,Y_n]$ and their error covariances $\Sigma_{n\mid n}$. The tests compare the result with direct conditioning of the joint Gaussian vector $(X_N,Y_1,\dots,Y_N)$, for a position–velocity model with position measurements only.

```{.python .starter}
import numpy as np


def kalman_filter(A, C, SV, SW, x0, S0, ys):
    """Kalman filter for X_n = A X_{n-1} + V_n, Y_n = C X_n + W_n (n >= 1), where
    X_0 ~ N(x0, S0), V_n ~ N(0, SV), W_n ~ N(0, SW), all independent.
    ys = [y_1, ..., y_N]. Return two lists of length N: the estimates
    E[X_n | Y_1..Y_n] and their error covariances."""
    ...
```

```{.python .tests}
import numpy as np


def test_scalar_steps():
    # a = c = 1, sigma_V^2 = 1, sigma_W^2 = 1, X_0 ~ N(0, 1)
    xs, Ss = kalman_filter([[1]], [[1]], [[1]], [[1]], [0], [[1]], [[2.0], [2.0]])
    # n = 1: prior variance 2, gain 2/3; n = 2: prior variance 5/3, gain 5/8
    assert np.allclose(xs[0], [4 / 3]) and np.allclose(Ss[0], [[2 / 3]])
    assert np.allclose(xs[1], [4 / 3 + 5 / 8 * (2 - 4 / 3)]) and np.allclose(Ss[1], [[5 / 8]])


def test_constant_signal_is_a_running_mean():
    # X_n = X_0 with no process noise and a flat prior: the estimate is close to the sample mean
    ys = [[5.0], [7.0], [3.0], [9.0]]
    xs, Ss = kalman_filter([[1]], [[1]], [[0]], [[1]], [0], [[1e9]], ys)
    for n in range(1, 5):
        assert np.allclose(xs[n - 1], [np.mean(ys[:n])], atol=1e-6)
        assert np.allclose(Ss[n - 1], [[1 / n]], atol=1e-6)


def batch_estimate(A, C, SV, SW, x0, S0, ys):
    """E[X_N | Y_1..Y_N] by conditioning the joint Gaussian of (X_N, Y_1..Y_N) directly."""
    N, s = len(ys), len(x0)
    # X_n = A^n X_0 + sum_{k<=n} A^(n-k) V_k: write every X_n as a linear map of (X_0, V_1..V_N)
    G = [np.hstack([np.linalg.matrix_power(A, n)] +
                   [np.linalg.matrix_power(A, n - k) if k <= n else np.zeros((s, s)) for k in range(1, N + 1)])
         for n in range(N + 1)]
    Z = np.block([[S0, np.zeros((s, s * N))], [np.zeros((s * N, s)), np.kron(np.eye(N), SV)]])
    H = np.vstack([C @ G[n] for n in range(1, N + 1)])
    SY = H @ Z @ H.T + np.kron(np.eye(N), SW)
    SXY = G[N] @ Z @ H.T
    mean_x = np.linalg.matrix_power(A, N) @ x0
    mean_y = np.concatenate([C @ np.linalg.matrix_power(A, n) @ x0 for n in range(1, N + 1)])
    return mean_x + SXY @ np.linalg.solve(SY, np.concatenate(ys) - mean_y)


def test_agrees_with_direct_conditioning():
    rng = np.random.default_rng(126)
    dt = 0.1
    A = np.array([[1, dt], [0, 1]])          # position and velocity
    C = np.array([[1.0, 0.0]])               # only position is measured
    SV, SW = np.diag([0.01, 0.1]), np.array([[0.5]])
    x0, S0 = np.array([1.0, -1.0]), np.eye(2)
    ys = [rng.normal(size=1) for _ in range(8)]
    xs, Ss = kalman_filter(A, C, SV, SW, x0, S0, ys)
    assert len(xs) == len(Ss) == 8
    for n in (1, 4, 8):
        assert np.allclose(xs[n - 1], batch_estimate(A, C, SV, SW, x0, S0, ys[:n]))
```
:::
