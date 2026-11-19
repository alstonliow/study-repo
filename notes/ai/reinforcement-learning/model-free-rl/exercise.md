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
