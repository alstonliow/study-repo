<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-4-q1" status="draft"}
a) For $x>0$, @thm-mean-value gives $c\in(0,x)$ with $f(x)=f(0)+f'(c)\,x=f'(c)\,x\ge0$.

b) $f(x)=x-\ln(1+x)$ has $f(0)=0$ and $f'(x)=1-\frac1{1+x}=\frac x{1+x}\ge0$ for $x\ge0$. By (a), $f\ge0$, i.e. $\ln(1+x)\le x$.

c) $g(x)=\ln(1+x)-x+\frac{x^2}2$: $g(0)=0$, $g'(x)=\frac1{1+x}-1+x=\frac{x^2}{1+x}\ge0$, so $g\ge0$.
$k(x)=x-\frac{x^2}2+\frac{x^3}3-\ln(1+x)$: $k(0)=0$, $k'(x)=1-x+x^2-\frac1{1+x}=\frac{(1-x+x^2)(1+x)-1}{1+x}=\frac{x^3}{1+x}\ge0$, so $k\ge0$.

d) With $S_n(x)=x-\frac{x^2}2+\frac{x^3}3-\dots+(-1)^{n+1}\frac{x^n}n$, for $x\ge0$:
$$S_{2m}(x)\le\ln(1+x)\le S_{2m+1}(x)\qquad(m\ge0).$$
(It is true: the derivative of $\pm(\ln(1+x)-S_n(x))$ is $\pm(-1)^n\frac{x^n}{1+x}$, by the geometric sum.)

e) Put $u=-x\in[0,1)$; we need $\ln(1-u)\le-u$. Let $f(u)=-u-\ln(1-u)$: $f(0)=0$ and $f'(u)=-1+\frac1{1-u}=\frac u{1-u}\ge0$ on $[0,1)$, so by (a) $f(u)\ge0$, which is the claim.
:::

::: {.solution for="prob-mit1801n-2g-q1" status="draft"}
$\frac{\ln2-\ln1}{2-1}=\ln2$ must equal $f'(c)=\frac1c$, so $c=\frac1{\ln2}\approx1.443$, which lies in $(1,2)$. It is the only one, since $1/c$ is one-to-one.
:::

::: {.solution for="prob-mit1801n-2g-q2" status="draft"}
Take $f(t)=\sqrt{1+t}$ on $[0,x]$: $\sqrt{1+x}=1+\frac{x}{2\sqrt{1+c}}$ for some $c\in(0,x)$. Since $c>0$, $\sqrt{1+c}>1$, so $\frac x{2\sqrt{1+c}}<\frac x2$ and $\sqrt{1+x}<1+\frac x2$.
:::

::: {.solution for="prob-mit1801n-2g-q5" status="draft"}
a) $f$ is differentiable, hence continuous. By @thm-rolle on $[a,b]$ and on $[b,c]$ there are $q_1\in(a,b)$ and $q_2\in(b,c)$ with $f'(q_1)=f'(q_2)=0$. Since $f''$ exists, $f'$ is differentiable on $[q_1,q_2]$, and Rolle's theorem again gives $p\in(q_1,q_2)\subset[a,c]$ with $f''(p)=0$.

b) $f(x)=x^3-(a+b+c)x^2+\cdots$, so $f''(x)=6x-2(a+b+c)$ and $p=\frac{a+b+c}3$, the average of the roots, which lies between $a$ and $c$. On the graph, $f'$ vanishes at the local maximum (between $a$ and $b$) and the local minimum (between $b$ and $c$), and $p$ is the inflection point between them.
:::

::: {.solution for="prob-mit1801n-2g-q6" status="draft"}
Let $a\le x_1<x_2\le b$. By form (2), $f(x_2)-f(x_1)=f'(c)(x_2-x_1)$ for some $c\in(x_1,x_2)$.

a) If $f'>0$, the right side is positive, so $f(x_2)>f(x_1)$: $f$ is increasing.

b) If $f'=0$, the right side is $0$, so $f(x_2)=f(x_1)$ for all such pairs: $f$ is constant. (This is @cor-sign-of-derivative.)
:::
