---
title: "The Nullspace and Solving Ax = 0"
sources: [mit1806-6, mit1806-7]
requires: [math/linear-algebra/vector-spaces/vector-spaces-and-subspaces]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lectures 6 and 7, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-nullspace .definition name="Nullspace"}

The *nullspace* of an $m\times n$ matrix $A$ is
$$N(A)=\{\mathbf{x}\in\mathbb{R}^n: A\mathbf{x}=\mathbf{0}\}.$$
It is a subspace of $\mathbb{R}^n$: if $A\mathbf{x}=A\mathbf{y}=\mathbf{0}$ then $A(c\mathbf{x}+d\mathbf{y})=\mathbf{0}$.

:::

By contrast, the solutions of $A\mathbf{x}=\mathbf{b}$ with $\mathbf{b}\neq\mathbf{0}$ never form a subspace: $\mathbf{0}$ is not a solution.

## Echelon form and reduced row echelon form

Elimination works on rectangular matrices too. When a column has no pivot (all entries at or below the current row are zero), move on to the next column.

::: {#def-echelon-form .definition name="Echelon form, pivot and free variables"}

Elimination on an $m\times n$ matrix $A$ produces an *echelon* (staircase) matrix $U$: the first nonzero entry of each row, its *pivot*, lies to the right of the pivot in the row above, and zero rows come last. The number of pivots is the *rank* $r$ of $A$. The unknowns that belong to pivot columns are *pivot variables*; the other $n-r$ are *free variables*.

:::

::: {#fig-nullspace-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (3.3,-2.2);
\draw[bold, accent] (0,-0.55) -- (0,0) -- (0.55,0) -- (0.55,-0.55) -- (1.65,-0.55) -- (1.65,-1.1) -- (2.2,-1.1) -- (2.2,-1.65) -- (3.3,-1.65);
\draw[hl cell] (0.0,0.0) rectangle (0.55,-0.55); \node[lab] at (0.275,-0.275) {$p$};
\draw[hl cell] (0.55,-0.55) rectangle (1.1,-1.1); \node[lab] at (0.83,-0.83) {$p$};
\draw[hl cell] (1.65,-1.1) rectangle (2.2,-1.65); \node[lab] at (1.93,-1.375) {$p$};
\node[lab] at (0.83,-0.275) {$*$};
\node[lab] at (1.375,-0.275) {$*$};
\node[lab] at (1.93,-0.275) {$*$};
\node[lab] at (2.475,-0.275) {$*$};
\node[lab] at (3.03,-0.275) {$*$};
\node[lab] at (1.375,-0.83) {$*$};
\node[lab] at (1.93,-0.83) {$*$};
\node[lab] at (2.475,-0.83) {$*$};
\node[lab] at (3.03,-0.83) {$*$};
\node[lab] at (2.475,-1.375) {$*$};
\node[lab] at (3.03,-1.375) {$*$};
\node[lab, muted] at (0.275,-0.83) {$0$};
\node[lab, muted] at (0.275,-1.375) {$0$};
\node[lab, muted] at (0.83,-1.375) {$0$};
\node[lab, muted] at (1.375,-1.375) {$0$};
\node[lab, muted] at (0.275,-1.93) {$0$};
\node[lab, muted] at (0.83,-1.93) {$0$};
\node[lab, muted] at (1.375,-1.93) {$0$};
\node[lab, muted] at (1.93,-1.93) {$0$};
\node[lab, muted] at (2.475,-1.93) {$0$};
\node[lab, muted] at (3.03,-1.93) {$0$};
\node[lab, note, anchor=west, align=left] at (3.6,-1.1) {$p$: pivots (nonzero)\\$*$: any entries\\below the staircase: zeros\\pivot columns $1,2,4$; free $3,5,6$};
\end{tikzpicture}
\end{center}
```

The shape of an echelon matrix, $4\times6$ of rank $3$. Each pivot is to the right of the one above it, everything below the staircase is zero, and the columns without pivots belong to the free variables.

:::

::: {#def-reduced-row-echelon-form .definition name="Reduced row echelon form"}

Continuing elimination upwards to clear the entries above each pivot, and dividing each pivot row by its pivot, produces the *reduced row echelon form* $R=\operatorname{rref}(A)$: every pivot is $1$ and is the only nonzero entry in its column. Row operations do not change the nullspace, so
$$N(A)=N(U)=N(R).$$

:::

::: {#thm-special-solutions .theorem name="Special solutions span the nullspace"}

Let $A$ have rank $r$ and $n-r$ free variables. For each free variable, set it to $1$, the other free variables to $0$, and solve $R\mathbf{x}=\mathbf{0}$ for the pivot variables. These $n-r$ *special solutions* are in $N(A)$ and every vector of $N(A)$ is exactly one combination of them.

:::

::: {.proof}

1. In $R$, each nonzero row reads $x_{p}+\sum_{f\text{ free}}r_{f}x_f=0$ for its pivot variable $x_p$. So the free variables can be chosen at will and then determine the pivot variables uniquely.

2. A special solution is such a choice, so it lies in $N(R)=N(A)$.

3. Let $\mathbf{x}\in N(A)$ have free variables $x_{f_1},\dots,x_{f_{n-r}}$. The combination $\mathbf{y}=\sum_kx_{f_k}\mathbf{s}_k$ of the special solutions has the same free variables and is in $N(A)$. By step 1 the pivot variables agree too, so $\mathbf{x}=\mathbf{y}$.

4. The coefficients are forced to be the free variables of $\mathbf{x}$, so the combination is unique.

:::

::: {#fig-nullspace-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[cell, fill=primaryLight] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$2$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell, fill=primaryLight] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$1$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[cell, fill=primaryLight] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$0$};
\draw[hl cell] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell, fill=primaryLight] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$2$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$0$};
\draw[cell frame] (1.650,-0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$0$};
\node[lab, note] at (1.100,-0.350) {$R$: free columns $2,4$ shaded};
\draw[cell frame] (3.200,1.450) rectangle (3.750,2.000);
\node[lab] at (3.475,1.725) {$-2$};
\draw[hl cell] (3.200,0.900) rectangle (3.750,1.450);
\node[lab] at (3.475,1.175) {$1$};
\draw[cell frame] (3.200,0.350) rectangle (3.750,0.900);
\node[lab] at (3.475,0.625) {$0$};
\draw[cell, fill=primaryLight] (3.200,-0.200) rectangle (3.750,0.350);
\node[lab] at (3.475,0.075) {$0$};
\node[lab, note] at (3.475,-0.550) {$\mathbf s_1$};
\draw[cell frame] (4.600,1.450) rectangle (5.150,2.000);
\node[lab] at (4.875,1.725) {$-1$};
\draw[cell, fill=primaryLight] (4.600,0.900) rectangle (5.150,1.450);
\node[lab] at (4.875,1.175) {$0$};
\draw[cell frame] (4.600,0.350) rectangle (5.150,0.900);
\node[lab] at (4.875,0.625) {$-2$};
\draw[hl cell] (4.600,-0.200) rectangle (5.150,0.350);
\node[lab] at (4.875,0.075) {$1$};
\node[lab, note] at (4.875,-0.550) {$\mathbf s_2$};
\node[lab, note, anchor=west, align=left] at (5.6,0.9) {set one free variable to $1$,\\the others to $0$ (highlighted);\\the pivot variables are\\minus the shaded entries of $R$};
\end{tikzpicture}
\end{center}
```

Reading the special solutions of @exm-nullspace-three-by-four from $R$. For $\mathbf s_1$ the free variables are $x_2=1$, $x_4=0$, and the pivot rows give $x_1=-2$, $x_3=0$; for $\mathbf s_2$, $x_2=0$, $x_4=1$ give $x_1=-1$, $x_3=-2$.

:::

::: {#cor-more-unknowns-than-equations .corollary name="More unknowns than equations"}

If $n>m$, then $A\mathbf{x}=\mathbf{0}$ has a nonzero solution.

:::

::: {.proof}

1. There is at most one pivot per row, so $r\le m<n$.

2. Hence there is at least one free variable, and its special solution is nonzero.

:::

::: {#fig-nullspace-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (4.4,-1.2);
\draw[decorate, decoration={brace, amplitude=3pt, mirror}] (-0.1,0) -- (-0.1,-1.2) node[midway, left=3pt, lab, tick] {$m$};
\draw[decorate, decoration={brace, amplitude=3pt}] (0,0.1) -- (4.4,0.1) node[midway, above=3pt, lab, tick] {$n>m$};
\draw[hl cell] (0,0) rectangle (1.6,-1.2); \node[lab, note] at (0.8,-0.6) {$\le m$ pivots};
\fill[tintB] (1.6,0) rectangle (4.4,-1.2); \node[lab, note] at (3.0,-0.6) {$\ge n-m$ free};
\end{tikzpicture}
\end{center}
```

A wide matrix: there are at most $m$ pivots, one per row, so at least $n-m$ columns are free (drawn together, though in general they are spread out). Each free column gives a special solution, so $N(A)\ne\{\mathbf 0\}$.

:::

::: {#exm-nullspace-three-by-four .example name="Nullspace of a 3 by 4 matrix"}

$$A=\begin{bmatrix}1&2&0&1\\2&4&1&4\\3&6&1&5\end{bmatrix}\ \longrightarrow\ R=\begin{bmatrix}1&2&0&1\\0&0&1&2\\0&0&0&0\end{bmatrix}.$$
The pivot columns are $1$ and $3$, so $r=2$ and $x_2,x_4$ are free. The special solutions are
$$\mathbf{s}_1=(-2,1,0,0),\qquad\mathbf{s}_2=(-1,0,-2,1),$$
and $N(A)$ is the plane of all $c\,\mathbf{s}_1+d\,\mathbf{s}_2$ in $\mathbb{R}^4$.

:::

::: {#fig-nullspace-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.75]
\foreach \i/\j/\v in {1/1/1,1/2/2,1/3/0,1/4/1,2/1/0,2/2/0,2/3/1,2/4/2,3/1/0,3/2/0,3/3/0,3/4/0} \draw[cell frame] (\j-1,-\i) rectangle node[lab] {$\v$} (\j,-\i+1);
\foreach \j in {2,4} \fill[tintB] (\j-1,-3) rectangle (\j,0);
\draw[hl cell] (0,-1) rectangle node[lab] {$1$} (1,0);
\draw[hl cell] (2,-2) rectangle node[lab] {$1$} (3,-1);
\draw[emph, primary] (0,0) -- (0,-1) -- (2,-1) -- (2,-2) -- (4,-2);
\foreach \j/\t in {1/pivot,2/free,3/pivot,4/free} \node[tick] at (\j-0.5,0.35) {\t};
\node[lab, left] at (-0.2,-1.5) {$R=$};
\end{tikzpicture}
\end{center}
```

The reduced matrix $R$ of @exm-nullspace-three-by-four. The staircase separates the pivots (highlighted, columns $1$ and $3$) from the zeros below; the shaded columns $2$ and $4$ have no pivot, so $x_2$ and $x_4$ are free and give the special solutions.

:::

::: {#prp-nullspace-matrix .proposition name="The nullspace matrix"}

If the pivot columns come first, $R=\begin{bmatrix}I&F\\0&0\end{bmatrix}$ with $F$ of size $r\times(n-r)$. Then the special solutions are the columns of
$$N=\begin{bmatrix}-F\\I\end{bmatrix},\qquad RN=0.$$
In general the rows of $N$ are placed in the order of the variables.

:::

::: {.proof}

1. By block multiplication (@prp-block-multiplication), $RN=\begin{bmatrix}-F+F\\0\end{bmatrix}=0$.

2. Column $k$ of $N$ has free part equal to column $k$ of $I$, which is the choice that defines the $k$-th special solution in @thm-special-solutions.

:::

::: {#fig-nullspace-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,1.650) rectangle (0.550,2.200);
\node[lab] at (0.275,1.925) {$-2$};
\draw[cell, fill=primaryLight] (0.550,1.650) rectangle (1.100,2.200);
\node[lab] at (0.825,1.925) {$-1$};
\draw[hl cell] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$1$};
\draw[hl cell] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$0$};
\draw[cell, fill=primaryLight] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[cell, fill=primaryLight] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$-2$};
\draw[hl cell] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[hl cell] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$1$};
\node[lab, note] at (0.550,-0.350) {$N$};
\node[lab, note, anchor=west] at (1.4,1.925) {pivot row $x_1$: $-F$};
\node[lab, note, anchor=west] at (1.4,1.375) {free row $x_2$: $I$};
\node[lab, note, anchor=west] at (1.4,0.825) {pivot row $x_3$: $-F$};
\node[lab, note, anchor=west] at (1.4,0.275) {free row $x_4$: $I$};
\node[lab, anchor=west] at (5,1.1) {$R=\begin{bmatrix}I&F\end{bmatrix}$ (columns reordered),\quad $F=\begin{bmatrix}2&1\\0&2\end{bmatrix}$};
\end{tikzpicture}
\end{center}
```

The nullspace matrix $N$ of @exm-nullspace-three-by-four has the special solutions as columns. Its free rows form the identity and its pivot rows form $-F$, so $RN=0$.

:::
