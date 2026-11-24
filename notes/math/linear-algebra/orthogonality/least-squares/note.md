---
title: "Least Squares Approximation"
sources: [mit1806-16]
requires: [math/linear-algebra/orthogonality/projections]
relations:
  related: [math/calculus/multivariable/differentiation/least-squares-fitting]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 16, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

An overdetermined system $A\mathbf{x}=\mathbf{b}$ (more equations than unknowns) usually has no solution: $\mathbf{b}$ is not in $C(A)$. The best we can do is to make the error small.

::: {#def-least-squares-solution .definition name="Least squares solution"}

A *least squares solution* of $A\mathbf{x}=\mathbf{b}$ is a vector $\hat{\mathbf{x}}$ that minimises
$$\lVert A\mathbf{x}-\mathbf{b}\rVert^2=\sum_i\big((A\mathbf{x})_i-b_i\big)^2.$$

:::

::: {#fig-least-squares-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (1.6,-0.6); \node[lab] at (0.8,-0.3) {$A^{\mathsf T}$};
\draw[cell frame] (1.8,0) rectangle (2.4,-1.6); \node[lab] at (2.1,-0.8) {$A$};
\draw[cell frame] (2.6,0) rectangle (2.85,-0.6); \node[lab, tick] at (2.725,-0.3) {$\hat{\mathbf x}$};
\node[lab] at (3.15,-0.3) {$=$};
\draw[cell frame] (3.45,0) rectangle (5.05,-0.6); \node[lab] at (4.25,-0.3) {$A^{\mathsf T}$};
\draw[cell frame] (5.25,0) rectangle (5.5,-1.6); \node[lab, tick] at (5.375,-0.8) {$\mathbf b$};
\node[lab, tick] at (0.8,-0.85) {$n\times m$}; \node[lab, tick] at (2.1,-1.85) {$m\times n$};
\draw[decorate, decoration={brace, amplitude=3pt, mirror}] (0,-2.2) -- (2.4,-2.2) node[midway, below=3pt, lab, note] {$A^{\mathsf T}A$: small, $n\times n$};
\end{tikzpicture}
\end{center}
```

Shapes in the normal equations for a tall $A$ ($m$ data points, $n$ unknowns, $m>n$). Multiplying by $A^{\mathsf T}$ turns $m$ equations that cannot all hold into $n$ equations that can.

:::

::: {#thm-least-squares-normal-equations .theorem name="Least squares solves the normal equations"}

$\hat{\mathbf{x}}$ is a least squares solution if and only if $A^{\mathsf T}A\hat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}$. If the columns of $A$ are independent it is unique, and $A\hat{\mathbf{x}}$ is the projection of $\mathbf{b}$ onto $C(A)$.

:::

::: {.proof}

1. $A\mathbf{x}$ ranges over $C(A)$, so minimising $\lVert A\mathbf{x}-\mathbf{b}\rVert$ means finding the point of $C(A)$ closest to $\mathbf{b}$.

2. For independent columns this is @thm-projection-onto-subspace.

3. In general, step 2 of that proof shows that any $\hat{\mathbf{x}}$ with $A^{\mathsf T}(\mathbf{b}-A\hat{\mathbf{x}})=\mathbf{0}$ is a minimiser; conversely at a minimiser the error must be orthogonal to $C(A)$, or moving along a column direction would reduce it.

:::

::: {#fig-least-squares-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\fill[tintA] (-1.6,-0.7) -- (2.6,-0.7) -- (3.6,0.9) -- (-0.6,0.9) -- cycle;
\draw[faint] (-1.6,-0.7) -- (2.6,-0.7) -- (3.6,0.9) -- (-0.6,0.9) -- cycle;
\node[lab, note, primary] at (3.0,-0.45) {$C(A)$};
\fill[ink] (0,0) circle[pt] node[below left, lab, tick] {$\mathbf 0$};
\draw[->, emph, ink] (0,0) -- (2,2.1) node[above, lab] {$\mathbf b$};
\draw[->, emph, primary] (0,0) -- (2,0.3) node[below right, lab] {$\mathbf p=A\hat{\mathbf x}$};
\draw[->, emph, accent] (2,0.3) -- (2,2.1) node[midway, right, lab] {$\mathbf e=\mathbf b-A\hat{\mathbf x}$};
\draw[muted] (2,0.5) -- (1.82,0.47) -- (1.82,0.27);
\end{scope}
\node[lab, note, anchor=west, align=left] at (4.2,1.0) {$\mathbf e\perp C(A)$ means\\$A^{\mathsf T}(\mathbf b-A\hat{\mathbf x})=\mathbf 0$:\\the normal equations};
\end{tikzpicture}
\end{center}
```

Least squares as projection. When $\mathbf b$ is not in the column space, the closest point $A\hat{\mathbf x}$ is the projection $\mathbf p$, and the error is perpendicular to every column of $A$.

:::

::: {#exm-least-squares-line .example name="Fitting a straight line"}

Fit $b=C+Dt$ to the points $(t,b)=(0,1),(1,3),(2,4),(3,4)$. The four equations $C+Dt_i=b_i$ are
$$A=\begin{bmatrix}1&0\\1&1\\1&2\\1&3\end{bmatrix},\qquad \mathbf{b}=\begin{bmatrix}1\\3\\4\\4\end{bmatrix},\qquad
A^{\mathsf T}A=\begin{bmatrix}4&6\\6&14\end{bmatrix},\qquad A^{\mathsf T}\mathbf{b}=\begin{bmatrix}12\\23\end{bmatrix}.$$
The normal equations give $\hat C=\frac32$, $\hat D=1$: the best line is $b=\frac32+t$. Its values at the four points are $\mathbf{p}=(\frac32,\frac52,\frac72,\frac92)$ and the errors are $\mathbf{e}=\mathbf{b}-\mathbf{p}=(-\frac12,\frac12,\frac12,-\frac12)$. As predicted, $\mathbf{e}$ is perpendicular to both columns of $A$: its entries sum to $0$, and $\sum_i t_ie_i=0+\frac12+1-\frac32=0$.

:::

::: {#fig-least-squares-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.300,0) -- (3.600,0) node[lab, right] {$t$};
\draw[->, faint] (0,-0.200) -- (0,3.000) node[lab, above] {$b$};
\draw[hl] (-0.200,0.780) -- (3.400,2.940) node[lab, right] {$b=\frac32+t$};
\draw[dashed] (0.000,0.900) -- (0.000,0.600);
\node[dot] at (0.000,0.600) {};
\node[lab, tick, left] at (-0.050,0.750) {$e=-\tfrac12$};
\node[lab, tick, below] at (0.000,0) {0};
\draw[dashed] (1.000,1.500) -- (1.000,1.800);
\node[dot] at (1.000,1.800) {};
\node[lab, tick, left] at (0.950,1.650) {$e=\tfrac12$};
\node[lab, tick, below] at (1.000,0) {1};
\draw[dashed] (2.000,2.100) -- (2.000,2.400);
\node[dot] at (2.000,2.400) {};
\node[lab, tick, left] at (1.950,2.250) {$e=\tfrac12$};
\node[lab, tick, below] at (2.000,0) {2};
\draw[dashed] (3.000,2.700) -- (3.000,2.400);
\node[dot] at (3.000,2.400) {};
\node[lab, tick, left] at (2.950,2.550) {$e=-\tfrac12$};
\node[lab, tick, below] at (3.000,0) {3};
\end{tikzpicture}
\end{center}
```

The best line $b=\frac32+t$ and the vertical errors $e_i=b_i-p_i$, which sum to zero and are orthogonal to $(0,1,2,3)$.

:::

::: {#rmk-least-squares-1 .remark name="Calculus gives the same equations"}

Setting the partial derivatives of $E(C,D)=\sum_i(C+Dt_i-b_i)^2$ to zero gives $\sum_i(C+Dt_i-b_i)=0$ and $\sum_it_i(C+Dt_i-b_i)=0$, which are the two normal equations. Fitting a parabola $C+Dt+Et^2$ adds a column $t_i^2$ to $A$; the method is unchanged.

:::

::: {#fig-least-squares-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[y={(0,0.8cm)}]
\draw[->, muted] (0,0) -- (3.8,0) node[right, lab, tick] {$t$}; \draw[->, muted] (0,0) -- (0,5) node[above, lab, tick] {$b$};
\draw[emph, primary] (-0.2,1.3) -- (3.6,5.1);
\fill[tintB] (0,1) rectangle (0.5,1.5);
\draw[accent] (0,1) rectangle (0.5,1.5);
\fill[ink] (0,1) circle[pt];
\fill[tintB] (1,2.5) rectangle (1.5,3);
\draw[accent] (1,2.5) rectangle (1.5,3);
\fill[ink] (1,3) circle[pt];
\fill[tintB] (2,3.5) rectangle (2.5,4);
\draw[accent] (2,3.5) rectangle (2.5,4);
\fill[ink] (2,4) circle[pt];
\fill[tintB] (3,4) rectangle (3.5,4.5);
\draw[accent] (3,4) rectangle (3.5,4.5);
\fill[ink] (3,4) circle[pt];
\node[lab, note, anchor=west] at (3.9,3.5) {each square has area $e_i^2=\frac14$; the line minimises the total, $1$};
\end{tikzpicture}
\end{center}
```

What is minimised in @exm-least-squares-line: the total area of the squares on the vertical errors. Setting the derivatives of $\sum_i(C+Dt_i-b_i)^2$ in $C$ and $D$ to zero gives the normal equations again.

:::
