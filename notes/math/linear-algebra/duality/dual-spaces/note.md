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

::: {#exm-annihilator .example name="Annihilator of a plane"}

In $\mathbb R^3$ let $U$ be spanned by $(1,0,1)^{\mathsf T}$ and $(0,1,1)^{\mathsf T}$. A row $\mathbf a^{\mathsf T}=(a,b,c)$ kills $U$ when $a+c=0$ and $b+c=0$, so $U^0$ is spanned by $(1,1,-1)$: $\dim U+\dim U^0=2+1=3$. The annihilator plays the role of a normal vector without any inner product; for a matrix $A$, the annihilator of its column space is the left nullspace $N(A^{\mathsf T})$ read as rows.

:::
