<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-2b-q2" status="draft"}
$f(x)=\frac1{1+x^2}$ is even, positive, with $f\to0$ as $x\to\pm\infty$.

- $f'(x)=\frac{-2x}{(1+x^2)^2}$: zero only at $x=0$, positive for $x<0$ and negative for $x>0$, so $(0,1)$ is the maximum (the only critical point).
- $f''(x)=\frac{6x^2-2}{(1+x^2)^3}$: zero at $x=\pm\frac1{\sqrt3}$, negative between them and positive outside. The inflection points are $\big(\pm\frac1{\sqrt3},\frac34\big)$.

Sketches (one above the other): $f$ is a bell-shaped curve with top $(0,1)$, concave down for $\lvert x\rvert<1/\sqrt3$ and concave up outside. $f'$ is odd: it rises from $0$ at $-\infty$ to its maximum $\frac{3\sqrt3}8\approx0.65$ at $x=-\frac1{\sqrt3}$, passes through $0$ at $x=0$ (the vertical line from the maximum of $f$), reaches its minimum $-\frac{3\sqrt3}8$ at $x=\frac1{\sqrt3}$, and returns to $0$; the extremes of $f'$ sit under the inflection points of $f$. $f''$ is even: $f''(0)=-2$, zero at $\pm\frac1{\sqrt3}$ (under the inflection points), maximum $\frac12$ at $x=\pm1$, then decreasing to $0$.
:::
