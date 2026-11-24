<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18s096ps-1-q3" status="draft"}
(a) Add linear maps and multiply them by scalars pointwise: $(L+M)[X]=L[X]+M[X]$, $(\alpha L)[X]=\alpha L[X]$. Sums and multiples of linear maps are linear, and the axioms hold because they hold in the output space. Through $\operatorname{vec}$ (@def-vec) each such map is an $n^2\times n^2$ matrix, and every such matrix gives one, so $\dim V=(n^2)^2=n^4$.

(b) The map $A\mapsto L_A$, $L_A[X]=AX$, is linear: $L_{A+\alpha B}=L_A+\alpha L_B$. So its image $W=\{L_A\}$ is a subspace of $V$, hence a vector space. It is injective, because $L_A=0$ gives $A=L_A[I]=0$. So $\dim W=\dim\mathbb{R}^{n\times n}=n^2$. (In Kronecker form, $L_A$ has the matrix $I\otimes A$ by @thm-vec-kronecker-identity.)

(c) For $n\ge2$, $n^2<n^4$, so $W$ is a proper subspace and there is some $L\in V\setminus W$, for example the transpose $X\mapsto X^{\mathsf T}$. Then $cL\notin W$ for every real $c\neq0$, since otherwise $L=\tfrac1c(cL)\in W$; more generally $L+M\notin W$ for every $M\in W$. That is infinitely many maps. (For $n=1$ the two spaces coincide.)
:::

::: {.solution for="prob-mit18s096ps-2-q4" status="draft"}
(a) The Jacobian is $\begin{bmatrix}\cosh\theta&\sinh\theta\\\sinh\theta&\cosh\theta\end{bmatrix}$ (@prob-mit18s096ps-1-q0), with determinant $\cosh^2\theta-\sinh^2\theta=1$. So the map preserves area. Its eigenvectors are $(1,1)$ and $(1,-1)$ with eigenvalues $e^{\theta}$ and $e^{-\theta}$: a small square around a point becomes a parallelogram of the same area, stretched by $e^{\theta}$ along the diagonal $(1,1)$ and compressed by $e^{-\theta}$ along $(1,-1)$. (The map is linear, so this is the same at every point.)

(b)(i) A centred-difference Jacobian in Python, with $\operatorname{vec}$ taken column by column for both $dM$ and the output so that the determinant has the right sign:

```python
import numpy as np
M = np.array([[0., 1, 4], [1, 0, 1], [4, 1, 0]])

def F(M, f):
    lam, X = np.linalg.eig(M)
    return (X @ np.diag(f(lam)) @ np.linalg.inv(X)).real

def jacobian(f, M, h=1e-5):
    cols = []
    for j in range(3):
        for i in range(3):                    # column-major order, as vec
            E = np.zeros((3, 3)); E[i, j] = h
            cols.append(((F(M + E, f) - F(M - E, f)) / (2 * h)).ravel(order="F"))
    return np.array(cols).T

for f in (np.exp, np.square, np.sin):
    print(np.linalg.det(jacobian(f, M)))
```

It prints about $939.059$ for $e^\lambda$, $4096.000$ for $\lambda^2$ and $8.41346\times10^{-6}$ for $\sin\lambda$.

(ii) The eigenvalues of $M$ are $-4$ and $2\pm\sqrt6$, that is $-4$, $-0.4495$ and $4.4495$. Evaluating the formula with these gives $939.059$, $4096$ and $8.41346\times10^{-6}$, the same values to six digits. For $f(\lambda)=\lambda^2$ the Jacobian is $I\otimes M+M^{\mathsf T}\otimes I$ exactly (@exm-matrix-square-jacobian), with eigenvalues $\lambda_i+\lambda_j$, and its determinant is again $4096$, consistent with the eigenvalue remark in @sec-math-calculus-matrix-derivatives-jacobians-and-kronecker-products.
:::

::: {.solution for="prob-mit18s096-3-q1" status="draft"}
Let $E_{ij}$ be the $m\times n$ matrix with a $1$ in position $(i,j)$ and $0$ elsewhere. Every $A$ is uniquely $A=\sum_{i,j}a_{ij}E_{ij}$, so the $E_{ij}$ form a basis of $\mathbb{R}^{m\times n}$ (@sec-math-linear-algebra-vector-spaces-matrix-spaces-and-rank-one).

$\operatorname{vec}A$ lists the coefficients $a_{ij}$ column by column (@def-vec), so it is the coordinate vector of $A$ in this basis taken in the order

$$E_{11},E_{21},\dots,E_{m1},\;E_{12},\dots,E_{m2},\;\dots,\;E_{1n},\dots,E_{mn},$$

that is, $E_{ij}=e_ie_j^{\mathsf T}$ ordered with $i$ running fastest (column-major order).
:::

::: {.solution for="prob-mit18s096-3-q2" status="draft"}
Identities 1–3 are @prp-kronecker-properties, proved there block by block. The others:

4. If $A^{\mathsf T}A=I$ and $B^{\mathsf T}B=I$, then by 1 and 2, $(A\otimes B)^{\mathsf T}(A\otimes B)=(A^{\mathsf T}A)\otimes(B^{\mathsf T}B)=I_n\otimes I_m=I_{nm}$.

5. 1. By 2, $A\otimes B=(A\otimes I_m)(I_n\otimes B)$.

   2. $I_n\otimes B$ is block diagonal with $n$ copies of $B$, so its determinant is $\det(B)^n$.

   3. $A\otimes I_m$ has blocks $a_{ij}I_m$. Reordering rows and columns by the same permutation (take entry $k$ of every block together) turns it into $I_m\otimes A$, block diagonal with $m$ copies of $A$. A simultaneous permutation of rows and columns does not change the determinant, so $\det(A\otimes I_m)=\det(A)^m$.

   4. Multiply.

6. The diagonal blocks of $A\otimes B$ are $a_{ii}B$, so $\operatorname{tr}(A\otimes B)=\sum_ia_{ii}\operatorname{tr}B=(\operatorname{tr}A)(\operatorname{tr}B)$.

7. View $u\otimes v$ as the Kronecker product of an $n\times1$ and an $m\times1$ matrix. By 2, $(A\otimes B)(u\otimes v)=(Au)\otimes(Bv)=(\lambda u)\otimes(\mu v)=\lambda\mu\,(u\otimes v)$, and $u\otimes v\neq0$ since its entries are all products $u_iv_k$ and some $u_i,v_k$ are nonzero. In vectorized form, $u\otimes v=\operatorname{vec}(vu^{\mathsf T})$, and @thm-vec-kronecker-identity gives $(A\otimes B)\operatorname{vec}X=\operatorname{vec}(BXA^{\mathsf T})$, which for $X=vu^{\mathsf T}$ is $\operatorname{vec}\bigl(Bv(Au)^{\mathsf T}\bigr)=\lambda\mu\operatorname{vec}X$.
:::
