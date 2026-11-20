::: {.problem #prob-cs221hw-4-q4 origin="external" source="cs221hw-4-q4"}
In the previous question, we've seen how value iteration can take an MDP which describes the full dynamics of the game and return an optimal policy, and we've also seen how model-based value iteration with Monte Carlo simulation can estimate MDP dynamics if unknown at first and then learn the respective optimal policy. But suppose you are trying to control a complex system in the real world where trying to explicitly model all possible transitions and rewards is intractable. We will see how model-free reinforcement learning can nevertheless find the optimal policy.

(e) Despite its worse performance on this problem, why could the function approximation Q-learning outperform the tabular Q-learning in some other environments? Consider the situations where the exploration period is limited, where the state space is very high dimensional and difficult to explore, and/or you have space constraints.

*Expected:* 2-3 sentences discussing why `FunctionApproxQLearning` can be better in various scenarios.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-fourier-features-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-mountaincar" packages="numpy"}
Continuous states need features before linear function approximation (@def-q-function-approximation) applies. Write `fourier_features(s, order, low, high)`, the Fourier basis of a state.

- `s`, `low` and `high` are arrays of shape `(k,)`, with `low <= s <= high`. First rescale the state to $\tilde{\mathbf s}=(\mathbf s-\text{low})/(\text{high}-\text{low})\in[0,1]^k$.
- For every integer vector $\mathbf c\in\{0,1,\dots,\text{order}\}^k$ there is one feature, $\cos(\pi\,\mathbf c\cdot\tilde{\mathbf s})$.
- Return the array of the $(\text{order}+1)^k$ features, with the vectors $\mathbf c$ in lexicographic order, as `itertools.product(range(order + 1), repeat=k)` lists them.

```{.python .starter}
import itertools
import numpy as np


def fourier_features(s, order, low, high):
    """Fourier basis features cos(pi c . s_scaled) for all c in {0..order}^k."""
    ...
```

```{.python .tests}
import numpy as np


def test_one_dimension():
    phi = fourier_features(np.array([0.5]), 3, np.array([0.0]), np.array([1.0]))
    assert np.allclose(phi, [1.0, 0.0, -1.0, 0.0], atol=1e-12)


def test_two_dimensions_and_rescaling():
    low, high = np.array([-1.2, -0.07]), np.array([0.6, 0.07])
    s = np.array([-0.3, 0.0])                  # rescaled: (0.5, 0.5)
    phi = fourier_features(s, 1, low, high)
    # c = (0,0), (0,1), (1,0), (1,1)
    assert np.allclose(phi, [1.0, 0.0, 0.0, -1.0], atol=1e-12)


def test_length_and_constant_feature():
    rng = np.random.default_rng(5)
    s = rng.uniform(size=3)
    phi = fourier_features(s, 2, np.zeros(3), np.ones(3))
    assert phi.shape == (27,) and np.isclose(phi[0], 1.0)
    assert np.all(np.abs(phi) <= 1)
    assert np.isclose(phi[-1], np.cos(np.pi * 2 * s.sum()))


def test_corners():
    phi = fourier_features(np.array([0.0, 1.0]), 2, np.zeros(2), np.ones(2))
    assert np.allclose(phi, [1, -1, 1, 1, -1, 1, 1, -1, 1])
```
:::

::: {#prob-linear-q-learning-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-mountaincar" packages="numpy"}
Implement one step of Q-learning with a linear function approximator (@def-q-function-approximation). Write `linear_q_update(theta, phi, s, a, r, t, end, actions, gamma, eta)`.

- `phi(s, a)` returns the feature vector $\boldsymbol\phi(s,a)$, an array of the shape of `theta`, and $Q_\theta(s,a)=\theta\cdot\boldsymbol\phi(s,a)$.
- $(s,a,r,t)$ is one transition, `end` says whether $t$ is an end state, and `actions` lists the actions available in $t$.
- Return the new parameter vector after one gradient step of size `eta` on the squared error to the Q-learning target, the target treated as a constant. Do not change `theta`.

```{.python .starter}
import numpy as np


def linear_q_update(theta, phi, s, a, r, t, end, actions, gamma, eta):
    """One Q-learning step for Q(s, a) = theta . phi(s, a); return the new theta."""
    ...
```

```{.python .tests}
import numpy as np


def phi2(s, a):
    # two actions, two state features each; the block of action a holds the state
    v = np.zeros(4)
    v[2 * a:2 * a + 2] = s
    return v


def test_hand_step():
    theta = np.array([1.0, 0.0, 0.0, 2.0])
    s, t = np.array([1.0, 1.0]), np.array([0.0, 1.0])
    # Q(s, 0) = 1; max over t is Q(t, 1) = 2; target 0.5 + 0.5 * 2 = 1.5
    new = linear_q_update(theta, phi2, s, 0, 0.5, t, False, [0, 1], 0.5, 0.1)
    assert np.allclose(new, [1.05, 0.05, 0.0, 2.0])
    assert np.allclose(theta, [1.0, 0.0, 0.0, 2.0]), "theta was modified"


def test_end_state_target_is_reward():
    theta = np.array([0.0, 0.0, 10.0, 10.0])
    s, t = np.array([1.0, 0.0]), np.array([1.0, 1.0])
    new = linear_q_update(theta, phi2, s, 0, 3.0, t, True, [0, 1], 0.9, 0.5)
    assert np.allclose(new, [1.5, 0.0, 10.0, 10.0])


def test_indicator_features_give_tabular_q_learning():
    S, A, gamma, eta = 3, 2, 0.9, 0.3
    onehot = lambda s, a: np.eye(S * A)[s * A + a]
    rng = np.random.default_rng(6)
    theta, Q = np.zeros(S * A), np.zeros((S, A))
    for _ in range(100):
        s, a, t = int(rng.integers(S)), int(rng.integers(A)), int(rng.integers(S))
        r, end = float(rng.normal()), bool(t == 2)
        theta = linear_q_update(theta, onehot, s, a, r, t, end, list(range(A)), gamma, eta)
        target = r if end else r + gamma * Q[t].max()
        Q[s, a] += eta * (target - Q[s, a])
    assert np.allclose(theta.reshape(S, A), Q)
```
:::
