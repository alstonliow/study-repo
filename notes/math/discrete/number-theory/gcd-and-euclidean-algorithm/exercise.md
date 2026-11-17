<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-number-theory-12 origin="external" source="fit1058-cn-7.19-q12"}
Use the Euclidean algorithm to find the gcd of the consecutive Fibonacci
numbers 34 and 55. What do you notice about the other numbers found at each
step?

Prove, by induction on $n$, that for all $n\ge3$ the Euclidean algorithm uses
$n-2$ subtractions to compute $\gcd(f_n,f_{n+1})$, and that every
intermediate number found is also a Fibonacci number.
:::

::: {.problem #prob-cs70hw-4-q1 origin="external" source="cs70hw-4-q1"}
**Fibonacci GCD.** The Fibonacci sequence is given by $F_n = F_{n-1} + F_{n-2}$, where $F_0 = 0$ and $F_1 = 1$. Prove that, for all $n \ge 0$, $\gcd(F_n, F_{n-1}) = 1$.
:::

::: {.problem #prob-mit6042f10-3-q2 origin="external" source="mit6042f10-3-q2"}
Prove the following statements, assuming all numbers are positive integers.

(a) If $a \mid b$, then $\forall c$, $a \mid bc$

(b) If $a \mid b$ and $a \mid c$, then $a \mid sb + tc$.

(c) $\forall c$, $a \mid b \iff ca \mid cb$

(d) $\gcd(ka, kb) = k \gcd(a, b)$
:::

::: {.problem #prob-mit6042f10-3-q5 origin="external" source="mit6042f10-3-q5"}
Here is a very, very fun game. We start with two distinct, positive integers written on a blackboard. Call them $x$ and $y$. You and I now take turns. (I'll let you decide who goes first.) On each player's turn, he or she must write a new positive integer on the board that is a common divisor of two numbers that are already there. If a player can not play, then he or she loses.

For example, suppose that 12 and 15 are on the board initially. Your first play can be 3 or 1. Then I play 3 or 1, whichever one you did not play. Then you can not play, so you lose.

(a) Show that every number on the board at the end of the game is either $x$, $y$, or a positive divisor of $\gcd(x, y)$.

(b) Show that every positive divisor of $\gcd(x, y)$ is on the board at the end of the game.

(c) Describe a strategy that lets you win this game every time.
:::
