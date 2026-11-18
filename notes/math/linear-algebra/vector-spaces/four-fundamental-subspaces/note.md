---
title: "The Four Fundamental Subspaces"
sources: [mit1806-10]
requires: [math/linear-algebra/vector-spaces/independence-basis-dimension]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.06SC (Fall 2011), Lecture 10, in our own wording; proofs written out in steps. Example numbers checked with sympy. -->

::: {#def-four-fundamental-subspaces .definition name="The four fundamental subspaces"}

An $m\times n$ matrix $A$ has four subspaces:

1. the *column space* $C(A)\subseteq\mathbb{R}^m$;
2. the *nullspace* $N(A)\subseteq\mathbb{R}^n$;
3. the *row space* $C(A^{\mathsf T})\subseteq\mathbb{R}^n$, all combinations of the rows;
4. the *left nullspace* $N(A^{\mathsf T})\subseteq\mathbb{R}^m$, all $\mathbf{y}$ with $A^{\mathsf T}\mathbf{y}=\mathbf{0}$, equivalently $\mathbf{y}^{\mathsf T}A=\mathbf{0}^{\mathsf T}$.

:::

::: {#thm-fundamental-theorem-dimensions .theorem name="Dimensions of the four subspaces"}

If $A$ is $m\times n$ with rank $r$, then
$$\dim C(A)=\dim C(A^{\mathsf T})=r,\qquad \dim N(A)=n-r,\qquad \dim N(A^{\mathsf T})=m-r.$$
In particular row rank equals column rank.

:::

::: {.proof}

1. **Row space.** Elimination $EA=R$ ($E$ invertible) replaces rows by combinations of rows and can be undone, so $C(A^{\mathsf T})=C(R^{\mathsf T})$. The $r$ nonzero rows of $R$ are independent (each has a $1$ in a pivot column where the others have $0$) and span it. So $\dim C(A^{\mathsf T})=r$.

2. **Column space.** The pivot columns of $A$ are a basis of $C(A)$ (@exm-basis-of-column-space): $A\mathbf{x}=\mathbf{0}\iff R\mathbf{x}=\mathbf{0}$, so the same columns are independent in $A$ as in $R$, and every other column is a combination of the pivot columns in both. So $\dim C(A)=r$.

3. **Nullspace.** The $n-r$ special solutions are a basis of $N(A)$ by @thm-special-solutions.

4. **Left nullspace.** Apply step 3 to the $n\times m$ matrix $A^{\mathsf T}$, whose rank is $\dim C(A^{\mathsf T})=r$ by step 1: $\dim N(A^{\mathsf T})=m-r$.

:::

::: {#prp-left-nullspace-from-elimination .proposition name="A basis for the left nullspace"}

If $EA=R$ with $E$ invertible and the last $m-r$ rows of $R$ zero, then the last $m-r$ rows of $E$ are a basis of $N(A^{\mathsf T})$ (as row vectors $\mathbf{y}^{\mathsf T}$ with $\mathbf{y}^{\mathsf T}A=\mathbf{0}^{\mathsf T}$).

:::

::: {.proof}

1. Row $i$ of $EA$ is (row $i$ of $E$)$\,A$. For $i>r$ this is a zero row of $R$.

2. These $m-r$ rows of the invertible $E$ are independent, and $\dim N(A^{\mathsf T})=m-r$, so they form a basis (@cor-basis-from-independent-set).

:::

::: {#exm-four-subspaces .example name="The four subspaces of a 3 by 4 matrix"}

For $A=\begin{bmatrix}1&2&0&1\\2&4&1&4\\3&6&1&5\end{bmatrix}$ (rank $2$, @exm-nullspace-three-by-four):

| subspace | dimension | basis |
|---|---|---|
| $C(A)\subseteq\mathbb{R}^3$ | $2$ | $(1,2,3)$, $(0,1,1)$ |
| $C(A^{\mathsf T})\subseteq\mathbb{R}^4$ | $2$ | $(1,2,0,1)$, $(0,0,1,2)$ |
| $N(A)\subseteq\mathbb{R}^4$ | $2$ | $(-2,1,0,0)$, $(-1,0,-2,1)$ |
| $N(A^{\mathsf T})\subseteq\mathbb{R}^3$ | $1$ | $(-1,-1,1)$ |

The left nullspace vector records the dependence among the rows: $-(\text{row }1)-(\text{row }2)+(\text{row }3)=\mathbf{0}$.

:::

::: {#fig-four-fundamental-subspaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0.9) rectangle (3,2.6);
\draw[regionB] (0,-0.9) rectangle (3,0.7);
\draw[regionA] (5.2,0.9) rectangle (8.2,2.6);
\draw[regionB] (5.2,-0.9) rectangle (8.2,0.7);
\node[lab, align=center] at (1.5,1.75) {row space $C(A^{\mathsf T})$\\ $\dim r$};
\node[lab, align=center] at (1.5,-0.1) {nullspace $N(A)$\\ $\dim n-r$};
\node[lab, align=center] at (6.7,1.75) {column space $C(A)$\\ $\dim r$};
\node[lab, align=center] at (6.7,-0.1) {left nullspace $N(A^{\mathsf T})$\\ $\dim m-r$};
\node[lab] at (1.5,3.0) {$\mathbb{R}^n$};
\node[lab] at (6.7,3.0) {$\mathbb{R}^m$};
\draw[->, emph] (3.1,1.9) -- node[lab, above] {$A\mathbf{x}_r=\mathbf b$} (5.1,1.9);
\draw[->, emph] (3.1,-0.1) -- node[lab, above] {$A\mathbf{x}_n=\mathbf 0$} (5.1,1.3);
\end{tikzpicture}
\end{center}
```

The four subspaces of an $m\times n$ matrix of rank $r$. $A$ maps the row space onto the column space and the nullspace to $\mathbf 0$; each pair is orthogonal.

:::

::: {#rmk-four-fundamental-subspaces-1 .remark name="The big picture"}

$\mathbb{R}^n$ holds the row space ($r$) and the nullspace ($n-r$); $\mathbb{R}^m$ holds the column space ($r$) and the left nullspace ($m-r$). The note @sec-math-linear-algebra-orthogonality-orthogonal-subspaces shows that each pair is orthogonal and fills its space.

:::
