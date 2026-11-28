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

::: {#prob-gaussian-fusion-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-kalman" packages="numpy"}
A vector $X$ has prior $N(\hat x_1,\Sigma_1)$, and a sensor reports $Y=X+W$ with $W\sim N(0,\Sigma_2)$ independent of $X$. Write `fuse(x1, S1, x2, S2)` that returns the mean and covariance of $X$ given $Y=\hat x_2$ (@thm-jointly-gaussian-conditional), as NumPy arrays. This is the update step of the Kalman filter (@thm-kalman-filter). The tests check it against the "add the precisions" form and show that the plain average $(\hat x_1+\hat x_2)/2$ is a poor estimate when the covariances differ.

```{.python .starter}
import numpy as np


def fuse(x1, S1, x2, S2):
    """X has prior N(x1, S1); we observe Y = X + W with W ~ N(0, S2) independent of X,
    and Y = x2. Return (mean, covariance) of X given Y = x2."""
    ...
```

```{.python .tests}
import numpy as np


def test_scalar():
    x, S = fuse([0.0], [[1.0]], [2.0], [[1.0]])
    assert np.allclose(x, [1.0]) and np.allclose(S, [[0.5]])
    x, S = fuse([0.0], [[1.0]], [3.0], [[2.0]])
    assert np.allclose(x, [1.0]) and np.allclose(S, [[2 / 3]])


def test_precision_form():
    # the same answer as adding precisions: S = (S1^-1 + S2^-1)^-1, x = S (S1^-1 x1 + S2^-1 x2)
    rng = np.random.default_rng(0)
    for _ in range(5):
        M1, M2 = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))
        S1, S2 = M1 @ M1.T + 0.1 * np.eye(3), M2 @ M2.T + 0.1 * np.eye(3)
        x1, x2 = rng.normal(size=3), rng.normal(size=3)
        P1, P2 = np.linalg.inv(S1), np.linalg.inv(S2)
        S = np.linalg.inv(P1 + P2)
        xf, Sf = fuse(x1, S1, x2, S2)
        assert np.allclose(Sf, S) and np.allclose(xf, S @ (P1 @ x1 + P2 @ x2))


def test_correlated_noise_is_not_averaged():
    # the unweighted average ignores the covariances
    S1 = np.array([[4.0, 1.0], [1.0, 0.81]])
    S2 = np.array([[0.25, -0.4], [-0.4, 9.0]])
    x, S = fuse(np.array([3.0, 5.0]), S1, np.array([2.0, 7.0]), S2)
    assert not np.allclose(x, [2.5, 6.0])
    assert np.all(np.linalg.eigvalsh(S1 - S) > -1e-12) and np.all(np.linalg.eigvalsh(S2 - S) > -1e-12)


def test_useless_measurement():
    x, S = fuse([1.0, 2.0], np.eye(2), [9.0, 9.0], 1e12 * np.eye(2))
    assert np.allclose(x, [1.0, 2.0], atol=1e-9) and np.allclose(S, np.eye(2), atol=1e-9)
```
:::

::: {.problem #prob-camib-sts-3-q1 origin="external" source="camib-sts-3-q1"}
Let $X\sim N_n(\mu,\Sigma)$, and let $A$ be an arbitrary $m\times n$ matrix. Prove directly from the definition that $AX$ has an $m$-variate normal distribution $AX\sim N_m(A\mu,A\Sigma A^{\mathsf T})$.
:::

::: {.problem #prob-camib-sts-3-q2 origin="external" source="camib-sts-3-q2"}
Let $X$ and $Y$ be $N(0,1)$ random variables such that $\mathrm{cov}(X,Y)=0$. Show by example that $X$ and $Y$ need not be independent. (Hint: Take $Y=XZ$ where $X$ and $Z$ are independent and the distribution of $Z$ is chosen appropriately.)
:::

::: {.problem #prob-camib-sts-3-q4 origin="external" source="camib-sts-3-q4"}
Let $X\sim N_n(\mu,\Sigma)$, and let $X_1$ denote the first $n_1$ components of $X$. Let $\mu_1$ denote the first $n_1$ components of $\mu$, and let $\Sigma_{11}$ denote the upper left $n_1\times n_1$ block of $\Sigma$. Show that $X_1\sim N_{n_1}(\mu_1,\Sigma_{11})$.
:::
