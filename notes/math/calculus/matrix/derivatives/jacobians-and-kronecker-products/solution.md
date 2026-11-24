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
