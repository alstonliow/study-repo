::: {#prob-causal-attention-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-machinelearning" solution="withheld" packages="numpy"}
Implement self-attention with a causal mask (@def-self-attention) in NumPy as `causal_self_attention(X, WQ, WK, WV)`.

- `X` has shape `(n, d)`, one row per position; `WQ` and `WK` have shape `(d, dk)` and `WV` shape `(d, dv)`.
- Scale the scores by $1/\sqrt{d_k}$, mask every score of a position $j>i$ before the row-wise softmax, and return the output of shape `(n, dv)`.
- Compute the softmax stably: large scores must not give `nan` or `inf`.

```{.python .starter}
import numpy as np


def causal_self_attention(X, WQ, WK, WV):
    """softmax(mask(Q K^T / sqrt(dk))) V with a causal mask; shape (n, dv)."""
    ...
```

```{.python .tests}
import math
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(5, 4))
WQ, WK, WV = rng.normal(size=(4, 3)), rng.normal(size=(4, 3)), rng.normal(size=(4, 2))


def test_shape_and_first_row():
    out = causal_self_attention(X, WQ, WK, WV)
    assert out.shape == (5, 2)
    assert np.allclose(out[0], X[0] @ WV), "position 1 can attend only to itself"


def test_zero_queries_average_the_prefix():
    out = causal_self_attention(X, np.zeros((4, 3)), WK, WV)
    V = X @ WV
    for i in range(5):
        assert np.allclose(out[i], V[: i + 1].mean(axis=0))


def test_future_does_not_leak():
    out = causal_self_attention(X, WQ, WK, WV)
    Y = X.copy()
    Y[3:] = rng.normal(size=(2, 4))
    out2 = causal_self_attention(Y, WQ, WK, WV)
    assert np.allclose(out[:3], out2[:3]) and not np.allclose(out[3:], out2[3:])


def test_two_positions_by_hand():
    I = np.eye(2)
    out = causal_self_attention(I, I, I, I)
    # row 2: scores q2.k1 = 0 and q2.k2 = 1, each divided by sqrt(2)
    a = math.exp(1 / math.sqrt(2))
    assert np.allclose(out[1], [1 / (1 + a), a / (1 + a)])


def test_large_scores_are_stable():
    out = causal_self_attention(1000 * X, WQ, WK, WV)
    assert np.all(np.isfinite(out))
```
:::

::: {.problem #prob-cs231na-3-q1 origin="external" source="cs231na-3-q1"}
Several key design decisions were made in designing the scaled dot product attention we introduced above. Explain why the following choices were beneficial:
1. Using multiple attention heads as opposed to one.
2. Dividing by $\sqrt{d/h}$ before applying the softmax function. Recall that $d$ is the feature dimension and $h$ is the number of heads.
3. Adding a linear transformation to the output of the attention operation.

Only one or two sentences per choice is necessary, but be sure to be specific in addressing what would have happened without each given implementation detail, why such a situation would be suboptimal, and how the proposed implementation improves the situation.
:::
