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
