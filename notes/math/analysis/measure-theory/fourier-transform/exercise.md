::: {.problem #prob-camii-pms-7-q1 origin="external" source="camii-pms-7-q1"}
Let $u,v\in L^1(\mathbb R^d)$ and define $f:\mathbb R^d\to\mathbb C$ by $f(x)=u(x)+iv(x)$. Set
$$\int_{\mathbb R^d}f(x)\,dx=\int_{\mathbb R^d}u(x)\,dx+i\int_{\mathbb R^d}v(x)\,dx.$$
Show that, for all $y\in\mathbb R^d$, we have
$$\int_{\mathbb R^d}f(x-y)\,dx=\int_{\mathbb R^d}f(x)\,dx=\int_{\mathbb R^d}f(-x)\,dx$$
and show that
$$\Big|\int_{\mathbb R^d}f(x)\,dx\Big|\le\int_{\mathbb R^d}|f(x)|\,dx.$$
:::

::: {.problem #prob-camii-pms-7-q2 origin="external" source="camii-pms-7-q2"}
Show that the Fourier transform of a finite Borel measure on $\mathbb R^d$ is a bounded continuous function.
:::

::: {.problem #prob-camii-pms-7-q4 origin="external" source="camii-pms-7-q4"}
For a finite Borel measure $\mu$ on the line show that, if $\int|x|^k\,d\mu(x)<\infty$, then the Fourier transform $\hat\mu$ of $\mu$ has a $k$th continuous derivative, which at $0$ is given by
$$\hat\mu^{(k)}(0)=i^k\int x^k\,d\mu(x).$$
:::

::: {.problem #prob-camii-pms-7-q5 origin="external" source="camii-pms-7-q5"}
Define a function $\psi$ on $\mathbb R$ by setting $\psi(x)=C\exp\{-(1-x^2)^{-1}\}$ for $|x|<1$ and $\psi(x)=0$ otherwise, where $C$ is a constant chosen so that $\int_{\mathbb R}\psi(x)\,dx=1$. For $f\in L^1(\mathbb R)$ of compact support, show that $f*\psi$ is $C^\infty$ and of compact support.
:::
