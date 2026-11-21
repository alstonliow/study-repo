<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-conv-forward-code" status="draft"}
```{.python}
import numpy as np


def conv_forward(x, w, b, stride, pad):
    """Naive forward pass of a convolutional layer."""
    N, C, H, W = x.shape
    K, _, F, _ = w.shape
    Ho, Wo = (H - F + 2 * pad) // stride + 1, (W - F + 2 * pad) // stride + 1
    xp = np.pad(x, ((0, 0), (0, 0), (pad, pad), (pad, pad)))
    out = np.zeros((N, K, Ho, Wo))
    for i in range(Ho):
        for j in range(Wo):
            win = xp[:, :, i * stride:i * stride + F, j * stride:j * stride + F]
            out[:, :, i, j] = np.einsum("ncuv,kcuv->nk", win, w) + b
    return out
```
:::
