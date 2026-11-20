<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-4-q2" status="draft"}
The chain on $\{0,\dots,k-1\}$ is a birth–death chain, so it is reversible (its transition graph is a path, so @thm-kolmogorov-criterion holds trivially) and detailed balance $\pi(i)p=\pi(i+1)q$ gives $\pi(i)=\rho^i\pi(0)$. Normalising:
$$\pi(i)=\frac{1-\rho}{1-\rho^k}\,\rho^i\quad(\rho\ne1),\qquad\pi(i)=\frac1k\quad(\rho=1),\qquad i=0,\dots,k-1.$$
It is unique because the chain is irreducible.
:::

::: {.solution for="prob-metropolis-hastings-code" status="draft"}
```{.python}
import math
import random


def metropolis_hastings(log_f, propose, log_q, x0, steps, rng):
    """Run the Metropolis-Hastings chain from x0 for `steps` steps and return the
    list of the states after each step. log_f(x) is log of an unnormalised target
    (may be -inf); propose(x, rng) draws a candidate y; log_q(x, y) is log of the
    probability of proposing y from x. Use rng.random() for the accept test."""
    x, lx = x0, log_f(x0)
    out = []
    for _ in range(steps):
        y = propose(x, rng)
        ly = log_f(y)
        if ly > -math.inf:
            log_a = ly + log_q(y, x) - lx - log_q(x, y)
            if log_a >= 0 or rng.random() < math.exp(log_a):
                x, lx = y, ly
        out.append(x)
    return out
```

1. Keep $\log f$ of the current state, so that each step evaluates $\log f$ once, at the candidate.
2. A candidate with $f(y)=0$ is never accepted. Otherwise the log of the acceptance ratio is $\log f(y)+\log q(y,x)-\log f(x)-\log q(x,y)$. A ratio of at least $1$ always accepts; otherwise accept when `rng.random()` is below its exponential.
3. Detailed balance: for $x\ne y$ the chain moves with probability $q(x,y)a(x,y)$, and $\pi(x)q(x,y)a(x,y)=\min\{\pi(x)q(x,y),\pi(y)q(y,x)\}$ is symmetric in $x$ and $y$. Without the factor $q(y,x)/q(x,y)$ the asymmetric test fails: the chain drifts in the direction the proposal favours.
:::
