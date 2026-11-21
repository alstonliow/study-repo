::: {.problem #prob-camii-pms-3-q4 origin="external" source="camii-pms-3-q4"}
Let $X$ be a non-negative integer-valued random variable. Show that
$$\mathbb E(X)=\sum_{n=1}^\infty\mathbb P(X\ge n).$$
Deduce that, if $\mathbb E(X)=\infty$ and $X_1,X_2,\dots$ is a sequence of independent random variables with the same distribution as $X$, then, almost surely, $\limsup_n(X_n/n)\ge1$, and moreover $\limsup_n(X_n/n)=\infty$. Now suppose that $Y_1,Y_2,\dots$ is any sequence of independent identically distributed random variables with $\mathbb E|Y_1|=\infty$. Show that, almost surely, $\limsup_n(|Y_n|/n)=\infty$, and moreover $\limsup_n(|Y_1+\dots+Y_n|/n)=\infty$.
:::

::: {.problem #prob-camii-pms-10-q1 origin="external" source="camii-pms-10-q1"}
Let $(X_n:n\in\mathbb N)$ be a sequence of independent random variables, such that $\mathbb E(X_n)=\mu$ and $\mathbb E(X_n^4)\le M$ for all $n$, for some constants $\mu\in\mathbb R$ and $M<\infty$. Set $P_n=X_1X_2+X_2X_3+\dots+X_{n-1}X_n$. Show that $P_n/n$ converges a.s. as $n\to\infty$ and identify the limit.
:::

::: {.problem #prob-camii-pms-10-q3 origin="external" source="camii-pms-10-q3"}
Let $f$ be a bounded continuous function on $(0,\infty)$, having Laplace transform
$$\hat f(\lambda)=\int_0^\infty e^{-\lambda x}f(x)\,dx,\qquad\lambda\in(0,\infty).$$
Let $(X_n:n\in\mathbb N)$ be a sequence of independent exponential random variables, of parameter $\lambda$. Show that $\hat f$ has derivatives of all orders on $(0,\infty)$ and that, for all $n\in\mathbb N$, for some $C(\lambda,n)\neq0$ independent of $f$, we have
$$\Big(\frac{d}{d\lambda}\Big)^{n-1}\hat f(\lambda)=C(\lambda,n)\,\mathbb E\big(f(S_n)\big)$$
where $S_n=X_1+\dots+X_n$. Deduce that if $\hat f\equiv0$ then also $f\equiv0$.
:::
