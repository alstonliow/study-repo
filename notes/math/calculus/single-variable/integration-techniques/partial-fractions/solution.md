<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-7-q4" status="draft"}
a) $\frac{\cos x}{1-\sin^2x}=\frac{\cos x}{\cos^2x}=\frac1{\cos x}=\sec x$. With $u=\sin x$, $du=\cos x\,dx$:
$$\int\sec x\,dx=\int\frac{du}{1-u^2}=\int\frac12\Big(\frac1{1+u}+\frac1{1-u}\Big)du=\frac12\ln\Big|\frac{1+u}{1-u}\Big|+c=\frac12\ln\frac{1+\sin x}{1-\sin x}+c,$$
using cover-up (@prp-cover-up): $\frac1{(1-u)(1+u)}$ has coefficient $\frac12$ at both factors. (The fraction is positive since $\lvert\sin x\rvert<1$ where $\sec x$ is defined.)

b) $\frac{1+\sin x}{1-\sin x}=\frac{(1+\sin x)^2}{1-\sin^2x}=\frac{(1+\sin x)^2}{\cos^2x}$, so
$$\frac12\ln\frac{(1+\sin x)^2}{\cos^2x}=\ln\Big|\frac{1+\sin x}{\cos x}\Big|=\ln\lvert\sec x+\tan x\rvert,$$
the formula of @prp-tan-sec-integrals.
:::

::: {.solution for="prob-mit1801n-5e-q2" status="draft"}
Cover-up (@prp-cover-up): $\frac x{(x-2)(x+3)}=\frac{2/5}{x-2}+\frac{3/5}{x+3}$, so the integral is $\frac25\ln\lvert x-2\rvert+\frac35\ln\lvert x+3\rvert+c$.
:::

::: {.solution for="prob-mit1801n-5e-q3" status="draft"}
$\frac{x}{(x-2)(x+2)(x+3)}=\frac{1/10}{x-2}+\frac{1/2}{x+2}-\frac{3/5}{x+3}$ (cover-up at $2,-2,-3$), so the integral is $\frac1{10}\ln\lvert x-2\rvert+\frac12\ln\lvert x+2\rvert-\frac35\ln\lvert x+3\rvert+c$.
:::

::: {.solution for="prob-mit1801n-5e-q5" status="draft"}
$\frac{3x+2}{x(x+1)^2}=\frac Ax+\frac B{x+1}+\frac C{(x+1)^2}$: cover-up gives $A=2$ and $C=\frac{-1}{-1}=1$; the $x^2$ coefficients give $A+B=0$, so $B=-2$. The integral is $2\ln\lvert x\rvert-2\ln\lvert x+1\rvert-\frac1{x+1}+c$.
:::

::: {.solution for="prob-mit1801n-5e-q6" status="draft"}
$\frac{2x-9}{(x^2+9)(x+2)}=\frac A{x+2}+\frac{Bx+C}{x^2+9}$ with $A=\frac{-13}{13}=-1$ (cover-up); comparing coefficients in $2x-9=-(x^2+9)+(Bx+C)(x+2)$ gives $B=1$, $C=0$. The integral is $-\ln\lvert x+2\rvert+\frac12\ln(x^2+9)+c$.
:::

::: {.solution for="prob-mit1801n-5e-q10" status="draft"}
Divide first: $\frac{x^2+1}{x^2+2x+2}=1-\frac{2x+1}{x^2+2x+2}=1-\frac{2x+2}{x^2+2x+2}+\frac1{(x+1)^2+1}$. So the integral is
$$x-\ln(x^2+2x+2)+\tan^{-1}(x+1)+c .$$
:::
