---
title: "Preconditioning"
sources: [mit18335-21]
requires: [math/numerical/krylov-methods/cg-convergence, math/numerical/krylov-methods/gmres]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 21 (preconditioning techniques), in our own wording; proofs written out in steps; the CG and preconditioned CG runs were done with numpy. -->

Krylov methods converge fast when the eigenvalues are clustered away from the origin (GMRES) or the condition number is small (CG). A *preconditioner* $M\approx A$, cheap to invert, changes the system into an equivalent one with better spectral properties. Finding a good preconditioner is problem-dependent and usually more important than the choice of Krylov method.

::: {#def-preconditioning .definition name="Left, right and split preconditioning"}

Let $M$ be nonsingular with $M^{-1}\mathbf{v}$ cheap to compute. Instead of $A\mathbf{x}=\mathbf{b}$ solve

1. (left) $M^{-1}A\mathbf{x}=M^{-1}\mathbf{b}$;

2. (right) $AM^{-1}\mathbf{y}=\mathbf{b}$, then $\mathbf{x}=M^{-1}\mathbf{y}$;

3. (split, for symmetric positive definite $A$ and $M=CC^{\mathsf T}$) $C^{-1}AC^{-\mathsf T}\mathbf{z}=C^{-1}\mathbf{b}$, then $\mathbf{x}=C^{-\mathsf T}\mathbf{z}$.

All three have the same solution. $M^{-1}A$, $AM^{-1}$ and $C^{-1}AC^{-\mathsf T}$ are similar to each other, so they have the same eigenvalues; a good $M$ makes these eigenvalues clustered, ideally near $1$. The extremes are $M=I$ (no change, free) and $M=A$ (one step, but as costly as the original problem).

:::

::: {#def-preconditioned-cg .definition name="Preconditioned conjugate gradients"}

For symmetric positive definite $A$ and $M$, CG applied to the split system can be rewritten so that only $M^{-1}$, never $C$, is needed: with $\mathbf{z}_n=M^{-1}\mathbf{r}_n$,
$$\alpha_n=\frac{\mathbf{r}_{n-1}^{\mathsf T}\mathbf{z}_{n-1}}{\mathbf{p}_{n-1}^{\mathsf T}A\mathbf{p}_{n-1}},\quad\mathbf{x}_n=\mathbf{x}_{n-1}+\alpha_n\mathbf{p}_{n-1},\quad\mathbf{r}_n=\mathbf{r}_{n-1}-\alpha_nA\mathbf{p}_{n-1},$$
$$\mathbf{z}_n=M^{-1}\mathbf{r}_n,\quad\beta_n=\frac{\mathbf{r}_n^{\mathsf T}\mathbf{z}_n}{\mathbf{r}_{n-1}^{\mathsf T}\mathbf{z}_{n-1}},\quad\mathbf{p}_n=\mathbf{z}_n+\beta_n\mathbf{p}_{n-1},$$
starting from $\mathbf{r}_0=\mathbf{b}$, $\mathbf{z}_0=M^{-1}\mathbf{r}_0$, $\mathbf{p}_0=\mathbf{z}_0$.

:::

```{=latex}
\begin{algorithm}
\caption{Preconditioned conjugate gradients}
\begin{algorithmic}
\INPUT symmetric positive definite $A$ and $M$ (routines for $A\mathbf{v}$ and $M^{-1}\mathbf{v}$), $\mathbf{b}$
\STATE $\mathbf{x}\gets\mathbf{0}$, $\mathbf{r}\gets\mathbf{b}$, $\mathbf{z}\gets M^{-1}\mathbf{r}$, $\mathbf{p}\gets\mathbf{z}$, $\rho\gets\mathbf{r}^{\mathsf T}\mathbf{z}$
\WHILE{not converged}
    \STATE $\mathbf{w}\gets A\mathbf{p}$; \quad $\alpha\gets\rho/(\mathbf{p}^{\mathsf T}\mathbf{w})$
    \STATE $\mathbf{x}\gets\mathbf{x}+\alpha\mathbf{p}$; \quad $\mathbf{r}\gets\mathbf{r}-\alpha\mathbf{w}$
    \STATE $\mathbf{z}\gets M^{-1}\mathbf{r}$; \quad $\rho_{\text{new}}\gets\mathbf{r}^{\mathsf T}\mathbf{z}$
    \STATE $\mathbf{p}\gets\mathbf{z}+(\rho_{\text{new}}/\rho)\mathbf{p}$; \quad $\rho\gets\rho_{\text{new}}$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#thm-pcg-equivalence .theorem name="Preconditioned CG is CG on the split system"}

With $M=CC^{\mathsf T}$, the iterates of @def-preconditioned-cg are $\mathbf{x}_n=C^{-\mathsf T}\mathbf{z}^{\text{CG}}_n$, where $\mathbf{z}^{\text{CG}}_n$ are the CG iterates for $\hat A=C^{-1}AC^{-\mathsf T}$ and $\hat{\mathbf{b}}=C^{-1}\mathbf{b}$. Hence $\mathbf{x}_n$ minimises $\lVert\mathbf{x}-\mathbf{x}_*\rVert_A$ over $\mathcal K_n(M^{-1}A,M^{-1}\mathbf{b})$, and @thm-cg-chebyshev-bound holds with $\kappa(\hat A)=\kappa$ of $M^{-1}A$ (its eigenvalues are those of $M^{-1}A$).

:::

::: {.proof}

1. Run CG (@def-conjugate-gradient) on $(\hat A,\hat{\mathbf{b}})$ with variables $\hat{\mathbf{x}},\hat{\mathbf{r}},\hat{\mathbf{p}}$, and substitute $\hat{\mathbf{x}}=C^{\mathsf T}\mathbf{x}$, $\hat{\mathbf{r}}=C^{-1}\mathbf{r}$, $\hat{\mathbf{p}}=C^{\mathsf T}\mathbf{p}$.

2. Then $\hat{\mathbf{r}}^{\mathsf T}\hat{\mathbf{r}}=\mathbf{r}^{\mathsf T}C^{-\mathsf T}C^{-1}\mathbf{r}=\mathbf{r}^{\mathsf T}M^{-1}\mathbf{r}=\mathbf{r}^{\mathsf T}\mathbf{z}$ and $\hat{\mathbf{p}}^{\mathsf T}\hat A\hat{\mathbf{p}}=\mathbf{p}^{\mathsf T}A\mathbf{p}$, so $\alpha_n$ and $\beta_n$ agree.

3. The updates transform as: $\hat{\mathbf{x}}_n=\hat{\mathbf{x}}_{n-1}+\alpha\hat{\mathbf{p}}$ becomes $\mathbf{x}_n=\mathbf{x}_{n-1}+\alpha\mathbf{p}$; $\hat{\mathbf{r}}_n=\hat{\mathbf{r}}_{n-1}-\alpha\hat A\hat{\mathbf{p}}$ becomes $\mathbf{r}_n=\mathbf{r}_{n-1}-\alpha A\mathbf{p}$; and $\hat{\mathbf{p}}_n=\hat{\mathbf{r}}_n+\beta\hat{\mathbf{p}}$ becomes $\mathbf{p}_n=C^{-\mathsf T}C^{-1}\mathbf{r}_n+\beta\mathbf{p}=\mathbf{z}_n+\beta\mathbf{p}_{n-1}$.

4. The optimality and the bound transfer from @thm-cg-properties and @thm-cg-chebyshev-bound because $\lVert\hat{\mathbf{x}}-\hat{\mathbf{x}}_*\rVert_{\hat A}=\lVert\mathbf{x}-\mathbf{x}_*\rVert_A$ and $\hat A=C^{-1}(AM^{-1})C$ is similar to $AM^{-1}$, hence has the eigenvalues of $M^{-1}A$.

:::

::: {#exm-jacobi-preconditioner .example name="Jacobi preconditioning of a badly scaled matrix"}

Take the $400\times400$ second-difference matrix $T$ (with $2.01$ on the diagonal and $-1$ beside it, $\kappa(T)\approx400$) and scale it badly: $B=STS$ with $S$ diagonal and entries spread between $1$ and $100$. Then $\kappa(B)\approx3.8\times10^5$, and CG reduces the residual only to $10^{-4}$ in $400$ steps. The *Jacobi* (diagonal) preconditioner $M=\operatorname{diag}(B)$ undoes the scaling: $M^{-1/2}BM^{-1/2}=T/2.01$ has $\kappa\approx400$ again, and preconditioned CG reaches $10^{-10}$ in $200$ steps and machine precision by $300$.

:::

::: {#fig-preconditioning-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.027cm, y=0.36cm]
\draw[->, faint] (0,0) -- (410,0) node[lab, right] {$n$};
\draw[->, faint] (0,0) -- (0,-15.8) node[lab, below] {$\log_{10}\lVert\mathbf{r}_n\rVert/\lVert\mathbf{b}\rVert$};
\foreach \x in {100,200,300,400} {\draw[faint] (\x,-0.15) -- (\x,0.15); \node[tick, above] at (\x,0.15) {$\x$};}
\foreach \y in {-4,-8,-12} {\draw[faint] (-3,\y) -- (3,\y); \node[tick, left] at (-3,\y) {$\y$};}
\draw[emph] plot coordinates {(0,0) (40,-2.43) (80,-3.02) (120,-3.38) (160,-3.74) (200,-3.73) (240,-4.06) (280,-4.17) (320,-4.32) (360,-4.03) (400,-4.1)};
\draw[hl] plot coordinates {(0,0) (40,-3.67) (80,-5.57) (120,-7.48) (160,-9.19) (200,-10.85) (240,-12.64) (280,-14.37) (320,-14.86) (360,-14.82) (400,-14.82)};
\node[lab] at (330,-3.0) {CG};
\node[lab] at (250,-10.8) {Jacobi-preconditioned CG};
\end{tikzpicture}
\end{center}
```

Residuals for @exm-jacobi-preconditioner. Diagonal scaling ruins the conditioning ($\kappa\approx3.8\times10^5$) and CG stalls; the Jacobi preconditioner removes the scaling, and preconditioned CG converges at the rate set by $\kappa\approx400$.

:::

::: {#rmk-preconditioning-1 .remark name="A catalogue of preconditioners"}

1. *Jacobi* $M=\operatorname{diag}(A)$ and *block Jacobi*: trivial to apply, fixes bad scaling, little else.

2. *Incomplete factorizations*: perform Cholesky or LU but drop fill-in outside a chosen pattern (ILU(0), IC(0): keep only the pattern of $A$) or below a threshold. Cheap and often effective, but may break down for indefinite problems.

3. *Multigrid* and *domain decomposition*: for discretised PDEs, a preconditioner built from coarse-grid corrections can make $\kappa(M^{-1}A)$ bounded independently of the mesh size; then the iteration count does not grow as the mesh is refined.

4. *Problem-based*: a simpler physical model (e.g. constant coefficients) whose solver is fast, used as $M$ for the full model.

For nonsymmetric problems with GMRES, right preconditioning is often preferred because the residual it minimises is the true residual $\mathbf{b}-A\mathbf{x}$. The preconditioner may even change from step to step ("flexible GMRES").

:::
