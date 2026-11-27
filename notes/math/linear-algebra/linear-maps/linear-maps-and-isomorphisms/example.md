<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 2.1, restated in our own words with our own checks. -->

::: {#exm-linear-maps-cambridge .example name="Linear maps on spaces of functions"}

1. For $A\in\operatorname{Mat}_{n,m}(F)$ the map $F^m\to F^n$, $v\mapsto Av$, is linear: $(A(\lambda u+\mu v))_i=\sum_jA_{ij}(\lambda u_j+\mu v_j)=\lambda(Au)_i+\mu(Av)_i$.
2. For fixed $g\in F^X$, multiplication $m_g:F^X\to F^X$, $m_g(f)(x)=g(x)f(x)$, is linear; for example $f(x)\mapsto2x^2f(x)$.
3. On $C([a,b],\mathbb R)$, $f\mapsto\bigl(x\mapsto\int_a^xf(t)\,dt\bigr)$ is linear, by linearity of the integral.
4. On $C^\infty([a,b],\mathbb R)$, $D:f\mapsto f'$ is linear.
5. If $\alpha,\beta\in L(U,V)$ and $\lambda\in F$, then $\alpha+\beta$ and $\lambda\alpha$, defined pointwise, are linear; so $L(U,V)$ is itself an $F$-vector space.
6. A composite of linear maps is linear; so $D^2$, $D^2+m_g\circ D$ and so on are linear.

:::

::: {#exm-kernel-image-equations .example name="Kernels and images as solution sets"}

1. For $A\in\operatorname{Mat}_{m,n}(F)$ and $\alpha:F^n\to F^m$, $x\mapsto Ax$, the system $Ax=b$ is solvable exactly when $b\in\operatorname{im}\alpha$, and $\ker\alpha$ is the set of solutions of $Ax=0$.
2. For fixed $p,q\in C^\infty(\mathbb R,\mathbb R)$ let $\beta(f)=f''+pf'+qf$ on $C^\infty(\mathbb R,\mathbb R)$. Then $f''+pf'+qf=y$ has a smooth solution exactly when $y\in\operatorname{im}\beta$, and $\ker\beta$ is the solution space of the homogeneous equation. In both cases the full solution set of a solvable equation is one solution plus the kernel.

:::
