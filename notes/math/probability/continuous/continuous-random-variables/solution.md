<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-13-q4" status="draft"}
Measure time in hours after noon. The arrival times $(A,B)$ are uniform on the unit square, with joint density $1$ (@thm-independent-joint-density). They meet exactly when $|A-B|\le\frac14$. The complement consists of two right triangles with legs $\frac34$, of total area $2\cdot\frac12\cdot\bigl(\frac34\bigr)^2=\frac9{16}$. So they meet with probability $1-\frac9{16}=\frac7{16}$.
:::

::: {.solution for="prob-cs70hw-14-q1" status="draft"}
(a) $Y$ takes values in $[1,5]$, and for $1\le y\le5$, $\Pr(Y\le y)=\Pr\bigl(X\le\frac{y-1}2\bigr)=\frac{y-1}4$. So $Y\sim U[1,5]$: CDF $\frac{y-1}4$ on $[1,5]$ ($0$ before, $1$ after), PDF $\frac14$ on $[1,5]$. $E[Y]=2E[X]+1=3$ and $\mathrm{Var}(Y)=4\,\mathrm{Var}(X)=4\cdot\frac{4}{12}=\frac43$ (@prp-continuous-uniform-mean-variance).

(b) The total integral must be $1$:
$$\int_1^2\int_0^2\Bigl(cxy+\frac14\Bigr)dy\,dx=c\cdot\frac32\cdot2+\frac14\cdot2=3c+\frac12,$$
so $c=\frac16$. The marginals are $f_X(x)=\int_0^2\bigl(\frac{xy}6+\frac14\bigr)dy=\frac x3+\frac12$ on $[1,2]$ and $f_Y(y)=\int_1^2\bigl(\frac{xy}6+\frac14\bigr)dx=\frac y4+\frac14$ on $[0,2]$. At $(x,y)=(1,0)$, $f_X(1)f_Y(0)=\frac56\cdot\frac14=\frac5{24}\ne\frac14=f(1,0)$, and the same holds on a neighbourhood of this point, so $X$ and $Y$ are not independent.
:::

::: {.solution for="prob-cs70hw-14-q4" status="draft"}
(a) $N(0,1)$ works: its density is positive everywhere. $U[0,1]$ does not: $\Pr(X\in(2,3))=0$.

(b) $F(x+\varepsilon)-F(x)=\Pr(x<X\le x+\varepsilon)\ge\Pr(X\in(x,x+\varepsilon))>0$. Also $0<F(x)<1$ for every $x$ (there is positive probability below and above $x$), $F$ is continuous (it is an integral of a density), and $F(x)\to0$ as $x\to-\infty$, $F(x)\to1$ as $x\to\infty$. A continuous strictly increasing function with these limits takes every value in $(0,1)$ exactly once (intermediate value theorem), so $F:\mathbb R\to(0,1)$ is a bijection and has an inverse.

(c) For every $x$, since $F$ is increasing and bijective, $F^{-1}(U)\le x\iff U\le F(x)$, so $\Pr(F^{-1}(U)\le x)=\Pr(U\le F(x))=F(x)$. Thus $F^{-1}(U)$ has the same CDF as $X$: it has the distribution of $X$.

(d) Yes. If $X$ takes values $x_1<\dots<x_m$ with probabilities $p_1,\dots,p_m$, split $(0,1)$ into consecutive intervals of lengths $p_1,\dots,p_m$ and output $x_i$ when $U$ falls in the $i$-th interval; this happens with probability $p_i$.
:::

::: {.solution for="prob-cs70hw-14-q5" status="draft"}
(a) For $0\le y\le1$, $Y>y$ means all $X_i>y$: $\Pr(Y>y)=(1-y)^n$ by independence, and $\Pr(Y>y)=0$ for $y\ge1$. So $E[Y]=\int_0^1(1-y)^n\,dy=\frac1{n+1}$.

(b) $\Pr(Z\le z)=z^n$ for $0\le z\le1$, so $Z$ has density $nz^{n-1}$ there and $E[Z]=\int_0^1z\cdot nz^{n-1}\,dz=\frac n{n+1}$. (Also $1-Z$ has the distribution of $Y$, since $1-X_i\sim U[0,1]$.)
:::

::: {.solution for="prob-cs70hw-14-q6" status="draft"}
(a) $f_A(x)=1$ for $0\le x\le1$.

(b) For Bob, $\Pr(X\le x)$ is the area of the disk of radius $x$ divided by the area of the board: $\frac{\pi x^2}\pi=x^2$. So $f_B(x)=2x$ on $[0,1]$.

(c) By the law of total probability, $\Pr(X\le x)=px+(1-p)x^2$, so $f(x)=p+2(1-p)x$ on $[0,1]$.

(d) $A$ and $B$ partition the outcomes, so the two conditional probabilities sum to $1$. By Bayes' theorem, for small $dx$,
$$\Pr(A\mid X\in[x,x+dx])\approx\frac{p\cdot1\,dx}{f(x)\,dx},\qquad\Pr(B\mid X\in[x,x+dx])\approx\frac{(1-p)\,2x\,dx}{f(x)\,dx}.$$
Guess $A$ when $p>2(1-p)x$, i.e. when $x<\frac p{2(1-p)}$ (for every $x\in[0,1]$ if $p\ge\frac23$).
:::
