<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-4-q4" status="draft"}
Tabular Q-learning learns each discretised state separately, so it needs every relevant state visited many times, and its table grows exponentially with the dimension of the state. Function approximation shares parameters between similar states, so an update in one state also improves the estimates of nearby, never-visited states. This matters when exploration is limited (few episodes, or exploration that is costly), when the state space is high-dimensional and most states are never seen, and when memory is limited, since the number of weights is fixed by the feature map rather than by the number of states.
:::

::: {.solution for="prob-fourier-features-code" status="draft"}
```{.python}
import itertools
import numpy as np


def fourier_features(s, order, low, high):
    """Fourier basis features cos(pi c . s_scaled) for all c in {0..order}^k."""
    x = (np.asarray(s, dtype=float) - low) / (high - low)
    C = np.array(list(itertools.product(range(order + 1), repeat=len(x))))
    return np.cos(np.pi * C @ x)
```

1. The rows of `C` are the vectors $\mathbf c$ in the required order, so `C @ x` holds all the inner products $\mathbf c\cdot\tilde{\mathbf s}$ at once.
2. The feature for $\mathbf c=\mathbf 0$ is the constant $1$, which plays the role of a bias. Larger entries of $\mathbf c$ give faster oscillations, so a higher order lets a linear $Q_\theta$ represent finer detail; the number of features grows as $(\text{order}+1)^k$.
3. Rescaling to $[0,1]$ first makes every state variable count equally, whatever its units (in mountain car, the position ranges over about $1.8$ and the velocity over $0.14$).
:::

::: {.solution for="prob-linear-q-learning-code" status="draft"}
```{.python}
import numpy as np


def linear_q_update(theta, phi, s, a, r, t, end, actions, gamma, eta):
    """One Q-learning step for Q(s, a) = theta . phi(s, a); return the new theta."""
    f = phi(s, a)
    target = r if end else r + gamma * max(theta @ phi(t, b) for b in actions)
    return theta - eta * (theta @ f - target) * f
```

1. The gradient of $Q_\theta(s,a)=\theta\cdot\boldsymbol\phi(s,a)$ with respect to $\theta$ is $\boldsymbol\phi(s,a)$, so the step on $\tfrac12(Q_\theta(s,a)-y)^2$ is $\theta-\eta\,(Q_\theta(s,a)-y)\,\boldsymbol\phi(s,a)$.
2. The target $y$ is computed from the current $\theta$ before the step and not differentiated.
3. Returning `theta - ...` builds a new array, so the caller's `theta` is unchanged.
4. With one indicator feature per state and action, $\theta$ is the Q-table and the step is exactly tabular Q-learning (@prp-indicator-features-tabular); the last test checks this.
:::
