<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-7-q3" status="draft"}
a) $\int\tan^{n+2}x\,dx=\int\tan^nx\,(\sec^2x-1)\,dx=\int\tan^nx\sec^2x\,dx-\int\tan^nx\,dx$. In the first integral put $u=\tan x$, $du=\sec^2x\,dx$: it is $\int u^n\,du=\frac{\tan^{n+1}x}{n+1}+c$.

b) With $n=2$ and then $n=0$: $\int\tan^4x\,dx=\frac{\tan^3x}3-\int\tan^2x\,dx=\frac{\tan^3x}3-\Big(\tan x-\int dx\Big)=\frac{\tan^3x}3-\tan x+x+c$.
:::

::: {.solution for="prob-mit1801n-5c-q5" status="draft"}
As in @exm-odd-power: $-\frac{\cos^3x}3+\frac{\cos^5x}5+c$.
:::

::: {.solution for="prob-mit1801n-5c-q7" status="draft"}
$\sin4x\cos4x=\frac12\sin8x$, so the integrand is $\frac14\sin^28x=\frac18(1-\cos16x)$, and the integral is $\frac x8-\frac{\sin16x}{128}+c$.
:::

::: {.solution for="prob-mit1801n-5c-q9" status="draft"}
$\int\frac{(1-\cos^2x)\sin x}{\cos^2x}dx$; with $u=\cos x$: $-\int(u^{-2}-1)\,du=\frac1u+u=\sec x+\cos x+c$.
:::

::: {.solution for="prob-mit1801n-5c-q11" status="draft"}
$\cos2x=2\cos^2x-1$; with $u=\cos x$: $-\int(2u^2-1)\,du=\cos x-\frac23\cos^3x+c$.
:::
