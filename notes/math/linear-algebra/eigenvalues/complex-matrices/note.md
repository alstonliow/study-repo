---
title: "Complex Matrices and the Fourier Matrix"
sources: [mit1806-26]
requires: [math/linear-algebra/eigenvalues/symmetric-matrices]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 26, in our own wording; proofs written out in steps. The FFT algorithm itself (divide and conquer on polynomials) is in cs/algorithm-design/fast-fourier-transform; this note is the matrix side. -->

For complex vectors the plain dot product fails as a length: $(1,i)\cdot(1,i)=1+i^2=0$. Conjugating one factor fixes this.

::: {#def-complex-inner-product .definition name="Inner product and length in C^n"}

For $\mathbf{z},\mathbf{w}\in\mathbb{C}^n$,
$$\mathbf{w}^{\mathsf H}\mathbf{z}=\bar w_1z_1+\dots+\bar w_nz_n,\qquad \lVert\mathbf{z}\rVert^2=\mathbf{z}^{\mathsf H}\mathbf{z}=\lvert z_1\rvert^2+\dots+\lvert z_n\rvert^2,$$
where $A^{\mathsf H}=\bar A^{\mathsf T}$ is the *conjugate transpose*. $\mathbf{z}$ and $\mathbf{w}$ are orthogonal when $\mathbf{w}^{\mathsf H}\mathbf{z}=0$.

:::

::: {#def-hermitian-unitary .definition name="Hermitian and unitary matrices"}

A complex square matrix $S$ is *Hermitian* if $S^{\mathsf H}=S$. A complex square matrix $Q$ is *unitary* if $Q^{\mathsf H}Q=I$, i.e. its columns are orthonormal for the inner product above. Real symmetric and real orthogonal matrices are the real cases.

:::

::: {#thm-hermitian-real-eigenvalues .theorem name="Hermitian matrices"}

A Hermitian matrix has real eigenvalues, and eigenvectors for different eigenvalues are orthogonal. A unitary matrix preserves lengths and all its eigenvalues have $\lvert\lambda\rvert=1$.

:::

::: {.proof}

1. If $S\mathbf{z}=\lambda\mathbf{z}$, then $\mathbf{z}^{\mathsf H}S\mathbf{z}=\lambda\lVert\mathbf{z}\rVert^2$. This number equals its own conjugate, since $(\mathbf{z}^{\mathsf H}S\mathbf{z})^{\mathsf H}=\mathbf{z}^{\mathsf H}S^{\mathsf H}\mathbf{z}=\mathbf{z}^{\mathsf H}S\mathbf{z}$. So $\lambda$ is real.

2. Orthogonality follows as in step 4 of @thm-symmetric-real-eigenvalues with $\mathsf H$ in place of $\mathsf T$.

3. $\lVert Q\mathbf{z}\rVert^2=\mathbf{z}^{\mathsf H}Q^{\mathsf H}Q\mathbf{z}=\lVert\mathbf{z}\rVert^2$. If $Q\mathbf{z}=\lambda\mathbf{z}$ then $\lVert\mathbf{z}\rVert=\lvert\lambda\rvert\lVert\mathbf{z}\rVert$, so $\lvert\lambda\rvert=1$.

:::

::: {#def-fourier-matrix .definition name="Fourier matrix" related="def-dft"}

Let $w=e^{2\pi i/n}$. The $n\times n$ *Fourier matrix* has entries $(F_n)_{jk}=w^{jk}$ for $j,k=0,\dots,n-1$:
$$F_4=\begin{bmatrix}1&1&1&1\\1&i&i^2&i^3\\1&i^2&i^4&i^6\\1&i^3&i^6&i^9\end{bmatrix}=\begin{bmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{bmatrix}.$$

:::

::: {#thm-fourier-matrix-orthogonal .theorem name="The columns of F are orthogonal"}

$F_n^{\mathsf H}F_n=nI$. Hence $F_n/\sqrt n$ is unitary and $F_n^{-1}=\frac1n\bar F_n$.

:::

::: {.proof}

1. Entry $(j,k)$ of $F_n^{\mathsf H}F_n$ is $\sum_{m=0}^{n-1}\overline{w^{mj}}w^{mk}=\sum_m w^{m(k-j)}$, because $\bar w=w^{-1}$.

2. For $j=k$ every term is $1$ and the sum is $n$.

3. For $j\neq k$, $q=w^{k-j}\neq1$ is an $n$-th root of unity, and the geometric sum is $\frac{q^n-1}{q-1}=0$.

4. $F_n$ is symmetric, so $F_n^{\mathsf H}=\bar F_n$, giving $F_n^{-1}=\frac1n\bar F_n$.

:::

::: {#thm-fft-factorization .theorem name="FFT as a matrix factorization" related="thm-fft"}

For $n=2m$,
$$F_n=\begin{bmatrix}I&D\\I&-D\end{bmatrix}\begin{bmatrix}F_m&0\\0&F_m\end{bmatrix}P,$$
where $D=\operatorname{diag}(1,w,\dots,w^{m-1})$ and $P$ is the permutation that puts the even-indexed components of a vector first and the odd-indexed ones after them. Applying this recursively multiplies by $F_n$ in $\frac12n\log_2n$ complex multiplications instead of $n^2$.

:::

::: {.proof}

1. Let $\mathbf{y}=F_n\mathbf{c}$, so $y_j=\sum_kw^{jk}c_k$. Split into even $k=2l$ and odd $k=2l+1$: $y_j=\sum_l(w^2)^{jl}c_{2l}+w^j\sum_l(w^2)^{jl}c_{2l+1}$.

2. $w^2$ is the primitive $m$-th root of unity, so the two sums are $(F_m\mathbf{c}')_j$ and $(F_m\mathbf{c}'')_j$ for the even part $\mathbf{c}'$ and the odd part $\mathbf{c}''$ (indices taken mod $m$).

3. For $j<m$ this is $y'_j+w^jy''_j$; for $j+m$ it is $y'_j-w^jy''_j$, because $w^m=-1$. These are the three factors.

4. Each level of the recursion costs $m=n/2$ multiplications by entries of $D$, and there are $\log_2n$ levels.

:::
