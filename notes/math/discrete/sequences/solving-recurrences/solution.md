<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sequences-02" status="draft"}
(a) $a_1 = 2$, $a_2 = 2\cdot2\cdot2 = 8$, $a_3 = 6\cdot8 = 48$,
    $a_4 = 8\cdot48 = 384$, $a_5 = 10\cdot384 = 3840$.

(b) Let $P(n)$ be the statement $a_n = 2^n n!$.

    1. *Base case.* $a_1 = 2 = 2^1\cdot1!$.

    2. *Inductive step.* Let $n\ge2$ and assume $P(n-1)$. Then
       $$a_n = 2n\,a_{n-1} = 2n\cdot2^{n-1}(n-1)! = 2^n\,n!.$$

    3. By induction, $P(n)$ holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-03" status="draft"}
(a) $b_1 = 3$, $b_2 = 9$, $b_3 = 81$, $b_4 = 6561$, $b_5 = 43{,}046{,}721$.
    Each term is $3$ raised to a power, and the exponent doubles each time:
    $3^1, 3^2, 3^4, 3^8, 3^{16}$.

(b) $b_n = 3^{2^{n-1}}$.

(c) 1. *Base case.* $b_1 = 3 = 3^{2^0}$.

    2. *Inductive step.* Let $n\ge2$ and assume $b_{n-1} = 3^{2^{n-2}}$. Then
       $$b_n = b_{n-1}^2 = \bigl(3^{2^{n-2}}\bigr)^2 = 3^{2\cdot2^{n-2}} = 3^{2^{n-1}}.$$

    3. By induction, the formula holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-04" status="draft"}
(a) $3, 5, 9, 17, 33, 65, 129$. The differences $2, 4, 8, 16, 32, 64$ double
    each time.

(b) $q_n = 2^n + 1$.

(c) 1. *Base cases.* $q_1 = 3 = 2^1 + 1$ and $q_2 = 5 = 2^2 + 1$.

    2. *Inductive step.* Let $n\ge3$ and assume the formula for $n-1$ and
       $n-2$. Then
       $$q_n = 3(2^{n-1}+1) - 2(2^{n-2}+1) = 3\cdot2^{n-1} - 2^{n-1} + 3 - 2 = 2^n + 1.$$

    3. By (strong) induction, the formula holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-05" status="draft"}
Let $P(n)$ be the statement $g_n\le n\log n - n + H_n$.

1. *Base case.* $g_1 = 0$, and the right-hand side is
   $1\cdot0 - 1 + 1 = 0$.

2. *Inductive step.* Let $n\ge2$ and assume $P(n-1)$:
   $$g_n = g_{n-1} + \log n\le (n-1)\log(n-1) - (n-1) + H_{n-1} + \log n.$$

3. By the hint, $\log(n-1) = \log n + \log\bigl(1 - \frac1n\bigr)\le\log n - \frac1n$.
   Since $n-1\ge0$,
   $$(n-1)\log(n-1)\le(n-1)\log n - \frac{n-1}n = (n-1)\log n - 1 + \frac1n.$$

4. Substituting into step 2:
   $$g_n\le (n-1)\log n - 1 + \frac1n - n + 1 + H_{n-1} + \log n = n\log n - n + \Bigl(H_{n-1} + \frac1n\Bigr) = n\log n - n + H_n.$$

5. This is $P(n)$. By induction, $P(n)$ holds for all $n\ge1$.
:::

::: {.solution for="prob-sequences-06" status="draft"}
**Explore.** $r_1, \dots, r_6 = 1, 2, 5, 14, 41, 122$. Each term is a bit less
than $3$ times the previous one.

**A simple bound.** $r_n\le3^{n-1}$. By induction: $r_1 = 1 = 3^0$, and if
$r_{n-1}\le3^{n-2}$, then $r_n = 3r_{n-1} - 1 < 3^{n-1}$.

**An exact formula.** Comparing with powers of $3$: $2r_n - 1 = 1, 3, 9, 27, 81, \dots$.
So conjecture
$$r_n = \frac{3^{n-1}+1}2.$$

1. *Base case.* $r_1 = \frac{1+1}2 = 1$.

2. *Inductive step.* Let $n\ge2$ and assume $r_{n-1} = \frac{3^{n-2}+1}2$. Then
   $$r_n = 3\cdot\frac{3^{n-2}+1}2 - 1 = \frac{3^{n-1} + 3 - 2}2 = \frac{3^{n-1}+1}2.$$

3. By induction, the formula holds for all $n\ge1$.

(This also follows from rewriting the recurrence as
$r_n - \frac12 = 3\bigl(r_{n-1} - \frac12\bigr)$.)
:::
