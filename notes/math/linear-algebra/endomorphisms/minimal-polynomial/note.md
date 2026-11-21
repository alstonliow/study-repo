---
title: "The Minimal Polynomial"
sources: [camib-la-6]
requires: [math/linear-algebra/endomorphisms/eigenvalues-of-endomorphisms, math/discrete/polynomials/polynomials-and-roots]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.2, in our own wording; examples ours (checked with sympy); proofs written out in steps. The course's aside on polynomials (division, factor theorem, at most deg f roots) is already in math/discrete/polynomials/polynomials-and-roots and is not repeated; it holds over any field. -->

For $p(t)=\sum_ia_it^i\in F[t]$ and $\alpha\in\operatorname{End}(V)$, put $p(\alpha)=\sum_ia_i\alpha^i$, with $\alpha^0=\iota$. Then $(pq)(\alpha)=p(\alpha)q(\alpha)$, and all polynomials in $\alpha$ commute with each other.

::: {#def-minimal-polynomial .definition name="Minimal polynomial"}

The *minimal polynomial* $m_\alpha$ of $\alpha\in\operatorname{End}(V)$ is the monic polynomial of least degree with $m_\alpha(\alpha)=0$. For a matrix $A$, $m_A$ is defined in the same way.

:::

A non-zero polynomial killing $\alpha$ exists: $\operatorname{End}(V)$ has dimension $n^2$ (@thm-matrix-of-linear-map), so $\iota,\alpha,\dots,\alpha^{n^2}$ are linearly dependent. (Cayley–Hamilton, @thm-cayley-hamilton, gives one of degree $n$.)

::: {#lem-minimal-polynomial-divides .lemma name="The minimal polynomial divides every annihilating polynomial"}

For $p\in F[t]$, $p(\alpha)=0$ if and only if $m_\alpha$ divides $p$. In particular $m_\alpha$ is unique.

:::

::: {.proof}

1. Divide (@thm-polynomial-division): $p=q\,m_\alpha+r$ with $\deg r<\deg m_\alpha$ or $r=0$.

2. Then $r(\alpha)=p(\alpha)-q(\alpha)m_\alpha(\alpha)=p(\alpha)$.

3. If $p(\alpha)=0$, then $r(\alpha)=0$; by minimality of $\deg m_\alpha$, $r$ cannot be a non-zero polynomial, so $r=0$. Conversely, if $m_\alpha\mid p$, then $p(\alpha)=q(\alpha)\cdot0=0$.

4. Two monic polynomials of least degree divide each other, so they are equal.

:::

Similar matrices have the same minimal polynomial, since $p(P^{-1}AP)=P^{-1}p(A)P$.

::: {#prp-eigenvalue-root-of-minimal-polynomial .proposition name="Eigenvalues are roots of the minimal polynomial"}

If $\alpha(v)=\lambda v$ with $v\ne0$, then $p(\alpha)v=p(\lambda)v$ for every $p\in F[t]$. In particular every eigenvalue $\lambda$ of $\alpha$ is a root of $m_\alpha$.

:::

::: {.proof}

1. $\alpha^iv=\lambda^iv$ by induction on $i$, so $p(\alpha)v=\sum a_i\lambda^iv=p(\lambda)v$.

2. With $p=m_\alpha$: $0=m_\alpha(\alpha)v=m_\alpha(\lambda)v$, and $v\ne0$, so $m_\alpha(\lambda)=0$.

:::

The converse, that every root of $m_\alpha$ in $F$ is an eigenvalue, follows from Cayley–Hamilton (@cor-minimal-and-characteristic-same-roots).

::: {#thm-diagonalisability-minimal-polynomial .theorem name="Diagonalisability theorem"}

$\alpha\in\operatorname{End}(V)$ is diagonalisable if and only if $p(\alpha)=0$ for some polynomial $p$ that is a product of distinct linear factors, $p(t)=(t-\lambda_1)\cdots(t-\lambda_k)$ with distinct $\lambda_i\in F$. Equivalently, if and only if $m_\alpha$ is such a product.

:::

::: {.proof}

1. If $\alpha$ is diagonalisable with distinct eigenvalues $\lambda_1,\dots,\lambda_k$, let $p(t)=\prod_i(t-\lambda_i)$. For an eigenvector $v$ with eigenvalue $\lambda_j$, $p(\alpha)v=p(\lambda_j)v=0$ (@prp-eigenvalue-root-of-minimal-polynomial). A basis of eigenvectors is killed by $p(\alpha)$, so $p(\alpha)=0$.

2. Conversely, let $p(\alpha)=0$ with $p=\prod_{i=1}^k(t-\lambda_i)$, $\lambda_i$ distinct. Let $q_j(t)=\prod_{i\ne j}\frac{t-\lambda_i}{\lambda_j-\lambda_i}$, so $q_j(\lambda_i)=\delta_{ij}$.

3. The polynomial $q_1+\dots+q_k-1$ has degree $<k$ and vanishes at the $k$ points $\lambda_1,\dots,\lambda_k$, so it is $0$ (@thm-at-most-d-roots). Hence $\sum_jq_j(\alpha)=\iota$, and every $v=\sum_jq_j(\alpha)v$.

4. $(\alpha-\lambda_j\iota)q_j(\alpha)$ is a scalar multiple of $p(\alpha)=0$, so $q_j(\alpha)v\in E(\lambda_j)$. Hence $V=\sum_jE(\lambda_j)$ (the $E(\lambda_j)$ that are $\{0\}$ contribute nothing), and $\alpha$ is diagonalisable by @thm-diagonalizable-iff-eigenspaces.

5. For the last sentence: $p(\alpha)=0$ for such a $p$ iff $m_\alpha\mid p$ (@lem-minimal-polynomial-divides), and a monic divisor of a product of distinct linear factors is again such a product.

:::

::: {#thm-simultaneous-diagonalisation .theorem name="Simultaneous diagonalisation"}

Let $\alpha,\beta\in\operatorname{End}(V)$ both be diagonalisable. There is a basis in which both are diagonal if and only if $\alpha\beta=\beta\alpha$.

:::

::: {.proof}

1. Diagonal matrices commute, so if both are diagonal in one basis, $\alpha\beta=\beta\alpha$.

2. Conversely, let $V=E_1\oplus\dots\oplus E_k$ be the eigenspace decomposition of $\alpha$ (@thm-diagonalizable-iff-eigenspaces). Each $E_i$ is $\beta$-invariant: if $\alpha v=\lambda_iv$, then $\alpha(\beta v)=\beta\alpha v=\lambda_i\beta v$.

3. $m_\beta(\beta)=0$, so the restriction $\beta|_{E_i}$ is also killed by $m_\beta$, a product of distinct linear factors; by @thm-diagonalisability-minimal-polynomial $\beta|_{E_i}$ is diagonalisable.

4. Choose in each $E_i$ a basis of eigenvectors of $\beta|_{E_i}$. Its vectors are eigenvectors of $\alpha$ (with eigenvalue $\lambda_i$) and of $\beta$. Together they form a basis of $V$ (@prp-direct-sum-criteria) in which both maps are diagonal.

:::

::: {#exm-minimal-polynomial .example name="Minimal polynomials"}

1. $A=\begin{bmatrix}2&0&0\\0&2&0\\0&0&3\end{bmatrix}$ has $\chi_A=(t-2)^2(t-3)$ but $m_A=(t-2)(t-3)$: diagonal matrices are killed by the product over their distinct diagonal entries.
2. $B=\begin{bmatrix}2&1&0\\0&2&0\\0&0&3\end{bmatrix}$ has the same $\chi$, but $(B-2I)(B-3I)=\begin{bmatrix}0&-1&0\\0&0&0\\0&0&0\end{bmatrix}\ne0$, so $m_B=(t-2)^2(t-3)$ and $B$ is not diagonalisable.
3. A projection $\pi$ ($\pi^2=\pi$) is killed by $t^2-t=t(t-1)$, so it is diagonalisable with eigenvalues among $0,1$. An involution ($\sigma^2=\iota$) is killed by $(t-1)(t+1)$, which has distinct factors when $1+1\ne0$; over $\mathbb F_2$ the swap matrix is an involution that is not diagonalisable (@exm-endomorphism-not-diagonalisable).

:::

::: {#fig-minimal-polynomial-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[xshift=0cm]
\node[lab] (n000) at (0,-0.0) {$e_1$};
\node[lab] (n001) at (1.5,-0.0) {$0$};
\draw[map] (n000) -- node[lab, tick, above] {$A-2I$} (n001);
\node[lab] (n010) at (0,-0.9) {$e_2$};
\node[lab] (n011) at (1.5,-0.9) {$0$};
\draw[map] (n010) -- node[lab, tick, above] {$A-2I$} (n011);
\node[lab] (n020) at (0,-1.8) {$e_3$};
\node[lab] (n021) at (1.5,-1.8) {$0$};
\draw[map] (n020) -- node[lab, tick, above] {$A-3I$} (n021);
\node[lab, above] at (1.2,0.5) {$A$: $m_A=(t-2)(t-3)$};
\end{scope}
\begin{scope}[xshift=4.5cm]
\node[lab] (n400) at (0,-0.0) {$e_2$};
\node[lab] (n401) at (1.5,-0.0) {$e_1$};
\draw[map] (n400) -- node[lab, tick, above] {$B-2I$} (n401);
\node[lab] (n402) at (3.0,-0.0) {$0$};
\draw[map] (n401) -- node[lab, tick, above] {$B-2I$} (n402);
\node[lab] (n410) at (0,-0.9) {$e_3$};
\node[lab] (n411) at (1.5,-0.9) {$0$};
\draw[map] (n410) -- node[lab, tick, above] {$B-3I$} (n411);
\node[lab, above] at (1.2,0.5) {$B$: $m_B=(t-2)^2(t-3)$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Parts 1 and 2: for $A$ one step of $A-2I$ kills $e_1$ and $e_2$, but for $B$ the vector $e_2$ needs two steps of $B-2I$. The exponent of $t-\lambda$ in $m$ is the length of the longest such chain.

:::
