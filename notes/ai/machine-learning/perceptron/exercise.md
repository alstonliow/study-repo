::: {#prob-perceptron-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-machinelearning" solution="withheld" packages="numpy"}
Implement the binary perceptron (@def-perceptron) as `perceptron(F, y, max_passes=1000)`.

- `F` is an array of shape `(n, d)` whose row $i$ is the feature vector $\mathbf f(x_i)$ (include a constant feature for a bias), and `y` an array of $n$ labels in $\{-1,+1\}$.
- Start from $\mathbf w=\mathbf 0$ and pass over the examples in order, predicting $+1$ exactly when $\mathbf w\cdot\mathbf f(x)>0$.
- Return $\mathbf w$ after the first pass with no mistakes, or `None` if `max_passes` passes all make mistakes.

```{.python .starter}
import numpy as np


def perceptron(F, y, max_passes=1000):
    """Train a binary perceptron; return the weight vector, or None if it
    has not converged after max_passes passes."""
    ...
```

```{.python .tests}
import numpy as np


def test_four_points_trace():
    # the example of the note: features (1, a, b)
    F = np.array([[1, 1, 2], [1, 2, 0], [1, 0, 1], [1, 3, 2]], dtype=float)
    y = np.array([1, -1, 1, -1])
    assert np.allclose(perceptron(F, y), [0, -3, 2])


def test_zero_score_is_negative():
    # with w = 0 the first prediction is -1, so a first example labelled -1 is no mistake
    w = perceptron(np.array([[1.0, 1.0]]), np.array([-1]))
    assert np.allclose(w, [0, 0])
    assert np.allclose(perceptron(np.array([[1.0, 1.0]]), np.array([1])), [1, 1])


def test_separable_cloud():
    rng = np.random.default_rng(0)
    X = rng.uniform(-1, 1, size=(200, 2))
    X = X[np.abs(X[:, 0] + 2 * X[:, 1] - 0.3) > 0.1]          # keep a margin
    y = np.where(X[:, 0] + 2 * X[:, 1] - 0.3 > 0, 1, -1)
    F = np.hstack([np.ones((len(X), 1)), X])
    w = perceptron(F, y)
    assert w is not None
    assert np.all(np.where(F @ w > 0, 1, -1) == y), "the returned w must classify every example"


def test_not_separable():
    F = np.array([[1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=float)   # XOR
    y = np.array([-1, -1, 1, 1])
    assert perceptron(F, y, max_passes=50) is None
```
:::
