---
title: "Symmetric Bilinear Forms and Quadratic Forms"
sources: [camib-la-7]
requires: [math/linear-algebra/bilinear-forms/bilinear-forms]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 7.1 (first half), in our own wording; examples ours (checked with sympy); proofs written out in steps. -->

From now on the form takes both arguments from the same space $V$, and one basis is used for both. By @prp-bilinear-form-change-of-basis the matrix then changes by $A\mapsto P^{\mathsf T}AP$.

::: {#def-symmetric-form-congruence .definition name="Symmetric form, congruent matrices"}

A bilinear form $\phi:V\times V\to F$ is *symmetric* if $\phi(u,v)=\phi(v,u)$ for all $u,v$; equivalently its matrix in any basis is symmetric. Square matrices $A,B$ are *congruent* if $B=P^{\mathsf T}AP$ for some invertible $P$.

:::

::: {#fig-symmetric-forms-and-quadratic-forms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] at (0,0) {similarity: $P^{-1}AP$}; \node[lab, note, align=center] at (0,-0.9) {$A$ is a map $V\to V$\\eigenvalues are invariant};
\node[hl box] at (5.4,0) {congruence: $P^{\mathsf T}AP$}; \node[lab, note, align=center] at (5.4,-0.9) {$A$ is a form $V\times V\to F$\\$p,q$ and rank are invariant};
\node[lab, note, align=center] at (2.7,1.0) {the same when $P^{-1}=P^{\mathsf T}$ (orthogonal $P$)};
\end{tikzpicture}
\end{center}
```

A square matrix can describe a linear map or a bilinear form, and the two change differently with the basis. They agree for orthogonal changes of basis, which is why the spectral theorem diagonalises a symmetric matrix in both senses at once.

:::

Congruence is an equivalence relation, and two matrices are congruent exactly when they represent the same form on $V$ in two bases. Congruence preserves symmetry and rank but not eigenvalues or determinant: $\det(P^{\mathsf T}AP)=(\det P)^2\det A$.

::: {#def-quadratic-form .definition name="Quadratic form"}

A map $q:V\to F$ is a *quadratic form* if $q(v)=\phi(v,v)$ for some bilinear form $\phi$ on $V$. In coordinates, $q(\mathbf x)=\mathbf x^{\mathsf T}A\mathbf x=\sum_{i,j}a_{ij}x_ix_j$.

:::

::: {#fig-symmetric-forms-and-quadratic-forms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell, fill=primaryLight] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell, fill=primaryLight] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[hl cell] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$3$};
\draw[cell, fill=primaryLight] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$2$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell, fill=primaryLight] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[hl cell] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\node[lab, note, anchor=west, align=left] at (2.0,0.825) {$q=\textcolor{accent}{1}x^2+\textcolor{accent}{3}y^2+\textcolor{accent}{1}z^2+\textcolor{primary}{2}xy+\textcolor{primary}{4}yz$\\squares go on the diagonal;\\a cross term $c\,x_ix_j$ is split, $\frac c2$ into $(i,j)$ and $(j,i)$};
\end{tikzpicture}
\end{center}
```

Reading off the symmetric matrix of the quadratic form of @exm-diagonalising-quadratic-form. Splitting each cross term in half makes the matrix symmetric, and then $q(\mathbf x)=\mathbf x^{\mathsf T}A\mathbf x$.

:::

Different bilinear forms can give the same quadratic form: $\mathbf x^{\mathsf T}A\mathbf x=\mathbf x^{\mathsf T}A^{\mathsf T}\mathbf x$, and $x_1x_2$ comes from $\begin{bmatrix}0&1\\0&0\end{bmatrix}$ and from $\begin{bmatrix}0&\frac12\\\frac12&0\end{bmatrix}$. Away from characteristic $2$ the symmetric one is unique.

::: {#prp-polarization-identity .proposition name="Polarization identity"}

Let $1+1\ne0$ in $F$. If $q$ is a quadratic form on $V$, there is exactly one symmetric bilinear form $\phi$ with $q(v)=\phi(v,v)$, namely
$$\phi(u,v)=\tfrac12\big(q(u+v)-q(u)-q(v)\big).$$

:::

::: {.proof}

1. Existence: if $q(v)=\psi(v,v)$, then $\phi(u,v)=\frac12(\psi(u,v)+\psi(v,u))$ is symmetric bilinear and $\phi(v,v)=\psi(v,v)$.

2. Uniqueness: for symmetric $\phi$, $q(u+v)=\phi(u+v,u+v)=q(u)+2\phi(u,v)+q(v)$, which determines $\phi(u,v)$ when $2$ is invertible.

:::

::: {#thm-symmetric-form-diagonalizable .theorem name="Symmetric forms can be diagonalised"}

Let $1+1\ne0$ in $F$ and $\phi$ a symmetric bilinear form on a finite-dimensional $V$. There is a basis $e_1,\dots,e_n$ of $V$ with $\phi(e_i,e_j)=0$ for $i\ne j$: the matrix of $\phi$ is diagonal. Equivalently, every symmetric matrix is congruent to a diagonal matrix.

:::

::: {.proof}

Induction on $n=\dim V$; $n\le1$ is trivial.

1. If $\phi=0$, every basis works. Otherwise $q(v)=\phi(v,v)$ is not identically $0$: if it were, polarization (@prp-polarization-identity) would give $\phi=0$. Pick $e_1$ with $\phi(e_1,e_1)\ne0$.

2. Let $U=\{u\in V:\phi(e_1,u)=0\}$, the kernel of the non-zero functional $\phi(e_1,\cdot)$, of dimension $n-1$ (@thm-rank-nullity). Since $\phi(e_1,e_1)\ne0$, $e_1\notin U$, so $V=\langle e_1\rangle\oplus U$ (@prp-direct-sum-criteria).

3. By induction, $\phi$ restricted to $U$ has a diagonal basis $e_2,\dots,e_n$. Then $e_1,\dots,e_n$ is a basis of $V$, and $\phi(e_1,e_j)=0$ for $j\ge2$ because $e_j\in U$.

:::

::: {#fig-symmetric-forms-and-quadratic-forms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[xshift=0cm]
\draw[faint] (-1.4,0) -- (1.4,0); \draw[faint] (0,-1.4) -- (0,1.4);
\draw[hl] (0,0) circle (1);
\node[lab, below] at (0,-1.5) {$x^2+y^2=1$};
\end{scope}
\begin{scope}[xshift=3.4cm]
\draw[faint] (-1.4,0) -- (1.4,0); \draw[faint] (0,-1.4) -- (0,1.4);
\draw[hl, domain=-0.85:0.85, smooth, variable=\t] plot ({cosh(\t)},{sinh(\t)});
\draw[hl, domain=-0.85:0.85, smooth, variable=\t] plot ({-cosh(\t)},{sinh(\t)});
\node[lab, below] at (0,-1.5) {$x^2-y^2=1$};
\end{scope}
\begin{scope}[xshift=6.8cm]
\draw[faint] (-1.4,0) -- (1.4,0); \draw[faint] (0,-1.4) -- (0,1.4);
\draw[hl] (1,-1.3) -- (1,1.3); \draw[hl] (-1,-1.3) -- (-1,1.3);
\node[lab, below] at (0,-1.5) {$x^2=1$};
\end{scope}
\end{tikzpicture}
\end{center}
```

After diagonalising, a real quadratic form on $\mathbb R^2$ is $\pm x^2\pm y^2$ or simpler, and the curve $q=1$ shows which: an ellipse for signature $(2,0)$, a hyperbola for $(1,1)$, two lines for rank $1$.

:::

```{=latex}
\begin{algorithm}
\caption{Diagonalising a symmetric form}
\begin{algorithmic}
\INPUT A symmetric bilinear form $\phi$ on $V$, $\dim V=n$, with $1+1\ne0$ in $F$
\OUTPUT A basis $e_1,\dots,e_n$ with $\phi(e_i,e_j)=0$ for $i\ne j$
\STATE $U\gets V$; $k\gets0$
\WHILE{$\phi|_U\ne0$}
    \STATE pick $u\in U$ with $\phi(u,u)\ne0$ (one of $u_1$, $u_2$, $u_1+u_2$ works if $\phi(u_1,u_2)\ne0$)
    \STATE $k\gets k+1$; $e_k\gets u$; $U\gets\{x\in U:\phi(e_k,x)=0\}$
\ENDWHILE
\STATE complete with any basis $e_{k+1},\dots,e_n$ of $U$
\RETURN $e_1,\dots,e_n$
\end{algorithmic}
\end{algorithm}
```

The proof is an algorithm: completing the square.

::: {#exm-diagonalising-quadratic-form .example name="Diagonalising by completing the square"}

Let $q(x,y,z)=x^2+2xy+3y^2+4yz+z^2$ on $\mathbb R^3$, with symmetric matrix $A=\begin{bmatrix}1&1&0\\1&3&2\\0&2&1\end{bmatrix}$. Then
$$q=(x+y)^2+2y^2+4yz+z^2=(x+y)^2+2(y+z)^2-z^2.$$
With new coordinates $x'=x+y$, $y'=y+z$, $z'=z$, $q=x'^2+2y'^2-z'^2$. If $\mathbf x'=M\mathbf x$, then $P=M^{-1}$ and $P^{\mathsf T}AP=\operatorname{diag}(1,2,-1)$. The determinant checks the result: $\det A=-2=(\det P)^2\cdot(1\cdot2\cdot(-1))$ with $\det P=1$.

:::

::: {#thm-complex-symmetric-forms .theorem name="Classification over the complex numbers"}

Let $\phi$ be a symmetric bilinear form of rank $r$ on an $n$-dimensional complex vector space. There is a basis in which
$$[\phi]=\begin{bmatrix}I_r&0\\0&0\end{bmatrix}.$$
So two complex symmetric matrices are congruent if and only if they have the same rank.

:::

::: {.proof}

1. By @thm-symmetric-form-diagonalizable there is a basis with $\phi(e_i,e_j)=0$ for $i\ne j$; reorder it so that $\phi(e_i,e_i)=\lambda_i\ne0$ exactly for $i\le r'$. The diagonal matrix has rank $r'$, so $r'=r$.

2. For $i\le r$ choose a complex square root $\mu_i$ of $\lambda_i$ and replace $e_i$ by $e_i/\mu_i$. Then $\phi(e_i,e_i)=\lambda_i/\mu_i^2=1$.

3. Congruent matrices have the same rank, and matrices of equal rank are congruent to the same normal form.

:::

Over $\mathbb R$ step 2 fails for negative $\lambda_i$, and signs survive: that is Sylvester's law (@sec-math-linear-algebra-bilinear-forms-sylvester-law-of-inertia).
