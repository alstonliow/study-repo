<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-number-theory-01 origin="external" source="fit1058-cn-7.19-q1"}
(a) Write the statement that integer $d$ is a divisor of integer $n$ as
    a predicate logic expression, using integer multiplication and
    without using $\mid$.

(b) Write the statement that integer $n$ is prime as a predicate logic
    expression. You may use $\mid$ and $\le$.

(c) Write the statement that $d$ is the greatest common divisor of $m$
    and $n$ as a predicate logic expression, using $\mid$ and $\le$.
:::

::: {.problem #prob-number-theory-02 origin="external" source="fit1058-cn-7.19-q2"}
A positive integer $n$ is *perfect* if it equals the sum of its own
proper divisors.

(a) Show by direct calculation that the first two perfect numbers are
    6 and 28.

(b) Verify that 496 is perfect.
:::

::: {.problem #prob-number-theory-05 origin="external" source="fit1058-cn-7.19-q5"}
The online game Primel (<https://converged.yt/primel/>) is about
guessing an unknown five-digit prime (like Wordle). Non-prime guesses are not
penalised but give no information; you have at most six prime guesses.

(a) Are there any prohibitions on certain digits in certain positions
    in prime numbers in general? What does this mean for the digits in
    your first guess?

(b) The density of primes decreases as numbers get higher (e.g. more
    five-digit primes start with 1 than with 5). What five digits
    would be best in your first guess? Which five-digit prime do you
    recommend?

(c) Try asking ChatGPT for help choosing your next guess, and check
    whether its suggestions are actually prime. How many attempts are
    necessary before it gives an actual prime satisfying the conditions?
:::

::: {.problem #prob-number-theory-09 origin="external" source="fit1058-cn-7.19-q9"}
Prove each of the following.

(a) $4\mid n$ iff the last two decimal digits of $n$ give a multiple
    of 4.

(b) $8\mid n$ iff the last three decimal digits of $n$ give a multiple
    of 8.

(c) $25\mid n$ iff the last two decimal digits of $n$ give a multiple
    of 25.

(d) Extend (a) and (b) to higher powers of 2.

(e) (Challenge) For which $d$ can divisibility of $n$ by $d$ be tested
    by looking only at some constant number of digits at the end of
    $n$?
:::

::: {.problem #prob-mit6042f10-3-q6 origin="external" source="mit6042f10-3-q6"}
In one of the previous problems, you calculated square roots of numbers modulo primes equivalent to 3 modulo 4. In this problem you will prove that there are an infinite number of such primes!

(a) As a warm-up, prove that there are an infinite number of prime numbers. (Hint: Suppose that the set $F$ of all prime numbers is finite, that is $F = \{p_1, p_2, \ldots, p_k\}$ and define $n = p_1 p_2 \cdots p_k + 1$.)

(b) Prove that if $p$ is an odd prime, then $p \equiv 1 \pmod 4$ or $p \equiv 3 \pmod 4$.

(c) Prove that if $n \equiv 3 \pmod 4$, then $n$ has a prime factor $p \equiv 3 \pmod 4$.

(d) Let $F$ be the set of all primes $p$ such that $p \equiv 3 \pmod 4$. Prove by contradiction that $F$ has an infinte number of primes.

(Hint: Suppose that $F$ is finite, that is $F = \{p_1, p_2, \ldots, p_k\}$ and define $n = 4p_1 p_2 \cdots p_k - 1$. Prove that there exists a prime $p_i \in F$ such that $p_i \mid n$.)
:::
