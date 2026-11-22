---
title: "Gram–Schmidt and Orthogonal Complements"
sources: [camib-la-8, mit1806-17]
requires: [math/linear-algebra/inner-product-spaces/inner-products]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 8.2, in our own wording; examples ours (checked with sympy); proofs written out in steps. MIT 18.06 runs Gram-Schmidt on vectors of R^m (def-gram-schmidt) and proves that row space and nullspace are orthogonal complements (thm-fundamental-theorem-orthogonality); the abstract versions here carry generalizes= or related=. Merge of the Gram-Schmidt blocks proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): def-gram-schmidt and thm-gram-schmidt (18.06 L17, the process for vectors of R^m and its correctness) merged into thm-gram-schmidt-abstract (same formula and induction). -->

::: {#thm-gram-schmidt-abstract .theorem name="Gram–Schmidt process"}

Let $v_1,v_2,\dots$ be a finite or infinite sequence of linearly independent vectors in an inner product space $V$. Define recursively
$$w_k=v_k-\sum_{i<k}\langle v_k,e_i\rangle e_i,\qquad e_k=\frac{w_k}{\lVert w_k\rVert}.$$
Then $e_1,e_2,\dots$ is orthonormal and $\langle e_1,\dots,e_k\rangle=\langle v_1,\dots,v_k\rangle$ for every $k$.

:::

::: {.proof}

Induction on $k$; assume $e_1,\dots,e_{k-1}$ are orthonormal with $\langle e_1,\dots,e_{k-1}\rangle=\langle v_1,\dots,v_{k-1}\rangle$.

1. $w_k\ne0$: otherwise $v_k\in\langle e_1,\dots,e_{k-1}\rangle=\langle v_1,\dots,v_{k-1}\rangle$, contradicting independence. So $e_k$ is defined and has norm $1$.

2. For $j<k$: $\langle w_k,e_j\rangle=\langle v_k,e_j\rangle-\sum_{i<k}\langle v_k,e_i\rangle\langle e_i,e_j\rangle=\langle v_k,e_j\rangle-\langle v_k,e_j\rangle=0$. So $e_k$ is orthogonal to the earlier $e_j$.

3. $e_k\in\langle v_1,\dots,v_k\rangle$ and $v_k=\lVert w_k\rVert e_k+\sum_{i<k}\langle v_k,e_i\rangle e_i\in\langle e_1,\dots,e_k\rangle$, so the spans agree.

:::

::: {#fig-gram-schmidt-and-orthogonal-complements-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (v) at (0,0) {$v_k$};
\node[box] (w) at (4.4,0) {$w_k=v_k-\sum_{i<k}\langle v_k,e_i\rangle e_i$};
\node[hl box] (e) at (9.4,0) {$e_k=w_k/\lVert w_k\rVert$};
\draw[->, emph] (v) -- node[above, lab, tick] {remove} (w);
\draw[->, emph] (w) -- node[above, lab, tick] {normalise} (e);
\draw[->, emph, accent] (e) to[bend left=25] node[below, lab, note] {use $e_1,\dots,e_k$ for the next vector} (v);
\end{tikzpicture}
\end{center}
```

One round of Gram–Schmidt in any inner product space: remove from $v_k$ its components along the earlier $e_i$, then scale to length $1$. $w_k\neq0$ because $v_k$ is not in the span of the earlier vectors.

:::

```{=latex}
\begin{algorithm}
\caption{Gram--Schmidt in an inner product space}
\begin{algorithmic}
\INPUT Linearly independent $v_1,\dots,v_k$ in an inner product space
\OUTPUT Orthonormal $e_1,\dots,e_k$ with $\langle e_1,\dots,e_j\rangle=\langle v_1,\dots,v_j\rangle$ for all $j$
\FOR{$j=1,\dots,k$}
    \STATE $w_j\gets v_j-\sum_{i<j}\langle v_j,e_i\rangle e_i$
    \STATE $e_j\gets w_j/\lVert w_j\rVert$
\ENDFOR
\RETURN $e_1,\dots,e_k$
\end{algorithmic}
\end{algorithm}
```

::: {#cor-orthonormal-basis-exists .corollary name="Orthonormal bases exist"}

Every finite-dimensional inner product space has an orthonormal basis, and every orthonormal set extends to one.

:::

::: {.proof}

1. Extend the orthonormal set $e_1,\dots,e_k$ to a basis $e_1,\dots,e_k,v_{k+1},\dots,v_n$ (@cor-independent-set-extends-to-basis).

2. Apply @thm-gram-schmidt-abstract. The first $k$ vectors are unchanged ($w_j=e_j$ since $\langle e_j,e_i\rangle=0$ for $i<j$), and the result is an orthonormal set of $n=\dim V$ vectors, hence a basis (@prp-parseval, @cor-independent-set-extends-to-basis).

:::

::: {#exm-gram-schmidt-polynomials .example name="Legendre polynomials"}

On $\mathbb R[t]_{\le2}$ with $\langle f,g\rangle=\int_{-1}^1f(t)g(t)\,dt$, apply Gram–Schmidt to $1,t,t^2$. $\lVert1\rVert^2=2$ gives $e_1=\frac1{\sqrt2}$. $\langle t,e_1\rangle=0$ and $\lVert t\rVert^2=\frac23$ give $e_2=\sqrt{\tfrac32}\,t$. Then $w_3=t^2-\langle t^2,e_1\rangle e_1-\langle t^2,e_2\rangle e_2=t^2-\frac13$, with $\lVert w_3\rVert^2=\frac8{45}$, so $e_3=\frac{\sqrt{10}}4(3t^2-1)$. Up to scaling these are the Legendre polynomials $1,\ t,\ \frac12(3t^2-1)$.

:::

::: {#fig-gram-schmidt-and-orthogonal-complements-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-2.2,0) -- (2.4,0) node[lab, anchor=west] {$t$};
\draw[->] (0,-1.6) -- (0,2.4);
\node[lab, tick, anchor=north] at (-2,0) {$-1$}; \node[lab, tick, anchor=north] at (2,0) {$1$};
\draw[emph, primary] (-2.000,0.849) -- (-1.950,0.849) -- (-1.900,0.849) -- (-1.850,0.849) -- (-1.800,0.849) -- (-1.750,0.849) -- (-1.700,0.849) -- (-1.650,0.849) -- (-1.600,0.849) -- (-1.550,0.849) -- (-1.500,0.849) -- (-1.450,0.849) -- (-1.400,0.849) -- (-1.350,0.849) -- (-1.300,0.849) -- (-1.250,0.849) -- (-1.200,0.849) -- (-1.150,0.849) -- (-1.100,0.849) -- (-1.050,0.849) -- (-1.000,0.849) -- (-0.950,0.849) -- (-0.900,0.849) -- (-0.850,0.849) -- (-0.800,0.849) -- (-0.750,0.849) -- (-0.700,0.849) -- (-0.650,0.849) -- (-0.600,0.849) -- (-0.550,0.849) -- (-0.500,0.849) -- (-0.450,0.849) -- (-0.400,0.849) -- (-0.350,0.849) -- (-0.300,0.849) -- (-0.250,0.849) -- (-0.200,0.849) -- (-0.150,0.849) -- (-0.100,0.849) -- (-0.050,0.849) -- (0.000,0.849) -- (0.050,0.849) -- (0.100,0.849) -- (0.150,0.849) -- (0.200,0.849) -- (0.250,0.849) -- (0.300,0.849) -- (0.350,0.849) -- (0.400,0.849) -- (0.450,0.849) -- (0.500,0.849) -- (0.550,0.849) -- (0.600,0.849) -- (0.650,0.849) -- (0.700,0.849) -- (0.750,0.849) -- (0.800,0.849) -- (0.850,0.849) -- (0.900,0.849) -- (0.950,0.849) -- (1.000,0.849) -- (1.050,0.849) -- (1.100,0.849) -- (1.150,0.849) -- (1.200,0.849) -- (1.250,0.849) -- (1.300,0.849) -- (1.350,0.849) -- (1.400,0.849) -- (1.450,0.849) -- (1.500,0.849) -- (1.550,0.849) -- (1.600,0.849) -- (1.650,0.849) -- (1.700,0.849) -- (1.750,0.849) -- (1.800,0.849) -- (1.850,0.849) -- (1.900,0.849) -- (1.950,0.849) -- (2.000,0.849);
\draw[emph, accent] (-2.000,-1.470) -- (-1.950,-1.433) -- (-1.900,-1.396) -- (-1.850,-1.359) -- (-1.800,-1.323) -- (-1.750,-1.286) -- (-1.700,-1.249) -- (-1.650,-1.212) -- (-1.600,-1.176) -- (-1.550,-1.139) -- (-1.500,-1.102) -- (-1.450,-1.066) -- (-1.400,-1.029) -- (-1.350,-0.992) -- (-1.300,-0.955) -- (-1.250,-0.919) -- (-1.200,-0.882) -- (-1.150,-0.845) -- (-1.100,-0.808) -- (-1.050,-0.772) -- (-1.000,-0.735) -- (-0.950,-0.698) -- (-0.900,-0.661) -- (-0.850,-0.625) -- (-0.800,-0.588) -- (-0.750,-0.551) -- (-0.700,-0.514) -- (-0.650,-0.478) -- (-0.600,-0.441) -- (-0.550,-0.404) -- (-0.500,-0.367) -- (-0.450,-0.331) -- (-0.400,-0.294) -- (-0.350,-0.257) -- (-0.300,-0.220) -- (-0.250,-0.184) -- (-0.200,-0.147) -- (-0.150,-0.110) -- (-0.100,-0.073) -- (-0.050,-0.037) -- (0.000,0.000) -- (0.050,0.037) -- (0.100,0.073) -- (0.150,0.110) -- (0.200,0.147) -- (0.250,0.184) -- (0.300,0.220) -- (0.350,0.257) -- (0.400,0.294) -- (0.450,0.331) -- (0.500,0.367) -- (0.550,0.404) -- (0.600,0.441) -- (0.650,0.478) -- (0.700,0.514) -- (0.750,0.551) -- (0.800,0.588) -- (0.850,0.625) -- (0.900,0.661) -- (0.950,0.698) -- (1.000,0.735) -- (1.050,0.772) -- (1.100,0.808) -- (1.150,0.845) -- (1.200,0.882) -- (1.250,0.919) -- (1.300,0.955) -- (1.350,0.992) -- (1.400,1.029) -- (1.450,1.066) -- (1.500,1.102) -- (1.550,1.139) -- (1.600,1.176) -- (1.650,1.212) -- (1.700,1.249) -- (1.750,1.286) -- (1.800,1.323) -- (1.850,1.359) -- (1.900,1.396) -- (1.950,1.433) -- (2.000,1.470);
\draw[emph, secondary] (-2.000,1.897) -- (-1.950,1.757) -- (-1.900,1.620) -- (-1.850,1.486) -- (-1.800,1.357) -- (-1.750,1.230) -- (-1.700,1.108) -- (-1.650,0.988) -- (-1.600,0.873) -- (-1.550,0.761) -- (-1.500,0.652) -- (-1.450,0.547) -- (-1.400,0.446) -- (-1.350,0.348) -- (-1.300,0.254) -- (-1.250,0.163) -- (-1.200,0.076) -- (-1.150,-0.008) -- (-1.100,-0.088) -- (-1.050,-0.164) -- (-1.000,-0.237) -- (-0.950,-0.307) -- (-0.900,-0.372) -- (-0.850,-0.435) -- (-0.800,-0.493) -- (-0.750,-0.548) -- (-0.700,-0.600) -- (-0.650,-0.648) -- (-0.600,-0.693) -- (-0.550,-0.733) -- (-0.500,-0.771) -- (-0.450,-0.805) -- (-0.400,-0.835) -- (-0.350,-0.862) -- (-0.300,-0.885) -- (-0.250,-0.904) -- (-0.200,-0.920) -- (-0.150,-0.933) -- (-0.100,-0.942) -- (-0.050,-0.947) -- (0.000,-0.949) -- (0.050,-0.947) -- (0.100,-0.942) -- (0.150,-0.933) -- (0.200,-0.920) -- (0.250,-0.904) -- (0.300,-0.885) -- (0.350,-0.862) -- (0.400,-0.835) -- (0.450,-0.805) -- (0.500,-0.771) -- (0.550,-0.733) -- (0.600,-0.693) -- (0.650,-0.648) -- (0.700,-0.600) -- (0.750,-0.548) -- (0.800,-0.493) -- (0.850,-0.435) -- (0.900,-0.372) -- (0.950,-0.307) -- (1.000,-0.237) -- (1.050,-0.164) -- (1.100,-0.088) -- (1.150,-0.008) -- (1.200,0.076) -- (1.250,0.163) -- (1.300,0.254) -- (1.350,0.348) -- (1.400,0.446) -- (1.450,0.547) -- (1.500,0.652) -- (1.550,0.761) -- (1.600,0.873) -- (1.650,0.988) -- (1.700,1.108) -- (1.750,1.230) -- (1.800,1.357) -- (1.850,1.486) -- (1.900,1.620) -- (1.950,1.757) -- (2.000,1.897);
\node[lab, anchor=west] at (2.05,0.85) {$e_1$};
\node[lab, anchor=west] at (2.05,1.47) {$e_2$};
\node[lab, anchor=west] at (2.05,1.95) {$e_3$};
\end{tikzpicture}
\end{center}
```

The orthonormal polynomials $e_1,e_2,e_3$ produced by Gram–Schmidt from $1,t,t^2$ on $[-1,1]$. Each $e_k$ has $k-1$ roots in $(-1,1)$, and the integral of any product $e_ie_j$ with $i
e j$ over $[-1,1]$ is $0$.

:::

::: {#def-orthogonal-complement .definition name="Orthogonal complement" generalizes="def-orthogonal-subspaces"}

For a subspace $W$ of an inner product space $V$, the *orthogonal complement* is
$$W^\perp=\{v\in V:\langle v,w\rangle=0\text{ for all }w\in W\}.$$
$V$ is the *orthogonal direct sum* of $W_1,\dots,W_k$ if $V=W_1\oplus\dots\oplus W_k$ and $W_i\perp W_j$ for $i\ne j$.

:::

::: {#thm-orthogonal-complement .theorem name="Orthogonal decomposition" related="thm-fundamental-theorem-orthogonality"}

Let $V$ be a finite-dimensional inner product space and $W\le V$. Then

1. $V=W\oplus W^\perp$, an orthogonal direct sum, and $\dim W^\perp=\dim V-\dim W$;
2. $(W^\perp)^\perp=W$;
3. if $e_1,\dots,e_k$ is an orthonormal basis of $W$, the *orthogonal projection* $\pi(v)=\sum_{i=1}^k\langle v,e_i\rangle e_i$ is the projection onto $W$ along $W^\perp$.

:::

::: {.proof}

1. $W^\perp$ is a subspace, being an intersection of kernels of the linear maps $v\mapsto\langle v,w\rangle$.

2. $W\cap W^\perp=\{0\}$: if $w\in W\cap W^\perp$ then $\langle w,w\rangle=0$, so $w=0$.

3. For any $v$, $\pi(v)\in W$ and $v-\pi(v)\in W^\perp$: indeed $\langle v-\pi(v),e_j\rangle=\langle v,e_j\rangle-\langle v,e_j\rangle=0$ for each $j$, and the $e_j$ span $W$. So $v=\pi(v)+(v-\pi(v))$ and $V=W+W^\perp$; with step 2 the sum is direct (@prp-direct-sum-criteria), and the dimension formula follows. This also proves item 3.

4. $W\le(W^\perp)^\perp$ by definition, and by item 1 twice both have dimension $\dim W$, so they are equal.

:::

::: {#fig-gram-schmidt-and-orthogonal-complements-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.00,0.00) rectangle (0.75,0.45);
\draw[cell, fill=primaryLight] (0.75,0.00) rectangle (1.50,0.45);
\node[lab, tick] at (0.75,-0.22) {$U$};
\draw[cell, fill=accentLight] (1.50,0.00) rectangle (2.25,0.45);
\draw[cell, fill=accentLight] (2.25,0.00) rectangle (3.00,0.45);
\draw[cell, fill=accentLight] (3.00,0.00) rectangle (3.75,0.45);
\node[lab, tick] at (2.62,-0.22) {$U^\perp$};
\node[lab, note, anchor=west, align=left] at (4.0,0.2) {$V=U\oplus U^\perp$: an orthonormal basis of $U$\\extends to one of $V$; the added vectors\\are an orthonormal basis of $U^\perp$};
\end{tikzpicture}
\end{center}
```

The orthogonal decomposition, one cell per orthonormal basis vector. Extending by Gram–Schmidt keeps the new vectors perpendicular to $U$, so $\dim U+\dim U^\perp=\dim V$.

:::

::: {#prp-best-approximation .proposition name="The projection is the best approximation" generalizes="thm-projection-onto-subspace"}

With $\pi$ as in @thm-orthogonal-complement, $\lVert v-\pi(v)\rVert\le\lVert v-w\rVert$ for every $w\in W$, with equality only for $w=\pi(v)$.

:::

::: {.proof}

1. $v-w=(v-\pi(v))+(\pi(v)-w)$, where $v-\pi(v)\in W^\perp$ and $\pi(v)-w\in W$.

2. For orthogonal vectors $\lVert a+b\rVert^2=\lVert a\rVert^2+2\operatorname{Re}\langle a,b\rangle+\lVert b\rVert^2=\lVert a\rVert^2+\lVert b\rVert^2$. So $\lVert v-w\rVert^2=\lVert v-\pi(v)\rVert^2+\lVert\pi(v)-w\rVert^2$, and the second term is $0$ only if $w=\pi(v)$.

:::

::: {#fig-gram-schmidt-and-orthogonal-complements-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (-1.6,-0.7) -- (2.6,-0.7) -- (3.6,0.9) -- (-0.6,0.9) -- cycle;
\node[lab, note, primary] at (3.0,-0.45) {$U$};
\fill[ink] (1.4,1.9) circle[pt] node[above, lab] {$v$}; \fill[primary] (1.4,0.2) circle[pt] node[below, lab, tick] {$\pi(v)$};
\draw[emph, accent] (1.4,1.9) -- (1.4,0.2);
\fill[muted] (-0.3,0.4) circle[pt] node[below, lab, tick] {$u$}; \draw[faint, dashed] (1.4,1.9) -- (-0.3,0.4);
\draw[faint, dashed] (-0.3,0.4) -- (1.4,0.2);
\draw[muted] (1.4,0.4) -- (1.25,0.42) -- (1.25,0.22);
\node[lab, note, anchor=west, align=left] at (4.0,1.0) {$\lVert v-u\rVert^2=\lVert v-\pi v\rVert^2+\lVert\pi v-u\rVert^2$\\$\ge\lVert v-\pi v\rVert^2$, by Pythagoras};
\end{tikzpicture}
\end{center}
```

Why the orthogonal projection is the best approximation from $U$. For any other $u\in U$ the error $v-u$ is the hypotenuse of a right triangle whose legs are $v-\pi(v)$ (perpendicular to $U$) and $\pi(v)-u$ (inside $U$).

:::

In @exm-gram-schmidt-polynomials, the quadratic closest to $t^4$ in this inner product is $\sum_{i\le3}\langle t^4,e_i\rangle e_i=\frac67t^2-\frac3{35}$. Least squares (@thm-least-squares-normal-equations) is the case $V=\mathbb R^m$ with the dot product and $W$ the column space.
