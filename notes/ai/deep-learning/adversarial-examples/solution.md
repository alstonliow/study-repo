<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-fgsm-linear-code" status="draft"}
```{.python}
import numpy as np


def fgsm(x, y, W, b, eps):
    """FGSM perturbation of x against a linear softmax classifier."""
    s = W @ x + b
    p = np.exp(s - s.max())
    p /= p.sum()
    p[y] -= 1.0
    grad = W.T @ p
    return x + eps * np.sign(grad)
```

1. The gradient of the cross entropy with respect to the scores is $\mathbf p-\mathbf e_y$ (@thm-cross-entropy-gradient), and $\mathbf s=W\mathbf x+\mathbf b$ gives $\nabla_{\mathbf x}J=W^{\mathsf T}(\mathbf p-\mathbf e_y)$.
2. With two classes this is $p_1(\mathbf w_1-\mathbf w_0)$, whose sign is that of $\mathbf w_1-\mathbf w_0$, as in the first test.
:::
