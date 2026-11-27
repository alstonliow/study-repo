<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 1.1, restated in our own words with our own checks. -->

::: {#exm-function-spaces-over-field .example name="Spaces of functions"}

1. For any set $X$ and any $F$-vector space $V$, the maps $X\to V$ form a vector space $V^X$ under $(f+g)(x)=f(x)+g(x)$ and $(\lambda f)(x)=\lambda f(x)$. The case $V=F$ is $F^X$.
2. Inside $\mathbb R^{[a,b]}$, the continuous functions $C([a,b],\mathbb R)$ and the infinitely differentiable functions $C^\infty([a,b],\mathbb R)$ are subspaces: sums and scalar multiples of continuous (smooth) functions are continuous (smooth), and $0$ is both. So $C^\infty([a,b],\mathbb R)\le C([a,b],\mathbb R)\le\mathbb R^{[a,b]}$.
3. $\operatorname{Mat}_{m,n}(\mathbb R)$ with entrywise operations is $\mathbb R^X$ for $X=\{1,\dots,m\}\times\{1,\dots,n\}$.

:::

::: {#exm-affine-plane-not-subspace .example name="A plane is a subspace only through the origin"}

Let $U_t=\{x\in\mathbb R^3:x_1+x_2+x_3=t\}$.

1. If $t=0$, then $x,y\in U_0$ give $(x+\lambda y)_1+(x+\lambda y)_2+(x+\lambda y)_3=0+\lambda\cdot0=0$, and $0\in U_0$; so $U_0$ is a subspace.

2. If $t\ne0$, then $0\notin U_t$, so $U_t$ is not a subspace.

:::

::: {#exm-finite-support-subspace .example name="Functions of finite support"}

For $f\in F^X$ let $\operatorname{supp}f=\{x\in X:f(x)\ne0\}$. The functions with finite support form a subspace of $F^X$.

1. $\operatorname{supp}0=\emptyset$ is finite.

2. $\operatorname{supp}(f+g)\subseteq\operatorname{supp}f\cup\operatorname{supp}g$, a union of two finite sets.

3. $\operatorname{supp}(\lambda f)=\operatorname{supp}f$ for $\lambda\ne0$, and $\lambda f=0$ for $\lambda=0$.

If $X$ is infinite this subspace is proper: the constant function $1$ is not in it.

:::
