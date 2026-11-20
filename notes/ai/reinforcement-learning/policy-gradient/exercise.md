::: {#prob-reinforce-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-mountaincar" packages="numpy"}
Implement the REINFORCE update (@def-reinforce) for a softmax policy with linear scores (@def-stochastic-policy):
$$\pi_\theta(a\mid s)=\frac{\exp(\boldsymbol\theta_a\cdot\boldsymbol\phi(s))}{\sum_{b}\exp(\boldsymbol\theta_b\cdot\boldsymbol\phi(s))},$$
where $\boldsymbol\theta_a$ is row $a$ of the parameter matrix $\theta$ of shape `(A, d)` and `phi(s)` returns $\boldsymbol\phi(s)$ of shape `(d,)`.

Write `reinforce_update(theta, phi, rollout, gamma, eta)`. `rollout` is a list of triples `(s, a, r)`: in state `s` the policy took action `a` and received reward `r`. With the utility $u(\tau)=\sum_t\gamma^t r_t$, return the parameters after one REINFORCE step of size `eta`. Do not change `theta`.

```{.python .starter}
import numpy as np


def reinforce_update(theta, phi, rollout, gamma, eta):
    """One REINFORCE step for a softmax policy with scores theta @ phi(s)."""
    ...
```

```{.python .tests}
import numpy as np

phi = lambda s: np.array([1.0, s])


def log_lik(theta, rollout):
    total = 0.0
    for s, a, _ in rollout:
        z = theta @ phi(s)
        total += z[a] - np.log(np.sum(np.exp(z)))
    return total


def num_grad(f, x, h=1e-6):
    g = np.zeros_like(x)
    for i in np.ndindex(x.shape):
        e = np.zeros_like(x)
        e[i] = h
        g[i] = (f(x + e) - f(x - e)) / (2 * h)
    return g


def test_matches_gradient_of_log_likelihood():
    rng = np.random.default_rng(7)
    theta = rng.normal(size=(3, 2))
    rollout = [(0.5, 2, 1.0), (-1.0, 0, 0.0), (2.0, 1, 3.0)]
    gamma, eta = 0.9, 0.1
    u = 1.0 + 0.9 * 0.0 + 0.81 * 3.0
    new = reinforce_update(theta, phi, rollout, gamma, eta)
    assert new.shape == theta.shape
    expected = theta + eta * u * num_grad(lambda th: log_lik(th, rollout), theta)
    assert np.allclose(new, expected, atol=1e-6)


def test_hand_step():
    theta = np.zeros((2, 2))
    # pi = (1/2, 1/2); grad log pi(1 | s) has rows -phi/2 and +phi/2
    new = reinforce_update(theta, phi, [(1.0, 1, 4.0)], 1.0, 0.5)
    assert np.allclose(new, [[-1.0, -1.0], [1.0, 1.0]])
    assert not theta.any(), "theta was modified"


def test_zero_utility_changes_nothing():
    theta = np.ones((2, 2))
    assert np.allclose(reinforce_update(theta, phi, [(0.3, 0, 0.0), (0.1, 1, 0.0)], 0.9, 1.0), theta)


def test_rewarded_action_becomes_likelier():
    theta = np.zeros((2, 2))
    new = reinforce_update(theta, phi, [(0.0, 1, 1.0)], 1.0, 0.1)
    z = new @ phi(0.0)
    assert z[1] > z[0]
```
:::
