---
title: "The Spectral Theorem for Compact Self-Adjoint Operators"
sources: [camii-lan-4, camii-lans-4]
requires: [math/analysis/hilbert-spaces/compact-operators, math/analysis/hilbert-spaces/orthonormal-bases]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Section 4.6, and Example Sheet 4 (questions 9, 12, 13), in our own wording; proofs written out in steps. The finite-dimensional spectral theorem is math/linear-algebra/inner-product-spaces/spectral-theorem. -->

A compact self-adjoint operator is diagonalisable with an orthonormal basis of eigenvectors and eigenvalues tending to $0$. This is the infinite-dimensional version of the spectral theorem for symmetric matrices.

::: {#prp-self-adjoint-norm .proposition name="Norm of a self-adjoint operator"}

For self-adjoint $T\in B(H)$, $\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|$.

:::

::: {.proof}

1. Let $M=\sup_{\|x\|=1}|\langle Tx,x\rangle|\le\|T\|$.

2. For $x,y$, using $T=T^*$, $4\operatorname{Re}\langle Tx,y\rangle=\langle T(x+y),x+y\rangle-\langle T(x-y),x-y\rangle\le M(\|x+y\|^2+\|x-y\|^2)=2M(\|x\|^2+\|y\|^2)$.

3. For $\|x\|=1$ with $Tx\ne0$ take $y=Tx/\|Tx\|$: $4\|Tx\|\le4M$. So $\|T\|\le M$.

:::

::: {#lem-extremal-eigenvalue .lemma name="An extremal value is an eigenvalue"}

Let $T\in K(H)$ be self-adjoint and non-zero. Then $\|T\|$ or $-\|T\|$ is an eigenvalue of $T$.

:::

::: {.proof}

1. By @prp-self-adjoint-norm there are unit vectors $x_n$ with $\langle Tx_n,x_n\rangle\to\mu$, where $\mu=\pm\|T\|$.

2. $\|(T-\mu)x_n\|^2=\|Tx_n\|^2-2\mu\langle Tx_n,x_n\rangle+\mu^2\le2\mu^2-2\mu\langle Tx_n,x_n\rangle\to0$.

3. By compactness pass to a subsequence with $Tx_n\to y$. Then $\mu x_n=Tx_n-(T-\mu)x_n\to y$, so $x_n\to y/\mu$, a unit vector $x$ with $Tx=\mu x$ by continuity.

:::

::: {#prp-eigenspaces-orthogonal .proposition name="Eigenspaces of a self-adjoint operator"}

For self-adjoint $T$, eigenvalues are real, eigenvectors for distinct eigenvalues are orthogonal, and if $F$ is a closed invariant subspace ($TF\subseteq F$) then so is $F^\perp$.

:::

::: {.proof}

1. If $Tx=\lambda x$, $x\ne0$, then $\lambda\|x\|^2=\langle Tx,x\rangle=\langle x,Tx\rangle=\bar\lambda\|x\|^2$.

2. If $Tx=\lambda x$, $Ty=\mu y$, $\lambda\ne\mu$, then $\lambda\langle x,y\rangle=\langle Tx,y\rangle=\langle x,Ty\rangle=\mu\langle x,y\rangle$, so $\langle x,y\rangle=0$.

3. If $y\in F^\perp$ and $x\in F$ then $\langle Ty,x\rangle=\langle y,Tx\rangle=0$.

:::

::: {#thm-spectral-compact .theorem name="Spectral theorem for compact self-adjoint operators"}

Let $H$ be a Hilbert space and $T\in K(H)$ self-adjoint. Then $H$ has an orthonormal basis of eigenvectors of $T$ on $\overline{\operatorname{im}T}$ together with a basis of $\ker T$: precisely, there are real eigenvalues $\lambda_1,\lambda_2,\dots$ with $|\lambda_1|\ge|\lambda_2|\ge\cdots$, $\lambda_n\to0$ if there are infinitely many, and orthonormal eigenvectors $e_n$ with
$$Tx=\sum_n\lambda_n\langle x,e_n\rangle e_n\qquad(x\in H),$$
the series converging in norm; $\{e_n\}$ together with an orthonormal basis of $\ker T$ is an orthonormal basis of $H$.

:::

::: {.proof}

1. *Construction.* Let $H_0=H$, $T_0=T$. If $T_{n-1}:=T|_{H_{n-1}}\ne0$, by @lem-extremal-eigenvalue choose a unit $e_n\in H_{n-1}$ and $\lambda_n=\pm\|T_{n-1}\|$ with $Te_n=\lambda_ne_n$. Put $H_n=\{e_1,\dots,e_n\}^\perp$. By @prp-eigenspaces-orthogonal, $H_n$ is invariant under $T$, so $T_n=T|_{H_n}$ is again compact self-adjoint, and $|\lambda_{n+1}|=\|T_n\|\le\|T_{n-1}\|=|\lambda_n|$.

2. *Eigenvalues tend to $0$.* By @thm-compact-spectrum-discrete the only possible accumulation point of the eigenvalues is $0$; if infinitely many $e_n$ are produced, $\lambda_n\to0$. (Or directly: $(e_n)$ is orthonormal, so $e_n\to0$ weakly and compactness forces $Te_n\to0$.)

3. *The expansion.* For $x\in H$ and $N$ finite, $x-\sum_{n\le N}\langle x,e_n\rangle e_n\in H_N$, and $\|T|_{H_N}\|=|\lambda_{N+1}|$. Hence
$$\Big\|Tx-\sum_{n\le N}\lambda_n\langle x,e_n\rangle e_n\Big\|=\Big\|T\Big(x-\sum_{n\le N}\langle x,e_n\rangle e_n\Big)\Big\|\le|\lambda_{N+1}|\|x\|\to0.$$
If the construction stops with $T_N=0$ then $T$ vanishes on $H_N$, and the formula holds exactly.

4. *Basis.* The vectors in $\bigcap_nH_n$ are in $\ker T$ (by step 3 $Tx=0$ when $x\perp$ all $e_n$), and conversely $\ker T\perp e_n$ (as $\lambda_n\ne0$ and eigenvectors for different eigenvalues are orthogonal). So $\bigcap H_n=\ker T$, and $H=\overline{\operatorname{span}}\{e_n\}\oplus\ker T$ by @thm-projection.

:::

::: {#fig-spectral-theorem-compact-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle (1.2); \draw[->, faint] (-1.6,0) -- (1.6,0); \draw[->, faint] (0,-1.6) -- (0,1.6);
\draw[map] (2.0,0) -- (3.2,0); \node[lab, above] at (2.6,0) {$T$};
\draw[regionA] (5.6,0) ellipse (1.9 and 0.7);
\draw[hl] (3.7,0) -- (7.5,0) node[lab, right] {$\lambda_1e_1$}; \draw[hl] (5.6,-0.7) -- (5.6,0.7); \node[lab, above] at (5.6,0.7) {$\lambda_2e_2$};
\end{tikzpicture}
\end{center}
```

A compact self-adjoint operator stretches the unit ball along orthonormal axes $e_n$ by factors $\lambda_n\to0$.

:::

::: {#cor-compact-self-adjoint-functional-calculus .corollary name="Positive square root"}

If $T\in K(H)$ is positive ($\langle Tx,x\rangle\ge0$), there is a unique positive operator $S$ with $S^2=T$, and $S$ is compact.

:::

::: {.proof}

1. By @thm-spectral-compact, $T=\sum\lambda_n\langle\cdot,e_n\rangle e_n$ with $\lambda_n=\langle Te_n,e_n\rangle\ge0$. Define $Sx=\sum\sqrt{\lambda_n}\langle x,e_n\rangle e_n$. It is bounded with $\|S\|^2=\|T\|$, positive, and compact (a norm limit of finite rank operators since $\sqrt{\lambda_n}\to0$). Clearly $S^2=T$.

2. *Uniqueness.* If $S'$ is positive with $S'^2=T$, then $S'$ commutes with $T$, so each eigenspace of $T$ is $S'$-invariant. On the eigenspace for $\lambda>0$ (finite-dimensional), $S'$ is positive with square $\lambda$, hence has the single eigenvalue $\sqrt\lambda$: so $S'=\sqrt\lambda$ there. On $\ker T$, $\|S'x\|^2=\langle Tx,x\rangle=0$ so $S'x=0$. Thus $S'=S$ on a basis, hence everywhere.

:::

::: {#exm-compact-no-eigenvalue .example name="A compact operator with no eigenvalue"}

On $L^2[0,1]$ the Volterra operator $(Vf)(x)=\int_0^xf(t)\,dt$ is compact (it maps the unit ball to a bounded equicontinuous family in $C[0,1]$, by Arzelà–Ascoli) but has no eigenvalue: $Vf=\lambda f$ with $\lambda\ne0$ forces $f(0)=0$ and $f'=f/\lambda$, so $f=0$, and $Vf=0$ forces $f=0$. Its spectrum is $\{0\}$. So the spectral theorem needs self-adjointness, and the Fredholm alternative gives $\sigma(V)\setminus\{0\}=\emptyset$ consistently.

:::
