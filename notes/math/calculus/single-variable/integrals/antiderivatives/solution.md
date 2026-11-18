<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-4-q2" status="draft"}
$\frac{d}{dx}\frac12\tan^2x=\tan x\sec^2x$ (chain rule, $(\tan x)'=\sec^2x$), and $\frac{d}{dx}\frac12\sec^2x=\sec x\cdot\sec x\tan x=\tan x\sec^2x$. So both are antiderivatives (substitutions $u=\tan x$ and $u=\sec x$ respectively).

There is no contradiction: $\frac12\sec^2x-\frac12\tan^2x=\frac12$ is constant, and by @thm-antiderivatives-differ-by-constant two antiderivatives may differ by a constant. Each formula should be read with its own $+c$.
:::

::: {.solution for="prob-mit1801n-3a-q1" status="draft"}
d) $d(e^{3x}\sin x)=(3e^{3x}\sin x+e^{3x}\cos x)\,dx=e^{3x}(3\sin x+\cos x)\,dx$.

e) $\frac{dx}{2\sqrt x}+\frac{dy}{2\sqrt y}=0$, so $dy=-\frac{\sqrt y}{\sqrt x}\,dx=-\frac{1-\sqrt x}{\sqrt x}\,dx=\Big(1-\frac1{\sqrt x}\Big)dx$.
:::

::: {.solution for="prob-mit1801n-3a-q2" status="draft"}
a) $\frac25x^5+x^3+\frac12x^2+8x+c$.

c) With $u=8+9x$, $du=9\,dx$: $\frac19\int u^{1/2}du=\frac2{27}(8+9x)^{3/2}+c$.

e) With $u=8-2x^2$, $du=-4x\,dx$: $-\frac14\int u^{-1/2}du=-\frac12\sqrt{8-2x^2}+c$.

g) With $u=x^5$: $\frac75e^{x^5}+c$.

i) $\frac13\ln\lvert3x+2\rvert+c$.

k) $\frac x{x+5}=1-\frac5{x+5}$, so the integral is $x-5\ln\lvert x+5\rvert+c$.

(Each is checked by differentiating, @thm-substitution-indefinite.)
:::

::: {.solution for="prob-mit1801n-3a-q3" status="draft"}
a) $-\frac15\cos5x+c$.

c) With $u=\cos x$, $du=-\sin x\,dx$: $-\int u^2du=-\frac13\cos^3x+c$.

e) $5\tan(x/5)+c$.

g) $\sec^9x\tan x=\sec^8x\cdot(\sec x\tan x)$; with $u=\sec x$, $du=\sec x\tan x\,dx$: $\int u^8du=\frac19\sec^9x+c$.
:::

::: {.solution for="prob-mit1801n-5b-q9" status="draft"}
With $u=1+e^x$: $\int u^{-1/3}du=\frac32(1+e^x)^{2/3}+c$.
:::

::: {.solution for="prob-mit1801n-5b-q11" status="draft"}
$\frac19\tan9x+c$.
:::

::: {.solution for="prob-mit1801n-5b-q13" status="draft"}
$u=x^3$, $du=3x^2dx$: $\frac13\int\frac{du}{1+u^2}=\frac13\tan^{-1}(x^3)+c$.
:::

::: {.solution for="prob-mit1801n-5b-q16" status="draft"}
With $u=\tan^{-1}x$, $du=\frac{dx}{1+x^2}$, and limits $\mp\frac\pi4$ (@thm-substitution-definite): $\int_{-\pi/4}^{\pi/4}u\,du=0$. (Also clear because the integrand is odd.)
:::
