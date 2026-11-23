---
title: "GMRES"
sources: [mit18335-20]
requires: [math/numerical/krylov-methods/arnoldi-iteration, math/numerical/qr-and-least-squares/least-squares-algorithms]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 20 (the GMRES algorithm and convergence of GMRES and Arnoldi), in our own wording; proofs written out in steps; residual histories computed with numpy for random 200 by 200 matrices. -->

GMRES ("generalized minimal residuals") solves $A\mathbf{x}=\mathbf{b}$ for a general nonsingular $A$ by choosing, at step $n$, the vector of the Krylov space $\mathcal K_n(A,\mathbf{b})$ with the smallest residual. Thanks to the Arnoldi relation this $m$-dimensional least squares problem becomes an $(n+1)\times n$ one.

::: {#def-gmres .definition name="GMRES"}

Starting from $\mathbf{x}_0=\mathbf{0}$, the $n$-th GMRES iterate is
$$\mathbf{x}_n=\operatorname*{arg\,min}_{\mathbf{x}\in\mathcal K_n}\lVert\mathbf{b}-A\mathbf{x}\rVert_2 .$$
With the Arnoldi relation $AQ_n=Q_{n+1}\tilde H_n$ and $\mathbf{x}=Q_n\mathbf{y}$, it is computed as $\mathbf{x}_n=Q_n\mathbf{y}_n$ where
$$\mathbf{y}_n=\operatorname*{arg\,min}_{\mathbf{y}\in\mathbb{C}^n}\bigl\lVert\tilde H_n\mathbf{y}-\lVert\mathbf{b}\rVert\mathbf{e}_1\bigr\rVert_2 .$$

:::

::: {#prp-gmres-small-problem .proposition name="The small least squares problem"}

For $\mathbf{x}=Q_n\mathbf{y}$, $\lVert\mathbf{b}-A\mathbf{x}\rVert_2=\bigl\lVert\lVert\mathbf{b}\rVert\mathbf{e}_1-\tilde H_n\mathbf{y}\bigr\rVert_2$, so the two minimisation problems in @def-gmres are equivalent.

:::

::: {.proof}

1. $\mathbf{b}=\lVert\mathbf{b}\rVert\mathbf{q}_1=Q_{n+1}\lVert\mathbf{b}\rVert\mathbf{e}_1$ and $AQ_n\mathbf{y}=Q_{n+1}\tilde H_n\mathbf{y}$ (@thm-arnoldi-relation).

2. So $\mathbf{b}-AQ_n\mathbf{y}=Q_{n+1}\bigl(\lVert\mathbf{b}\rVert\mathbf{e}_1-\tilde H_n\mathbf{y}\bigr)$, and $Q_{n+1}$ has orthonormal columns, which preserve norms.

:::

```{=latex}
\begin{algorithm}
\caption{GMRES}
\begin{algorithmic}
\INPUT $A$ (as a routine), $\mathbf{b}$, tolerance
\STATE $\mathbf{q}_1\gets\mathbf{b}/\lVert\mathbf{b}\rVert$
\FOR{$n=1,2,\dots$}
    \STATE one Arnoldi step: $\mathbf{q}_{n+1}$ and column $n$ of $\tilde H_n$
    \STATE update the QR factorization of $\tilde H_n$ by one Givens rotation
    \STATE residual norm $\rho_n=\min_{\mathbf{y}}\lVert\tilde H_n\mathbf{y}-\lVert\mathbf{b}\rVert\mathbf{e}_1\rVert$ \COMMENT{read off, $O(1)$}
    \IF{$\rho_n/\lVert\mathbf{b}\rVert<$ tolerance}
        \STATE solve the triangular system for $\mathbf{y}_n$; \textbf{return} $\mathbf{x}_n=Q_n\mathbf{y}_n$
    \ENDIF
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

Because $\tilde H_n$ grows by one column and one row per step, its QR factorization is updated by a single Givens rotation (@def-givens-rotation) applied to the new column; the residual norm is the magnitude of the last entry of the rotated right-hand side, so it is known at every step without forming $\mathbf{x}_n$.

::: {#thm-gmres-polynomial .theorem name="GMRES as polynomial approximation"}

Let $P_n$ be the set of polynomials $p$ of degree $\le n$ with $p(0)=1$. The GMRES residual is $\mathbf{r}_n=p_n(A)\mathbf{b}$, where $p_n$ minimises $\lVert p(A)\mathbf{b}\rVert$ over $P_n$. Consequently the residual norms never increase, and GMRES finds the exact solution after at most $m$ steps. If $A=V\Lambda V^{-1}$ is diagonalizable with spectrum $\Lambda(A)$,
$$\frac{\lVert\mathbf{r}_n\rVert}{\lVert\mathbf{b}\rVert}\le\kappa(V)\,\min_{p\in P_n}\ \max_{\lambda\in\Lambda(A)}\lvert p(\lambda)\rvert .$$

:::

::: {.proof}

1. $\mathbf{x}\in\mathcal K_n$ means $\mathbf{x}=q(A)\mathbf{b}$ with $\deg q<n$, so $\mathbf{b}-A\mathbf{x}=(1-zq(z))|_{z=A}\mathbf{b}=p(A)\mathbf{b}$ with $p=1-zq\in P_n$, and every $p\in P_n$ arises this way.

2. Minimising the residual over $\mathcal K_n$ is therefore minimising $\lVert p(A)\mathbf{b}\rVert$ over $P_n$. Since $P_n\subseteq P_{n+1}$ the minimum cannot increase.

3. The characteristic polynomial $\chi$ of $A$ has $\chi(0)=\det(-A)\ne0$; then $p=\chi/\chi(0)\in P_m$ and $p(A)=0$ (@thm-cayley-hamilton), so $\mathbf{r}_m=\mathbf{0}$.

4. *Bound.* $p(A)=Vp(\Lambda)V^{-1}$, so $\lVert p(A)\mathbf{b}\rVert\le\lVert V\rVert\lVert V^{-1}\rVert\max_{\lambda}\lvert p(\lambda)\rvert\,\lVert\mathbf{b}\rVert$. Take the minimum over $p\in P_n$.

:::

::: {#exm-gmres-disk .example name="Eigenvalues in a disk away from the origin"}

If the eigenvalues lie in the disk $\lvert z-c\rvert\le\rho$ with $\rho<\lvert c\rvert$, the polynomial $p(z)=(1-z/c)^n\in P_n$ has $\lvert p(\lambda)\rvert\le(\rho/\lvert c\rvert)^n$ there, so GMRES converges at least like $\kappa(V)(\rho/\lvert c\rvert)^n$. For $A=2I+0.5G/\sqrt m$ with $G$ a $200\times200$ matrix of independent standard normal entries, the eigenvalues fill roughly the disk $\lvert z-2\rvert\le0.5$, and the measured residual falls by a factor about $0.25=\rho/c$ per step, reaching $10^{-6}$ at $n=10$. For $A=0.9I+G/\sqrt m$ the eigenvalue disk $\lvert z-0.9\rvert\le1$ contains the origin; no polynomial with $p(0)=1$ can be small on it, and GMRES nearly stagnates: after $30$ steps the residual has only fallen to $0.35$.

:::

::: {#fig-gmres-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.3cm, y=0.55cm]
\draw[->, faint] (0,0) -- (31.5,0) node[lab, right] {$n$};
\draw[->, faint] (0,0) -- (0,-6.8) node[lab, below] {$\log_{10}\lVert\mathbf{r}_n\rVert/\lVert\mathbf{b}\rVert$};
\foreach \x in {10,20,30} {\draw[faint] (\x,-0.12) -- (\x,0.12); \node[tick, above] at (\x,0.12) {$\x$};}
\foreach \y in {-2,-4,-6} {\draw[faint] (-0.25,\y) -- (0.25,\y); \node[tick, left] at (-0.25,\y) {$\y$};}
\draw[hl] plot coordinates {(0,0) (1,-0.61) (2,-1.2) (3,-1.79) (4,-2.37) (5,-3.0) (6,-3.63) (7,-4.25) (8,-4.86) (9,-5.47) (10,-6.1)};
\draw[emph] plot coordinates {(0,0) (1,-0.14) (2,-0.21) (3,-0.25) (4,-0.27) (6,-0.28) (10,-0.28) (14,-0.3) (20,-0.3) (22,-0.32) (24,-0.35) (26,-0.36) (28,-0.4) (30,-0.45)};
\node[lab, anchor=west] at (10.6,-5.8) {disk $\lvert z-2\rvert\le0.5$};
\node[lab, anchor=west] at (15,-1.0) {disk $\lvert z-0.9\rvert\le1$};
\begin{scope}[xshift=6.6cm, yshift=-2.4cm, x=0.6cm, y=0.6cm]
\draw[faint, ->] (-1.4,0) -- (3.2,0); \draw[faint, ->] (0,-1.3) -- (0,1.3);
\draw[hl] (2,0) circle (0.5); \draw[emph] (0.9,0) circle (1);
\fill (0,0) circle (1.5pt) node[tick, below left] {$0$};
\end{scope}
\end{tikzpicture}
\end{center}
```

GMRES residuals for the two matrices of @exm-gmres-disk, with their eigenvalue disks (inset). When the origin is well outside the disk the residual falls geometrically at the rate $0.25$; when the disk surrounds the origin GMRES stagnates.

:::

::: {#rmk-gmres-1 .remark name="Restarted GMRES"}

Step $n$ costs $O(nm)$ flops for orthogonalisation and $Q_n$ needs $nm$ storage, so in practice one runs *GMRES($k$)*: after $k$ steps form $\mathbf{x}_k$, and restart with the residual as new right-hand side. Restarting limits the cost but discards the polynomial built so far; GMRES($k$) may stagnate where full GMRES would converge. A good preconditioner (@sec-math-numerical-krylov-methods-preconditioning), which makes the eigenvalues cluster away from the origin, is usually more important than the choice of $k$.

:::
