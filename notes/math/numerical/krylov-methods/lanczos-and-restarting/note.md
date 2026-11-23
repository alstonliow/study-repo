---
title: "The Lanczos Iteration and Restarting"
sources: [mit18335-19]
requires: [math/numerical/krylov-methods/arnoldi-iteration, math/numerical/eigenvalue-algorithms/shifted-qr-algorithm]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 19 (Arnoldi and Lanczos with restarting) and its note on why restarting is not trivial, in our own wording; proofs written out in steps; the loss of orthogonality was measured with numpy. -->

For a Hermitian matrix the Arnoldi iteration simplifies dramatically: the Hessenberg matrix is tridiagonal, so each new vector needs to be orthogonalised only against the previous two. This is the Lanczos iteration. Its two practical difficulties, loss of orthogonality in floating point and growing cost for nonsymmetric Arnoldi, both lead to the question of how to restart a Krylov method without throwing away what it has learned.

::: {#def-lanczos-iteration .definition name="Lanczos iteration"}

For Hermitian $A$, set $\beta_0=0$, $\mathbf{q}_0=\mathbf{0}$, $\mathbf{q}_1=\mathbf{b}/\lVert\mathbf{b}\rVert$, and for $n=1,2,\dots$:
$$\mathbf{v}=A\mathbf{q}_n,\quad\alpha_n=\mathbf{q}_n^{\mathsf H}\mathbf{v},\quad\mathbf{v}\gets\mathbf{v}-\beta_{n-1}\mathbf{q}_{n-1}-\alpha_n\mathbf{q}_n,\quad\beta_n=\lVert\mathbf{v}\rVert,\quad\mathbf{q}_{n+1}=\mathbf{v}/\beta_n .$$
The matrix $T_n=Q_n^{\mathsf H}AQ_n$ is real symmetric tridiagonal with diagonal $\alpha_1,\dots,\alpha_n$ and off-diagonal $\beta_1,\dots,\beta_{n-1}$.

:::

```{=latex}
\begin{algorithm}
\caption{Lanczos iteration}
\begin{algorithmic}
\INPUT Hermitian $A$, $\mathbf{b}\ne\mathbf{0}$
\STATE $\beta_0\gets0$, $\mathbf{q}_0\gets\mathbf{0}$, $\mathbf{q}_1\gets\mathbf{b}/\lVert\mathbf{b}\rVert$
\FOR{$n=1,2,\dots$}
    \STATE $\mathbf{v}\gets A\mathbf{q}_n$
    \STATE $\alpha_n\gets\mathbf{q}_n^{\mathsf H}\mathbf{v}$
    \STATE $\mathbf{v}\gets\mathbf{v}-\beta_{n-1}\mathbf{q}_{n-1}-\alpha_n\mathbf{q}_n$
    \STATE $\beta_n\gets\lVert\mathbf{v}\rVert$; \quad $\mathbf{q}_{n+1}\gets\mathbf{v}/\beta_n$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-lanczos-three-term .theorem name="The three-term recurrence"}

If $A$ is Hermitian, the Arnoldi matrix $H_n$ is real, symmetric and tridiagonal, so Arnoldi reduces to the Lanczos iteration: $A\mathbf{q}_n=\beta_{n-1}\mathbf{q}_{n-1}+\alpha_n\mathbf{q}_n+\beta_n\mathbf{q}_{n+1}$.

:::

::: {.proof}

1. $H_n=Q_n^{\mathsf H}AQ_n$ (@thm-arnoldi-relation) is Hermitian because $A$ is.

2. A Hermitian upper Hessenberg matrix is tridiagonal: its entries below the subdiagonal vanish, hence so do their mirror images above the superdiagonal.

3. The subdiagonal entries $h_{n+1,n}=\lVert\mathbf{v}\rVert$ are real and nonnegative, so the superdiagonal entries equal them; the diagonal of a Hermitian matrix is real. Writing $\alpha_n=h_{nn}$ and $\beta_n=h_{n+1,n}$, column $n$ of $AQ_n=Q_{n+1}\tilde H_n$ is the stated recurrence.

:::

Lanczos needs only three vectors at a time to compute $T_n$ and its Ritz values: $O(m)$ storage and $O(m)$ work per step beyond the product with $A$.

::: {#rmk-lanczos-and-restarting-1 .remark name="Loss of orthogonality and ghost eigenvalues"}

In floating point the vectors $\mathbf{q}_j$ lose orthogonality, and not gradually: Paige showed that orthogonality is lost exactly in the direction of Ritz vectors that have converged. Once a Ritz value has converged, rounding errors reintroduce its eigenvector, and the iteration finds the same eigenvalue again: *ghost* copies appear among the Ritz values. The eigenvalues are still found, just with spurious duplicates. Remedies are full reorthogonalisation (back to Arnoldi's cost), *selective* reorthogonalisation against converged Ritz vectors only, or simply discarding duplicates.

:::

::: {#exm-lanczos-ghosts .example name="Ghost eigenvalues in double precision"}

Run Lanczos on the diagonal matrix of @exm-ritz-values (eigenvalues filling $[0,2]$ plus $2.5$ and $3$). At $n=10$, $\lVert I-Q_n^{\mathsf T}Q_n\rVert\approx10^{-14}$; at $n=20$ it is $10^{-9}$, at $n=30$ about $10^{-3}$, and by $n=40$ orthogonality is gone. At $n=40$ the Ritz values contain $3.0$ twice, and at $n=80$ three times, although $3$ is a simple eigenvalue.

:::

::: {#fig-lanczos-and-restarting-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.11cm, y=0.3cm]
\draw[->, faint] (0,-15) -- (85,-15) node[lab, right] {$n$};
\draw[->, faint] (0,-15) -- (0,1.5) node[lab, above] {$\log_{10}\lVert I-Q_n^{\mathsf T}Q_n\rVert$};
\foreach \x in {20,40,60,80} {\draw[faint] (\x,-15.3) -- (\x,-14.7); \node[tick, below] at (\x,-15.3) {$\x$};}
\foreach \y in {-14,-10,-6,-2} {\draw[faint] (-0.6,\y) -- (0.6,\y); \node[tick, left] at (-0.6,\y) {$\y$};}
\draw[hl] plot coordinates {(10,-14.09) (20,-8.86) (30,-3.07) (40,0) (50,0) (60,0) (80,0.3)};
\foreach \p in {(10,-14.09),(20,-8.86),(30,-3.07),(40,0),(50,0),(60,0),(80,0.3)} {\fill[accent] \p circle (2.2pt);}
\node[note] at (40,-2) {one ghost of $3$};
\node[note] at (73,-2) {two ghosts};
\draw[faint, ->] (40,-1.3) -- (40,-0.4);
\draw[faint, ->] (73,-1.3) -- (79,-0.1);
\end{tikzpicture}
\end{center}
```

Loss of orthogonality of the Lanczos vectors in @exm-lanczos-ghosts. It grows exponentially once the outlier $3$ has converged (by $n\approx8$), and complete loss coincides with the appearance of duplicate Ritz values.

:::

::: {#rmk-lanczos-and-restarting-2 .remark name="Why restarting is not trivial"}

Arnoldi on a nonsymmetric matrix costs $O(n^2m)$ work and $O(nm)$ storage after $n$ steps, so one restarts after a fixed number $n$ of steps with a new starting vector. The obvious choice, the current Ritz vector for the wanted eigenvalue, discards the information in the other Krylov directions: the convergence of a Krylov method comes from polynomial approximation over the whole space, and the restarted method may stall. For several wanted eigenvalues one would have to combine several Ritz vectors into one starting vector, and no single combination keeps them all. A good restart must keep a whole *subspace*, not one vector.

:::

::: {#def-implicit-restart .definition name="Implicitly restarted Arnoldi"}

After $n=k+p$ Arnoldi steps, with $k$ wanted Ritz values, take the $p$ unwanted Ritz values $\mu_1,\dots,\mu_p$ as shifts and apply $p$ steps of the shifted QR algorithm to $H_n$ (@def-shifted-qr-algorithm), $H_n\gets V^{\mathsf H}H_nV$, and update $Q_n\gets Q_nV$. Keeping the first $k$ columns gives an Arnoldi factorization of length $k$,
$$AQ_k^+=Q_k^+H_k^++\mathbf{f}_k\mathbf{e}_k^{\mathsf T},$$
whose starting vector is $\mathbf{q}_1^+\propto\prod_i(A-\mu_iI)\mathbf{q}_1$. Then $p$ further Arnoldi steps bring the length back to $n$, and the cycle repeats.

:::

::: {#prp-implicit-restart-filter .proposition name="The implicit restart is a polynomial filter"}

The restarted factorization is exactly the one Arnoldi would produce from the starting vector $\psi(A)\mathbf{q}_1$, where $\psi(z)=\prod_{i=1}^p(z-\mu_i)$. It costs $O(n^2m)$ flops per restart and no new products with $A$.

:::

::: {.proof}

1. One shifted QR step on $H_n$ with shift $\mu$ gives $H_n-\mu I=VR$ and $H_n^+=V^{\mathsf H}H_nV$. Multiply $AQ_n=Q_nH_n+\mathbf{f}\mathbf{e}_n^{\mathsf T}$ on the right by $V$: $A(Q_nV)=(Q_nV)H_n^++\mathbf{f}\mathbf{e}_n^{\mathsf T}V$.

2. $V$ is upper Hessenberg (as in @prp-qr-step-similarity), so $\mathbf{e}_n^{\mathsf T}V$ has nonzeros only in its last two entries. After $p$ steps the product of the $V$'s has $\mathbf{e}_n^{\mathsf T}V$ zero in its first $k-1$ entries, so the first $k$ columns satisfy an Arnoldi relation of length $k$ with a residual in the last column only.

3. *Starting vector.* From $(A-\mu I)Q_n=Q_n(H_n-\mu I)+\mathbf{f}\mathbf{e}_n^{\mathsf T}=Q_nVR+\mathbf{f}\mathbf{e}_n^{\mathsf T}$, the first column gives $(A-\mu I)\mathbf{q}_1=r_{11}(Q_nV)\mathbf{e}_1$, because $\mathbf{e}_n^{\mathsf T}\mathbf{e}_1=0$. So the new first vector is proportional to $(A-\mu I)\mathbf{q}_1$; repeating for each shift gives $\psi(A)\mathbf{q}_1$.

4. An Arnoldi factorization is determined by its starting vector (the Krylov spaces are), which proves the claim. The work is $p$ QR steps on an $n\times n$ Hessenberg matrix and the update $Q_nV$, $O(n^2m)$ in all.

:::

The filter $\psi$ vanishes at the unwanted Ritz values, so the restarted vector has its components along the corresponding eigenvectors damped, while the wanted directions are kept. This is the method behind ARPACK (`eigs`). The *thick restart* (Krylov–Schur) variant achieves the same with a Schur factorization of $H_n$ and is simpler to stabilise.

::: {#fig-lanczos-and-restarting-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.4cm, y=0.9cm]
\draw[->, faint] (-0.1,0) -- (3.3,0) node[lab, right] {$z$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {$\lvert\psi(z)\rvert$ (scaled)};
\draw[emph, domain=0:3.1, samples=120] plot (\x,{min(2.3,0.6*abs((\x-0.4)*(\x-1.0)*(\x-1.6)))});
\foreach \m in {0.4,1.0,1.6} {\fill[accent] (\m,0) circle (2pt);}
\node[note] at (1.0,-0.45) {unwanted Ritz values $\mu_i$ (shifts)};
\fill (2.5,0) circle (2pt); \fill (3.0,0) circle (2pt);
\node[note] at (2.75,-0.45) {wanted};
\end{tikzpicture}
\end{center}
```

The filter polynomial of an implicit restart with shifts $0.4$, $1.0$, $1.6$ (the unwanted Ritz values in the interior of the spectrum). It is small near the unwanted part and large near the wanted outlying eigenvalues, so the new starting vector $\psi(A)\mathbf{q}_1$ is enriched in the wanted eigenvectors.

:::
