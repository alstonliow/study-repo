::: {#prob-gan-losses-code .problem .coding origin="self" source="res-stanford-cs231n-notes-generative-models" packages="numpy"}
Write `gan_losses(logits_real, logits_fake)` returning `(d_loss, g_loss)`, the discriminator loss and the non-saturating generator loss of @def-gan-training, as averages to be *minimized*. The discriminator outputs $D=\sigma(s)$ for logits $s$:

$$
\text{d\_loss}=-\operatorname{mean}\log\sigma(s_{\text{real}})-\operatorname{mean}\log\bigl(1-\sigma(s_{\text{fake}})\bigr),\qquad \text{g\_loss}=-\operatorname{mean}\log\sigma(s_{\text{fake}}).
$$

Compute $\log\sigma(s)$ stably for logits of any size, using $\log\sigma(s)=-\log(1+e^{-s})$ and $\log(1-\sigma(s))=\log\sigma(-s)$.

```{.python .starter}
import numpy as np


def gan_losses(logits_real, logits_fake):
    """Discriminator loss and non-saturating generator loss from logits."""
    ...
```

```{.python .tests}
import numpy as np


def test_zero_logits():
    d, g = gan_losses(np.zeros(3), np.zeros(5))
    assert np.isclose(d, 2 * np.log(2)) and np.isclose(g, np.log(2))


def test_values():
    s_r, s_f = np.array([2.0, -1.0]), np.array([0.5])
    sig = lambda s: 1 / (1 + np.exp(-s))
    d, g = gan_losses(s_r, s_f)
    assert np.isclose(d, -np.mean(np.log(sig(s_r))) - np.mean(np.log(1 - sig(s_f))))
    assert np.isclose(g, -np.log(sig(0.5)))


def test_extreme_logits_are_finite():
    d, g = gan_losses(np.array([800.0, -800.0]), np.array([-900.0, 900.0]))
    assert np.isfinite(d) and np.isfinite(g)
    assert np.isclose(g, 450.0)
```
:::
