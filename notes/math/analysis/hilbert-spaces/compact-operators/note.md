---
title: "Compact Operators"
sources: [camii-lan-4, camii-lans-4]
requires: [math/analysis/hilbert-spaces/spectrum]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 4.5, and Example Sheet 4 (questions 3, 10, 12), in our own wording; proofs written out in steps. -->

Compact operators are the infinite-dimensional operators closest to matrices: they are uniform limits of finite-rank operators, and their spectrum behaves like that of a matrix, apart from $0$.

::: {#def-compact-operator .definition name="Compact operator"}

Let $X,Y$ be Banach spaces. $T\in B(X,Y)$ is *compact* if the closure of $T(B_X(1))$ is compact in $Y$; equivalently, for every bounded sequence $(x_n)$ in $X$ the sequence $(Tx_n)$ has a convergent subsequence. Write $K(X,Y)$ for the compact operators and $K(X)=K(X,X)$. Operators of finite rank are compact (bounded sets in finite-dimensional spaces are relatively compact).

:::

::: {#exm-diagonal-compact .example name="Diagonal operators"}

Let $a=(a_n)\in\ell^\infty$ and $T:\ell^2\to\ell^2$, $T(\sum x_ne_n)=\sum a_nx_ne_n$. Then $T\in B(\ell^2)$ and $\|T\|=\|a\|_\infty$. Its eigenvalues are the $a_n$, its approximate point spectrum and spectrum are $\overline{\{a_n\}}$, and $T$ is compact if and only if $a\in c_0$. Indeed, if $a\in c_0$, the truncations $T_N=\sum_{n\le N}a_nx_ne_n$ have finite rank and $\|T-T_N\|=\sup_{n>N}|a_n|\to0$, so $T$ is a norm limit of finite rank operators (@prp-compact-closed). If $a_n\not\to0$, there is $\varepsilon>0$ and infinitely many $n$ with $|a_n|\ge\varepsilon$; then $Te_n$ for these $n$ are $\varepsilon$-separated ($\|Te_n-Te_m\|\ge\varepsilon\sqrt2$), with no convergent subsequence.

:::

::: {#prp-compact-closed .proposition name="The compact operators form a closed ideal"}

$K(X,Y)$ is a closed subspace of $B(X,Y)$. If $T\in K(X,Y)$, $S\in B(Y,Z)$, $R\in B(W,X)$ then $STR$ is compact. A norm limit of finite rank operators is compact; on a Hilbert space the converse holds, so $K(H)$ is the closure of the finite rank operators.

:::

::: {.proof}

1. *Subspace.* If $T_1,T_2$ are compact and $(x_n)$ is bounded, extract a subsequence along which $T_1x_n$ converges, then a further one along which $T_2x_n$ converges.

2. *Closed.* Let $T_k\to T$ in norm with $T_k$ compact. Then $T(B_X(1))$ is totally bounded: given $\varepsilon$ pick $k$ with $\|T-T_k\|<\varepsilon/3$ and a finite $\varepsilon/3$-net of $T_k(B_X(1))$; it is an $\varepsilon$-net of $T(B_X(1))$. $Y$ is complete, so totally bounded sets are relatively compact (@thm-compact-iff-complete-totally-bounded).

3. *Ideal:* $R(B_W(1))\subseteq B_X(\|R\|)$, so $TR$ is compact; continuous maps send compact sets to compact sets, so $S$ composed with $T$ is compact.

4. *Hilbert space, converse.* Let $T\in K(H)$ and $\varepsilon>0$. The closure of $T(B_H(1))$ is compact, so it has a finite $\varepsilon$-net $y_1,\dots,y_m$. Let $P$ be the orthogonal projection onto $\operatorname{span}(y_1,\dots,y_m)$. Then $PT$ has finite rank and for $\|x\|\le1$, picking $y_i$ with $\|Tx-y_i\|<\varepsilon$, $\|Tx-PTx\|\le\|Tx-y_i\|+\|P(y_i-Tx)\|<2\varepsilon$. So $\|T-PT\|\le2\varepsilon$.

:::

::: {#prp-compact-adjoint .proposition name="Compact operators and adjoints"}

On a Hilbert space, $T\in K(H)$ implies $T^*\in K(H)$.

:::

::: {.proof}

$T$ is a norm limit of finite rank operators $T_k$ by @prp-compact-closed, so $T^*$ is a norm limit of the $T_k^*$ (as $\|T^*-T_k^*\|=\|T-T_k\|$), which have finite rank ($\operatorname{im}T_k^*\subseteq(\ker T_k)^\perp$ and $\dim(\ker T_k)^\perp=\operatorname{rank}T_k$). Apply @prp-compact-closed again.

:::

::: {#thm-compact-infinite-dim-not-invertible .theorem name="Compact operators are never invertible in infinite dimensions"}

If $X$ is an infinite-dimensional Banach space and $T\in K(X)$, then $T$ is not invertible; hence $0\in\sigma(T)$.

:::

::: {.proof}

If $T$ were invertible then $I=T^{-1}T$ would be compact by @prp-compact-closed, so the closed unit ball would be compact, contradicting @thm-unit-ball-compact.

:::

::: {#lem-fredholm-range-closed .lemma name="$I-T$ has closed range"}

Let $T\in K(X)$ on a Banach space and $\lambda\ne0$. Then $\operatorname{im}(T-\lambda I)$ is closed.

:::

::: {.proof}

1. Write $S=T-\lambda$ and $N=\ker S$, which is finite-dimensional (the unit ball of $N$ satisfies $T x=\lambda x$ and is compact, so $\dim N<\infty$ by @thm-unit-ball-compact).

2. *Claim:* there is $c>0$ with $\|Sx\|\ge c\operatorname{dist}(x,N)$. If not, there are $x_n$ with $\operatorname{dist}(x_n,N)=1$ and $Sx_n\to0$. As $N$ is finite-dimensional we may subtract the nearest point of $N$ and assume $\|x_n\|\le2$. By compactness of $T$ pass to a subsequence with $Tx_n\to y$. Then $\lambda x_n=Tx_n-Sx_n\to y$, so $x_n\to y/\lambda=:x$ with $Sx=\lim Sx_n=0$ and $x\in N$, contradicting $\operatorname{dist}(x_n,N)=1$.

3. Let $z$ be in the closure of $\operatorname{im}S$, with $Sx_n\to z$. Replace $x_n$ by $x_n-\nu_n$ where $\nu_n\in N$ is a nearest point of $N$ (it exists since $N$ is finite-dimensional); the images $Sx_n$ are unchanged and now $\|x_n\|=\operatorname{dist}(x_n,N)$. By the claim $\|x_n\|=\operatorname{dist}(x_n,N)\le c^{-1}\|Sx_n\|$, which is bounded. Then $(Tx_n)$ has a convergent subsequence, so $\lambda x_n=Tx_n-Sx_n$ converges along it to some $x$, and $Sx=\lim Sx_n=z$ by continuity. So $z\in\operatorname{im}S$.

:::

::: {#thm-fredholm-hilbert .theorem name="Fredholm alternative on a Hilbert space"}

Let $T\in K(H)$ and $\lambda\ne0$. Then $T-\lambda I$ is injective if and only if it is surjective, i.e. either $\lambda\in\rho(T)$ or $\lambda$ is an eigenvalue. Consequently, $\sigma(T)\setminus\{0\}=\sigma_p(T)\setminus\{0\}$.

:::

::: {.proof}

1. Suppose $S=T-\lambda$ is injective but not surjective. Put $H_n=\operatorname{im}(S^n)$. These are closed by @lem-fredholm-range-closed applied to $S^n=(T-\lambda)^n=T'-(-\lambda)^n$ with $T'$ compact (expand the binomial), and decreasing: $H_0\supsetneq H_1\supsetneq\cdots$. The inclusions are strict: if $H_n=H_{n+1}$, then since $S^n$ is injective, applying $(S^n)^{-1}$ gives $H=SH$, contradicting that $S$ is not surjective.

2. Choose unit vectors $x_n\in H_n\cap H_{n+1}^\perp$. For $m<n$, $Tx_m-Tx_n=\lambda x_m+Sx_m-Tx_n$ and $Sx_m-Tx_n=Sx_m-Sx_n-\lambda x_n\in H_{m+1}$. Hence $\|Tx_m-Tx_n\|\ge|\lambda|\,\operatorname{dist}(x_m,H_{m+1})=|\lambda|$, since $x_m\perp H_{m+1}$.

3. So $(Tx_n)$ has no convergent subsequence, contradicting compactness.

4. Conversely, if $S$ is surjective then $S^*=T^*-\bar\lambda$ is injective ($\ker S^*=(\operatorname{im}S)^\perp=0$), with $T^*$ compact (@prp-compact-adjoint), so by the first part $S^*$ is surjective, hence $S$ injective: $(\ker S)^\perp=\overline{\operatorname{im}S^*}=H$.

:::

::: {#thm-compact-spectrum-discrete .theorem name="Spectrum of a compact operator"}

Let $X$ be an infinite-dimensional Banach space and $T\in K(X)$ (on a Hilbert space for the full statement). Then $0\in\sigma(T)$, and $\sigma(T)\setminus\{0\}$ consists of eigenvalues of finite multiplicity; the only possible accumulation point of $\sigma(T)$ is $0$.

:::

::: {.proof}

1. $0\in\sigma(T)$ by @thm-compact-infinite-dim-not-invertible. Non-zero spectrum consists of eigenvalues by @thm-fredholm-hilbert (Hilbert case), and the eigenspaces are finite-dimensional by step 1 of @lem-fredholm-range-closed.

2. *Accumulation only at $0$.* Suppose there are distinct eigenvalues $\lambda_n$ with $|\lambda_n|\ge\varepsilon>0$, eigenvectors $e_n$ and $Y_n=\operatorname{span}(e_1,\dots,e_n)$. The eigenvectors are linearly independent so $Y_n\subsetneq Y_{n+1}$. By Riesz's lemma (@lem-riesz) choose unit $y_n\in Y_n$ with $\operatorname{dist}(y_n,Y_{n-1})\ge\frac12$.

3. For $m<n$, $Ty_n-Ty_m=\lambda_ny_n-(\lambda_ny_n-Ty_n+Ty_m)$ where $\lambda_ny_n-Ty_n\in Y_{n-1}$ (it kills the $e_n$ component) and $Ty_m\in Y_m\subseteq Y_{n-1}$. So $\|Ty_n-Ty_m\|\ge|\lambda_n|/2\ge\varepsilon/2$, again contradicting compactness.

:::

::: {#fig-compact-operators-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.4,0) -- (5.2,0); \draw[->, faint] (0,-1.2) -- (0,1.4);
\foreach \k in {1,2,3,4,5,6,7,8} { \node[dot] at ({4.4/\k},{0.5*sin(\k*80)/\k}) {}; }
\node[hl dot] at (0,0) {}; \node[lab, below left] at (0,0) {$0$};
\node[lab, above] at (3.2,0.9) {eigenvalues accumulate only at $0$};
\end{tikzpicture}
\end{center}
```

The non-zero spectrum of a compact operator is a sequence of eigenvalues tending to $0$.

:::
