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

::: {.solution for="prob-eecs126-4-q1" status="draft"}
1. *Stationarity.* For every $y$, $\sum_x\pi(x)P(x,y)=\sum_x\pi(y)\tilde P(y,x)=\pi(y)\sum_x\tilde P(y,x)=\pi(y)$, because the rows of $\tilde P$ sum to $1$. So $\pi P=\pi$. An irreducible chain on a finite space has exactly one stationary distribution, and it is positive everywhere, so $\pi$ is *the* stationary distribution and $\pi(y)>0$.

2. *The reversed chain.* Start the chain from $\pi$, so that $P(X_n=x)=\pi(x)$ for all $n$. Then $P(X_n=x\mid X_{n+1}=y)=\frac{P(X_n=x)P(x,y)}{P(X_{n+1}=y)}=\frac{\pi(x)P(x,y)}{\pi(y)}=\tilde P(y,x)$. By the Markov property, the past and the future are independent given the present, so the time-reversed process is again a Markov chain. Its transition matrix is $\tilde P$.

3. *Detailed balance.* If $\pi(x)P(x,y)=\pi(y)P(y,x)$ for all $x,y$, apply part 1 with $\tilde P=P$: $\pi$ is the stationary distribution (and the chain is its own reversal, which is @thm-detailed-balance-invariant).
:::

::: {.solution for="prob-eecs126-4-q2" status="draft"}
Let $\pi$ be the stationary distribution.

1. *Cut equations.* For any set $S$ of states, the flow out of $S$ equals the flow into $S$: $\sum_{u\in S,v\notin S}\pi(u)P(u,v)=\sum_{u\in S,v\notin S}\pi(v)P(v,u)$. Indeed, summing the balance equations $\pi(u)=\sum_v\pi(v)P(v,u)$ over $u\in S$ gives $\sum_{u\in S}\sum_v\pi(u)P(u,v)=\sum_{u\in S}\sum_v\pi(v)P(v,u)$ (the left side uses $\sum_vP(u,v)=1$). The terms with $v\in S$ are the same on both sides and cancel.

2. *Pairs that are not neighbours.* If $x\ne y$ are not joined in the graph, then $P(x,y)=P(y,x)=0$, and detailed balance $\pi(x)P(x,y)=\pi(y)P(y,x)$ holds trivially. For $x=y$ it is trivial too.

3. *Neighbours.* Let $\{x,y\}$ be an edge of the tree. Removing it splits the tree into two components; let $S$ be the one containing $x$. The only edge of the graph between $S$ and its complement is $\{x,y\}$. So the only transitions between $S$ and $S^c$ are $x\to y$ and $y\to x$, and the cut equation of step 1 reads $\pi(x)P(x,y)=\pi(y)P(y,x)$.

4. Steps 2 and 3 cover all pairs, so $\pi$ satisfies detailed balance.
:::
