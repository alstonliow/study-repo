::: {.problem #prob-cs231na-2-q7 origin="external" source="cs231na-2-q7"}
In our current image captioning setup, our RNN language model produces a word at every timestep as its output. However, an alternate way to pose the problem is to train the network to operate over _characters_ (e.g. 'a', 'b', etc.) as opposed to words, so that at it every timestep, it receives the previous character as input and tries to predict the next character in the sequence. For example, the network might generate a caption like

'A', ' ', 'c', 'a', 't', ' ', 'o', 'n', ' ', 'a', ' ', 'b', 'e', 'd'

Can you describe one advantage of an image-captioning model that uses a character-level RNN? Can you also describe one disadvantage? HINT: there are several valid answers, but it might be useful to compare the parameter space of word-level and character-level models.
:::

::: {#prob-rnn-bptt-code .problem .coding origin="adapted" source="res-stanford-cs231n-assignments-ps2" packages="numpy"}
Write `rnn_bptt(x, h0, Wx, Wh, b, dh)` for a vanilla RNN in row-vector form, $\mathbf h_t=\tanh(\mathbf x_tW_x+\mathbf h_{t-1}W_h+\mathbf b)$ (@def-vanilla-rnn), on one sequence.

- `x` has shape `(T, D)`, `h0` shape `(M,)`, `Wx` shape `(D, M)`, `Wh` shape `(M, M)`, `b` shape `(M,)`.
- `dh` of shape `(T, M)` holds the gradient of the loss with respect to each $\mathbf h_t$ coming from the outputs only.
- Run the forward pass, then backpropagation through time (@def-bptt), and return `(dx, dh0, dWx, dWh, db)`.

```{.python .starter}
import numpy as np


def rnn_bptt(x, h0, Wx, Wh, b, dh):
    """Forward pass of a vanilla RNN, then gradients by backpropagation through time."""
    ...
```

```{.python .tests}
import numpy as np

rng = np.random.default_rng(6)
T, D, M = 4, 3, 2
x, h0 = rng.normal(size=(T, D)), rng.normal(size=M)
Wx, Wh, b = rng.normal(size=(D, M)), rng.normal(size=(M, M)) * 0.5, rng.normal(size=M)
dh = rng.normal(size=(T, M))


def loss(x_, h0_, Wx_, Wh_, b_):
    h, total = h0_, 0.0
    for t in range(T):
        h = np.tanh(x_[t] @ Wx_ + h @ Wh_ + b_)
        total += h @ dh[t]
    return total


def test_against_finite_differences():
    grads = rnn_bptt(x, h0, Wx, Wh, b, dh)
    args = [x, h0, Wx, Wh, b]
    for k, (arr, g) in enumerate(zip(args, grads)):
        num = np.zeros_like(arr)
        for idx in np.ndindex(arr.shape):
            p, m = [a.copy() for a in args], [a.copy() for a in args]
            p[k][idx] += 1e-6
            m[k][idx] -= 1e-6
            num[idx] = (loss(*p) - loss(*m)) / 2e-6
        assert g.shape == arr.shape
        assert np.allclose(g, num, atol=1e-6)


def test_scalar_example_from_the_note():
    # W_hh = 0.5, W_xh = 1, inputs 1, 0, 0, 0; gradient only on h_4
    d = np.zeros((4, 1)); d[3] = 1.0
    out = rnn_bptt(np.array([[1.0], [0.0], [0.0], [0.0]]), np.zeros(1), np.eye(1), 0.5 * np.eye(1), np.zeros(1), d)
    dx = out[0]
    h1 = np.tanh(1.0)
    assert np.isclose(dx[0, 0] / (1 - h1**2), 0.104, atol=1e-3)
```
:::
