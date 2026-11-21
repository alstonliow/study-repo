::: {#prob-max-pool-backward-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps2" packages="numpy"}
Write `max_pool_backward(dout, x, size, stride)` for max pooling (@def-max-pooling) of `x` with shape `(N, C, H, W)`. `dout` is the upstream gradient of shape `(N, C, H', W')`. Return `dx` with the shape of `x`, routing each upstream entry to the position of its window's maximum (@prp-max-pooling-backward; if a window has several maxima, use the first in row-major order) and adding the contributions of overlapping windows.

```{.python .starter}
import numpy as np


def max_pool_backward(dout, x, size, stride):
    """Gradient of max pooling with respect to its input."""
    ...
```

```{.python .tests}
import numpy as np


def test_four_by_four_map():
    x = np.array([[1, 3, 2, 1], [4, 6, 5, 0], [3, 1, 1, 2], [0, 2, 4, 3]], float)[None, None]
    dout = np.array([[10.0, 20.0], [30.0, 40.0]])[None, None]
    dx = max_pool_backward(dout, x, 2, 2)
    expected = np.zeros((4, 4))
    expected[1, 1], expected[1, 2], expected[2, 0], expected[3, 2] = 10, 20, 30, 40
    assert np.allclose(dx[0, 0], expected)


def test_overlapping_windows_add():
    x = np.array([[0.0, 5.0, 0.0]])[None, None]
    dx = max_pool_backward(np.array([[1.0, 2.0]])[None, None], x.reshape(1, 1, 1, 3), 1, 1)[0, 0]
    assert dx.shape == (1, 3)
    x2 = np.array([[1.0, 9.0, 2.0], [0.0, 0.0, 0.0]])[None, None]
    dx2 = max_pool_backward(np.array([[1.0, 2.0]])[None, None], x2, 2, 1)[0, 0]
    assert np.allclose(dx2, [[0.0, 3.0, 0.0], [0.0, 0.0, 0.0]])


def test_ties_go_to_first():
    x = np.ones((1, 1, 2, 2))
    dx = max_pool_backward(np.array([[[[7.0]]]]), x, 2, 2)
    assert np.allclose(dx[0, 0], [[7.0, 0.0], [0.0, 0.0]])
```
:::
