::: {.problem #prob-cs221hw-4-q1 origin="external" source="cs221hw-4-q1"}
In this problem, you will perform value iteration updates manually on a basic game to build your intuitions about solving MDPs. In this MDP, we have that:

- The set of possible states in this game is $\text{States} = \{-2, -1, 0, +1, +2\}$.
- The set of possible actions is $\text{Actions}(s) = \{a_1, a_2\}$ for all states that are not end states.
- The starting state is $0$ and there are two end states, $-2$ and $+2$.

Recall that the transition function $T: \text{States} \times \text{Actions} \rightarrow \Delta\text{States}$ (distribution over states) encodes the probability of transitioning to a next state $s'$ after being in state $s$ and taking action $a$ as $T(s, a, s')$.

In this MDP, the transition dynamics are given as follows: $\forall i \in \{-1, 0, 1\} \subseteq \text{States}$,

- $T(i, a_1, i-1) = 0.8$ and $T(i, a_1, i+1) = 0.2$
- $T(i, a_2, i-1) = 0.7$ and $T(i, a_2, i+1) = 0.3$

Think of this MDP as a chain formed by states $\{-2, -1, 0, +1, +2\}$. In words, action $a_1$ has an 80% chance of moving the agent backwards in the chain and a 20% chance of moving the agent forward. Similarly, action $a_2$ has a 70% chance of sending the agent backwards and a 30% chance of moving the agent forward. We will use a discount factor $\gamma = 1$.

The reward function for this MDP is:

$$\text{Reward}(s,a,s') = \begin{cases} 10 & \text{if } s' = -2, \\ 50 & \text{if } s' = +2, \\ -5 & \text{otherwise}. \end{cases}$$

(a) What is the value of $V^*_i(s)$ for each $s \in \text{States}$ after each iteration $i \in \{1, 2\}$ of value iteration? Recall that $\forall s \in \text{States}$, $V^*_0(s) = 0$ and, for any $i$, end state $s_{\text{end}}$, we have $V^*_i(s_\text{end}) = 0$.

*Expected:* The $V^*_i(s)$ of all 5 states after each iteration $i = 1, 2$ (10 values in total), with your work shown: for each non-end state and each iteration, write out the expected value of each action (for example, $0.8 \cdot (\ldots) + 0.2 \cdot (\ldots)$) and which one is the max. We need to see this work to give partial credit, so don't report only the final values.

(b) Using $V^*_2(\cdot)$, what is the corresponding optimal policy $\pi^*$ for all non-end states?

*Expected:* For each non-end state, the expected value of $a_1$ and of $a_2$ computed using $V^*_2$ (written out as in 1a), and the resulting optimal action $\pi^*(s)$.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::

::: {.problem #prob-cs188hw-4-q1 origin="external" source="cs188hw-4-q1"}
**MDP.** Pacman is in the following grid, starting at state $H$. He can take any one of four actions: Up, Down, Left and Right. If he tries to take an action that would move him towards a wall, then he stays in place. For example, if he goes down from $H$, he will remain at $H$. $A$, $E$, and $F$ are exit states. From an exit state, there is **only** an Exit action available, which results in Pacman going to the terminal state and collecting the appropriate award shown in the diagram and listed below.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[hl cell] (0.0,0.0) rectangle (1.6,-1.0);
\node[lab, align=center] at (0.8,-0.5) {$A$\\$+125$};
\draw[cell frame] (1.6,0.0) rectangle (3.2,-1.0);
\node[lab, align=center] at (2.4000000000000004,-0.5) {$B$};
\draw[cell frame] (3.2,0.0) rectangle (4.800000000000001,-1.0);
\node[lab, align=center] at (4.0,-0.5) {$C$};
\draw[cell frame] (0.0,-1.0) rectangle (1.6,-2.0);
\node[lab, align=center] at (0.8,-1.5) {$D$};
\draw[hl cell] (1.6,-1.0) rectangle (3.2,-2.0);
\node[lab, align=center] at (2.4000000000000004,-1.5) {$E$\\$-25$};
\draw[hl cell] (3.2,-1.0) rectangle (4.800000000000001,-2.0);
\node[lab, align=center] at (4.0,-1.5) {$F$\\$+25$};
\draw[cell frame] (0.0,-2.0) rectangle (1.6,-3.0);
\node[lab, align=center] at (0.8,-2.5) {$G$};
\draw[cell frame] (1.6,-2.0) rectangle (3.2,-3.0);
\node[lab, align=center] at (2.4000000000000004,-2.5) {$H$};
\draw[cell frame] (3.2,-2.0) rectangle (4.800000000000001,-3.0);
\node[lab, align=center] at (4.0,-2.5) {$I$};
\end{tikzpicture}
\end{center}
```



For any exit state $s$ and action $a$:
$$
R(s,a=\text{Exit},s'=\text{Exit})=\begin{cases}125 & \text{if } s=A\\ -25 & \text{if } s=E\\ 25 & \text{if } s=F\\ 0 & \text{otherwise}\end{cases}
$$

Assume all actions are deterministic unless otherwise specified.

1. Fill in the optimal action(s) for $H$ when $\gamma=1$.

   Up Left Right
2. Fill in the optimal action(s) for $H$ when $\gamma=\frac{1}{5}$.

   Up Left Right
3. Fill in the optimal action(s) for $H$ when $\gamma=\frac{1}{10}$.

   Up Left Right

Assume for the next two parts only that the transition function for the MDP is deterministic for all transitions except the following:
$$
T(H,\text{Right},I)=p\qquad T(H,\text{Left},E)=p
$$
$$
T(H,\text{Right},E)=1-p\qquad T(H,\text{Left},G)=1-p
$$
What values of $p$ for the given discount factor $\gamma$ would ensure that Pacman strictly prefers taking action Right from $H$:

4. $\gamma=1$

   0 0.1 0.5 0.9 1 None of the above
5. $\gamma=\frac{1}{10}$

   0 0.1 0.5 0.9 1 None of the above

Consider the following new grid:

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[hl cell] (1.7,0.0) rectangle (3.4,-1.0);
\node[lab, align=center] at (2.55,-0.5) {$E$\\$-100$};
\draw[cell frame] (0.0,-1.0) rectangle (1.7,-2.0);
\node[lab, align=center] at (0.85,-1.5) {$A$\\$+0$};
\draw[cell frame] (1.7,-1.0) rectangle (3.4,-2.0);
\node[lab, align=center] at (2.55,-1.5) {$C$\\$+0$};
\draw[hl cell] (3.4,-1.0) rectangle (5.1,-2.0);
\node[lab, align=center] at (4.25,-1.5) {$F$\\$-50$};
\draw[cell frame] (0.0,-2.0) rectangle (1.7,-3.0);
\node[lab, align=center] at (0.85,-2.5) {$B$\\$-1$};
\draw[hl cell] (1.7,-2.0) rectangle (3.4,-3.0);
\node[lab, align=center] at (2.55,-2.5) {$D$\\$+100$};
\end{tikzpicture}
\end{center}
```



Here, $D$, $E$ and $F$ are exit states.

Pacman starts in state $A$. The reward for entering each state is reflected in the grid. Assume that discount factor $\gamma=1$.

6. Write the optimal values $V^*(s)$ for $s=A$ and $s=C$ and the optimal policy $\pi^*(s)$ for $s=A$.

   $V^*(A)=$ $V^*(C)=$ $\pi^*(A)=$ Up Down Left Right
7. Now, instead of Pacman, Pacbaby is travelling in this grid. Pacbaby has a more limited set of actions than Pacman and can never go left. Hence, Pacbaby has to choose between actions: Up, Down and Right.

   Pacman is rational, but Pacbaby is indecisive. If Pacbaby enters state $C$, Pacbaby finds the two best actions and randomly, with equal probability, chooses between the two. Let $\pi^*(s)$ represent the optimal policy for **Pacman**. Let $V(s)$ be the values under the policy where Pacbaby acts according to $\pi^*(s)$ for all $s\ne C$, and follows the indecisive policy when at state $C$. What are the values $V(s)$ for $s=A$ and $s=C$?

   $V(A)=$ $V(C)=$
8. Now Pacman knows that Pacbaby is going to be indecisive when at state $C$ and he decides to recompute the optimal policy for Pacbaby at all other states, anticipating his indecisiveness at $C$. What is Pacbaby's new policy $\pi(s)$ and new value $V(s)$ for $s=A$?

   $V(A)=$ $\pi(A)=$ Up Down Left Right

*Note (these notes):* Grids redrawn; highlighted squares are exit states.
:::

::: {#prob-value-iteration-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-mountaincar" packages="numpy"}
Implement value iteration (@def-value-iteration) for an MDP given by arrays. Write `value_iteration(T, R, end, gamma, tol=1e-10)`.

- States are `0, ..., S-1` and actions `0, ..., A-1`; every action is available in every state.
- `T[s, a, t]` is the probability of moving from `s` to `t` with action `a`, and `R[s, a, t]` the reward of that move; both arrays have shape `(S, A, S)`.
- `end` is a boolean array of shape `(S,)`: end states have value $0$.
- Iterate from $V^{(0)}=0$ until the largest change of a value is below `tol`. Return `(V, pi)`: the values, an array of shape `(S,)`, and the greedy policy, an integer array of shape `(S,)` (for end states any action). Among tied actions take the smallest.

```{.python .starter}
import numpy as np


def value_iteration(T, R, end, gamma, tol=1e-10):
    """Return (V, pi) for the MDP with transition array T and reward array R."""
    ...
```

```{.python .tests}
import itertools
import numpy as np


def number_line(n, p, left, right):
    """States 0..n-1 on a line; 0 and n-1 are end states. Action 0 tries to
    move left, action 1 right; it succeeds with probability p, else the move
    goes the other way. Entering 0 pays `left`, entering n-1 pays `right`,
    every other move costs 1."""
    T, R = np.zeros((n, 2, n)), np.full((n, 2, n), -1.0)
    R[:, :, 0], R[:, :, n - 1] = left, right
    for s in range(1, n - 1):
        T[s, 0, s - 1] += p
        T[s, 0, s + 1] += 1 - p
        T[s, 1, s + 1] += p
        T[s, 1, s - 1] += 1 - p
    end = np.zeros(n, dtype=bool)
    end[[0, n - 1]] = True
    return T, R, end


def best_by_brute_force(T, R, end, gamma):
    """Optimal values: evaluate every deterministic policy exactly."""
    S = len(end)
    best = np.full(S, -np.inf)
    for pi in itertools.product(range(T.shape[1]), repeat=S):
        P = np.array([T[s, pi[s]] for s in range(S)])
        r = np.array([P[s] @ R[s, pi[s]] for s in range(S)])
        P[end], r[end] = 0, 0
        best = np.maximum(best, np.linalg.solve(np.eye(S) - gamma * P, r))
    return best


def test_number_line():
    for p, left, right, gamma in [(0.8, 10, 50, 1.0), (0.7, 20, 5, 0.9), (1.0, 3, 30, 0.5)]:
        T, R, end = number_line(6, p, left, right)
        V, pi = value_iteration(T, R, end, gamma)
        assert np.allclose(V, best_by_brute_force(T, R, end, gamma), atol=1e-6)
        assert V[0] == 0 and V[-1] == 0


def test_greedy_policy():
    T, R, end = number_line(5, 0.9, 1, 100)
    V, pi = value_iteration(T, R, end, 1.0)
    assert list(pi[1:4]) == [1, 1, 1]
    T, R, end = number_line(5, 0.9, 100, 1)
    assert list(value_iteration(T, R, end, 1.0)[1][1:4]) == [0, 0, 0]


def test_ties_take_smallest_action():
    # one state, two identical actions that loop with reward 1
    T = np.ones((1, 2, 1))
    R = np.ones((1, 2, 1))
    V, pi = value_iteration(T, R, np.array([False]), 0.5)
    assert np.isclose(V[0], 2.0) and pi[0] == 0
```
:::
