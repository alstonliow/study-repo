<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-13-q1" status="draft"}
(a) 1. $\mathcal H$ is a vector space: $(X+Y)^2\le2X^2+2Y^2$, so sums (and scalar multiples) stay in $\mathcal H$.
2. $\langle X,Y\rangle$ is finite since $|XY|\le\frac12(X^2+Y^2)$.
3. It is symmetric, and linear in each argument by linearity of expectation.
4. $\langle X,X\rangle=E[X^2]\ge0$, and $E[X^2]=0$ forces $X=0$ almost surely, i.e. $X=0$ in $\mathcal H$ under the identification of the footnote.

(b) $Py$ is the unique $u\in U$ with $y-u\perp U$ (@thm-projection-random-variables; uniqueness: if $u,u'$ both work, $u-u'\in U$ is orthogonal to itself, so it is $0$). For $y_1,y_2\in V$ and a scalar $a$, the vector $aPy_1+Py_2$ lies in $U$, and
$$(ay_1+y_2)-(aPy_1+Py_2)=a(y_1-Py_1)+(y_2-Py_2)\perp U.$$
By uniqueness $P(ay_1+y_2)=aPy_1+Py_2$.

(c) Let $u=\sum_i\langle y,v_i\rangle v_i\in U$. By orthonormality $\langle y-u,v_j\rangle=\langle y,v_j\rangle-\langle y,v_j\rangle=0$ for every $j$, so $y-u\perp U$ and $u=Py$ by uniqueness.
:::

::: {.solution for="prob-eecs126hw-13-q2" status="draft"}
$f(x\mid\theta)=\frac1\theta$ for $0\le x\le\theta$.

(a) The likelihood $\frac1\theta$ on $\theta\ge x$ is largest at $\theta=x$: the MLE is $X$. The posterior is $\propto\frac1{100}\cdot\frac1\theta$ on $[x,100]$, also decreasing, so the MAP is also $X$.

(b) $E[\Theta]=50$, $\operatorname{Var}\Theta=\frac{2500}3$, $E[X\mid\Theta]=\Theta/2$ so $E[X]=25$ and $\operatorname{Cov}(\Theta,X)=\operatorname{Cov}(\Theta,\Theta/2)=\frac{1250}3$. By the law of total variance,
$$\operatorname{Var}X=E\Bigl[\frac{\Theta^2}{12}\Bigr]+\operatorname{Var}\frac\Theta2=\frac{10000/3}{12}+\frac{2500/3}{4}=\frac{4375}9.$$
By @thm-llse,
$$L[\Theta\mid X]=50+\frac{1250/3}{4375/9}(X-25)=50+\frac67(X-25)=\frac{6X+200}{7}.$$
:::

::: {.solution for="prob-eecs126hw-13-q4" status="draft"}
$T=B\Theta$ with $B\sim\text{Bernoulli}(p)$ independent of $\Theta$, and $D=T+N$.

1. $E[T]=p\lambda$, $E[T^2]=pE[\Theta^2]=p(\lambda+\lambda^2)$, so $\operatorname{Var}T=p\lambda+p(1-p)\lambda^2$.
2. $N$ is independent of $T$: $\operatorname{Cov}(T,D)=\operatorname{Var}T$, $\operatorname{Var}D=\operatorname{Var}T+\mu$, $E[D]=p\lambda+\mu$.
3. By @thm-llse,
$$L[T\mid D]=p\lambda+\frac{p\lambda+p(1-p)\lambda^2}{p\lambda+p(1-p)\lambda^2+\mu}\bigl(D-p\lambda-\mu\bigr).$$
:::

::: {.solution for="prob-eecs126hw-14-q1" status="draft"}
(a) Given $X=x$, the other $n-x$ balls fall uniformly into the other $m-1$ bins, so $E[Y\mid X]=\frac{n-X}{m-1}$.

(b) Both are $\frac{n-X}{m-1}$. The MMSE $E[Y\mid X]$ is the best estimator of any form (@thm-mmse-conditional-expectation), and here it is linear, hence also quadratic; so it is the best in those smaller classes too.

(c) $X\sim\text{Bin}(n,\frac1m)$, so $E[X]=E[Y]=\frac nm$.

(d) $\operatorname{var}(X)=\frac nm\bigl(1-\frac1m\bigr)=\frac{n(m-1)}{m^2}$.

(e) With indicators $X=\sum_iA_i$, $Y=\sum_iB_i$ for ball $i$ landing in bin 1 or 2: $\operatorname{cov}(A_i,B_j)=0$ for $i\ne j$ and $\operatorname{cov}(A_i,B_i)=0-\frac1{m^2}$. So $\operatorname{cov}(X,Y)=-\frac n{m^2}$.

(f) $L[Y\mid X]=\frac nm+\frac{-n/m^2}{n(m-1)/m^2}\bigl(X-\frac nm\bigr)=\frac nm-\frac{X-n/m}{m-1}=\frac{n-X}{m-1}$, as in (b).
:::

::: {.solution for="prob-eecs126hw-14-q2" status="draft"}
(a) Write $g(Y)=E[X\mid Y]-\phi(Y)$. Then
$$E[(X-\phi(Y))^2]=E[(X-E[X\mid Y])^2]+E[g(Y)^2]+2E[(X-E[X\mid Y])g(Y)].$$
By the tower property, the cross term is $2E\bigl[g(Y)\,E[X-E[X\mid Y]\mid Y]\bigr]=0$. So the error is $E[(X-E[X\mid Y])^2]+E[g(Y)^2]$, minimised exactly when $g(Y)=0$, i.e. $\phi(Y)=E[X\mid Y]$ (almost surely).

(b) The same argument with $Y=(Y_1,\dots,Y_n)$ shows that $E[X\mid Y_1,\dots,Y_n]$ beats every function of $(Y_1,\dots,Y_n)$. The average $\frac1n\sum_iE[X\mid Y_i]$ is one such function.
:::

::: {.solution for="prob-eecs126hw-14-q3" status="draft"}
Both are $1+p\lambda T$.

1. $P(N=n)=p^{n-1}(1-p)$ for $n\ge1$, and given $N=n$, $T$ has the Erlang density $\lambda^nt^{n-1}e^{-\lambda t}/(n-1)!$ (@thm-poisson-process-counts).
2. The joint weight is $(1-p)\lambda e^{-\lambda t}\frac{(p\lambda t)^{n-1}}{(n-1)!}$. Summing over $n$ gives $f_T(t)=(1-p)\lambda e^{-(1-p)\lambda t}$, and dividing,
$$P(N=n\mid T=t)=e^{-p\lambda t}\frac{(p\lambda t)^{n-1}}{(n-1)!}:$$
given $T=t$, $N-1\sim\text{Poisson}(p\lambda t)$.
3. So $E[N\mid T]=1+p\lambda T$. It is linear in $T$, so it is also the LLSE.
:::
