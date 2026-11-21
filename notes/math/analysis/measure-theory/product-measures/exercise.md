::: {.problem #prob-camii-pms-3-q11 origin="external" source="camii-pms-3-q11"}
Let $X_1,\dots,X_n$ be random variables with density functions $f_1,\dots,f_n$ respectively. Suppose that the $\mathbb R^n$-valued random variable $X=(X_1,\dots,X_n)$ also has a density function $f$. Show that $X_1,\dots,X_n$ are independent if and only if
$$f(x_1,\dots,x_n)=f_1(x_1)\dots f_n(x_n)\quad\text{a.e.}$$
:::

::: {.problem #prob-camii-pms-3-q12 origin="external" source="camii-pms-3-q12"}
Show that, for all non-negative measurable functions $f$ on $[0,\infty)$, the function $(x,y)\mapsto f(|(x,y)|)$ is measurable on $\mathbb R^2$ and (without using the Jacobian formula)
$$\int_{\mathbb R^2}f(|(x,y)|)\,dx\,dy=2\pi\int_0^\infty rf(r)\,dr.$$
Hence show that $(2\pi)^{-1/2}e^{-x^2/2}$ is a probability density function.
:::

::: {.problem #prob-camii-pms-3-q13 origin="external" source="camii-pms-3-q13"}
Let $\mu$ and $\nu$ be probability measures on $(E,\mathcal E)$ and let $f:E\to[0,R]$ be a measurable function. Suppose that $\nu(A)=\mu(f\mathbf 1_A)$ for all $A\in\mathcal E$. Let $(X_n:n\in\mathbb N)$ be a sequence of independent random variables in $E$ with law $\mu$ and let $(U_n:n\in\mathbb N)$ be a sequence of independent $U[0,1]$ random variables. Assume also that the two sequences $(X_n)$ and $(U_n)$ are independent of each other. Set
$$T=\min\{n\in\mathbb N:\ RU_n\le f(X_n)\},\qquad Y=X_T.$$
Show that $Y$ has law $\nu$. (This justifies simulation by rejection sampling.)
:::
