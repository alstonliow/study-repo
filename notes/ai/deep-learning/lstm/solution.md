<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-lstm-step-code" status="draft"}
```{.python}
import numpy as np


def lstm_step(x, h_prev, c_prev, Wx, Wh, b):
    """One LSTM step; returns (h, c)."""
    a = x @ Wx + h_prev @ Wh + b
    M = a.shape[-1] // 4
    sig = lambda z: 1 / (1 + np.exp(-z))
    i, f, o = sig(a[..., :M]), sig(a[..., M:2 * M]), sig(a[..., 2 * M:3 * M])
    g = np.tanh(a[..., 3 * M:])
    c = f * c_prev + i * g
    return o * np.tanh(c), c
```
:::
