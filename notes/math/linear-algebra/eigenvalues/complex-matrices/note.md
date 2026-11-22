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

::: {#fig-complex-matrices-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.40,0) -- (1.5,0);
\draw[->, muted] (0,-1.40) -- (0,1.5);
\fill[primary] (1,0) circle[pt] node[below, lab] {$1$}; \fill[accent] (0,1) circle[pt] node[right, lab] {$i$};
\draw[faint] (0,0) circle[radius=1];
\node[lab, tick] at (1.4,-0.25) {Re}; \node[lab, tick] at (0.3,1.45) {Im};
\end{scope}
\node[lab, anchor=west, align=left] at (2.0,0.2) {$\mathbf z=(1,i)$:\\$\mathbf z^{\mathsf T}\mathbf z=1+i^2=0$\quad(wrong length)\\$\mathbf z^{\mathsf H}\mathbf z=\lvert1\rvert^2+\lvert i\rvert^2=2$};
\end{tikzpicture}
\end{center}
```

Why the inner product in $\mathbb C^n$ conjugates. Both entries of $\mathbf z=(1,i)$ lie on the unit circle, so $\lVert\mathbf z\rVert^2$ should be $2$; without the conjugate the squares cancel.

:::

::: {#def-hermitian-unitary .definition name="Hermitian and unitary matrices"}

A complex square matrix $S$ is *Hermitian* if $S^{\mathsf H}=S$. A complex square matrix $Q$ is *unitary* if $Q^{\mathsf H}Q=I$, i.e. its columns are orthonormal for the inner product above. Real symmetric and real orthogonal matrices are the real cases.

:::

::: {#thm-hermitian-real-eigenvalues .theorem name="Hermitian matrices"}

A Hermitian matrix has real eigenvalues, and eigenvectors for different eigenvalues are orthogonal. A unitary matrix preserves lengths and all its eigenvalues have $\lvert\lambda\rvert=1$.

:::

::: {.proof}

1. If $S\mathbf{z}=\lambda\mathbf{z}$, then $\mathbf{z}^{\mathsf H}S\mathbf{z}=\lambda\lVert\mathbf{z}\rVert^2$. This number equals its own conjugate, since $(\mathbf{z}^{\mathsf H}S\mathbf{z})^{\mathsf H}=\mathbf{z}^{\mathsf H}S^{\mathsf H}\mathbf{z}=\mathbf{z}^{\mathsf H}S\mathbf{z}$. So $\lambda$ is real.

2. Orthogonality follows as in step 3 of @lem-self-adjoint-eigenvalues with $\mathsf H$ in place of $\mathsf T$.

3. $\lVert Q\mathbf{z}\rVert^2=\mathbf{z}^{\mathsf H}Q^{\mathsf H}Q\mathbf{z}=\lVert\mathbf{z}\rVert^2$. If $Q\mathbf{z}=\lambda\mathbf{z}$ then $\lVert\mathbf{z}\rVert=\lvert\lambda\rvert\lVert\mathbf{z}\rVert$, so $\lvert\lambda\rvert=1$.

:::

::: {#def-fourier-matrix .definition name="Fourier matrix" related="def-dft"}

Let $w=e^{2\pi i/n}$. The $n\times n$ *Fourier matrix* has entries $(F_n)_{jk}=w^{jk}$ for $j,k=0,\dots,n-1$:
$$F_4=\begin{bmatrix}1&1&1&1\\1&i&i^2&i^3\\1&i^2&i^4&i^6\\1&i^3&i^6&i^9\end{bmatrix}=\begin{bmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{bmatrix}.$$

:::

::: {#fig-complex-matrices-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (-0.45,-0.45) rectangle (0.45,0.45);
\draw[faint] (0.00,0.00) circle[radius=0.3];
\draw[->, emph, primary] (0.00,0.00) -- (0.300,0.000);
\draw[cell frame] (0.45,-0.45) rectangle (1.35,0.45);
\draw[faint] (0.90,0.00) circle[radius=0.3];
\draw[->, emph, primary] (0.90,0.00) -- (1.200,0.000);
\draw[cell frame] (1.35,-0.45) rectangle (2.25,0.45);
\draw[faint] (1.80,0.00) circle[radius=0.3];
\draw[->, emph, primary] (1.80,0.00) -- (2.100,0.000);
\draw[cell frame] (2.25,-0.45) rectangle (3.15,0.45);
\draw[faint] (2.70,0.00) circle[radius=0.3];
\draw[->, emph, primary] (2.70,0.00) -- (3.000,0.000);
\draw[cell frame] (-0.45,-1.35) rectangle (0.45,-0.45);
\draw[faint] (0.00,-0.90) circle[radius=0.3];
\draw[->, emph, primary] (0.00,-0.90) -- (0.300,-0.900);
\draw[hl cell] (0.45,-1.35) rectangle (1.35,-0.45);
\draw[faint] (0.90,-0.90) circle[radius=0.3];
\draw[->, emph, primary] (0.90,-0.90) -- (0.900,-0.600);
\draw[hl cell] (1.35,-1.35) rectangle (2.25,-0.45);
\draw[faint] (1.80,-0.90) circle[radius=0.3];
\draw[->, emph, primary] (1.80,-0.90) -- (1.500,-0.900);
\draw[hl cell] (2.25,-1.35) rectangle (3.15,-0.45);
\draw[faint] (2.70,-0.90) circle[radius=0.3];
\draw[->, emph, primary] (2.70,-0.90) -- (2.700,-1.200);
\draw[cell frame] (-0.45,-2.25) rectangle (0.45,-1.35);
\draw[faint] (0.00,-1.80) circle[radius=0.3];
\draw[->, emph, primary] (0.00,-1.80) -- (0.300,-1.800);
\draw[hl cell] (0.45,-2.25) rectangle (1.35,-1.35);
\draw[faint] (0.90,-1.80) circle[radius=0.3];
\draw[->, emph, primary] (0.90,-1.80) -- (0.600,-1.800);
\draw[cell frame] (1.35,-2.25) rectangle (2.25,-1.35);
\draw[faint] (1.80,-1.80) circle[radius=0.3];
\draw[->, emph, primary] (1.80,-1.80) -- (2.100,-1.800);
\draw[hl cell] (2.25,-2.25) rectangle (3.15,-1.35);
\draw[faint] (2.70,-1.80) circle[radius=0.3];
\draw[->, emph, primary] (2.70,-1.80) -- (2.400,-1.800);
\draw[cell frame] (-0.45,-3.15) rectangle (0.45,-2.25);
\draw[faint] (0.00,-2.70) circle[radius=0.3];
\draw[->, emph, primary] (0.00,-2.70) -- (0.300,-2.700);
\draw[hl cell] (0.45,-3.15) rectangle (1.35,-2.25);
\draw[faint] (0.90,-2.70) circle[radius=0.3];
\draw[->, emph, primary] (0.90,-2.70) -- (0.900,-3.000);
\draw[hl cell] (1.35,-3.15) rectangle (2.25,-2.25);
\draw[faint] (1.80,-2.70) circle[radius=0.3];
\draw[->, emph, primary] (1.80,-2.70) -- (1.500,-2.700);
\draw[hl cell] (2.25,-3.15) rectangle (3.15,-2.25);
\draw[faint] (2.70,-2.70) circle[radius=0.3];
\draw[->, emph, primary] (2.70,-2.70) -- (2.700,-2.400);
\node[lab, note, anchor=west, align=left] at (3.3,-1.35) {entry $(j,k)$ is $w^{jk}$, $w=i$:\\arrow at angle $jk\cdot90^\circ$;\\row $j$ turns $j$ times as fast};
\end{tikzpicture}
\end{center}
```

The $4\times4$ Fourier matrix drawn entry by entry, rows and columns numbered from $0$. Row $0$ is constant and each later row winds around the circle at its own frequency; rows of different frequency are orthogonal.

:::

::: {#fig-complex-matrices-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.6]
\draw[->] (-1.4,0) -- (1.7,0) node[lab, right] {$\mathrm{Re}$};
\draw[->] (0,-1.4) -- (0,1.5) node[lab, above] {$\mathrm{Im}$};
\draw[faint] (0,0) circle (1);
\foreach \k in {0,...,7} \fill[ink] (45*\k:1) circle[pt];
\draw[->, accent, emph] (0,0) -- (45:0.94);
\node[hl dot] at (45:1) {};
\draw (0.35,0) arc[start angle=0, end angle=45, radius=0.35];
\node[tick] at (22:0.55) {$\frac{2\pi}8$};
\node[lab, above right] at (45:1) {$w$};
\node[lab, right] at (0.08,1.1) {$w^2=i$};
\node[lab, above left] at (180:1) {$w^4=-1$};
\node[lab, below right] at (0:1) {$w^8=1$};
\end{tikzpicture}
\end{center}
```

The powers of $w=e^{2\pi i/8}$ are the eighth roots of unity, equally spaced on the unit circle; they are the entries of $F_8$. Multiplying by $w$ turns by the angle $2\pi/8$.

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

::: {#fig-complex-matrices-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] (in0) at (0,0.0) {$x_0$};
\node[lab] (in1) at (0,-0.8) {$x_2$};
\node[lab] (in2) at (0,-1.6) {$x_1$};
\node[lab] (in3) at (0,-2.40) {$x_3$};
\draw[cell frame] (0.6,0.3) rectangle (1.8,-1.1); \node[lab, note] at (1.2,-0.4) {$F_2$};
\draw[cell frame] (0.6,-1.3) rectangle (1.8,-2.7); \node[lab, note] at (1.2,-2.0) {$F_2$};
\draw[->] (in0) -- (0.6,0.0);
\fill[ink] (2.3,0.0) circle[pt]; \draw (1.8,0.0) -- (2.3,0.0);
\draw[->] (in1) -- (0.6,-0.8);
\fill[ink] (2.3,-0.8) circle[pt]; \draw (1.8,-0.8) -- (2.3,-0.8);
\draw[->] (in2) -- (0.6,-1.6);
\fill[ink] (2.3,-1.6) circle[pt]; \draw (1.8,-1.6) -- (2.3,-1.6);
\draw[->] (in3) -- (0.6,-2.40);
\fill[ink] (2.3,-2.40) circle[pt]; \draw (1.8,-2.40) -- (2.3,-2.40);
\draw[->, emph, primary] (2.3,0.0) -- (4.2,0.0);
\draw[->, emph, primary] (2.3,0.0) -- (4.2,-1.6);
\draw[->, emph, accent] (2.3,-1.6) -- (4.2,0.0);
\draw[->, emph, accent] (2.3,-1.6) -- (4.2,-1.6);
\draw[->, emph, primary] (2.3,-0.8) -- (4.2,-0.8);
\draw[->, emph, primary] (2.3,-0.8) -- (4.2,-2.40);
\draw[->, emph, accent] (2.3,-2.40) -- (4.2,-0.8);
\draw[->, emph, accent] (2.3,-2.40) -- (4.2,-2.40);
\node[lab, tick, accent] at (2.75,-1.40) {$\times 1$};
\node[lab, tick, accent] at (2.75,-2.2) {$\times w$};
\node[lab, anchor=west] at (4.3,0.0) {$y_0$};
\node[lab, anchor=west] at (4.3,-0.8) {$y_1$};
\node[lab, anchor=west] at (4.3,-1.6) {$y_2$};
\node[lab, anchor=west] at (4.3,-2.40) {$y_3$};
\node[lab, tick, accent] at (3.8,-2.2) {$-$}; \node[lab, tick, accent] at (3.8,-1.45) {$-$};
\node[lab, note, anchor=west, align=left] at (5.2,-1.2) {$y_j=y'_j+w^jy''_j$\\$y_{j+2}=y'_j-w^jy''_j$\\($j=0,1$, $w=i$)};
\end{tikzpicture}
\end{center}
```

The factorization for $n=4$ as a butterfly. $P$ sorts the input into even and odd components, two half-size transforms $F_2$ give $\mathbf y'$ and $\mathbf y''$, and the last factor combines them with the weights $1,w$ and opposite signs.

:::
