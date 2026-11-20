<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-8b-q1" status="draft"}
a) The limit is $0$ for every real $m$. For $m\le0$ both factors are bounded and $e^{-x}\to0$. For $m>0$ write it as $\frac{x^m}{e^x}$ ($\infty/\infty$) and apply @thm-lhopital $\lceil m\rceil$ times: each time the power drops by one while $e^x$ stays, until the numerator is $m(m-1)\cdots x^{m-\lceil m\rceil}$, which is bounded for $x\ge1$.

b) The integrand is continuous on $[0,\infty)$, so only the infinite end matters. By (a) with $m=n+2$, $\frac{x^ne^{-x}}{x^{-2}}=x^{n+2}e^{-x}\to0$, so $x^ne^{-x}\le x^{-2}$ for $x\ge b$, some $b\ge1$. Since $\int_b^\infty x^{-2}dx$ converges (@thm-p-integrals), so does $\int_b^\infty x^ne^{-x}dx$ by @thm-comparison-integrals. (A limit of $0$ rather than a positive number is enough for convergence, by this direct comparison.)

c) With $u=x^{n+1}$, $v=-e^{-x}$ (@thm-integration-by-parts):
$$\int_0^Nx^{n+1}e^{-x}dx=\Big[-x^{n+1}e^{-x}\Big]_0^N+(n+1)\int_0^Nx^ne^{-x}dx .$$
The boundary term is $-N^{n+1}e^{-N}\to0$ by (a) (and it is $0$ at $x=0$). Letting $N\to\infty$, $A(n+1)=(n+1)A(n)$, so $c_n=n+1$.

d) $A(0)=\int_0^\infty e^{-x}dx=1$. By induction $A(n)=n\,A(n-1)=\dots=n!$.

e) $A(-\tfrac12)=\int_0^\infty x^{-1/2}e^{-x}dx$. On $(0,1]$, $x^{-1/2}e^{-x}\le x^{-1/2}$, whose integral converges ($p=\frac12<1$); on $[1,\infty)$, $x^{-1/2}e^{-x}\le e^{-x}$. So it converges. Substituting $x=u^2$, $dx=2u\,du$:
$$A(-\tfrac12)=\int_0^\infty\frac{e^{-u^2}}{u}\,2u\,du=2\int_0^\infty e^{-u^2}du=\sqrt\pi,$$
using the Gaussian integral (@prp-gaussian-integral).
:::

::: {.solution for="prob-mit1801n-6b-q1" status="draft"}
$\frac1{\sqrt{x^3+5}}<x^{-3/2}$ and $\int_1^\infty x^{-3/2}dx$ converges (@thm-p-integrals, $p=\frac32>1$), so the integral **converges** (@thm-comparison-integrals).
:::

::: {.solution for="prob-mit1801n-6b-q2" status="draft"}
$\frac{x^2}{x^3+2}\Big/\frac1x\to1$ as $x\to\infty$, and $\int_1^\infty\frac{dx}x$ diverges, so by limit comparison the integral **diverges** (the part over $[0,1]$ is finite).
:::

::: {.solution for="prob-mit1801n-6b-q7" status="draft"}
a) $\frac18$ (@exm-improper-basic).

f) With $u=\ln x$: $\int_1^\infty\frac{du}{u^2}=1$. Convergent, value $1$.

k) Integrating by parts twice, $\int e^{-2x}\cos x\,dx=\frac{e^{-2x}(\sin x-2\cos x)}5$. At $\infty$ this tends to $0$, at $0$ it is $-\frac25$, so the integral converges to $\frac25$.

m) $-\frac1{2(x+2)^2}\Big|_0^\infty=0+\frac18=\frac18$.
:::

::: {.solution for="prob-mit1801n-6b-q8" status="draft"}
$\int_0^xe^{-t^2}dt$ increases to $\frac{\sqrt\pi}2>0$ (and is at least $\int_0^1e^{-t^2}dt>0$ for $x\ge1$), while $e^{x^2}\to\infty$. So the product tends to $+\infty$.
:::

::: {.solution for="prob-cama1s-4-q5" status="draft"}
Both converge.

(i) $|\sin y| \le |y|$, so $0 \le \sin^2(1/x) \le 1/x^2$, and $\int_1^\infty x^{-2}\,dx = 1$. By comparison the integral converges.

(ii)

1. On $[0,1]$ the integrand is continuous (as $p > 0$), so $\int_0^1$ is an ordinary integral.

2. For $x \ge 1$, $x^{p+2}e^{-x^q} \to 0$ as $x \to \infty$ (put $y = x^q$: it is $y^{(p+2)/q}e^{-y}$, and $e^y$ grows faster than any power). So there is $X$ with $x^pe^{-x^q} \le x^{-2}$ for $x \ge X$.

3. By comparison with $\int_X^\infty x^{-2}\,dx$, $\int_1^\infty x^pe^{-x^q}\,dx$ converges. So the whole integral converges.
:::

::: {.solution for="prob-cama1s-4-q6" status="draft"}
(a)

1. Let $|F| \le M$. Since $F' = f$ (fundamental theorem of calculus) and $g$ is $C^1$, integration by parts on $[a,R]$ gives
$$\int_a^R fg = F(R)g(R) - \int_a^R F(x)g'(x)\,dx.$$

2. $|F(R)g(R)| \le M|g(R)| \to 0$.

3. $g$ is monotone, so $g'$ has constant sign and $\int_a^R |g'| = |g(R) - g(a)| \to |g(a)|$. Hence $\int_a^\infty |Fg'| \le M|g(a)|$ converges, and $\int_a^\infty Fg'$ converges absolutely.

4. So $\int_a^R fg$ has a limit as $R \to \infty$.

5. For $\int_1^\infty x^{-1/2}\sin x\,dx$: $f = \sin$ is continuous with $F(x) = \cos 1 - \cos x$, so $|F| \le 2$; $g(x) = x^{-1/2}$ is decreasing, $C^1$, and tends to $0$.

(b) *For $\int|f|$:*

1. $L < 1$: choose $r \in (L, 1)$. For $x \ge X$, $|f(x)|^{1/x} < r$, so $|f(x)| < r^x$, and $\int_X^\infty r^x\,dx$ converges. So $\int_a^\infty|f|$ converges.

2. $L > 1$: for large $x$, $|f(x)| > 1$, so $\int_X^R|f| \ge R - X \to \infty$. It diverges.

3. $L = 1$: no conclusion. $f(x) = 1/x^2$ on $[1,\infty)$ has $|f(x)|^{1/x} = e^{-2\log x/x} \to 1$ and $\int_1^\infty f$ converges; $f = 1$ has $L = 1$ and diverges.

*For $\int f$:*

4. $L < 1$: converges, since absolute convergence implies convergence.

5. $L = 1$: no conclusion, by the same two examples.

6. $L > 1$: if $f$ is continuous, then $f$ has no zeros for large $x$ (as $|f| > 1$), so by the intermediate value theorem it has constant sign there and $\int f$ diverges like $\int |f|$. Without continuity it can converge. Let $f(x) = \sigma(x)e^{2x}$, where on each $[n, n+1)$ we cut the interval into $2K_n$ consecutive pieces of equal $e^{2x}$-mass $\mu_n = e^{2n}(e^2 - 1)/(4K_n)$, with $K_n$ chosen so that $\mu_n \le 1/n$, and $\sigma = +1, -1, +1, \ldots$ alternately on the pieces. Then $f$ is integrable on bounded intervals, $|f(x)|^{1/x} = e^2$, $\int_n^{n+1}f = 0$, and $|\int_n^tf| \le \mu_n \le 1/n$ for $t \in [n, n+1]$. So $\int_a^R f$ converges as $R \to \infty$.

(c) No, even for continuous $f$. Let $f$ be $0$ except for a triangular spike of height $1$ and base $[n - n^{-2}, n + n^{-2}]$ at each integer $n \ge 2$. Then $f \ge 0$ is continuous, $\int_1^R f \le \sum_n n^{-2}$ is bounded and increasing in $R$, so the integral converges, but $f(n) = 1$ for all $n$.
:::
