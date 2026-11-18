<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802n-4c-q1" status="draft"}
a) $\mathbf{F}=3x^2y\,\mathbf{i}+(x^3+3y^2)\,\mathbf{j}$.

b) (i) $x=y^2$, $dx=2y\,dy$, $-1\le y\le1$: $\int_{-1}^1\big(3y^5\cdot2y+y^6+3y^2\big)dy=\int_{-1}^1(7y^6+3y^2)\,dy=2+2=4$.

(ii) The vertical segment $x=1$ from $(1,-1)$ to $(1,1)$: $dx=0$, $\int_{-1}^1(1+3y^2)\,dy=4$.

(iii) $f(1,1)-f(1,-1)=2-(-2)=4$.
:::

::: {.solution for="prob-mit1802n-4c-q2" status="draft"}
a) $\mathbf{F}=(1+xy)e^{xy}\,\mathbf{i}+x^2e^{xy}\,\mathbf{j}$.

b) (i) On $C$, $xy=1$, $dy=-dx/x^2$, and $x$ runs from $1$ down to $0$: $\mathbf{F}\cdot d\mathbf{r}=2e\,dx+x^2e\big(-\frac{dx}{x^2}\big)=e\,dx$, so the integral is $\int_1^0e\,dx=-e$.

(ii) Along $C$, $f=xe^{1}\to0$ as $x\to0$, and $f(1,1)=e$: the integral is $0-e=-e$.
:::

::: {.solution for="prob-mit1802n-4c-q3" status="draft"}
a) $\mathbf{F}=\cos x\cos y\,\mathbf{i}-\sin x\sin y\,\mathbf{j}$.

b) By the fundamental theorem the integral is $f(P_1)-f(P_0)$, and $-1\le f\le1$, so it is at most $2$. It equals $2$ for any path from a point where $f=-1$ to one where $f=1$, e.g. the segment of the $x$-axis from $(-\frac\pi2,0)$ to $(\frac\pi2,0)$.
:::
