<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-1-10 origin="external" source="fit1058-cn-9.10-q10"}
Suppose events $A,B,C$ are independent. Must $A$ also be independent of
$B\cap C$? Justify with a proof or a counterexample.
:::

::: {.problem #prob-probability-1-11 origin="external" source="fit1058-cn-9.10-q11"}
Recall the network reliability problems in §9.7. All links behave
independently with survival probability $p$. Consider the network

```{=latex}
\begin{center}
    \begin{tikzpicture}[scale=0.9, dotgraph]
        \node[label=left:$S$] (S) at (0,0) {};
        \node[label=above:$M$] (M) at (2,1) {};
        \node[label=below:$N$] (N) at (2,-1) {};
        \node[label=right:$T$] (T) at (4,0) {};
        \draw (S)--(M)--(T)--(N)--(S);
        \begin{scope}[xshift=6.5cm]
            \node[label=left:$S$] (S2) at (0,0) {};
            \node[label=above:$M$] (M2) at (2,1) {};
            \node[label=below:$N$] (N2) at (2,-1) {};
            \node[label=right:$T$] (T2) at (4,0) {};
            \draw (S2)--(M2)--(T2)--(N2)--(S2);
            \draw (M2)--(N2);
        \end{scope}
    \end{tikzpicture}
    \end{center}
```

(a) (Left network.) Give an expression in $p$ for the probability that
    there is a path of surviving links from $S$ to $T$.

(b) Compare your answer to (a) with Exercise 4.8(b). Discuss the
    relationship.

(c) (Right network: add a link between $M$ and $N$.) Give an expression
    in $p$ for the probability that there is a path of surviving links
    from $S$ to $T$.

(d) Compare your answer to (c) with Exercise 4.8(c). Discuss the
    relationship.
:::

::: {.problem #prob-probability-1-13 origin="external" source="fit1058-cn-9.10-q13"}
What is the probability that a Scrabble letter is a vowel, given that it is
in the first half of the alphabet?
:::

::: {.problem #prob-probability-1-14 origin="external" source="fit1058-cn-9.10-q14"}
Prove that, for any two events $A$ and $B$, $\Pr(A\mid B)=\Pr(B\mid A)$ if and
only if the events have the same probability.
:::

::: {.problem #prob-probability-1-15 origin="external" source="fit1058-cn-9.10-q15"}
Consider again the four-node, five-link network from Exercise 11, with
$p=\frac12$.

1.  What is the probability that there is a path from $S$ to $T$?

2.  What is the probability that there is a path from $M$ to $N$?
:::

::: {.problem #prob-cs70-14-q1 origin="external" source="cs70-14.5-q1"}
Suppose five cards are dealt from a standard deck of playing cards. Let $A_i$ be the event that the $i$th card is an ace. Show that $P[A_i] = \frac{1}{13}$ for all $i = 1, \dots, 5$.
:::

::: {.problem #prob-cs70-14-q3 origin="external" source="cs70-14.5-q3"}
Show that Definitions 14.4 and 14.5 of mutual independence are equivalent.

*Note (these notes):* Definition 14.4 is @def-mutual-independence-events; Definition 14.5 is the form with complements in @prp-mutual-independence-complements.
:::

::: {.problem #prob-cs70-14-q4 origin="external" source="cs70-14.5-q4"}
In the Monty Hall problem, find $P[C_1 \cap P_1 \cap H_3]$.

*Note (these notes):* $C_i$, $P_i$ and $H_i$ are as in @exm-monty-hall.
:::

::: {.problem #prob-cs70-14-q5 origin="external" source="cs70-14.5-q5"}
In the Monty Hall problem, show that $P[H_3 \mid C_1] = \frac{1}{2}$.

*Note (these notes):* $C_i$, $P_i$ and $H_i$ are as in @exm-monty-hall.
:::

::: {.problem #prob-cs70hw-9-q6 origin="external" source="cs70hw-9-q6"}
**Monty Hall's Revenge.** Due to a quirk of the television studio's recruitment process, Monty Hall has ended up drawing all the contestants for his game show from among the ranks of former CS70 students. Unfortunately for Monty, the former students' amazing probability skills have made his cars-and-goats gimmick unprofitable for the studio. Monty decides to up the stakes by asking his contestants to generalise to three new situations with a variable number of doors, goats, and cars:

(a) There are $n$ doors for some $n > 2$. One has a car behind it, and the remaining $n - 1$ have goats. As in the ordinary Monty Hall problem, Monty will reveal one door with a goat behind it after you make your first selection. How would switching affect the odds that you select the car?

(Hint: Think about the size of the sample space for the experiment where you always switch. How many of those outcomes are favorable?)

(b) Again there are $n > 2$ doors, one with a car and $n - 1$ with goats, but this time Monty will reveal $n - 2$ doors with goats behind them instead of just one. How does switching affect the odds of winning in this modified scenario?

(c) Finally, imagine there are $k < n-1$ cars and $n-k$ goats behind the $n > 2$ doors. After you make your first pick, Monty will reveal $j < n - k$ doors with goats. What values of $j, k$ maximize the relative improvement in your odds of winning if you choose to switch? (i.e. what $j, k$ maximizes the ratio between your odds of winning when you switch, and your odds of winning when you do not switch?)
:::

::: {.problem #prob-cs70hw-10-q1 origin="external" source="cs70hw-10-q1"}
**Independent Complements.** Let $\Omega$ be a sample space, and let $A, B \subseteq \Omega$ be two independent events.

(a) Prove or disprove: $\overline{A}$ and $\overline{B}$ must be independent.

(b) Prove or disprove: $A$ and $\overline{B}$ must be independent.

(c) Prove or disprove: $A$ and $\overline{A}$ must be independent.

(d) Prove or disprove: It is possible that $A = B$.
:::

::: {.problem #prob-cs70hw-10-q3 origin="external" source="cs70hw-10-q3"}
**Flipping Coins.** Consider the following scenarios, where we apply probability to a game of flipping coins. In the game, we flip one coin each round. The game will not stop until two consecutive heads appear.

(a) What is the probability that the game ends by flipping exactly five coins?

(b) Given that the game ends after flipping the fifth coin, what is the probability that three heads appear in the sequence?

(c) If we change the rule that the game will not stop until three consecutive tails or three consecutive heads appear, what is the probability that the game stops by flipping at most six coins?
:::

::: {.problem #prob-cs70hw-10-q4 origin="external" source="cs70hw-10-q4"}
**To Be Fair.** Suppose you have a biased coin with $P(\text{heads}) \ne 0.5$. How could you use this coin to simulate a fair coin? (Hint: Think about pairs of tosses.)
:::
