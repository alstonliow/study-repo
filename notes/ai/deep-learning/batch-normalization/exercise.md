::: {.problem #prob-cs231na-2-q3 origin="external" source="cs231na-2-q3"}
Which of these data preprocessing steps is analogous to batch normalization, and which is analogous to layer normalization?

1. Scaling each image in the dataset, so that the RGB channels for each row of pixels within an image sums up to 1.
2. Scaling each image in the dataset, so that the RGB channels for all pixels within an image sums up to 1.  
3. Subtracting the mean image of the dataset from each image in the dataset.
4. Setting all RGB values to either 0 or 1 depending on a given threshold.
:::

::: {.problem #prob-cs231na-2-q4 origin="external" source="cs231na-2-q4"}
When is layer normalization likely to not work well, and why?

1. Using it in a very deep network
2. Having a very small dimension of features
3. Having a high regularization term
:::

::: {#prob-batchnorm-backward-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps2" packages="numpy"}
Write `batchnorm_backward(dout, x, gamma, eps=1e-5)` for training-mode batch normalization (@def-batch-normalization) of an input `x` of shape `(N, D)`. Given the upstream gradient `dout` $=\partial L/\partial Y$, return `(dx, dgamma, dbeta)` using the closed form of @thm-batch-normalization-backward, recomputing what you need from `x` (no loop over the examples).

```{.python .starter}
import numpy as np


def batchnorm_backward(dout, x, gamma, eps=1e-5):
    """Gradients of training-mode batch normalization."""
    ...
```

```{.python .tests}
import numpy as np


def forward(x, gamma, beta, eps=1e-5):
    xh = (x - x.mean(axis=0)) / np.sqrt(x.var(axis=0) + eps)
    return gamma * xh + beta


def test_against_finite_differences():
    rng = np.random.default_rng(2)
    x, gamma, beta = rng.normal(size=(5, 3)), rng.normal(size=3), rng.normal(size=3)
    dout = rng.normal(size=(5, 3))
    dx, dgamma, dbeta = batchnorm_backward(dout, x, gamma)
    L = lambda x_, g_, b_: np.sum(forward(x_, g_, b_) * dout)
    h = 1e-6
    for arr, grad, which in [(x, dx, 0), (gamma, dgamma, 1), (beta, dbeta, 2)]:
        num = np.zeros_like(arr)
        for idx in np.ndindex(arr.shape):
            args_p, args_m = [x.copy(), gamma.copy(), beta.copy()], [x.copy(), gamma.copy(), beta.copy()]
            args_p[which][idx] += h
            args_m[which][idx] -= h
            num[idx] = (L(*args_p) - L(*args_m)) / (2 * h)
        assert np.allclose(grad, num, atol=1e-5)


def test_constant_upstream_gradient_gives_zero_dx():
    rng = np.random.default_rng(3)
    x = rng.normal(size=(4, 2))
    dx, dgamma, dbeta = batchnorm_backward(np.ones((4, 2)), x, np.array([1.0, 2.0]))
    assert np.allclose(dx, 0.0, atol=1e-10) and np.allclose(dbeta, [4.0, 4.0])
```
:::
