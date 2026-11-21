::: {#prob-conv-forward-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps2" packages="numpy"}
Write `conv_forward(x, w, b, stride, pad)` for the convolutional layer of @def-convolutional-layer on a batch.

- `x` has shape `(N, C, H, W)`, the filters `w` shape `(K, C, F, F)`, the biases `b` shape `(K,)`.
- Pad height and width with `pad` zeros on each side, then return the output of shape `(N, K, H', W')` with the sizes of @prp-conv-output-size (assume they are integers). Loops over output positions are fine.

```{.python .starter}
import numpy as np


def conv_forward(x, w, b, stride, pad):
    """Naive forward pass of a convolutional layer."""
    ...
```

```{.python .tests}
import numpy as np


def test_one_channel_by_hand():
    x = np.arange(16.0).reshape(1, 1, 4, 4)
    w = np.array([[[[1.0, 0.0], [0.0, -1.0]]]])
    out = conv_forward(x, w, np.array([0.5]), stride=2, pad=0)
    # each window gives top-left minus bottom-right = -5, plus the bias
    assert out.shape == (1, 1, 2, 2)
    assert np.allclose(out, -4.5)


def test_padding_keeps_size_and_matches_sum():
    rng = np.random.default_rng(4)
    x, w, b = rng.normal(size=(2, 3, 5, 5)), rng.normal(size=(4, 3, 3, 3)), rng.normal(size=4)
    out = conv_forward(x, w, b, stride=1, pad=1)
    assert out.shape == (2, 4, 5, 5)
    xp = np.pad(x, ((0, 0), (0, 0), (1, 1), (1, 1)))
    assert np.isclose(out[1, 2, 0, 3], np.sum(xp[1, :, 0:3, 3:6] * w[2]) + b[2])


def test_one_by_one_is_channel_mixing():
    rng = np.random.default_rng(5)
    x, w = rng.normal(size=(1, 3, 2, 2)), rng.normal(size=(2, 3, 1, 1))
    out = conv_forward(x, w, np.zeros(2), stride=1, pad=0)
    assert np.allclose(out[0], np.einsum("kc,chw->khw", w[:, :, 0, 0], x[0]))
```
:::
