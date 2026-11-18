<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

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
