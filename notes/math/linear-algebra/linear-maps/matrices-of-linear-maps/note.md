---
title: "Matrices of Linear Maps"
sources: [camib-la-2, mit1806-30]
requires: [math/linear-algebra/linear-maps/linear-maps-and-isomorphisms]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 2.2, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 defines the matrix of a transformation (def-matrix-of-linear-transformation) and states that it computes the map; the versions here prove that composition is matrix multiplication and that L(U,V) is isomorphic to a matrix space. Merge proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): def-matrix-of-linear-transformation (18.06 L30) merged into def-matrix-of-linear-map (same definition). -->

Once bases are chosen, a linear map between finite-dimensional spaces is the same thing as a matrix. Let $U$ have basis $\mathcal B=(e_1,\dots,e_m)$ and $V$ basis $\mathcal C=(f_1,\dots,f_n)$; write $[u]_{\mathcal B}\in F^m$ for the coordinate column of $u$.

::: {#def-matrix-of-linear-map .definition name="Matrix of a linear map"}

The *matrix* of $\alpha\in\mathcal L(U,V)$ with respect to $\mathcal B$ and $\mathcal C$ is the $n\times m$ matrix $A=[\alpha]_{\mathcal B,\mathcal C}$ defined by
$$\alpha(e_j)=\sum_{i=1}^na_{ij}f_i\qquad(j=1,\dots,m).$$
Column $j$ of $A$ is $[\alpha(e_j)]_{\mathcal C}$.

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
For $p=1+t+t^2+t^3$, $[p]_{\mathcal B}=(1,1,1,1)^{\mathsf T}$ and $[D]\,[p]_{\mathcal B}=(1,2,3)^{\mathsf T}$, the coordinates of $p'=1+2t+3t^2$. Over a field where $3=0$, such as $\mathbb F_3$, the same matrix has a zero last column, and $D(t^3)=0$.

:::

::: {#rmk-matrices-of-linear-maps-1 .remark name="Maps first, matrices second"}

A matrix depends on two choices of basis; the map does not. Statements that are true of the map, such as "$\alpha$ is injective" or "$\dim\ker\alpha=2$", are true of every matrix representing it. The next notes ask which properties of a matrix survive a change of basis: for maps $U\to V$ only the rank (@thm-rank-normal-form), for maps $V\to V$ much more (@sec-math-linear-algebra-endomorphisms-eigenvalues-of-endomorphisms).

:::
