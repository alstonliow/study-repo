<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-4-q6" status="draft"}
**(a)**

1. With logits $z=\theta^\top\phi(s)$, $\log\pi_\theta(a\mid s)=z_a-\log\sum_{a'}e^{z_{a'}}$.
2. Its gradient with respect to the logits is $\nabla_z\log\pi_\theta(a\mid s)=e_a-\pi_\theta(\cdot\mid s)$ (the negative of the cross-entropy gradient $p-y$).
3. Chain rule: $z_{a'}=\sum_j\theta_{ja'}\phi_j(s)$, so $\partial z_{a'}/\partial\theta_{ja'}=\phi_j(s)$ and $z_{a'}$ does not depend on other columns.
4. Hence, as a $d\times 3$ matrix,
$$\nabla_\theta\log\pi_\theta(a\mid s)=\phi(s)\,\big(e_a-\pi_\theta(\cdot\mid s)\big)^\top.$$

**(b)** At $\theta=0$ the policy is uniform, so $\nabla_\theta\log\pi_\theta(\text{right})=e_2-(\tfrac13,\tfrac13,\tfrac13)=(-\tfrac13,-\tfrac13,\tfrac23)$. The episode's utility is $-1$.

1. No baseline: the weight is $\text{utility}-b=-1$, so the update is
$$\eta\,(-1)\,(-\tfrac13,-\tfrac13,\tfrac23)=\eta\,(\tfrac13,\tfrac13,-\tfrac23).$$
$\theta_2$ drops, so the car is **less** likely to accelerate right, even though it took the best action.
2. Baseline $b=-2$: the weight is $-1-(-2)=+1$, so the update is
$$\eta\,(-\tfrac13,-\tfrac13,\tfrac23),$$
and the car is **more** likely to accelerate right. All rewards are negative, so without a baseline every sampled action is pushed down; the good action is only pushed down less than bad ones would be, which shows up only on average over many episodes. The baseline measures the reward against the policy's expected reward, so an action better than average gets a positive weight in every single update.
:::

::: {.solution for="prob-bootstrapped-policy-gradient-code" status="draft"}
```{.python}
import numpy as np


def bootstrapped_update(theta, phi, rollout, V, gamma, eta):
    """Policy gradient step weighted by the bootstrapped advantage of each step."""
    step = np.zeros_like(theta, dtype=float)
    for i, (s, a, r, t, end) in enumerate(rollout):
        adv = r + (0.0 if end else gamma * V(t)) - V(s)
        f = phi(s)
        z = theta @ f
        p = np.exp(z - z.max())
        p /= p.sum()
        p[a] -= 1.0                            # p - e_a
        step += gamma ** i * adv * np.outer(-p, f)
    return theta + eta * step
```

1. The gradient of $\log\pi_\theta(a\mid s)$ is the outer product of $\mathbf e_a-\boldsymbol\pi$ with $\boldsymbol\phi(s)$, as for REINFORCE.
2. Each step gets its own weight $\gamma^i\hat A_i$ instead of the shared utility $u(\tau)$. Since $r_i+\gamma\hat V(t_i)$ estimates $Q(s_i,a_i)$ and $\hat V(s_i)$ acts as a baseline, the weight says how much better $a_i$ turned out than the critic expected.
3. If the critic satisfies $r_i+\gamma\hat V(t_i)=\hat V(s_i)$ on every step, every advantage is $0$ and the policy does not move, as the last test checks; with REINFORCE the same rollout would still move it.
:::
