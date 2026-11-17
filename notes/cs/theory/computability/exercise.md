::: {.problem #prob-cs70hw-9-q1 origin="external" source="cs70hw-9-q1"}
**Unprogrammable Programs.** Prove whether the programs described below can exist or not.

(a) A program $P(F, x, y)$ that returns true if the program $F$ outputs $y$ when given $x$ as input (i.e. $F(x) = y$) and false otherwise.

(b) A program $P$ that takes two programs $F$ and $G$ as arguments, and returns true if $F$ and $G$ halt on the same set of inputs (or false otherwise).
:::

::: {.problem #prob-cs70hw-9-q2 origin="external" source="cs70hw-9-q2"}
**Computations on Programs.**

(a) Is it possible to write a program that takes a natural number $n$ as input, and finds the shortest arithmetic formula which computes $n$? For the purpose of this question, a formula is a sequence consisting of some valid combination of (decimal) digits, standard binary operators ($+$, $\times$, the "^" operator that raises to a power), and parentheses. We define the length of a formula as the number of characters in the formula. Specifically, each operator, decimal digit, or parentheses counts as one character.

(Hint: Think about whether it's possible to enumerate the set of possible arithmetic formulas. How would you know when to stop?)

(b) Now say you wish to write a program that, given a natural number input $n$, finds another program (e.g. in Java or C) which prints out $n$. The discovered program should have the minimum execution-time-plus-length of all the programs that print $n$. Execution time is measured by the number of CPU instructions executed, while "length" is the number of characters in the source code. Can this be done?

(Hint: Is it possible to tell whether a program halts on a given input within $t$ steps? What can you say about the execution-time-plus-length of the program if you know that it does not halt within $t$ steps?)
:::

::: {.problem #prob-cs70hw-9-q3 origin="external" source="cs70hw-9-q3"}
**Kolmogorov Complexity.** Compressing a bit string $x$ of length $n$ can be interpreted as the task of creating a program of fewer than $n$ bits that returns $x$. The Kolmogorov complexity of a string $K(x)$ is the length of an optimally-compressed copy of $x$; that is, $K(x)$ is the length of shortest program that returns $x$.

(a) Explain why the notion of the "smallest positive integer that cannot be defined in under 280 characters" is paradoxical.

(b) Prove that for any length $n$, there is at least one string of bits that cannot be compressed to less than $n$ bits.

(c) Say you have a program $K$ that outputs the Kolmogorov complexity of any input string. Under the assumption that you can use such a program $K$ as a subroutine, design another program $P$ that takes an integer $n$ as input, and outputs the length-$n$ binary string with the highest Kolmogorov complexity. If there is more than one string with the highest complexity, output the one that comes first alphabetically.

(d) Let's say you compile the program $P$ you just wrote and get an $m$ bit executable, for some $m \in \mathbb{N}$ (i.e. the program $P$ can be represented in $m$ bits). Prove that the program $P$ (and consequently the program $K$) cannot exist.

(Hint: Consider what happens when $P$ is given a very large input $n$.)
:::
