::: {.problem #prob-cs221hw-4-q6 origin="external" source="cs221hw-4-q6"}
In Problem 3 we estimated the MDP, and in Problems 4 and 5 we estimated Q-values. In this problem we will estimate the policy *directly*, using REINFORCE from the [policy gradient lecture](https://stanford-cs221.github.io/lectures/?trace=policy_gradient). We will train a policy for Mountain Car, see why it needs a baseline, add bootstrapping, and compare the result with your Q-learning agents.

Our policy is a linear softmax over your Fourier features from 4b. With features $\phi(s) \in \mathbb{R}^d$ and a $d \times 3$ matrix $\theta$ (one column per action), the logits are $z = \theta^\top \phi(s)$ and $$\pi_\theta(a \mid s) = \frac{e^{z_a}}{\sum_{a'} e^{z_{a'}}}.$$ As in lecture, the utility of a rollout (one episode) $\tau = (s_0, a_1, r_1, s_1, \ldots, a_n, r_n, s_n)$ is $\text{utility}(\tau) = \sum_{t=1}^n \gamma^{t-1} r_t$ (what the plots call the discounted reward of an episode). After each rollout, REINFORCE with a baseline $b$ takes a gradient ascent step on the lecture's objective $$J(\theta, \tau) = \sum_{t=1}^n \log \pi_\theta(a_t \mid s_{t-1})\, \big(\text{utility}(\tau) - b\big).$$

(a) Before we can do gradient ascent on the policy, we need the gradient of $\log \pi_\theta(a \mid s)$ with respect to $\theta$. Derive it for our softmax policy; your answer should be a $d \times 3$ matrix.

*Hint: $\log \pi_\theta(a \mid s)$ is the negative of the cross-entropy loss from HW2 Problem 1d, with logits $z$ and label $a$.*

*Expected:* Your derivation, showing the gradient with respect to the logits and the chain rule through $z = \theta^\top \phi(s)$, and the final matrix written in terms of $\phi(s)$, $\pi_\theta(\cdot \mid s)$, and the one-hot vector $e_a$ for action $a$.

(b) Let's try the REINFORCE update on a tiny version of Mountain Car. Use our softmax policy with a single feature $\phi(s) = 1$, so $\theta = (\theta_0, \theta_1, \theta_2)$ is one logit per action (accelerate left, don't accelerate, accelerate right) and $\pi_\theta(a) = e^{\theta_a} / (e^{\theta_0} + e^{\theta_1} + e^{\theta_2})$. Each episode is a single step, with reward $-3$ for accelerating left, $-2$ for not accelerating, and $-1$ for accelerating right. Start at $\theta = (0, 0, 0)$, and suppose the car accelerates right, the best action.

i.  With no baseline ($b = 0$), compute the update $\eta\, \nabla_\theta J(\theta, \tau)$ to $\theta$, with step size $\eta > 0$. Is the car more or less likely to accelerate right next time?
ii. Now compute the update with the baseline $b = -2$, the expected reward under the current policy. Is the car now more or less likely to accelerate right, and why does the baseline change the answer?

*Expected:* For (i), the update in terms of $\eta$, with your work shown, and "more" or "less". For (ii), the same, and 1-2 sentences on why the baseline changes the answer.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-bootstrapped-policy-gradient-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-mountaincar" packages="numpy"}
Replace the utility of the whole rollout in a policy gradient step by the bootstrapped advantage of each step (@def-advantage, @def-actor-critic). The policy is the softmax policy with linear scores of @prob-reinforce-code: $\pi_\theta(a\mid s)\propto\exp(\boldsymbol\theta_a\cdot\boldsymbol\phi(s))$, with $\theta$ of shape `(A, d)`.

Write `bootstrapped_update(theta, phi, rollout, V, gamma, eta)`.

- `rollout` is a list of tuples `(s, a, r, t, end)`: step $i$ went from state $s_i$ with action $a_i$ and reward $r_i$ to state $t_i$, and `end` says whether $t_i$ is an end state.
- `V(s)` is a critic's value estimate $\hat V(s)$. The advantage estimate of step $i$ is $\hat A_i=r_i+\gamma\hat V(t_i)-\hat V(s_i)$, with $\hat V(t_i)$ replaced by $0$ if $t_i$ is an end state.
- Return the parameters after the step $\theta\gets\theta+\eta\sum_i\gamma^i\hat A_i\,\nabla_\theta\log\pi_\theta(a_i\mid s_i)$. Do not change `theta`.

```{.python .starter}
import numpy as np


def bootstrapped_update(theta, phi, rollout, V, gamma, eta):
    """Policy gradient step weighted by the bootstrapped advantage of each step."""
    ...
```

```{.python .tests}
import numpy as np

phi = lambda s: np.array([1.0, s])


def glp(theta, s, a):
    z = theta @ phi(s)
    p = np.exp(z - z.max())
    p /= p.sum()
    return np.outer(np.eye(len(p))[a] - p, phi(s))


def test_hand_step():
    theta = np.zeros((2, 2))
    V = lambda s: 2.0 * s
    rollout = [(1.0, 1, 1.0, 2.0, False)]      # A = 1 + 0.5 * 4 - 2 = 1
    new = bootstrapped_update(theta, phi, rollout, V, 0.5, 1.0)
    assert np.allclose(new, [[-0.5, -0.5], [0.5, 0.5]])
    assert not theta.any(), "theta was modified"


def test_weights_and_end_state():
    rng = np.random.default_rng(8)
    theta = rng.normal(size=(3, 2))
    V = lambda s: s * s
    rollout = [(0.5, 2, 1.0, -1.0, False), (-1.0, 0, 0.0, 2.0, False), (2.0, 1, 3.0, 9.0, True)]
    gamma, eta = 0.9, 0.05
    adv = [1.0 + 0.9 * 1.0 - 0.25, 0.0 + 0.9 * 4.0 - 1.0, 3.0 - 4.0]
    expected = theta + eta * sum(gamma ** i * A * glp(theta, s, a)
                                 for i, (A, (s, a, _, _, _)) in enumerate(zip(adv, rollout)))
    assert np.allclose(bootstrapped_update(theta, phi, rollout, V, gamma, eta), expected)


def test_consistent_critic_gives_no_update():
    # if r + gamma V(t) = V(s) at every step, every advantage is 0
    V = lambda s: 10.0 - s
    rollout = [(0.0, 0, 1.0, 1.0, False), (1.0, 1, 1.0, 2.0, False)]
    theta = np.ones((2, 2))
    assert np.allclose(bootstrapped_update(theta, phi, rollout, V, 1.0, 1.0), theta)
```
:::
