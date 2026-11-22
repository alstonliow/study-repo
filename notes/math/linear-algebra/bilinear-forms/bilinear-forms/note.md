---
title: "Bilinear Forms"
sources: [camib-la-4]
requires: [math/linear-algebra/duality/dual-maps]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Chapter 4, in our own wording; examples ours (checked with sympy); proofs written out in steps. -->

A bilinear form takes two vectors and returns a scalar, linearly in each. The dot product is the model, but a bilinear form need be neither symmetric nor positive.

::: {#def-bilinear-form .definition name="Bilinear form"}

Let $V,W$ be $F$-vector spaces. A *bilinear form* is a map $\psi:V\times W\to F$ that is linear in each argument when the other is fixed:
$$\psi(\lambda v_1+\mu v_2,w)=\lambda\psi(v_1,w)+\mu\psi(v_2,w),\qquad \psi(v,\lambda w_1+\mu w_2)=\lambda\psi(v,w_1)+\mu\psi(v,w_2).$$
If $\mathcal B=(e_1,\dots,e_n)$ and $\mathcal C=(f_1,\dots,f_m)$ are bases, the *matrix* of $\psi$ is $[\psi]_{\mathcal B,\mathcal C}=A$ with $a_{ij}=\psi(e_i,f_j)$.

:::

::: {#fig-bilinear-forms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (1.300,1.300);
\node[lab] at (0.650,0.650) {$\scriptstyle\psi(e_1,f_1)$};
\draw[cell frame] (1.300,0.000) rectangle (2.600,1.300);
\node[lab] at (1.950,0.650) {$\scriptstyle\psi(e_1,f_2)$};
\draw[cell frame] (2.600,0.000) rectangle (3.900,1.300);
\node[lab] at (3.250,0.650) {$\scriptstyle\psi(e_1,f_3)$};
\draw[cell frame] (0.000,-1.300) rectangle (1.300,0.000);
\node[lab] at (0.650,-0.650) {$\scriptstyle\psi(e_2,f_1)$};
\draw[cell frame] (1.300,-1.300) rectangle (2.600,0.000);
\node[lab] at (1.950,-0.650) {$\scriptstyle\psi(e_2,f_2)$};
\draw[cell, fill=primaryLight] (2.600,-1.300) rectangle (3.900,0.000);
\node[lab] at (3.250,-0.650) {$\scriptstyle\psi(e_2,f_3)$};
\node[lab, tick] at (0.65,1.5) {$f_1$}; \node[lab, tick] at (1.95,1.5) {$f_2$}; \node[lab, tick] at (3.25,1.5) {$f_3$};
\node[lab, tick] at (-0.25,0.65) {$e_1$}; \node[lab, tick] at (-0.25,-0.65) {$e_2$};
\node[lab, note, anchor=west, align=left] at (4.2,0.0) {$\psi(\mathbf x,\mathbf y)=\mathbf x^{\mathsf T}A\,\mathbf y$\\with $\mathbf x$, $\mathbf y$ the coordinate columns};
\end{tikzpicture}
\end{center}
```

The matrix of a bilinear form $\psi:U\times V\to F$ with $\dim U=2$, $\dim V=3$: entry $(i,j)$ is the value on the $i$-th basis vector of $U$ and the $j$-th of $V$. By bilinearity these six numbers determine $\psi$.

:::

Expanding both arguments,
$$\psi(v,w)=\sum_{i,j}\lambda_i\mu_j\psi(e_i,f_j)=[v]_{\mathcal B}^{\mathsf T}\,A\,[w]_{\mathcal C},$$
so in coordinates every bilinear form on $F^n\times F^m$ is $(\mathbf x,\mathbf y)\mapsto\mathbf x^{\mathsf T}A\mathbf y$ for a unique $n\times m$ matrix $A$.

::: {#exm-bilinear-forms .example name="Bilinear forms"}

1. The dot product on $\mathbb R^n$ has matrix $I$ in the standard basis.
2. $\psi(\mathbf x,\mathbf y)=x_1y_2-x_2y_1$ on $F^2$ has matrix $\begin{bmatrix}0&1\\-1&0\end{bmatrix}$; it is the determinant of $[\mathbf x\ \mathbf y]$ and satisfies $\psi(\mathbf x,\mathbf x)=0$.
3. On $C[0,1]$, $\psi(f,g)=\int_0^1f(t)g(t)k(t)\,dt$ for a fixed continuous weight $k$.
4. The *evaluation pairing* $V^*\times V\to F$, $(\theta,v)\mapsto\theta(v)$; in a basis and its dual basis its matrix is $I$.

:::

::: {#fig-bilinear-forms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.4,0) -- (3.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,2.4) node[lab, above] {$y$};
\fill[shade] (0,0) -- (2.4,0.6) -- (3.2,2.0) -- (0.8,1.4) -- cycle;
\draw[->, emph] (0,0) -- (2.4,0.6) node[lab, below right] {$\mathbf x$};
\draw[->, emph] (0,0) -- (0.8,1.4) node[lab, above left] {$\mathbf y$};
\node[lab] at (1.6,1.0) {$\psi(\mathbf x,\mathbf y)$};
\end{tikzpicture}
\end{center}
```

The form $\psi(\mathbf x,\mathbf y)=x_1y_2-x_2y_1$ of item 2 over $\mathbb R$ is the signed area of the parallelogram on $\mathbf x$ and $\mathbf y$: positive when $\mathbf y$ is anticlockwise from $\mathbf x$, and $0$ when $\mathbf y=\mathbf x$.

:::

::: {#prp-bilinear-form-change-of-basis .proposition name="Change of basis for a bilinear form"}

If $P$ and $Q$ are the change of basis matrices from $\mathcal B$ to $\mathcal B'$ and from $\mathcal C$ to $\mathcal C'$ (as in @thm-change-of-basis-two-spaces), then
$$[\psi]_{\mathcal B',\mathcal C'}=P^{\mathsf T}\,[\psi]_{\mathcal B,\mathcal C}\,Q.$$

:::

::: {.proof}

1. Coordinates change by $[v]_{\mathcal B}=P[v]_{\mathcal B'}$ and $[w]_{\mathcal C}=Q[w]_{\mathcal C'}$.

2. So $\psi(v,w)=(P[v]_{\mathcal B'})^{\mathsf T}A\,Q[w]_{\mathcal C'}=[v]_{\mathcal B'}^{\mathsf T}(P^{\mathsf T}AQ)[w]_{\mathcal C'}$, and the matrix of a form is determined by this identity (take $v,w$ to be basis vectors).

:::

::: {#fig-bilinear-forms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,1.4) {$U\times V$};
\node[box] (b) at (4,1.4) {$F$};
\draw[->, emph] (a) -- (b) node[midway, above, lab] {$\psi$};
\node[lab, anchor=west] at (-1.5,0) {$[\psi]_{\mathcal B',\mathcal C'}=P^{\mathsf T}\,[\psi]_{\mathcal B,\mathcal C}\,Q$};
\node[lab, note, anchor=west, align=left] at (5.0,0.7) {a linear map changes by $Q^{-1}AP$,\\a bilinear form by $P^{\mathsf T}AQ$:\\both inputs are changed, none is an output};
\end{tikzpicture}
\end{center}
```

How the matrix of a bilinear form changes with the bases. Both arguments are vectors fed in, so both get the change-of-basis matrix ($P$ for $U$, $Q$ for $V$), one of them transposed because it stands on the left of $A$.

:::

Compare a linear map $V\to W$, whose matrix changes to $Q^{-1}AP$: forms and maps are both described by matrices, but they transform differently.

::: {#def-bilinear-form-kernels .definition name="Kernels, non-degenerate forms, rank"}

A bilinear form $\psi:V\times W\to F$ gives two linear maps
$$\psi_L:V\to W^*,\ \ \psi_L(v)=\psi(v,\cdot),\qquad \psi_R:W\to V^*,\ \ \psi_R(w)=\psi(\cdot,w).$$
The *left kernel* is $\ker\psi_L=\{v:\psi(v,w)=0\ \forall w\}$ and the *right kernel* is $\ker\psi_R$. $\psi$ is *non-degenerate* if both kernels are $\{0\}$. The *rank* of $\psi$ is the rank of any matrix representing it.

:::

The rank is well defined because $P^{\mathsf T}AQ$ has the rank of $A$ (@thm-rank-normal-form).

::: {#thm-bilinear-form-kernels .theorem name="Rank and non-degeneracy"}

Let $V,W$ be finite-dimensional, $\psi$ a bilinear form with matrix $A$ in bases $\mathcal B,\mathcal C$.

1. In the dual bases, $[\psi_R]=A$ and $[\psi_L]=A^{\mathsf T}$.
2. $r(\psi_L)=r(\psi_R)=r(A)$, so $\dim V-\dim\ker\psi_L=\dim W-\dim\ker\psi_R$.
3. $\psi$ is non-degenerate if and only if $\dim V=\dim W$ and $A$ is invertible. Then $\psi_L$ and $\psi_R$ are isomorphisms.

:::

::: {.proof}

1. $\psi_R(f_j)$ is the functional $e_i\mapsto a_{ij}$, so by @thm-dual-basis $\psi_R(f_j)=\sum_ia_{ij}\varepsilon_i$: column $j$ of $[\psi_R]$ is column $j$ of $A$. Likewise $\psi_L(e_i)=\sum_ja_{ij}\eta_j$, so column $i$ of $[\psi_L]$ is row $i$ of $A$.

2. Row rank equals column rank (@thm-row-rank-equals-column-rank); the second statement is @thm-rank-nullity for $\psi_L$ and $\psi_R$.

3. Both kernels vanish $\iff$ $r(A)=\dim V$ and $r(A)=\dim W$ by item 2 $\iff$ $A$ is square and invertible. Then $\psi_L,\psi_R$ are injective maps between spaces of equal dimension, hence isomorphisms (@cor-injective-iff-surjective).

:::

So a non-degenerate form identifies $W$ with $V^*$. For example, the dot product identifies $\mathbb R^n$ with its dual by $\mathbf a\mapsto\mathbf a^{\mathsf T}$.

::: {#exm-degenerate-form .example name="A degenerate form"}

On $\mathbb R^2\times\mathbb R^3$ let $\psi(\mathbf x,\mathbf y)=\mathbf x^{\mathsf T}A\mathbf y$ with $A=\begin{bmatrix}1&0&1\\2&0&2\end{bmatrix}$, of rank $1$. The left kernel is $\{\mathbf x:\mathbf x^{\mathsf T}A=0\}=\langle(2,-1)^{\mathsf T}\rangle$, of dimension $2-1$; the right kernel is $\{\mathbf y:A\mathbf y=0\}=\langle(0,1,0)^{\mathsf T},(1,0,-1)^{\mathsf T}\rangle$, of dimension $3-1$, as @thm-bilinear-form-kernels predicts.

:::

::: {#fig-bilinear-forms-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$1$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$0$};
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell, fill=primaryLight] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$2$};
\draw[cell, fill=primaryLight] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell, fill=primaryLight] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$2$};
\node[lab, note] at (0.825,-0.350) {$A$, rank $1$};
\node[lab, note, anchor=west, align=left] at (2.0,0.55) {left kernel ($\subseteq\mathbb R^2$): $\langle(2,-1)\rangle$, dimension $2-1$\\right kernel ($\subseteq\mathbb R^3$): $\langle(0,1,0),(1,0,-1)\rangle$, dimension $3-1$};
\draw[cell, fill=primaryLight] (0.00,-1.40) rectangle (0.75,-0.95);
\node[lab, tick] at (0.38,-1.62) {$r$};
\draw[cell, fill=accentLight] (0.75,-1.40) rectangle (1.50,-0.95);
\node[lab, tick] at (1.12,-1.62) {ker};
\node[lab, anchor=east] at (-0.10,-1.17) {$\mathbb R^2$};
\draw[cell, fill=primaryLight] (4.20,-1.40) rectangle (4.95,-0.95);
\node[lab, tick] at (4.58,-1.62) {$r$};
\draw[cell, fill=accentLight] (4.95,-1.40) rectangle (5.70,-0.95);
\draw[cell, fill=accentLight] (5.70,-1.40) rectangle (6.45,-0.95);
\node[lab, tick] at (5.70,-1.62) {right kernel};
\node[lab, anchor=east] at (4.10,-1.17) {$\mathbb R^3$};
\end{tikzpicture}
\end{center}
```

@exm-degenerate-form: the two kernels of a form can have different dimensions, but each side has dimension rank plus kernel, as in @thm-bilinear-form-kernels.

:::
