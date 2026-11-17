<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-proofs-01"}
::: {.proof name="Proof (by cases)"}

Let $\operatorname{Collatz}(x) = C(x)$.

**Case 1: $x$ is odd, $x=2n+1$.**
$$\begin{aligned}
        C(x) &= 3(2n+1)+1 = 6n+4 = 2(3n+2) \quad \text{(even)} \\
        C^{(2)}(x) &= 3n+2 = 3\left(\frac{x-1}{2}\right)+2
            = \frac{3x-3}{2}+2 = \frac{3}{2}x+\frac12
    \end{aligned}$$
$$\implies C^{(2)}(x) < \frac32 x+1. \tag{1}$$

**Case 2: $x$ is even, $x=2m$.** Then $C(x)=m$.

**Case 2a: $m$ is odd.**
$$C^{(2)}(x) = 3m+1 = \frac32 x+1. \tag{2}$$

**Case 2b: $m$ is even.**
$$C^{(2)}(x) = \frac{m}{2} = \frac{x}{4}
            < \frac32 x < \frac32 x+1. \tag{3}$$

By (1), (2), (3), in all cases,
$$C^{(2)}(x) \le \frac32 x+1.$$

:::
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-1-q4" status="draft"}
(a) True. Let $n=2k+1$. Then $n^2+4n=n(n+4)=(2k+1)(2k+5)$, a product of two odd numbers, hence odd.

(b) True, by contraposition. If $a>11$ and $b>4$, then $a+b>15$.

(c) True, by contraposition. If $r$ is rational, $r=\frac pq$ with integers $p,q$, $q\ne0$, then $r^2=\frac{p^2}{q^2}$ is rational.

(d) False. For $n=7$: $5\cdot7^3=1715$ but $7!=5040$. (It holds for $n=1,\dots,6$ and fails for every $n\ge7$.)
:::

::: {.solution for="prob-mit6042f10-1-q6" status="draft"}
1. *Squares modulo $4$.* $(2i)^2=4i^2\equiv0$ and $(2j+1)^2=4(j^2+j)+1\equiv1\pmod4$.

2. *Cases.* Let $k$ be the number of odd numbers among $w,x,y$, so $k\in\{0,1,2,3\}$. By step 1, $w^2+x^2+y^2\equiv k\pmod4$.

3. If $k=0$, the sum is even, so $z^2$ is even and $z$ is even (an odd $z$ has an odd square).

4. If $k=1$ or $k=3$, the sum is odd, so $z$ is odd. If $k=2$, then $z^2\equiv2\pmod4$, which no square is: this case is impossible.

5. So $z$ is even exactly in case $k=0$, i.e. when $w$, $x$ and $y$ are all even.
:::
