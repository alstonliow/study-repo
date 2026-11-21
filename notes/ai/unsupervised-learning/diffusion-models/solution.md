<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-ddpm-reverse-step-code" status="draft"}
```{.python}
import numpy as np


def ddpm_reverse_step(x_t, t, eps_pred, betas, z):
    """x_{t-1} from x_t and the predicted noise."""
    alphas = 1.0 - betas
    abar = np.cumprod(alphas)
    beta, alpha, ab = betas[t - 1], alphas[t - 1], abar[t - 1]
    mean = (x_t - beta / np.sqrt(1 - ab) * eps_pred) / np.sqrt(alpha)
    if t == 1:
        return mean
    var = (1 - abar[t - 2]) / (1 - ab) * beta
    return mean + np.sqrt(var) * z
```

1. The mean is the noise form of $\tilde{\boldsymbol\mu}_t$ in @prp-diffusion-posterior, with $\boldsymbol\varepsilon$ replaced by its prediction; the first test checks it against the $\mathbf x_0$ form when the prediction is exact.
2. The variance is $\tilde\beta_t$, which needs $\bar\alpha_{t-1}$ (`abar[t-2]` in 0-based storage); at $t=1$ the step returns the mean.
:::
