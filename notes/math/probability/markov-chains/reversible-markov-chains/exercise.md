::: {.problem #prob-eecs126hw-4-q2 origin="external" source="eecs126hw-4-q2"}
**Finite Random Walk.**

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (0) at (0,0) {$0$};
\node[small vertex] (1) at (1.6,0) {$1$};
\node[small vertex] (2) at (3.2,0) {$2$};
\node[lab] at (5.0,0) {$\cdots$};
\node[small vertex] (a) at (7.0,0) {$k-2$};
\node[small vertex] (b) at (8.6,0) {$k-1$};
\draw[->] (0) to[loop left] node[lab,tick,left] {$1-p$} (0);
\draw[->] (b) to[loop right] node[lab,tick,right] {$p$} (b);
\draw[->] (0) to[bend left=30] node[lab,tick,above] {$p$} (1);
\draw[->] (1) to[bend left=30] node[lab,tick,below] {$1-p$} (0);
\draw[->] (1) to[bend left=30] node[lab,tick,above] {$p$} (2);
\draw[->] (2) to[bend left=30] node[lab,tick,below] {$1-p$} (1);
\draw[->] (a) to[bend left=30] node[lab,tick,above] {$p$} (b);
\draw[->] (b) to[bend left=30] node[lab,tick,below] {$1-p$} (a);
\draw[->] (2) to[bend left=30] node[lab,tick,above] {$p$} (4.5,0.25);
\draw[->] (5.5,-0.25) to[bend left=30] node[lab,tick,below] {$1-p$} (2);
\draw[->] (5.5,0.25) to[bend left=30] node[lab,tick,above] {$p$} (a);
\draw[->] (a) to[bend left=30] node[lab,tick,below] {$1-p$} (4.5,-0.25);
\end{tikzpicture}
\end{center}
```

Assume $0<p<1$. Find the stationary distribution. Hint: Let $q=1-p$ and $\rho=\frac pq$, but be careful when $\rho=1$.
:::

::: {#prob-metropolis-hastings-code .problem .coding origin="adapted" source="res-ucb-eecs126-labs-mcmc"}
Let $f>0$ on a set of states be proportional to a target distribution $\pi$ whose normalising constant is unknown. Let $q(x,y)$ be a proposal: a distribution of candidates $y$ from each state $x$. From $x$, the *Metropolis–Hastings* chain draws $y\sim q(x,\cdot)$. It moves to $y$ with probability
$$a(x,y)=\min\Bigl\{1,\ \frac{f(y)\,q(y,x)}{f(x)\,q(x,y)}\Bigr\}$$
and otherwise stays at $x$. This chain satisfies detailed balance with $\pi$ (@def-detailed-balance), so $\pi$ is invariant (@thm-detailed-balance-invariant).

Write `metropolis_hastings(log_f, propose, log_q, x0, steps, rng)`. It runs the chain from `x0` and returns the list of the states after each of the `steps` steps. It is given $\log f$ (which may be $-\infty$ where $f=0$), a sampler `propose(x, rng)` and $\log q$. Work with logarithms to avoid overflow, and use `rng.random()` for the accept test. The tests compare the visit frequencies with $\pi$, also for a proposal that is not symmetric.

```{.python .starter}
import math
import random


def metropolis_hastings(log_f, propose, log_q, x0, steps, rng):
    """Run the Metropolis-Hastings chain from x0 for `steps` steps and return the
    list of the states after each step. log_f(x) is log of an unnormalised target
    (may be -inf); propose(x, rng) draws a candidate y; log_q(x, y) is log of the
    probability of proposing y from x. Use rng.random() for the accept test."""
    ...
```

```{.python .tests}
import math
import random
from collections import Counter

w = [1, 2, 3, 2, 1, 0]          # target on the cycle 0..5, proportional to w
target = [wi / sum(w) for wi in w]
log_f = lambda x: math.log(w[x]) if w[x] else -math.inf


def freqs(xs):
    c = Counter(xs)
    return [c[i] / len(xs) for i in range(len(w))]


def test_symmetric_proposal():
    propose = lambda x, rng: (x + rng.choice([-1, 1])) % 6
    log_q = lambda x, y: math.log(0.5)
    xs = metropolis_hastings(log_f, propose, log_q, 2, 60_000, random.Random(0))
    assert len(xs) == 60_000
    assert all(abs(a - b) < 0.02 for a, b in zip(freqs(xs), target)), freqs(xs)


def test_asymmetric_proposal_needs_the_correction():
    # steps +1 with probability 0.8 and -1 with probability 0.2
    propose = lambda x, rng: (x + (1 if rng.random() < 0.8 else -1)) % 6
    log_q = lambda x, y: math.log(0.8 if y == (x + 1) % 6 else 0.2)
    xs = metropolis_hastings(log_f, propose, log_q, 0, 80_000, random.Random(1))
    assert all(abs(a - b) < 0.02 for a, b in zip(freqs(xs), target)), freqs(xs)


def test_never_enters_zero_probability():
    propose = lambda x, rng: (x + rng.choice([-1, 1])) % 6
    xs = metropolis_hastings(log_f, propose, lambda x, y: 0.0, 0, 5_000, random.Random(2))
    assert 5 not in xs


def test_zero_steps():
    assert metropolis_hastings(log_f, None, None, 3, 0, random.Random(3)) == []
```
:::

::: {.problem #prob-eecs126-4-q1 origin="external" source="eecs126-4-q1"}
Consider an irreducible Markov chain on the finite state space $\mathcal X$ with transition probability matrix $P$.

1. Suppose that $\tilde P$ is another transition probability matrix of the same dimensions as $P$ (the rows sum to 1). Show that if $\pi$ is a probability distribution on $\mathcal X$ which satisfies $\pi(x)P(x,y)=\pi(y)\tilde P(y,x)$ for all $x,y\in\mathcal X$, then $\pi$ is the stationary distribution and $\tilde P$ is the transition probability matrix of the reversed chain.

2. In particular, if $\pi$ satisfies the detailed balance equations (1), then $\pi$ is the stationary distribution.

*Note (these notes):* Equations (1) are the detailed balance equations of @def-detailed-balance. The *reversed chain* of a chain started from its stationary distribution $\pi$ has transition probabilities $P(X_n=x\mid X_{n+1}=y)$.
:::

::: {.problem #prob-eecs126-4-q2 origin="external" source="eecs126-4-q2"}
The graph associated with a Markov chain is formed by taking the transition diagram of the chain, forgetting the directions of all of the edges, removing multiple edges, and removing self-loops. If the graph of a finite-state irreducible Markov chain is a tree, then the stationary distribution of the Markov chain satisfies detailed balance.
:::
