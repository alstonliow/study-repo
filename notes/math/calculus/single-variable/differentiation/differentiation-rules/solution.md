<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-1-q7" status="draft"}
a) Apply @thm-derivative-product-rule to $(uv)\cdot w$: $D(uvw)=D(uv)\,w+uv\,Dw=u'vw+uv'w+uvw'$.

b) Claim: $D(u_1\cdots u_n)=\sum_{i=1}^n u_1\cdots u_{i-1}\,u_i'\,u_{i+1}\cdots u_n$ (differentiate one factor at a time and add).

1. Base case $n=1$: $Du_1=u_1'$.

2. Inductive step: assume the formula for $n$ factors and let $P=u_1\cdots u_n$. By the product rule, $D(Pu_{n+1})=P'u_{n+1}+P\,u_{n+1}'$.

3. By the hypothesis, $P'u_{n+1}=\sum_{i=1}^n u_1\cdots u_i'\cdots u_n\,u_{n+1}$, which gives the terms $i=1,\dots,n$ of the formula for $n+1$ factors; $P\,u_{n+1}'$ is the term $i=n+1$.
:::

::: {.solution for="prob-mit1801n-1e-q1" status="draft"}
a) $10x^9+15x^4+6x^2$. c) $\frac12$ ($\pi^3$ is a constant).
:::

::: {.solution for="prob-mit1801n-1e-q2" status="draft"}
$\frac{x^7}7+\frac{5x^6}6+x^4+c$, checked by differentiating.
:::

::: {.solution for="prob-mit1801n-1e-q3" status="draft"}
$y'=3x^2+2x-1=(3x-1)(x+1)=0$ at $x=\frac13$ and $x=-1$. The points are $\big(\frac13,\frac{49}{27}\big)$ and $(-1,3)$.
:::

::: {.solution for="prob-mit1801n-1e-q4" status="draft"}
Both pieces equal $4$ at $x=0$, so $f$ is continuous for all $a,b$. The slopes at $0$ are $b$ (left) and $8$ (right), so $f$ is differentiable exactly when $b=8$; $a$ can be anything.
:::

::: {.solution for="prob-mit1801n-1e-q5" status="draft"}
By @thm-quotient-rule, $\dfrac{(1+x)-x}{(1+x)^2}=\dfrac1{(1+x)^2}$.
:::
