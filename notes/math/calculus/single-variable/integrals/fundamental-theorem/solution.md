<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-5-q1" status="draft"}
a) $y'=y/100$ with $y(0)=65$ gives $y=65e^{t/100}$ (@exm-exponential-growth). Day 3 is $3\le t\le4$ and day 4 is $4\le t\le5$. On the graph (a slowly rising, slightly convex curve near $y\approx67$) shade the region under the curve over $[3,4]$, labelled "day 3", and over $[4,5]$, labelled "day 4". Since each day has length $1$, these areas are the average temperatures:
$$\int_3^465e^{t/100}dt=6500(e^{0.04}-e^{0.03})\approx67.32^\circ,\qquad\int_4^565e^{t/100}dt\approx67.99^\circ.$$

b) Shade the region between the line $y=65$ and the curve for $0\le t\le50$. The total degree days are
$$\int_0^{50}\big(65e^{t/100}-65\big)dt=\int_0^{50}65e^{t/100}dt-65\cdot50 .$$
By @thm-ftc-1, $\int_0^{50}65e^{t/100}dt=6500e^{t/100}\Big|_0^{50}=6500(e^{1/2}-1)\approx4216.69$, so the total is about $4216.69-3250\approx966.7$ degree days.

c) With $n$ pieces of width $\frac{50}n$ and left endpoints (the function increases), the lower sum is
$$\sum_{i=0}^{n-1}65e^{i/(2n)}\cdot\frac{50}n=\frac{3250}{n}\cdot\frac{e^{1/2}-1}{e^{1/(2n)}-1}=6500\,(e^{1/2}-1)\cdot\frac{1/(2n)}{e^{1/(2n)}-1}.$$
As $n\to\infty$, $\frac{h}{e^h-1}\to1$ with $h=\frac1{2n}$, so the sums tend to $6500(e^{1/2}-1)$, as in (b).
:::

::: {.solution for="prob-mit1801f06-5-q2" status="draft"}
a) $\cos(t^2)$ is even (it depends on $t^2$), equals $1$ at $t=0$ and is very flat there: $\cos(t^2)\approx1-\frac{t^4}2$. Its first zeros are at $t^2=\pi/2$, i.e. $t=\pm\sqrt{\pi/2}\approx\pm1.2533$. After that it oscillates between $\pm1$ faster and faster (zeros at $t=\pm\sqrt{\pi/2+k\pi}$).

b) By @thm-ftc-2, $f'(x)=\cos(x^2)$, which vanishes at $x=\pm\sqrt{\pi/2+k\pi}$, $k=0,1,2,\ldots$ $f$ is odd (its derivative is even and $f(0)=0$).
For $x>0$: $f'$ changes from $+$ to $-$ at $\sqrt{\pi/2+2m\pi}$ (local maxima) and from $-$ to $+$ at $\sqrt{3\pi/2+2m\pi}$ (local minima).
For $x<0$, by oddness: local minima at $-\sqrt{\pi/2+2m\pi}$ and local maxima at $-\sqrt{3\pi/2+2m\pi}$ ($m=0,1,\ldots$).

c) On $[-2,2]$ (since $\sqrt{3\pi/2}\approx2.17>2$): a local maximum at $x=\sqrt{\pi/2}\approx1.25$ with $f\approx0.98$, and by oddness a local minimum at $(-1.25,-0.98)$. Inflection points where $f''(x)=-2x\sin(x^2)$ changes sign: $x=0$ (point $(0,0)$, slope $1$) and $x=\pm\sqrt\pi\approx\pm1.77$, with $f(\sqrt\pi)\approx0.66$. Between $0$ and $1.25$ the graph rises almost like $y=x$ and then bends over; it decreases from $1.25$ to $2$, where $f(2)\approx0.46$; the left half is the reflection through the origin.

d) $\cos(t^2)=1-\frac{t^4}2+\frac{t^8}{24}-\cdots$, so $f(0.1)=0.1-\frac{(0.1)^5}{10}+\frac{(0.1)^9}{216}-\cdots=0.1-0.000001+\ldots\approx0.099999$ (to six decimals; the next term is about $5\times10^{-12}$).

e) i) Put $t=\sqrt{\pi/2}\,u$, $dt=\sqrt{\pi/2}\,du$ (@thm-substitution-definite): $f(x)=\sqrt{\pi/2}\int_0^{x\sqrt{2/\pi}}\cos\big(\tfrac\pi2u^2\big)du=\sqrt{\pi/2}\;g\big(\sqrt{2/\pi}\,x\big)$. So $c_1=\sqrt{\pi/2}$, $c_2=\sqrt{2/\pi}$. With the factor $\pi/2$ the zeros of $\cos(\frac\pi2u^2)$ are at $u^2=1,3,5,\ldots$; the first one is at $u=1$.

ii) Put $v=t^2$ ($t>0$), $dt=\frac{dv}{2\sqrt v}$: $f(x)=\int_0^{x^2}\frac{\cos v}{2\sqrt v}dv=\frac12h(x^2)$, so $c=\frac12$.

iii) For fixed $x>0$, put $z=xt^2$, so $t=\sqrt{z/x}$ and $dt=\frac{dz}{2\sqrt{xz}}$; $t$ from $0$ to $1$ means $z$ from $0$ to $x$. Then $\int_0^1\cos(xt^2)dt=\frac1{2\sqrt x}\int_0^x\frac{\cos z}{\sqrt z}dz=\frac{h(x)}{2\sqrt x}$, so $k(x)=\frac12h(x)$. By (ii), $\frac12h(x)=f(\sqrt x)$, hence $k(x)=f(\sqrt x)$.
:::

::: {.solution for="prob-mit1801n-3c-q1" status="draft"}
$\int_3^6(x-2)^{-1/2}dx=2\sqrt{x-2}\Big|_3^6=2(2-1)=2$.
:::

::: {.solution for="prob-mit1801n-3c-q2" status="draft"}
$\frac29(3x+5)^{3/2}\Big|_0^2=\frac29\big(11^{3/2}-5^{3/2}\big)\approx5.623$.
:::

::: {.solution for="prob-mit1801n-3c-q3" status="draft"}
With $u=x^2+1$: $\frac12\ln(x^2+1)\Big|_1^2=\frac12(\ln5-\ln2)=\frac12\ln\frac52\approx0.458$.
:::

::: {.solution for="prob-mit1801n-3c-q5" status="draft"}
One arch is $0\le x\le\pi$: $\int_0^\pi\sin x\,dx=-\cos x\Big|_0^\pi=2$ (@exm-ftc-1).
:::

::: {.solution for="prob-mit1801n-3d-q1" status="draft"}
a) Let $G(x)=\ln(x+\sqrt{x^2+a^2})-\ln a$. Then
$$G'(x)=\frac{1+\frac x{\sqrt{x^2+a^2}}}{x+\sqrt{x^2+a^2}}=\frac1{\sqrt{x^2+a^2}},$$
and $G(0)=\ln a-\ln a=0$. The left side also has derivative $\frac1{\sqrt{x^2+a^2}}$ (@thm-ftc-2) and value $0$ at $x=0$. Two functions with the same derivative differ by a constant (@thm-antiderivatives-differ-by-constant), and here the constant is $0$.

b) Both sides have the same derivative, so they are equal if they agree at $x=c$, where the left side is $0$: we need $\ln(c+\sqrt{c^2+a^2})=0$, i.e. $\sqrt{c^2+a^2}=1-c$. Squaring, $a^2=1-2c$, so $c=\frac{1-a^2}2$ (and then $1-c=\frac{1+a^2}2>0$, so the square root is consistent).
:::

::: {.solution for="prob-mit1801n-3d-q4" status="draft"}
By @thm-ftc-2:

b) $F(x)=2+\displaystyle\int_0^x\sin(t^3)\,dt$.

c) $F(x)=-1+\displaystyle\int_1^x\sin(t^3)\,dt$.
:::

::: {.solution for="prob-mit1801n-3d-q5" status="draft"}
a) For small $\Delta x$ the integral is the area of a thin strip of width $\Delta x$ and height about $f(1)=\frac1{\sqrt2}$; dividing by $\Delta x$ and letting $\Delta x\to0$ gives $\frac1{\sqrt2}$ (the integrand is continuous).

b) The expression is $\frac{F(1+\Delta x)-F(1)}{\Delta x}\to F'(1)=\frac{1}{\sqrt{1+1}}=\frac1{\sqrt2}$ by @thm-ftc-2.
:::

::: {.solution for="prob-mit1801n-3d-q8" status="draft"}
Differentiate both sides (@thm-ftc-2): $f(x)=2(\sin x+1)+2x\cos x$. So $f(\pi/2)=2\cdot2+0=4$.
:::

::: {.solution for="prob-mit1801n-3e-q1" status="draft"}
In $L(1/a)=\int_1^{1/a}\frac{dt}t$ put $t=1/u$, $dt=-\frac{du}{u^2}$; $t=1$ gives $u=1$ and $t=1/a$ gives $u=a$. By @thm-substitution-definite,
$$L(1/a)=\int_1^a u\Big(-\frac{du}{u^2}\Big)=-\int_1^a\frac{du}u=-L(a).$$
:::

::: {.solution for="prob-mit1801n-3e-q2" status="draft"}
a) Put $u=\sqrt2\,t$, $du=\sqrt2\,dt$: $E(x)=\frac{\sqrt2}{\sqrt{2\pi}}\int_0^{x/\sqrt2}e^{-t^2}dt=\frac1{\sqrt\pi}F\big(x/\sqrt2\big)$. Hence $\lim_{x\to\infty}E(x)=\frac1{\sqrt\pi}\cdot\frac{\sqrt\pi}2=\frac12$.

c) $\frac1{\sqrt{2\pi}}\int_a^b=\frac1{\sqrt{2\pi}}\Big(\int_0^b-\int_0^a\Big)=E(b)-E(a)$ (@prp-integral-properties). This is the probability that a standard normal variable lies between $a$ and $b$ (@def-normal-distribution).
:::

::: {.solution for="prob-mit1801n-3e-q3" status="draft"}
$u=\ln x$, $du=dx/x$; $x=1\mapsto u=0$, $x=e\mapsto u=1$: $\int_0^1\sqrt u\,du=\frac23$.
:::

::: {.solution for="prob-mit1801n-3e-q6" status="draft"}
b) On $[0,\pi]$, $0\le\sin x\le1$, so $\sin^2x\le\sin x$, with strict inequality except where $\sin x$ is $0$ or $1$. Hence $\int_0^\pi\sin^2x\,dx<\int_0^\pi\sin x\,dx=2$. (The exact value is $\pi/2$.)

c) $\sqrt{x^2+1}>x$, so $\int_{10}^{20}\sqrt{x^2+1}\,dx>\int_{10}^{20}x\,dx=\frac{400-100}2=150$ (@prp-integral-properties). (The integral is about $150.35$.)
:::
