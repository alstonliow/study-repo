---
title: "Change of Basis and Image Compression"
sources: [mit1806-31]
requires: [math/linear-algebra/positive-definite/linear-transformations, math/linear-algebra/eigenvalues/similar-matrices-and-jordan-form]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 31, in our own wording; proofs written out in steps. -->

::: {#prp-change-of-coordinates .proposition name="Change of coordinates"}

Let the columns of an invertible $n\times n$ matrix $W$ be a basis $\mathbf{w}_1,\dots,\mathbf{w}_n$ of $\mathbb{R}^n$. A vector $\mathbf{x}$ (standard coordinates) has coordinates $\mathbf{c}$ in the new basis exactly when
$$\mathbf{x}=W\mathbf{c},\qquad \mathbf{c}=W^{-1}\mathbf{x}.$$
If the basis is orthonormal, $\mathbf{c}=W^{\mathsf T}\mathbf{x}$, i.e. $c_i=\mathbf{w}_i^{\mathsf T}\mathbf{x}$.

:::

::: {.proof}

1. $\mathbf{x}=c_1\mathbf{w}_1+\dots+c_n\mathbf{w}_n=W\mathbf{c}$ by @def-matrix-times-vector; $W$ is invertible, so $\mathbf{c}=W^{-1}\mathbf{x}$.

2. For orthonormal columns $W^{-1}=W^{\mathsf T}$ (@def-orthogonal-matrix).

:::

::: {#fig-change-of-basis-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.0]
\foreach \a in {0,1,2} \draw[faint] ({2*\a},{0.5*\a}) -- ({2*\a+1},{0.5*\a+3});
\foreach \b in {0,1,2} \draw[faint] ({0.5*\b},{1.5*\b}) -- ({0.5*\b+4},{1.5*\b+1});
\draw[->] (-0.4,0) -- (5.2,0); \draw[->] (0,-0.4) -- (0,3.6);
\draw[dashed] (3,0.75) -- (3.5,2.25) -- (0.5,1.5);
\draw[->, emph, primary] (0,0) -- (2,0.5) node[lab, below right] {$\mathbf w_1$};
\draw[->, emph, primary] (0,0) -- (0.5,1.5) node[lab, left] {$\mathbf w_2$};
\draw[->, hl] (0,0) -- (3.5,2.25) node[lab, above right] {$\mathbf x=1.5\,\mathbf w_1+\mathbf w_2$};
\end{tikzpicture}
\end{center}
```

One vector, two coordinate systems. In the basis $\mathbf w_1,\mathbf w_2$ (grid lines) the vector $\mathbf x$ has coordinates $\mathbf c=(1.5,1)$, since $\mathbf x=W\mathbf c$; its standard coordinates are the entries of $\mathbf x$ itself.

:::

::: {#thm-change-of-basis-similar .theorem name="Change of basis gives a similar matrix"}

If a linear transformation $T:\mathbb{R}^n\to\mathbb{R}^n$ has matrix $A$ in one basis and $B$ in another, and $M$ converts coordinates in the second basis to coordinates in the first, then
$$B=M^{-1}AM.$$
In particular $A$ and $B$ are similar (@def-similar-matrices) and share their eigenvalues.

:::

::: {.proof}

1. Start with second-basis coordinates $\mathbf{d}$. Then $M\mathbf{d}$ are the first-basis coordinates of the same vector.

2. Applying $T$ in the first basis gives $AM\mathbf{d}$, and converting back gives $M^{-1}AM\mathbf{d}$.

3. These are the second-basis coordinates of $T(\mathbf{v})$, which by @thm-matrix-represents-transformation are also $B\mathbf{d}$. Since $\mathbf{d}$ is arbitrary, $B=M^{-1}AM$.

:::

Choosing the eigenvectors as the basis gives $B=\Lambda$, as in @exm-matrix-of-projection. Choosing $\mathbf{v}$'s for the input and $\mathbf{u}$'s for the output, from the SVD (@thm-svd), gives the diagonal matrix $\Sigma$ even for rectangular $A$.

## Compression

An image of $512\times512$ grey pixels is a vector with $512^2$ components in the standard basis. Compression changes to a basis in which most coordinates are small, and throws those away.

::: {#def-good-basis-for-compression .definition name="What makes a basis good for compression"}

A basis is useful for compression if (1) coordinates are fast to compute, for example by an FFT-like algorithm or because the basis is orthogonal; and (2) a few basis vectors are enough to approximate typical signals well.

:::

::: {#exm-haar-basis .example name="A Haar-type basis in R^4"}

The orthogonal vectors
$$(1,1,1,1),\quad(1,1,-1,-1),\quad(1,-1,0,0),\quad(0,0,1,-1)$$
measure an average, a coarse difference and two fine differences. For the smooth signal $\mathbf{x}=(4,4,3,3)$ the coordinates are $c_i=\mathbf{w}_i^{\mathsf T}\mathbf{x}/\mathbf{w}_i^{\mathsf T}\mathbf{w}_i$:
$$\mathbf{c}=\big(\tfrac{14}4,\tfrac24,0,0\big)=(3.5,0.5,0,0).$$
Two of the four coefficients are zero, so storing two numbers recovers $\mathbf{x}$ exactly. The Fourier basis (@def-fourier-matrix) and wavelet bases do the same on a large scale (JPEG uses $8\times8$ cosine bases).

:::
