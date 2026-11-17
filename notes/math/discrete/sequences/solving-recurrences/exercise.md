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

::: {.problem #prob-mit6042f10-8-q1 origin="external" source="mit6042f10-8-q1"}
Find $\Theta$ bounds for the following divide-and-conquer recurrences. Assume $T(1) = 1$ in all cases. Show your work.

(a) $T(n) = 8T(\lfloor n/2 \rfloor) + n$

(b) $T(n) = 2T(\lfloor n/8 \rfloor + 1/n) + n$

(c) $T(n) = 7T(\lfloor n/20 \rfloor) + 2T(\lfloor n/8 \rfloor) + n$

(d) $T(n) = 2T(\lfloor n/4 \rfloor + 1) + n^{1/2}$

(e) $T(n) = 3T(\lfloor n/9 + n^{1/9} \rfloor) + 1$
:::

::: {.problem #prob-mit6042f10-8-q2 origin="external" source="mit6042f10-8-q2"}
It is easy to misuse induction when working with asymptotic notation.

**False Claim** If
$$T(1) = 1 \text{ and } T(n) = 4T(n/2) + n$$
Then $T(n) = O(n)$.

**False Proof** We show this by induction. Let $P(n)$ be the proposition that $T(n) = O(n)$.

*Base Case:* $P(1)$ is true because $T(1) = 1 = O(1)$.

*Inductive Case:* For $n \ge 1$, assume that $P(n - 1), \ldots, P(1)$ are true. We then have that
$$T(n) = 4T(n/2) + n = 4O(n/2) + n = O(n)$$
And we are done.

(a) Identify the flaw in the above proof.

(b) A simple attempt to prove $T(n) \ne O(n)$ via induction ultimately fails. We assume for sake of contradiction that $T(n) = O(n)$. Then there exists positive integer $n_0$ and positive real number $c$ such that for all $n \ge n_0$, $T(n) \le cn$. We then define $P(n)$ as the proposition that $T(n) \le cn$.

We then proceed with strong induction.

*Base Case, $n = n_0$:* $P(n_0)$ is true, by assumption.

*Inductive Step:* We assume $P(n_0), P(n_0 + 1), \ldots, P(n - 1)$ true.

Fill in the rest of this proof attempt, and explain why it doesn't work.

Note: As this problem was updated so late, the graders will be instructed to be exceedingly lenient when grading this.

(c) Using Akra-Bazzi theorem, find the correct asymptotic behavior of this recurrence.

(d) We have now seen several recurrences of the form $T(n) = aT(\lfloor n/b \rfloor) + n$. Some of them give a runtime that is $O(n)$, and some don't. Find the relationship between $a$ and $b$ that yields $T(n) = O(n)$, and prove that this is sufficient.
:::

::: {.problem #prob-mit6042f10-8-q4 origin="external" source="mit6042f10-8-q4"}
Find closed-form solutions to the following linear recurrences.

(a) $x_n = 4x_{n-1} - x_{n-2} - 6x_{n-3}$ $\quad(x_0 = 3, x_1 = 4, x_2 = 14)$

(b) $x_n = -x_{n-1} + 2x_{n-2} + n$ $\quad(x_0 = 5, x_1 = -4/9)$
:::
