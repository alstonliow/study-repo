<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-2-q3" status="draft"}
1. Let $\mathcal P_X=\{\{X\le x\}:\ x\in\mathbb R\}\cup\{\emptyset,\Omega\}$ and similarly $\mathcal P_Y$. They are π-systems ($\{X\le x\}\cap\{X\le x'\}=\{X\le\min(x,x')\}$) containing $\Omega$.

2. $\sigma(\mathcal P_X)=\sigma(X)$: $\sigma(X)=\{X^{-1}(B):B\in\mathcal B\}$, and the half-lines $(-\infty,x]$ generate $\mathcal B$ (@prp-measurable-closure, @lem-measurable-generator); preimages commute with the σ-algebra operations.

3. The product formula holds on $\mathcal P_X\times\mathcal P_Y$: for half-lines by hypothesis, trivially if a set is $\emptyset$, and if, say, the first set is $\Omega$, let $x\to\infty$ in the hypothesis and use continuity from below: $\Pr(Y\le y)=\lim_x\Pr(X\le x,Y\le y)=\lim_x\Pr(X\le x)\Pr(Y\le y)$.

4. By @thm-independence-pi-systems, $\sigma(X)$ and $\sigma(Y)$ are independent.
:::

::: {.solution for="prob-camii-pms-2-q7" status="draft"}
1. *(a)* $C_n$ is a union of $2^n$ disjoint closed intervals of length $3^{-n}$, so $\lambda(C)\le\lambda(C_n)=(2/3)^n\to0$. The points $\sum_k2a_k3^{-k}$ with $a_k\in\{0,1\}$ lie in $C$ (at stage $n$ the $n$th digit chooses the left or right third), and distinct sequences give distinct points (ternary expansions with digits in $\{0,2\}$ are unique). So $C$ is in bijection with a superset of $\{0,1\}^{\mathbb N}$, which is uncountable.

2. *Recursion.* $C_{n+1}=\frac13C_n\cup\big(\frac23+\frac13C_n\big)$, a disjoint union of two copies each carrying half of the uniform distribution. Hence, for $x\in[0,1]$,
$$F_{n+1}(x)=\begin{cases}\frac12F_n(3x),&x\le\frac13,\\ \frac12,&\frac13\le x\le\frac23,\\ \frac12+\frac12F_n(3x-2),&x\ge\frac23,\end{cases}$$
with $F_0(x)=x$.

3. *(b)* Let $d_n=\sup_{[0,1]}|F_{n+1}-F_n|$. Subtracting the recursions for $n$ and $n-1$, the middle pieces cancel and the outer ones give $d_n\le\frac12d_{n-1}$. A direct check gives $d_0=\sup|F_1(x)-x|=\frac16$ (attained at $x=\frac13,\frac23$). So $d_n\le\frac16 2^{-n}$, $\sum_nd_n<\infty$, and $F_n$ converges uniformly on $[0,1]$.

4. *(c)* Each $F_n$ is continuous on $[0,1]$ (uniform distribution on a finite union of intervals), with $F_n(0)=0$, $F_n(1)=1$; a uniform limit of continuous functions is continuous.

5. *(d)* An open interval $J$ removed at stage $m$ is disjoint from $C_n$ for all $n\ge m$, so each $F_n$ ($n\ge m$) is constant on $J$, and so is $F$. Hence $F'=0$ on $[0,1]\setminus C$, which has full measure by (a).
:::

::: {.solution for="prob-camii-pms-4-q4" status="draft"}
1. By @prp-independence-product-law the law of $(X,Y)$ is $\mu_X\otimes\mu_Y$. By the image-measure formula and Tonelli,
$$E|XY|=\int\!\!\int|x||y|\,\mu_X(dx)\mu_Y(dy)=\int|x|\mu_X(dx)\int|y|\mu_Y(dy)=E|X|\,E|Y|,$$
valid in $[0,\infty]$ with $0\cdot\infty=0$.

2. If $X,Y$ are integrable, step 1 shows $XY$ is integrable, i.e. $(x,y)\mapsto xy$ is $\mu_X\otimes\mu_Y$-integrable. Fubini then gives $E[XY]=\int\!\!\int xy\,\mu_X(dx)\mu_Y(dy)=E[X]E[Y]$.
:::
