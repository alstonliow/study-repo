::: {.problem #prob-camii-pms-9-q1 origin="external" source="camii-pms-9-q1"}
Let $(E,\mathcal E,\mu)$ be a measure space and $\tau:E\to E$ a measure-preserving transformation. Show that $\mathcal E_\tau:=\{A\in\mathcal E:\ \tau^{-1}(A)=A\}$ is a σ-algebra, and that a measurable function $f$ is $\mathcal E_\tau$-measurable if and only if it is *invariant*, that is $f\circ\tau=f$.
:::

::: {.problem #prob-camii-pms-9-q2 origin="external" source="camii-pms-9-q2"}
Show that, if $\theta$ is an ergodic measure-preserving transformation and $f$ is a measurable real-valued $\theta$-invariant function, then there exists a constant $c\in\mathbb R$ such that $f=c$ a.e.
:::

::: {.problem #prob-camii-pms-9-q3 origin="external" source="camii-pms-9-q3"}
For $x\in[0,1)$, set $\tau(x)=2x\bmod1$. Show that $\tau$ is a measure-preserving transformation of $([0,1),\mathcal B([0,1)),dx)$, and that $\tau$ is ergodic. Identify the invariant function $\overline f$ corresponding to each integrable function $f$.
:::

::: {.problem #prob-camii-pms-9-q4 origin="external" source="camii-pms-9-q4"}
Fix $a\in[0,1)$ and define, for $x\in[0,1)$, $\tau(x)=x+a\bmod1$. Show that $\tau$ is also a measure-preserving transformation of $([0,1),\mathcal B([0,1)),dx)$. Determine for which values of $a$ the transformation $\tau$ is ergodic. Hint: you may use the fact that any integrable function $f$ on $[0,1)$ whose Fourier coefficients all vanish must itself vanish a.e.. Identify, for all values of $a$, the invariant function $\overline f$ corresponding to an integrable function $f$.
:::

::: {.problem #prob-camii-pms-9-q5 origin="external" source="camii-pms-9-q5"}
Call a sequence of random variables $(X_n:n\in\mathbb N)$ on a probability space $(\Omega,\mathcal F,\mathbb P)$ *stationary* if for each $n,k\in\mathbb N$ the random vectors $(X_1,\dots,X_n)$ and $(X_{k+1},\dots,X_{k+n})$ have the same distribution: for $A_1,\dots,A_n\in\mathcal B$,
$$\mathbb P(X_1\in A_1,\dots,X_n\in A_n)=\mathbb P(X_{k+1}\in A_1,\dots,X_{k+n}\in A_n).$$
Show that, if $(X_n:n\in\mathbb N)$ is a stationary sequence and $X_1\in L^p$, for some $p\in[1,\infty)$, then
$$\frac1n\sum_{i=1}^nX_i\to X\qquad\text{a.s. and in }L^p,$$
for some random variable $X\in L^p$ and find $\mathbb E(X)$.
:::
