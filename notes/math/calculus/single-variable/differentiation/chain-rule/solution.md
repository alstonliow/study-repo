<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     Problem-set problems (prob-mit1801f06-*): no official solutions were available.
     Notes exercises (prob-mit1801n-*): checked by computation (Python/sympy) and compared with the official
     solutions in section S of the 18.01 Notes where they were consulted (1A, 1B, 1C, 2C-13 to 2E-10). -->

::: {.solution for="prob-mit1801f06-2a-q2" status="draft"}
a) By @thm-derivative-chain-rule twice: $3\tan^2(x^4)\cdot\sec^2(x^4)\cdot4x^3=12x^3\tan^2(x^4)\sec^2(x^4)$.

b) *Product rule:* $2\sin y\cos y\cdot\cos^2y+\sin^2y\cdot2\cos y(-\sin y)=2\sin y\cos y(\cos^2y-\sin^2y)=\sin2y\cos2y$.

*As $f(2y)$:* $\sin y\cos y=\frac12\sin2y$, so $\sin^2y\cos^2y=\frac14\sin^2(2y)=f(2y)$ with $f(u)=\frac14\sin^2u$. Then $\frac{d}{dy}f(2y)=2f'(2y)=2\cdot\frac12\sin2y\cos2y=\sin2y\cos2y$.

The answers agree; both equal $\frac12\sin4y$.
:::

::: {.solution for="prob-mit1801f06-2a-q3" status="draft"}
a) $y'=u'v+uv'$ by the product rule. Differentiating each term again, $y''=(u''v+u'v')+(u'v'+uv'')=u''v+2u'v'+uv''$.

b) Differentiate each term of (a) by the product rule: $(u''v)'=u'''v+u''v'$, $(2u'v')'=2u''v'+2u'v''$, $(uv'')'=u'v''+uv'''$. Adding,
$$y'''=u'''v+3u''v'+3u'v''+uv'''.$$
The coefficients $1,2,1$ and $1,3,3,1$ are binomial coefficients (Leibniz's rule).
:::

::: {.solution for="prob-mit1801n-1j-q1" status="draft"}
a) $10x\cos(5x^2)$.

b) $2\sin(3x)\cdot3\cos(3x)=6\sin3x\cos3x=3\sin6x$.

e) $\dfrac{x\cos x-\sin x}{x^2}$.

m) The derivatives are $-2\sin2x$; $-2\cos x\sin x-2\sin x\cos x=-4\sin x\cos x=-2\sin2x$; and $-4\cos x\sin x=-2\sin2x$. All the same. The first two functions are equal (double-angle formula), but $2\cos^2x=1+\cos2x$ is larger by the constant $1$: equal derivatives only force a constant difference (@cor-sign-of-derivative).
:::

::: {.solution for="prob-mit1801n-1f-q1" status="draft"}
a) Chain rule: $2(x^2+2)\cdot2x=4x^3+8x$. Expanding first: $(x^4+4x^2+4)'=4x^3+8x$.

b) Chain rule: $100(x^2+2)^{99}\cdot2x=200x(x^2+2)^{99}$. Expanding a hundredth power would be hopeless, so the chain rule is the method of choice.
:::

::: {.solution for="prob-mit1801n-1f-q2" status="draft"}
$10x^9(x^2+1)^{10}+x^{10}\cdot10(x^2+1)^9\cdot2x=10x^9(x^2+1)^9(3x^2+1)$.
:::

::: {.solution for="prob-mit1801n-1f-q6" status="draft"}
If $f(-x)=f(x)$ for all $x$, differentiating both sides gives $-f'(-x)=f'(x)$, i.e. $f'(-x)=-f'(x)$: $f'$ is odd. If $f(-x)=-f(x)$, differentiating gives $-f'(-x)=-f'(x)$, i.e. $f'(-x)=f'(x)$: $f'$ is even.
:::

::: {.solution for="prob-mit1801n-1f-q7" status="draft"}
b) $m=m_0(1-v^2/c^2)^{-1/2}$, so $\dfrac{dm}{dv}=-\frac12m_0(1-v^2/c^2)^{-3/2}\cdot\Big(-\frac{2v}{c^2}\Big)=\dfrac{m_0v}{c^2(1-v^2/c^2)^{3/2}}$.

d) $\dfrac{dQ}{dt}=\dfrac{a}{(1+bt^2)^3}-\dfrac{3at\cdot2bt}{(1+bt^2)^4}=\dfrac{a(1-5bt^2)}{(1+bt^2)^4}$.
:::

::: {.solution for="prob-mit1801n-1g-q1" status="draft"}
$y=1-\frac5{x+5}$, so $y'=\frac5{(x+5)^2}$ and $y''=-\frac{10}{(x+5)^3}$.
:::

::: {.solution for="prob-mit1801n-1g-q5" status="draft"}
a) $y'=u'v+uv'$, $y''=u''v+2u'v'+uv''$, $y'''=u'''v+3u''v'+3u'v''+uv'''$ (as in @prob-mit1801f06-2a-q3).

b) For $n=1,2,3$ Leibniz' formula has coefficients $1,1$; $1,2,1$; $1,3,3,1$, matching (a). For $u=x^p$, $v=(1+x)^q$ with $n=p+q$: $u^{(k)}=0$ for $k>p$ and $v^{(j)}=0$ for $j>q$, so in the term $\binom nku^{(k)}v^{(n-k)}$ both factors are non-zero only when $k\le p$ and $n-k\le q$, i.e. $k=p$. Using $u^{(p)}=p!$ and $v^{(q)}=q!$ (@prp-nth-derivative-power),
$$y^{(p+q)}=\binom{p+q}{p}p!\,q!=(p+q)!.$$
:::
