::: {.problem #prob-cs188hw-5-q2 origin="external" source="cs188hw-5-q2"}
**Square World.** In this question we will consider the following gridworld:

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[hl cell] (0.0,0.0) rectangle (1.0,-0.8);
\node[lab, align=center] at (0.5,-0.4) {0};
\draw[hl cell] (1.0,0.0) rectangle (2.0,-0.8);
\node[lab, align=center] at (1.5,-0.4) {0};
\draw[hl cell] (2.0,0.0) rectangle (3.0,-0.8);
\node[lab, align=center] at (2.5,-0.4) {0};
\draw[hl cell] (3.0,0.0) rectangle (4.0,-0.8);
\node[lab, align=center] at (3.5,-0.4) {0};
\draw[hl cell] (4.0,0.0) rectangle (5.0,-0.8);
\node[lab, align=center] at (4.5,-0.4) {0};
\draw[hl cell] (5.0,0.0) rectangle (6.0,-0.8);
\node[lab, align=center] at (5.5,-0.4) {0};
\draw[hl cell] (0.0,-0.8) rectangle (1.0,-1.6);
\node[lab, align=center] at (0.5,-1.2000000000000002) {$+1$};
\draw[cell frame] (1.0,-0.8) rectangle (2.0,-1.6);
\node[lab, align=center] at (1.5,-1.2000000000000002) {$A$};
\draw[cell frame] (2.0,-0.8) rectangle (3.0,-1.6);
\node[lab, align=center] at (2.5,-1.2000000000000002) {$B$};
\draw[cell frame] (3.0,-0.8) rectangle (4.0,-1.6);
\node[lab, align=center] at (3.5,-1.2000000000000002) {$C$};
\draw[cell frame] (4.0,-0.8) rectangle (5.0,-1.6);
\node[lab, align=center] at (4.5,-1.2000000000000002) {$D$};
\draw[hl cell] (5.0,-0.8) rectangle (6.0,-1.6);
\node[lab, align=center] at (5.5,-1.2000000000000002) {$+100$};
\draw[hl cell] (0.0,-1.6) rectangle (1.0,-2.4000000000000004);
\node[lab, align=center] at (0.5,-2.0) {0};
\draw[hl cell] (1.0,-1.6) rectangle (2.0,-2.4000000000000004);
\node[lab, align=center] at (1.5,-2.0) {0};
\draw[hl cell] (2.0,-1.6) rectangle (3.0,-2.4000000000000004);
\node[lab, align=center] at (2.5,-2.0) {0};
\draw[hl cell] (3.0,-1.6) rectangle (4.0,-2.4000000000000004);
\node[lab, align=center] at (3.5,-2.0) {0};
\draw[hl cell] (4.0,-1.6) rectangle (5.0,-2.4000000000000004);
\node[lab, align=center] at (4.5,-2.0) {0};
\draw[hl cell] (5.0,-1.6) rectangle (6.0,-2.4000000000000004);
\node[lab, align=center] at (5.5,-2.0) {0};
\end{tikzpicture}
\end{center}
```



Every grid square corresponds to a state. If a state is annotated with a number, it means that after entering this state only one action is available, the Exit action, and this will result in the reward indicated by the number and the episode will end. There is no reward otherwise. For the other 4 states, named $A$, $B$, $C$, $D$, two actions are available: Left and Right. Assume $\gamma=1$ in this problem.

1. Assume that the failure probability for the actions Left and Right is 0.5, and in case of failure the agent moves up or down, and the episode is terminated after the Exit action.

   What are the optimal values?

   | State $s$: | $A$ | $B$ | $C$ | $D$ |
   |---|---|---|---|---|
   | $V^*(s)$ | | | | |
2. Still assume the failure probability in the previous part. Now assume further that there is an *integer* living reward $r$ when the episode is not terminated. Is there a value of $r$ that would make the optimal policy **only** decide Left at state D? If so, what's the minimum value of $r$?
3. Assume we collected the following episodes of experience in the form (state, action, next state, reward). We use X1 and X100 for the leftmost and rightmost states in the middle row, and Done for the terminal state after an Exit.
$$
(B,\text{Left},A,0),\ (A,\text{Left},\text{X1},0),\ (\text{X1},\text{Exit},\text{Done},+1)
$$
$$
(B,\text{Right},C,0),\ (C,\text{Right},D,0),\ (D,\text{Right},\text{X100},0),\ (\text{X100},\text{Exit},\text{Done},+100)
$$
   If we run Q-learning initializing all Q-values equal to 0, and with appropriate stepsizing, replaying each episode infinitely often till convergence, what will be the resulting values?

   | (State, Action) | (B, Left) | (B, Right) | (C, Left) | (C, Right) |
   |---|---|---|---|---|
   | $Q^*(s,a)$ | | | | |
4. Now we are trying to do feature-based Q-learning. Answer the below True or False question.

   There exists a set of features that are functions of state only such that approximate Q-learning will converge to the optimal Q-values.

   True False

*Note (these notes):* Grid redrawn; highlighted squares are exit states.
:::

::: {#prob-tabular-q-learning-code .problem .coding origin="adapted" source="res-stanford-cs221-hw-mountaincar" packages="numpy"}
Implement tabular Q-learning (@def-q-learning) with an $\epsilon$-greedy policy (@def-epsilon-greedy) as a class `QLearning(S, A, gamma, eta)` for states `0, ..., S-1` and actions `0, ..., A-1`.

- The attribute `Q` is a float array of shape `(S, A)`, initially zero.
- `act(s, epsilon, rng)` returns an action: with probability `epsilon` one drawn uniformly at random, otherwise one maximizing `Q[s]` (the smallest such action). `rng` is a `random.Random`; use it for all randomness.
- `update(s, a, r, t, end)` incorporates the transition $(s,a,r,t)$, where `end` says whether $t$ is an end state: it moves `Q[s, a]` a fraction `eta` of the way towards the Q-learning target.

```{.python .starter}
import numpy as np


class QLearning:
    def __init__(self, S, A, gamma, eta):
        ...

    def act(self, s, epsilon, rng):
        """Epsilon-greedy action in state s."""
        ...

    def update(self, s, a, r, t, end):
        """Move Q[s, a] towards r + gamma * max_a' Q[t, a'] (just r if t is an end state)."""
        ...
```

```{.python .tests}
import random
import numpy as np


def test_single_updates():
    q = QLearning(3, 2, gamma=0.5, eta=0.25)
    assert q.Q.shape == (3, 2) and not q.Q.any()
    q.Q[1] = [2.0, 6.0]
    q.update(0, 1, 1.0, 1, False)              # target 1 + 0.5 * 6 = 4
    assert np.isclose(q.Q[0, 1], 1.0)
    q.update(0, 1, 1.0, 1, True)               # target 1
    assert np.isclose(q.Q[0, 1], 1.0)
    q.update(2, 0, -4.0, 2, False)             # target -4 + 0.5 * 0
    assert np.isclose(q.Q[2, 0], -1.0)


def test_greedy_and_ties():
    q = QLearning(2, 3, 0.9, 0.1)
    rng = random.Random(0)
    q.Q[0] = [1.0, 5.0, 5.0]
    assert all(q.act(0, 0.0, rng) == 1 for _ in range(20))
    assert all(q.act(1, 0.0, rng) == 0 for _ in range(20))


def test_exploration_frequencies():
    q = QLearning(1, 4, 0.9, 0.1)
    q.Q[0] = [0.0, 0.0, 3.0, 0.0]
    rng = random.Random(1)
    n = 20000
    counts = np.bincount([q.act(0, 0.4, rng) for _ in range(n)], minlength=4) / n
    assert np.allclose(counts, [0.1, 0.1, 0.7, 0.1], atol=0.02)


def test_learns_a_chain():
    # states 0..3, 3 is the end; action 1 moves right, action 0 stays; entering 3 pays 1
    q = QLearning(4, 2, gamma=0.9, eta=0.5)
    for _ in range(200):
        for s in range(3):
            q.update(s, 0, 0.0, s, False)
            q.update(s, 1, 1.0 if s == 2 else 0.0, s + 1, s == 2)
    assert np.allclose(q.Q[:3, 1], [0.81, 0.9, 1.0], atol=1e-6)
    assert np.allclose(q.Q[:3, 0], [0.729, 0.81, 0.9], atol=1e-6)
```
:::
