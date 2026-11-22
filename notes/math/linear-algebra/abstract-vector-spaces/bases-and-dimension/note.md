---
title: "Bases, the Steinitz Exchange Lemma and Dimension"
sources: [camib-la-1, mit1806-9, mit1806-11]
requires: [math/linear-algebra/abstract-vector-spaces/vector-spaces-over-a-field, math/linear-algebra/vector-spaces/independence-basis-dimension]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 1.2, in our own wording; examples ours; proofs written out in steps. MIT 18.06 proves that dimension is well defined for subspaces of R^n via elimination (thm-dimension-well-defined) and states the dimension of a sum (thm-dimension-of-sum); the exchange-lemma versions here work over any field and carry related=. Merges proposed to the owner. -->

<!-- Merged 2026-11-20 (owner): prp-basis-unique-coordinates, thm-dimension-well-defined (18.06 L9) and thm-dimension-of-sum (L11) merged into prp-basis-iff-unique-expression, thm-dimension-invariant and thm-dimension-of-sum-and-intersection; the 18.06 elimination argument for dimension is kept as a pointer paragraph there. -->

Throughout, $V$ is a vector space over a field $F$ (@def-vector-space-over-field).

::: {#def-span-independence-basis .definition name="Span, linear independence, basis" generalizes="def-linear-independence"}

Let $S\subseteq V$.

1. The *span* $\langle S\rangle$ is the set of finite linear combinations $\lambda_1s_1+\dots+\lambda_ns_n$ with $s_i\in S$, $\lambda_i\in F$ (and $\langle\varnothing\rangle=\{0\}$). $S$ *spans* $V$ if $\langle S\rangle=V$.
2. $S$ is *linearly independent* if whenever $\lambda_1s_1+\dots+\lambda_ns_n=0$ with distinct $s_i\in S$, all $\lambda_i=0$. Otherwise $S$ is *linearly dependent*.
3. $S$ is a *basis* of $V$ if it is linearly independent and spans $V$.
4. $V$ is *finite-dimensional* if it has a finite spanning set.

:::

The span $\langle S\rangle$ is the smallest subspace of $V$ containing $S$. Sums are always finite: in $F[t]$ the monomials $1,t,t^2,\dots$ form a basis, but in the space $F^{\mathbb N}$ of all sequences the unit sequences $e_1,e_2,\dots$ are independent and span only the sequences with finitely many non-zero terms.

::: {#prp-basis-iff-unique-expression .proposition name="Bases give unique coordinates"}

Vectors $e_1,\dots,e_n$ form a basis of $V$ if and only if every $v\in V$ can be written as $v=\sum_i\lambda_ie_i$ for exactly one $(\lambda_1,\dots,\lambda_n)\in F^n$.

:::

::: {.proof}

1. Spanning is the existence of such an expression.

2. If the $e_i$ are independent and $\sum\lambda_ie_i=\sum\mu_ie_i$, then $\sum(\lambda_i-\mu_i)e_i=0$, so $\lambda_i=\mu_i$ for all $i$.

3. Conversely, if expressions are unique, then $0=\sum0\,e_i$ is the only expression of $0$, which is independence.

:::

::: {#fig-bases-and-dimension-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x={(1cm,0)}, y={(0.5cm,0.6cm)}]
\draw[gridline] (-2,-2) -- (-2,2); \draw[gridline] (-2,-2) -- (2,-2);
\draw[gridline] (-1,-2) -- (-1,2); \draw[gridline] (-2,-1) -- (2,-1);
\draw[gridline] (0,-2) -- (0,2); \draw[gridline] (-2,0) -- (2,0);
\draw[gridline] (1,-2) -- (1,2); \draw[gridline] (-2,1) -- (2,1);
\draw[gridline] (2,-2) -- (2,2); \draw[gridline] (-2,2) -- (2,2);
\draw[->, emph, primary] (0,0) -- (1,0) node[below, lab] {$b_1$};
\draw[->, emph, secondary] (0,0) -- (0,1) node[left, lab] {$b_2$};
\draw[faint, dashed] (2,0) -- (2,1);
\draw[->, emph, accent] (0,0) -- (2,1) node[right, lab] {$v=2b_1+b_2$};
\fill[ink] (0,0) circle[pt];
\end{scope}
\end{tikzpicture}
\end{center}
```

A basis turns $V$ into a coordinate grid: every vector is reached by exactly one combination of the basis vectors, here $v=2b_1+b_2$, so $v$ has the coordinates $(2,1)$. The grid need not be square; no inner product is involved.

:::

::: {#lem-dependence-one-in-span-of-others .lemma name="A dependent set has a redundant vector"}

$S$ is linearly dependent if and only if some $s_0\in S$ lies in $\langle S\setminus\{s_0\}\rangle$. In that case $\langle S\setminus\{s_0\}\rangle=\langle S\rangle$.

:::

::: {.proof}

1. If $\lambda_0s_0+\lambda_1s_1+\dots+\lambda_ns_n=0$ with distinct $s_i$ and $\lambda_0\ne0$, then $s_0=-\lambda_0^{-1}(\lambda_1s_1+\dots+\lambda_ns_n)$.

2. If $s_0=\mu_1s_1+\dots+\mu_ns_n$ with $s_i\ne s_0$, then $1\cdot s_0-\mu_1s_1-\dots-\mu_ns_n=0$ is a dependence with a non-zero coefficient.

3. Any combination involving $s_0$ becomes a combination of the others after substituting this expression for $s_0$, so removing $s_0$ does not change the span.

:::

So every finite spanning set contains a basis: remove redundant vectors one at a time until none is left. In particular every finite-dimensional space has a finite basis.

::: {#thm-steinitz-exchange .theorem name="Steinitz exchange lemma"}

Let $u_1,\dots,u_m\in V$ be linearly independent and let $w_1,\dots,w_n$ span $V$. Then $m\le n$, and after renumbering the $w_j$, the vectors
$$u_1,\dots,u_m,\ w_{m+1},\dots,w_n$$
span $V$.

:::

::: {.proof}

Induction on $k$: we show that for $0\le k\le m$, after renumbering, $k\le n$ and $u_1,\dots,u_k,w_{k+1},\dots,w_n$ span $V$. The case $k=0$ is the hypothesis.

1. Suppose the claim holds for $k<m$. Since these vectors span, $u_{k+1}=\sum_{i\le k}\alpha_iu_i+\sum_{j>k}\beta_jw_j$.

2. Some $\beta_j$ is non-zero: otherwise $u_{k+1}$ is a combination of $u_1,\dots,u_k$, contradicting independence. In particular there is some $j>k$, so $k+1\le n$. Renumber so that $\beta_{k+1}\ne0$.

3. Then $w_{k+1}=\beta_{k+1}^{-1}\big(u_{k+1}-\sum_{i\le k}\alpha_iu_i-\sum_{j>k+1}\beta_jw_j\big)$ lies in the span of $u_1,\dots,u_{k+1},w_{k+2},\dots,w_n$.

4. So this new list spans every vector of the old list, hence spans $V$. This is the claim for $k+1$; at $k=m$ we get the theorem.

:::

::: {#fig-bases-and-dimension-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (1.50,0.00) rectangle (2.25,0.45);
\draw[cell, fill=primaryLight] (2.25,0.00) rectangle (3.00,0.45);
\draw[cell, fill=primaryLight] (3.00,0.00) rectangle (3.75,0.45);
\node[lab, tick] at (2.62,-0.22) {$w_1,w_2,w_3$};
\draw[cell, fill=primaryLight] (3.75,0.00) rectangle (4.50,0.45);
\draw[cell, fill=primaryLight] (4.50,0.00) rectangle (5.25,0.45);
\node[lab, tick] at (4.50,-0.22) {$w_4,w_5$};
\node[lab, anchor=east] at (1.40,0.23) {start};
\draw[cell, fill=accentLight] (1.50,-0.95) rectangle (2.25,-0.50);
\node[lab, tick] at (1.88,-1.17) {$u_1$};
\draw[cell, fill=primaryLight] (2.25,-0.95) rectangle (3.00,-0.50);
\draw[cell, fill=primaryLight] (3.00,-0.95) rectangle (3.75,-0.50);
\node[lab, tick] at (3.00,-1.17) {$w_2,w_3$};
\draw[cell, fill=primaryLight] (3.75,-0.95) rectangle (4.50,-0.50);
\draw[cell, fill=primaryLight] (4.50,-0.95) rectangle (5.25,-0.50);
\node[lab, anchor=east] at (1.40,-0.72) {step 1};
\draw[cell, fill=accentLight] (1.50,-1.90) rectangle (2.25,-1.45);
\draw[cell, fill=accentLight] (2.25,-1.90) rectangle (3.00,-1.45);
\node[lab, tick] at (2.25,-2.12) {$u_1,u_2$};
\draw[cell, fill=primaryLight] (3.00,-1.90) rectangle (3.75,-1.45);
\node[lab, tick] at (3.38,-2.12) {$w_3$};
\draw[cell, fill=primaryLight] (3.75,-1.90) rectangle (4.50,-1.45);
\draw[cell, fill=primaryLight] (4.50,-1.90) rectangle (5.25,-1.45);
\node[lab, anchor=east] at (1.40,-1.67) {step 2};
\draw[cell, fill=accentLight] (1.50,-2.85) rectangle (2.25,-2.40);
\draw[cell, fill=accentLight] (2.25,-2.85) rectangle (3.00,-2.40);
\draw[cell, fill=accentLight] (3.00,-2.85) rectangle (3.75,-2.40);
\node[lab, tick] at (2.62,-3.07) {$u_1,u_2,u_3$};
\draw[cell, fill=primaryLight] (3.75,-2.85) rectangle (4.50,-2.40);
\draw[cell, fill=primaryLight] (4.50,-2.85) rectangle (5.25,-2.40);
\node[lab, tick] at (4.50,-3.07) {$w_4,w_5$};
\node[lab, anchor=east] at (1.40,-2.62) {end};
\node[lab, note, anchor=west, align=left] at (5.6,-1.2) {each step swaps one $w_j$\\for the next $u_i$ and the list\\still spans $V$; the $u$'s never\\run out of $w$'s, so $m\le n$};
\end{tikzpicture}
\end{center}
```

The exchange lemma with $m=3$ independent vectors $u_i$ and a spanning list of $n=5$ vectors $w_j$. Each $u_i$ replaces one of the remaining $w_j$ (after renumbering), and the list keeps spanning $V$ at every stage.

:::

::: {#thm-dimension-invariant .theorem name="Dimension is well defined"}

If $V$ is finite-dimensional, all bases of $V$ are finite and have the same number of elements, the *dimension* $\dim V=\dim_FV$.

:::

::: {.proof}

1. $V$ has a finite spanning set of some size $n$. Any finite independent subset has at most $n$ elements by @thm-steinitz-exchange, so an infinite independent set (whose finite subsets are all independent) cannot exist. Hence every basis is finite.

2. If $e_1,\dots,e_m$ and $f_1,\dots,f_n$ are bases, the $e$'s are independent and the $f$'s span, so $m\le n$; exchanging roles, $n\le m$.

:::

The field matters: $\dim_{\mathbb C}\mathbb C=1$ (basis $1$) but $\dim_{\mathbb R}\mathbb C=2$ (basis $1,i$).

::: {#cor-independent-set-extends-to-basis .corollary name="Consequences of the exchange lemma"}

Let $\dim V=n$.

1. Any $n$ linearly independent vectors form a basis, and any $n$ spanning vectors form a basis.
2. Every linearly independent set extends to a basis of $V$.
3. If $U\le V$, then $U$ is finite-dimensional, $\dim U\le n$, and $\dim U=n$ only if $U=V$.

:::

::: {.proof}

1. If $u_1,\dots,u_n$ are independent, apply @thm-steinitz-exchange with a basis as spanning set: the $u$'s replace all $n$ vectors, so they span. If $w_1,\dots,w_n$ span, they contain a basis by @lem-dependence-one-in-span-of-others, which has $n$ elements by @thm-dimension-invariant, so it is the whole list.

2. Let $u_1,\dots,u_m$ be independent ($m\le n$) and $e_1,\dots,e_n$ a basis. By @thm-steinitz-exchange, $u_1,\dots,u_m,e_{m+1},\dots,e_n$ span $V$ after renumbering; these are $n$ spanning vectors, hence a basis by item 1.

3. An independent subset of $U$ is independent in $V$, so has at most $n$ elements. Take an independent subset of $U$ of maximal size $m\le n$. Adding any $u\in U$ makes it dependent, so by @lem-dependence-one-in-span-of-others (applied to the dependence, whose coefficient of $u$ must be non-zero) $u$ is in its span: it is a basis of $U$ and $\dim U=m$. If $m=n$, it is a basis of $V$ by item 1, so $U=V$.

:::

::: {#thm-dimension-of-sum-and-intersection .theorem name="Dimension of a sum"}

If $U,W$ are subspaces of a finite-dimensional space $V$, then
$$\dim(U+W)+\dim(U\cap W)=\dim U+\dim W.$$

:::

::: {.proof}

1. Take a basis $v_1,\dots,v_r$ of $U\cap W$ and extend it (@cor-independent-set-extends-to-basis) to a basis $v_1,\dots,v_r,u_1,\dots,u_s$ of $U$ and to a basis $v_1,\dots,v_r,w_1,\dots,w_t$ of $W$.

2. The combined list $v_1,\dots,v_r,u_1,\dots,u_s,w_1,\dots,w_t$ spans $U+W$, since every $u+w$ is a combination of it.

3. It is independent: suppose $\sum\alpha_iv_i+\sum\beta_ju_j+\sum\gamma_kw_k=0$. Then $x=\sum\gamma_kw_k=-\sum\alpha_iv_i-\sum\beta_ju_j$ lies in $W$ and in $U$, so in $U\cap W$, and $x=\sum\delta_iv_i$ for some $\delta_i$. Independence of the basis of $W$ in $\sum\gamma_kw_k-\sum\delta_iv_i=0$ gives all $\gamma_k=0$; then independence of the basis of $U$ gives all $\alpha_i,\beta_j=0$.

4. Hence $\dim(U+W)=r+s+t=(r+s)+(r+t)-r$.

:::

::: {#fig-bases-and-dimension-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.00,0.00) rectangle (0.75,0.45);
\draw[cell, fill=primaryLight] (0.75,0.00) rectangle (1.50,0.45);
\node[lab, tick] at (0.75,-0.22) {$U$ only};
\draw[cell, fill=secondarySoft] (1.50,0.00) rectangle (2.25,0.45);
\node[lab, tick] at (1.88,-0.22) {$U\cap W$};
\draw[cell, fill=accentLight] (2.25,0.00) rectangle (3.00,0.45);
\draw[cell, fill=accentLight] (3.00,0.00) rectangle (3.75,0.45);
\draw[cell, fill=accentLight] (3.75,0.00) rectangle (4.50,0.45);
\node[lab, tick] at (3.38,-0.22) {$W$ only};
\draw[decorate, decoration={brace, amplitude=4pt}] (0,0.55) -- (2.25,0.55) node[midway, above=4pt, lab, note, primary] {$\dim U=3$};
\draw[decorate, decoration={brace, amplitude=4pt, mirror}] (1.5,-0.45) -- (4.5,-0.45) node[midway, below=4pt, lab, note, accent] {$\dim W=4$};
\node[lab, note, anchor=west, align=left] at (4.9,0.2) {a basis of $U\cap W$ (middle cell) extends\\to bases of $U$ and of $W$; together\\they give a basis of $U+W$:\\$\dim(U+W)=3+4-1=6$};
\end{tikzpicture}
\end{center}
```

Why $\dim(U+W)=\dim U+\dim W-\dim(U\cap W)$: in the sum $\dim U+\dim W$ the basis vectors of the intersection are counted twice.

:::

::: {#prp-dimension-of-quotient .proposition name="Dimension of a quotient"}

If $U\le V$ and $V$ is finite-dimensional, then $\dim V/U=\dim V-\dim U$. More precisely, if $u_1,\dots,u_m$ is a basis of $U$ extended to a basis $u_1,\dots,u_m,v_{m+1},\dots,v_n$ of $V$, then the cosets $v_{m+1}+U,\dots,v_n+U$ form a basis of $V/U$ (@def-quotient-space).

:::

::: {.proof}

1. Spanning: if $v=\sum\alpha_iu_i+\sum\beta_jv_j$, then $v+U=\sum\beta_j(v_j+U)$ because $\sum\alpha_iu_i\in U$.

2. Independence: if $\sum\beta_j(v_j+U)=0+U$, then $\sum\beta_jv_j\in U$, so $\sum\beta_jv_j=\sum\alpha_iu_i$ for some $\alpha_i$. Independence of the basis of $V$ gives all $\beta_j=0$.

:::

::: {#fig-bases-and-dimension-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.00,0.00) rectangle (0.75,0.45);
\draw[cell, fill=primaryLight] (0.75,0.00) rectangle (1.50,0.45);
\node[lab, tick] at (0.75,-0.22) {basis of $U$};
\draw[cell, fill=accentLight] (1.50,0.00) rectangle (2.25,0.45);
\draw[cell, fill=accentLight] (2.25,0.00) rectangle (3.00,0.45);
\draw[cell, fill=accentLight] (3.00,0.00) rectangle (3.75,0.45);
\node[lab, tick] at (2.62,-0.22) {extension $v_1,v_2,v_3$};
\node[lab, anchor=east] at (-0.10,0.23) {$V$:};
\draw[->] (2.6,-0.35) -- (2.6,-1.05);
\draw[cell, fill=accentLight] (1.50,-1.60) rectangle (2.25,-1.15);
\draw[cell, fill=accentLight] (2.25,-1.60) rectangle (3.00,-1.15);
\draw[cell, fill=accentLight] (3.00,-1.60) rectangle (3.75,-1.15);
\node[lab, tick] at (2.62,-1.82) {$v_1+U,\ v_2+U,\ v_3+U$};
\node[lab, anchor=east] at (1.40,-1.38) {$V/U$:};
\node[lab, note, anchor=west] at (4.1,-1.35) {$\dim V/U=\dim V-\dim U=5-2$};
\end{tikzpicture}
\end{center}
```

A basis of $U$ extended to a basis of $V$. The basis vectors of $U$ become $0$ in $V/U$, and the cosets of the added vectors form a basis of the quotient.

:::

::: {#exm-dimension-of-sum .example name="Two planes in four dimensions"}

In $\mathbb R^4$ let $U=\langle e_1,e_2\rangle$ and $W=\langle e_2+e_3,\ e_4\rangle$. Then $U+W=\langle e_1,e_2,e_3,e_4\rangle=\mathbb R^4$ has dimension $4=2+2-\dim(U\cap W)$, so $U\cap W=\{0\}$. Replacing $W$ by $W'=\langle e_2,e_3\rangle$ gives $U+W'=\langle e_1,e_2,e_3\rangle$ of dimension $3$, so $\dim(U\cap W')=1$; indeed $U\cap W'=\langle e_2\rangle$.

:::

::: {#fig-bases-and-dimension-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) ellipse (1.6 and 1.0); \draw (0,0) ellipse (1.6 and 1.0);
\fill[tintB] (1.6,0) ellipse (1.6 and 1.0); \draw (1.6,0) ellipse (1.6 and 1.0);
\node[lab] at (-1.0,1.2) {$U$}; \node[lab] at (2.6,1.2) {$W'$};
\node[lab] at (-0.7,0) {$e_1$}; \node[lab] at (0.8,0) {$e_2$}; \node[lab] at (2.3,0) {$e_3$};
\node[lab, below] at (0.8,-1.05) {$U\cap W'=\langle e_2\rangle$};
\end{tikzpicture}
\end{center}
```

$U=\langle e_1,e_2\rangle$ and $W'=\langle e_2,e_3\rangle$ share the basis vector $e_2$. A basis of $U+W'$ counts $e_2$ once: $\dim(U+W')=2+2-1=3$.

:::
