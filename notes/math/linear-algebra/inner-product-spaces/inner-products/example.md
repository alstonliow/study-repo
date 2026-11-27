<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 8.1, restated in our own words with our own checks. -->

::: {#exm-weighted-inner-product .example name="Weighted inner products on functions"}

Let $w:[0,1]\to\mathbb R$ be continuous with $w(t)>0$ for all $t$. On $C([0,1],F)$, $F=\mathbb R$ or $\mathbb C$, set
$$\langle f,g\rangle_w=\int_0^1w(t)f(t)\overline{g(t)}\,dt .$$

1. It is linear in $f$ and conjugate-symmetric, like the unweighted product.

2. $\langle f,f\rangle_w=\int_0^1w\lvert f\rvert^2\ge0$, and if $f(t_0)\ne0$ then $w\lvert f\rvert^2>0$ on an interval around $t_0$ by continuity, so $\langle f,f\rangle_w>0$.

So each positive weight gives a different inner product on the same space; $w=1$ is the usual one.

:::
