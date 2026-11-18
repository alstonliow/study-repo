<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-7-q1" status="draft"}
(Take $a>0$.)

a) $\displaystyle\int_1^ae^{-xy}\,dy=\Big[-\frac{e^{-xy}}x\Big]_{y=1}^{y=a}=\frac{e^{-x}-e^{-ax}}x$.

b) $\displaystyle\int_0^\infty\frac{e^{-x}-e^{-ax}}x\,dx=\int_0^\infty\!\!\int_1^ae^{-xy}\,dy\,dx=\int_1^a\!\!\int_0^\infty e^{-xy}\,dx\,dy=\int_1^a\frac{dy}y=\ln a .$

(The integrand is positive for $a>1$, so exchanging the order of these improper integrals is allowed; for $a<1$ apply the same to $-1$ times the integrand.)
:::

::: {.solution for="prob-mit1802f07-7-q4" status="draft"}
By rotational symmetry we may put one vertex at $(1,0)$; the other two have independent uniformly distributed angles $\theta_1,\theta_2\in[0,2\pi]$. The area does not depend on which of the two is called $\theta_1$, so we may average over the triangle $R:0\le\theta_1\le\theta_2\le2\pi$, of area $2\pi^2$, where (Problem Set 4, Problem 2) $A=\frac12\big(\sin\theta_1+\sin(\theta_2-\theta_1)-\sin\theta_2\big)\ge0$.

Inner integral: $\int_0^{\theta_2}A\,d\theta_1=\frac12\big[(1-\cos\theta_2)+(1-\cos\theta_2)-\theta_2\sin\theta_2\big]=1-\cos\theta_2-\frac12\theta_2\sin\theta_2$.

Outer integral: $\int_0^{2\pi}\big(1-\cos\theta_2-\frac12\theta_2\sin\theta_2\big)\,d\theta_2=2\pi-0-\frac12(-2\pi)=3\pi$ (using $\int_0^{2\pi}\theta\sin\theta\,d\theta=-2\pi$).

Average area $=\dfrac{3\pi}{2\pi^2}=\dfrac3{2\pi}\approx0.477$. The maximum $\frac{3\sqrt3}4\approx1.299$ is $\frac{\pi\sqrt3}2\approx2.72$ times the average.
:::

::: {.solution for="prob-mit1802n-3a-q1" status="draft"}
a) Inner: $[6x^2y+y^2]_{-1}^1=12x^2$. Outer: $\int_0^212x^2\,dx=32$.

b) Inner: $[-u\cos t+\frac{t^2}2\cos u]_0^\pi=2u+\frac{\pi^2}2\cos u$. Outer: $\big[u^2+\frac{\pi^2}2\sin u\big]_0^{\pi/2}=\frac{\pi^2}4+\frac{\pi^2}2=\frac{3\pi^2}4$.

c) Inner: $[x^2y^2]_{\sqrt x}^{x^2}=x^6-x^3$. Outer: $\frac17-\frac14=-\frac3{28}$.

d) Inner: $u\sqrt{u^2+4}$. Outer: $\big[\frac13(u^2+4)^{3/2}\big]_0^1=\frac{5\sqrt5-8}3$.
:::

::: {.solution for="prob-mit1802n-3a-q2" status="draft"}
a) $R$: $0\le y\le2$, $-y\le x\le0$. i) $\displaystyle\int_{-2}^0\!\!\int_{-x}^2dy\,dx$  ii) $\displaystyle\int_0^2\!\!\int_{-y}^0dx\,dy$.

b) i) $\displaystyle\int_0^2\!\!\int_0^{2x-x^2}dy\,dx$  ii) Solving $y=2x-x^2$ for $x$: $x=1\pm\sqrt{1-y}$, so $\displaystyle\int_0^1\!\!\int_{1-\sqrt{1-y}}^{1+\sqrt{1-y}}dx\,dy$.

c) The line $y=x$ meets the circle at $(\sqrt2,\sqrt2)$. i) Two pieces: $\displaystyle\int_0^{\sqrt2}\!\!\int_0^xdy\,dx+\int_{\sqrt2}^2\!\!\int_0^{\sqrt{4-x^2}}dy\,dx$  ii) $\displaystyle\int_0^{\sqrt2}\!\!\int_y^{\sqrt{4-y^2}}dx\,dy$.
:::

::: {.solution for="prob-mit1802n-3a-q3" status="draft"}
a) $\displaystyle\int_0^2\!\!\int_0^{(2-x)/2}x\,dy\,dx=\int_0^2\Big(x-\frac{x^2}2\Big)dx=2-\frac43=\frac23$.

b) $\displaystyle\int_0^1\!\!\int_0^{1-y^2}(2x+y^2)\,dx\,dy=\int_0^1\big[(1-y^2)^2+y^2(1-y^2)\big]dy=\int_0^1(1-y^2)\,dy=\frac23$.
:::

::: {.solution for="prob-mit1802n-3a-q4" status="draft"}
b) $R$: $0\le x\le1$, $x^2\le y\le x$. $V=\displaystyle\int_0^1\!\!\int_{x^2}^xxy\,dy\,dx=\int_0^1\frac{x^3-x^5}2\,dx=\frac12\Big(\frac14-\frac16\Big)=\frac1{24}$.

c) $x^2-y^2\ge0$ means $|y|\le x$. $V=\displaystyle\int_0^1\!\!\int_{-x}^x(x^2-y^2)\,dy\,dx=\int_0^1\frac43x^3\,dx=\frac13$.
:::

::: {.solution for="prob-mit1802n-3a-q5" status="draft"}
a) $R$: $0\le x\le y\le2$. $\displaystyle\int_0^2\!\!\int_0^ye^{-y^2}\,dx\,dy=\int_0^2ye^{-y^2}\,dy=\frac{1-e^{-4}}2$.

b) $R$: $0\le u\le\frac12$, $0\le t\le u^2$. $\displaystyle\int_0^{1/2}\!\!\int_0^{u^2}\frac{e^u}u\,dt\,du=\int_0^{1/2}ue^u\,du=\big[(u-1)e^u\big]_0^{1/2}=1-\frac{\sqrt e}2$.

c) $R$: $0\le u\le1$, $0\le x\le u^3$. $\displaystyle\int_0^1\!\!\int_0^{u^3}\frac{dx\,du}{1+u^4}=\int_0^1\frac{u^3}{1+u^4}\,du=\frac{\ln2}4$.
:::

::: {.solution for="prob-mit1802n-3a-q6" status="draft"}
$R$ is symmetric under $x\to-x$ and under $y\to-y$.

- $\iint x\,dA=0$ (odd in $x$).
- $\iint e^x\,dA=2\iint_{\text{upper half-disc}}e^x\,dA$ (even in $y$; not zero, since $e^x>0$).
- $\iint x^2\,dA=4\iint_{\text{first quadrant}}x^2\,dA$ (even in both).
- $\iint x^2y\,dA=0$ (odd in $y$).
- $\iint(x^2+y)\,dA=\iint x^2\,dA=4\iint_{\text{first quadrant}}x^2\,dA$ (the $y$ part is $0$).
- $\iint xy\,dA=0$.
:::
