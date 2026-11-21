---
title: "Circulant Matrices and the Convolution Rule"
sources: [mit18065-30, mit18065-31, mit18065-32]
requires: [math/linear-algebra/eigenvalues/complex-matrices]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lectures 30–32 (video lectures and problem sets; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->

A circulant matrix has constant diagonals that wrap around. Every circulant is a polynomial in one cyclic shift, so all circulants of one size share the same eigenvectors: the columns of the Fourier matrix. Multiplying circulants is cyclic convolution, and the Fourier matrix turns it into componentwise multiplication. Indices run from $0$ to $n-1$ and are read modulo $n$; $F$ is the Fourier matrix with $F_{jk}=w^{jk}$, $w=e^{2\pi i/n}$ (@def-fourier-matrix), and $\mathbf{f}_k$ is its column $k$.

::: {#def-circulant-matrix .definition name="Circulant matrix"}

Let $P$ be the $n\times n$ cyclic shift with $P_{i,i+1}=1$ (so $P_{n-1,0}=1$) and zeros elsewhere. For $\mathbf{c}=(c_0,\dots,c_{n-1})$ the *circulant matrix* is
$$C(\mathbf{c})=c_0I+c_1P+c_2P^2+\dots+c_{n-1}P^{n-1},\qquad C_{ij}=c_{j-i}.$$
Its first row is $\mathbf{c}$, and each row is the previous one shifted one place to the right. For $n=3$:
$$C(\mathbf{c})=\begin{bmatrix}c_0&c_1&c_2\\c_2&c_0&c_1\\c_1&c_2&c_0\end{bmatrix}.$$

:::

::: {#thm-circulant-eigenvectors .theorem name="Eigenvectors of every circulant"}

$$C(\mathbf{c})\,\mathbf{f}_k=(F\mathbf{c})_k\,\mathbf{f}_k\qquad(k=0,\dots,n-1).$$
So $C(\mathbf{c})=\frac1n F\,\operatorname{diag}(F\mathbf{c})\,\overline F$: the eigenvectors are the Fourier columns for every $\mathbf{c}$, and the eigenvalues are the entries of $F\mathbf{c}$.

:::

::: {.proof}

1. $(P\mathbf{f}_k)_j=(\mathbf{f}_k)_{j+1}=w^{(j+1)k}=w^k(\mathbf{f}_k)_j$, using $w^n=1$ for the wrap-around. So $P\mathbf{f}_k=w^k\mathbf{f}_k$.

2. Then $P^m\mathbf{f}_k=w^{mk}\mathbf{f}_k$, and $C(\mathbf{c})\mathbf{f}_k=\sum_mc_mw^{mk}\mathbf{f}_k=(F\mathbf{c})_k\mathbf{f}_k$.

3. In matrix form $C(\mathbf{c})F=F\operatorname{diag}(F\mathbf{c})$. Since $\overline F F=nI$ (@thm-fourier-matrix-orthogonal), $F^{-1}=\frac1n\overline F$.

:::

::: {#def-cyclic-convolution .definition name="Cyclic and ordinary convolution"}

The *cyclic convolution* of $\mathbf{c},\mathbf{d}\in\mathbb{C}^n$ is the vector $\mathbf{c}\circledast\mathbf{d}\in\mathbb{C}^n$ with
$$(\mathbf{c}\circledast\mathbf{d})_k=\sum_{i+j\equiv k\ (\mathrm{mod}\ n)}c_id_j .$$
The *ordinary convolution* $\mathbf{c}*\mathbf{d}\in\mathbb{C}^{2n-1}$ has $(\mathbf{c}*\mathbf{d})_k=\sum_{i+j=k}c_id_j$: the coefficients of the product of the polynomials $\sum c_ix^i$ and $\sum d_jx^j$. Cyclic convolution folds entry $k+n$ of $\mathbf{c}*\mathbf{d}$ back onto entry $k$.

:::

::: {#thm-cyclic-convolution-rule .theorem name="Convolution rule" related="cor-fast-polynomial-multiplication"}

$$C(\mathbf{c})\,C(\mathbf{d})=C(\mathbf{c}\circledast\mathbf{d}),\qquad F(\mathbf{c}\circledast\mathbf{d})=(F\mathbf{c})\odot(F\mathbf{d}),$$
where $\odot$ multiplies vectors component by component.

:::

::: {.proof}

1. $C(\mathbf{c})C(\mathbf{d})=\sum_{i,j}c_id_jP^{i+j}$, and $P^n=I$, so $P^{i+j}=P^k$ with $k\equiv i+j$. Collecting terms gives $\sum_k(\mathbf{c}\circledast\mathbf{d})_kP^k$.

2. Apply both sides to $\mathbf{f}_k$. By @thm-circulant-eigenvectors the left side gives $(F\mathbf{c})_k(F\mathbf{d})_k\mathbf{f}_k$ and the right side gives $(F(\mathbf{c}\circledast\mathbf{d}))_k\mathbf{f}_k$.

:::

::: {#cor-circulants-commute .corollary name="Circulants commute"}

Any two $n\times n$ circulants commute, and the eigenvalues of $C(\mathbf{c})C(\mathbf{d})$ are the products $(F\mathbf{c})_k(F\mathbf{d})_k$.

:::

::: {.proof}

$\mathbf{c}\circledast\mathbf{d}=\mathbf{d}\circledast\mathbf{c}$ from the symmetric definition, so @thm-cyclic-convolution-rule gives $C(\mathbf{c})C(\mathbf{d})=C(\mathbf{d})C(\mathbf{c})$.

:::

::: {#exm-circulant-three .example name="A 3 by 3 circulant"}

For $\mathbf{c}=(1,2,3)$,
$$C=\begin{bmatrix}1&2&3\\3&1&2\\2&3&1\end{bmatrix},\qquad F\mathbf{c}=\big(6,\ -\tfrac32-\tfrac{\sqrt3}2i,\ -\tfrac32+\tfrac{\sqrt3}2i\big).$$
The eigenvalue $6$ belongs to $\mathbf{f}_0=(1,1,1)$ (every row sums to $6$), and the three eigenvalues add to $3=\operatorname{tr}C$. With $\mathbf{d}=(0,1,0)$, $C(\mathbf{d})=P$ and $\mathbf{c}\circledast\mathbf{d}=(3,1,2)$: multiplying by $P$ shifts $\mathbf{c}$ cyclically.

:::

::: {#fig-circulant-matrices-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (c00) at (0.000,1.000) {$1$};
\node[small vertex] (c01) at (0.866,-0.500) {$2$};
\node[small vertex] (c02) at (-0.866,-0.500) {$3$};
\draw[map] (c00) to[bend left=25] (c01);
\draw[map] (c01) to[bend left=25] (c02);
\draw[map] (c02) to[bend left=25] (c00);
\node[small vertex] (c10) at (4.200,1.000) {$3$};
\node[small vertex] (c11) at (5.066,-0.500) {$1$};
\node[small vertex] (c12) at (3.334,-0.500) {$2$};
\draw[map] (c10) to[bend left=25] (c11);
\draw[map] (c11) to[bend left=25] (c12);
\draw[map] (c12) to[bend left=25] (c10);
\node[lab, below] at (0,-1.1) {$\mathbf c=(1,2,3)$}; \node[lab, below] at (4.2,-1.1) {$P\mathbf c=(3,1,2)$};
\draw[map, hl] (1.5,0) -- node[lab, above] {$P$} (2.7,0);
\end{tikzpicture}
\end{center}
```

Entries of $\mathbf c$ placed around a cycle (read clockwise from the top): the shift $P$ turns the cycle one step. A circulant $C(\mathbf c)$ is $c_0I+c_1P+c_2P^2$, a combination of these rotations.

:::

::: {#rmk-circulant-matrices-1 .remark name="Convolutional neural networks"}

A convolutional layer applies the same small filter at every position of a signal or image, so its weight matrix is a (block) Toeplitz matrix, which becomes circulant under periodic boundary conditions. It has only as many free weights as the filter, not $n^2$, and by @thm-circulant-eigenvectors the FFT can apply it in $O(n\log n)$ operations (@thm-fft).

:::
