---
title: "Eigenvalues and Eigenvectors"
sources: [mit1806-21]
requires: [math/linear-algebra/determinants/cramers-rule-and-volume]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 21, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-eigenvalue .definition name="Eigenvalue and eigenvector"}

Let $A$ be an $n\times n$ matrix. A nonzero vector $\mathbf{x}$ is an *eigenvector* of $A$ with *eigenvalue* $\lambda$ if
$$A\mathbf{x}=\lambda\mathbf{x}.$$
The eigenvectors for $\lambda$, together with $\mathbf{0}$, form the *eigenspace* $N(A-\lambda I)$.

:::

An eigenvector keeps its direction under $A$; the eigenvalue says how it is stretched, shrunk or reversed. Eigenvalue $0$ means $\mathbf{x}\in N(A)$, so $A$ is singular.

::: {#thm-characteristic-equation .theorem name="The characteristic equation"}

$\lambda$ is an eigenvalue of $A$ if and only if
$$\det(A-\lambda I)=0.$$
The left side is a polynomial of degree $n$ in $\lambda$ (the *characteristic polynomial*), so $A$ has exactly $n$ eigenvalues in $\mathbb{C}$, counted with multiplicity.

:::

::: {.proof}

1. $A\mathbf{x}=\lambda\mathbf{x}$ with $\mathbf{x}\neq\mathbf{0}$ means $(A-\lambda I)\mathbf{x}=\mathbf{0}$ has a nonzero solution, i.e. $A-\lambda I$ is singular.

2. By @thm-determinant-consequences (property 8) this happens exactly when $\det(A-\lambda I)=0$.

3. In the big formula (@thm-big-formula-determinant) the only term of degree $n$ comes from the diagonal: $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$, which has leading coefficient $(-1)^n$. By the fundamental theorem of algebra it has $n$ complex roots with multiplicity.

:::

::: {#fig-eigenvalues-and-eigenvectors-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x={(0.9cm,0)}]
\draw[->, muted] (-0.3,0) -- (6.6,0) node[right, lab, tick] {$\lambda$}; \draw[->, muted] (0,-1.2) -- (0,2.7);
\draw[emph, primary] (0.000,2.500) -- (0.079,2.364) -- (0.158,2.231) -- (0.236,2.101) -- (0.315,1.974) -- (0.394,1.850) -- (0.472,1.729) -- (0.551,1.611) -- (0.630,1.497) -- (0.709,1.385) -- (0.787,1.277) -- (0.866,1.172) -- (0.945,1.070) -- (1.024,0.970) -- (1.103,0.875) -- (1.181,0.782) -- (1.260,0.692) -- (1.339,0.605) -- (1.417,0.522) -- (1.496,0.441) -- (1.575,0.364) -- (1.654,0.290) -- (1.732,0.219) -- (1.811,0.150) -- (1.890,0.086) -- (1.969,0.024) -- (2.047,-0.035) -- (2.126,-0.091) -- (2.205,-0.143) -- (2.284,-0.193) -- (2.362,-0.239) -- (2.441,-0.282) -- (2.520,-0.322) -- (2.599,-0.359) -- (2.677,-0.393) -- (2.756,-0.424) -- (2.835,-0.452) -- (2.914,-0.477) -- (2.993,-0.498) -- (3.071,-0.517) -- (3.150,-0.532) -- (3.229,-0.544) -- (3.307,-0.553) -- (3.386,-0.559) -- (3.465,-0.562) -- (3.544,-0.562) -- (3.623,-0.559) -- (3.701,-0.552) -- (3.780,-0.543) -- (3.859,-0.530) -- (3.938,-0.515) -- (4.016,-0.496) -- (4.095,-0.474) -- (4.174,-0.449) -- (4.252,-0.421) -- (4.331,-0.390) -- (4.410,-0.355) -- (4.489,-0.318) -- (4.567,-0.278) -- (4.646,-0.234) -- (4.725,-0.187) -- (4.804,-0.138) -- (4.882,-0.085) -- (4.961,-0.029) -- (5.040,0.030) -- (5.119,0.093) -- (5.197,0.158) -- (5.276,0.226) -- (5.355,0.298) -- (5.434,0.372) -- (5.513,0.450) -- (5.591,0.531) -- (5.670,0.615) -- (5.749,0.702) -- (5.827,0.792) -- (5.906,0.885) -- (5.985,0.981) -- (6.064,1.081) -- (6.143,1.183) -- (6.221,1.289) -- (6.300,1.397);
\fill[accent] (2,0) circle[pt] node[below left, lab] {$2$}; \fill[accent] (5,0) circle[pt] node[below right, lab] {$5$};
\node[lab, note, primary, anchor=west] at (5.2,2.4) {$\det(A-\lambda I)=\lambda^2-7\lambda+10$};
\end{tikzpicture}
\end{center}
```

The characteristic polynomial of $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$ (@exm-eigenvalues-two-by-two), drawn at a quarter of its height. Its roots $2$ and $5$ are the values of $\lambda$ that make $A-\lambda I$ singular.

:::

::: {#thm-trace-determinant-eigenvalues .theorem name="Trace and determinant"}

If $A$ has eigenvalues $\lambda_1,\dots,\lambda_n$ (with multiplicity), then
$$\lambda_1+\dots+\lambda_n=\operatorname{tr}A=a_{11}+\dots+a_{nn},\qquad \lambda_1\lambda_2\cdots\lambda_n=\det A.$$

:::

::: {.proof}

1. Since the eigenvalues are the roots, $\det(A-\lambda I)=(\lambda_1-\lambda)\cdots(\lambda_n-\lambda)$.

2. Setting $\lambda=0$ gives $\det A=\lambda_1\cdots\lambda_n$.

3. Compare the coefficients of $\lambda^{n-1}$. On the right it is $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$. On the left, only the diagonal term of the big formula contributes to $\lambda^{n-1}$ (any other term omits at least two diagonal entries), giving $(-1)^{n-1}(a_{11}+\dots+a_{nn})$.

:::

::: {#exm-eigenvalues-two-by-two .example name="A 2 by 2 example"}

For $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$:
$$\det(A-\lambda I)=(4-\lambda)(3-\lambda)-2=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2).$$
So $\lambda_1=5$, $\lambda_2=2$; check: $5+2=7=\operatorname{tr}A$ and $5\cdot2=10=\det A$. The eigenvectors solve $(A-\lambda I)\mathbf{x}=\mathbf{0}$: $\mathbf{x}_1=(1,1)$ and $\mathbf{x}_2=(1,-2)$.

:::

::: {#fig-eigenvalues-and-eigenvectors-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.800,0) -- (2.400,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.800) -- (0,2.300) node[lab, above] {$y$};
\draw[->, emph] (0.000,0.000) -- (0.380,0.380);
\node[lab, left] at (0.380,0.380) {$\mathbf x_1$};
\draw[->, hl] (0.000,0.000) -- (1.900,1.900);
\node[lab, right] at (1.900,1.900) {$A\mathbf x=5\mathbf x$};
\draw[->, emph] (0.000,0.000) -- (0.380,-0.760);
\node[lab, left] at (0.380,-0.760) {$\mathbf x_2$};
\draw[->, hl] (0.000,0.000) -- (0.760,-1.520);
\node[lab, right] at (0.760,-1.520) {$A\mathbf x=2\mathbf x$};
\end{tikzpicture}
\end{center}
```

The eigenvectors keep their direction: $A\mathbf x_1=5\mathbf x_1$ and $A\mathbf x_2=2\mathbf x_2$ (thick: the images).

:::

::: {#exm-eigenvalues-special-matrices .example name="Projections, permutations, rotations"}

1. A projection $P$ has eigenvalues $1$ (vectors in its column space) and $0$ (vectors in its nullspace).
2. The exchange $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has $\lambda=1$ for $(1,1)$ and $\lambda=-1$ for $(1,-1)$.
3. The rotation $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ turns every real vector by $90^\circ$, so it has no real eigenvector. Its characteristic polynomial $\lambda^2+1$ has roots $\pm i$.
4. A triangular matrix has its diagonal entries as eigenvalues, since $\det(A-\lambda I)$ is the product of $a_{ii}-\lambda$.

:::

::: {#fig-eigenvalues-and-eigenvectors-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.5,0) -- (1.60,0);
\draw[->, muted] (0,-1.5) -- (0,1.60);
\draw[faint, primary] (-1.3,-0.65) -- (1.4,0.7);
\draw[->, emph, primary] (0,0) -- (1,0.5) node[above, lab] {$\lambda=1$};
\draw[->, emph, accent] (0,0) -- (-0.45,0.9) node[above, lab] {$\lambda=0$};
\fill[accent] (0,0) circle[pt];
\node[lab, note, align=center] at (0,-1.95) {projection onto a line};
\end{scope}
\begin{scope}[shift={(4,0)}]
\draw[->, muted] (-1.5,0) -- (1.60,0);
\draw[->, muted] (0,-1.5) -- (0,1.60);
\draw[faint, dashed] (-1.3,-1.3) -- (1.3,1.3);
\draw[->, emph, primary] (0,0) -- (0.9,0.9) node[above, lab] {$(1,1)$: $\lambda=1$};
\draw[->, faint] (0,0) -- (0.8,-0.8) node[right, lab] {$(1,-1)$};
\draw[->, emph, accent] (0,0) -- (-0.8,0.8) node[left, lab] {$\lambda=-1$};
\node[lab, note, align=center] at (0,-1.95) {exchange $\begin{bmatrix}0&1\\1&0\end{bmatrix}$};
\end{scope}
\begin{scope}[shift={(8,0)}]
\draw[->, muted] (-1.5,0) -- (1.60,0);
\draw[->, muted] (0,-1.5) -- (0,1.60);
\draw[->, emph, primary] (0,0) -- (1,0.3) node[right, lab] {$\mathbf x$};
\draw[->, emph, accent] (0,0) -- (-0.3,1) node[above, lab] {$A\mathbf x$};
\draw[->, muted] (0.5,0.15) arc[start angle=17, end angle=107, radius=0.52];
\node[lab, note, align=center] at (0,-1.95) {rotation by $90^\circ$:\\no real eigenvector};
\end{scope}
\end{tikzpicture}
\end{center}
```

Items 1–3 of @exm-eigenvalues-special-matrices. A projection keeps vectors on its line and kills those perpendicular to it; the exchange (a reflection in the dashed line) keeps $(1,1)$ and reverses $(1,-1)$; the rotation turns every real vector, so its eigenvalues are $\pm i$.

:::

::: {#rmk-eigenvalues-and-eigenvectors-1 .remark name="What eigenvalues do not do"}

Elimination changes eigenvalues, and in general the eigenvalues of $A+B$ and of $AB$ are not sums or products of the eigenvalues of $A$ and $B$. They are when $A$ and $B$ share the same eigenvectors. Adding $cI$ shifts every eigenvalue by $c$ and keeps the eigenvectors.

:::
