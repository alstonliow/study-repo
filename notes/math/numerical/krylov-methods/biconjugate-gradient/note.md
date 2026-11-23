---
title: "Biconjugate Gradients and Short-Recurrence Methods"
sources: [mit18335-23]
requires: [math/numerical/krylov-methods/preconditioning]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 23 (biconjugate gradient algorithms), in our own wording; proofs written out in steps; the residual histories were computed with numpy and scipy. -->

GMRES works for any nonsingular matrix but its cost per step grows; CG has constant cost per step but needs symmetry and definiteness. For nonsymmetric matrices one cannot have both an optimality property and short recurrences in general (Faber and Manteuffel). Biconjugate gradients keep the short recurrences and give up optimality, by working with two Krylov spaces, one for $A$ and one for $A^{\mathsf T}$.

::: {#def-biconjugate-gradient .definition name="Biconjugate gradients (BiCG)"}

Choose a "shadow" vector $\tilde{\mathbf{r}}_0$ (often $\tilde{\mathbf{r}}_0=\mathbf{r}_0=\mathbf{b}$). Set $\mathbf{x}_0=\mathbf{0}$, $\mathbf{p}_0=\mathbf{r}_0$, $\tilde{\mathbf{p}}_0=\tilde{\mathbf{r}}_0$, and for $n=1,2,\dots$:
$$\alpha_n=\frac{\tilde{\mathbf{r}}_{n-1}^{\mathsf T}\mathbf{r}_{n-1}}{\tilde{\mathbf{p}}_{n-1}^{\mathsf T}A\mathbf{p}_{n-1}},\quad\mathbf{x}_n=\mathbf{x}_{n-1}+\alpha_n\mathbf{p}_{n-1},\quad\mathbf{r}_n=\mathbf{r}_{n-1}-\alpha_nA\mathbf{p}_{n-1},\quad\tilde{\mathbf{r}}_n=\tilde{\mathbf{r}}_{n-1}-\alpha_nA^{\mathsf T}\tilde{\mathbf{p}}_{n-1},$$
$$\beta_n=\frac{\tilde{\mathbf{r}}_n^{\mathsf T}\mathbf{r}_n}{\tilde{\mathbf{r}}_{n-1}^{\mathsf T}\mathbf{r}_{n-1}},\quad\mathbf{p}_n=\mathbf{r}_n+\beta_n\mathbf{p}_{n-1},\quad\tilde{\mathbf{p}}_n=\tilde{\mathbf{r}}_n+\beta_n\tilde{\mathbf{p}}_{n-1}.$$
For symmetric positive definite $A$ and $\tilde{\mathbf{r}}_0=\mathbf{r}_0$ it reduces to CG.

:::

```{=latex}
\begin{algorithm}
\caption{Biconjugate gradients}
\begin{algorithmic}
\INPUT $A$ (routines for $A\mathbf{v}$ and $A^{\mathsf T}\mathbf{v}$), $\mathbf{b}$, shadow vector $\tilde{\mathbf{r}}$
\STATE $\mathbf{x}\gets\mathbf{0}$, $\mathbf{r}\gets\mathbf{b}$, $\mathbf{p}\gets\mathbf{r}$, $\tilde{\mathbf{p}}\gets\tilde{\mathbf{r}}$, $\rho\gets\tilde{\mathbf{r}}^{\mathsf T}\mathbf{r}$
\WHILE{not converged}
    \STATE $\mathbf{w}\gets A\mathbf{p}$; \quad $\alpha\gets\rho/(\tilde{\mathbf{p}}^{\mathsf T}\mathbf{w})$ \COMMENT{breakdown if $\tilde{\mathbf{p}}^{\mathsf T}\mathbf{w}=0$}
    \STATE $\mathbf{x}\gets\mathbf{x}+\alpha\mathbf{p}$; \quad $\mathbf{r}\gets\mathbf{r}-\alpha\mathbf{w}$; \quad $\tilde{\mathbf{r}}\gets\tilde{\mathbf{r}}-\alpha A^{\mathsf T}\tilde{\mathbf{p}}$
    \STATE $\rho_{\text{new}}\gets\tilde{\mathbf{r}}^{\mathsf T}\mathbf{r}$; \quad $\beta\gets\rho_{\text{new}}/\rho$; \quad $\rho\gets\rho_{\text{new}}$
    \STATE $\mathbf{p}\gets\mathbf{r}+\beta\mathbf{p}$; \quad $\tilde{\mathbf{p}}\gets\tilde{\mathbf{r}}+\beta\tilde{\mathbf{p}}$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#thm-bicg-biorthogonality .theorem name="Biorthogonality in BiCG"}

As long as no denominator vanishes, for $j<n$:
$$\tilde{\mathbf{r}}_j^{\mathsf T}\mathbf{r}_n=0,\qquad\mathbf{r}_j^{\mathsf T}\tilde{\mathbf{r}}_n=0,\qquad\tilde{\mathbf{p}}_j^{\mathsf T}A\mathbf{p}_n=0,\qquad\mathbf{p}_j^{\mathsf T}A^{\mathsf T}\tilde{\mathbf{p}}_n=0 .$$
So $\mathbf{r}_n\perp\mathcal K_n(A^{\mathsf T},\tilde{\mathbf{r}}_0)$ (a *Petrov–Galerkin* condition) with $\mathbf{x}_n\in\mathcal K_n(A,\mathbf{b})$, and in exact arithmetic BiCG terminates in at most $m$ steps.

:::

::: {.proof}

1. The proof of @thm-cg-properties goes through word for word with each inner product $\mathbf{u}^{\mathsf T}\mathbf{v}$ between two "primal" vectors replaced by the pairing $\tilde{\mathbf{u}}^{\mathsf T}\mathbf{v}$ of a shadow vector with a primal one, and $\mathbf{u}^{\mathsf T}A\mathbf{v}$ by $\tilde{\mathbf{u}}^{\mathsf T}A\mathbf{v}=(A^{\mathsf T}\tilde{\mathbf{u}})^{\mathsf T}\mathbf{v}$. Symmetry of $A$ was used only to move $A$ across an inner product, which is now exactly what the shadow recurrence with $A^{\mathsf T}$ provides.

2. The induction for $\tilde{\mathbf{r}}_j^{\mathsf T}\mathbf{r}_n=0$: for $j<n-1$, $\tilde{\mathbf{r}}_j^{\mathsf T}\mathbf{r}_{n-1}=0$ and $\tilde{\mathbf{r}}_j^{\mathsf T}A\mathbf{p}_{n-1}=(A^{\mathsf T}\tilde{\mathbf{r}}_j)^{\mathsf T}\mathbf{p}_{n-1}=0$ since $A^{\mathsf T}\tilde{\mathbf{r}}_j$ is a combination of $A^{\mathsf T}\tilde{\mathbf{p}}_j,A^{\mathsf T}\tilde{\mathbf{p}}_{j-1}$. For $j=n-1$ the choice of $\alpha_n$ gives zero, using $\tilde{\mathbf{r}}_{n-1}=\tilde{\mathbf{p}}_{n-1}-\beta_{n-1}\tilde{\mathbf{p}}_{n-2}$. The other three relations follow the same pattern.

3. The $\mathbf{r}_j$ span $\mathcal K_n(A,\mathbf{b})$ and the $\tilde{\mathbf{r}}_j$ span $\mathcal K_n(A^{\mathsf T},\tilde{\mathbf{r}}_0)$, giving the Petrov–Galerkin form. A nonzero $\mathbf{r}_m$ would be orthogonal to the $m$-dimensional $\mathcal K_m(A^{\mathsf T},\tilde{\mathbf{r}}_0)=\mathbb{R}^m$, which is impossible, unless that space has smaller dimension, which is a breakdown.

:::

::: {#rmk-biconjugate-gradient-1 .remark name="Breakdowns, irregular convergence and the transpose"}

BiCG has no minimisation property, so its residual can grow and oscillate. It can also *break down*: $\tilde{\mathbf{r}}_{n-1}^{\mathsf T}\mathbf{r}_{n-1}=0$ or $\tilde{\mathbf{p}}_{n-1}^{\mathsf T}A\mathbf{p}_{n-1}=0$ with nonzero vectors (in practice, near-breakdowns that amplify rounding errors); look-ahead variants step over them. Its derivatives address these defects. *QMR* minimises a quasi-residual built from the same two-sided Lanczos basis, giving smooth convergence. *CGS* and *BiCGSTAB* avoid products with $A^{\mathsf T}$, which are often unavailable: since $\mathbf{r}_n=p_n(A)\mathbf{b}$ and $\tilde{\mathbf{r}}_n=p_n(A^{\mathsf T})\tilde{\mathbf{r}}_0$, the coefficients only need $\tilde{\mathbf{r}}_0^{\mathsf T}p_n(A)^2\mathbf{b}$, and BiCGSTAB replaces one factor $p_n$ by a product of locally optimal degree-one factors to smooth the convergence. Each costs two products with $A$ per step, against one for GMRES, but constant work and storage.

:::

::: {#exm-bicg-compared .example name="GMRES, BiCG and BiCGSTAB on one matrix"}

For $A=2I+1.2G/\sqrt m$ with $G$ a $300\times300$ standard Gaussian matrix (eigenvalues roughly in $\lvert z-2\rvert\le1.2$) and $\mathbf{b}=(1,\dots,1)$, GMRES reduces the residual smoothly by a factor about $0.6$ per step, reaching $10^{-9}$ at $n=40$. BiCG follows a similar overall trend but irregularly: its residual first rises above $1$, then drops in jumps, reaching $10^{-8}$ at $n=40$. BiCGSTAB reaches $10^{-9}$ in $20$ steps, but each of its steps uses two products with $A$, so it costs the same number of products as GMRES with far less orthogonalisation work.

:::

::: {#fig-biconjugate-gradient-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.26cm, y=0.6cm]
\draw[->, faint] (0,0.6) -- (42,0.6) node[lab, right] {matrix–vector products};
\draw[->, faint] (0,0.6) -- (0,-10) node[lab, below] {$\log_{10}\lVert\mathbf{r}\rVert/\lVert\mathbf{b}\rVert$};
\foreach \x in {10,20,30,40} {\draw[faint] (\x,0.5) -- (\x,0.7); \node[tick, above] at (\x,0.7) {$\x$};}
\foreach \y in {-2,-4,-6,-8} {\draw[faint] (-0.3,\y) -- (0.3,\y); \node[tick, left] at (-0.3,\y) {$\y$};}
\draw[emph] plot coordinates {(0,0) (2,-0.5) (4,-0.92) (6,-1.32) (8,-1.78) (10,-2.2) (12,-2.65) (14,-3.14) (16,-3.61) (18,-4.11) (20,-4.62) (22,-5.09) (24,-5.52) (26,-5.99) (28,-6.45) (30,-6.94) (32,-7.47) (34,-7.96) (36,-8.42) (38,-8.91) (40,-9.39)};
\draw[hl] plot coordinates {(0,0) (4,-0.41) (8,0.09) (12,-0.78) (16,-1.42) (20,-1.48) (24,-1.93) (28,-2.05) (32,-3.33) (36,-3.85) (40,-4.28)};
\draw[emph, dashed] plot coordinates {(0,0) (2,-0.46) (4,-0.9) (6,-1.31) (8,-0.75) (10,-1.83) (12,-2.11) (14,-2.55) (16,-3.15) (18,-3.68) (20,-3.72) (22,-3.07) (24,-4.59) (26,-5.35) (28,-5.16) (30,-6.53) (32,-6.99) (34,-7.3) (36,-7.99) (38,-7.98) (40,-8.92)};
\node[lab] at (33,-9.4) {GMRES};
\node[lab] at (36,-3.2) {BiCG};
\node[lab] at (23,-6.6) {BiCGSTAB};
\end{tikzpicture}
\end{center}
```

Residuals in @exm-bicg-compared against the number of products with $A$ or $A^{\mathsf T}$ (two per step for BiCG and BiCGSTAB). GMRES decreases monotonically, as its optimality guarantees; BiCG and BiCGSTAB zigzag, and BiCG is slowest per product because half of its products go into the shadow sequence.

:::
