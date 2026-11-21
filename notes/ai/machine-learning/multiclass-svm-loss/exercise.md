::: {.problem #prob-cs231na-1-q7 origin="external" source="cs231na-1-q7"}
True or false? Suppose the overall training loss is defined as the sum of the per-datapoint loss over all training examples. It is possible to add a new datapoint to a training set that would change the softmax loss, but leave the SVM loss unchanged.
:::

::: {#prob-multiclass-svm-loss-code .problem .coding origin="self" source="res-stanford-cs231n-notes-linear-classification" packages="numpy"}
Write `svm_loss_grad(W, X, y, reg, delta=1.0)` for the regularized multiclass SVM objective of @def-multiclass-svm-loss, vectorized over the examples.

- `W` has shape `(D, K)`, `X` shape `(N, D)` (rows are examples, so the scores are `X @ W`), `y` integer labels of shape `(N,)`.
- Return `(loss, dW)`: the average hinge loss over the $N$ examples plus `reg * np.sum(W**2)`, and its gradient with the shape of `W`, using @thm-multiclass-svm-gradient (at a kink, take the derivative of $\max(0,u)$ at $u=0$ to be $0$).

```{.python .starter}
import numpy as np


def svm_loss_grad(W, X, y, reg, delta=1.0):
    """Average multiclass hinge loss plus L2 penalty, and its gradient."""
    ...
```

```{.python .tests}
import numpy as np


def test_three_classes():
    # scores (2, 5, -1) with correct class 0, as in the note's example
    W = np.array([[2.0, 5.0, -1.0]])
    loss, dW = svm_loss_grad(W, np.array([[1.0]]), np.array([0]), 0.0)
    assert np.isclose(loss, 4.0)
    assert np.allclose(dW, [[-1.0, 1.0, 0.0]])


def test_regularization_and_numerical_gradient():
    rng = np.random.default_rng(0)
    W, X, y = rng.normal(size=(4, 3)), rng.normal(size=(6, 4)), rng.integers(0, 3, size=6)
    loss, dW = svm_loss_grad(W, X, y, 0.1)
    h, num = 1e-6, np.zeros_like(W)
    for idx in np.ndindex(W.shape):
        E = np.zeros_like(W)
        E[idx] = h
        num[idx] = (svm_loss_grad(W + E, X, y, 0.1)[0] - svm_loss_grad(W - E, X, y, 0.1)[0]) / (2 * h)
    assert np.allclose(dW, num, atol=1e-5)
    assert loss > 0.1 * np.sum(W**2)


def test_margins_satisfied():
    W = np.array([[10.0, 0.0], [0.0, 10.0]])
    loss, dW = svm_loss_grad(W, np.eye(2), np.array([0, 1]), 0.0)
    assert loss == 0.0 and np.all(dW == 0)
```
:::
