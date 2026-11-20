::: {.problem #prob-cs70hw-14-q7 origin="external" source="cs70hw-14-q7"}
**Sampling a Gaussian With Uniform.** In this question, we will see one way to generate a normal random variable if we have access to a random number generator that outputs numbers between 0 and 1 uniformly at random.

As a general comment, remember that showing two random variables have the same CDF or PDF is sufficient for showing that they have the same distribution.

(a) First, let us see how to generate an exponential random variable with a uniform random variable. Let $U_1 \sim \mathrm{Uniform}(0, 1)$. Prove that $-\ln U_1 \sim \mathrm{Expo}(1)$.

(b) Let $N_1, N_2 \sim \mathcal{N}(0, 1)$, where $N_1$ and $N_2$ are independent. Prove that $N_1^2 + N_2^2 \sim \mathrm{Expo}(1/2)$.

Hint: You may use the fact that over a region $R$, if we convert to polar coordinates $(x, y) \to (r, \theta)$, then the double integral over the region $R$ will be
$$\iint_R f(x, y)\, dx\, dy = \iint_R f(r\cos\theta, r\sin\theta) \cdot r\, dr\, d\theta.$$

(c) Suppose we have two uniform random variables, $U_1$ and $U_2$. How would you transform these two random variables into a normal random variable with mean 0 and variance 1?

Hint: What part (b) tells us is that the point $(N_1, N_2)$ will have a distance from the origin that is distributed as the square root of an exponential distribution. Try to use $U_1$ to sample the radius, and then use $U_2$ to sample the angle.
:::

::: {.problem #prob-eecs126hw-3-q4 origin="external" source="eecs126hw-3-q4"}
**Gaussian Densities.**

(a) Let $X_1\sim N(0,1)$, $X_2\sim N(0,1)$, where $X_1$ and $X_2$ are independent. Convolve the densities of $X_1$ and $X_2$ to show that $X_1+X_2\sim N(0,2)$. Remark. Note that this property is similar to the one shared by independent Poisson random variables.

(b) Let $X\sim N(0,1)$. Compute $E[X^n]$ for all integers $n\ge1$.
:::

::: {.problem #prob-eecs126hw-6-q5 origin="external" source="eecs126hw-6-q5"}
**Matrix Sketching.** Matrix sketching is an important technique in randomized linear algebra to do large computations efficiently. For example, to compute the multiplication $A^T\times B$ of two large matrices $A$ and $B$, we can use a random sketch matrix $S$ to compute a "sketch" $SA$ of $A$ and a "sketch" $SB$ of $B$. Such a sketching matrix has the property that $S^TS\approx I$ so that the approximate multiplication $A^TS^TSB$ is close to $A^TB$.

In this problem, we will discuss two popular sketching schemes and understand how they help in approximate computation. Let $\hat I=S^TS$ and the dimension of sketch matrix $S$ be $d\times n$ (typically $d\ll n$).

(a) (Gaussian-sketch) Define
$$S=\frac{1}{\sqrt d}\begin{pmatrix}S_{11}&\cdots&\cdots&S_{1n}\\\vdots&\ddots&&\vdots\\S_{d1}&\cdots&\cdots&S_{dn}\end{pmatrix}$$
such that $S_{ij}$'s are chosen i.i.d. from $N(0,1)$ for all $i\in[1,d]$ and $j\in[1,n]$. Find the element-wise mean and variance (as a function of $d$) of the matrix $\hat I=S^TS$, that is, find $E[\hat I_{ij}]$ and $\operatorname{Var}[\hat I_{ij}]$ for all $i\in[1,n]$ and $j\in[1,n]$.

(b) (Count-sketch) For each column $j\in[1,n]$ of $S$, choose a row $i$ uniformly randomly from $[1,d]$ such that
$$S_{ij}=\begin{cases}1,&\text{with probability }0.5\\-1,&\text{with probability }0.5\end{cases}$$
and assign $S_{kj}=0$ for all $k\ne i$. An example of a $3\times8$ count-sketch is
$$S=\begin{pmatrix}0&-1&1&0&0&-1&0&0\\1&0&0&0&-1&0&-1&0\\0&0&0&1&0&0&0&-1\end{pmatrix}$$
Again, find the element-wise mean and variance (as a function of $d$) of the matrix $\hat I=S^TS$.

Note that for sufficiently large $d$, the matrix $\hat I$ is close to the identity matrix for both cases. We will use this fact in the lab to do an approximate matrix multiplication.

Note: You can use the fact that the fourth moment of a standard Gaussian is 3 without proof.
:::

::: {#prob-count-sketch-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-sketching" packages="numpy"}
A *count sketch* $S$ is a $d\times n$ matrix with one nonzero entry in each column: $S_{h(j),j}=\sigma_j\in\{-1,+1\}$ for a row $h(j)\in\{0,\dots,d-1\}$. When the $h(j)$ are uniform and the $\sigma_j$ are fair signs, all independent, $E[S^{\mathsf T}S]=I$ (@prob-eecs126hw-6-q5). So $(SA)^{\mathsf T}(SA)$ estimates $A^{\mathsf T}A$ from a $d\times m$ matrix instead of an $n\times m$ one.

Write `count_sketch(A, h, sign, d)` that returns $SA$ for given arrays `h` and `sign`, without forming $S$. Row $j$ of $A$, times $\sigma_j$, is added to row $h(j)$ of the result, which takes time $O(nm)$; a Gaussian sketch with $S_{ij}\sim N(0,1/d)$ would need $O(dnm)$. The tests take $A=I$, so that the result is $S$ itself, and check the mean and variance of $S^{\mathsf T}S$ found in that problem.

```{.python .starter}
import numpy as np


def count_sketch(A, h, sign, d):
    """Return C = S A for the d x n count sketch S with S[h[j], j] = sign[j]
    and all other entries 0, without forming S (time O(n m) for A of shape n x m)."""
    ...
```

```{.python .tests}
import numpy as np


def explicit(h, sign, d):
    S = np.zeros((d, len(h)))
    S[h, np.arange(len(h))] = sign
    return S


def test_matches_explicit_matrix():
    rng = np.random.default_rng(0)
    A = rng.normal(size=(7, 3))
    h = np.array([0, 2, 2, 1, 0, 2, 1])
    sign = np.array([1, -1, 1, 1, -1, -1, 1])
    assert np.allclose(count_sketch(A, h, sign, 3), explicit(h, sign, 3) @ A)


def test_collisions_add_up():
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    assert np.allclose(count_sketch(A, [0, 0], [1, 1], 2), [[4, 6], [0, 0]])
    assert np.allclose(count_sketch(A, [1, 1], [1, -1], 2), [[0, 0], [-2, -2]])


def test_sketch_of_identity_is_unbiased():
    # S = count_sketch(I): E[S^T S] = I, the diagonal is exactly 1, Var of off-diagonal = 1/d
    rng = np.random.default_rng(1)
    n, d, trials = 6, 4, 4000
    prods = []
    for _ in range(trials):
        h = rng.integers(0, d, size=n)
        sign = rng.choice([-1, 1], size=n)
        S = count_sketch(np.eye(n), h, sign, d)
        prods.append(S.T @ S)
    prods = np.array(prods)
    assert np.allclose(prods[:, np.arange(n), np.arange(n)], 1)
    assert np.allclose(prods.mean(axis=0), np.eye(n), atol=0.05)
    off = prods[:, 0, 1]
    assert abs(off.var() - 1 / d) < 0.03
```
:::

::: {.problem #prob-mit6041f10-5-q4 origin="external" source="mit6041f10-5-q4"}
Signal Classification: Consider the communication of binary-valued messages over some transmission medium. Specifically, any message transmitted between locations is one of two possible symbols, 0 or 1. Each symbol occurs with equal probability. It is also known that any numerical value sent over this wire is subject to distortion; namely, if the value $X$ is transmitted, the value $Y$ received at the other end is described by $Y = X + N$ where the random variable $N$ represents additive noise that is independent of $X$. The noise $N$ is normally distributed with mean $\mu = 0$ and variance $\sigma^2 = 4$.

(a) Suppose the transmitter encodes the symbol 0 with the value $X = -2$ and the symbol 1 with the value $X = 2$. At the other end, the received message is decoded according to the following rules:
  - If $Y \geq 0$, then conclude the symbol 1 was sent.
  - If $Y < 0$. then conclude the symbol 0 was sent.

  Determine the probability of error for this encoding/decoding scheme. Reduce your calculations to a single numerical value.
(b) In an effort to reduce the probability of error, the following modifications are made. The transmitter encodes the symbols with a repeated scheme. The symbol 0 is encoded with the vector $X = [-2, -2, -2]^\intercal$ and the symbol 1 is encoded with the vector $X = [2, 2, 2]^\intercal$. The vector $Y = [Y_1, Y_2, Y_3]^\intercal$ received at the other end is described by $Y = X + N$. The vector $N = [N_1, N_2, N_3]^\intercal$ represents the noise vector where each $N_i$ is a random variable assumed to be normally distributed with mean $\mu = 0$ and variance $\sigma^2 = 4$. Assume each $N_i$ is independent of each other and independent of the $X_i$'s. Each component value of $Y$ is decoded with the same rule as in part (a). The receiver then uses a majority rule to determine which symbol was sent. The receiver's decoding rules are:
  - If 2 or more components of $Y$ are greater than 0, then conclude the symbol 1 was sent.
  - If 2 or more components of $Y$ are less than 0, then conclude the symbol 0 was sent.

  Determine the probability of error for this modified encoding/decoding scheme. Reduce your calculations to a single numerical value.
:::
