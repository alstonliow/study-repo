::: {#prob-ddpm-reverse-step-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps3" packages="numpy"}
Write `ddpm_reverse_step(x_t, t, eps_pred, betas, z)`, one step of the DDPM reverse process of @def-ddpm. `betas` is the array $(\beta_1,\dots,\beta_T)$ stored 0-based (so $\beta_t$ is `betas[t-1]`), `t` is the step in $1,\dots,T$, `eps_pred` the network's noise prediction and `z` a standard normal array of the shape of `x_t`. Return $\mathbf x_{t-1}$; at $t=1$ ignore `z`.

```{.python .starter}
import numpy as np


def ddpm_reverse_step(x_t, t, eps_pred, betas, z):
    """x_{t-1} from x_t and the predicted noise."""
    ...
```

```{.python .tests}
import numpy as np

betas = np.linspace(1e-4, 0.02, 50)
alphas = 1 - betas
abar = np.cumprod(alphas)


def test_posterior_mean_with_true_noise():
    rng = np.random.default_rng(11)
    x0, eps = rng.normal(size=5), rng.normal(size=5)
    t = 20
    x_t = np.sqrt(abar[t - 1]) * x0 + np.sqrt(1 - abar[t - 1]) * eps
    mean = (np.sqrt(abar[t - 2]) * betas[t - 1] * x0 + np.sqrt(alphas[t - 1]) * (1 - abar[t - 2]) * x_t) / (1 - abar[t - 1])
    var = (1 - abar[t - 2]) / (1 - abar[t - 1]) * betas[t - 1]
    assert np.allclose(ddpm_reverse_step(x_t, t, eps, betas, np.zeros(5)), mean)
    z = rng.normal(size=5)
    assert np.allclose(ddpm_reverse_step(x_t, t, eps, betas, z), mean + np.sqrt(var) * z)


def test_last_step_has_no_noise():
    x1, eps = np.array([0.3, -0.2]), np.array([1.0, 0.5])
    out = ddpm_reverse_step(x1, 1, eps, betas, np.array([100.0, 100.0]))
    expected = (x1 - betas[0] / np.sqrt(1 - abar[0]) * eps) / np.sqrt(alphas[0])
    assert np.allclose(out, expected)
```
:::
