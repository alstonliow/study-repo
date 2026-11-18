<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-4-q5" status="draft"}
Divide $[0,1]$ into $n$ pieces of width $\frac1n$. Since $e^x$ is increasing, its smallest value on $[\frac{i}n,\frac{i+1}n]$ is at the left end, so the lower sum is
$$\sum_{i=0}^{n-1}e^{i/n}\cdot\frac1n=\frac1n\sum_{i=0}^{n-1}\big(e^{1/n}\big)^i=\frac1n\cdot\frac{e-1}{e^{1/n}-1}=\frac{e-1}{n(e^{1/n}-1)},$$
by the geometric sum with ratio $e^{1/n}$ (and $(e^{1/n})^n=e$).

With $h=1/n$, $n(e^{1/n}-1)=\frac{e^h-1}h\to1$ as $h\to0$ (this is $e^h\approx1+h$, or the definition of $e$, @def-number-e). So the lower sums tend to $e-1$, and $\int_0^1e^x\,dx=e-1$.
:::

::: {.solution for="prob-mit1801n-3b-q2" status="draft"}
a) $\displaystyle\sum_{k=1}^6(-1)^{k+1}(2k+1)$.

b) $\displaystyle\sum_{k=1}^n\frac1{k^2}$.
:::

::: {.solution for="prob-mit1801n-3b-q3" status="draft"}
The subintervals are $[-1,0],[0,1],[1,2],[2,3]$ (width $1$), and $x^2$ takes the values $1,0,1,4,9$ at the division points.

- Left: $1+0+1+4=6$. Right: $0+1+4+9=14$.
- Upper (largest value on each piece): $1+1+4+9=15$. Lower (smallest value): $0+0+1+4=5$.

The exact value $\frac{28}3\approx9.33$ lies between the lower and upper sums. (On $[-1,0]$ the function decreases, so there the upper value is at the left end.)
:::

::: {.solution for="prob-mit1801n-3b-q4" status="draft"}
On $[0,b]$ ($b>0$) $x^2$ is increasing, so the upper sum uses right endpoints and the lower sum left endpoints. Their difference telescopes:
$$\sum_{i=1}^n\big(f(x_i)-f(x_{i-1})\big)\frac bn=\big(f(b)-f(0)\big)\frac bn=\frac{b^3}n\to0 .$$
:::

::: {.solution for="prob-mit1801n-3b-q5" status="draft"}
With $\Delta x=b/n$ and $x_k=kb/n$, the expression is $\frac1b\sum_{k=1}^n\sin(x_k)\Delta x$, a right Riemann sum for $\int_0^b\sin x\,dx$. So for $b\ne0$ the limit is
$$\frac1b\int_0^b\sin x\,dx=\frac{1-\cos b}b ,$$
and for $b=0$ it is $0$.
:::
