<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-4-q1" status="draft"}
a) For $x>0$, @thm-mean-value gives $c\in(0,x)$ with $f(x)=f(0)+f'(c)\,x=f'(c)\,x\ge0$.

b) $f(x)=x-\ln(1+x)$ has $f(0)=0$ and $f'(x)=1-\frac1{1+x}=\frac x{1+x}\ge0$ for $x\ge0$. By (a), $f\ge0$, i.e. $\ln(1+x)\le x$.

c) $g(x)=\ln(1+x)-x+\frac{x^2}2$: $g(0)=0$, $g'(x)=\frac1{1+x}-1+x=\frac{x^2}{1+x}\ge0$, so $g\ge0$.
$k(x)=x-\frac{x^2}2+\frac{x^3}3-\ln(1+x)$: $k(0)=0$, $k'(x)=1-x+x^2-\frac1{1+x}=\frac{(1-x+x^2)(1+x)-1}{1+x}=\frac{x^3}{1+x}\ge0$, so $k\ge0$.

d) With $S_n(x)=x-\frac{x^2}2+\frac{x^3}3-\dots+(-1)^{n+1}\frac{x^n}n$, for $x\ge0$:
$$S_{2m}(x)\le\ln(1+x)\le S_{2m+1}(x)\qquad(m\ge0).$$
(It is true: the derivative of $\pm(\ln(1+x)-S_n(x))$ is $\pm(-1)^n\frac{x^n}{1+x}$, by the geometric sum.)

e) Put $u=-x\in[0,1)$; we need $\ln(1-u)\le-u$. Let $f(u)=-u-\ln(1-u)$: $f(0)=0$ and $f'(u)=-1+\frac1{1-u}=\frac u{1-u}\ge0$ on $[0,1)$, so by (a) $f(u)\ge0$, which is the claim.
:::
