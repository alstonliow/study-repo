::: {.problem #prob-cs231na-2-q5 origin="external" source="cs231na-2-q5"}
What happens if we do not divide the values being passed through inverse dropout by `p` in the dropout layer? Why does that happen?
:::

::: {#prob-inverted-dropout-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps2" packages="numpy"}
Write `dropout_forward(x, p, train, rng)` and `dropout_backward(dout, mask)` for inverted dropout with keep probability `p` (@def-dropout).

- In training mode draw the keep mask as `rng.random(x.shape) < p` (one call to `rng`) and return `(out, mask)` with `mask` the float array $\mathbf r/p$, so that `out = x * mask`.
- In test mode return `(x, None)` and do not use `rng`.
- `dropout_backward` returns the gradient with respect to `x` in training mode.

```{.python .starter}
import numpy as np


def dropout_forward(x, p, train, rng):
    """Inverted dropout; returns (out, mask)."""
    ...


def dropout_backward(dout, mask):
    """Gradient of inverted dropout in training mode."""
    ...
```

```{.python .tests}
import numpy as np


def test_mask_and_scaling():
    x = np.arange(1.0, 7.0).reshape(2, 3)
    out, mask = dropout_forward(x, 0.5, True, np.random.default_rng(0))
    keep = np.random.default_rng(0).random(x.shape) < 0.5
    assert np.allclose(out, np.where(keep, 2 * x, 0.0))
    assert np.allclose(dropout_backward(np.ones_like(x), mask), np.where(keep, 2.0, 0.0))


def test_test_mode_is_identity():
    x = np.ones((3, 3))
    out, mask = dropout_forward(x, 0.3, False, None)
    assert out is x and mask is None


def test_expectation_is_preserved():
    x = np.full(200000, 3.0)
    out, _ = dropout_forward(x, 0.8, True, np.random.default_rng(1))
    assert abs(out.mean() - 3.0) < 0.02
```
:::
