---
title: "Norms of Vectors and Matrices"
sources: [mit18065-8, mit18065-10, mit18065-11, mit18335-4]
requires: [math/linear-algebra/positive-definite/singular-value-decomposition]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.065 (Spring 2018), Lectures 8, 10 and 11 (video lectures and problem sets; no written lecture notes), in our own wording; proofs written out in steps. Numbers checked with numpy. -->

A norm measures the size of a vector or a matrix. For matrices the useful norms are all read off from the singular values, and the ratio of the largest to the smallest singular value measures how sensitive $A\mathbf{x}=\mathbf{b}$ is to errors.

::: {#def-vector-p-norms .definition name="The ℓ¹, ℓ² and ℓ^∞ norms" related="def-norm"}

For $\mathbf{v}=(v_1,\dots,v_n)\in\mathbb{R}^n$,
$$\lVert\mathbf{v}\rVert_1=\sum_{i}\lvert v_i\rvert,\qquad \lVert\mathbf{v}\rVert_2=\Big(\sum_i v_i^2\Big)^{1/2},\qquad \lVert\mathbf{v}\rVert_\infty=\max_i\lvert v_i\rvert.$$
Each satisfies $\lVert\mathbf{v}\rVert\ge0$ with equality only for $\mathbf{v}=\mathbf{0}$, $\lVert c\mathbf{v}\rVert=\lvert c\rvert\,\lVert\mathbf{v}\rVert$, and the triangle inequality $\lVert\mathbf{v}+\mathbf{w}\rVert\le\lVert\mathbf{v}\rVert+\lVert\mathbf{w}\rVert$. Without a subscript, $\lVert\mathbf{v}\rVert=\lVert\mathbf{v}\rVert_2$.

:::

::: {#prp-vector-norm-comparisons .proposition name="Comparing the three norms"}

For every $\mathbf{v}\in\mathbb{R}^n$,
$$\lVert\mathbf{v}\rVert_\infty\le\lVert\mathbf{v}\rVert_2\le\lVert\mathbf{v}\rVert_1\le\sqrt n\,\lVert\mathbf{v}\rVert_2\le n\,\lVert\mathbf{v}\rVert_\infty .$$

:::

::: {.proof}

1. $\lVert\mathbf{v}\rVert_\infty^2=\max_i v_i^2\le\sum_i v_i^2=\lVert\mathbf{v}\rVert_2^2$.

2. $\lVert\mathbf{v}\rVert_1^2=\sum_{i,j}\lvert v_i\rvert\lvert v_j\rvert\ge\sum_i v_i^2=\lVert\mathbf{v}\rVert_2^2$, since the cross terms are nonnegative.

3. By Cauchy–Schwarz with the all-ones vector, $\sum_i\lvert v_i\rvert\cdot1\le\sqrt n\,\lVert\mathbf{v}\rVert_2$.

4. $\lVert\mathbf{v}\rVert_2^2=\sum_i v_i^2\le n\max_i v_i^2$, so $\sqrt n\,\lVert\mathbf{v}\rVert_2\le n\lVert\mathbf{v}\rVert_\infty$.

:::

::: {#fig-matrix-norms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.6,0) -- (1.8,0) node[lab, right] {$v_1$};
\draw[->, faint] (0,-1.5) -- (0,1.7) node[lab, above] {$v_2$};
\draw[faint] (-1,-1) rectangle (1,1);
\draw[emph] (0,0) circle (1);
\draw[hl] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
\node[lab] at (1.25,1.15) {$\ell^\infty$};
\node[lab] at (-0.86,0.86) {$\ell^2$};
\node[lab] at (0.25,0.38) {$\ell^1$};
\end{tikzpicture}
\end{center}
```

Unit balls in $\mathbb{R}^2$: the $\ell^1$ diamond lies inside the $\ell^2$ disc, which lies inside the $\ell^\infty$ square, matching $\lVert\mathbf{v}\rVert_\infty\le\lVert\mathbf{v}\rVert_2\le\lVert\mathbf{v}\rVert_1$.

:::

::: {#def-matrix-norms .definition name="Spectral, Frobenius and nuclear norms"}

For a real $m\times n$ matrix $A$,
$$\lVert A\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert A\mathbf{x}\rVert_2}{\lVert\mathbf{x}\rVert_2},\qquad \lVert A\rVert_F=\Big(\sum_{i,j}a_{ij}^2\Big)^{1/2},\qquad \lVert A\rVert_*=\sigma_1+\dots+\sigma_r .$$

:::

::: {#thm-matrix-norms-singular-values .theorem name="Matrix norms from singular values"}

If $A$ has singular values $\sigma_1\ge\dots\ge\sigma_r>0$, then
$$\lVert A\rVert_2=\sigma_1,\qquad \lVert A\rVert_F^2=\sigma_1^2+\dots+\sigma_r^2,\qquad \lVert A\rVert_*=\sigma_1+\dots+\sigma_r .$$
All three are unchanged when $A$ is multiplied on either side by an orthogonal matrix.

:::

::: {.proof}

1. Write $A=U\Sigma V^{\mathsf T}$ (@thm-svd). Orthogonal matrices preserve lengths (@prp-orthonormal-columns-preserve-length), so with $\mathbf{y}=V^{\mathsf T}\mathbf{x}$ we get $\lVert A\mathbf{x}\rVert=\lVert\Sigma\mathbf{y}\rVert$ and $\lVert\mathbf{x}\rVert=\lVert\mathbf{y}\rVert$.

2. $\lVert\Sigma\mathbf{y}\rVert^2=\sum_i\sigma_i^2y_i^2\le\sigma_1^2\lVert\mathbf{y}\rVert^2$, with equality for $\mathbf{y}=\mathbf{e}_1$. So $\lVert A\rVert_2=\sigma_1$.

3. $\lVert A\rVert_F^2=\operatorname{tr}(A^{\mathsf T}A)$, and $A^{\mathsf T}A=V\Sigma^{\mathsf T}\Sigma V^{\mathsf T}$ has the same trace as $\Sigma^{\mathsf T}\Sigma$, which is $\sum\sigma_i^2$.

4. If $Q_1,Q_2$ are orthogonal, $Q_1AQ_2=(Q_1U)\Sigma(Q_2^{\mathsf T}V)^{\mathsf T}$ is an SVD with the same $\Sigma$, so every norm defined by the $\sigma$'s is unchanged.

:::

::: {#fig-matrix-norms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (0,0) -- (8.2,0); \draw[->, muted] (0,0) -- (0,2.4);
\draw[bar] (0.40,0) rectangle (1.00,1.342); \node[lab, tick] at (0.70,-0.25) {$\sigma_1$};
\draw[bar] (2.00,0) rectangle (2.60,0.447); \node[lab, tick] at (2.30,-0.55) {$\sigma_2$};
\draw[cell, fill=accentLight] (3.60,0) rectangle (4.20,1.342); \node[lab, tick] at (3.90,-0.25) {$\lVert A\rVert_2=\sigma_1$};
\draw[cell, fill=accentLight] (5.20,0) rectangle (5.80,1.414); \node[lab, tick] at (5.50,-0.55) {$\lVert A\rVert_F=\sqrt{50}$};
\draw[cell, fill=accentLight] (6.80,0) rectangle (7.40,1.789); \node[lab, tick] at (7.10,-0.25) {$\lVert A\rVert_*=4\sqrt5$};
\end{tikzpicture}
\end{center}
```

Three norms of $A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$ from its singular values $3\sqrt5\approx6.7$ and $\sqrt5\approx2.2$: the largest one, the root of the sum of squares, and the sum. Always $\lVert A\rVert_2\le\lVert A\rVert_F\le\lVert A\rVert_*$.

:::

::: {#prp-frobenius-submultiplicative .proposition name="Norms of products"}

$$\lVert AB\rVert_2\le\lVert A\rVert_2\lVert B\rVert_2,\qquad \lVert AB\rVert_F\le\lVert A\rVert_F\lVert B\rVert_F .$$

:::

::: {.proof}

1. $\lVert AB\mathbf{x}\rVert\le\lVert A\rVert_2\lVert B\mathbf{x}\rVert\le\lVert A\rVert_2\lVert B\rVert_2\lVert\mathbf{x}\rVert$ for every $\mathbf{x}$.

2. Let $\mathbf{r}_i^{\mathsf T}$ be the rows of $A$ and $\mathbf{b}_j$ the columns of $B$. By Cauchy–Schwarz, $(AB)_{ij}^2=(\mathbf{r}_i^{\mathsf T}\mathbf{b}_j)^2\le\lVert\mathbf{r}_i\rVert^2\lVert\mathbf{b}_j\rVert^2$.

3. Summing over all $i$ and $j$: $\lVert AB\rVert_F^2\le\big(\sum_i\lVert\mathbf{r}_i\rVert^2\big)\big(\sum_j\lVert\mathbf{b}_j\rVert^2\big)=\lVert A\rVert_F^2\lVert B\rVert_F^2$.

:::

::: {#rmk-matrix-norms-1 .remark name="Unit balls"}

The unit ball $\{\mathbf{v}:\lVert\mathbf{v}\rVert\le1\}$ in $\mathbb{R}^2$ is a diamond for $\ell^1$, a disc for $\ell^2$ and a square for $\ell^\infty$. Each is convex, by the triangle inequality. For $0<p<1$ the formula $(\sum\lvert v_i\rvert^p)^{1/p}$ gives a non-convex "ball" and fails the triangle inequality, so it is not a norm. Minimising $\lVert\mathbf{x}\rVert_1$ subject to $A\mathbf{x}=\mathbf{b}$ tends to give sparse solutions, because the diamond first touches the plane $A\mathbf{x}=\mathbf{b}$ at a corner; minimising $\lVert\mathbf{x}\rVert_2$ gives $A^{+}\mathbf{b}$ (@thm-pseudoinverse-properties).

:::

::: {#def-condition-number .definition name="Condition number"}

For an invertible $n\times n$ matrix $A$,
$$\kappa(A)=\lVert A\rVert_2\,\lVert A^{-1}\rVert_2=\frac{\sigma_1}{\sigma_n}\ \ge1 .$$

:::

::: {#thm-condition-number-error .theorem name="Relative error is at most κ times larger"}

If $A\mathbf{x}=\mathbf{b}$ and $A(\mathbf{x}+\delta\mathbf{x})=\mathbf{b}+\delta\mathbf{b}$ with $\mathbf{b}\ne\mathbf{0}$, then
$$\frac{\lVert\delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(A)\,\frac{\lVert\delta\mathbf{b}\rVert}{\lVert\mathbf{b}\rVert}.$$

:::

::: {.proof}

1. Subtracting, $A\,\delta\mathbf{x}=\delta\mathbf{b}$, so $\lVert\delta\mathbf{x}\rVert=\lVert A^{-1}\delta\mathbf{b}\rVert\le\lVert A^{-1}\rVert_2\lVert\delta\mathbf{b}\rVert$.

2. From $\mathbf{b}=A\mathbf{x}$, $\lVert\mathbf{b}\rVert\le\lVert A\rVert_2\lVert\mathbf{x}\rVert$, so $1/\lVert\mathbf{x}\rVert\le\lVert A\rVert_2/\lVert\mathbf{b}\rVert$.

3. Multiply the two inequalities.

4. Equality holds when $\mathbf{x}$ is along $\mathbf{v}_1$ and $\delta\mathbf{b}$ along $\mathbf{u}_n$, so the bound cannot be improved.

:::

::: {#fig-matrix-norms-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.1,0) -- (1.2,0);
\draw[->, muted] (0,-1.1) -- (0,1.2);
\draw[emph, primary] (0,0) circle[radius=0.5];
\node[lab, note, primary] at (0,-1.4) {$\delta\mathbf b$: a circle};
\end{scope}
\draw[->] (1.3,0) -- (2.3,0) node[midway, above, lab, note] {$A^{-1}$};
\begin{scope}[shift={(4.4,0)}]
\draw[->, muted] (-1.9,0) -- (1.9,0); \draw[->, muted] (0,-1.1) -- (0,1.1);
\draw[emph, accent, rotate=20] (0,0) ellipse[x radius=1.5, y radius=0.5];
\node[lab, note, accent] at (0,-1.4) {$\delta\mathbf x$: stretched by up to $1/\sigma_n$};
\end{scope}
\node[lab, note, anchor=west, align=left] at (6.6,0) {$\dfrac{\lVert\delta\mathbf x\rVert}{\lVert\mathbf x\rVert}\le\kappa(A)\dfrac{\lVert\delta\mathbf b\rVert}{\lVert\mathbf b\rVert}$,\\ $\kappa=\sigma_1/\sigma_n$};
\end{tikzpicture}
\end{center}
```

Errors in $\mathbf b$ of equal size come out of $A^{-1}$ with very different sizes: those along the weakest direction of $A$ are amplified most. The ratio of the strongest to the weakest stretch is the condition number.

:::

::: {#exm-condition-number-hilbert .example name="Small and large condition numbers"}

$A=\begin{bmatrix}3&0\\4&5\end{bmatrix}$ has $\sigma_1=3\sqrt5$, $\sigma_2=\sqrt5$ (@exm-svd-two-by-two). So $\lVert A\rVert_2=3\sqrt5$, $\lVert A\rVert_F=\sqrt{50}$, $\lVert A\rVert_*=4\sqrt5$ and $\kappa(A)=3$.

The $3\times3$ Hilbert matrix $H_{ij}=1/(i+j-1)$ is symmetric positive definite with $\kappa(H)\approx524$; for $n=10$ it is about $1.6\times10^{13}$, so in double precision almost every digit of the solution of $H\mathbf{x}=\mathbf{b}$ can be lost. Orthogonal matrices have $\kappa(Q)=1$, which is why computations with $Q$ are safe.

:::

::: {#fig-matrix-norms-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, muted] (0,0) -- (4.6,0) node[right, lab, tick] {$n$}; \draw[->, muted] (0,0) -- (0,3.0) node[above, lab, tick] {$\log_{10}\kappa(H_n)$};
\fill[accent] (0.50,0.000) circle[pt]; \node[lab, tick] at (0.50,-0.2) {1};
\fill[accent] (1.00,0.360) circle[pt]; \node[lab, tick] at (1.00,-0.2) {2};
\fill[accent] (1.50,0.761) circle[pt]; \node[lab, tick] at (1.50,-0.2) {3};
\fill[accent] (2.00,1.173) circle[pt]; \node[lab, tick] at (2.00,-0.2) {4};
\fill[accent] (2.50,1.590) circle[pt]; \node[lab, tick] at (2.50,-0.2) {5};
\fill[accent] (3.00,2.009) circle[pt]; \node[lab, tick] at (3.00,-0.2) {6};
\fill[accent] (3.50,2.430) circle[pt]; \node[lab, tick] at (3.50,-0.2) {7};
\fill[accent] (4.00,2.851) circle[pt]; \node[lab, tick] at (4.00,-0.2) {8};
\draw[faint] (0,0.00) -- (-0.08,0.00) node[left, lab, tick] {0};
\draw[faint] (0,1.40) -- (-0.08,1.40) node[left, lab, tick] {5};
\draw[faint] (0,2.80) -- (-0.08,2.80) node[left, lab, tick] {10};
\node[lab, note, anchor=west, align=left] at (4.8,1.5) {each step costs about\\$1.5$ more decimal digits};
\end{tikzpicture}
\end{center}
```

Condition numbers of the Hilbert matrices $H_n$ on a logarithmic scale, from $\kappa(H_1)=1$ and $\kappa(H_3)\approx524$ upward. They grow roughly geometrically, so $H\mathbf x=\mathbf b$ becomes hopeless in double precision near $n=12$.

:::

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 4 (norms on vector spaces), in our own wording: induced norms for any pair of vector norms and the one- and infinity-norm formulas. -->

::: {#def-induced-matrix-norm .definition name="Induced matrix norm" generalizes="def-matrix-norms"}

Given norms $\lVert\cdot\rVert_{(n)}$ on $\mathbb{C}^n$ and $\lVert\cdot\rVert_{(m)}$ on $\mathbb{C}^m$, the *induced* (or *operator*) norm of an $m\times n$ matrix $A$ is
$$\lVert A\rVert_{(m,n)}=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert A\mathbf{x}\rVert_{(m)}}{\lVert\mathbf{x}\rVert_{(n)}}=\max_{\lVert\mathbf{x}\rVert_{(n)}=1}\lVert A\mathbf{x}\rVert_{(m)},$$
the largest factor by which $A$ stretches a vector. For the $p$-norms on both sides it is written $\lVert A\rVert_p$; $\lVert A\rVert_2$ is the spectral norm of @def-matrix-norms. The maximum exists because the unit sphere is compact and all norms on $\mathbb{C}^n$ are equivalent (@thm-norms-equivalent-finite-dimension).

:::

::: {#prp-induced-one-infinity-norms .proposition name="One- and infinity-norms of a matrix"}

For an $m\times n$ matrix $A$ with entries $a_{ij}$,
$$\lVert A\rVert_1=\max_{1\le j\le n}\sum_{i=1}^m\lvert a_{ij}\rvert\quad(\text{largest column sum}),\qquad \lVert A\rVert_\infty=\max_{1\le i\le m}\sum_{j=1}^n\lvert a_{ij}\rvert\quad(\text{largest row sum}).$$
Every induced norm is submultiplicative: $\lVert AB\rVert\le\lVert A\rVert\,\lVert B\rVert$.

:::

::: {.proof}

1. *One-norm, upper bound.* Write $A\mathbf{x}=\sum_j x_j\mathbf{a}_j$ with columns $\mathbf{a}_j$. Then $\lVert A\mathbf{x}\rVert_1\le\sum_j\lvert x_j\rvert\,\lVert\mathbf{a}_j\rVert_1\le\big(\max_j\lVert\mathbf{a}_j\rVert_1\big)\lVert\mathbf{x}\rVert_1$.

2. *One-norm, attained.* If column $k$ has the largest sum, $\mathbf{x}=\mathbf{e}_k$ gives $\lVert A\mathbf{e}_k\rVert_1=\lVert\mathbf{a}_k\rVert_1$ with $\lVert\mathbf{e}_k\rVert_1=1$.

3. *Infinity-norm, upper bound.* For $\lVert\mathbf{x}\rVert_\infty=1$, each entry satisfies $\lvert(A\mathbf{x})_i\rvert=\lvert\sum_j a_{ij}x_j\rvert\le\sum_j\lvert a_{ij}\rvert$, so $\lVert A\mathbf{x}\rVert_\infty\le\max_i\sum_j\lvert a_{ij}\rvert$.

4. *Infinity-norm, attained.* If row $k$ has the largest sum, take $x_j=\overline{a_{kj}}/\lvert a_{kj}\rvert$ (and $x_j=1$ where $a_{kj}=0$). Then $\lVert\mathbf{x}\rVert_\infty=1$ (or $\mathbf{x}$ is any unit vector if row $k$ is zero) and $(A\mathbf{x})_k=\sum_j\lvert a_{kj}\rvert$.

5. *Submultiplicativity.* $\lVert AB\mathbf{x}\rVert\le\lVert A\rVert\,\lVert B\mathbf{x}\rVert\le\lVert A\rVert\,\lVert B\rVert\,\lVert\mathbf{x}\rVert$ for every $\mathbf{x}$.

:::

::: {#exm-induced-norms .example name="Three induced norms of one matrix"}

For $A=\begin{bmatrix}1&2\\0&2\end{bmatrix}$ the column sums are $1,4$ and the row sums $3,2$, so $\lVert A\rVert_1=4$ and $\lVert A\rVert_\infty=3$. The singular values are the square roots of the eigenvalues of $A^{\mathsf T}A=\begin{bmatrix}1&2\\2&8\end{bmatrix}$, giving $\lVert A\rVert_2=\sqrt{(9+\sqrt{65})/2}\approx2.921$. The vector $\mathbf{e}_2$ realises $\lVert A\rVert_1$ and $(1,1)$ realises $\lVert A\rVert_\infty$.

:::

::: {#fig-matrix-norms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.62]
\begin{scope}
\draw[->, faint] (-4.4,0) -- (4.4,0); \draw[->, faint] (0,-3.2) -- (0,3.2);
\draw[emph] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
\draw[hl] (1,0) -- (2,2) -- (-1,0) -- (-2,-2) -- cycle;
\fill (2,2) circle (2.5pt) node[lab, right] {$A\mathbf{e}_2$};
\draw[faint, dashed] (4,0) -- (0,4) -- (-4,0) -- (0,-4) -- cycle;
\node[lab] at (0,-3.9) {$\lVert A\rVert_1=4$};
\end{scope}
\begin{scope}[xshift=10.5cm]
\draw[->, faint] (-4.4,0) -- (4.4,0); \draw[->, faint] (0,-3.2) -- (0,3.2);
\draw[emph] (-1,-1) rectangle (1,1);
\draw[hl] (3,2) -- (-1,-2) -- (-3,-2) -- (1,2) -- cycle;
\fill (3,2) circle (2.5pt) node[lab, right] {$A(1,1)$};
\draw[faint, dashed] (-3,-3) rectangle (3,3);
\node[lab] at (0,-3.9) {$\lVert A\rVert_\infty=3$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The unit ball (thin) of the $1$-norm (left) and the $\infty$-norm (right) and its image under $A=\left[\begin{smallmatrix}1&2\\0&2\end{smallmatrix}\right]$ (thick). The induced norm is the smallest multiple of the unit ball (dashed) that contains the image; it is reached at a corner of the ball.

:::
