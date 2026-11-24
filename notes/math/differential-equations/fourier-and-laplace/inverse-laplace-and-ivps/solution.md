<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-29-q1" status="draft"}
**(a)** The transfer function is $W(s)=\dfrac1{as+b}=\dfrac1a\cdot\dfrac1{s+b/a}$, so $w(t)=\dfrac1au(t)e^{-bt/a}$. The step response has transform $\dfrac1{s(as+b)}$. For $b\neq0$, partial fractions give $\dfrac1b\left(\dfrac1s-\dfrac{1}{s+b/a}\right)$, so $v(t)=\dfrac1bu(t)\left(1-e^{-bt/a}\right)$; for $b=0$, $v=\dfrac tau(t)$.

**(b)** Take $b\neq0$ and $t>0$.

(i) Try $x_p=ct+d$: $ac+bct+bd=t$ gives $c=\tfrac1b$, $d=-\tfrac a{b^2}$. Adding the transient $Ce^{-bt/a}$ and using $x(0)=0$: $C=\tfrac a{b^2}$, so
$$x=\frac tb-\frac a{b^2}+\frac a{b^2}e^{-bt/a}.$$

(ii) $w*t=\dfrac1a\displaystyle\int_0^te^{-b(t-\tau)/a}\,\tau\,d\tau$. Integrating by parts, $\displaystyle\int_0^t\tau e^{b\tau/a}d\tau=\frac ab te^{bt/a}-\frac{a^2}{b^2}\left(e^{bt/a}-1\right)$; multiplying by $\frac1ae^{-bt/a}$ gives the same $x$.

(iii) $(as+b)X=\dfrac1{s^2}$, so $X=\dfrac{1}{s^2(as+b)}=\dfrac{1}{b\,s^2}-\dfrac{a}{b^2s}+\dfrac{a^2}{b^2(as+b)}$, which inverts to the same $x$.

(If $b=0$ all three methods give $x=\dfrac{t^2}{2a}$.)
:::
