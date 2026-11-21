<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-2-q5" status="draft"}
1. Without the division, a training-time dropout layer outputs $\mathbf{r}\odot\mathbf{h}$, whose expectation is $p\,\mathbf{h}$ (@prp-dropout-expectation). The following layers learn their weights for inputs of that size.
2. At test time the layer is the identity, so the following layer receives $\mathbf{h}$, about $1/p$ times larger than during training (twice as large for $p=0.5$).
3. Its pre-activations are then systematically too large, and the shift compounds through later layers, so the test-time predictions are not those of the averaged network and accuracy drops. Either divide by $p$ during training (inverted dropout) or multiply by $p$ at test time.
:::

::: {.solution for="prob-inverted-dropout-code" status="draft"}
```{.python}
import numpy as np


def dropout_forward(x, p, train, rng):
    """Inverted dropout; returns (out, mask)."""
    if not train:
        return x, None
    mask = (rng.random(x.shape) < p) / p
    return x * mask, mask


def dropout_backward(dout, mask):
    """Gradient of inverted dropout in training mode."""
    return dout * mask
```
:::
