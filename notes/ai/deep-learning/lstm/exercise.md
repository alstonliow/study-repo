::: {#prob-lstm-step-code .problem .coding origin="self" source="res-stanford-cs231n-notes-recurrent-networks" packages="numpy"}
Write `lstm_step(x, h_prev, c_prev, Wx, Wh, b)`, one step of the LSTM of @def-lstm in row-vector form: $\mathbf a=\mathbf xW_x+\mathbf h_{t-1}W_h+\mathbf b$ with `Wx` of shape `(D, 4M)`, `Wh` of shape `(M, 4M)` and `b` of shape `(4M,)`. Split $\mathbf a$ into four consecutive blocks of length $M$, in the order input, forget, output gate, candidate. `x` may be a single vector `(D,)` or a batch `(N, D)` (then `h_prev`, `c_prev` are `(N, M)`). Return `(h, c)`.

```{.python .starter}
import numpy as np


def lstm_step(x, h_prev, c_prev, Wx, Wh, b):
    """One LSTM step; returns (h, c)."""
    ...
```

```{.python .tests}
import numpy as np


def sig(z):
    return 1 / (1 + np.exp(-z))


def test_gates_by_hand():
    # M = 1, D = 1: a = (0, 3, 0, 0.5) for x = 1, h_prev = 0
    Wx = np.array([[0.0, 3.0, 0.0, 0.5]])
    h, c = lstm_step(np.array([1.0]), np.zeros(1), np.array([2.0]), Wx, np.zeros((1, 4)), np.zeros(4))
    c_exp = sig(3.0) * 2.0 + 0.5 * np.tanh(0.5)
    assert np.allclose(c, [c_exp])
    assert np.allclose(h, [0.5 * np.tanh(c_exp)])


def test_batch_matches_single():
    rng = np.random.default_rng(7)
    N, D, M = 3, 2, 4
    x, h, c = rng.normal(size=(N, D)), rng.normal(size=(N, M)), rng.normal(size=(N, M))
    Wx, Wh, b = rng.normal(size=(D, 4 * M)), rng.normal(size=(M, 4 * M)), rng.normal(size=4 * M)
    H, C = lstm_step(x, h, c, Wx, Wh, b)
    assert H.shape == (N, M)
    h1, c1 = lstm_step(x[1], h[1], c[1], Wx, Wh, b)
    assert np.allclose(H[1], h1) and np.allclose(C[1], c1)


def test_forget_gate_closed_and_input_open():
    # huge negative forget bias, huge positive input bias: the cell becomes the candidate
    b = np.array([50.0, -50.0, 50.0, 0.0])
    h, c = lstm_step(np.array([0.3]), np.zeros(1), np.array([9.0]), np.array([[0.0, 0.0, 0.0, 1.0]]), np.zeros((1, 4)), b)
    assert np.allclose(c, np.tanh(0.3))
```
:::
