---
title: "The Size and Complexity of Linear Programs"
sources: [mit6854-11, mit6854-12]
requires: [math/combinatorial-optimization/polyhedra/simplex-method, math/combinatorial-optimization/polyhedra/ellipsoid-method]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.854J (Fall 2008, Goemans), Lecture 11 (Sections 2-3) and Lecture 12 (Section 2), in our own wording; proofs written out in steps. -->

To call an algorithm for linear programming polynomial one must measure the input in bits. This note shows that vertices have short descriptions, that linear programming lies in $\mathrm{NP}\cap\mathrm{coNP}$, and how the ellipsoid method (@def-ellipsoid-method) becomes a polynomial algorithm for it (Khachiyan, 1979).

## Input size

Integer data are written in binary: an integer $k$ takes $\operatorname{size}(k)=1+\lceil\log(|k|+1)\rceil$ bits, a vector or matrix the sum of the sizes of its entries. For the program $\min\{c^{\mathsf T}x:Ax=b,\ x\ge0\}$ with $A\in\mathbb Z^{m\times n}$ it is convenient to use instead
$$L=m+n+\log\det_{\max}+\log b_{\max}+\log c_{\max},$$
where $\det_{\max}$ is the largest $|\det|$ of a square submatrix of $A$, $b_{\max}=\max|b_i|$ and $c_{\max}=\max|c_j|$. So $2^L=2^{m+n}\det_{\max}b_{\max}c_{\max}$.

::: {#prp-lp-size .proposition name="$L$ measures the input size"}

$L\le\operatorname{size}(A)+\operatorname{size}(b)+\operatorname{size}(c)\le mnL$ (for $m,n\ge2$). Hence an algorithm is polynomial in the bit size of the program if and only if it is polynomial in $L$.

:::

::: {.proof}

1. For a square integer matrix $M$ with columns $a_1,\dots,a_k$, Hadamard's inequality gives $|\det M|\le\prod_i\lVert a_i\rVert$, and $1+\lVert a_i\rVert\le2^{\operatorname{size}(a_i)-k}$ by counting bits. So $1+|\det M|\le\prod_i(1+\lVert a_i\rVert)\le2^{\operatorname{size}(M)}$, and $\log\det_{\max}\le\operatorname{size}(A)$.

2. Also $m+\log b_{\max}\le\operatorname{size}(b)$ and $n+\log c_{\max}\le\operatorname{size}(c)$. Adding gives the first inequality.

3. Every entry of $A$ is a $1\times1$ submatrix, so it has size at most $2+\log\det_{\max}$. Hence $\operatorname{size}(A)\le mn(2+\log\det_{\max})$, and similarly $\operatorname{size}(b)\le m(2+\log b_{\max})$, $\operatorname{size}(c)\le n(2+\log c_{\max})$. For $m,n\ge2$ the sum is at most $mnL$.

:::

::: {#thm-vertex-size .theorem name="Vertices are small"}

Every vertex $x$ of $\{x:Ax=b,\ x\ge0\}$ has coordinates $x_j=p_j/q$ with integers $0\le p_j<2^L$ and $1\le q<2^L$.

:::

::: {.proof}

1. $x$ is a basic feasible solution (@prp-vertices-are-bfs): $x_B=A_B^{-1}b$, $x_N=0$.

2. By Cramer's rule, $x_B=\operatorname{adj}(A_B)\,b/\det A_B$. Take $q=|\det A_B|\le\det_{\max}<2^L$.

3. Each entry of the adjugate is a minor of $A$, so $|p_j|\le m\det_{\max}b_{\max}<2^L$, and $p_j\ge0$ because $x\ge0$.

:::

## Linear programming is in NP ∩ coNP

The decision version asks, for integer $A,b,c$ and a rational $\lambda$, whether $\min\{c^{\mathsf T}x:Ax=b,\ x\ge0\}\le\lambda$.

::: {#thm-lp-np-conp .theorem name="LP lies in $\mathrm{NP}\cap\mathrm{coNP}$"}

Both the yes and the no instances of the decision version have certificates of size polynomial in $L$.

:::

::: {.proof}

1. *Yes.* If the minimum is finite and at most $\lambda$, an optimal vertex exists (@thm-optimal-vertex) and has polynomial size by @thm-vertex-size; checking $Ax=b$, $x\ge0$, $c^{\mathsf T}x\le\lambda$ is easy. If the program is unbounded, a vertex of the feasible set together with a vertex of $\{x:Ax=0,\ x\ge0,\ c^{\mathsf T}x=-1\}$ (a direction of decrease) is a certificate, again of polynomial size.

2. *No.* If the program is infeasible, Farkas' lemma (@lem-farkas) gives $y$ with $A^{\mathsf T}y\ge0$, $b^{\mathsf T}y<0$, and a vertex of the corresponding polyhedron is small. Otherwise the minimum exceeds $\lambda$, and by strong duality (@thm-lp-strong-duality) a vertex $y$ of $\{y:A^{\mathsf T}y\le c\}$ with $b^{\mathsf T}y>\lambda$ exists and is small.

:::

## Solving LP with the ellipsoid method

The ellipsoid method finds a point of a full-dimensional bounded convex set given a separation oracle, in a number of steps logarithmic in the ratio of an initial ball to the volume of the set. Three reductions make linear programming fit.

::: {#prp-lp-to-feasibility .proposition name="Optimisation to feasibility"}

Optimising $\min\{c^{\mathsf T}x:Ax=b,\ x\ge0\}$ reduces to at most three feasibility tests: of $Ax=b,x\ge0$ (if empty, the program is infeasible); of $A^{\mathsf T}y\le c$ (if empty, it is unbounded); and of the system $Ax=b$, $x\ge0$, $A^{\mathsf T}y\le c$, $c^{\mathsf T}x=b^{\mathsf T}y$, whose solutions are exactly the optimal primal–dual pairs.

:::

::: {.proof}

1. If the primal is feasible and the dual is not, the primal is unbounded, by strong duality (@thm-lp-strong-duality) applied to the alternatives.

2. If both are feasible, both have optima with equal values, and weak duality (@thm-lp-weak-duality) shows that any feasible pair with $c^{\mathsf T}x=b^{\mathsf T}y$ is optimal. So the last system is non-empty and its points are the optimal pairs.

:::

::: {#prp-lp-inner-outer .proposition name="Bounded and full-dimensional"}

Let $P=\{x:Ax\le b\}$ with $A$ an integer matrix of full column rank. Then $P\ne\varnothing$ if and only if
$$P'=\{x:Ax\le b+2^{-L}\mathbf 1,\ -2^L\le x_j\le2^L\ \text{for all }j\}$$
is non-empty. If so, $P'$ contains a cube of side $2^{1-2L}$, while it lies in the cube of side $2^{L+1}$.

:::

::: {.proof}

1. *If $P\ne\varnothing$.* Full column rank gives $P$ a vertex, and its coordinates are bounded by $2^L$ in absolute value (as in @thm-vertex-size). That vertex lies in $P'$.

2. Around that vertex $\hat x$, every $x$ with $|x_j-\hat x_j|\le2^{-2L}$ has $a_i^{\mathsf T}x\le b_i+n\,a_{\max}2^{-2L}\le b_i+2^{-L}$, since $n\,a_{\max}\le2^L$. So $P'$ contains a small cube.

3. *If $P=\varnothing$.* By Farkas' lemma there is $y\ge0$ with $A^{\mathsf T}y=0$, $b^{\mathsf T}y=-1$, and we may take $y$ a vertex of this system. By Cramer's rule its entries are $r_i/s$ with $0\le r_i,s\le m\,b_{\max}\det_{\max}$, so $\mathbf 1^{\mathsf T}y\le m\cdot m\,b_{\max}\det_{\max}<2^L/2$.

4. Then $(b+2^{-L}\mathbf 1)^{\mathsf T}y\le-1+\tfrac12<0$ while $A^{\mathsf T}y=0$, $y\ge0$; by Farkas' lemma $\{x:Ax\le b+2^{-L}\mathbf 1\}$ is empty, so $P'$ is empty.

:::

::: {#fig-lp-complexity-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
\fill[tintA] (0,0)--(2,0)--(0,1.5)--cycle;
\draw[emph] (0,0)--(2,0)--(0,1.5)--cycle;
\draw[hl, dashed] (-0.25,-0.25)--(2.45,-0.25)--(-0.25,1.78)--cycle;
\draw[faint] (-1,-1) rectangle (3.2,2.6);
\node[lab] at (0.6,0.45) {$P$};
\node[lab] at (1.6,1.05) {$P'$};
\node[lab, tick] at (2.6,2.35) {$[-2^L,2^L]^n$};
\end{tikzpicture}
\end{center}
```

Loosening every constraint by $2^{-L}$ turns a non-empty $P$ (here a triangle) into a full-dimensional $P'$ that contains a small cube, while the box $[-2^L,2^L]^n$ bounds the search; an empty $P$ stays empty.

:::

The ratio of the volumes of the outer and inner cubes is $2^{O(nL)}$, so the ellipsoid method decides whether $P'$ is empty in $O(n^2L)$ iterations, each polynomial in $n$ and $L$.

::: {#def-lp-rounding-to-vertex .definition name="Recovering an exact solution"}

A point of $P'$ need not lie in $P$. Instead, use the feasibility test repeatedly: go through the rows $i=1,\dots,m$ of $Ax\le b$, keeping a set $I$ of rows to be made tight; add $i$ to $I$ if the system with the rows $I\cup\{i\}$ as equalities and the remaining rows as inequalities is still feasible. At the end solve $a_i^{\mathsf T}x=b_i$ ($i\in I$) by Gaussian elimination.

:::

::: {#rmk-lp-complexity-2 .remark editor="No figure: the procedure only makes rows tight one by one through feasibility tests; a picture of a point sliding to a vertex adds nothing to the text."}

Each accepted row stays tight in some solution of the current system, so the final system still has a solution, and the tight rows determine it.

:::

The system stays feasible throughout, and the tight rows at the end determine a unique point (a vertex of $P$, by @thm-vertex-unique-solution), so $m$ more feasibility tests give an exact optimal vertex. Together:

::: {#thm-lp-polynomial .theorem name="Khachiyan"}

Linear programs with rational data can be solved in time polynomial in their bit size.

:::

::: {#rmk-lp-complexity-1 .remark name="Strongly polynomial?"}

The number of iterations of the ellipsoid method, and of interior point methods (@def-primal-dual-ipm), depends on $L$, not only on $m$ and $n$. Whether linear programming has a *strongly* polynomial algorithm, with a number of arithmetic operations bounded by a polynomial in $m$ and $n$, is open; minimum-cost circulation does (@thm-goldberg-tarjan-strong).

:::
