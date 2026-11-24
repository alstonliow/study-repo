---
title: "Jacobians of Matrix Functions and Kronecker Products"
sources: [mit18s096-3]
requires: [math/calculus/matrix/derivatives/linear-operator-derivatives, math/linear-algebra/vector-spaces/matrix-spaces-and-rank-one]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 3 (Jacobians of matrix functions, the matrix-square example, Kronecker products and their cost), in our own wording; the numbers in the example are ours, checked in Python; proofs written out in steps. -->

A function from $m\times n$ matrices to $p\times q$ matrices has a derivative that is a linear operator between matrix spaces. Choosing a way to list the entries of a matrix as a column turns that operator into an ordinary $pq\times mn$ Jacobian matrix, and the Kronecker product writes such Jacobians compactly.

::: {#def-vec .definition name="Vectorization"}

For $X\in\mathbb{R}^{m\times n}$ with columns $x_1,\dots,x_n$, the *vectorization* $\operatorname{vec}X\in\mathbb{R}^{mn}$ stacks the columns:

$$
\operatorname{vec}X=\begin{bmatrix}x_1\\ \vdots\\ x_n\end{bmatrix}.
$$

$\operatorname{vec}$ is a linear isomorphism $\mathbb{R}^{m\times n}\to\mathbb{R}^{mn}$. If $f$ maps matrices to matrices, its *Jacobian matrix* at $X$ is the matrix $J$ with $\operatorname{vec}\bigl(f'(X)[dX]\bigr)=J\operatorname{vec}(dX)$ for all $dX$.

:::

::: {#def-kronecker-product .definition name="Kronecker product"}

For $A\in\mathbb{R}^{m\times n}$ and $B\in\mathbb{R}^{p\times q}$, the *Kronecker product* is the $mp\times nq$ block matrix

$$
A\otimes B=\begin{bmatrix}a_{11}B&\cdots&a_{1n}B\\ \vdots&\ddots&\vdots\\ a_{m1}B&\cdots&a_{mn}B\end{bmatrix}.
$$

:::

::: {#prp-kronecker-properties .proposition name="Rules for Kronecker products"}

Whenever the products are defined,

1. $(A\otimes B)(C\otimes D)=(AC)\otimes(BD)$;
2. $(A\otimes B)^{\mathsf T}=A^{\mathsf T}\otimes B^{\mathsf T}$;
3. if $A$ and $B$ are invertible, $(A\otimes B)^{-1}=A^{-1}\otimes B^{-1}$.

:::

::: {.proof}

1. Block $(i,j)$ of $(A\otimes B)(C\otimes D)$ is $\sum_k(a_{ik}B)(c_{kj}D)=\bigl(\sum_ka_{ik}c_{kj}\bigr)BD=(AC)_{ij}\,BD$, which is block $(i,j)$ of $(AC)\otimes(BD)$.

2. Block $(i,j)$ of the transpose is the transpose of block $(j,i)$, namely $a_{ji}B^{\mathsf T}=(A^{\mathsf T})_{ij}B^{\mathsf T}$.

3. By rule 1, $(A\otimes B)(A^{-1}\otimes B^{-1})=I\otimes I=I$.

:::

::: {#thm-vec-kronecker-identity .theorem name="The key identity"}

For $A\in\mathbb{R}^{m\times p}$, $X\in\mathbb{R}^{p\times q}$ and $B\in\mathbb{R}^{q\times n}$,

$$
\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}X.
$$

So the linear operator $X\mapsto AXB$ has Jacobian matrix $B^{\mathsf T}\otimes A$.

:::

::: {.proof}

1. Column $j$ of $AXB$ is $AXb_j$, where $b_j$ is column $j$ of $B$.

2. Write $Xb_j=\sum_kb_{kj}x_k$ with $x_k$ the columns of $X$. Then column $j$ of $AXB$ is $\sum_kb_{kj}Ax_k$.

3. Block row $j$ of $(B^{\mathsf T}\otimes A)\operatorname{vec}X$ is $\sum_k(B^{\mathsf T})_{jk}Ax_k=\sum_kb_{kj}Ax_k$, the same column.

4. Stacking over $j$ gives the identity.

:::

::: {#fig-jacobians-and-kronecker-products-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\foreach \i in {0,1}{\foreach \j in {0,1}{
  \draw[cell frame] (\j*1.1,-\i*0.8) rectangle (\j*1.1+1.1,-\i*0.8+0.8);}}
\draw[hl cell] (0,-0.8) rectangle (1.1,0.8);
\node[lab] at (0.55,0.4) {$x_{11}$}; \node[lab] at (1.65,0.4) {$x_{12}$};
\node[lab] at (0.55,-0.4) {$x_{21}$}; \node[lab] at (1.65,-0.4) {$x_{22}$};
\node[lab, above] at (1.1,0.85) {$X$};
\draw[map] (2.4,0) -- node[lab, above] {vec} (3.6,0);
\draw[hl cell] (4,0.6) rectangle (5.1,1.8);
\foreach \k/\t in {0/x_{11},1/x_{21},2/x_{12},3/x_{22}}{
  \draw[faint] (4,1.2-\k*0.6) rectangle (5.1,1.8-\k*0.6); \node[lab] at (4.55,1.5-\k*0.6) {$\t$};}
\node[lab, right] at (5.3,1.2) {first column};
\end{tikzpicture}
\end{center}
```

$\operatorname{vec}$ reads a matrix column by column. With this order, the operator $X\mapsto AXB$ becomes multiplication by $B^{\mathsf T}\otimes A$.

:::

::: {#exm-matrix-square-jacobian .example name="The Jacobian of the matrix square"}

Let $f(X)=X^2$ on $n\times n$ matrices, so $f'(X)[dX]=dX\,X+X\,dX$ (@exm-differential-quadratic-form). Writing $dX\,X=I\,dX\,X$ and $X\,dX=X\,dX\,I$, @thm-vec-kronecker-identity gives the Jacobian

$$
J=I\otimes X+X^{\mathsf T}\otimes I .
$$

For $X=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, with $\operatorname{vec}X=(x_{11},x_{21},x_{12},x_{22})$,

$$
J=\begin{bmatrix}2&2&3&0\\3&5&0&3\\2&0&5&2\\0&2&3&8\end{bmatrix}.
$$

For example the first row says $d(X^2)_{11}=2\,dx_{11}+2\,dx_{21}+3\,dx_{12}$, which matches $(X^2)_{11}=x_{11}^2+x_{12}x_{21}$ at this $X$. A finite-difference check in Python agrees to about seven digits.

:::

::: {#rmk-jacobians-and-kronecker-products-1 .remark name="Eigenvalues of the matrix-square Jacobian"}

If $X$ is diagonalizable with eigenvalues $\lambda_1,\dots,\lambda_n$, then by @prp-kronecker-properties the matrix $I\otimes X+X^{\mathsf T}\otimes I$ has the $n^2$ eigenvalues $\lambda_i+\lambda_j$. In the example $\lambda_1\lambda_2=-2$ and $\lambda_1+\lambda_2=5$, so $\det J=(2\lambda_1)(2\lambda_2)(\lambda_1+\lambda_2)^2=-200$, which is what a direct computation gives.

:::

::: {#prp-kronecker-cost .proposition name="Do not form the Kronecker product"}

For $n\times n$ matrices $A,B,X$, computing $AXB$ as two matrix products costs about $2n^3$ scalar multiplications. Forming $B^{\mathsf T}\otimes A$ needs $n^4$ storage, and multiplying it by $\operatorname{vec}X$ costs $n^4$ multiplications.

:::

::: {.proof}

1. Each of $AX$ and $(AX)B$ is a product of two $n\times n$ matrices, costing $n^3$ multiplications.

2. $B^{\mathsf T}\otimes A$ is $n^2\times n^2$, so it has $n^4$ entries, and a matrix–vector product with it costs one multiplication per entry.

3. For $n=1000$ the first method needs about $2\cdot10^9$ multiplications, the second $10^{12}$ and eight terabytes of storage in double precision.

:::

::: {#fig-jacobians-and-kronecker-products-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0,0) rectangle (1,1); \node[lab] at (0.5,0.5) {$A$};
\draw[cell frame] (1.2,0) rectangle (2.2,1); \node[lab] at (1.7,0.5) {$X$};
\draw[cell frame] (2.4,0) rectangle (3.4,1); \node[lab] at (2.9,0.5) {$B$};
\node[lab, below] at (1.7,-0.1) {$AXB$: $2n^3$ work, $n^2$ storage};
\draw[hl cell] (5,-1) rectangle (8,2); \node[lab] at (6.5,0.5) {$B^{\mathsf T}\otimes A$};
\draw[cell frame] (8.2,-1) rectangle (8.5,2); \node[lab, right] at (8.5,0.5) {$\operatorname{vec}X$};
\node[lab, below] at (6.75,-1.1) {$n^4$ work and storage};
\end{tikzpicture}
\end{center}
```

The Kronecker form is good for reasoning (eigenvalues, determinants, solving for a Jacobian), but in computation one applies the operator $X\mapsto AXB$ directly.

:::
