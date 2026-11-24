---
title: "Matrices of Linear Maps"
sources: [camib-la-2, mit1806-30]
requires: [math/linear-algebra/linear-maps/linear-maps-and-isomorphisms]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 2.2, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 defines the matrix of a transformation (def-matrix-of-linear-transformation) and states that it computes the map; the versions here prove that composition is matrix multiplication and that L(U,V) is isomorphic to a matrix space. Merge proposed to the owner. -->

<!-- Merged 2026-11-24 (owner): thm-matrix-represents-transformation (18.06 L30) merged into thm-matrix-of-linear-map (items 1 and 3); exm-matrix-of-derivative (18.06 L30) merged into exm-matrix-of-differentiation, from which the nullspace and image remark comes. -->

<!-- Merged 2026-11-20 (owner): def-matrix-of-linear-transformation (18.06 L30) merged into def-matrix-of-linear-map (same definition). -->

Once bases are chosen, a linear map between finite-dimensional spaces is the same thing as a matrix. Let $U$ have basis $\mathcal B=(e_1,\dots,e_m)$ and $V$ basis $\mathcal C=(f_1,\dots,f_n)$; write $[u]_{\mathcal B}\in F^m$ for the coordinate column of $u$.

::: {#def-matrix-of-linear-map .definition name="Matrix of a linear map"}

The *matrix* of $\alpha\in\mathcal L(U,V)$ with respect to $\mathcal B$ and $\mathcal C$ is the $n\times m$ matrix $A=[\alpha]_{\mathcal B,\mathcal C}$ defined by
$$\alpha(e_j)=\sum_{i=1}^na_{ij}f_i\qquad(j=1,\dots,m).$$
Column $j$ of $A$ is $[\alpha(e_j)]_{\mathcal C}$.

:::

::: {#fig-matrices-of-linear-maps-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.500) rectangle (0.600,1.100);
\node[lab] at (0.300,0.800) {$a_{11}$};
\draw[cell frame] (0.000,-0.100) rectangle (0.600,0.500);
\node[lab] at (0.300,0.200) {$a_{21}$};
\node[lab, tick] at (0.3,1.35) {$[\alpha(e_1)]$};
\draw[cell, fill=primaryLight] (1.000,0.500) rectangle (1.600,1.100);
\node[lab] at (1.300,0.800) {$a_{12}$};
\draw[cell, fill=primaryLight] (1.000,-0.100) rectangle (1.600,0.500);
\node[lab] at (1.300,0.200) {$a_{22}$};
\node[lab, tick] at (1.3,1.35) {$[\alpha(e_2)]$};
\draw[cell frame] (2.000,0.500) rectangle (2.600,1.100);
\node[lab] at (2.300,0.800) {$a_{13}$};
\draw[cell frame] (2.000,-0.100) rectangle (2.600,0.500);
\node[lab] at (2.300,0.200) {$a_{23}$};
\node[lab, tick] at (2.3,1.35) {$[\alpha(e_3)]$};
\node[lab, note, anchor=west, align=left] at (2.9,0.55) {column $j$ = coordinates of $\alpha(e_j)$ in the basis $f_1,f_2$:\\$\alpha(e_2)=a_{12}f_1+a_{22}f_2$};
\end{tikzpicture}
\end{center}
```

How to build $[\alpha]_{\mathcal B,\mathcal C}$ for $\alpha:U\to V$ with $\dim U=3$, $\dim V=2$: apply $\alpha$ to each basis vector of $U$ and write the result in the basis of $V$, one column at a time.

:::

::: {#thm-matrix-of-linear-map .theorem name="Linear maps are matrices"}

1. $[\alpha(u)]_{\mathcal C}=[\alpha]_{\mathcal B,\mathcal C}\,[u]_{\mathcal B}$ for every $u\in U$.
2. The map $\alpha\mapsto[\alpha]_{\mathcal B,\mathcal C}$ is an isomorphism $\mathcal L(U,V)\to\operatorname{Mat}_{n,m}(F)$. Hence $\dim\mathcal L(U,V)=\dim U\cdot\dim V$.
3. If $W$ has basis $\mathcal D$ and $\beta\in\mathcal L(V,W)$, then
$$[\beta\alpha]_{\mathcal B,\mathcal D}=[\beta]_{\mathcal C,\mathcal D}\,[\alpha]_{\mathcal B,\mathcal C}.$$

:::

::: {.proof}

1. If $u=\sum_j\lambda_je_j$, then $\alpha(u)=\sum_j\lambda_j\sum_ia_{ij}f_i=\sum_i\big(\sum_ja_{ij}\lambda_j\big)f_i$, whose coordinate column is $A[u]_{\mathcal B}$.

2. The map is linear, since $\alpha(e_j)+\beta(e_j)$ has coordinates the sum of those of $\alpha(e_j)$ and $\beta(e_j)$. It is bijective: by @thm-linear-map-from-basis, for any matrix $A$ there is exactly one $\alpha$ with $\alpha(e_j)=\sum_ia_{ij}f_i$. Then $\dim\mathcal L(U,V)=\dim\operatorname{Mat}_{n,m}(F)=nm$ by @thm-isomorphic-iff-same-dimension.

3. By item 1 applied twice, $[\beta\alpha(u)]_{\mathcal D}=[\beta]\,[\alpha(u)]_{\mathcal C}=[\beta]\,[\alpha]\,[u]_{\mathcal B}$ for every $u$. Taking $u=e_j$ shows that column $j$ of $[\beta\alpha]$ and of $[\beta][\alpha]$ agree.

:::

::: {#fig-matrices-of-linear-maps-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (U) at (0,0) {$U$};
\node[box] (V) at (3,0) {$V$};
\node[box] (W) at (6,0) {$W$};
\draw[->, emph] (U) -- (V) node[midway, above, lab] {$\alpha$};
\draw[->, emph] (V) -- (W) node[midway, above, lab] {$\beta$};
\draw[->, emph, accent] (U) to[bend right=30] node[below, lab] {$\beta\circ\alpha$} (W);
\node[lab, anchor=west] at (7.0,0) {$[\beta\alpha]_{\mathcal B,\mathcal D}=[\beta]_{\mathcal C,\mathcal D}\,[\alpha]_{\mathcal B,\mathcal C}$};
\end{tikzpicture}
\end{center}
```

Composing maps corresponds to multiplying their matrices, in the same order as the composition: the map applied first stands on the right. This is the reason matrix multiplication is defined as it is.

:::

::: {#fig-matrices-of-linear-maps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] (U) at (0,1.8) {$U$}; \node[lab] (V) at (3.2,1.8) {$V$};
\node[lab] (Fn) at (0,0) {$F^n$}; \node[lab] (Fm) at (3.2,0) {$F^m$};
\draw[map] (U) -- node[lab, above] {$\alpha$} (V);
\draw[map] (Fn) -- node[lab, below] {$[\alpha]_{\mathcal B,\mathcal C}$} (Fm);
\draw[map] (U) -- node[lab, left] {$[\,\cdot\,]_{\mathcal B}$} (Fn);
\draw[map] (V) -- node[lab, right] {$[\,\cdot\,]_{\mathcal C}$} (Fm);
\end{tikzpicture}
\end{center}
```

Coordinates turn the map into a matrix: going right then down equals going down then right, $[\alpha(u)]_{\mathcal C}=[\alpha]_{\mathcal B,\mathcal C}[u]_{\mathcal B}$. For differentiation (@exm-matrix-of-differentiation), $p\mapsto p'$ on top is $(1,1,1,1)^{\mathsf T}\mapsto(1,2,3)^{\mathsf T}$ below.

:::

Item 3 is the reason matrix multiplication is defined the way it is (@def-matrix-product): it is composition of maps written in coordinates. Associativity of the matrix product follows at once from associativity of composition.

::: {#exm-matrix-of-differentiation .example name="Differentiation as a matrix"}

Let $U=F[t]_{\le3}$ with basis $\mathcal B=(1,t,t^2,t^3)$ and $V=F[t]_{\le2}$ with basis $\mathcal C=(1,t,t^2)$. Differentiation $D:U\to V$ sends $1,t,t^2,t^3$ to $0,1,2t,3t^2$, so
$$[D]_{\mathcal B,\mathcal C}=\begin{bmatrix}0&1&0&0\\0&0&2&0\\0&0&0&3\end{bmatrix}.$$
For $p=1+t+t^2+t^3$, $[p]_{\mathcal B}=(1,1,1,1)^{\mathsf T}$ and $[D]\,[p]_{\mathcal B}=(1,2,3)^{\mathsf T}$, the coordinates of $p'=1+2t+3t^2$. The nullspace of $D$ is the constants and its image is all of $V$, matching the calculus. Over a field where $3=0$, such as $\mathbb F_3$, the same matrix has a zero last column, and $D(t^3)=0$.

:::

::: {#fig-matrices-of-linear-maps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\node[lab] at (0.275,1.375) {$0$};
\draw[cell, fill=primaryLight] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$0$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\node[lab] at (1.925,1.375) {$0$};
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\node[lab] at (0.275,0.825) {$0$};
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\node[lab] at (0.825,0.825) {$0$};
\draw[cell, fill=primaryLight] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$2$};
\draw[cell frame] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$0$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$0$};
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$0$};
\draw[cell, fill=primaryLight] (1.650,-0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$3$};
\node[lab, note] at (1.100,-0.350) {$[D]_{\mathcal B,\mathcal C}$};
\draw[cell frame] (2.450,1.375) rectangle (3.000,1.925);
\node[lab] at (2.725,1.650) {$1$};
\draw[cell frame] (2.450,0.825) rectangle (3.000,1.375);
\node[lab] at (2.725,1.100) {$1$};
\draw[cell frame] (2.450,0.275) rectangle (3.000,0.825);
\node[lab] at (2.725,0.550) {$1$};
\draw[cell frame] (2.450,-0.275) rectangle (3.000,0.275);
\node[lab] at (2.725,-0.000) {$1$};
\node[lab, note] at (2.725,-0.625) {$[p]_{\mathcal B}$};
\node[lab] at (3.3,0.825) {$=$};
\draw[hl cell] (3.600,1.100) rectangle (4.150,1.650);
\node[lab] at (3.875,1.375) {$1$};
\draw[hl cell] (3.600,0.550) rectangle (4.150,1.100);
\node[lab] at (3.875,0.825) {$2$};
\draw[hl cell] (3.600,-0.000) rectangle (4.150,0.550);
\node[lab] at (3.875,0.275) {$3$};
\node[lab, note] at (3.875,-0.350) {$[p']_{\mathcal C}$};
\node[lab, note, anchor=west, align=left] at (4.5,0.825) {$p=1+t+t^2+t^3$\\$p'=1+2t+3t^2$};
\end{tikzpicture}
\end{center}
```

@exm-matrix-of-differentiation: multiplying the coordinate column of $p$ by the matrix of $D$ gives the coordinate column of $p'$. Column $j$ of the matrix holds the coordinates of the derivative of the $j$-th basis polynomial.

:::

::: {#rmk-matrices-of-linear-maps-1 .remark name="Maps first, matrices second"}

A matrix depends on two choices of basis; the map does not. Statements that are true of the map, such as "$\alpha$ is injective" or "$\dim\ker\alpha=2$", are true of every matrix representing it. The next notes ask which properties of a matrix survive a change of basis: for maps $U\to V$ only the rank (@thm-rank-normal-form), for maps $V\to V$ much more (@sec-math-linear-algebra-endomorphisms-eigenvalues-of-endomorphisms).

:::
