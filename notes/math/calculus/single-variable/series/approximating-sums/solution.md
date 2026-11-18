<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-7-q3" status="draft"}
(a) $f(x)=\frac1{(2x+1)^2}$ is decreasing, and $\int_k^\infty f(x)\,dx=\frac1{2(2k+1)}$. Keep the first term $f(1)=\frac19$ and bound the rest as in @thm-integral-bounds (letting $n\to\infty$):
$$\int_2^\infty f\le\sum_{i\ge2}f(i)\le f(2)+\int_2^\infty f,\quad\text{i.e.}\quad\tfrac1{10}\le\sum_{i\ge2}f(i)\le\tfrac1{25}+\tfrac1{10}.$$
So $0.2111\le\sum_{i\ge1}f(i)\le0.2511$, bounds that differ by $0.04$. (The exact value is $\frac{\pi^2}8-1\approx0.2337$.)

(b) Inequality 1 holds; inequality 2 fails.

1. On $[i-1,i]$, $\ln(x+2)\ge\ln(i+1)$, so $\ln(i+1)\le\int_{i-1}^i\ln(x+2)\,dx$; sum over $i=1,\dots,n$.

2. On $[i-1,i]$, $\ln(x+1)\le\ln(i+1)$, with strict inequality except at $x=i$, so $\int_1^n\ln(x+1)\,dx<\sum_{i=2}^n\ln(i+1)$ for $n>1$. Adding $\ln2$ gives $\ln2+\int_1^n\ln(x+1)\,dx<\sum_{i=1}^n\ln(i+1)$: the inequality goes the other way.
:::

::: {.solution for="prob-mit6042f10-7-q4" status="draft"}
(a) During second $i$ the rug is $i$ metres $=100i$ cm long, so the bug crosses $\frac1{100i}$ of it.

(b) A uniform stretch does not change the fraction of the rug behind the bug, so the fractions add up: $\sum_{i=1}^n\frac1{100i}=\frac{H_n}{100}$.

(c) The bug arrives when $H_n\ge100$. Since $H_n\approx\ln n+\gamma$ with $\gamma\approx0.577$ (@cor-harmonic-bounds gives $\ln(n+1)\le H_n\le1+\ln n$), this needs $n\approx e^{100-\gamma}\approx1.5\times10^{43}$ seconds. The bug does make it, eventually.
:::

::: {.solution for="prob-mit6042f10-7-q6" status="draft"}
(a) $\frac{n!}{(n+1)!}=\frac1{n+1}\to0$. So $n!=o((n+1)!)$ and hence $n!=O((n+1)!)$ are true; $\Omega$, $\Theta$ and $\omega$ are false.

(b) By @prp-factorial-bounds, $n!\ge e(n/e)^n$, so
$$\frac{n!}{(n/3)^{n+e}}\ge e\Bigl(\frac3e\Bigr)^n\Bigl(\frac3n\Bigr)^e\to\infty,$$
because $\frac3e>1$ and the exponential $(3/e)^n$ outgrows the polynomial factor $n^e$.

(c) $n!=1\cdot2\cdot3\cdots n\ge1\cdot2\cdot2\cdots2=2^{n-1}$ for $n\ge1$, so $n!\ge\frac12\cdot2^n$, i.e. $n!=\Omega(2^n)$.
:::
