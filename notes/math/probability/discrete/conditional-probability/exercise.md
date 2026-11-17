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

::: {.problem #prob-mit6042f10-10-q1 origin="external" source="mit6042f10-10-q1"}
Suppose $\Pr\{\} : S \to [0, 1]$ is a probability function on a sample space, $S$, and let $B$ be an event such that $\Pr\{B\} > 0$. Define a function $\Pr_B\{\cdot\}$ on outcomes $w \in S$ by the rule:
$$\Pr_B\{w\} = \begin{cases}\Pr\{w\}/\Pr\{B\} & \text{if } w \in B,\\ 0 & \text{if } w \notin B.\end{cases} \tag{1}$$

(a) Prove that $\Pr_B\{\cdot\}$ is also a probability function on $S$ according to Definition 14.4.2.

(b) Prove that
$$\Pr_B\{A\} = \frac{\Pr\{A \cap B\}}{\Pr\{B\}}$$
for all $A \subseteq S$.

*Note (these notes):* Definition 14.4.2 refers to the 2010 course notes; it is the definition of a probability function on a sample space, @def-probability-general-case.
:::

::: {.problem #prob-mit6042f10-10-q6 origin="external" source="mit6042f10-10-q6"}
I have a deck of 52 regular playing cards, 26 red, 26 black, randomly shuffled. They all lie face down in the deck so that you can't see them. I will draw a card off the top of the deck and turn it face up so that you can see it and then put it aside. I will continue to turn up cards like this but at some point while there are still cards left in the deck, you have to declare that you want the next card in the deck to be turned up. If that next card turns up black you win and otherwise you lose. Either way, the game is then over.

(a) Show that if you take the first card before you have seen any cards, you then have probability 1/2 of winning the game.

(b) Suppose you don't take the first card and it turns up red. Show that you have then have a probability of winning the game that is greater than 1/2.

(c) If there are $r$ red cards left in the deck and $b$ black cards, show that the probability of winning in you take the next card is $b/(r + b)$.

(d) Either,

1. come up with a strategy for this game that gives you a probability of winning strictly greater than 1/2 and prove that the strategy works, or,
2. come up with a proof that no such strategy can exist.
:::

::: {.problem #prob-mit6042f10-11-q1 origin="external" source="mit6042f10-11-q1"}
You are organizing a neighborhood census and instruct your census takers to knock on doors and note the sex of any child that answers the knock. Assume that there are two children in a household and that girls and boys are equally likely to be children and to open the door.

A sample space for this experiment has outcomes that are triples whose first element is either B or G for the sex of the elder child, likewise for the second element and the sex of the younger child, and whose third coordinate is E or Y indicating whether the elder child or younger child opened the door. For example, (B, G, Y) is the outcome that the elder child is a boy, the younger child is a girl, and the girl opened the door.

(a) Let $T$ be the event that the household has two girls, and $O$ be the event that a girl opened the door. List the outcomes in $T$ and $O$.

(b) What is the probability $\Pr(T \mid O)$, that both children are girls, given that a girl opened the door?

(c) Where is the mistake in the following argument for computing $\Pr(T \mid O)$?

> If a girl opens the door, then we know that there is at least one girl in the household. The probability that there is at least one girl is
> $$1 - \Pr(\text{both children are boys}) = 1 - (1/2 \times 1/2) = 3/4.$$
> So,
> $$\begin{aligned}\Pr(T \mid \text{there is at least one girl in the household}) &= \frac{\Pr(T \cap \text{there is at least one girl in the household})}{\Pr\{\text{there is at least one girl in the household}\}}\\ &= \frac{\Pr(T)}{\Pr\{\text{there is at least one girl in the household}\}}\\ &= (1/4)/(3/4) = 1/3.\end{aligned}$$
> Therefore, given that a girl opened the door, the probability that there are two girls in the household is 1/3.
:::

::: {.problem #prob-mit6042f10-11-q4 origin="external" source="mit6042f10-11-q4"}
We're covering probability in 6.042 lecture one day, and you volunteer for one of Professor Leighton's demonstrations. He shows you a coin and says he'll bet you \$1 that the coin will come up heads. Now, you've been to lecture before and therefore suspect the coin is biased, such that the probability of a flip coming up heads, $\Pr\{H\}$, is $p$ for $1/2 < p \le 1$.

You call him out on this, and Professor Leighton offers you a deal. He'll allow you to come up with an algorithm using the biased coin to simulate a fair coin, such that the probability you win and he loses, $\Pr\{W\}$, is equal to the probability that he wins and you lose, $\Pr\{L\}$.

You come up with the following algorithm:

1. Flip the coin twice.
2. Based on the results:
   - $TH \Rightarrow$ you win [W], and the game terminates.
   - $HT \Rightarrow$ Professor Leighton wins [L], and the game terminates.
   - $(HH \lor TT) \Rightarrow$ discard the result and flip again.
3. If at the end of $N$ rounds nobody has won, declare a tie.

As an example, for $N = 3$, an outcome of $HT$ would mean the game ends early and you lose, $HHTH$ would mean the game ends early and you win, and $HHTTTT$ would mean you play the full $N$ rounds and result in a tie.

(a) Assume the flips are mutually independent. Show that $\Pr\{W\} = \Pr\{L\}$.

(b) Show that, if $p < 1$, the probability of a tie goes to 0 as $N$ goes to infinity.
:::

::: {.problem #prob-mit6042f10-11-q5 origin="external" source="mit6042f10-11-q5"}
(a) Suppose $A$ and $B$ are disjoint events. Prove that $A$ and $B$ are not independent, unless $\Pr(A)$ or $\Pr(B)$ is zero.

(b) If $A$ and $B$ are independent, prove that $A$ and $\overline{B}$ are also independent.

Hint: $\Pr\bigl(A \cap \overline{B}\bigr) = \Pr(A) - \Pr(A \cap B)$.

(c) Give an example of events $A$, $B$, $C$ such that $A$ is independent of $B$, $A$ is independent of $C$, but $A$ is not independent of $B \cup C$.

(d) Prove that if $C$ is independent of $A$, and $C$ is independent of $B$, and $C$ is independent of $A \cap B$, then $C$ is independent of $A \cup B$.

Hint: Calculate $\Pr(A \cup B \mid C)$.
:::

::: {.problem #prob-mit6042f10-11-q6 origin="external" source="mit6042f10-11-q6"}
Three very rare DNA markers were found in the DNA collected at a crime scene. Only one in every 1,000 people has marker A, one in every 3,000 people has marker B, and one in every 5,000 people has marker C. Joe the plumber was arrested and accused of committing the crime, because he had all those markers present in his DNA.

The prosecutor argues that the chances of any person having all three DNA markers is
$$\frac{1}{1000} \cdot \frac{1}{3000} \cdot \frac{1}{5000} = \frac{1}{15{,}000{,}000{,}000},$$
which is more than 1 over the number of people in the world. This, plus the fact that Joe the plumber lives only 100 miles away from the crime scene must clearly mean that he is guilty. Having taken 6.042, you should be suspicious of this reasoning.

(a) What assumption has the prosecutor made (even though he hasn't realized it) about the presence of the 3 markers in human DNA?

(b) What would be the probability of a person having all three markers assuming that the markers appear pairwise independently? Under this assumption, can it be stated with such certainty that Joe the plumber commited the crime?

(c) What can you say about the probability of a person having all three markers if there is no independence between the markers?

(d) In fact, it turns out that neither of the above assumptions is correct. A researcher from MIT (who was actually in your recitation section for 6.042 back in the day) has discovered that while markers B and C appear independently, the probability of having marker B if you have marker A is $\frac12$ and the probability of having marker C if you have marker A is $\frac13$. The defence attorney now argues that the probability of a randomly selected person having all three markers is
$$\Pr[A \cap B \cap C] = \Pr[A] \cdot \Pr[B \mid A] \cdot \Pr[C \mid A] = \frac{1}{1000} \cdot \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6{,}000}.$$
Called as a witness, the MIT researcher points out that this is not necessarily true and that in fact he himself does not know what the probability is. What is wrong with the defence attorney's reasoning? (We assume that the MIT researcher published correct information and that, since he took 6.042, he knows what he is talking about.)
:::
