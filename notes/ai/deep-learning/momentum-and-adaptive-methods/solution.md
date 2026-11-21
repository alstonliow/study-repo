<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-1-q12" status="draft"}
1. The cache adds the square of every gradient and never decreases, so the effective learning rate $\eta/(\sqrt{\text{cache}}+\varepsilon)$ of each weight only shrinks. After $t$ steps with gradients of typical size $g$, the cache is about $tg^2$ and the step about $\eta/\sqrt t$ (@prp-adagrad-decay): over a long run the updates become very small and learning stalls, even if the weights are still far from a good solution.
2. Adam does not have this problem. Its second-moment estimate $\mathbf{v}_t$ is an exponential moving average of $\mathbf{g}^2$ (@def-adam), which forgets old gradients and stays of the size of recent squared gradients instead of growing with $t$. With bias correction, the step is of size about $\eta$ in every coordinate (for steady gradients exactly $\eta$, @prp-adam-bias-correction), so it does not decay unless the learning rate is annealed.
:::

::: {.solution for="prob-adam-update-code" status="draft"}
```{.python}
import numpy as np


def adam_update(w, g, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """One Adam step; returns the new (w, m, v)."""
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * g**2
    m_hat = m / (1 - beta1**t)
    v_hat = v / (1 - beta2**t)
    return w - lr * m_hat / (np.sqrt(v_hat) + eps), m, v
```
:::
