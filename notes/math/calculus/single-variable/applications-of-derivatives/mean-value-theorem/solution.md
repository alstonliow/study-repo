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

::: {.solution for="prob-cama1s-2-q10" status="draft"}
(a), (b) and (d) are true; (c) is false.

(a) If $f$ is increasing, every difference quotient $(f(x+h) - f(x))/h$ is $\ge 0$ (numerator and denominator have the same sign), so the limit $f'(x)$ is $\ge 0$.

(b) For $a \le x < y \le b$ the mean value theorem gives $\xi \in (x,y)$ with $f(y) - f(x) = f'(\xi)(y - x) \ge 0$.

(c) $f(x) = x^3$ on $[-1,1]$ is strictly increasing, but $f'(0) = 0$.

(d) As in (b), $f(y) - f(x) = f'(\xi)(y - x) > 0$.
:::

::: {.solution for="prob-cama1s-2-q12" status="draft"}
1. Let $\varepsilon > 0$ and choose $X > 0$ with $|f'(t) - \ell| < \varepsilon$ for $t \ge X$.

2. For $x > X$ the mean value theorem gives $\xi \in (X, x)$ with $f(x) = f(X) + f'(\xi)(x - X)$. Hence
$$\frac{f(x)}{x} - \ell = \frac{f(X)}{x} + (f'(\xi) - \ell)\Big(1 - \frac Xx\Big) - \frac{\ell X}{x}.$$

3. The middle term has modulus less than $\varepsilon$, and the other two tend to $0$ as $x \to \infty$. So $|f(x)/x - \ell| < 2\varepsilon$ for all large $x$, which proves the claim.

4. The converse fails: $f(x) = \sin(x^2)$ has $f(x)/x \to 0$, but $f'(x) = 2x\cos(x^2)$ takes the values $\pm 2\sqrt{m\pi}$ at $x = \sqrt{m\pi}$, so it has no limit.
:::

::: {.solution for="prob-cama1s-2-q13" status="draft"}
Let $p(x) = 2x^5 + 3x^4 + 2x + 16$.

1. $x \ge 0$: every term is $\ge 0$ and the constant is $16$, so $p(x) > 0$.

2. $-1 < x < 0$: $2x^5 > -2$, $3x^4 > 0$ and $2x > -2$, so $p(x) > 12$.

3. $x < -2$: $p(x) = x^4(2x + 3) + 2x + 16$ with $2x + 3 < -1$ and $x^4 > 16$, so $x^4(2x+3) < -16$; also $2x + 16 < 12$. Hence $p(x) < -4$.

4. $p(-2) = -4 < 0$ and $p(-1) = 15 > 0$, so by the intermediate value theorem there is a root in $(-2,-1)$.

5. $p'(x) = 10x^4 + 12x^3 + 2 = 2(x+1)(5x^3 + x^2 - x + 1)$. Let $r(x) = 5x^3 + x^2 - x + 1$. On $[-2,-1]$, $r'(x) = 15x^2 + 2x - 1 > 0$, so $r(x) \le r(-1) = -2 < 0$; and $x + 1 \le 0$. So $p' \ge 0$ on $[-2,-1]$ with equality only at $-1$, and $p$ is strictly increasing there. Hence the root is unique. (Numerically it is $x \approx -1.9338$.)
:::

::: {.solution for="prob-cama1s-3-q2" status="draft"}
1. For $h \ne 0$, $\left|\dfrac{f(x+h) - f(x)}{h}\right| \le |h| \to 0$, so $f$ is differentiable with $f'(x) = 0$ for every $x$.

2. By the mean value theorem, $f(y) - f(x) = f'(\xi)(y - x) = 0$ for all $x < y$. So $f$ is constant.
:::

::: {.solution for="prob-cama1s-3-q3" status="draft"}
1. The mean value theorem gives a $\theta \in (0,1)$ that depends on $h$, so the correct identity is $(f(c+h) - f(c))/h = f'(c + \theta(h)h)$.

2. As $h \to 0$ the left side tends to $f'(c)$, so $f'(c + \theta(h)h) \to f'(c)$ along the particular points $t_h = c + \theta(h)h$. That is all one can conclude.

3. The argument fails at the step "then $f'(c + \theta h) \to f'(c)$" read as "$f'(t) \to f'(c)$ as $t \to c$": the points $t_h$ need not fill a neighbourhood of $c$, and $f'$ may behave badly at the other points. Concluding continuity there assumes what was to be proved.

4. Example: $f(x) = x^2\sin(1/x)$, $f(0) = 0$ is differentiable on $\mathbb{R}$ with $f'(0) = 0$, but $f'(x) = 2x\sin(1/x) - \cos(1/x)$ has no limit as $x \to 0$.
:::

::: {.solution for="prob-cama1s-3-q5" status="draft"}
1. Let $g(x) = f(x) - zx$. Then $g$ is differentiable, $g'(a) = f'(a) - z < 0$ and $g'(b) = f'(b) - z > 0$.

2. $g$ is continuous on $[a,b]$, so it attains its minimum at some $c \in [a,b]$.

3. Since $g'(a) < 0$, $(g(a+h) - g(a))/h < 0$ for small $h > 0$, so $g(a+h) < g(a)$: the minimum is not at $a$. Similarly $g'(b) > 0$ gives $g(b-h) < g(b)$ for small $h > 0$: the minimum is not at $b$.

4. So $c \in (a,b)$ is an interior minimum of a differentiable function, and $g'(c) = 0$, that is, $f'(c) = z$.

5. The case $f'(a) > z > f'(b)$ follows by applying this to $-f$. A subset of $\mathbb{R}$ that contains every value between any two of its points is an interval, so $f'$ maps intervals to intervals.
:::
