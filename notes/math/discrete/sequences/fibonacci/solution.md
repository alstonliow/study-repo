<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sequences-07" status="draft"}
**Finding the formula.** As for the Fibonacci numbers, look for solutions
$l_n = x^n$ of $l_n = l_{n-1} + l_{n-2}$. This needs $x^2 = x + 1$, so
$$x = \varphi = \frac{1+\sqrt5}2\quad\text{or}\quad x = \psi = \frac{1-\sqrt5}2.$$
Try $l_n = A\varphi^n + B\psi^n$ and fit the first two terms. Since
$\varphi + \psi = 1$ and $\varphi\psi = -1$,
$$\varphi^2 + \psi^2 = (\varphi+\psi)^2 - 2\varphi\psi = 3,$$
so $A = B = 1$ works: $\varphi + \psi = 1 = l_1$ and $\varphi^2 + \psi^2 = 3 = l_2$.
The conjecture is
$$l_n = \varphi^n + \psi^n.$$

**Proof by induction.** Let $P(n)$ be the statement $l_n = \varphi^n + \psi^n$.

1. *Base cases.* $P(1)$ and $P(2)$ were checked above.

2. *Inductive step.* Let $n\ge3$ and assume $P(n-1)$ and $P(n-2)$. Then
   $$l_n = l_{n-1} + l_{n-2} = \varphi^{n-2}(\varphi + 1) + \psi^{n-2}(\psi + 1).$$

3. Since $\varphi^2 = \varphi + 1$ and $\psi^2 = \psi + 1$, this is
   $\varphi^n + \psi^n$, which is $P(n)$.

4. By (strong) induction, $P(n)$ holds for all $n\ge1$.

Since $|\psi|<1$, $l_n$ is the integer nearest to $\varphi^n$ for $n\ge2$.
:::
