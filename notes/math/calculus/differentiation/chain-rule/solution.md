<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

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
