<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-proofs-06"}
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

::: {.solution for="prob-proofs-07"}
Let $P(n)$ be the statement $\sum_{i=0}^n 2^i = 2^{n+1}-1$.

1. *Base case $n = 0$.* The left side is $2^0 = 1$, and the right side is
   $2^1 - 1 = 1$.

2. *Inductive step.* Let $n\ge0$ and assume $P(n)$. Then
   $$\sum_{i=0}^{n+1}2^i = \sum_{i=0}^{n}2^i + 2^{n+1} = (2^{n+1}-1) + 2^{n+1} = 2^{n+2}-1,$$
   which is $P(n+1)$.

3. By the Principle of Mathematical Induction, $P(n)$ holds for all
   $n\in\mathbb N_0$.
:::

::: {.solution for="prob-proofs-08"}
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

::: {.solution for="prob-proofs-09"}
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

::: {.solution for="prob-proofs-13"}
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

::: {.solution for="prob-cs70-3-q1"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-2-q1" status="draft"}
(a)

1. *Base case $n=3$:* $2^3=8>7=2\cdot3+1$.

2. *Inductive step:* suppose $2^k>2k+1$ for some $k\ge3$. Then $2^{k+1}=2\cdot2^k>4k+2=(2k+3)+(2k-1)>2k+3=2(k+1)+1$, since $2k-1>0$.

(b)

1. *Base case $n=1$:* both sides are $1$.

2. *Inductive step:* if the formula holds for $k$, then
   $$\sum_{i=1}^{k+1}i^2=\frac{k(k+1)(2k+1)}6+(k+1)^2=\frac{(k+1)\bigl(2k^2+7k+6\bigr)}6=\frac{(k+1)(k+2)(2k+3)}6,$$
   which is the formula for $k+1$.

(c) Let $a_n=\frac54\cdot8^n+3^{3n-1}$; it is an integer because $4\mid8^n$.

1. *Base case $n=1$:* $a_1=10+9=19$.

2. *Inductive step:* suppose $19\mid a_k$. Since $3^{3(k+1)-1}=27\cdot3^{3k-1}$,
   $$a_{k+1}=8\cdot\tfrac54\cdot8^k+27\cdot3^{3k-1}=8a_k+19\cdot3^{3k-1}.$$
   Both terms are divisible by $19$, so $19\mid a_{k+1}$.
:::

::: {.solution for="prob-mit6042f10-2-q4" status="draft"}
The inductive step fails for $n=0$, the step from $P(0)$ to $P(1)$. There the formula uses $a^{n-1}=a^{-1}$, but the hypothesis $P(0)$ only says $a^k=1$ for natural numbers $k\le0$, i.e. for $k=0$; it says nothing about $a^{-1}$. So $a^1=1$ is never established, and the chain of implications breaks at its first link. (For $n\ge1$ the step is valid, which is why the error is easy to miss.)
:::

::: {.solution for="prob-mit6042f10-2-q5" status="draft"}
Strong induction on $n$.

1. *Base cases:* $G_0=0=3^0-2^0$ and $G_1=1=3-2$.

2. *Step:* let $n\ge2$ and suppose the formula holds for $n-1$ and $n-2$. Then
   $$G_n=5(3^{n-1}-2^{n-1})-6(3^{n-2}-2^{n-2})=3^{n-2}(15-6)-2^{n-2}(10-6)=3^n-2^n.$$
:::
