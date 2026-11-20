::: {.problem #prob-cs188hw-9-q1 origin="external" source="cs188hw-9-q1"}
**Course Evaluations.** Every semester we try to make CS 188 a little better. Let $S_t$ represent the quality of the CS 188 offering at semester $t$, where $S_t\in\{1,2,3,4,5\}$. Changes to the course are incremental so between semester $t$ and $t+1$, the value of $S$ can only change by at most 1. Each possible transition occurs with equal probability. As examples: if $S_t=1$, then $S_{t+1}\in\{1,2\}$ each with probability $\frac12$. If $S_t=2$, then $S_{t+1}\in\{1,2,3\}$ each with probability $\frac13$.

Let $E_t\in\{+e,-e\}$ represent the feedback we receive from student evaluations for the semester $t$, where $+e$ is generally positive feedback and $-e$ is negative feedback. Student feedback is dependent on whether released assignments were helpful for the given semester ($A_t\in\{+a,-a\}$) which is dependent on the quality of the semester's course offering ($S_t$). Additionally, student evaluations are also dependent on events external to the class ($X_t\in\{+x,-x\}$).

The following HMM depicts the described scenario:

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm, y=1cm]
\node[vertex] (S0) at (0.0,0) {$S_{0}$};
\node[vertex] (A0) at (0.0,-1.2) {$A_{0}$};
\node[vertex] (X0) at (1.0,-1.2) {$X_{0}$};
\node[vertex] (E0) at (0.5,-2.4) {$E_{0}$};
\node[vertex] (S1) at (2.0,0) {$S_{1}$};
\node[vertex] (A1) at (2.0,-1.2) {$A_{1}$};
\node[vertex] (X1) at (3.0,-1.2) {$X_{1}$};
\node[vertex] (E1) at (2.5,-2.4) {$E_{1}$};
\node[vertex] (S2) at (4.0,0) {$S_{t}$};
\node[vertex] (A2) at (4.0,-1.2) {$A_{t}$};
\node[vertex] (X2) at (5.0,-1.2) {$X_{t}$};
\node[vertex] (E2) at (4.5,-2.4) {$E_{t}$};
\draw[->] (S0) -- (A0);
\draw[->] (A0) -- (E0);
\draw[->] (X0) -- (E0);
\draw[->] (S1) -- (A1);
\draw[->] (A1) -- (E1);
\draw[->] (X1) -- (E1);
\draw[->] (S0) -- (S1);
\draw[->] (S2) -- (A2);
\draw[->] (A2) -- (E2);
\draw[->] (X2) -- (E2);
\draw[->, dashed] (S1) -- (S2);
\end{tikzpicture}
\end{center}
```

Consider the above dynamic Bayes net which ends at some finite timestep $t$. In this problem, we are trying to approximate the most likely value of $S_t$ given all the evidence variables up to and including $t$. For each of the following subparts, first decide whether the given method can be used to solve this problem. Then, if yes, select all CPTs which must be known to run the algorithm.

1. Variable elimination

   No $\quad$ Yes: $P(S_0)$, $P(S_t\mid S_{t-1})$, $t>0$ $\quad P(A_t\mid S_t)\,\forall t$ $\quad P(E_t\mid X_t,A_t)\,\forall t$ $\quad P(X_t)\,\forall t$
2. Value iteration

   No $\quad$ Yes: $P(S_0)$, $P(S_t\mid S_{t-1})$, $t>0$ $\quad P(A_t\mid S_t)\,\forall t$ $\quad P(E_t\mid X_t,A_t)\,\forall t$ $\quad P(X_t)\,\forall t$
3. Gibbs sampling

   No $\quad$ Yes: $P(S_0)$, $P(S_t\mid S_{t-1})$, $t>0$ $\quad P(A_t\mid S_t)\,\forall t$ $\quad P(E_t\mid X_t,A_t)\,\forall t$ $\quad P(X_t)\,\forall t$
4. Prior sampling

   No $\quad$ Yes: $P(S_0)$, $P(S_t\mid S_{t-1})$, $t>0$ $\quad P(A_t\mid S_t)\,\forall t$ $\quad P(E_t\mid X_t,A_t)\,\forall t$ $\quad P(X_t)\,\forall t$
5. Particle filtering

   No $\quad$ Yes: $P(S_0)$, $P(S_t\mid S_{t-1})$, $t>0$ $\quad P(A_t\mid S_t)\,\forall t$ $\quad P(E_t\mid X_t,A_t)\,\forall t$ $\quad P(X_t)\,\forall t$

For the HMM shown above, determine the correct recursive formula for the belief distribution update from $B(S_{t-1})$ to $B(S_t)$. Recall that the belief distribution $B(S_t)$ represents the probability $P(S_t\mid E_{0:t})$ and involves two steps: (i) Time elapse and (ii) Observation update.
$$
B(S_t)\propto\text{(ii)}\cdot\text{(i)}
$$

6. Fill in blank (i).
   - $\sum_{S_{t-1}}P(S_t\mid S_{t-1})B(S_{t-1})$
   - $\sum_{S_{t-1}}P(S_t\mid S_{t-1})P(A_t\mid S_t)B(S_{t-1})$
   - $\sum_{S_{t-1}}\sum_{A_{t-1}}P(S_t\mid S_{t-1})P(A_{t-1}\mid S_{t-1})B(S_{t-1})$
   - $\sum_{S_{t-1}}\sum_{A_{t-1}}P(S_t\mid S_{t-1})P(A_{t-1}\mid S_{t-1})P(A_t\mid S_t)B(S_{t-1})$
7. Fill in blank (ii).
   - $P(E_t\mid X_t,A_t)$
   - $P(E_t\mid X_t,A_t)P(X_t)P(A_t\mid S_t)$
   - $\sum_{x\in X_t}\sum_{a\in A_t}P(E_t\mid x,a)$
   - $\sum_{x\in X_t}\sum_{a\in A_t}P(E_t\mid x,a)P(x)P(a\mid S_t)$
   - $\prod_{x\in X_t}\prod_{a\in A_t}P(E_t\mid x,a)$
   - $\prod_{x\in X_t}\prod_{a\in A_t}P(E_t\mid x,a)P(x)P(a\mid S_t)$

Due to the differences between CS188 offerings in the fall and spring semesters, we realize that only student evaluations from past fall semesters are accurate enough to be incorporated into our model. Assume that a fall semester occurs during an even timestep and that $t$ is even in the diagram below. The new HMM can be repesented as follows:

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm, y=1cm]
\node[vertex] (S0) at (0.0,0) {$S_{t}$};
\node[vertex] (A0) at (0.0,-1.2) {$A_{t}$};
\node[vertex] (X0) at (1.0,-1.2) {$X_{t}$};
\node[vertex] (E0) at (0.5,-2.4) {$E_{t}$};
\node[vertex] (S1) at (2.0,0) {$S_{t+1}$};
\node[vertex] (S2) at (4.0,0) {$S_{t+2}$};
\node[vertex] (A2) at (4.0,-1.2) {$A_{t+2}$};
\node[vertex] (X2) at (5.0,-1.2) {$X_{t+2}$};
\node[vertex] (E2) at (4.5,-2.4) {$E_{t+2}$};
\draw[->] (S0) -- (A0);
\draw[->] (A0) -- (E0);
\draw[->] (X0) -- (E0);
\draw[->] (S0) -- (S1);
\draw[->] (S2) -- (A2);
\draw[->] (A2) -- (E2);
\draw[->] (X2) -- (E2);
\draw[->] (S1) -- (S2);
\end{tikzpicture}
\end{center}
```

8. In this question, we are trying to derive a recursive formula for the two-step belief distribution update from $B(S_t)$ to $B(S_{t+2})$ for the new problem described above. Which of the following steps represent the correct and most efficient method of performing HMM updates to get the belief distribution at $S_{t+2}$ from the current belief at $S_t$?

   For the following notation, let $B(S_t)=P(S_t\mid E_{0:t:2})$ and $B'(S_t)=P(S_t\mid E_{0:t-1:2})$ where $E_{0:i:2}$ represents the set of all evidence variables at even timesteps up to $i$. Further, let $O(E_t)$ represent the value of the observation update expression from the previous part. (Note that $O(E_{t+1})$ and $O(E_{t+2})$ would represent the appropriate observation update expressions for timestep $t+1$ and $t+2$ respectively.)
   - $B'(S_{t+1})=\sum_{S_t}P(S_{t+1}\mid S_t)B(S_t)$; $B'(S_{t+2})=\sum_{S_{t+1}}P(S_{t+2}\mid S_{t+1})B'(S_{t+1})$; $B(S_{t+2})\propto O(E_{t+2})B'(S_{t+2})$
   - $B'(S_{t+1})=\sum_{S_t}P(S_{t+1}\mid S_t)B(S_t)$; $B(S_{t+1})=\sum_{E_{t+1}}O(E_{t+1})B'(S_{t+1})$; $B'(S_{t+2})=\sum_{S_{t+1}}P(S_{t+2}\mid S_{t+1})B(S_{t+1})$; $B(S_{t+2})\propto O(E_{t+2})B'(S_{t+2})$
   - $B'(S_{t+2})=\sum_{S_{t+1}}\sum_{S_t}P(S_{t+2}\mid S_{t+1})P(S_{t+1}\mid S_t)B(S_t)$; $B(S_{t+2})\propto O(E_{t+2})B'(S_{t+2})$
   - $B'(S_{t+1})=\sum_{S_t}P(S_{t+1}\mid S_t)B(S_t)$; $B(S_{t+1})\propto O(E_{t+1})B'(S_{t+1})$; $B'(S_{t+2})=\sum_{S_{t+1}}P(S_{t+2}\mid S_{t+1})B(S_{t+1})$; $B(S_{t+2})\propto O(E_{t+2})B'(S_{t+2})$
   - None of the above

Now consider a scenario where instead of getting one general student feedback as evidence ($E_t$), we instead get individual student feedback from 100 students. Let the variable $E_{t,n}$ represent the evidence from student $n$ at timestep $t$. Assume that the new evidence variables ($E_{t,n}$) can each take on the value of $+e$ or $-e$ with the same probability distribution as the single variable case ($E_t$).

9. Which of the following statements are true regarding this new setup?
   - The evidence variables within the same timestep are independent of each other ($E_{t,j}\perp\!\!\!\perp E_{t,k}\ \forall j\ne k$).
   - The evidence variables between any two different timesteps are independent of each other ($E_{(t_1),j}\perp\!\!\!\perp E_{(t_2),k}\ \forall t_1\ne t_2$).
   - The expression to calculate the time elapse step from $S_t$ to $S_{t+1}$ for this new setup will be the same as the time elapse expression in the case of one evidence from Q1.6.
   - None of the above
10. In the observation update at timestep $t$, we receive as evidence 60 positive evaluations ($+e$) and 40 negative evaluations ($-e$). Let $x$ be the observation update probability at timestep $t$ of observing one positive evaluation ($x=O(E_t=+e)$). Now, let $f(x)$ represent the new observation update expression for the case with the observed 100 evidence variables. Which of the following functions $f$ gives the correct observation update for the new scenario? For this part only, regardless of your previous answer, please assume that each students' feedback is independent of each other.
    - $f(x)=x^{100}$
    - $f(x)=60x\cdot40(1-x)$
    - $f(x)=x^{60}\cdot(1-x)^{40}$
    - None of the above

*Note (these notes):* Both networks are redrawn here; the dashed edge stands for the omitted time steps.
:::

::: {#prob-hmm-filtering-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-tracking" solution="withheld" packages="numpy"}
Implement exact filtering in a hidden Markov model (@def-hmm) with the forward algorithm (@thm-forward-algorithm). Write `filter_beliefs(prior, T, O, evidence)`.

- The states are `0, ..., n-1` and the observations `0, ..., m-1`.
- `prior` has shape `(n,)`: `prior[x]` $=P(X_1=x)$.
- `T` has shape `(n, n)`: `T[x, y]` $=P(X_{t+1}=y\mid X_t=x)$.
- `O` has shape `(n, m)`: `O[x, e]` $=P(E_t=e\mid X_t=x)$.
- `evidence` is the list $e_1,\dots,e_k$ with $k\ge1$; assume each has positive probability given the earlier ones.

Return an array of shape `(k, n)` whose row $t-1$ is the belief $B_t$ (@def-filtering). The first observation updates the prior directly; every later one comes after one elapse-time step.

```{.python .starter}
import numpy as np


def filter_beliefs(prior, T, O, evidence):
    """Beliefs B_1, ..., B_k of the HMM (prior, T, O) as rows of a (k, n) array."""
    ...
```

```{.python .tests}
import numpy as np

# the weather of the example: 0 = rain, 1 = sun; observation 0 = umbrella, 1 = none
prior = np.array([0.5, 0.5])
T = np.array([[0.7, 0.3], [0.3, 0.7]])
O = np.array([[0.8, 0.2], [0.3, 0.7]])


def test_umbrella_example():
    B = filter_beliefs(prior, T, O, [0, 0, 1])
    assert B.shape == (3, 2)
    assert np.allclose(B[0], [8 / 11, 3 / 11])
    assert np.allclose(B[1], [104 / 131, 27 / 131])
    assert np.isclose(B[2, 0], 0.316, atol=1e-3)
    assert np.allclose(B.sum(axis=1), 1.0)


def test_first_belief_uses_prior_only():
    B = filter_beliefs(np.array([0.9, 0.1]), T, O, [1])
    expected = np.array([0.9 * 0.2, 0.1 * 0.7])
    assert np.allclose(B[0], expected / expected.sum())


def test_uninformative_observations_follow_the_chain():
    # with O constant, filtering is prediction: B_t = prior T^(t-1)
    O_flat = np.full((3, 2), 0.5)
    T3 = np.array([[0.5, 0.5, 0.0], [0.0, 0.5, 0.5], [0.5, 0.0, 0.5]])
    p = np.array([1.0, 0.0, 0.0])
    B = filter_beliefs(p, T3, O_flat, [0, 1, 0, 0])
    for t in range(4):
        assert np.allclose(B[t], p @ np.linalg.matrix_power(T3, t))


def test_impossible_state_stays_impossible():
    # observation 1 is impossible in state 2, so the belief of state 2 is 0 after it
    O3 = np.array([[0.5, 0.5], [0.5, 0.5], [1.0, 0.0]])
    T3 = np.full((3, 3), 1 / 3)
    B = filter_beliefs(np.full(3, 1 / 3), T3, O3, [0, 1, 1])
    assert np.allclose(B[1], [0.5, 0.5, 0.0]) and np.allclose(B[2], [0.5, 0.5, 0.0])
    assert np.allclose(B[0], [0.25, 0.25, 0.5])
```
:::
