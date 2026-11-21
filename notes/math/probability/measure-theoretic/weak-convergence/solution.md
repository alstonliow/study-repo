<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-7-q3" status="draft"}
1. *Normal: integrable.* $\varphi(u)=e^{i\mu u-\sigma^2u^2/2}$ (@prp-gaussian-vector-characteristic-function with $n=1$), so $|\varphi(u)|=e^{-\sigma^2u^2/2}$, integrable.

2. *The others: not integrable.* If $\varphi_X$ were integrable, then by @thm-characteristic-function-uniqueness $X$ would have a bounded *continuous* density $f$.

3. A binomial or Poisson variable takes countably many values, so $\Pr(X=k)>0$ for some integer $k$; but a variable with a density has $\Pr(X=k)=\int_{\{k\}}f=0$. Contradiction.

4. For $U[0,1]$, $f$ would agree a.e. with $\mathbf 1_{[0,1]}$. A continuous function equal to $1$ a.e. on $(0,1)$ equals $1$ on $(0,1)$, and equal to $0$ a.e. on $(-1,0)$ equals $0$ there; then it cannot be continuous at $0$. Contradiction. (Directly: $|\varphi(u)|=\big|\frac{2\sin(u/2)}u\big|$, not integrable as in problem 3.6.)
:::

::: {.solution for="prob-camii-pms-7-q8" status="draft"}
1. *(⇒)* Let $x$ be a continuity point of $F_X$ and $k\ge1$. Take continuous $h$ with $\mathbf 1_{(-\infty,x]}\le h\le\mathbf 1_{(-\infty,x+1/k]}$. Then $\limsup_nF_{X_n}(x)\le\lim_nE[h(X_n)]=E[h(X)]\le F_X(x+\frac1k)$. With $h$ between $\mathbf 1_{(-\infty,x-1/k]}$ and $\mathbf 1_{(-\infty,x]}$, $\liminf_nF_{X_n}(x)\ge F_X(x-\frac1k)$. Let $k\to\infty$; by continuity at $x$ both bounds tend to $F_X(x)$.

2. *(⇐)* By the Skorokhod representation (@thm-skorokhod-representation) there are $\tilde X_n\to\tilde X$ a.s. with the same laws. For bounded continuous $g$, $g(\tilde X_n)\to g(\tilde X)$ a.s., so by bounded convergence $E[g(X_n)]=E[g(\tilde X_n)]\to E[g(\tilde X)]=E[g(X)]$.
:::

::: {.solution for="prob-camii-pms-7-q9" status="draft"}
1. *Mollifier.* Let $\psi(x)=C\exp(-(1-|x|^2)^{-1})$ for $|x|<1$, $0$ otherwise, normalised to integral $1$; as in problem 7.5 it is $C^\infty$ with support in the unit ball. Let $\psi_\delta(x)=\delta^{-d}\psi(x/\delta)$. For $g$ continuous of compact support, $g*\psi_\delta$ is $C^\infty$ of compact support (differentiate under the integral) and $\|g*\psi_\delta-g\|_\infty\le\sup_{|y|\le\delta}\sup_x|g(x-y)-g(x)|\to0$ by uniform continuity.

2. *Continuous $g$ of compact support.* $|\mu_n(g)-\mu(g)|\le2\|g-g*\psi_\delta\|_\infty+|\mu_n(g*\psi_\delta)-\mu(g*\psi_\delta)|$. Let $n\to\infty$, then $\delta\to0$: $\mu_n(g)\to\mu(g)$.

3. *All bounded continuous $g$.* Repeat steps 4 and 5 of the proof of @thm-levy-continuity, which use only convergence for continuous functions of compact support: choose $R$ with $\mu(\{|x|>R\})\le\varepsilon$ and continuous $\chi$ with $\mathbf 1_{\{|x|\le R\}}\le\chi\le\mathbf 1_{\{|x|\le R+1\}}$; then $\mu_n(1-\chi)\le2\varepsilon$ for large $n$, and splitting $g=g\chi+g(1-\chi)$ gives $\limsup_n|\mu_n(g)-\mu(g)|\le4\varepsilon\|g\|_\infty$.
:::

::: {.solution for="prob-camii-pms-8-q1" status="draft"}
1. $Y$ is an affine image of $X$: each $\langle u,Y\rangle=\langle V^{-1/2}u,X\rangle-\langle u,V^{-1/2}\mu\rangle$ is normal, so $Y$ is Gaussian, with mean $0$ and covariance $V^{-1/2}VV^{-1/2}=I$ ($V^{-1/2}$ is symmetric and commutes with $V$).

2. By @prp-gaussian-vector-characteristic-function, $\varphi_Y(u)=e^{-|u|^2/2}=\prod_je^{-u_j^2/2}$, the characteristic function of independent $N(0,1)$ coordinates; by uniqueness the $Y_j$ are independent $N(0,1)$.

3. $V_{11}=\operatorname{Var}X_1>0$ ($V$ is positive definite). Let $a=V_{12}/V_{11}$ and $Z=X_2-aX_1$. Then $(X_1,Z)$ is a linear image of $X$, hence Gaussian, and $\operatorname{Cov}(X_1,Z)=V_{12}-aV_{11}=0$. By @prp-gaussian-vector-characteristic-function, $Z$ is independent of $X_1$.

4. $Z$ is normal with mean $\mu_2-a\mu_1$ and variance $V_{22}-2aV_{12}+a^2V_{11}=V_{22}-V_{12}^2/V_{11}$: $Z\sim N\big(\mu_2-\frac{V_{12}}{V_{11}}\mu_1,\ V_{22}-\frac{V_{12}^2}{V_{11}}\big)$.
:::

::: {.solution for="prob-camii-pms-8-q2" status="draft"}
1. Let $A$ be an orthogonal $n\times n$ matrix whose last row is $(\frac1{\sqrt n},\dots,\frac1{\sqrt n})$ (complete this unit vector to an orthonormal basis). Put $Y=AX$.

2. $Y$ is Gaussian with mean $0$ and covariance $AA^{\mathsf T}=I$, so (as in problem 8.1) $Y$ has the same law as $X$: independent $N(0,1)$ coordinates.

3. $Y_n=\frac1{\sqrt n}\sum_mX_m=\sqrt n\,\overline X$, and $\sum_mY_m^2=|AX|^2=|X|^2=\sum_mX_m^2$. Hence
$$\sum_{m=1}^{n-1}Y_m^2=\sum_mX_m^2-n\overline X^2=\sum_m(X_m-\overline X)^2 .$$

4. So $\big(\overline X,\sum_m(X_m-\overline X)^2\big)=\big(\frac{Y_n}{\sqrt n},\sum_{m<n}Y_m^2\big)=\Phi(Y)$ for the Borel map $\Phi(y)=(y_n/\sqrt n,\sum_{m<n}y_m^2)$. Since $Y$ and $X$ have the same law, $\Phi(Y)$ and $\Phi(X)$ do too, and $\Phi(X)$ is the second pair.
:::

::: {.solution for="prob-camii-pms-10-q2" status="draft"}
1. Let $g(x)=e^{-|x|}$. Then $\hat g(u)=\int_0^\infty e^{-x}(e^{iux}+e^{-iux})dx=\frac1{1-iu}+\frac1{1+iu}=\frac2{1+u^2}$, which is integrable.

2. By the inversion formula (@thm-fourier-inversion; both sides are continuous, so the identity holds everywhere), $e^{-|x|}=\frac1{2\pi}\int\frac2{1+u^2}e^{-iux}du=\int\frac{e^{-iux}}{\pi(1+u^2)}du$.

3. Rename the variables and replace $x$ by $-u$: $\varphi(u)=\int\frac{e^{iux}}{\pi(1+x^2)}dx=e^{-|u|}$.

4. For independent Cauchy $X_1,\dots,X_n$ and $S_n=X_1+\dots+X_n$, $\varphi_{S_n/n}(u)=\varphi(u/n)^n=e^{-|u|}$ (@prp-convolution-properties). By @thm-characteristic-function-uniqueness, $S_n/n$ is Cauchy.
:::

::: {.solution for="prob-camii-pms-10-q4" status="draft"}
1. *(a)* $X\neq0$ a.s., so $X/|X|$ is an a.s. defined random point of $\mathbb S^{n-1}$; let $\rho$ be its law. For orthogonal $U$, $UX$ is Gaussian with mean $0$ and covariance $UU^{\mathsf T}=I$, so $UX$ has the law of $X$ (@prp-gaussian-vector-characteristic-function), and $|UX|=|X|$. Hence $\rho(UA)=\Pr(X/|X|\in UA)=\Pr(U^{\mathsf T}X/|U^{\mathsf T}X|\in A)=\rho(A)$. By the uniqueness stated, $\rho=\mu_n$.

2. *(b)* The $X_m^2$ are i.i.d. with mean $1$, so $R_n^2/n\to1$ a.s. by the strong law (@thm-strong-law-of-large-numbers), and $R_n/\sqrt n\to1$ by continuity of the square root.

3. *(c)* Use the single sequence of (b). By (a), $(X_1,\dots,X_n)/R_n\sim\mu_n$, so $\gamma_n$ is the law of $W_n=\frac{\sqrt n}{R_n}(X_1,\dots,X_k)$.

4. By (b), $W_n\to(X_1,\dots,X_k)$ a.s. For bounded continuous $g$ on $\mathbb R^k$, bounded convergence gives $\gamma_n(g)=E[g(W_n)]\to E[g(X_1,\dots,X_k)]$, the integral of $g$ against the standard Gaussian on $\mathbb R^k$. That is weak convergence.
:::
