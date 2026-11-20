::: {#prob-model-based-estimate-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-mountaincar" packages="numpy"}
Estimate an MDP from experience as model-based reinforcement learning does (@def-model-based-rl). Write `estimate_mdp(transitions, S, A)`.

- `transitions` is a list of tuples `(s, a, r, t)`: in state `s` action `a` was taken, it paid reward `r` and led to state `t`. States are `0, ..., S-1` and actions `0, ..., A-1`.
- Return `(T_hat, R_hat)`, two float arrays of shape `(S, A, S)`: `T_hat[s, a, t]` is $N(s,a,t)/N(s,a)$, and `R_hat[s, a, t]` is the average reward observed on the move $(s,a,t)$.
- Entries for a pair `(s, a)` that was never tried, and rewards of moves never observed, are $0$.

```{.python .starter}
import numpy as np


def estimate_mdp(transitions, S, A):
    """Count-based estimates (T_hat, R_hat) of transitions and rewards."""
    ...
```

```{.python .tests}
import numpy as np


def test_counts_and_averages():
    data = [(0, 1, 2.0, 1), (0, 1, 4.0, 1), (0, 1, -3.0, 2), (1, 0, 5.0, 1)]
    T, R = estimate_mdp(data, 3, 2)
    assert T.shape == R.shape == (3, 2, 3)
    assert np.allclose(T[0, 1], [0, 2 / 3, 1 / 3])
    assert np.isclose(R[0, 1, 1], 3.0) and np.isclose(R[0, 1, 2], -3.0)
    assert np.allclose(T[1, 0], [0, 1, 0]) and np.isclose(R[1, 0, 1], 5.0)


def test_untried_pairs_are_zero():
    T, R = estimate_mdp([(0, 0, 1.0, 1)], 2, 2)
    assert np.all(T[0, 1] == 0) and np.all(T[1] == 0) and np.all(R[1] == 0)
    assert np.isclose(T.sum(), 1.0)


def test_rows_are_distributions():
    rng = np.random.default_rng(4)
    data = [(int(rng.integers(4)), int(rng.integers(2)), float(rng.normal()), int(rng.integers(4)))
            for _ in range(200)]
    T, R = estimate_mdp(data, 4, 2)
    tried = {(s, a) for s, a, _, _ in data}
    for s in range(4):
        for a in range(2):
            assert np.isclose(T[s, a].sum(), 1.0 if (s, a) in tried else 0.0)
    s, a, _, t = data[0]
    rewards = [r for s2, a2, r, t2 in data if (s2, a2, t2) == (s, a, t)]
    assert np.isclose(R[s, a, t], np.mean(rewards))


def test_no_data():
    T, R = estimate_mdp([], 2, 1)
    assert T.shape == (2, 1, 2) and not T.any() and not R.any()
```
:::
