---
title: "Triangular Form and the Cayley–Hamilton Theorem"
sources: [camib-la-6]
requires: [math/linear-algebra/endomorphisms/minimal-polynomial]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.3, in our own wording; examples ours (checked with sympy); proofs written out in steps. The course gives two proofs of Cayley-Hamilton, by triangular form over C and by the adjugate over any field; both are kept, in our wording. -->

::: {#def-triangulable .definition name="Triangulable endomorphism"}

$\alpha\in\operatorname{End}(V)$ is *triangulable* if some basis makes $[\alpha]$ upper triangular. Equivalently, there is a basis $v_1,\dots,v_n$ with $\alpha(v_j)\in\langle v_1,\dots,v_j\rangle$ for each $j$.

:::

::: {#thm-triangulable-iff-splits .theorem name="Triangulable means the characteristic polynomial splits"}

$\alpha$ is triangulable if and only if $\chi_\alpha(t)=\prod_{i=1}^n(t-\lambda_i)$ for some (not necessarily distinct) $\lambda_i\in F$. Over $\mathbb C$, every endomorphism is triangulable.

:::

::: {.proof}

1. If $[\alpha]$ is upper triangular with diagonal $\lambda_1,\dots,\lambda_n$, then $tI-[\alpha]$ is upper triangular too, and $\chi_\alpha=\prod(t-\lambda_i)$ by @lem-determinant-transpose.

2. Conversely, induct on $n$; $n=1$ is clear. As $\chi_\alpha(\lambda_1)=0$, $\lambda_1$ is an eigenvalue (@prp-eigenvalue-iff-root) with an eigenvector $v_1$. Extend to a basis $v_1,w_2,\dots,w_n$. In this basis
$$[\alpha]=\begin{bmatrix}\lambda_1&\ast\\0&C\end{bmatrix},\qquad \chi_\alpha(t)=(t-\lambda_1)\det(tI-C)$$
by @lem-block-triangular-determinant.

3. Cancelling $t-\lambda_1$ (polynomial division is unique), $\det(tI-C)=\prod_{i\ge2}(t-\lambda_i)$ splits. By induction there is $Q\in\operatorname{GL}_{n-1}(F)$ with $Q^{-1}CQ$ upper triangular.

4. With $P=\begin{bmatrix}1&0\\0&Q\end{bmatrix}$, $P^{-1}[\alpha]P=\begin{bmatrix}\lambda_1&\ast\\0&Q^{-1}CQ\end{bmatrix}$ is upper triangular.

5. Over $\mathbb C$ every polynomial splits (fundamental theorem of algebra).

:::

::: {#thm-cayley-hamilton .theorem name="Cayley–Hamilton theorem"}

Every endomorphism of a finite-dimensional vector space satisfies its characteristic polynomial:
$$\chi_\alpha(\alpha)=0.$$
Equivalently, $\chi_A(A)=0$ for every $A\in\operatorname{Mat}_n(F)$; so $m_\alpha$ divides $\chi_\alpha$ (@lem-minimal-polynomial-divides).

:::

::: {.proof}

First proof, over $\mathbb C$ (or whenever $\chi_\alpha$ splits).

1. By @thm-triangulable-iff-splits choose a basis $v_1,\dots,v_n$ in which $[\alpha]$ is upper triangular with diagonal $\lambda_1,\dots,\lambda_n$, and let $U_j=\langle v_1,\dots,v_j\rangle$, $U_0=\{0\}$. Then $(\alpha-\lambda_j\iota)U_j\subseteq U_{j-1}$: the $j$-th column has $\lambda_j$ on the diagonal and zeros below it.

2. Hence $(\alpha-\lambda_1\iota)\cdots(\alpha-\lambda_n\iota)V=(\alpha-\lambda_1\iota)\cdots(\alpha-\lambda_n\iota)U_n\subseteq U_0=\{0\}$, applying the factors from the right. That product is $\chi_\alpha(\alpha)$.

Second proof, over any field.

1. Let $A=[\alpha]$ and $B(t)=\operatorname{adj}(tI-A)$. Its entries are determinants of $(n-1)\times(n-1)$ submatrices, polynomials of degree $\le n-1$, so $B(t)=\sum_{k=0}^{n-1}B_kt^k$ with $B_k\in\operatorname{Mat}_n(F)$.

2. By @thm-adjugate, $(tI-A)B(t)=\chi_A(t)I$. Write $\chi_A(t)=\sum_{k=0}^nc_kt^k$ and compare coefficients of $t^k$ (both sides are polynomials with matrix coefficients): with $B_{-1}=B_n=0$,
$$B_{k-1}-AB_k=c_kI\qquad(0\le k\le n).$$

3. Multiply the $k$-th equation on the left by $A^k$ and add:
$$\sum_{k=0}^n\big(A^kB_{k-1}-A^{k+1}B_k\big)=\sum_{k=0}^nc_kA^k=\chi_A(A).$$

4. The left side telescopes: the term $A^{k+1}B_k$ subtracted at step $k$ is added back at step $k+1$, and the end terms $A^0B_{-1}$ and $A^{n+1}B_n$ are $0$. So $\chi_A(A)=0$.

:::

::: {#fig-cayley-hamilton-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] (u0) at (0.0,0) {$U_0$};
\node[lab] (u1) at (1.9,0) {$U_1$};
\node[lab] (u2) at (3.8,0) {$U_2$};
\node[lab] (u3) at (5.70,0) {$U_3$};
\draw[map] (u3) to[bend right=35] node[lab, tick, above] {$\alpha-\lambda_3\iota$} (u2);
\draw[map] (u2) to[bend right=35] node[lab, tick, above] {$\alpha-\lambda_2\iota$} (u1);
\draw[map] (u1) to[bend right=35] node[lab, tick, above] {$\alpha-\lambda_1\iota$} (u0);
\node[lab] at (0.95,0) {$\subset$};
\node[lab] at (2.85,0) {$\subset$};
\node[lab] at (4.75,0) {$\subset$};
\node[lab, below] at (2.85,-0.4) {$U_0=\{0\},\quad U_j=\langle v_1,\dots,v_j\rangle$};
\end{tikzpicture}
\end{center}
```

The first proof for $n=3$: in a triangular basis, $\alpha-\lambda_j\iota$ maps $U_j$ into $U_{j-1}$, so applying the three factors of $\chi_\alpha(\alpha)$ walks $V=U_3$ down to $\{0\}$.

:::

Substituting $t=A$ directly into "$\chi_A(t)=\det(tI-A)$" is not a proof: $\det(AI-A)=\det0$ is a scalar, while $\chi_A(A)$ is a matrix.

::: {#cor-minimal-and-characteristic-same-roots .corollary name="Same roots"}

$m_\alpha$ and $\chi_\alpha$ have the same roots in $F$, namely the eigenvalues of $\alpha$. For $\lambda\in F$: $\lambda$ is an eigenvalue $\iff$ $\chi_\alpha(\lambda)=0$ $\iff$ $m_\alpha(\lambda)=0$.

:::

::: {.proof}

1. Eigenvalue $\iff$ root of $\chi_\alpha$ is @prp-eigenvalue-iff-root.

2. Eigenvalues are roots of $m_\alpha$ by @prp-eigenvalue-root-of-minimal-polynomial.

3. A root of $m_\alpha$ is a root of $\chi_\alpha$, since $m_\alpha\mid\chi_\alpha$ by @thm-cayley-hamilton.

:::

::: {#exm-cayley-hamilton .example name="Inverse and powers from Cayley–Hamilton"}

$A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ has $\chi_A(t)=t^2-5t-2$, so $A^2=5A+2I$. Then $A(A-5I)=2I$ gives $A^{-1}=\frac12(A-5I)=\begin{bmatrix}-2&1\\\frac32&-\frac12\end{bmatrix}$, and every power of $A$ is a combination of $I$ and $A$: $A^3=5A^2+2A=27A+10I=\begin{bmatrix}37&54\\81&118\end{bmatrix}$.

:::
