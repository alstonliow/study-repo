<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-6-q2" status="draft"}
The period is $T=\frac1{60}$ s. Using $\sin^2u=\frac{1-\cos2u}2$ (@prp-sine-cosine-powers-even),
$$\operatorname{Ave}(V^2)=60\int_0^{1/60}C^2\sin^2(120\pi t)\,dt=60C^2\Big[\frac t2-\frac{\sin(240\pi t)}{480\pi}\Big]_0^{1/60}=60C^2\cdot\frac1{120}=\frac{C^2}2 .$$
So the RMS voltage is $\sqrt{C^2/2}=C/\sqrt2\approx0.707\,C$. (For a $120$ V RMS supply the peak is about $170$ V.)
:::

::: {.solution for="prob-mit1801f06-6-q3" status="draft"}
a) The part of the unit square above $y=x^2$ has area $\int_0^1(1-x^2)\,dx=\frac23$, so the probability is $\frac23$.

b) In $[0,2]^2$, $x^2<y\le2$ requires $x<\sqrt2$, and the area is $\int_0^{\sqrt2}(2-x^2)\,dx=2\sqrt2-\frac{2\sqrt2}3=\frac{4\sqrt2}3$. Dividing by the whole area $4$: $\frac{\sqrt2}3\approx0.471$.

c) For $a>0$, $\int_0^Ne^{-at}dt=\frac{1-e^{-aN}}a\to\frac1a$, so $W=\frac1a$ (@exm-improper-basic). (For $a\le0$ the integral diverges.)

d) $P([0,T])=a\int_0^Te^{-at}dt=1-e^{-aT}$. Half-life $1$ means $e^{-a}=\frac12$, so $a=\ln2\approx0.693$ and $W=\frac1{\ln2}\approx1.443$. The probability of decay during $1\le t\le2$ is
$$P([1,2])=\ln2\int_1^2e^{-t\ln2}\,dt=\ln2\int_1^22^{-t}\,dt=e^{-a}-e^{-2a}=\frac12-\frac14=0.25 .$$
:::
