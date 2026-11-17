<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-proofs-06 origin="external" source="fit1058-cn-3.15-q6"}
Prove by mathematical induction: for all $k$,
$$(*)\qquad \text{the sum of the first $k$ odd numbers equals } k^2.$$

(a) Give a simple expression for the $k$-th odd number.

(b) Inductive basis: prove $(*)$ for $k=1$.

(c) Inductive step: let $k\ge1$ and assume $(*)$ for $k$. Express the
    sum of the first $k+1$ odd numbers in terms of the sum of the first
    $k$ odd numbers, plus something else.

(d) Use the inductive hypothesis to replace the sum of the first $k$ odd
    numbers by something else.

(e) Simplify your expression. What do you notice?

(f) Draw your final conclusion, stating that you are using the
    Principle of Mathematical Induction.
:::

::: {.problem #prob-proofs-07 origin="external" source="fit1058-cn-3.15-q7"}
Prove by induction on $n$ that, for all $n\in\mathbb{N}_0$,
$$1+2+2^2+2^3+\cdots+2^n = 2^{n+1}-1.$$
:::

::: {.problem #prob-proofs-08 origin="external" source="fit1058-cn-3.15-q8"}
Prove by induction that, for all $n$:
$$1^2+2^2+\cdots+n^2 = \frac{n(n+1)(2n+1)}{6}.$$
:::

::: {.problem #prob-proofs-09 origin="external" source="fit1058-cn-3.15-q9"}
Prove by induction that, for all $n$:
$$1^3+2^3+\cdots+n^3 = (1+2+\cdots+n)^2.$$
:::

::: {.problem #prob-proofs-13 origin="external" source="fit1058-cn-3.15-q13"}
Identify the errors in the following “theorem” and “proof”.

**“Theorem.”** For all $n\in\mathbb{N}$, a circular disc can be cut into $2^n$
pieces by $n$ straight lines.

**“Proof.”**

1.  For $n=0$ the disc is in one piece $=2^0$.

2.  For $n=1$, a single line cuts it into two pieces $=2^1$.

3.  For $n=2$, a second line crossing the first cuts across both pieces,
    giving $2\times2=2^2$ pieces.

4.  It is clear from the cases so far that, once the circle is cut by
    some number of lines, another line can be used to divide every
    piece into two, doubling the number of pieces.

5.  So with $n$ lines, repeated doubling gives $2^n$ pieces. “$\square$”
:::

::: {.problem #prob-cs70-3-q1 origin="external" source="cs70-3.6-q1"}
Prove for any natural number $n$ that $1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{1}{6}n(n + 1)(2n + 1)$.
:::

::: {.problem #prob-cs70hw-2-q1 origin="external" source="cs70hw-2-q1"}
**Induction.** Prove the following using induction:

(a) For all natural numbers $n > 2$, $2^n > 2n + 1$.

(b) For all positive integers $n$, $1^2 + 2^2 + 3^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$.

(c) For all positive natural numbers $n$, $\frac{5}{4} \cdot 8^n + 3^{3n-1}$ is divisible by 19.
:::

::: {.problem #prob-mit6042f10-2-q4 origin="external" source="mit6042f10-2-q4"}
Find the flaw in the following bogus proof that $a^n = 1$ for all nonnegative integers $n$, whenever $a$ is a nonzero real number.

*Proof.* The bogus proof is by induction on $n$, with hypothesis
$$P(n) ::= \forall k \le n.\ a^k = 1,$$
where $k$ is a nonnegative integer valued variable.

*Base Case:* $P(0)$ is equivalent to $a^0 = 1$, which is true by definition of $a^0$. (By convention, this holds even if $a = 0$.)

*Inductive Step:* By induction hypothesis, $a^k = 1$ for all $k \in \mathbb{N}$ such that $k \le n$. But then
$$a^{n+1} = \frac{a^n \cdot a^n}{a^{n-1}} = \frac{1 \cdot 1}{1} = 1,$$
which implies that $P(n + 1)$ holds. It follows by induction that $P(n)$ holds for all $n \in \mathbb{N}$, and in particular, $a^n = 1$ holds for all $n \in \mathbb{N}$.
:::

::: {.problem #prob-mit6042f10-2-q5 origin="external" source="mit6042f10-2-q5"}
Let the sequence $G_0, G_1, G_2, \ldots$ be defined recursively as follows: $G_0 = 0$, $G_1 = 1$, and $G_n = 5G_{n-1} - 6G_{n-2}$, for every $n \in \mathbb{N}$, $n \ge 2$.

Prove that for all $n \in \mathbb{N}$, $G_n = 3^n - 2^n$.
:::
