---
title: "Eigenvalue Algorithms Must Iterate; Hessenberg Reduction"
sources: [mit18335-15]
requires: [math/numerical/eigenvalue-algorithms/schur-factorization]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 15 (companion matrices, ill-conditioning, Hessenberg factorization) and the note on introducing zeros by similarity transformations, in our own wording; proofs written out in steps; the perturbed roots were computed with mpmath at 40 digits. -->

No finite sequence of arithmetic operations and root extractions computes the eigenvalues of a general matrix, so eigenvalue algorithms are iterative. Before iterating, a finite *direct* phase reduces $A$ by unitary similarity to Hessenberg form, which makes each later iteration cheap.

::: {#def-companion-matrix .definition name="Companion matrix"}

For a monic polynomial $p(z)=z^m+a_{m-1}z^{m-1}+\dots+a_1z+a_0$, the *companion matrix* is
$$C_p=\begin{bmatrix}0&&&&-a_0\\1&0&&&-a_1\\&1&\ddots&&\vdots\\&&\ddots&0&-a_{m-2}\\&&&1&-a_{m-1}\end{bmatrix}.$$

:::

::: {#prp-companion-characteristic-polynomial .proposition name="Every polynomial is a characteristic polynomial"}

$\det(zI-C_p)=p(z)$, so the roots of $p$ are the eigenvalues of $C_p$. Consequently, for $m\ge5$ there is no algorithm that computes the eigenvalues of every $m\times m$ matrix exactly in finitely many arithmetic operations and $k$-th roots.

:::

::: {.proof}

1. Expand $\det(zI-C_p)$ along the last column. The entry in row $i$ of that column is $a_{i-1}$ for $i<m$ and $z+a_{m-1}$ for $i=m$.

2. Deleting row $i$ and the last column leaves a block matrix whose upper-left $(i-1)\times(i-1)$ block is lower bidiagonal with $z$ on the diagonal and whose lower-right block is upper bidiagonal with $-1$ on the diagonal; its determinant is $z^{i-1}(-1)^{m-i}$.

3. With the cofactor sign $(-1)^{i+m}$ the term for row $i$ is $a_{i-1}z^{i-1}$ (and $(z+a_{m-1})z^{m-1}$ for $i=m$). Summing gives $p(z)$.

4. An exact finite algorithm for eigenvalues would, applied to $C_p$, give a formula in radicals for the roots of every polynomial of degree $m$, which Abel and Ruffini showed does not exist for $m\ge5$.

:::

::: {#prp-root-conditioning .proposition name="Conditioning of a polynomial root"}

Let $\xi$ be a simple root of $p(z)=\sum_ia_iz^i$. If the single coefficient $a_i$ is perturbed to $a_i(1+\epsilon)$, the root moves to first order by $\delta\xi=-\epsilon a_i\xi^i/p'(\xi)$, so the relative condition number of $\xi$ with respect to $a_i$ is
$$\kappa=\frac{\lvert a_i\xi^{i-1}\rvert}{\lvert p'(\xi)\rvert}.$$

:::

::: {.proof}

1. The perturbed root satisfies $p(\xi+\delta\xi)+\epsilon a_i(\xi+\delta\xi)^i=0$.

2. Expanding to first order and using $p(\xi)=0$: $p'(\xi)\delta\xi+\epsilon a_i\xi^i=0$.

3. Hence $\delta\xi=-\epsilon a_i\xi^i/p'(\xi)$, and $\dfrac{\lvert\delta\xi\rvert/\lvert\xi\rvert}{\lvert\epsilon\rvert}=\dfrac{\lvert a_i\xi^{i-1}\rvert}{\lvert p'(\xi)\rvert}$.

:::

::: {#exm-wilkinson-polynomial .example name="Wilkinson's polynomial"}

For $p(z)=\prod_{k=1}^{20}(z-k)$ the coefficient of $z^{15}$ is about $-1.67\times10^{9}$, and at $\xi=15$, $\lvert p'(15)\rvert=14!\,5!\approx1.05\times10^{13}$. By @prp-root-conditioning the root $15$ has condition number about $1.67\times10^9\cdot15^{14}/1.05\times10^{13}\approx4.7\times10^{12}$ with respect to that one coefficient. Perturbing all coefficients by random relative amounts of size $10^{-10}$ moves the larger roots by order one, and many become complex pairs.

:::

::: {#fig-hessenberg-reduction-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=0.5cm]
\draw[->, faint] (-0.5,0) -- (23.5,0) node[lab, right] {$\operatorname{Re}z$};
\draw[->, faint] (0,-5.8) -- (0,6.2) node[lab, above] {$\operatorname{Im}z$};
\foreach \x in {5,10,15,20} {\draw[faint] (\x,-0.15) -- (\x,0.15); \node[tick, below] at (\x,-0.15) {$\x$};}
\foreach \y in {-4,4} {\draw[faint] (-0.15,\y) -- (0.15,\y); \node[tick, left] at (-0.15,\y) {$\y$};}
\foreach \k in {1,...,20} {\node[tick, text=accent] at (\k,0) {$\times$};}
\fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (4.01,0.00) circle (1.6pt); \fill (4.97,0.00) circle (1.6pt); \fill (5.79,0.00) circle (1.6pt); \fill (20.69,-0.67) circle (1.6pt); \fill (20.69,0.67) circle (1.6pt); \fill (6.57,-1.10) circle (1.6pt); \fill (6.57,1.10) circle (1.6pt); \fill (8.16,2.43) circle (1.6pt); \fill (8.16,-2.43) circle (1.6pt); \fill (19.43,2.97) circle (1.6pt); \fill (19.43,-2.97) circle (1.6pt); \fill (10.30,-3.66) circle (1.6pt); \fill (10.30,3.66) circle (1.6pt); \fill (16.40,-4.47) circle (1.6pt); \fill (16.40,4.47) circle (1.6pt); \fill (13.07,-4.52) circle (1.6pt); \fill (13.07,4.52) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (4.00,0.00) circle (1.6pt); \fill (5.13,0.00) circle (1.6pt); \fill (5.43,0.00) circle (1.6pt); \fill (6.59,-1.27) circle (1.6pt); \fill (6.59,1.27) circle (1.6pt); \fill (21.47,-1.40) circle (1.6pt); \fill (21.47,1.40) circle (1.6pt); \fill (8.19,-2.47) circle (1.6pt); \fill (8.19,2.47) circle (1.6pt); \fill (10.22,3.64) circle (1.6pt); \fill (10.22,-3.64) circle (1.6pt); \fill (19.32,3.73) circle (1.6pt); \fill (19.32,-3.73) circle (1.6pt); \fill (12.86,-4.59) circle (1.6pt); \fill (12.86,4.59) circle (1.6pt); \fill (16.08,4.80) circle (1.6pt); \fill (16.08,-4.80) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (4.00,0.00) circle (1.6pt); \fill (5.08,0.00) circle (1.6pt); \fill (5.58,0.00) circle (1.6pt); \fill (6.69,1.15) circle (1.6pt); \fill (6.69,-1.15) circle (1.6pt); \fill (21.81,1.64) circle (1.6pt); \fill (21.81,-1.64) circle (1.6pt); \fill (8.28,2.31) circle (1.6pt); \fill (8.28,-2.31) circle (1.6pt); \fill (10.26,-3.37) circle (1.6pt); \fill (10.26,3.37) circle (1.6pt); \fill (19.26,-4.13) circle (1.6pt); \fill (19.26,4.13) circle (1.6pt); \fill (12.62,-4.36) circle (1.6pt); \fill (12.62,4.36) circle (1.6pt); \fill (15.75,4.92) circle (1.6pt); \fill (15.75,-4.92) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (3.99,0.00) circle (1.6pt); \fill (5.05,0.00) circle (1.6pt); \fill (16.92,0.00) circle (1.6pt); \fill (5.96,0.42) circle (1.6pt); \fill (5.96,-0.42) circle (1.6pt); \fill (21.30,-1.52) circle (1.6pt); \fill (21.30,1.52) circle (1.6pt); \fill (7.25,-1.83) circle (1.6pt); \fill (7.25,1.83) circle (1.6pt); \fill (9.16,3.16) circle (1.6pt); \fill (9.16,-3.16) circle (1.6pt); \fill (18.63,3.85) circle (1.6pt); \fill (18.63,-3.85) circle (1.6pt); \fill (11.72,4.26) circle (1.6pt); \fill (11.72,-4.26) circle (1.6pt); \fill (15.00,4.69) circle (1.6pt); \fill (15.00,-4.69) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (3.99,0.00) circle (1.6pt); \fill (5.16,-0.34) circle (1.6pt); \fill (5.16,0.34) circle (1.6pt); \fill (20.97,0.85) circle (1.6pt); \fill (20.97,-0.85) circle (1.6pt); \fill (6.40,1.49) circle (1.6pt); \fill (6.40,-1.49) circle (1.6pt); \fill (8.00,-2.79) circle (1.6pt); \fill (8.00,2.79) circle (1.6pt); \fill (19.64,-3.24) circle (1.6pt); \fill (19.64,3.24) circle (1.6pt); \fill (10.19,-4.07) circle (1.6pt); \fill (10.19,4.07) circle (1.6pt); \fill (16.54,4.85) circle (1.6pt); \fill (16.54,-4.85) circle (1.6pt); \fill (13.10,4.97) circle (1.6pt); \fill (13.10,-4.97) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (4.01,0.00) circle (1.6pt); \fill (4.83,0.00) circle (1.6pt); \fill (21.22,0.00) circle (1.6pt); \fill (5.85,-0.89) circle (1.6pt); \fill (5.85,0.89) circle (1.6pt); \fill (7.42,-2.04) circle (1.6pt); \fill (7.42,2.04) circle (1.6pt); \fill (20.40,-2.22) circle (1.6pt); \fill (20.40,2.22) circle (1.6pt); \fill (9.39,3.07) circle (1.6pt); \fill (9.39,-3.07) circle (1.6pt); \fill (11.64,-3.93) circle (1.6pt); \fill (11.64,3.93) circle (1.6pt); \fill (17.80,-4.10) circle (1.6pt); \fill (17.80,4.10) circle (1.6pt); \fill (14.48,4.55) circle (1.6pt); \fill (14.48,-4.55) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (4.00,0.00) circle (1.6pt); \fill (4.97,0.00) circle (1.6pt); \fill (21.56,0.00) circle (1.6pt); \fill (6.16,-0.43) circle (1.6pt); \fill (6.16,0.43) circle (1.6pt); \fill (7.57,-1.47) circle (1.6pt); \fill (7.57,1.47) circle (1.6pt); \fill (20.36,-2.53) circle (1.6pt); \fill (20.36,2.53) circle (1.6pt); \fill (9.23,2.64) circle (1.6pt); \fill (9.23,-2.64) circle (1.6pt); \fill (11.48,-3.79) circle (1.6pt); \fill (11.48,3.79) circle (1.6pt); \fill (17.57,-4.11) circle (1.6pt); \fill (17.57,4.11) circle (1.6pt); \fill (14.37,4.43) circle (1.6pt); \fill (14.37,-4.43) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (4.00,0.00) circle (1.6pt); \fill (5.11,0.00) circle (1.6pt); \fill (5.51,0.00) circle (1.6pt); \fill (21.05,-1.12) circle (1.6pt); \fill (21.05,1.12) circle (1.6pt); \fill (6.70,-1.20) circle (1.6pt); \fill (6.70,1.20) circle (1.6pt); \fill (8.35,2.29) circle (1.6pt); \fill (8.35,-2.29) circle (1.6pt); \fill (19.25,3.30) circle (1.6pt); \fill (19.25,-3.30) circle (1.6pt); \fill (10.31,-3.38) circle (1.6pt); \fill (10.31,3.38) circle (1.6pt); \fill (12.90,4.35) circle (1.6pt); \fill (12.90,-4.35) circle (1.6pt); \fill (16.14,-4.50) circle (1.6pt); \fill (16.14,4.50) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (3.99,0.00) circle (1.6pt); \fill (9.01,0.00) circle (1.6pt); \fill (22.38,0.00) circle (1.6pt); \fill (5.26,-0.22) circle (1.6pt); \fill (5.26,0.22) circle (1.6pt); \fill (6.80,1.33) circle (1.6pt); \fill (6.80,-1.33) circle (1.6pt); \fill (8.66,-2.64) circle (1.6pt); \fill (8.66,2.64) circle (1.6pt); \fill (21.00,-3.21) circle (1.6pt); \fill (21.00,3.21) circle (1.6pt); \fill (10.94,-4.10) circle (1.6pt); \fill (10.94,4.10) circle (1.6pt); \fill (17.67,-5.07) circle (1.6pt); \fill (17.67,5.07) circle (1.6pt); \fill (13.98,-5.16) circle (1.6pt); \fill (13.98,5.16) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (3.99,0.00) circle (1.6pt); \fill (5.17,-0.31) circle (1.6pt); \fill (5.17,0.31) circle (1.6pt); \fill (6.44,-1.48) circle (1.6pt); \fill (6.44,1.48) circle (1.6pt); \fill (21.51,1.49) circle (1.6pt); \fill (21.51,-1.49) circle (1.6pt); \fill (8.11,-2.75) circle (1.6pt); \fill (8.11,2.75) circle (1.6pt); \fill (19.17,-3.73) circle (1.6pt); \fill (19.17,3.73) circle (1.6pt); \fill (10.35,-3.93) circle (1.6pt); \fill (10.35,3.93) circle (1.6pt); \fill (16.11,-4.57) circle (1.6pt); \fill (16.11,4.57) circle (1.6pt); \fill (13.14,4.60) circle (1.6pt); \fill (13.14,-4.60) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (3.99,0.00) circle (1.6pt); \fill (5.15,0.00) circle (1.6pt); \fill (5.54,0.00) circle (1.6pt); \fill (6.96,0.00) circle (1.6pt); \fill (21.87,0.00) circle (1.6pt); \fill (7.14,-1.48) circle (1.6pt); \fill (7.14,1.48) circle (1.6pt); \fill (20.79,-2.76) circle (1.6pt); \fill (20.79,2.76) circle (1.6pt); \fill (8.90,-2.95) circle (1.6pt); \fill (8.90,2.95) circle (1.6pt); \fill (11.24,-4.27) circle (1.6pt); \fill (11.24,4.27) circle (1.6pt); \fill (17.86,4.70) circle (1.6pt); \fill (17.86,-4.70) circle (1.6pt); \fill (14.31,5.08) circle (1.6pt); \fill (14.31,-5.08) circle (1.6pt); \fill (1.00,0.00) circle (1.6pt); \fill (2.00,0.00) circle (1.6pt); \fill (3.00,0.00) circle (1.6pt); \fill (4.00,0.00) circle (1.6pt); \fill (5.00,0.00) circle (1.6pt); \fill (21.75,0.00) circle (1.6pt); \fill (6.14,-0.27) circle (1.6pt); \fill (6.14,0.27) circle (1.6pt); \fill (7.31,-1.56) circle (1.6pt); \fill (7.31,1.56) circle (1.6pt); \fill (20.57,-2.66) circle (1.6pt); \fill (20.57,2.66) circle (1.6pt); \fill (9.03,2.95) circle (1.6pt); \fill (9.03,-2.95) circle (1.6pt); \fill (11.40,-4.16) circle (1.6pt); \fill (11.40,4.16) circle (1.6pt); \fill (17.76,-4.39) circle (1.6pt); \fill (17.76,4.39) circle (1.6pt); \fill (14.42,-4.81) circle (1.6pt); \fill (14.42,4.81) circle (1.6pt);
\end{tikzpicture}
\end{center}
```

Roots of Wilkinson's polynomial after each coefficient is multiplied by $1+10^{-10}g$ with $g$ standard normal, twelve independent trials (dots), against the exact roots $1,\dots,20$ (crosses on the axis). The small roots stay put; roots near $10$–$20$ scatter far into the complex plane. Computing eigenvalues via the characteristic polynomial would inherit this sensitivity.

:::

::: {#rmk-hessenberg-reduction-1 .remark name="Why not triangularize directly"}

A Householder reflector $Q_1^{\mathsf H}$ applied on the left can zero column $1$ below the diagonal, but the similarity also multiplies by $Q_1$ on the right, which recombines all columns and destroys those zeros. If instead $Q_1^{\mathsf H}$ only touches rows $2,\dots,m$, chosen to zero column $1$ below the *subdiagonal*, then multiplication by $Q_1$ on the right only combines columns $2,\dots,m$ and leaves column $1$ alone. Aiming one row lower makes the zeros survive.

:::

::: {#def-hessenberg-reduction .definition name="Hessenberg reduction"}

A matrix $H$ is *upper Hessenberg* if $h_{ij}=0$ for $i>j+1$. The *Hessenberg reduction* of $A\in\mathbb{C}^{m\times m}$ applies, for $k=1,\dots,m-2$, the Householder reflector $F_k$ that zeros entries $k+2,\dots,m$ of column $k$, on both sides:
$$A\gets Q_k^{\mathsf H}AQ_k,\qquad Q_k=\begin{bmatrix}I_k&0\\0&F_k\end{bmatrix}.$$
The result is $H=Q^{\mathsf H}AQ$ with $Q=Q_1\cdots Q_{m-2}$ unitary and $H$ upper Hessenberg, similar to $A$. If $A$ is Hermitian, so is $H$, and therefore $H$ is tridiagonal.

:::

```{=latex}
\begin{algorithm}
\caption{Householder reduction to Hessenberg form}
\begin{algorithmic}
\INPUT $A\in\mathbb{C}^{m\times m}$, overwritten by $H$
\FOR{$k=1,\dots,m-2$}
    \STATE $\mathbf{x}\gets A_{k+1:m,\,k}$
    \STATE $\mathbf{v}_k\gets\mathbf{x}+\operatorname{sign}(x_1)\lVert\mathbf{x}\rVert\mathbf{e}_1$; \quad $\mathbf{v}_k\gets\mathbf{v}_k/\lVert\mathbf{v}_k\rVert$
    \STATE $A_{k+1:m,\,k:m}\gets A_{k+1:m,\,k:m}-2\mathbf{v}_k\bigl(\mathbf{v}_k^{\mathsf H}A_{k+1:m,\,k:m}\bigr)$ \COMMENT{left}
    \STATE $A_{1:m,\,k+1:m}\gets A_{1:m,\,k+1:m}-2\bigl(A_{1:m,\,k+1:m}\mathbf{v}_k\bigr)\mathbf{v}_k^{\mathsf H}$ \COMMENT{right}
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#fig-hessenberg-reduction-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.04,0.05) -- (-0.10,0.05) -- (-0.10,-1.75) -- (-0.04,-1.75);
\draw[faint] (1.74,0.05) -- (1.80,0.05) -- (1.80,-1.75) -- (1.74,-1.75);
\node[tick] at (0.17,-0.17) {$\times$};
\node[tick] at (0.51,-0.17) {$\times$};
\node[tick] at (0.85,-0.17) {$\times$};
\node[tick] at (1.19,-0.17) {$\times$};
\node[tick] at (1.53,-0.17) {$\times$};
\node[tick] at (0.17,-0.51) {$\times$};
\node[tick] at (0.51,-0.51) {$\times$};
\node[tick] at (0.85,-0.51) {$\times$};
\node[tick] at (1.19,-0.51) {$\times$};
\node[tick] at (1.53,-0.51) {$\times$};
\node[tick] at (0.17,-0.85) {$\times$};
\node[tick] at (0.51,-0.85) {$\times$};
\node[tick] at (0.85,-0.85) {$\times$};
\node[tick] at (1.19,-0.85) {$\times$};
\node[tick] at (1.53,-0.85) {$\times$};
\node[tick] at (0.17,-1.19) {$\times$};
\node[tick] at (0.51,-1.19) {$\times$};
\node[tick] at (0.85,-1.19) {$\times$};
\node[tick] at (1.19,-1.19) {$\times$};
\node[tick] at (1.53,-1.19) {$\times$};
\node[tick] at (0.17,-1.53) {$\times$};
\node[tick] at (0.51,-1.53) {$\times$};
\node[tick] at (0.85,-1.53) {$\times$};
\node[tick] at (1.19,-1.53) {$\times$};
\node[tick] at (1.53,-1.53) {$\times$};
\node[note] at (0.85,-2.05) {$A$};
\draw[map] (1.85,-0.85) -- (2.30,-0.85);
\draw[faint] (2.41,0.05) -- (2.35,0.05) -- (2.35,-1.75) -- (2.41,-1.75);
\draw[faint] (4.19,0.05) -- (4.25,0.05) -- (4.25,-1.75) -- (4.19,-1.75);
\node[tick] at (2.62,-0.17) {$\times$};
\fill[accentLight] (2.81,-0.32) rectangle (3.11,-0.02);
\node[tick] at (2.96,-0.17) {$\times$};
\fill[accentLight] (3.15,-0.32) rectangle (3.45,-0.02);
\node[tick] at (3.30,-0.17) {$\times$};
\fill[accentLight] (3.49,-0.32) rectangle (3.79,-0.02);
\node[tick] at (3.64,-0.17) {$\times$};
\fill[accentLight] (3.83,-0.32) rectangle (4.13,-0.02);
\node[tick] at (3.98,-0.17) {$\times$};
\fill[accentLight] (2.47,-0.66) rectangle (2.77,-0.36);
\node[tick] at (2.62,-0.51) {$\times$};
\fill[accentLight] (2.81,-0.66) rectangle (3.11,-0.36);
\node[tick] at (2.96,-0.51) {$\times$};
\fill[accentLight] (3.15,-0.66) rectangle (3.45,-0.36);
\node[tick] at (3.30,-0.51) {$\times$};
\fill[accentLight] (3.49,-0.66) rectangle (3.79,-0.36);
\node[tick] at (3.64,-0.51) {$\times$};
\fill[accentLight] (3.83,-0.66) rectangle (4.13,-0.36);
\node[tick] at (3.98,-0.51) {$\times$};
\node[tick, text=rule] at (2.62,-0.85) {$0$};
\fill[accentLight] (2.81,-1.00) rectangle (3.11,-0.70);
\node[tick] at (2.96,-0.85) {$\times$};
\fill[accentLight] (3.15,-1.00) rectangle (3.45,-0.70);
\node[tick] at (3.30,-0.85) {$\times$};
\fill[accentLight] (3.49,-1.00) rectangle (3.79,-0.70);
\node[tick] at (3.64,-0.85) {$\times$};
\fill[accentLight] (3.83,-1.00) rectangle (4.13,-0.70);
\node[tick] at (3.98,-0.85) {$\times$};
\node[tick, text=rule] at (2.62,-1.19) {$0$};
\fill[accentLight] (2.81,-1.34) rectangle (3.11,-1.04);
\node[tick] at (2.96,-1.19) {$\times$};
\fill[accentLight] (3.15,-1.34) rectangle (3.45,-1.04);
\node[tick] at (3.30,-1.19) {$\times$};
\fill[accentLight] (3.49,-1.34) rectangle (3.79,-1.04);
\node[tick] at (3.64,-1.19) {$\times$};
\fill[accentLight] (3.83,-1.34) rectangle (4.13,-1.04);
\node[tick] at (3.98,-1.19) {$\times$};
\node[tick, text=rule] at (2.62,-1.53) {$0$};
\fill[accentLight] (2.81,-1.68) rectangle (3.11,-1.38);
\node[tick] at (2.96,-1.53) {$\times$};
\fill[accentLight] (3.15,-1.68) rectangle (3.45,-1.38);
\node[tick] at (3.30,-1.53) {$\times$};
\fill[accentLight] (3.49,-1.68) rectangle (3.79,-1.38);
\node[tick] at (3.64,-1.53) {$\times$};
\fill[accentLight] (3.83,-1.68) rectangle (4.13,-1.38);
\node[tick] at (3.98,-1.53) {$\times$};
\node[note] at (3.30,-2.05) {$Q_1^{\mathsf H}AQ_1$};
\draw[map] (4.30,-0.85) -- (4.75,-0.85);
\draw[faint] (4.86,0.05) -- (4.80,0.05) -- (4.80,-1.75) -- (4.86,-1.75);
\draw[faint] (6.64,0.05) -- (6.70,0.05) -- (6.70,-1.75) -- (6.64,-1.75);
\node[tick] at (5.07,-0.17) {$\times$};
\node[tick] at (5.41,-0.17) {$\times$};
\fill[accentLight] (5.60,-0.32) rectangle (5.90,-0.02);
\node[tick] at (5.75,-0.17) {$\times$};
\fill[accentLight] (5.94,-0.32) rectangle (6.24,-0.02);
\node[tick] at (6.09,-0.17) {$\times$};
\fill[accentLight] (6.28,-0.32) rectangle (6.58,-0.02);
\node[tick] at (6.43,-0.17) {$\times$};
\node[tick] at (5.07,-0.51) {$\times$};
\node[tick] at (5.41,-0.51) {$\times$};
\fill[accentLight] (5.60,-0.66) rectangle (5.90,-0.36);
\node[tick] at (5.75,-0.51) {$\times$};
\fill[accentLight] (5.94,-0.66) rectangle (6.24,-0.36);
\node[tick] at (6.09,-0.51) {$\times$};
\fill[accentLight] (6.28,-0.66) rectangle (6.58,-0.36);
\node[tick] at (6.43,-0.51) {$\times$};
\fill[accentLight] (5.26,-1.00) rectangle (5.56,-0.70);
\node[tick] at (5.41,-0.85) {$\times$};
\fill[accentLight] (5.60,-1.00) rectangle (5.90,-0.70);
\node[tick] at (5.75,-0.85) {$\times$};
\fill[accentLight] (5.94,-1.00) rectangle (6.24,-0.70);
\node[tick] at (6.09,-0.85) {$\times$};
\fill[accentLight] (6.28,-1.00) rectangle (6.58,-0.70);
\node[tick] at (6.43,-0.85) {$\times$};
\node[tick, text=rule] at (5.41,-1.19) {$0$};
\fill[accentLight] (5.60,-1.34) rectangle (5.90,-1.04);
\node[tick] at (5.75,-1.19) {$\times$};
\fill[accentLight] (5.94,-1.34) rectangle (6.24,-1.04);
\node[tick] at (6.09,-1.19) {$\times$};
\fill[accentLight] (6.28,-1.34) rectangle (6.58,-1.04);
\node[tick] at (6.43,-1.19) {$\times$};
\node[tick, text=rule] at (5.41,-1.53) {$0$};
\fill[accentLight] (5.60,-1.68) rectangle (5.90,-1.38);
\node[tick] at (5.75,-1.53) {$\times$};
\fill[accentLight] (5.94,-1.68) rectangle (6.24,-1.38);
\node[tick] at (6.09,-1.53) {$\times$};
\fill[accentLight] (6.28,-1.68) rectangle (6.58,-1.38);
\node[tick] at (6.43,-1.53) {$\times$};
\node[note] at (5.75,-2.05) {step 2};
\draw[map] (6.75,-0.85) -- (7.20,-0.85);
\draw[faint] (7.31,0.05) -- (7.25,0.05) -- (7.25,-1.75) -- (7.31,-1.75);
\draw[faint] (9.09,0.05) -- (9.15,0.05) -- (9.15,-1.75) -- (9.09,-1.75);
\node[tick] at (7.52,-0.17) {$\times$};
\node[tick] at (7.86,-0.17) {$\times$};
\node[tick] at (8.20,-0.17) {$\times$};
\fill[accentLight] (8.39,-0.32) rectangle (8.69,-0.02);
\node[tick] at (8.54,-0.17) {$\times$};
\fill[accentLight] (8.73,-0.32) rectangle (9.03,-0.02);
\node[tick] at (8.88,-0.17) {$\times$};
\node[tick] at (7.52,-0.51) {$\times$};
\node[tick] at (7.86,-0.51) {$\times$};
\node[tick] at (8.20,-0.51) {$\times$};
\fill[accentLight] (8.39,-0.66) rectangle (8.69,-0.36);
\node[tick] at (8.54,-0.51) {$\times$};
\fill[accentLight] (8.73,-0.66) rectangle (9.03,-0.36);
\node[tick] at (8.88,-0.51) {$\times$};
\node[tick] at (7.86,-0.85) {$\times$};
\node[tick] at (8.20,-0.85) {$\times$};
\fill[accentLight] (8.39,-1.00) rectangle (8.69,-0.70);
\node[tick] at (8.54,-0.85) {$\times$};
\fill[accentLight] (8.73,-1.00) rectangle (9.03,-0.70);
\node[tick] at (8.88,-0.85) {$\times$};
\fill[accentLight] (8.05,-1.34) rectangle (8.35,-1.04);
\node[tick] at (8.20,-1.19) {$\times$};
\fill[accentLight] (8.39,-1.34) rectangle (8.69,-1.04);
\node[tick] at (8.54,-1.19) {$\times$};
\fill[accentLight] (8.73,-1.34) rectangle (9.03,-1.04);
\node[tick] at (8.88,-1.19) {$\times$};
\node[tick, text=rule] at (8.20,-1.53) {$0$};
\fill[accentLight] (8.39,-1.68) rectangle (8.69,-1.38);
\node[tick] at (8.54,-1.53) {$\times$};
\fill[accentLight] (8.73,-1.68) rectangle (9.03,-1.38);
\node[tick] at (8.88,-1.53) {$\times$};
\node[note] at (8.20,-2.05) {$H$};
\end{tikzpicture}
\end{center}
```

Hessenberg reduction of a $5\times5$ matrix. Each step applies $Q_k^{\mathsf H}$ to rows $k+1,\dots,5$ (zeroing column $k$ below the subdiagonal) and $Q_k$ to columns $k+1,\dots,5$; the shaded entries are those changed by step $k$, and the zeros made earlier are untouched.

:::

::: {#thm-hessenberg-reduction-cost .theorem name="Cost and stability of Hessenberg reduction"}

Hessenberg reduction takes $\sim\tfrac{10}3m^3$ flops ($\sim\tfrac43m^3$ for tridiagonal reduction of a Hermitian matrix, exploiting symmetry), and it is backward stable: the computed $\tilde H$ satisfies $\tilde Q\tilde H\tilde Q^{\mathsf H}=A+\delta A$ with $\lVert\delta A\rVert/\lVert A\rVert=O(\varepsilon_{\text{mach}})$ for an exactly unitary $\tilde Q$.

:::

::: {.proof}

1. *Left multiplications.* Step $k$ updates an $(m-k)\times(m-k+1)$ block at $4$ flops per entry, the same work as step $k$ of Householder QR on an $m\times m$ matrix: $\sum_k4(m-k)^2\approx\tfrac43m^3$.

2. *Right multiplications.* Step $k$ updates an $m\times(m-k)$ block at $4$ flops per entry: $\sum_k4m(m-k)\approx2m^3$. The total is $\tfrac43m^3+2m^3=\tfrac{10}3m^3$.

3. *Hermitian case.* The trailing block stays Hermitian, so only its lower triangle need be updated, and the update can be organised as a symmetric rank-two update $B\gets B-\mathbf{v}\mathbf{w}^{\mathsf H}-\mathbf{w}\mathbf{v}^{\mathsf H}$ costing $\sim4(m-k)^2$ flops; summing gives $\tfrac43m^3$.

4. *Stability.* Each step is a pair of reflector applications, each backward stable with an error that unitary factors do not amplify; pushing the errors back to the start as in @thm-householder-qr-backward-stable gives $\delta A$ with $\lVert\delta A\rVert=O(\varepsilon_{\text{mach}})\lVert A\rVert$.

:::

::: {#rmk-hessenberg-reduction-2 .remark name="The two phases"}

Standard eigenvalue software works in two phases: (I) a direct reduction to Hessenberg (or tridiagonal) form in $O(m^3)$ flops, and (II) an iteration that converges to Schur (or diagonal) form. Hessenberg form is preserved by the QR algorithm (@sec-math-numerical-eigenvalue-algorithms-qr-algorithm), and a QR step on a Hessenberg matrix costs only $O(m^2)$ flops ($O(m)$ when tridiagonal), so phase II usually costs less than phase I.

:::
