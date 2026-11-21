<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-max-pool-backward-code" status="draft"}
```{.python}
import numpy as np


def max_pool_backward(dout, x, size, stride):
    """Gradient of max pooling with respect to its input."""
    N, C, Ho, Wo = dout.shape
    dx = np.zeros_like(x, dtype=float)
    for n in range(N):
        for c in range(C):
            for i in range(Ho):
                for j in range(Wo):
                    win = x[n, c, i * stride:i * stride + size, j * stride:j * stride + size]
                    u, v = np.unravel_index(np.argmax(win), win.shape)
                    dx[n, c, i * stride + u, j * stride + v] += dout[n, c, i, j]
    return dx
```
:::
