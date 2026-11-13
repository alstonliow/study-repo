<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-sequences-02 origin="external" source="fit1058-cn-6.16-q2"}
Define $(a_n:n\in\mathbb{N})$ by $a_1=2$, $a_n=2n\,a_{n-1}$.

(a) Find the first five terms.

(b) Prove by induction on $n$ that $a_n=2^n n!$.
:::

::: {.problem #prob-sequences-03 origin="external" source="fit1058-cn-6.16-q3"}
Define $(b_n:n\in\mathbb{N})$ by $b_1=3$, $b_n=b_{n-1}^2$.

(a) Explore this sequence.

(b) Conjecture a formula for the sequence.

(c) Prove that the formula is correct, by induction.
:::

::: {.problem #prob-sequences-04 origin="external" source="fit1058-cn-6.16-q4"}
Define $(q_n:n\in\mathbb{N})$ by $q_1=3$, $q_2=5$, $q_n=3q_{n-1}-2q_{n-2}$.

(a) Explore this sequence. Find the first seven terms.

(b) Conjecture a formula for the sequence.

(c) Prove that the formula is correct, by induction.
:::

::: {.problem #prob-sequences-05 origin="external" source="fit1058-cn-6.16-q5"}
Define $(g_n:n\in\mathbb{N})$ by $g_1=0$, $g_n=g_{n-1}+\log n$. Prove by induction on
$n$ that
$$g_n\le n\log n-n+H_n,$$
where $H_n=1+\frac12+\cdots+\frac1n$ (see Exercise 3.11). It may help to use
$\log(1+x)\le x$ for all $x\ge-1$, and
$$\log(n-1)=\log\Bigl(n\cdot\frac{n-1}{n}\Bigr)
        =\log\Bigl(n\Bigl(1-\frac1n\Bigr)\Bigr)
        =\log n+\log\Bigl(1-\frac1n\Bigr).$$
(All logarithms are natural logarithms.)
:::

::: {.problem #prob-sequences-06 origin="external" source="fit1058-cn-6.16-q6"}
Use the explore-conjecture-prove method to develop the best upper bound you
can for the $n$-th term of
$$r_1=1,\qquad r_n=3r_{n-1}-1,$$
and prove your bound by induction. Even better, find a formula for $r_n$ and
prove it by induction.
:::
