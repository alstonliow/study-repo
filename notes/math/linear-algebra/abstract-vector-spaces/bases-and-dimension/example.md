<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 1.2, restated in our own words with our own checks. -->

::: {#exm-span-dependence-r3 .example name="Span and dependence of three vectors"}

In $\mathbb R^3$ let $S=\{s_1,s_2,s_3\}$ with $s_1=(1,0,0)^{\mathsf T}$, $s_2=(0,1,1)^{\mathsf T}$, $s_3=(1,2,2)^{\mathsf T}$.

1. Every vector of $S$ has equal second and third entries, so $\langle S\rangle\subseteq\{(a,b,b)^{\mathsf T}:a,b\in\mathbb R\}$; conversely $(a,b,b)^{\mathsf T}=as_1+bs_2$. So $\langle S\rangle=\{(a,b,b)^{\mathsf T}\}$.

2. $s_1+2s_2-s_3=0$, so $S$ is linearly dependent.

3. $(0,0,1)^{\mathsf T}\notin\langle S\rangle$, so $S$ does not span $\mathbb R^3$.

4. Any two of the three vectors are independent and span the same plane, so each pair is a basis of $\langle S\rangle$ and $\dim\langle S\rangle=2$.

:::

::: {#exm-delta-functions-span .example name="Indicator functions span the finitely supported functions"}

For $x\in X$ let $\delta_x\in F^X$ be $1$ at $x$ and $0$ elsewhere. A linear combination $\sum_{i=1}^k\lambda_i\delta_{x_i}$ has support inside $\{x_1,\dots,x_k\}$; conversely a function $f$ with finite support $\{x_1,\dots,x_k\}$ equals $\sum_if(x_i)\delta_{x_i}$. So $\langle\delta_x:x\in X\rangle$ is exactly the space of functions with finite support (@exm-finite-support-subspace). The $\delta_x$ are independent, so they form a basis of it; when $X$ is infinite they do not span $F^X$.

:::
