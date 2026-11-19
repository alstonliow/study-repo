::: {.problem #prob-cs70hw-15-q1 origin="external" source="cs70hw-15-q1"}
**Playing Blackjack.** You are playing a game of Blackjack where you start with \$100. You are a particularly risk-loving player who does not believe in leaving the table until you either make \$400, or lose all your money. At each turn you either win \$100 with probability $p$, or you lose \$100 with probability $1 - p$.

(a) Formulate this problem as a Markov chain i.e. define your state space, transition probabilities, and determine your starting state.

(b) Find the probability that you end the game with \$400.
:::

::: {.problem #prob-cs70hw-15-q2 origin="external" source="cs70hw-15-q2"}
**Markov's Coupon Collecting.** Courtney is home for Thanksgiving and needs to make some trips to the Traitor Goes grocery store to prepare for the big turkey feast. Each time she goes to the store before the holiday, she receives one of the $n$ different coupons that are being given away. You may recall that we studied how to calculate the expected number of trips to the store needed to collect at least one of each coupon. Using geometric distributions and indicator variables, we determined that expected number of trips to be $n(\ln n + \gamma)$.

Let's re-derive that, this time with a Markov chain model and first-step equations.

(a) Define the states and transition probabilities for each state (explain what states can be transitioned to, and what probabilities those transitions occur with).

(b) Now set up first-step equations and solve for the expected number of grocery store trips Courtney needs to make before Thanksgiving so that she can have at least one of each of the $n$ distinct coupons.
:::

::: {.problem #prob-cs70hw-15-q3 origin="external" source="cs70hw-15-q3"}
**Reflecting Random Walk.** Alice starts at vertex 0 and wishes to get to vertex $n$. When she is at vertex 0 she has a probability of 1 of transitioning to vertex 1. For any other vertex $i$, there is a probability of $1/2$ of transitioning to $i + 1$ and a probability of $1/2$ of transitioning to $i - 1$.

(a) What is the expected number of steps Alice takes to reach vertex $n$? Write down the hitting-time equations, but do not solve them yet.

(b) Solve the hitting-time equations. [Hint: Let $R_i$ denote the expected number of steps to reach vertex $n$ starting from vertex $i$. As a suggestion, try writing $R_0$ in terms of $R_1$; then, use this to express $R_1$ in terms of $R_2$; and then use this to express $R_2$ in terms of $R_3$, and so on. See if you can notice a pattern.]
:::

::: {.problem #prob-cs70hw-15-q4 origin="external" source="cs70hw-15-q4"}
**Boba in a Straw.** Imagine that Jonathan is drinking milk tea and he has a very short straw: it has enough room to fit two boba (see figure).

Here is a formal description of the drinking process: We model the straw as having two "components" (the top component and the bottom component). At any given time, a component can contain nothing, or one boba. As Jonathan drinks from the straw, the following happens every second:

1. The contents of the top component enter Jonathan's mouth.
2. The contents of the bottom component move to the top component.
3. With probability $p$, a new boba enters the bottom component; otherwise the bottom component is now empty.

Help Jonathan evaluate the consequences of his incessant drinking!

(a) At the very start, the straw starts off completely empty. What is the expected number of seconds that elapse before the straw is completely filled with boba for the first time? [Write down the equations; you do not have to solve them.]

(b) Consider a slight variant of the previous part: now the straw is narrower at the bottom than at the top. This affects the drinking speed: if either (i) a new boba is about to enter the bottom component or (ii) a boba from the bottom component is about to move to the top component, then the action takes two seconds. If both (i) and (ii) are about to happen, then the action takes three seconds. Otherwise, the action takes one second. Under these conditions, answer the previous part again. [Write down the equations; you do not have to solve them.]

(c) Jonathan was annoyed by the straw so he bought a fresh new straw (the straw is no longer narrow at the bottom). What is the long-run average rate of Jonathan's calorie consumption? (Each boba is roughly 10 calories.)

(d) What is the long-run average number of boba which can be found inside the straw? [Maybe you should first think about the long-run distribution of the number of boba.]

*Note (these notes):* The figure of the straw is not reproduced.
:::

::: {.problem #prob-eecs126hw-1-q4 origin="external" source="eecs126hw-1-q4"}
**Random Walk on a Circle.** Suppose we have $n$ points labeled $\{1,2,\dots,n\}$ around a circle. An ant starts at point $1$, and at each second has an equal probability of moving clockwise or counterclockwise to an adjacent point. For each point $k\in\{2,3,\dots,n\}$, find the probability that the first time the ant lands at $k$, it has visited all other points already.
:::

::: {.problem #prob-eecs126d-5-q2 origin="external" source="eecs126d-5-q2"}
**Product of Rolls of a Die.** A fair die with labels (1 to 6) is rolled until the product of the last two rolls is 12. What is the expected number of rolls?

[Hint: You can model this process as a Markov chain with 3 states. Choose your states according to the outcome of last roll. For example, assign one state if it is outcome was 1 or 5 (which is useless if you want the product to be 12). If the outcome was 2,3,4 or 6, it's useful and can be assigned another state. Assign third state to the case when the product last two outcomes was 12.]
:::

::: {.problem #prob-eecs126hw-4-q1 origin="external" source="eecs126hw-4-q1"}
**Reducible Markov Chain.** Consider the following Markov chain, for $\alpha,\beta,p,q\in(0,1)$.

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (0) at (0.0,0) {$0$};
\node[small vertex] (1) at (1.6,0) {$1$};
\node[small vertex] (2) at (3.2,0) {$2$};
\node[small vertex] (3) at (4.800000000000001,0) {$3$};
\node[small vertex] (4) at (6.4,0) {$4$};
\node[small vertex] (5) at (8.0,0) {$5$};
\draw[->] (0) to[loop above] node[lab,tick,above] {$1-\alpha$} (0);
\draw[->] (1) to[loop above] node[lab,tick,above] {$1-\beta$} (1);
\draw[->] (4) to[loop above] node[lab,tick,above] {$1-p$} (4);
\draw[->] (5) to[loop above] node[lab,tick,above] {$1-q$} (5);
\draw[->] (0) to[bend left=30] node[lab,tick,above] {$\alpha$} (1);
\draw[->] (1) to[bend left=30] node[lab,tick,below] {$\beta$} (0);
\draw[->] (2)--node[lab,tick,above] {$1/2$} (1);
\draw[->] (2) to[bend left=30] node[lab,tick,above] {$1/2$} (3);
\draw[->] (3) to[bend left=30] node[lab,tick,below] {$1/2$} (2);
\draw[->] (3)--node[lab,tick,above] {$1/2$} (4);
\draw[->] (4) to[bend left=30] node[lab,tick,above] {$p$} (5);
\draw[->] (5) to[bend left=30] node[lab,tick,below] {$q$} (4);
\end{tikzpicture}
\end{center}
```

(a) Find all the recurrent and transient classes.

(b) Given that we start in state $2$, what is the probability that we will reach state $0$ before state $5$?

(c) What are all of the possible stationary distributions of this chain? Hint: Consider the recurrent classes.

(d) Suppose we start in the initial distribution $\pi_0:=\begin{bmatrix}0&0&\gamma&1-\gamma&0&0\end{bmatrix}$ for some $\gamma\in[0,1]$. Does the distribution of the chain converge, and if so, to what?
:::

::: {.problem #prob-eecs126hw-5-q4 origin="external" source="eecs126hw-5-q4"}
**Twitch Plays Pokemon.** You wake up one day and are surprised to see that it is 2014, when the world was peaceful. You immediately start playing Twitch Plays Pokemon. Suddenly, you realized that you may be able to analyze Twitch Plays Pokemon.

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0.0) rectangle (1.2,0.6);
\draw[cell frame] (1.2,0.0) rectangle (2.4,0.6);
\draw[cell frame] (2.4,0.0) rectangle (3.5999999999999996,0.6);
\draw[cell frame] (0.0,-0.6) rectangle (1.2,0.0);
\draw[cell frame] (1.2,-0.6) rectangle (2.4,0.0);
\draw[cell frame] (2.4,-0.6) rectangle (3.5999999999999996,0.0);
\draw[cell frame] (0.0,-1.2) rectangle (1.2,-0.6);
\draw[cell frame] (1.2,-1.2) rectangle (2.4,-0.6);
\draw[cell frame] (2.4,-1.2) rectangle (3.5999999999999996,-0.6);
\node[lab] at (0.6,0.3) {You};
\node[lab] at (3.0,-0.9) {Stairs};
\end{tikzpicture}
\end{center}
```

Figure 1: Part (a)

(a) The player in the top left corner performs a random walk on the 8 checkered squares and the square containing the stairs. At every step the player is equally likely to move to any of the squares in the four cardinal directions (North, West, East, South) if there is a square in that direction. Find the expected number of moves until the player reaches the stairs in Figure 1.

[Hint: Use symmetry to reduce the number of states in your Markov chain]

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0.0) rectangle (1.2,0.6);
\draw[cell frame] (1.2,0.0) rectangle (2.4,0.6);
\draw[cell frame] (2.4,0.0) rectangle (3.5999999999999996,0.6);
\draw[cell frame] (0.0,-0.6) rectangle (1.2,0.0);
\draw[cell frame] (1.2,-0.6) rectangle (2.4,0.0);
\draw[cell frame] (2.4,-0.6) rectangle (3.5999999999999996,0.0);
\draw[cell frame] (0.0,-1.2) rectangle (1.2,-0.6);
\draw[cell frame] (1.2,-1.2) rectangle (2.4,-0.6);
\draw[cell frame] (2.4,-1.2) rectangle (3.5999999999999996,-0.6);
\node[lab] at (0.6,0.3) {You};
\node[lab] at (0.6,-0.9) {Stairs};
\node[lab] at (3.0,-0.9) {Stairs};
\end{tikzpicture}
\end{center}
```

Figure 2: Part (b)

(b) The player randomly walks in the same way as in the previous part. Find the probability that the player reaches the stairs in the bottom right corner in Figure 2.

[Hint: For each squared box, assign a variable that denotes the probability of reaching the "good" stairs. Use symmetry again to reduce the number of such variables.]

Hint: For both problems use symmetry to reduce the number of states and variables. The equations are very reasonable to solve by hand.
:::
