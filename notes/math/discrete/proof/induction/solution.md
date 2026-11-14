<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-proofs-06" status="draft"}
(a) The $k$-th odd number is $2k-1$.

(b) For $k = 1$, the sum of the first odd number is $1 = 1^2$.

(c) The first $k+1$ odd numbers are the first $k$ plus the $(k+1)$-th, which
    is $2(k+1)-1 = 2k+1$:
    $$\sum_{i=1}^{k+1}(2i-1) = \sum_{i=1}^{k}(2i-1) + (2k+1).$$

(d) By the inductive hypothesis, $\sum_{i=1}^{k}(2i-1) = k^2$, so the sum is
    $$k^2 + 2k + 1.$$

(e) $k^2 + 2k + 1 = (k+1)^2$. This is $(*)$ for $k+1$.

(f) We proved $(*)$ for $k = 1$, and that $(*)$ for $k$ implies $(*)$ for
    $k+1$. By the Principle of Mathematical Induction, $(*)$ holds for all
    $k\ge1$.
:::

::: {.solution for="prob-proofs-07" status="draft"}
Let $P(n)$ be the statement $\sum_{i=0}^n 2^i = 2^{n+1}-1$.

1. *Base case $n = 0$.* The left side is $2^0 = 1$, and the right side is
   $2^1 - 1 = 1$.

2. *Inductive step.* Let $n\ge0$ and assume $P(n)$. Then
   $$\sum_{i=0}^{n+1}2^i = \sum_{i=0}^{n}2^i + 2^{n+1} = (2^{n+1}-1) + 2^{n+1} = 2^{n+2}-1,$$
   which is $P(n+1)$.

3. By the Principle of Mathematical Induction, $P(n)$ holds for all
   $n\in\mathbb N_0$.
:::

::: {.solution for="prob-proofs-08" status="draft"}
Let $P(n)$ be the statement $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}6$.

1. *Base case $n = 1$.* Both sides equal $1$, since
   $\frac{1\cdot2\cdot3}{6} = 1$.

2. *Inductive step.* Let $n\ge1$ and assume $P(n)$. Then
   $$\sum_{i=1}^{n+1}i^2 = \frac{n(n+1)(2n+1)}6 + (n+1)^2 = \frac{(n+1)\bigl(n(2n+1) + 6(n+1)\bigr)}6.$$

3. The bracket is $2n^2 + 7n + 6 = (n+2)(2n+3)$. So the sum is
   $$\frac{(n+1)(n+2)(2n+3)}6 = \frac{(n+1)\bigl((n+1)+1\bigr)\bigl(2(n+1)+1\bigr)}6,$$
   which is $P(n+1)$.

4. By the Principle of Mathematical Induction, $P(n)$ holds for all
   $n\ge1$. (For $n = 0$ both sides are $0$.)
:::

::: {.solution for="prob-proofs-09" status="draft"}
We use $1 + 2 + \cdots + n = \frac{n(n+1)}2$, so the claim is
$$\sum_{i=1}^n i^3 = \frac{n^2(n+1)^2}4.$$
Call this $P(n)$.

1. *Base case $n = 1$.* Both sides equal $1$.

2. *Inductive step.* Let $n\ge1$ and assume $P(n)$. Then
   $$\sum_{i=1}^{n+1}i^3 = \frac{n^2(n+1)^2}4 + (n+1)^3 = \frac{(n+1)^2\bigl(n^2 + 4(n+1)\bigr)}4.$$

3. $n^2 + 4n + 4 = (n+2)^2$, so the sum is
   $$\frac{(n+1)^2(n+2)^2}4 = \Bigl(\frac{(n+1)(n+2)}2\Bigr)^2 = (1 + 2 + \cdots + (n+1))^2,$$
   which is $P(n+1)$.

4. By the Principle of Mathematical Induction, $P(n)$ holds for all $n\ge1$.
:::

::: {.solution for="prob-proofs-13" status="draft"}
The "theorem" is false, and the error is in step 4.

1. Steps 1–3 are correct for $n = 0, 1, 2$.

2. Step 4 claims, from three small cases, that a new line can always cut every
   existing piece in two. This is never justified, and it is false. A
   straight line is convex: it meets each existing line at most once, so
   with $n$ lines already drawn it crosses at most $n$ of them, and it passes
   through at most $n+1$ pieces. So it adds at most $n+1$ pieces, not as many
   as already exist.

3. Concretely, with $3$ lines the maximum is $1 + 1 + 2 + 3 = 7 < 8 = 2^3$
   pieces. In general, $n$ lines give at most $1 + \frac{n(n+1)}2$ pieces.

4. Step 5 is not a valid induction either: there is no inductive step that
   was actually proved. "It is clear from the cases so far" is extrapolation
   from a pattern, not a proof.
:::
