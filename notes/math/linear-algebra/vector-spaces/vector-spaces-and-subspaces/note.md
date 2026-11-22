---
title: "Vector Spaces and Subspaces"
sources: [mit1806-5, mit1806-6]
requires: [math/linear-algebra/systems/transposes-and-permutations]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 5 (second half) and Lecture 6, in our own wording; proofs written out in steps. -->

::: {#def-vector-space .definition name="Vector space"}

A *(real) vector space* is a set $V$ with an addition $\mathbf{v}+\mathbf{w}\in V$ and a scalar multiplication $c\mathbf{v}\in V$ (for $c\in\mathbb{R}$) such that for all $\mathbf{u},\mathbf{v},\mathbf{w}\in V$ and $c,d\in\mathbb{R}$:

1. $\mathbf{v}+\mathbf{w}=\mathbf{w}+\mathbf{v}$ and $(\mathbf{u}+\mathbf{v})+\mathbf{w}=\mathbf{u}+(\mathbf{v}+\mathbf{w})$;
2. there is a zero vector $\mathbf{0}$ with $\mathbf{v}+\mathbf{0}=\mathbf{v}$, and each $\mathbf{v}$ has a $-\mathbf{v}$ with $\mathbf{v}+(-\mathbf{v})=\mathbf{0}$;
3. $1\mathbf{v}=\mathbf{v}$ and $(cd)\mathbf{v}=c(d\mathbf{v})$;
4. $c(\mathbf{v}+\mathbf{w})=c\mathbf{v}+c\mathbf{w}$ and $(c+d)\mathbf{v}=c\mathbf{v}+d\mathbf{v}$.

:::

The main example is $\mathbb{R}^n$. Others: the $m\times n$ real matrices, the real functions on an interval, the polynomials of degree at most $k$. In each, linear combinations (@def-linear-combination) stay inside the space.

::: {#def-subspace .definition name="Subspace"}

A *subspace* of a vector space $V$ is a nonempty subset $W\subseteq V$ that is closed under linear combinations:
$$\mathbf{v},\mathbf{w}\in W,\ c,d\in\mathbb{R}\ \Longrightarrow\ c\mathbf{v}+d\mathbf{w}\in W.$$
A subspace is itself a vector space with the same operations.

:::

::: {#prp-subspace-contains-zero .proposition name="Every subspace contains the zero vector"}

If $W$ is a subspace then $\mathbf{0}\in W$.

:::

::: {.proof}

1. $W$ is nonempty; take any $\mathbf{w}\in W$.

2. Then $0\mathbf{w}+0\mathbf{w}=\mathbf{0}\in W$.

:::

::: {#exm-subspaces-of-r3 .example name="The subspaces of R^3"}

The subspaces of $\mathbb{R}^3$ are: $\{\mathbf{0}\}$; every line through $\mathbf{0}$; every plane through $\mathbf{0}$; and $\mathbb{R}^3$ itself. A line or plane that misses the origin is not a subspace. Neither is the first quadrant of $\mathbb{R}^2$ (not closed under multiplication by $-1$), nor the union of two different lines through $\mathbf{0}$ (not closed under addition).

:::

::: {#fig-vector-spaces-and-subspaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[shift={(0,0)}]
\draw[->, muted] (-1.3,0) -- (1.4,0);
\draw[->, muted] (0,-1.3) -- (0,1.4);
\draw[emph, primary] (-1.2,-0.1) -- (1.2,1.1);
\fill[accent] (0,0) circle[pt];
\node[lab, note, align=center] at (0,-1.75) {line missing $\mathbf 0$};
\end{scope}
\begin{scope}[shift={(3.4,0)}]
\draw[->, muted] (-1.3,0) -- (1.4,0);
\draw[->, muted] (0,-1.3) -- (0,1.4);
\fill[tintA] (0,0) rectangle (1.2,1.2);
\draw[->, emph, primary] (0,0) -- (0.8,0.5) node[right, lab] {$\mathbf v$};
\draw[->, emph, accent] (0,0) -- (-0.8,-0.5) node[left, lab] {$-\mathbf v$};
\node[lab, note, align=center] at (0,-1.75) {first quadrant:\\$-\mathbf v$ leaves it};
\end{scope}
\begin{scope}[shift={(6.8,0)}]
\draw[->, muted] (-1.3,0) -- (1.4,0);
\draw[->, muted] (0,-1.3) -- (0,1.4);
\draw[emph, primary] (-1.2,0) -- (1.2,0); \draw[emph, primary] (0,-1.2) -- (0,1.2);
\draw[->, emph, secondary] (0,0) -- (0.8,0) node[above, lab] {};
\draw[->, emph, secondary] (0,0) -- (0,0.7) node[above, lab] {};
\draw[->, emph, accent] (0,0) -- (0.8,0.7) node[right, lab] {$\mathbf v+\mathbf w$};
\node[lab, note, align=center] at (0,-1.75) {two lines:\\the sum leaves them};
\end{scope}
\end{tikzpicture}
\end{center}
```

Three sets that are not subspaces, from @exm-subspaces-of-r3 (drawn in the plane). The first does not contain $\mathbf 0$; the second is not closed under multiplication by $-1$; the third is not closed under addition.

:::

::: {#fig-vector-spaces-and-subspaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x={(-0.5cm,-0.4cm)}, y={(1cm,0cm)}, z={(0cm,1cm)}, scale=1.2]
\fill[tintA] (-1.5,-1.5,0) -- (1.5,-1.5,0) -- (1.5,2,0) -- (-1.5,2,0) -- cycle;
\draw[primary] (-1.5,-1.5,0) -- (1.5,-1.5,0) -- (1.5,2,0) -- (-1.5,2,0) -- cycle;
\draw[faint] (0,0,0) -- (2.2,0,0); \draw[faint] (0,0,0) -- (0,2.6,0); \draw[faint] (0,0,0) -- (0,0,2.3);
\draw[emph, accent] (-0.5,-0.9,-0.7) -- (1.1,2,1.54) node[lab, above right] {line through $\mathbf 0$};
\draw[emph, muted, dashed] (1,1.8,1.3) -- (-1,-1.2,1.3) node[lab, left] {line missing $\mathbf 0$};
\node[hl dot] at (0,0,0) {};
\node[lab, below left] at (0,0,0) {$\{\mathbf 0\}$};
\node[lab, primary] at (1.3,2.1,0) {plane through $\mathbf 0$};
\end{tikzpicture}
\end{center}
```

Subspaces of $\mathbb R^3$ (@exm-subspaces-of-r3): $\{\mathbf 0\}$, lines and planes through $\mathbf 0$, and $\mathbb R^3$. The dashed line misses the origin, so it is not a subspace.

:::

::: {#prp-intersection-of-subspaces .proposition name="Intersection of subspaces"}

If $S$ and $T$ are subspaces of $V$, then $S\cap T$ is a subspace. The union $S\cup T$ is in general not a subspace.

:::

::: {.proof}

1. $\mathbf{0}\in S\cap T$, so it is nonempty.

2. If $\mathbf{v},\mathbf{w}\in S\cap T$, then $c\mathbf{v}+d\mathbf{w}$ lies in $S$ and in $T$, because each is closed under combinations.

3. For the union, two different lines through $\mathbf{0}$ in $\mathbb{R}^2$ are a counterexample (@exm-subspaces-of-r3).

:::

::: {#fig-vector-spaces-and-subspaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x={(-0.5cm,-0.4cm)}, y={(1cm,0)}, z={(0,1cm)}]
\fill[tintA] (-1.2,-1.5,0) -- (1.8,-1.5,0) -- (1.8,1.8,0) -- (-1.2,1.8,0) -- cycle;
\fill[tintC] (-1.2,0,-1) -- (1.8,0,-1) -- (1.8,0,1.6) -- (-1.2,0,1.6) -- cycle;
\draw[bold, accent] (-1.2,0,0) -- (1.8,0,0);
\fill[ink] (0,0,0) circle[pt];
\node[lab, note, primary] at (0,1.7,0.2) {plane $z=0$}; \node[lab, note, secondary] at (0,0,1.85) {plane $y=0$};
\node[lab, note, accent] at (2.1,0,0.25) {$x$-axis};
\end{scope}
\end{tikzpicture}
\end{center}
```

Two planes through $\mathbf 0$ in $\mathbb R^3$ meet in a line through $\mathbf 0$: the intersection of subspaces is a subspace. Their union is not one.

:::

::: {#def-column-space .definition name="Column space"}

The *column space* $C(A)$ of an $m\times n$ matrix $A$ is the set of all linear combinations of its columns. It is a subspace of $\mathbb{R}^m$.

:::

::: {#thm-column-space-solvability .theorem name="Ax = b is solvable exactly when b is in C(A)"}

$A\mathbf{x}=\mathbf{b}$ has a solution if and only if $\mathbf{b}\in C(A)$. Equivalently $C(A)=\{A\mathbf{x}:\mathbf{x}\in\mathbb{R}^n\}$.

:::

::: {.proof}

1. By @def-matrix-times-vector, $A\mathbf{x}=x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$ is a combination of the columns.

2. So the vectors $A\mathbf{x}$ are exactly the combinations of the columns, and $\mathbf{b}=A\mathbf{x}$ for some $\mathbf{x}$ exactly when $\mathbf{b}\in C(A)$.

3. $C(A)$ is a subspace: $c\,A\mathbf{x}+d\,A\mathbf{y}=A(c\mathbf{x}+d\mathbf{y})$.

:::

::: {#exm-column-space-plane .example name="A column space that is a plane"}

For $A=\begin{bmatrix}1&1&2\\2&1&3\\3&1&4\\4&1&5\end{bmatrix}$ the third column is the sum of the first two, so $C(A)$ is the plane in $\mathbb{R}^4$ spanned by $(1,2,3,4)$ and $(1,1,1,1)$. Four equations in three unknowns are solvable only for $\mathbf{b}$ in that plane.

:::
