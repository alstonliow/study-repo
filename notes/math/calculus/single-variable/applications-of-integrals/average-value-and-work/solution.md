<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

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

::: {.solution for="prob-mit1801n-4d-q2" status="draft"}
$\frac1{2a-a}\int_a^{2a}\frac{dx}x=\frac1a(\ln2a-\ln a)=\frac{\ln2}a$, so $C=\ln2$.
:::

::: {.solution for="prob-mit1801n-4d-q3" status="draft"}
$\operatorname{Ave}(v)=\frac1{b-a}\int_a^bs'(t)\,dt=\frac{s(b)-s(a)}{b-a}$ by @thm-ftc-1, which is the average velocity (distance travelled over time).
:::

::: {.solution for="prob-mit1801n-4d-q5" status="draft"}
$\int_0^xf(t)\,dt=x\,g(x)$. Differentiating (@thm-ftc-2), $f(x)=g(x)+x\,g'(x)$.
:::

::: {.solution for="prob-mit1801n-4j-q1" status="draft"}
A layer of water at depth $x$ and thickness $dx$ has volume $\pi\big(\frac12\big)^2dx=\frac\pi4dx$ and must be lifted $x$ meters, which takes $k\,x\,\frac\pi4dx$. Adding up the layers (@def-work),
$$E=\int_0^{100}\frac{\pi k}4\,x\,dx=\frac{\pi k}4\cdot5000=1250\pi k\approx3927k .$$
:::

::: {.solution for="prob-mit1801n-4j-q2" status="draft"}
During $[t,t+dt]$ the material present, $x_0e^{-kt}$ grams, produces about $r\,x_0e^{-kt}dt$ units. Over $60$ minutes,
$$R=\int_0^{60}rx_0e^{-kt}\,dt=\frac{rx_0}k\big(1-e^{-60k}\big).$$
:::

::: {.solution for="prob-mit1801n-4j-q3" status="draft"}
The ring between $r$ and $r+dr$ holds water of volume $2\pi r\,D\,dr$ at concentration $\frac k{1+r^2}$ (rings, as in @exm-pipe-flow). So
$$A=\int_0^R\frac{k}{1+r^2}\,2\pi rD\,dr=\pi kD\ln(1+R^2)\ \text{grams}.$$
:::
