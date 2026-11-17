<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 13, §3.7 "The Monty Hall Problem" (source key cs70-13.3.7, in note.md). -->

::: {#exm-monty-hall .example name="The Monty Hall problem" level="medium"}
A prize is behind one of three doors and the other two hide nothing. You pick
a door. The host knows where the prize is and opens one of the other two
doors, always one without the prize. You may then keep your door or switch to
the remaining closed one. Should you switch?

**Intuition misleads.** With two closed doors left, it is tempting to give
each probability $\frac12$. But your first pick is right with probability
$\frac13$, and opening an empty door does not change that. So the other
closed door must hold the prize with probability $\frac23$.

**Sample space.** To check this, write an outcome as a triple $(i,j,k)$: the
prize is behind door $i$, you pick door $j$, and the host opens door $k$. The
host never opens the prize door or your door, so only $12$ triples are
possible. Assume:

- the prize is equally likely to be behind each door;
- you pick each door with probability $\frac13$;
- when you have picked the prize door, the host opens either of the other two
  with probability $\frac12$.

**Probabilities of the outcomes.** Multiply along the choices
(@prp-multiplication-rule).

- If $i\neq j$, the host has only one door to open, so
  $\Pr(i,j,k)=\frac13\cdot\frac13\cdot1=\frac19$. There are $6$ such outcomes.
- If $i=j$, the host has two doors to choose from, so
  $\Pr(i,j,k)=\frac13\cdot\frac13\cdot\frac12=\frac1{18}$. There are $6$ such
  outcomes.

As a check, $6\cdot\frac19+6\cdot\frac1{18}=1$.

**Switching.** Switching wins exactly when your first pick was wrong, that is
when $i\neq j$. Then the host opens the other empty door and you switch to the
prize. So
$$
\Pr(\text{win by switching}) = 6\cdot\tfrac19 = \tfrac23,
\qquad
\Pr(\text{win by keeping}) = 6\cdot\tfrac1{18} = \tfrac13 .
$$
You should switch.

**Lesson.** Work systematically. Name the sample space, give each outcome its
probability, describe the event as a set of outcomes, and add up.

**Second solution, with conditional probability.** <!-- Merged 2026-11-17 (SPEC §7.8): this part was a separate example adapted from CS70 Note 14 (cs70-14.1). -->
Let $C_i$ be "you pick door $i$", $P_i$ "the prize is behind door $i$" and $H_i$ "the host opens door $i$".

1. By @thm-chain-rule,
   $$\Pr(C_1\cap P_2\cap H_3)=\Pr(C_1)\,\Pr(P_2\mid C_1)\,\Pr(H_3\mid C_1\cap P_2)=\tfrac13\cdot\tfrac13\cdot1=\tfrac19.$$
   The host must open door $3$: door $1$ is yours and door $2$ hides the prize.

2. Given $C_1$, the host opens door $3$ with probability $\frac12$ by symmetry, so $\Pr(C_1\cap H_3)=\frac13\cdot\frac12=\frac16$.

3. Hence $\Pr(P_2\mid C_1\cap H_3)=\dfrac{1/9}{1/6}=\dfrac23$: after the host opens door $3$, switching to door $2$ wins with probability $\frac23$.

Multiplying the three plain probabilities instead would give $\frac1{27}$, which is wrong because the events are not independent.
:::

<!-- The examples below are adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 14, §1 and §4 (source keys cs70-14.1, cs70-14.4, in note.md). -->

::: {#exm-conditioning-balls-and-bins .example name="Conditioning on an empty bin" level="easy"}
Throw $4$ labelled balls into $3$ labelled bins, all $3^4=81$ outcomes equally likely. Let $A$ be "bin $1$ is empty" and $B$ "bin $2$ is empty".

1. $\Pr(A)=\Pr(B)=\left(\frac23\right)^4=\frac{16}{81}$, since every ball must miss the bin.

2. $A\cap B$ means all four balls land in bin $3$: one outcome, so $\Pr(A\cap B)=\frac1{81}$.

3. By @def-conditional-probability, $\Pr(A\mid B)=\dfrac{1/81}{16/81}=\dfrac1{16}=0.0625$, much less than $\Pr(A)\approx0.1975$. Knowing that bin $2$ is empty makes it less likely that bin $1$ is empty too, because the balls have fewer places to go.
:::

::: {#exm-two-aces .example name="Two aces in a row" level="easy"}
Deal two cards from a shuffled deck. Let $B$ be "the first card is an ace" and $A$ "the second card is an ace". The outcomes are the $52\cdot51$ ordered pairs of distinct cards, all equally likely.

1. Both cards are aces in $4\cdot3=12$ ways, so $\Pr(A\cap B)=\frac{12}{52\cdot51}$.

2. $\Pr(B)=\frac4{52}$, so $\Pr(A\mid B)=\dfrac{12/(52\cdot51)}{4/52}=\dfrac3{51}$.

3. This is less than $\Pr(A)=\frac1{13}=\frac4{52}$: one ace has already gone.
:::

::: {#exm-pairwise-not-mutual .example name="Pairwise independent but not mutually independent" level="medium"}
Toss a fair coin twice. Let $A$ be "the first toss is H", $B$ "the second toss is H", and $C$ "both tosses are the same".

1. Each event has probability $\frac12$.

2. $A\cap B$, $A\cap C$ and $B\cap C$ are each the single outcome HH, so each has probability $\frac14=\frac12\cdot\frac12$. The three events are pairwise independent (@def-independent).

3. But $A\cap B\cap C$ is also HH, with probability $\frac14\ne\frac18=\Pr(A)\Pr(B)\Pr(C)$. So they are not mutually independent (@def-mutual-independence-events): if $A$ and $B$ both happen, $C$ is certain.
:::

::: {#exm-three-heads .example name="Independent tosses multiply" level="easy"}
Toss a coin with heads probability $p$ three times, and let $A_i$ be "toss $i$ is H". The tosses are mutually independent, so in @thm-chain-rule every conditional probability equals the plain one:
$$\Pr(A_1\cap A_2\cap A_3)=\Pr(A_1)\Pr(A_2)\Pr(A_3)=p^3,$$
which is $\frac18$ for a fair coin. In the same way any sequence of $n$ tosses with $k$ heads has probability $p^k(1-p)^{n-k}$. This is why the sample space of coin tosses is given those probabilities.
:::


::: {#exm-flush-product-rule .example name="A flush, card by card" level="medium" related="exm-flush"}
The probability that a $5$-card hand is all Hearts is, by @thm-chain-rule with $A_i$ = "card $i$ is a Heart",
$$\frac{13}{52}\cdot\frac{12}{51}\cdot\frac{11}{50}\cdot\frac{10}{49}\cdot\frac{9}{48}.$$
Flushes in different suits are mutually exclusive, so the probability of a flush is $4$ times this, about $0.002$. This agrees with counting hands (@exm-flush).
:::

::: {#exm-three-dice-game .example name="At least one match on three dice" level="medium"}
You choose a number from $1$ to $6$; three fair dice are thrown, and you win if your number shows on at least one die. Let $A_i$ be "your number shows on die $i$", so $\Pr(A_i)=\frac16$.

1. Adding gives $3\cdot\frac16=\frac12$, but this is wrong: the $A_i$ overlap, and the same reasoning with six dice would give probability $1$.

2. By inclusion-exclusion (@thm-general-case) and independence of the dice,
   $$\Pr(A_1\cup A_2\cup A_3)=3\cdot\frac16-3\cdot\frac1{36}+\frac1{216}=\frac{91}{216}\approx0.42.$$
:::
