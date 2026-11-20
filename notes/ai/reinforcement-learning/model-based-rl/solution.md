<!-- Solutions marked status="draft" were written by Claude in our own words,
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-model-based-estimate-code" status="draft"}
```{.python}
import numpy as np


def estimate_mdp(transitions, S, A):
    """Count-based estimates (T_hat, R_hat) of transitions and rewards."""
    N = np.zeros((S, A, S))                    # N(s, a, t)
    total = np.zeros((S, A, S))                # sum of rewards on (s, a, t)
    for s, a, r, t in transitions:
        N[s, a, t] += 1
        total[s, a, t] += r
    Nsa = N.sum(axis=2, keepdims=True)         # N(s, a)
    T_hat = np.divide(N, Nsa, out=np.zeros_like(N), where=Nsa > 0)
    R_hat = np.divide(total, N, out=np.zeros_like(N), where=N > 0)
    return T_hat, R_hat
```

1. One pass over the data fills two count arrays: how often each move $(s,a,t)$ happened, and the sum of its rewards.
2. $N(s,a)$ is the sum of $N(s,a,t)$ over $t$; dividing by it normalises each row into a distribution.
3. `np.divide(..., where=...)` divides only where the count is positive and leaves the zeros of `out` elsewhere, which covers untried pairs and unobserved moves without a warning about division by zero.
:::
