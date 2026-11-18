<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801n-1d-q3" status="draft"}
a) $\frac{x-2}{x^2-4}=\frac1{x+2}$ for $x\ne2$: a removable discontinuity at $x=2$ (limit $\frac14$) and an infinite one at $x=-2$ (@def-kinds-of-discontinuity).

d) Both one-sided limits at $0$ equal $a$, but $f(0)$ is not defined: a removable discontinuity at $0$.

e) $f'(x)=1$ for $x>0$ and $-1$ for $x<0$: a jump discontinuity at $0$.
:::

::: {.solution for="prob-mit1801n-1d-q4" status="draft"}
From @prob-mit1801n-1d-q1: a vertical asymptote at $x=2$ ($+\infty$ from the right, $-\infty$ from the left), and since $\frac{4x^2}{x-2}-4x\to8$, the line $y=4x+8$ is a slant asymptote at both ends. The derivative is $\frac{4x(x-4)}{(x-2)^2}$: a local maximum $(0,0)$ (the graph touches the axis there) and a local minimum $(4,32)$. So: from the lower left along $y=4x+8$ up to $(0,0)$, down to $-\infty$ at $x=2$; on the right, down from $+\infty$ to $(4,32)$ and up along $y=4x+8$.
:::
