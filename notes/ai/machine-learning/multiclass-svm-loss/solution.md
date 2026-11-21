<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-1-q7" status="draft"}
**Answer:** True.

1. Take a new example $(\mathbf{x},y)$ whose scores under the current $W$ satisfy every margin: $s_y-s_j\ge\Delta$ for all $j\ne y$, with $\Delta=1$ say. Such an example exists, for instance a large multiple of a training input that is already classified with margin, so that all score differences are scaled up.
2. Its SVM loss is $\sum_{j\ne y}\max(0,s_j-s_y+\Delta)=0$ (@def-multiclass-svm-loss), so the total SVM loss is unchanged.
3. Its cross entropy loss is $-\log\operatorname{softmax}(\mathbf{s})_y$, which is positive because every class has positive softmax probability, so the total softmax loss increases (@sec-ai-machine-learning-multiclass-svm-loss).
:::

::: {.solution for="prob-multiclass-svm-loss-code" status="draft"}
```{.python}
import numpy as np


def svm_loss_grad(W, X, y, reg, delta=1.0):
    """Average multiclass hinge loss plus L2 penalty, and its gradient."""
    N = X.shape[0]
    S = X @ W
    correct = S[np.arange(N), y][:, None]
    margins = np.maximum(0.0, S - correct + delta)
    margins[np.arange(N), y] = 0.0
    loss = margins.sum() / N + reg * np.sum(W**2)
    G = (margins > 0).astype(float)
    G[np.arange(N), y] = -G.sum(axis=1)
    dW = X.T @ G / N + 2 * reg * W
    return loss, dW
```

1. `G` holds $\partial L_i/\partial s_{ij}$: $1$ for every violated margin and minus their number in the correct column (@thm-multiclass-svm-gradient).
2. The scores are $S=XW$, so by @prp-matrix-product-gradient the data gradient is $X^{\mathsf T}G/N$; the penalty adds $2\lambda W$.
:::
