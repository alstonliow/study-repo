<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-2b-q2" status="draft"}
$f(x)=\frac1{1+x^2}$ is even, positive, with $f\to0$ as $x\to\pm\infty$.

- $f'(x)=\frac{-2x}{(1+x^2)^2}$: zero only at $x=0$, positive for $x<0$ and negative for $x>0$, so $(0,1)$ is the maximum (the only critical point).
- $f''(x)=\frac{6x^2-2}{(1+x^2)^3}$: zero at $x=\pm\frac1{\sqrt3}$, negative between them and positive outside. The inflection points are $\big(\pm\frac1{\sqrt3},\frac34\big)$.

Sketches (one above the other): $f$ is a bell-shaped curve with top $(0,1)$, concave down for $\lvert x\rvert<1/\sqrt3$ and concave up outside. $f'$ is odd: it rises from $0$ at $-\infty$ to its maximum $\frac{3\sqrt3}8\approx0.65$ at $x=-\frac1{\sqrt3}$, passes through $0$ at $x=0$ (the vertical line from the maximum of $f$), reaches its minimum $-\frac{3\sqrt3}8$ at $x=\frac1{\sqrt3}$, and returns to $0$; the extremes of $f'$ sit under the inflection points of $f$. $f''$ is even: $f''(0)=-2$, zero at $\pm\frac1{\sqrt3}$ (under the inflection points), maximum $\frac12$ at $x=\pm1$, then decreasing to $0$.
:::

::: {.solution for="prob-mit1801n-2b-q1" status="draft"}
a) $y'=3(x^2-1)$: increasing on $x<-1$ and $x>1$, decreasing on $-1<x<1$; local maximum $(-1,3)$, local minimum $(1,-1)$; $y\to\pm\infty$ as $x\to\pm\infty$. The values change sign on $(-\infty,-1)$, $(-1,1)$ and $(1,\infty)$, so $y=0$ has **three** solutions.

e) $y'=\frac4{(x+4)^2}>0$: increasing on $x<-4$ and on $x>-4$. Vertical asymptote $x=-4$ ($y\to+\infty$ from the left, $-\infty$ from the right), horizontal asymptote $y=1$. $y=0$ only at $x=0$: **one** solution.

h) $y'=-2xe^{-x^2}$: increasing for $x<0$, decreasing for $x>0$, maximum $(0,1)$, $y\to0$ at both ends, and $y>0$ always: **no** solutions.
:::

::: {.solution for="prob-mit1801n-2b-q2" status="draft"}
a) $y''=6x$ changes sign at $0$: inflection point $(0,1)$.

e) $y''=-\frac8{(x+4)^3}$ changes sign only at $x=-4$, which is not in the domain: no inflection points.

h) $y''=(4x^2-2)e^{-x^2}$ changes sign at $x=\pm\frac1{\sqrt2}$: inflection points $\big(\pm\frac1{\sqrt2},e^{-1/2}\big)$.
:::

::: {.solution for="prob-mit1801n-2b-q4" status="draft"}
$f$ rises from $x=0$ through $0$ at $x=4$ to a local maximum at $5$, falls through $0$ at $7$ to a local minimum at $8$, then rises through $0$ at $9$ to $x=10$. Since $f$ increases on $[0,5]$ and $f(4)=0$: $f(0)<0<f(5)$. Similarly $f(8)<0$ and $f(10)>0$.

By @thm-closed-interval-method the maximum is at $5$ or at $10$, and the minimum at $0$ or at $8$. So the maximum is positive and the minimum negative, but the data do not decide which candidate wins in either case, and give no values.
:::

::: {.solution for="prob-mit1801n-2b-q6" status="draft"}
a) We need $f'$ to vanish at $\pm1$, be positive for $x<-1$ and negative between: $f'(x)=x^2-1$ works, so $f(x)=\frac{x^3}3-x$ (or $x^3-3x$, or any positive multiple plus a constant).

b) For $f(x)=x^3-3x$: $f(-3)=-18$, local maximum $(-1,2)$, inflection point $(0,0)$, local minimum $(1,-2)$, $f(3)=18$. On $[-3,3]$ the local maximum and minimum are not the absolute ones, which are at the endpoints.
:::

::: {.solution for="prob-mit1801n-2b-q7" status="draft"}
a) If $f$ is increasing, $\Delta f=f(a+\Delta x)-f(a)$ has the same sign as $\Delta x$, so $\frac{\Delta f}{\Delta x}>0$ for every $\Delta x\ne0$. A limit of positive quantities is $\ge0$, so $f'(a)\ge0$.

b) Limits do not preserve strict inequalities: positive quotients can tend to $0$. Counterexample: $f(x)=x^3$ is increasing, but $f'(0)=0$.
:::
