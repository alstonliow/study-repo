::: {.problem #prob-cs221hw-1-q1 origin="external" source="cs221hw-1-q1"}
(a) **Linear Algebra Complexity:** Suppose you have two matrices $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$. What is the time complexity of computing their product $AB$ using the standard matrix multiplication algorithm? Express your answer using big-O notation and briefly justify why.

*Expected:* The time complexity in big-O notation and a 1-2 sentence explanation.

(b) **Einstein Summation (Written):** Given $X \in \mathbb R^{n\times d}$ and $\mathbf w \in \mathbb R^d$: (i) Write an `einsum` string for $X\mathbf w$; (ii) for the pairwise dot-product matrix $XX^\top$; (iii) for $\operatorname{diag}(X^\top X)$ (column-wise squared norms). For each string, briefly explain why it computes the requested quantity.

*Expected:* Use the `einops` format (e.g., `'n d, d m -> n m'`) rather than the `np.einsum` format (e.g., `'nd, dm -> nm'`).

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {#prob-einsum-cosine-scores-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-foundations" packages="numpy"}
Write `cosine_scores(A, C, causal=False)` with `np.einsum` (@def-einsum) and no Python loops.

- `A` has shape `(b, n, d)` and `C` has shape `(b, m, d)`: a batch of `b` pairs of sets of vectors in $\mathbb{R}^d$. No vector is zero.
- Return the array `S` of shape `(b, n, m)` whose entry `S[k, i, j]` is the cosine of the angle between `A[k, i]` and `C[k, j]`: their inner product divided by the product of their norms.
- If `causal` is true (then `n == m`), set every entry with `j > i` to `-np.inf`, so that position `i` only sees positions `0, ..., i`, as for the masked scores of a decoder.

```{.python .starter}
import numpy as np


def cosine_scores(A, C, causal=False):
    """Batched cosine similarities, shape (b, n, m); entries j > i are -inf if causal."""
    ...
```

```{.python .tests}
import numpy as np

rng = np.random.default_rng(0)


def slow(A, C):
    b, n, _ = A.shape
    m = C.shape[1]
    S = np.zeros((b, n, m))
    for k in range(b):
        for i in range(n):
            for j in range(m):
                S[k, i, j] = A[k, i] @ C[k, j] / (np.linalg.norm(A[k, i]) * np.linalg.norm(C[k, j]))
    return S


def test_small_example():
    A = np.array([[[1.0, 0.0], [1.0, 1.0]]])
    C = np.array([[[2.0, 0.0], [0.0, 3.0], [-1.0, 0.0]]])
    r = 1 / np.sqrt(2)
    expected = np.array([[[1.0, 0.0, -1.0], [r, r, -r]]])
    assert np.allclose(cosine_scores(A, C), expected)


def test_random_batch():
    A, C = rng.normal(size=(3, 4, 5)), rng.normal(size=(3, 6, 5))
    S = cosine_scores(A, C)
    assert S.shape == (3, 4, 6)
    assert np.allclose(S, slow(A, C))


def test_scale_invariant():
    A, C = rng.normal(size=(2, 3, 4)), rng.normal(size=(2, 3, 4))
    assert np.allclose(cosine_scores(5 * A, 0.1 * C), cosine_scores(A, C))


def test_causal_mask():
    A, C = rng.normal(size=(2, 4, 3)), rng.normal(size=(2, 4, 3))
    S = cosine_scores(A, C, causal=True)
    upper = np.triu(np.ones((4, 4), dtype=bool), k=1)
    assert np.all(np.isneginf(S[:, upper]))
    assert np.allclose(S[:, ~upper], slow(A, C)[:, ~upper])
```
:::
