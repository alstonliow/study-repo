<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-33-q2" status="draft"}
1. Put $\mathbf{x}_1=\mathbf{0}$. By @thm-points-from-distances, $G_{22}=9$, $G_{33}=25$, $G_{23}=\frac12(9+25-16)=9$, and row and column $1$ are zero:
$$G=\begin{bmatrix}0&0&0\\0&9&9\\0&9&25\end{bmatrix}.$$

2. The block $\begin{bmatrix}9&9\\9&25\end{bmatrix}$ has determinant $144>0$, so $G$ is positive semidefinite of rank $2$: the points lie in a plane.

3. Factor: $\mathbf{x}_2=(3,0)$; then $\mathbf{x}_2^{\mathsf T}\mathbf{x}_3=9$ and $\lVert\mathbf{x}_3\rVert^2=25$ give $\mathbf{x}_3=(3,4)$. Check $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert=4$. It is a $3$-$4$-$5$ right triangle with the right angle at $\mathbf{x}_2$.
:::

::: {.solution for="prob-mit18065ps-34-q1" status="draft"}
1. SVD route (@thm-orthogonal-procrustes): $Y^{\mathsf T}X=X$ is symmetric with eigenvalues $3$ for $\mathbf{q}_1=(1,1)/\sqrt2$ and $-1$ for $\mathbf{q}_2=(1,-1)/\sqrt2$. So $X=U\Sigma V^{\mathsf T}$ with $\Sigma=\operatorname{diag}(3,1)$, $V=[\mathbf{q}_1\ \mathbf{q}_2]$, $U=[\mathbf{q}_1\ {-\mathbf{q}_2}]$, and
$$Q=UV^{\mathsf T}=\mathbf{q}_1\mathbf{q}_1^{\mathsf T}-\mathbf{q}_2\mathbf{q}_2^{\mathsf T}=\begin{bmatrix}0&1\\1&0\end{bmatrix},$$
a reflection, with $\lVert X-Q\rVert_F^2=4$.

2. Rotations only: $\lVert X-Q\rVert_F^2=\lVert X\rVert_F^2+2-2\operatorname{tr}(Q^{\mathsf T}X)=12-4\cos\theta$, since $\operatorname{tr}(Q^{\mathsf T}X)=(\cos\theta+2\sin\theta)+(-2\sin\theta+\cos\theta)=2\cos\theta$.

3. The derivative $4\sin\theta=0$ gives $\theta=0$ (minimum, value $8$) or $\theta=\pi$ (maximum). So the best rotation is $Q=I$, and the reflection found by the SVD does better ($4<8$): the SVD answer ranges over all orthogonal matrices.
:::
