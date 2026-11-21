::: {.problem #prob-cs231na-1-q12 origin="external" source="cs231na-1-q12"}
AdaGrad, like Adam, is a per-parameter optimization method that uses the following update rule:

```
cache += dw**2
w += - learning_rate * dw / (np.sqrt(cache) + eps)
```

John notices that when he was training a network with AdaGrad that the updates became very small, and that his network was learning slowly. Using your knowledge of the AdaGrad update rule, why do you think the updates would become very small? Would Adam have the same issue?
:::

::: {#prob-adam-update-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps1" packages="numpy"}
Write `adam_update(w, g, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8)`, one step of Adam (@def-adam) at step number `t` (starting at $1$). The arrays `w`, `g` (the gradient), `m` and `v` have the same shape; return the new `(w, m, v)` without changing the arguments in place.

```{.python .starter}
import numpy as np


def adam_update(w, g, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """One Adam step; returns the new (w, m, v)."""
    ...
```

```{.python .tests}
import numpy as np


def test_constant_gradient_moves_by_lr():
    w, m, v = np.array([1.0, -2.0]), np.zeros(2), np.zeros(2)
    g = np.array([0.5, -3.0])
    for t in range(1, 4):
        w_new, m, v = adam_update(w, g, m, v, t, lr=0.1, eps=0.0)
        assert np.allclose(w_new - w, [-0.1, 0.1])
        w = w_new
    assert np.allclose(m, (1 - 0.9**3) * g)


def test_first_step_by_hand():
    w, m, v = adam_update(np.array([0.0]), np.array([2.0]), np.zeros(1), np.zeros(1), 1, lr=1.0)
    assert np.allclose(m, [0.2]) and np.allclose(v, [0.004])
    assert np.allclose(w, [-2.0 / (2.0 + 1e-8)])


def test_inputs_unchanged():
    w, g, m, v = np.ones(3), np.ones(3), np.zeros(3), np.zeros(3)
    adam_update(w, g, m, v, 1)
    assert np.all(w == 1) and np.all(m == 0) and np.all(v == 0)
```
:::
