<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6041f10-6-q1" status="draft"}
(a) $\int_1^2\int_0^xax\,dy\,dx=a\int_1^2x^2\,dx=\frac{7a}3$, so $a=\frac37$.

(b) For $0\le y\le1$ the section is $1\le x\le2$: $f_Y(y)=\int_1^2\frac37x\,dx=\frac9{14}$. For $1\le y\le2$ it is $y\le x\le2$: $f_Y(y)=\frac3{14}(4-y^2)$. Otherwise $f_Y(y)=0$.

(c) Given $Y=\frac32$, $f_{X\mid Y}(x\mid\frac32)\propto x$ on $[\frac32,2]$, so
$$E\Bigl[\frac1X\Bigm|Y=\tfrac32\Bigr]=\frac{\int_{3/2}^21\,dx}{\int_{3/2}^2x\,dx}=\frac{1/2}{7/8}=\frac47.$$

(d)

1. $f_X(x)=\int_0^x\frac37x\,dy=\frac37x^2$ on $[1,2]$, and given $X=x$ the density of $Y$ is constant in $y$, so $Y$ is uniform on $[0,x]$ and $Z=Y-X$ is uniform on $[-x,0]$.

2. By total probability, $f_Z(z)=\int f_X(x)\frac1x\mathbf 1\{-x\le z\le0\}\,dx=\int_{\max(1,-z)}^2\frac37x\,dx$.

3. Hence $f_Z(z)=\frac9{14}$ for $-1\le z\le0$, $f_Z(z)=\frac3{14}(4-z^2)$ for $-2\le z\le-1$, and $0$ otherwise (the mirror image of $f_Y$).
:::
