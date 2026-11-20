<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801n-6a-q1" status="draft"}
All are $0/0$ forms; apply @thm-lhopital.

b) $\lim\frac{-\frac12\sin(x/2)}{2x}=\lim\frac{-\frac14\cos(x/2)}2=-\frac18$.

e) $\lim\frac{1/(1+x^2)}5=\frac15$.

f) $\lim\frac{1-\cos x}{3x^2}=\lim\frac{\sin x}{6x}=\frac16$.

g) $\lim\frac{ax^{a-1}}{bx^{b-1}}=\frac ab$ (for $b\ne0$).

j) $\lim\frac{\frac12\cot(x/2)}{2(x-\pi)}$ is again $0/0$; once more: $\lim\frac{-\frac14\csc^2(x/2)}{2}=-\frac18$.
:::

::: {.solution for="prob-mit1801n-6a-q5" status="draft"}
The second application is illegal: $\frac{6x-4}{2-2x}$ tends to $\frac{-4}2=-2$, which is not an indeterminate form, so L'Hôpital's rule does not apply to it (check the form before differentiating). The correct limit is $-2$.
:::

::: {.solution for="prob-mit1801n-6a-q6" status="draft"}
The domain is $x>0$, $x\ne1$. Ends: as $x\to0^+$, $y\to0$; as $x\to1^\pm$, $y\to\pm\infty$; as $x\to\infty$, $y\to\infty$ (by L'Hôpital, $\lim\frac x{\ln x}=\lim x=\infty$).

$y'=\frac{\ln x-1}{(\ln x)^2}$: on $(0,1)$ it is negative, so $y$ decreases from $0$ to $-\infty$; on $(1,\infty)$ it is negative before $e$ and positive after, so $(e,e)$ is a local minimum (@exm-sketch-log).

$y''=\frac{2-\ln x}{x(\ln x)^3}$: concave down on $(0,1)$, concave up on $(1,e^2)$, concave down after $e^2$; inflection point $(e^2,e^2/2)$.
:::

::: {.solution for="prob-cama1s-3-q4" status="draft"}
(a)

1. Choose $\eta > 0$ with $g' \ne 0$ on $(a, a+\eta)$. For $x \in (a, a+\eta)$, $g(x) \ne 0$: otherwise Rolle's theorem on $[a,x]$ would give a zero of $g'$.

2. By Cauchy's mean value theorem on $[a,x]$ there is $\xi_x \in (a,x)$ with $\dfrac{f(x)}{g(x)} = \dfrac{f(x) - f(a)}{g(x) - g(a)} = \dfrac{f'(\xi_x)}{g'(\xi_x)}$.

3. As $x \to a$, $\xi_x \to a$, so $f'(\xi_x)/g'(\xi_x) \to \ell$.

(b) Apply (a) to $F(x) = f(x) - f(a)$ and $g(x) = x - a$ (so $g' = 1$): $\dfrac{f(x) - f(a)}{x - a} \to \ell$, which says $f'(a) = \ell$.

(c) $a = 0$, $f(x) = x^2\sin(1/x)$ with $f(0) = 0$, and $g(x) = x$, on $[0,1]$. Then $f(x)/g(x) = x\sin(1/x) \to 0$, but $f'(x)/g'(x) = 2x\sin(1/x) - \cos(1/x)$ has no limit.

(d) The limit is $n(n+1)/2$. Let $N(x)$ be the numerator. Then $N(1) = 1 - (n+1) + n = 0$ and $N'(x) = 1 - (n+1)^2x^n + n(n+2)x^{n+1}$, so $N'(1) = 0$. Also $N''(x) = -n(n+1)^2x^{n-1} + n(n+1)(n+2)x^n$, so $N''(1) = n(n+1)$. The denominator $D(x) = (1-x)^2$ has $D(1) = D'(1) = 0$ and $D'' = 2$. Applying the rule twice (with $D' = -2(1-x) \ne 0$ near $1$; for $x \to 1^-$, and similarly from the right) gives $N(x)/D(x) \to N''(1)/2 = n(n+1)/2$. (Indeed the expression equals $\sum_{k=1}^n kx^k$ for $x \ne 1$.)
:::
