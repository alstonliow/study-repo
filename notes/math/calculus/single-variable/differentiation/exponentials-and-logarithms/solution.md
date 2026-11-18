<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-2a-q6" status="draft"}
Let $y=u_1u_2\cdots u_n$ and suppose first all $u_i>0$. Then $\ln y=\ln u_1+\dots+\ln u_n$, and differentiating (@prp-logarithmic-differentiation)
$$\frac{y'}{y}=\frac{u_1'}{u_1}+\dots+\frac{u_n'}{u_n}.$$
Multiplying by $y$, the $i$-th term becomes $u_1\cdots u_{i-1}u_i'u_{i+1}\cdots u_n$, which is the formula of @prob-mit1801f06-1-q7. If some $u_i$ are negative, apply the argument to $\lvert y\rvert=\lvert u_1\rvert\cdots\lvert u_n\rvert$, using $(\ln\lvert u\rvert)'=u'/u$; at points where some $u_i=0$ the formula still holds by continuity of both sides, or by the inductive proof.
:::

::: {.solution for="prob-mit1801n-1h-q1" status="draft"}
a) $y_0e^{k\lambda}=\frac12y_0$ gives $k\lambda=\ln\frac12=-\ln2$, so $\lambda=-\frac{\ln2}k$ (positive, since $k<0$ for decay).

b) $y(t_1+\lambda)=y_0e^{kt_1}e^{k\lambda}=y_1\cdot\frac12$.
:::

::: {.solution for="prob-mit1801n-1h-q2" status="draft"}
$\mathrm{pH}=-\log_{10}[\mathrm H^+]$, and dilution halves the concentration, so
$$(\mathrm{pH})_{\text{diluted}}=-\log_{10}\frac{[\mathrm H^+]}2=(\mathrm{pH})_{\text{original}}+\log_{10}2\approx(\mathrm{pH})_{\text{original}}+0.3 .$$
:::

::: {.solution for="prob-mit1801n-1h-q3" status="draft"}
$\ln\big((y+1)(y-1)\big)=\ln(xe^{2x})$, so $y^2-1=xe^{2x}$ and, since $y>1$ for the logarithms to be defined, $y=\sqrt{1+xe^{2x}}$ (with $x>0$).
:::

::: {.solution for="prob-mit1801n-1h-q5" status="draft"}
With $u=e^x>0$: $u+\frac1u=y$, i.e. $u^2-yu+1=0$, so $u=\frac{y\pm\sqrt{y^2-4}}2$ (both roots are positive; real only for $y\ge2$). Hence
$$x=\ln\frac{y\pm\sqrt{y^2-4}}2,\qquad y\ge2,$$
the two signs giving the two values $\pm x$ (their product is $1$).
:::

::: {.solution for="prob-mit1801n-1i-q1" status="draft"}
c) $-2xe^{-x^2}$. d) $\ln x+1-1=\ln x$. e) $\frac{2x}{x^2}=\frac2x$. f) $\frac{2\ln x}x$.

m) $\dfrac{-e^x(1+e^x)-(1-e^x)e^x}{(1+e^x)^2}=\dfrac{-2e^x}{(1+e^x)^2}$.
:::

::: {.solution for="prob-mit1801n-1i-q4" status="draft"}
$\big(1+\frac1n\big)^{3n}=\Big(\big(1+\frac1n\big)^n\Big)^3\to e^3$, since $t\mapsto t^3$ is continuous.
:::

::: {.solution for="prob-mit1801n-5a-q5" status="draft"}
a) $\sinh$ is odd; $(\sinh x)'=\cosh x>0$, so it is increasing with no critical points; $(\sinh x)''=\sinh x$ is negative for $x<0$ and positive for $x>0$, so the only inflection point is the origin, where the slope is $1$. $\sinh x\to\pm\infty$ as $x\to\pm\infty$ (like $\pm\frac12e^{\lvert x\rvert}$).

b) Since $\sinh$ is increasing from $-\infty$ to $\infty$, it has an inverse defined on all of $\mathbb R$: $y=\sinh^{-1}x$ means $\sinh y=x$. Solving $e^y-e^{-y}=2x$ as a quadratic in $u=e^y>0$ gives $\sinh^{-1}x=\ln\big(x+\sqrt{x^2+1}\big)$. Its graph is the reflection of the graph of $\sinh$ in $y=x$: odd, increasing, through the origin with slope $1$, growing like $\ln(2x)$.

c) From $\sinh y=x$: $\cosh y\,y'=1$, and $\cosh y=\sqrt{1+\sinh^2y}=\sqrt{1+x^2}$, so $\dfrac{d}{dx}\sinh^{-1}x=\dfrac1{\sqrt{1+x^2}}$.
:::
