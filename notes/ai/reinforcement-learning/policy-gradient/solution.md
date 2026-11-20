<!-- Solutions marked status="draft" were written by Claude in our own words,
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-reinforce-code" status="draft"}
```{.python}
import numpy as np


def grad_log_pi(theta, f, a):
    """Gradient of log pi(a | s) with respect to theta, where f = phi(s)."""
    z = theta @ f
    p = np.exp(z - z.max())
    p /= p.sum()
    onehot = np.zeros(len(p))
    onehot[a] = 1.0
    return np.outer(onehot - p, f)


def reinforce_update(theta, phi, rollout, gamma, eta):
    """One REINFORCE step for a softmax policy with scores theta @ phi(s)."""
    u = sum(gamma ** t * r for t, (_, _, r) in enumerate(rollout))
    g = sum(grad_log_pi(theta, phi(s), a) for s, a, _ in rollout)
    return theta + eta * u * g
```

1. $\log\pi_\theta(a\mid s)=\boldsymbol\theta_a\cdot\boldsymbol\phi(s)-\log\sum_b\exp(\boldsymbol\theta_b\cdot\boldsymbol\phi(s))$. Differentiating with respect to row $\boldsymbol\theta_b$ gives $(\mathbf 1[b=a]-\pi_\theta(b\mid s))\,\boldsymbol\phi(s)$: the first term only for the action taken, the second from the log-sum-exp.
2. Stacking the rows, the gradient is the outer product of $\mathbf e_a-\boldsymbol\pi$ with $\boldsymbol\phi(s)$, as in `grad_log_pi`.
3. The whole rollout shares one weight, its utility $u(\tau)$; the step is gradient *ascent*, so `+`.
:::
