::: {#prob-fgsm-linear-code .problem .coding origin="self" source="res-stanford-cs231n-notes-adversarial-attacks" packages="numpy"}
Write `fgsm(x, y, W, b, eps)` for the untargeted fast gradient sign method (@def-fgsm) against a linear softmax classifier with scores $\mathbf s=W\mathbf x+\mathbf b$ ($W$ of shape `(K, D)`) and the cross entropy loss. Compute the input gradient $\nabla_{\mathbf x}J=W^{\mathsf T}(\mathbf p-\mathbf e_y)$, where $\mathbf p=\operatorname{softmax}(\mathbf s)$, and return $\mathbf x+\varepsilon\operatorname{sign}(\nabla_{\mathbf x}J)$.

```{.python .starter}
import numpy as np


def fgsm(x, y, W, b, eps):
    """FGSM perturbation of x against a linear softmax classifier."""
    ...
```

```{.python .tests}
import numpy as np


def ce(x, y, W, b):
    s = W @ x + b
    s = s - s.max()
    return -(s[y] - np.log(np.exp(s).sum()))


def test_two_classes_by_hand():
    W = np.array([[1.0, -1.0, 0.0], [0.0, 1.0, 2.0]])
    x = np.array([1.0, 0.0, 0.0])
    # correct class 0: the gradient is W^T (p - e_0) with p_1 > 0, so its sign is that of W[1] - W[0]
    out = fgsm(x, 0, W, np.zeros(2), 0.1)
    assert np.allclose(out, x + 0.1 * np.sign(W[1] - W[0]))


def test_loss_increases_and_budget():
    rng = np.random.default_rng(12)
    W, b, x = rng.normal(size=(4, 10)), rng.normal(size=4), rng.normal(size=10)
    out = fgsm(x, 2, W, b, 0.05)
    assert np.allclose(np.abs(out - x), 0.05)
    assert ce(out, 2, W, b) > ce(x, 2, W, b)
```
:::
