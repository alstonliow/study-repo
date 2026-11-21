<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-15-q1" status="draft"}
Differentiate $\mathbf{u}^{\mathsf T}\mathbf{u}=1$ by the product rule: $\frac{d\mathbf{u}}{dt}^{\mathsf T}\mathbf{u}+\mathbf{u}^{\mathsf T}\frac{d\mathbf{u}}{dt}=2\,\mathbf{u}^{\mathsf T}\frac{d\mathbf{u}}{dt}=0$.
:::

::: {.solution for="prob-mit18065ps-15-q2" status="draft"}
1. $T=\mathbf{u}\mathbf{u}^{\mathsf T}+\mathbf{v}\mathbf{v}^{\mathsf T}$ is positive semidefinite of rank at most $2$, so $\lambda_n(T)\ge0$ and $\lambda_3(T)=0$ (when $n\ge3$).

2. @thm-weyl-inequality with $j=1$ on $S=(S+T)+(-T)$ gives $\alpha_i\ge\lambda_i$.

3. Weyl with $j=3$ gives $\alpha_{i+2}\le\lambda_i+\lambda_3(T)=\lambda_i$.

4. So $\alpha_i\ge\lambda_i\ge\alpha_{i+2}$: each eigenvalue can move up, but by no more than two places. (Applying @thm-rank-one-interlacing twice gives the same.)
:::

::: {.solution for="prob-mit18065ps-15-q5" status="draft"}
1. $A_3$: rows sum to zero, so $\lambda=0$ with $(1,1,1)$; $(1,0,-1)$ gives $\lambda=1$; the trace $4$ leaves $\lambda=3$, with eigenvector $(1,-2,1)$. Eigenvalues $3,1,0$.

2. $A_2$: $\lambda^2-3\lambda+1=0$, so $\lambda=(3\pm\sqrt5)/2\approx2.618,\ 0.382$.

3. $A_1$: $\lambda=1$.

4. Interlacing (@thm-cauchy-interlacing): $3\ge2.618\ge1\ge0.382\ge0$, and $2.618\ge1\ge0.382$.
:::

::: {.solution for="prob-mit18065ps-16-q3" status="draft"}
1. (a) $A(t)=\begin{bmatrix}2+t&1+t\\1+t&t\end{bmatrix}$ has trace $2+2t$ and determinant $(2+t)t-(1+t)^2=-1$. So
$$\lambda_{1,2}(t)=1+t\pm\sqrt{(1+t)^2+1}.$$

2. (b) At $t=0$: $\lambda=1\pm\sqrt2$. For $\lambda_1=1+\sqrt2$, $(2-\lambda)x_1+x_2=0$ gives $\mathbf{x}_1\propto(1,\sqrt2-1)$; for $\lambda_2=1-\sqrt2$, $\mathbf{x}_2\propto(1,-\sqrt2-1)$. $A$ is symmetric, so $\mathbf{y}=\mathbf{x}$ (unit vectors).

3. $dA/dt=\mathbf{1}\mathbf{1}^{\mathsf T}$, so $\mathbf{x}^{\mathsf T}\frac{dA}{dt}\mathbf{x}=(\mathbf{1}^{\mathsf T}\mathbf{x})^2/\lVert\mathbf{x}\rVert^2$. For $\mathbf{x}_1$: $(\sqrt2)^2/(1+(\sqrt2-1)^2)=2/(4-2\sqrt2)=1+\frac{\sqrt2}2$. Differentiating (a): $\lambda_1'(0)=1+\frac{1}{\sqrt2}$, the same. Likewise $\lambda_2'(0)=1-\frac1{\sqrt2}$, and the two add to $2=\frac{d}{dt}\operatorname{tr}A$.

4. (c) $A(t)-A(0)=t\,\mathbf{1}\mathbf{1}^{\mathsf T}$ is positive semidefinite (rank one) for $t>0$. Then $\lambda_1(t)$ increases from $1+\sqrt2$; $\lambda_2(t)=-1/\big(1+t+\sqrt{(1+t)^2+1}\big)$ increases from $1-\sqrt2$ but stays negative, below $\lambda_1(0)$. So $\lambda_1(t)\ge\lambda_1(0)\ge\lambda_2(t)\ge\lambda_2(0)$, as @thm-rank-one-interlacing predicts.
:::

::: {.solution for="prob-mit18065ps-18-q4" status="draft"}
The first $i$: $Y=\operatorname{span}(\mathbf{q}_1,\dots,\mathbf{q}_i)$. For $\mathbf{x}=c_1\mathbf{q}_1+\dots+c_i\mathbf{q}_i$ the Rayleigh quotient is $\sum\lambda_kc_k^2/\sum c_k^2\ge\lambda_i$, with equality at $\mathbf{q}_i$. This $Y$ attains the max–min in @thm-courant-fischer. (Any other $i$ eigenvectors include some $\mathbf{q}_k$ with $k>i$, and the minimum drops to $\lambda_k<\lambda_i$.)
:::
