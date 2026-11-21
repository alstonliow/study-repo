<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-10-q7" status="draft"}
1. $A$ is symmetric, so $A^{\mathsf T}A=AA^{\mathsf T}=A^2=\begin{bmatrix}2&1\\1&1\end{bmatrix}$, with eigenvalues the roots of $\lambda^2-3\lambda+1$: $\frac{3\pm\sqrt5}2=\phi^2$ and $\phi^{-2}$, where $\phi=\frac{1+\sqrt5}2$.

2. $A$ itself has eigenvalues $\phi$ and $-1/\phi$ with eigenvectors $(\phi,1)$ and $(1,-\phi)$. Normalise: $\mathbf{v}_1=\frac{(\phi,1)}{\sqrt{1+\phi^2}}$, $\mathbf{v}_2=\frac{(1,-\phi)}{\sqrt{1+\phi^2}}$. These are the unit eigenvectors of $A^{\mathsf T}A$ (and of $AA^{\mathsf T}$).

3. Singular values $\sigma_1=\phi=\frac{1+\sqrt5}2$ and $\sigma_2=\frac1\phi=\frac{\sqrt5-1}2$. From $A\mathbf{v}=\sigma\mathbf{u}$: $\mathbf{u}_1=A\mathbf{v}_1/\sigma_1=\mathbf{v}_1$, and $\mathbf{u}_2=A\mathbf{v}_2/\sigma_2=-\mathbf{v}_2$ (because the eigenvalue is negative).

4. So $V=[\mathbf{v}_1\ \mathbf{v}_2]$, $U=[\mathbf{v}_1\ {-\mathbf{v}_2}]$, $\Sigma=\operatorname{diag}(\phi,1/\phi)$, and $U\Sigma V^{\mathsf T}=\phi\mathbf{v}_1\mathbf{v}_1^{\mathsf T}-\frac1\phi\mathbf{v}_2\mathbf{v}_2^{\mathsf T}=A$ by the spectral theorem (@cor-real-symmetric-orthogonally-diagonalisable). Check: $\sigma_1\sigma_2=1=\lvert\det A\rvert$.
:::

::: {.solution for="prob-mit1806s10-10-q8" status="draft"}
1. Assume all $\sigma_i>0$ and order the columns so that $\sigma_1\ge\dots\ge\sigma_n$ (otherwise $V$ below becomes a permutation matrix). Write $\mathbf{w}_i=\sigma_i\mathbf{u}_i$ with unit vectors $\mathbf{u}_i$, which are orthonormal.

2. Then $A=[\mathbf{u}_1\cdots\mathbf{u}_n]\operatorname{diag}(\sigma_1,\dots,\sigma_n)\,I$: take $V=I$, the $\sigma_i$ on the diagonal of $\Sigma$, and $\mathbf{u}_1,\dots,\mathbf{u}_n$ as the first columns of $U$, completed by an orthonormal basis of $N(A^{\mathsf T})$ if $m>n$.

3. Check: $A^{\mathsf T}A=\operatorname{diag}(\sigma_i^2)$ already, so its eigenvectors are the standard basis vectors, and $A\mathbf{e}_i=\mathbf{w}_i=\sigma_i\mathbf{u}_i$. If some $\mathbf{w}_i=\mathbf{0}$, its $\sigma_i=0$ and its $\mathbf{u}_i$ is any unit vector completing the orthonormal set.
:::

::: {.solution for="prob-mit1806s10-10-q9" status="draft"}
(a)

1. $V=\begin{pmatrix}\frac12&\frac1{\sqrt2}&\frac12\\\frac1{\sqrt2}&0&-\frac1{\sqrt2}\\\frac12&-\frac1{\sqrt2}&\frac12\end{pmatrix}$.

2. Up to scaling the columns are $(1,\sqrt2,1)$, $(1,0,-1)$, $(1,-\sqrt2,1)$. Multiply: $A^{\mathsf T}A(1,\sqrt2,1)=(2-\sqrt2,\ 2\sqrt2-2,\ 2-\sqrt2)=(2-\sqrt2)(1,\sqrt2,1)$; $A^{\mathsf T}A(1,0,-1)=(2,0,-2)$; $A^{\mathsf T}A(1,-\sqrt2,1)=(2+\sqrt2)(1,-\sqrt2,1)$.

(b) Multiplying out,
$$AV=\begin{pmatrix}\frac12&\frac{\sqrt2}2&\frac12\\\frac{\sqrt2-1}2&-\frac{\sqrt2}2&-\frac{\sqrt2+1}2\\\frac{1-\sqrt2}2&-\frac{\sqrt2}2&\frac{1+\sqrt2}2\\-\frac12&\frac{\sqrt2}2&-\frac12\end{pmatrix},\qquad (AV)^{\mathsf T}(AV)=V^{\mathsf T}A^{\mathsf T}AV=\operatorname{diag}(2-\sqrt2,\,2,\,2+\sqrt2).$$
So the columns are orthogonal with lengths $\sigma_i=\sqrt{\lambda_i}$, and $\mathbf{u}_i=A\mathbf{v}_i/\sigma_i$.

(c) $A^{\mathsf T}\mathbf{y}=\mathbf{0}$ says $y_1-y_2=y_2-y_3=y_3-y_4=0$, so $N(A^{\mathsf T})$ is the line through $(1,1,1,1)$ and $\mathbf{u}_4=\frac12(1,1,1,1)$.
:::

::: {.solution for="prob-mit18065ps-6-q6" status="draft"}
1. $A^{\mathsf T}A=\begin{bmatrix}9&12\\12&41\end{bmatrix}$ has trace $50$ and determinant $225$, so eigenvalues $45$ and $5$: $\sigma_1=3\sqrt5$, $\sigma_2=\sqrt5$ (check: $\sigma_1\sigma_2=15=\det A$).

2. Eigenvectors: $\mathbf{v}_1=(1,3)/\sqrt{10}$ (from $(A^{\mathsf T}A-45I)\mathbf{v}=\mathbf{0}$, i.e. $-36v_1+12v_2=0$) and $\mathbf{v}_2=(3,-1)/\sqrt{10}$.

3. $\mathbf{u}_i=A\mathbf{v}_i/\sigma_i$: $A(1,3)=(15,15)$ gives $\mathbf{u}_1=(1,1)/\sqrt2$; $A(3,-1)=(5,-5)$ gives $\mathbf{u}_2=(1,-1)/\sqrt2$.

4. Check: $\sigma_1\mathbf{u}_1\mathbf{v}_1^{\mathsf T}+\sigma_2\mathbf{u}_2\mathbf{v}_2^{\mathsf T}=\frac{3}{2}\begin{bmatrix}1&3\\1&3\end{bmatrix}+\frac12\begin{bmatrix}3&-1\\-3&1\end{bmatrix}=\begin{bmatrix}3&4\\0&5\end{bmatrix}$.
:::
