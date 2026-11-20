<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-7-q3" status="draft"}
(a) $f(x)=\frac1{(2x+1)^2}$ is decreasing, and $\int_k^\infty f(x)\,dx=\frac1{2(2k+1)}$. Keep the first term $f(1)=\frac19$ and bound the rest as in @thm-integral-bounds (letting $n\to\infty$):
$$\int_2^\infty f\le\sum_{i\ge2}f(i)\le f(2)+\int_2^\infty f,\quad\text{i.e.}\quad\tfrac1{10}\le\sum_{i\ge2}f(i)\le\tfrac1{25}+\tfrac1{10}.$$
So $0.2111\le\sum_{i\ge1}f(i)\le0.2511$, bounds that differ by $0.04$. (The exact value is $\frac{\pi^2}8-1\approx0.2337$.)

(b) Inequality 1 holds; inequality 2 fails.

1. On $[i-1,i]$, $\ln(x+2)\ge\ln(i+1)$, so $\ln(i+1)\le\int_{i-1}^i\ln(x+2)\,dx$; sum over $i=1,\dots,n$.

2. On $[i-1,i]$, $\ln(x+1)\le\ln(i+1)$, with strict inequality except at $x=i$, so $\int_1^n\ln(x+1)\,dx<\sum_{i=2}^n\ln(i+1)$ for $n>1$. Adding $\ln2$ gives $\ln2+\int_1^n\ln(x+1)\,dx<\sum_{i=1}^n\ln(i+1)$: the inequality goes the other way.
:::

::: {.solution for="prob-mit6042f10-7-q4" status="draft"}
(a) During second $i$ the rug is $i$ metres $=100i$ cm long, so the bug crosses $\frac1{100i}$ of it.

(b) A uniform stretch does not change the fraction of the rug behind the bug, so the fractions add up: $\sum_{i=1}^n\frac1{100i}=\frac{H_n}{100}$.

(c) The bug arrives when $H_n\ge100$. Since $H_n\approx\ln n+\gamma$ with $\gamma\approx0.577$ (@cor-harmonic-bounds gives $\ln(n+1)\le H_n\le1+\ln n$), this needs $n\approx e^{100-\gamma}\approx1.5\times10^{43}$ seconds. The bug does make it, eventually.
:::

::: {.solution for="prob-mit6042f10-7-q6" status="draft"}
(a) $\frac{n!}{(n+1)!}=\frac1{n+1}\to0$. So $n!=o((n+1)!)$ and hence $n!=O((n+1)!)$ are true; $\Omega$, $\Theta$ and $\omega$ are false.

(b) By @prp-factorial-bounds, $n!\ge e(n/e)^n$, so
$$\frac{n!}{(n/3)^{n+e}}\ge e\Bigl(\frac3e\Bigr)^n\Bigl(\frac3n\Bigr)^e\to\infty,$$
because $\frac3e>1$ and the exponential $(3/e)^n$ outgrows the polynomial factor $n^e$.

(c) $n!=1\cdot2\cdot3\cdots n\ge1\cdot2\cdot2\cdots2=2^{n-1}$ for $n\ge1$, so $n!\ge\frac12\cdot2^n$, i.e. $n!=\Omega(2^n)$.
:::

::: {.solution for="prob-cama1s-4-q11" status="draft"}
(a) $f(0) = 0$ and $f'(x) = -2x/(1 - x^2)$. For $0 < x \le \frac12$ the mean value theorem gives $\xi \in (0,x)$ with $|f(x)| = x|f'(\xi)| = x\cdot\frac{2\xi}{1 - \xi^2} \le x\cdot\frac{2x}{3/4} = \frac{8x^2}{3}$.

(b)

1. Substituting $x = n + t$: $I_n = \int_{-1/2}^{1/2}\big(\log(n + t) - \log n\big)\,dt = \int_{-1/2}^{1/2}\log(1 + t/n)\,dt$.

2. Pairing $t$ with $-t$: $I_n = \int_0^{1/2}\big(\log(1 + t/n) + \log(1 - t/n)\big)\,dt = \int_0^{1/2}f(t/n)\,dt$.

3. By (a), since $t/n \le \frac12$: $|I_n| \le \int_0^{1/2}\frac{8t^2}{3n^2}\,dt = \frac{8}{3n^2}\cdot\frac{1}{24} = \frac{1}{9n^2}$.

(c)

1. $\sum_{j=1}^n I_j = \int_{1/2}^{n+1/2}\log x\,dx - \log n! = (n + \tfrac12)\log(n + \tfrac12) - n - \tfrac12\log\tfrac12 - \log n!$, using $\int\log x = x\log x - x$.

2. $\sum I_j$ converges absolutely by (b), so $\log n! - (n + \tfrac12)\log(n + \tfrac12) + n$ converges.

3. $(n + \tfrac12)\log(n + \tfrac12) = (n + \tfrac12)\log n + (n + \tfrac12)\log(1 + \tfrac{1}{2n})$, and the last term tends to $\frac12$ (by question 8(a)). So $\log n! - (n + \tfrac12)\log n + n = \log\dfrac{e^nn!}{n^{n+1/2}}$ converges, and by continuity of $\exp$, $e^nn!/n^{n+1/2} \to \ell$ for some $\ell > 0$.
:::

::: {.solution for="prob-cama1s-4-q12" status="draft"}
1. *Recurrence.* For $n \ge 2$, integrating by parts with $\cos^n x = \cos^{n-1}x\cdot\cos x$:
$$I_n = \big[\cos^{n-1}x\sin x\big]_0^{\pi/2} + (n-1)\int_0^{\pi/2}\cos^{n-2}x\sin^2x\,dx = (n-1)(I_{n-2} - I_n),$$
so $nI_n = (n-1)I_{n-2}$.

2. *Bounds.* On $[0,\pi/2]$, $0 \le \cos x \le 1$, so $I_n$ is positive and decreasing in $n$. Hence $I_{2n+1} \le I_{2n} \le I_{2n-1} = \frac{2n+1}{2n}I_{2n+1}$, which gives $\frac{2n}{2n+1} \le \frac{I_{2n+1}}{I_{2n}} \le 1$. So $I_{2n+1}/I_{2n} \to 1$.

3. *Wallis.* From $I_0 = \pi/2$, $I_1 = 1$ and the recurrence,
$$I_{2n} = \frac{1\cdot3\cdots(2n-1)}{2\cdot4\cdots2n}\cdot\frac\pi2, \qquad I_{2n+1} = \frac{2\cdot4\cdots2n}{3\cdot5\cdots(2n+1)}.$$
So $\dfrac{I_{2n+1}}{I_{2n}} = \dfrac{2}{\pi}\cdot\dfrac{2\cdot2\cdot4\cdot4\cdots2n\cdot2n}{1\cdot3\cdot3\cdot5\cdots(2n-1)(2n+1)} \to 1$, which is the first form.

4. Since $2\cdot4\cdots2n = 2^nn!$ and $1\cdot3\cdots(2n-1) = (2n)!/(2^nn!)$, the fraction equals $\dfrac{(2^nn!)^4}{((2n)!)^2(2n+1)} = \dfrac{2^{4n}}{2n+1}\binom{2n}{n}^{-2}$, the second form.

5. *Stirling.* Let $a_n = e^nn!/n^{n+1/2} \to \ell > 0$ (previous question). Then $n! = a_nn^{n+1/2}e^{-n}$ and
$$\binom{2n}{n} = \frac{a_{2n}(2n)^{2n+1/2}e^{-2n}}{a_n^2n^{2n+1}e^{-2n}} = \frac{a_{2n}}{a_n^2}\cdot\frac{2^{2n+1/2}}{\sqrt n}.$$

6. Hence $\dfrac{2^{4n}}{2n+1}\binom{2n}{n}^{-2} = \dfrac{a_n^4}{a_{2n}^2}\cdot\dfrac{n}{2(2n+1)} \to \dfrac{\ell^4}{\ell^2}\cdot\dfrac14 = \dfrac{\ell^2}{4}$. By Wallis this limit is $\pi/2$, so $\ell^2 = 2\pi$ and $\ell = \sqrt{2\pi}$. (Numerically, $a_{200} \approx 2.5077$ against $\sqrt{2\pi} \approx 2.5066$.)
:::
