<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-2-q9" status="draft"}
1. Entry $(i,j)$ of $Q^{\mathsf T}Q$ is row $i$ of $Q^{\mathsf T}$ (that is, $\mathbf{q}_i^{\mathsf T}$) times column $j$ of $Q$: it is $\mathbf{q}_i^{\mathsf T}\mathbf{q}_j$.

2. (a) The diagonal of $I$ gives $\mathbf{q}_i^{\mathsf T}\mathbf{q}_i=\lVert\mathbf{q}_i\rVert^2=1$.

3. (b) The off-diagonal zeros of $I$ give $\mathbf{q}_i^{\mathsf T}\mathbf{q}_j=0$ for $i\neq j$.

4. (c) The rotation $Q=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$: its columns are unit vectors ($\cos^2\theta+\sin^2\theta=1$) and their dot product is $-\cos\theta\sin\theta+\sin\theta\cos\theta=0$.
:::

::: {.solution for="prob-mit1806s10-6-q6" status="draft"}
(a) Take the dot product with $\mathbf{q}_1$: $c_1\mathbf{q}_1^{\mathsf T}\mathbf{q}_1+c_2\mathbf{q}_1^{\mathsf T}\mathbf{q}_2+c_3\mathbf{q}_1^{\mathsf T}\mathbf{q}_3=c_1\cdot1+0+0=0$. Dotting with $\mathbf{q}_2$ and $\mathbf{q}_3$ gives $c_2=c_3=0$.

(b) Multiply $Q\mathbf{x}=\mathbf{0}$ by $Q^{\mathsf T}$: $\mathbf{x}=Q^{\mathsf T}Q\mathbf{x}=\mathbf{0}$, since $Q^{\mathsf T}Q=I$. So $N(Q)=\{\mathbf{0}\}$ and the columns are independent.
:::

::: {.solution for="prob-mit1806s10-6-q7" status="draft"}
1. $A=\mathbf{a}/\lVert\mathbf{a}\rVert=\frac1{\sqrt2}(1,-1,0,0)$.

2. $\mathbf{b}-(A^{\mathsf T}\mathbf{b})A=(0,1,-1,0)+\frac12(1,-1,0,0)=\frac12(1,1,-2,0)$, so $B=\frac1{\sqrt6}(1,1,-2,0)$.

3. $A^{\mathsf T}\mathbf{c}=0$ and $B^{\mathsf T}\mathbf{c}=-\frac2{\sqrt6}$, so $\mathbf{c}-(B^{\mathsf T}\mathbf{c})B=(0,0,1,-1)+\frac13(1,1,-2,0)=\frac13(1,1,1,-3)$ and $C=\frac1{\sqrt{12}}(1,1,1,-3)$.

4. Each of $\mathbf{a},\mathbf{b},\mathbf{c}$ has components summing to $0$, so they lie in $N([1\ 1\ 1\ 1])=\mathbf{d}^{\perp}$, which has dimension $4-1=3$. They are independent: $x_1\mathbf{a}+x_2\mathbf{b}+x_3\mathbf{c}=(x_1,\ x_2-x_1,\ x_3-x_2,\ -x_3)=\mathbf{0}$ forces $x_1=x_2=x_3=0$. Three independent vectors in a 3-dimensional space are a basis (@cor-basis-from-independent-set).

5. $A,B,C$ are combinations of $\mathbf{a},\mathbf{b},\mathbf{c}$, so they are in the same space, and orthonormal vectors are independent (@prob-mit1806s10-6-q6). So they are a basis too.
:::

::: {.solution for="prob-mit1806s10-6-q8" status="draft"}
1. The first three columns are the vectors of @prob-mit1806s10-6-q7, so the first three columns of $Q$ are $\frac1{\sqrt2}(1,-1,0,0)$, $\frac1{\sqrt6}(1,1,-2,0)$, $\frac1{\sqrt{12}}(1,1,1,-3)$.

2. The fourth column $(0,0,0,1)$ minus its projections onto those three leaves a vector orthogonal to all of them, hence in the direction of $(1,1,1,1)$; normalised, $\frac12(1,1,1,1)$.

3. Scaling the columns by $\sqrt2,\sqrt6,\sqrt{12},2$ gives the integer matrix
   $$\begin{bmatrix}1&1&1&1\\-1&1&1&1\\0&-2&1&1\\0&0&-3&1\end{bmatrix},$$
   whose columns are orthogonal. (MATLAB may return some columns with the opposite sign.)
:::

::: {.solution for="prob-mit1806s10-6-q9" status="draft"}
1. $A=Q_1R$ with $R$ invertible, so $C(A)=C(Q_1)$: the columns of $Q_1$ are an orthonormal basis of the column space (@thm-qr-factorization).

2. The columns of $Q_2$ are orthonormal and orthogonal to those of $Q_1$, hence to $C(A)$. They lie in $C(A)^{\perp}=N(A^{\mathsf T})$, which has dimension $m-n$, so they are an orthonormal basis of the left nullspace.
:::
