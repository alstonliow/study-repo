<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-3-q2" status="draft"}
(a) Integrating the joint density $\lambda e^{-\lambda x}\mu e^{-\mu y}$ over $x<y$:
$$P(X<Y)=\int_0^\infty\lambda e^{-\lambda x}e^{-\mu x}\,dx=\frac{\lambda}{\lambda+\mu}.$$

(b) $P(\min_kX_k>t)=\prod_kP(X_k>t)=e^{-(\sum_j\lambda_j)t}$, the tail of an $\text{Exponential}(\sum_j\lambda_j)$ variable.

(c) Let $Y=\min_{k\ne i}X_k$, which is $\text{Exponential}(\sum_{j\ne i}\lambda_j)$ by (b) and independent of $X_i$. Ties have probability $0$, so by (a) $P(X_i=\min_kX_k)=P(X_i<Y)=\lambda_i/\sum_j\lambda_j$. (This is @prp-min-of-exponentials.)
:::

::: {.solution for="prob-eecs126hw-3-q1" status="draft"}
The density is $A$ on $[1,2]\times[1,3]$ and on $[3,4]\times[1,3]$, $2A$ on $[2,3]\times[2,3]$, and $0$ elsewhere.

(a) Total mass $2A+2A+2A=6A=1$, so $A=\frac16$.

- $f_X$: integrating over $y$, each of the three columns gets $\frac13$, so $f_X=\frac13$ on $[1,4]$: $X$ is uniform.
- $f_Y$: for $1<y<2$ only the two outer columns contribute, $f_Y=2A=\frac13$; for $2<y<3$, $f_Y=A+2A+A=\frac23$.
- $\{X+Y\le3\}$ meets the support only in the triangle $1\le x\le2$, $1\le y\le3-x$, of area $\frac12$ and probability $\frac1{12}$. Given that event $(X,Y)$ is uniform on the triangle, so $f_{X\mid X+Y\le3}(x)=2(2-x)$ for $1\le x\le2$, a decreasing ramp.

(b) For $1<y<2$, $X$ is uniform on $[1,2]\cup[3,4]$; for $2<y<3$ the conditional density of $X$ is $1:2:1$ on the three columns. Both are symmetric about $2.5$, so $E[X\mid Y=y]=2.5$. Given $X=x$ in an outer column, $Y$ is uniform on $[1,3]$ and $E[Y\mid X=x]=2$; for $2<x<3$, $Y$ is uniform on $[2,3]$ and $E[Y\mid X=x]=2.5$.

(c) $E[X\mid Y]=2.5=E[X]$ is constant, so $E[XY]=E\bigl[Y\,E[X\mid Y]\bigr]=2.5\,E[Y]=E[X]E[Y]$ and $\operatorname{cov}(X,Y)=0$, although $X$ and $Y$ are not independent (@def-marginal-conditional-density).
:::

::: {.solution for="prob-mit6041f10-5-q1" status="draft"}
(a) $\int_1^2\int_x^2ax\,dy\,dx=a\int_1^2x(2-x)\,dx=a\bigl[x^2-\tfrac{x^3}3\bigr]_1^2=\tfrac{2a}3$, so $a=\frac32$.

(b) For $1\le y\le2$, $f_Y(y)=\int_1^y\frac32x\,dx=\frac34(y^2-1)$, and $0$ otherwise.

(c) Given $Y=\frac32$, $f_{X\mid Y}(x\mid\frac32)\propto x$ on $[1,\frac32]$. So
$$E\Bigl[\frac1X\Bigm|Y=\tfrac32\Bigr]=\frac{\int_1^{3/2}\frac1x\cdot x\,dx}{\int_1^{3/2}x\,dx}=\frac{1/2}{5/8}=\frac45.$$
:::

::: {.solution for="prob-mit6041f10-5-q5" status="draft"}
The quadrilateral is the parallelogram $\{0\le x\le1,\ x\le y\le x+1\}$ of area $1$, so $f_{X,Y}=1$ there.

(a) No. The support is not a product set: for example $f_X(0.9)f_Y(0.1)>0$ but $f_{X,Y}(0.9,0.1)=0$.

(b) For $0\le x\le1$ the vertical section has length $1$, so $X$ is uniform on $[0,1]$. For $0\le y\le1$ the horizontal section is $0\le x\le y$, so $f_Y(y)=y$; for $1\le y\le2$ it is $y-1\le x\le1$, so $f_Y(y)=2-y$.

(c) Given $X=x$, $Y$ is uniform on $[x,x+1]$, so $Y=X+U$ with $U$ uniform on $[0,1]$ and independent of $X$. Then $X+Y=2X+U$ and $E[X+Y]=1+\frac12=\frac32$.

(d) $\mathrm{Var}(2X+U)=4\cdot\frac1{12}+\frac1{12}=\frac5{12}$.
:::

::: {.solution for="prob-mit1805s22-5-q1" status="draft"}
(a) $\int_0^1\int_0^1(x^2+xy)\,dy\,dx=\frac13+\frac14=\frac7{12}$, so $c=\frac{12}7$. For $(x,y)\in[0,1]^2$,
$$F(x,y)=\frac{12}7\int_0^x\int_0^y(u^2+uv)\,dv\,du=\frac{12}7\Bigl(\frac{x^3y}3+\frac{x^2y^2}4\Bigr)=\frac{4x^3y+3x^2y^2}7 .$$

(b) $F_X(x)=F(x,1)=\frac{4x^3+3x^2}7$ and $F_Y(y)=F(1,y)=\frac{4y+3y^2}7$ on $[0,1]$; differentiating, $f_X(x)=\frac{12x^2+6x}7$ and $f_Y(y)=\frac{4+6y}7$.

(c) $E[X]=\int_0^1\frac{12x^3+6x^2}7dx=\frac57$, $E[X^2]=\int_0^1\frac{12x^4+6x^3}7dx=\frac{39}{70}$, so $\mathrm{Var}(X)=\frac{39}{70}-\frac{25}{49}=\frac{23}{490}\approx0.0469$.

(d) $E[Y]=\frac47$, $E[Y^2]=\frac{17}{42}$, $\mathrm{Var}(Y)=\frac{23}{294}$, and $E[XY]=\frac{12}7\int_0^1\int_0^1(x^3y+x^2y^2)\,dy\,dx=\frac{12}7\bigl(\frac18+\frac19\bigr)=\frac{17}{42}$. So
$$\mathrm{Cov}(X,Y)=\frac{17}{42}-\frac{20}{49}=-\frac1{294}\approx-0.0034,\qquad\mathrm{Cor}(X,Y)=\frac{-1/294}{\sqrt{\frac{23}{490}\cdot\frac{23}{294}}}\approx-0.056 .$$

(e) No: the covariance is not $0$ (equivalently, $f(x,y)\ne f_X(x)f_Y(y)$, e.g. at $(1,0)$: $\frac{12}7\ne\frac{18}7\cdot\frac47$).
:::

::: {.solution for="prob-mit1805s22-5-q4" status="draft"}
(a) $f(a,b)=\frac1{3600}$ on $[0,60]^2$ and $0$ elsewhere; for $(a,b)$ in the square, $F(a,b)=\frac{ab}{3600}$ (and $F$ is $0$, $\frac a{60}$, $\frac b{60}$ or $1$ outside it, by clamping $a$ and $b$ to $[0,60]$).

(b) $P(A<30)=\frac{30}{60}=\frac12$.

(c) (i) $P(A<15)P(30<B<45)=\frac14\cdot\frac14=\frac1{16}$. (ii) The event is the rectangle $[0,15]\times[30,45]$ of area $225$, and $\frac{225}{3600}=\frac1{16}$.

(d) Read as "$A\le B+5$" (arriving before Bernardo also counts): the complement is the triangle $a>b+5$ with legs $55$, area $\frac{55^2}2=1512.5$, so the probability is $1-\frac{1512.5}{3600}\approx0.580$. (If only $0<A-B<5$ is meant, the region is a strip of area $\frac{60^2-55^2}2=287.5$, probability $\approx0.080$.)

(e) They meet when $|A-B|\le15$. The complement is two triangles with legs $45$, total area $45^2=2025$, so the probability is $1-\frac{2025}{3600}=\frac7{16}=0.4375$.
:::
