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
