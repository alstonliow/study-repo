<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-proofs-10 origin="external" source="fit1058-cn-3.15-q10"}
Consider the following algorithm:

> for each $i=1,2,\dots,n$:\
> for each $j=1,2,\dots,i$:\
> for each $k=1,2,\dots,j$:\
> \[some action\]

(a) For each pair $i,j$, how many times is the action performed?

(b) For each $i$, how many times is the action performed? Write this
    both as a sum and (using a theorem in this chapter) as a simple
    algebraic expression in $i$.

(c) Write a sum, in terms of $n$, for the total number of times the
    action is performed.

(d) Work out this expression for $n=1,2,3,4,5$ (and more).

(e) Explore how these numbers behave.

(f) Conjecture a simple algebraic expression in $n$ for the total.

(g) Prove, by induction on $n$, that your expression is correct.
:::

::: {.problem #prob-proofs-11 origin="external" source="fit1058-cn-3.15-q11"}
The $n$-th harmonic number is $H_n = 1+\frac12+\frac13+\cdots+\frac1n$. We
prove by induction that $H_n\ge\log_e(n+1)$.

(i) Inductive basis: prove that $H_1\ge\log_e(1+1)$.

(ii) Let $n\ge1$ and assume $H_n\ge\log_e(n+1)$. Write $H_{n+1}$
     recursively using $H_n$, use the inductive hypothesis, then use
     $\log_e(1+x)\le x$ and an elementary property of logarithms to show
     $H_{n+1}\ge\log_e(n+2)$.

(iii) What can you now conclude, and why?

Afterthoughts: try to prove $H_n\ge\log_e n$ directly by induction — where
is the snag? Would the proof work for other bases? Can you prove
$H_n\le(\log_e n)+1$?
:::

::: {.problem #prob-cs70-3-q2 origin="external" source="cs70-3.6-q2"}
In real analysis, Bernoulli's Inequality is an inequality which approximates the exponentiations of $1 + x$. Prove this inequality, which states that $(1 + x)^n \ge 1 + nx$ if $n$ is a natural number and $1 + x > 0$.
:::

::: {.problem #prob-cs70-3-q3 origin="external" source="cs70-3.6-q3"}
A common recursively defined function is the factorial, defined for a nonnegative number $n$ as $n! = n(n - 1)(n - 2)\dots1$, with base case $0! = 1$. Let us reinforce our understanding of the connection between recursion and induction by considering the following theorem involving factorials.

Theorem: For all $n \in \mathbb{N}$, $n > 1 \implies n! < n^n$.

Prove this theorem using induction. (Hint: In the Inductive Step, write $(n + 1)! = (n + 1) \cdot n!$, and use the Induction Hypothesis.)
:::

::: {.problem #prob-cs70-3-q4 origin="external" source="cs70-3.6-q4"}
A celebrity at a party is someone whom everyone knows, yet who knows no one. Suppose that you are at a party with $n$ people. For any pair of people $A$ and $B$ at the party, you can ask $A$ if they know $B$ and receive an honest answer. Give a recursive algorithm to determine whether there is a celebrity at the party, and if so who, by asking at most $3n - 4$ questions. (Note: for the purpose of this question you are just visiting the party to ask questions. What you are trying to determine is whether the $n$ people actually attending the party include a celebrity.)

Prove by induction that your algorithm always correctly identifies a celebrity if there is one, and that the number of questions is at most $3n - 4$.
:::

::: {.problem #prob-cs70-3-q5 origin="external" source="cs70-3.6-q5"}
Use the proof of Theorem 3.6 to design an algorithm that, given any amount of postage of at least 12¢, outputs the numbers of 4¢ and 5¢ stamps that make up this postage. What's the largest number of 5¢ stamps your algorithm will ever use?

*Note (these notes):* Theorem 3.6 of CS70 Note 3 is @exm-postage-four-five.
:::

::: {.problem #prob-cs70hw-2-q2 origin="external" source="cs70hw-2-q2"}
**Negative pacman returns.** Pacman has had a bit of a wild night, and wakes up feeling a bit under the weather. He starts at some location $(i, j) \in \mathbb{N}^2$ in the third quadrant, and is constrained walk on the infinite 2D grid and stay in the third quadrant (say, by walls along the negative x and negative y axes). Every second he does one of the following (if possible):

(i) Walk one step up, to $(i, j + 1)$.

(ii) Walk one step right, to $(i + 1, j)$.

For example, if he is at $(-5, 0)$, his only option is to walk right to $(-4, 0)$; if Pacman is instead at $(-3, -2)$, he could walk either to $(-2, -2)$ or $(-3, -1)$.

Prove by induction that no matter how he walks, he will always reach $(0, 0)$ in finite time. (Hint: Try starting Pacman at a few small points like $(-2, -1)$ and looking all the different paths he could take to reach $(0, 0)$. Do you notice a pattern?)

*Note (these notes):* The positions meant are those with $i,j\le0$ (the third quadrant), as the example $(-5,0)$ shows.
:::

::: {.problem #prob-cs70hw-2-q3 origin="external" source="cs70hw-2-q3"}
**Losing Marbles.** Two EECS70 GSIs have inexplicably run out of research topics to pursue, papers to read, or homeworks to create, and so they decide to play an incredibly boring game. (This is EECS after all.)

In the game, there is an urn that contains some number of red marbles ($R$), green marbles ($G$), and blue marbles ($B$). There is also an infinite supply of marbles outside the urn.

When it is a player's turn, the player may either:

(i) Remove one red marble from the urn, and add 3 green marbles.

(ii) Remove two green marbles from the urn, and add 7 blue marbles.

(iii) Remove one blue marble from the urn.

These are the only legal moves. The last player that can make a legal move wins. We play optimally, of course – meaning we always play one of the best possible legal moves.

(a) If the urn contains $(R, G, B)$ red, green, and blue marbles initially, then determine the conditions on $R, G, B$ for the first player to win the game. Prove it. In this case, does it matter what strategy the players use?

Hint: Assign each marble a weight, and argue that at every step, the combined weight will go down by exactly 1.

(b) Prove by induction that, if the urn initially contains a finite number of marbles at the start of the game, then the game will end after a finite number of moves.

*Note (these notes):* The official solution states that the final weight is $0$; it can also be $4$ (one green marble left), which does not change the answer because $4$ is even.
:::
