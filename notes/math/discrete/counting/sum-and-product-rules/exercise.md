<!-- Migrated from 1058note exercises/chapters/08-counting-combinatorics.tex (CN 8.10 Exercises). -->

::: {.problem #prob-counting-01 origin="external" source="fit1058-cn-8.10-q1"}
Consider the following algorithm.

| for $i$ from 1 to $a$ do
|   for $j$ from 1 to $b$ do
|     for $k$ from 1 to $c$ do
|       for $l$ from 1 to $d$ do
|         beep!
|   for $m$ from 1 to $e$ do
|     for $n$ from 1 to $f$ do
|       beep!
|     for $o$ from 1 to $g$ do
|       beep!
|     for $p$ from 1 to $h$ do
|       beep!

(a) Give an expression in $a,b,c,d,e,f,g,h$ for the number of times
    this algorithm beeps.
(b) If each of these eight variables is $O(n)$, give a big-O expression
    for the number of beeps.
:::

::: {.problem #prob-counting-03 origin="external" source="fit1058-cn-8.10-q3"}
Two fair dice are thrown; the outcome is the ordered pair of numbers shown.

(a) How many possible outcomes are there?
(b) How many outcomes have the first number less than the second?
(c) How many outcomes have sum 7?
(d) How many outcomes have both numbers $\le3$?
(e) How many outcomes have neither number equal to 5?
:::

::: {.problem #prob-cs70hw-6-q6 origin="external" source="cs70hw-6-q6"}
**Good Game.** Player will send 'GG' (Good Game) to the winner after each defeat in a 1v1 competitive game. Maru is a skilled Terran player in the Game. And he is 27 pts behind Player Sierral. Suppose Sierral has finished all of his games and Maru has 10 games to go. If Maru wins the $i$-th game, he will get $i$ pts.

(a) What's the maximum number of GGs that Maru can send and have a higher points than Sierral?

(b) How many different ways that Maru can defeat Sierral (earns more than 27 pts)?
:::

::: {.problem #prob-cs70hw-7-q2 origin="external" source="cs70hw-7-q2"}
**Palindromes.** How many 5-digit palindromes are there? (A palindrome is a number that reads the same way forwards and backwards. For example, 27872 and 48484 are palindromes, but 28389 and 12541 are not.)
:::
