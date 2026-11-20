::: {.problem #prob-cs221hw-1-q2 origin="external" source="cs221hw-1-q2"}
(a) **Gradient Warmup:** Let's practice taking gradients, which is a key operation for being able to optimize continuous functions. Let $\mathbf w, \mathbf c \in \mathbb R^d$. For $f(\mathbf w)=\sum_{i=1}^d (w_i-c_i)^2$, derive $\nabla f(\mathbf w)$. Then evaluate the gradient at $\mathbf w=\mathbf 0$.

*Expected:* A compact vector expression for $\nabla f(\mathbf w)$ and its value at $\mathbf w = \mathbf 0$. Show your work.

(c) **Matrix Multiplication Gradient:** Consider two matrices $A$ (size $m \times n$) and $B$ (size $n \times p$) that are multiplied together to form $C = AB$, and then all entries of $C$ are summed to produce a scalar $s = \sum_{i,j} C_{i,j}$. Let $A = \begin{pmatrix} 2 & 1 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ and $B = \begin{pmatrix} 7 & 8 \\ 9 & 0 \\ 1 & 2 \end{pmatrix}$. Compute $C = AB$ and $s = \sum_{i,j} C_{i,j}$. Then find the gradient $\frac{\partial s}{\partial A_{i,k}}$ for each entry of matrix $A$, and similarly find $\frac{\partial s}{\partial B_{k,j}}$ for each entry of matrix $B$.

*Expected:* The computed matrices $C$ and scalar $s$, plus the gradient matrices $\frac{\partial s}{\partial A}$ and $\frac{\partial s}{\partial B}$ with numerical values for each entry. Show your work, including how you derived the gradients.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-backpropagation-gradient-check-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-foundations" packages="numpy"}
A gradient computed by backpropagation (@def-backpropagation) is usually checked against finite differences. Write `numerical_gradient(f, w, h=1e-5)`.

- `f` maps a NumPy array of the shape of `w` to a number; `w` is a float array of any shape.
- Return an array of the shape of `w` whose entry at each index $i$ is the central difference
$$\frac{f(\mathbf w+h\mathbf e_i)-f(\mathbf w-h\mathbf e_i)}{2h},$$
where $\mathbf e_i$ is $1$ at index $i$ and $0$ elsewhere.
- Do not change `w`, even temporarily in a way the caller can see after the call.

```{.python .starter}
import numpy as np


def numerical_gradient(f, w, h=1e-5):
    """Central-difference estimate of the gradient of f at w (same shape as w)."""
    ...
```

```{.python .tests}
import numpy as np

rng = np.random.default_rng(2)


def test_quadratic_is_exact():
    # central differences are exact for quadratics, up to rounding
    Q = np.array([[2.0, 1.0], [1.0, 3.0]])
    f = lambda w: 0.5 * w @ Q @ w + w[0]
    w = np.array([1.0, -2.0])
    assert np.allclose(numerical_gradient(f, w), Q @ w + [1.0, 0.0], atol=1e-6)


def test_matrix_argument():
    # the least-squares loss of a matrix: grad of 0.5 ||X W - Y||^2 is X^T (X W - Y)
    X, Y, W = rng.normal(size=(5, 3)), rng.normal(size=(5, 2)), rng.normal(size=(3, 2))
    f = lambda W: 0.5 * np.sum((X @ W - Y) ** 2)
    g = numerical_gradient(f, W)
    assert g.shape == W.shape
    assert np.allclose(g, X.T @ (X @ W - Y), atol=1e-5)


def test_catches_wrong_backward_pass():
    f = lambda w: np.sum(np.tanh(w))
    w = rng.normal(size=4)
    right, wrong = 1 - np.tanh(w) ** 2, 1 - np.tanh(w)
    g = numerical_gradient(f, w)
    assert np.allclose(g, right, atol=1e-7) and not np.allclose(g, wrong, atol=1e-3)


def test_w_unchanged():
    w = np.array([0.5, 1.5])
    before = w.copy()
    numerical_gradient(lambda v: float(np.prod(v)), w)
    assert np.array_equal(w, before)
```
:::
