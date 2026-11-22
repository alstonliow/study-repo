<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-gan-losses-code" status="draft"}
```{.python}
import numpy as np


def log_sigmoid(s):
    return -np.logaddexp(0.0, -s)


def gan_losses(logits_real, logits_fake):
    """Discriminator loss and non-saturating generator loss from logits."""
    d_loss = -np.mean(log_sigmoid(logits_real)) - np.mean(log_sigmoid(-logits_fake))
    g_loss = -np.mean(log_sigmoid(logits_fake))
    return float(d_loss), float(g_loss)
```

1. `np.logaddexp(0, -s)` computes $\log(1+e^{-s})$ without overflow, so $\log\sigma(s)$ stays finite for logits of any size.
2. The generator loss uses $\log\sigma(s_{\text{fake}})$, whose gradient in $s$ is $1-\sigma(s)$ and does not vanish when the discriminator rejects the samples (@prp-gan-non-saturating).
:::
