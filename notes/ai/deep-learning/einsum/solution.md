<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-1-q1" status="draft"}
**(a)** $C=AB$ has $mp$ entries and each, $C_{ij}=\sum_{k=1}^{n}A_{ik}B_{kj}$, costs $n$ multiplications and $n-1$ additions. The total is $\Theta(mnp)$, so $O(mnp)$.

**(b)** In `einops` notation each axis is named; an axis that appears in the inputs but not in the output is summed over.

1. $X\mathbf w$: `'n d, d -> n'`. The output keeps $n$ and sums over $d$: entry $i$ is $\sum_{k} X_{ik}w_k$.
2. $XX^\top$: `'n d, m d -> n m'` (both operands are $X$; the second copy's row axis is renamed $m$ so it stays separate). Entry $(i,j)$ is $\sum_k X_{ik}X_{jk}$, the dot product of rows $i$ and $j$.
3. $\operatorname{diag}(X^\top X)$: `'n d, n d -> d'`. Both operands share $n$ and $d$; $d$ is kept and $n$ is summed, giving $\sum_i X_{id}^2$, the squared norm of column $d$, which is exactly the diagonal entry $(X^\top X)_{dd}$.
:::

::: {.solution for="prob-einsum-cosine-scores-code" status="draft"}
```{.python}
import numpy as np


def cosine_scores(A, C, causal=False):
    """Batched cosine similarities, shape (b, n, m); entries j > i are -inf if causal."""
    A = A / np.linalg.norm(A, axis=-1, keepdims=True)
    C = C / np.linalg.norm(C, axis=-1, keepdims=True)
    S = np.einsum("bnd,bmd->bnm", A, C)
    if causal:
        n = S.shape[-1]
        later = np.triu(np.ones((n, n), dtype=bool), k=1)
        S = np.where(later, -np.inf, S)
    return S
```

1. Dividing each vector by its norm first turns every inner product into a cosine, so one einsum does the rest.
2. In `"bnd,bmd->bnm"` the batch index `b` appears in both inputs and the output, so it is matched, not summed; `d` is missing from the output, so it is summed.
3. The mask `np.triu(..., k=1)` is true exactly where `j > i`; `np.where` broadcasts it over the batch.
:::
