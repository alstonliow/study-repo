---
title: "Dual Spaces and Annihilators"
sources: [camib-la-3]
requires: [math/linear-algebra/linear-maps/equivalence-and-rank]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 3.1, in our own wording; examples ours (checked with sympy); proofs written out in steps. -->

A linear functional measures a vector by a single number: a coordinate, an integral, an evaluation. The functionals on $V$ form a vector space of their own.

::: {#def-dual-space .definition name="Dual space, dual basis"}

The *dual space* of an $F$-vector space $V$ is $V^*=\mathcal L(V,F)$, the space of linear maps $V\to F$ (*linear functionals*). If $e_1,\dots,e_n$ is a basis of $V$, its *dual basis* $\varepsilon_1,\dots,\varepsilon_n\in V^*$ is defined by
$$\varepsilon_i(e_j)=\delta_{ij}=\begin{cases}1&i=j,\\0&i\ne j.\end{cases}$$

:::

::: {#fig-dual-spaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.500,1.100) rectangle (1.050,1.650);
\node[lab] at (0.775,1.375) {$1$};
\draw[cell frame] (1.050,1.100) rectangle (1.600,1.650);
\node[lab] at (1.325,1.375) {$0$};
\draw[cell frame] (1.600,1.100) rectangle (2.150,1.650);
\node[lab] at (1.875,1.375) {$0$};
\draw[cell frame] (0.500,0.550) rectangle (1.050,1.100);
\node[lab] at (0.775,0.825) {$0$};
\draw[hl cell] (1.050,0.550) rectangle (1.600,1.100);
\node[lab] at (1.325,0.825) {$1$};
\draw[cell frame] (1.600,0.550) rectangle (2.150,1.100);
\node[lab] at (1.875,0.825) {$0$};
\draw[cell frame] (0.500,-0.000) rectangle (1.050,0.550);
\node[lab] at (0.775,0.275) {$0$};
\draw[cell frame] (1.050,-0.000) rectangle (1.600,0.550);
\node[lab] at (1.325,0.275) {$0$};
\draw[hl cell] (1.600,-0.000) rectangle (2.150,0.550);
\node[lab] at (1.875,0.275) {$1$};
\node[lab, tick] at (0.775,1.85) {$e_1$}; \node[lab, tick] at (1.325,1.85) {$e_2$}; \node[lab, tick] at (1.875,1.85) {$e_3$};
\node[lab, tick] at (0.2,1.375) {$\varepsilon_1$}; \node[lab, tick] at (0.2,0.825) {$\varepsilon_2$}; \node[lab, tick] at (0.2,0.275) {$\varepsilon_3$};
\node[lab, note, anchor=west, align=left] at (2.6,0.825) {$\varepsilon_i(e_j)=\delta_{ij}$: $\varepsilon_i$ reads off\\the $i$-th coordinate, $\varepsilon_i(v)=x_i$};
\end{tikzpicture}
\end{center}
```

The table of values of the dual basis on the basis is the identity. A functional is determined by its values on a basis, so these conditions fix each $\varepsilon_i$.

:::

So $\varepsilon_i$ reads off the $i$-th coordinate: $\varepsilon_i\big(\sum_j\lambda_je_j\big)=\lambda_i$. On $F^n$, functionals are row vectors $\mathbf a^{\mathsf T}$ acting by $\mathbf x\mapsto\mathbf a^{\mathsf T}\mathbf x$, and the dual of the standard basis is the standard basis of rows.

::: {#thm-dual-basis .theorem name="The dual basis is a basis"}

If $e_1,\dots,e_n$ is a basis of $V$, then $\varepsilon_1,\dots,\varepsilon_n$ is a basis of $V^*$, and every $\theta\in V^*$ is
$$\theta=\sum_{i=1}^n\theta(e_i)\,\varepsilon_i.$$
In particular $\dim V^*=\dim V$ when $V$ is finite-dimensional.

:::

::: {.proof}

1. Both sides of the displayed formula are linear and agree on each $e_j$: the right side gives $\sum_i\theta(e_i)\delta_{ij}=\theta(e_j)$. By @thm-linear-map-from-basis they are equal, so the $\varepsilon_i$ span.

2. If $\sum_i\lambda_i\varepsilon_i=0$, evaluating at $e_j$ gives $\lambda_j=0$. So the $\varepsilon_i$ are independent.

:::

$V\cong V^*$ in finite dimensions, but the isomorphism $e_i\mapsto\varepsilon_i$ depends on the basis. For infinite-dimensional $V$ the dual is strictly bigger: on $F[t]$, the functionals are determined by arbitrary sequences of values on $1,t,t^2,\dots$, so $F[t]^*\cong F^{\mathbb N}$.

::: {#prp-dual-basis-change .proposition name="How the dual basis changes"}

Let $\mathcal B,\mathcal B'$ be bases of $V$ with change of basis matrix $P$ (column $j$ of $P$ is $[e_j']_{\mathcal B}$), and let $\varepsilon_i,\varepsilon_i'$ be the dual bases. Then the change of basis matrix from $(\varepsilon_i)$ to $(\varepsilon_i')$ is $(P^{-1})^{\mathsf T}$.

:::

::: {.proof}

1. Write $\varepsilon_i'=\sum_k r_{ki}\varepsilon_k$, so column $i$ of $R=[r_{ki}]$ holds the coordinates of $\varepsilon_i'$.

2. Then $\delta_{ij}=\varepsilon_i'(e_j')=\sum_k r_{ki}\,\varepsilon_k\big(\sum_l p_{lj}e_l\big)=\sum_k r_{ki}p_{kj}=(R^{\mathsf T}P)_{ij}$.

3. So $R^{\mathsf T}P=I$, and $R=(P^{-1})^{\mathsf T}$.

:::

::: {#fig-dual-spaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x={(1cm,0)}, y={(0.5cm,0.6cm)}]
\draw[primary, faint] (-4.2,-2.2) -- (0.20,2.2);
\draw[accent, faint] (-2.6,-2) -- (2.6,-2);
\draw[primary, faint] (-3.2,-2.2) -- (1.20,2.2);
\draw[accent, faint] (-2.6,-1) -- (2.6,-1);
\draw[primary, faint] (-2.2,-2.2) -- (2.2,2.2);
\draw[accent, faint] (-2.6,0) -- (2.6,0);
\draw[primary, faint] (-1.20,-2.2) -- (3.2,2.2);
\draw[accent, faint] (-2.6,1) -- (2.6,1);
\draw[primary, faint] (-0.20,-2.2) -- (4.2,2.2);
\draw[accent, faint] (-2.6,2) -- (2.6,2);
\draw[->, emph, primary] (0,0) -- (1,0) node[below, lab] {$b_1$};
\draw[->, emph, secondary] (0,0) -- (1,1) node[above, lab] {$b_2$};
\fill[ink] (0,0) circle[pt];
\node[lab, note, primary] at (2.7,2.4) {$\beta_1=x-y$ constant}; \node[lab, note, accent, anchor=west] at (2.7,1) {$\beta_2=y$ constant};
\end{scope}
\end{tikzpicture}
\end{center}
```

The dual basis of $b_1=(1,0)$, $b_2=(1,1)$ is $\beta_1=x-y$, $\beta_2=y$, drawn by their level lines (axes sheared for clarity). $\beta_1$ is constant along $b_2$ and $\beta_2$ along $b_1$. Changing $b_2$ alone changes $\beta_1$, so dual bases change by the inverse transpose, not by the same matrix.

:::

Coordinates of vectors change by $P^{-1}$ and coordinates of functionals by $P^{\mathsf T}$: the number $\theta(v)$, a row times a column, does not depend on the basis.

::: {#def-annihilator .definition name="Annihilator"}

For a subspace $U\le V$, the *annihilator* of $U$ is
$$U^0=\{\theta\in V^*:\theta(u)=0\text{ for all }u\in U\}\ \le V^*.$$

:::

::: {#fig-dual-spaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[faint] (-4.4,-1.2) -- (0.4,1.2);
\node[lab, tick, left] at (-4.4,-1.2) {$\theta=-2$};
\draw[faint] (-3.4,-1.2) -- (1.4,1.2);
\draw[hl] (-2.4,-1.2) -- (2.4,1.2);
\draw[faint] (-1.4,-1.2) -- (3.4,1.2);
\draw[faint] (-0.4,-1.2) -- (4.4,1.2);
\node[lab, tick, right] at (4.4,1.2) {$\theta=2$};
\node[lab, above left] at (-0.2,1.2) {$U=\ker\theta$};
\draw[->, emph] (0,0) -- (1.6,0.8) node[lab, below right] {$u$};
\node[dot] at (0,0) {};
\end{tikzpicture}
\end{center}
```

A functional on $\mathbb R^2$ drawn by its level lines, here $\theta(x,y)=x-2y$. $\theta$ lies in the annihilator $U^0$ of the line $U$ exactly when its zero line contains $U$; up to scaling there is one such $\theta$, so $\dim U^0=2-1$.

:::

::: {#thm-dimension-of-annihilator .theorem name="Dimension of the annihilator"}

If $V$ is finite-dimensional and $U\le V$, then
$$\dim U+\dim U^0=\dim V.$$

:::

::: {.proof}

1. Extend a basis $e_1,\dots,e_k$ of $U$ to a basis $e_1,\dots,e_n$ of $V$, with dual basis $\varepsilon_1,\dots,\varepsilon_n$.

2. A functional $\theta=\sum\lambda_i\varepsilon_i$ (@thm-dual-basis) kills $U$ exactly when $\lambda_j=\theta(e_j)=0$ for $j\le k$.

3. So $\varepsilon_{k+1},\dots,\varepsilon_n$ is a basis of $U^0$, and $\dim U^0=n-k$.

:::

::: {#fig-dual-spaces-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.00,0.00) rectangle (0.75,0.45);
\draw[cell, fill=primaryLight] (0.75,0.00) rectangle (1.50,0.45);
\node[lab, tick] at (0.75,-0.22) {basis of $U$};
\draw[cell, fill=accentLight] (1.50,0.00) rectangle (2.25,0.45);
\draw[cell, fill=accentLight] (2.25,0.00) rectangle (3.00,0.45);
\draw[cell, fill=accentLight] (3.00,0.00) rectangle (3.75,0.45);
\node[lab, tick] at (2.62,-0.22) {extension};
\node[lab, anchor=east] at (-0.10,0.23) {$V$:};
\draw[cell frame] (0.00,-1.20) rectangle (0.75,-0.75);
\draw[cell frame] (0.75,-1.20) rectangle (1.50,-0.75);
\draw[cell, fill=accentLight] (1.50,-1.20) rectangle (2.25,-0.75);
\draw[cell, fill=accentLight] (2.25,-1.20) rectangle (3.00,-0.75);
\draw[cell, fill=accentLight] (3.00,-1.20) rectangle (3.75,-0.75);
\node[lab, tick] at (2.62,-1.42) {$\varepsilon_3,\varepsilon_4,\varepsilon_5$: basis of $U^0$};
\node[lab, anchor=east] at (-0.10,-0.97) {$V^*$:};
\node[lab, note, anchor=west] at (4.0,-0.5) {dual functionals of the extension kill $U$};
\end{tikzpicture}
\end{center}
```

Why $\dim U^0=\dim V-\dim U$: extend a basis of $U$ to one of $V$ and take the dual basis. The dual functionals of the added vectors vanish on $U$ and form a basis of $U^0$.

:::

::: {#exm-annihilator .example name="Annihilator of a plane"}

In $\mathbb R^3$ let $U$ be spanned by $(1,0,1)^{\mathsf T}$ and $(0,1,1)^{\mathsf T}$. A row $\mathbf a^{\mathsf T}=(a,b,c)$ kills $U$ when $a+c=0$ and $b+c=0$, so $U^0$ is spanned by $(1,1,-1)$: $\dim U+\dim U^0=2+1=3$. The annihilator plays the role of a normal vector without any inner product; for a matrix $A$, the annihilator of its column space is the left nullspace $N(A^{\mathsf T})$ read as rows.

:::

::: {#fig-dual-spaces-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x={(-0.5cm,-0.4cm)}, y={(1cm,0)}, z={(0,1cm)}]
\fill[tintA] (-1.2,-1.4,-2.6) -- (1.6,-1.4,0.2) -- (1.6,1.6,3.2) -- (-1.2,1.6,0.4) -- cycle;
\draw[->, emph, primary] (0,0,0) -- (1,0,1) node[left, lab, tick] {$(1,0,1)$}; \draw[->, emph, primary] (0,0,0) -- (0,1,1) node[right, lab, tick] {$(0,1,1)$};
\draw[->, emph, accent] (0,0,0) -- (0.6,0.6,-0.6) node[below, lab] {$(1,1,-1)$};
\fill[ink] (0,0,0) circle[pt];
\node[lab, note, primary] at (1.4,1.6,3.0) {$U$};
\end{scope}
\node[lab, note, anchor=west, align=left] at (2.6,0.3) {$U^0$: the row $(1,1,-1)$ and its multiples,\\the functionals that vanish on $U$;\\$\dim U+\dim U^0=2+1=3$};
\end{tikzpicture}
\end{center}
```

@exm-annihilator. The annihilator of a plane is spanned by one functional; drawn with the dot product it looks like a normal vector, but no inner product is needed to define it.

:::
