::: {.problem #prob-camii-pms-7-q3 origin="external" source="camii-pms-7-q3"}
Determine which of the following distributions on $\mathbb R$ have an integrable characteristic function: $N(\mu,\sigma^2)$ with $\sigma^2>0$, $\operatorname{Bin}(N,p)$, $\operatorname{Poisson}(\lambda)$, $U[0,1]$.
:::

::: {.problem #prob-camii-pms-7-q8 origin="external" source="camii-pms-7-q8"}
Let $(X_n:n\in\mathbb N)$ be a sequence of random variables in $\mathbb R$ and let $X$ be another such random variable. Show that $X_n\to X$ weakly if and only if $X_n\to X$ in distribution.
:::

::: {.problem #prob-camii-pms-7-q9 origin="external" source="camii-pms-7-q9"}
Let $\mu$ be a Borel probability measure on $\mathbb R^d$ and let $(\mu_n:n\in\mathbb N)$ be a sequence of such measures. Suppose that $\mu_n(f)\to\mu(f)$ for all $C^\infty$ functions on $\mathbb R^d$ of compact support. Show that $\mu_n$ converges weakly to $\mu$ on $\mathbb R^d$.
:::

::: {.problem #prob-camii-pms-8-q1 origin="external" source="camii-pms-8-q1"}
Let $n\ge2$ and let $X=(X_1,\dots,X_n)$ be a Gaussian random variable in $\mathbb R^n$ with mean $\mu$ and covariance matrix $V$. Assume that $V$ is invertible write $V^{-1/2}$ for the positive-definite square root of $V^{-1}$. Set $Y=(Y_1,\dots,Y_n)=V^{-1/2}(X-\mu)$. Show that $Y_1,\dots,Y_n$ are independent $N(0,1)$ random variables. Show further that we can write $X_2$ in the form $X_2=aX_1+Z$ where $Z$ is independent of $X_1$ and determine the distribution of $Z$.
:::

::: {.problem #prob-camii-pms-8-q2 origin="external" source="camii-pms-8-q2"}
Let $X_1,\dots,X_n$ be independent $N(0,1)$ random variables. Show that
$$\Big(\overline X,\ \sum_{m=1}^n(X_m-\overline X)^2\Big)\qquad\text{and}\qquad\Big(\frac{X_n}{\sqrt n},\ \sum_{m=1}^{n-1}X_m^2\Big)$$
have the same distribution, where $\overline X=(X_1+\dots+X_n)/n$.
:::

::: {.problem #prob-camii-pms-10-q2 origin="external" source="camii-pms-10-q2"}
The Cauchy distribution has density function $f(x)=\pi^{-1}(1+x^2)^{-1}$ for $x\in\mathbb R$. Show that the corresponding characteristic function is given by $\varphi(u)=e^{-|u|}$. Show also that, if $X_1,\dots,X_n$ are independent Cauchy random variables, then the random variable $(X_1+\dots+X_n)/n$ is also Cauchy.
:::

::: {.problem #prob-camii-pms-10-q4 origin="external" source="camii-pms-10-q4"}
For each $n\in\mathbb N$, there is a unique probability measure $\mu_n$ on the unit sphere $\mathbb S^{n-1}=\{x\in\mathbb R^n:\ |x|=1\}$ such that $\mu_n(A)=\mu_n(UA)$ for all Borel sets $A$ and all orthogonal $n\times n$ matrices $U$. Fix $k\in\mathbb N$ and, for $n\ge k$, let $\gamma_n$ denote the probability measure on $\mathbb R^k$ which is the law of $\sqrt n(x^1,\dots,x^k)$ under $\mu_n$. Show

(a) if $X\sim N(0,I_n)$ then $X/|X|\sim\mu_n$,

(b) if $(X_n:n\in\mathbb N)$ is a sequence of independent $N(0,1)$ random variables and if $R_n=\sqrt{X_1^2+\dots+X_n^2}$ then $R_n/\sqrt n\to1$ a.s.,

(c) $\gamma_n$ converges weakly to the standard Gaussian distribution on $\mathbb R^k$ as $n\to\infty$.
:::
