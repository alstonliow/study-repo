<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 2.3, restated in our own words with our own checks. -->

::: {#exm-dimension-via-rank-nullity .example name="A dimension from rank–nullity"}

Let $W=\{x\in\mathbb R^5:x_1+x_2+x_3=0,\ x_3-x_4-x_5=0\}$.

1. $W=\ker\alpha$ for $\alpha:\mathbb R^5\to\mathbb R^2$, $x\mapsto(x_1+x_2+x_3,\ x_3-x_4-x_5)^{\mathsf T}$.

2. $\alpha(e_1)=(1,0)^{\mathsf T}$ and $\alpha(e_4)=(0,-1)^{\mathsf T}$ span $\mathbb R^2$, so $r(\alpha)=2$.

3. Rank–nullity gives $\dim W=n(\alpha)=5-2=3$.

In general, $m$ homogeneous linear equations in $n$ unknowns have a solution space of dimension at least $n-m$.

:::

::: {#exm-sum-intersection-via-rank-nullity .example name="The dimension of a sum from rank–nullity"}

Let $U,W$ be subspaces of a finite-dimensional $V$ and $\alpha:U\oplus W\to V$, $(u,w)\mapsto u+w$ (external direct sum).

1. $\operatorname{im}\alpha=U+W$.

2. $(u,w)\in\ker\alpha$ iff $w=-u$, which forces $u\in U\cap W$; so $\ker\alpha=\{(u,-u):u\in U\cap W\}$, and $u\mapsto(u,-u)$ is an isomorphism $U\cap W\to\ker\alpha$.

3. Rank–nullity gives
$$\dim U+\dim W=\dim(U\oplus W)=\dim(U+W)+\dim(U\cap W),$$
without choosing bases.

:::
