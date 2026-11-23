---
title: "The Conjugate Gradient Method"
sources: [mit18335-21]
requires: [math/numerical/krylov-methods/lanczos-and-restarting]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 21 (the conjugate-gradient method), in our own wording; proofs written out in steps. -->

For a symmetric positive definite matrix the Krylov idea gives a method with short recurrences, constant storage and an optimality property: conjugate gradients (CG). It minimises the error in the energy norm over the Krylov space, which also makes it a minimisation method for the quadratic $\tfrac12\mathbf{x}^{\mathsf T}A\mathbf{x}-\mathbf{b}^{\mathsf T}\mathbf{x}$. Throughout, $A$ is real symmetric positive definite and $\mathbf{x}_*=A^{-1}\mathbf{b}$.

::: {#def-a-norm .definition name="Energy norm"}

The *$A$-norm* (energy norm) is $\lVert\mathbf{v}\rVert_A=\sqrt{\mathbf{v}^{\mathsf T}A\mathbf{v}}$, the norm of the inner product $\langle\mathbf{u},\mathbf{v}\rangle_A=\mathbf{u}^{\mathsf T}A\mathbf{v}$. Vectors with $\mathbf{u}^{\mathsf T}A\mathbf{v}=0$ are called *$A$-conjugate*. For $\varphi(\mathbf{x})=\tfrac12\mathbf{x}^{\mathsf T}A\mathbf{x}-\mathbf{b}^{\mathsf T}\mathbf{x}$ one has $\varphi(\mathbf{x})=\tfrac12\lVert\mathbf{x}-\mathbf{x}_*\rVert_A^2-\tfrac12\mathbf{x}_*^{\mathsf T}A\mathbf{x}_*$, so minimising $\varphi$ and minimising the $A$-norm of the error are the same.

:::

::: {#def-conjugate-gradient .definition name="Conjugate gradient iteration"}

Set $\mathbf{x}_0=\mathbf{0}$, $\mathbf{r}_0=\mathbf{b}$, $\mathbf{p}_0=\mathbf{r}_0$. For $n=1,2,\dots$:
$$\alpha_n=\frac{\mathbf{r}_{n-1}^{\mathsf T}\mathbf{r}_{n-1}}{\mathbf{p}_{n-1}^{\mathsf T}A\mathbf{p}_{n-1}},\quad\mathbf{x}_n=\mathbf{x}_{n-1}+\alpha_n\mathbf{p}_{n-1},\quad\mathbf{r}_n=\mathbf{r}_{n-1}-\alpha_nA\mathbf{p}_{n-1},$$
$$\beta_n=\frac{\mathbf{r}_n^{\mathsf T}\mathbf{r}_n}{\mathbf{r}_{n-1}^{\mathsf T}\mathbf{r}_{n-1}},\quad\mathbf{p}_n=\mathbf{r}_n+\beta_n\mathbf{p}_{n-1}.$$
Each step costs one product $A\mathbf{p}$, two inner products and three vector updates; four vectors are stored.

:::

```{=latex}
\begin{algorithm}
\caption{Conjugate gradients}
\begin{algorithmic}
\INPUT symmetric positive definite $A$ (as a routine), $\mathbf{b}$
\STATE $\mathbf{x}\gets\mathbf{0}$, $\mathbf{r}\gets\mathbf{b}$, $\mathbf{p}\gets\mathbf{r}$, $\rho\gets\mathbf{r}^{\mathsf T}\mathbf{r}$
\WHILE{$\sqrt\rho>\text{tol}\cdot\lVert\mathbf{b}\rVert$}
    \STATE $\mathbf{w}\gets A\mathbf{p}$; \quad $\alpha\gets\rho/(\mathbf{p}^{\mathsf T}\mathbf{w})$
    \STATE $\mathbf{x}\gets\mathbf{x}+\alpha\mathbf{p}$; \quad $\mathbf{r}\gets\mathbf{r}-\alpha\mathbf{w}$
    \STATE $\rho_{\text{new}}\gets\mathbf{r}^{\mathsf T}\mathbf{r}$; \quad $\mathbf{p}\gets\mathbf{r}+(\rho_{\text{new}}/\rho)\mathbf{p}$; \quad $\rho\gets\rho_{\text{new}}$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#thm-cg-properties .theorem name="Orthogonality and optimality of CG"}

As long as $\mathbf{r}_{n-1}\ne\mathbf{0}$:

1. $\mathcal K_n=\operatorname{span}\{\mathbf{x}_1,\dots,\mathbf{x}_n\}=\operatorname{span}\{\mathbf{p}_0,\dots,\mathbf{p}_{n-1}\}=\operatorname{span}\{\mathbf{r}_0,\dots,\mathbf{r}_{n-1}\}$;

2. the residuals are orthogonal, $\mathbf{r}_n^{\mathsf T}\mathbf{r}_j=0$ for $j<n$;

3. the search directions are $A$-conjugate, $\mathbf{p}_n^{\mathsf T}A\mathbf{p}_j=0$ for $j<n$;

4. $\mathbf{x}_n$ is the unique minimiser of $\lVert\mathbf{x}-\mathbf{x}_*\rVert_A$ over $\mathbf{x}\in\mathcal K_n$, and the errors $\lVert\mathbf{e}_n\rVert_A$, $\mathbf{e}_n=\mathbf{x}_*-\mathbf{x}_n$, decrease strictly until $\mathbf{e}_n=\mathbf{0}$, which happens after at most $m$ steps.

:::

::: {.proof}

1. *Spans,* by induction: $\mathbf{x}_n$ adds a multiple of $\mathbf{p}_{n-1}$, $\mathbf{r}_n$ adds a multiple of $A\mathbf{p}_{n-1}\in\mathcal K_{n+1}$, and $\mathbf{p}_n$ combines $\mathbf{r}_n$ and $\mathbf{p}_{n-1}$. So each span is contained in $\mathcal K_n$; that they equal it follows once (2) shows the residuals are nonzero and orthogonal, hence independent.

2. *Residuals orthogonal,* by induction on $n$ (with (3) assumed for smaller indices). From $\mathbf{r}_n=\mathbf{r}_{n-1}-\alpha_nA\mathbf{p}_{n-1}$: for $j<n-1$, $\mathbf{r}_{n-1}^{\mathsf T}\mathbf{r}_j=0$, and $\mathbf{p}_{n-1}^{\mathsf T}A\mathbf{r}_j=0$ because $\mathbf{r}_j$ is a combination of $\mathbf{p}_j,\mathbf{p}_{j-1}$, both $A$-conjugate to $\mathbf{p}_{n-1}$. For $j=n-1$, write $\mathbf{r}_{n-1}=\mathbf{p}_{n-1}-\beta_{n-1}\mathbf{p}_{n-2}$; then $\mathbf{r}_{n-1}^{\mathsf T}A\mathbf{p}_{n-1}=\mathbf{p}_{n-1}^{\mathsf T}A\mathbf{p}_{n-1}$, and the choice of $\alpha_n$ makes $\mathbf{r}_n^{\mathsf T}\mathbf{r}_{n-1}=0$.

3. *Directions conjugate.* $\mathbf{p}_n^{\mathsf T}A\mathbf{p}_j=\mathbf{r}_n^{\mathsf T}A\mathbf{p}_j+\beta_n\mathbf{p}_{n-1}^{\mathsf T}A\mathbf{p}_j$. For $j<n-1$ both terms vanish: $A\mathbf{p}_j=(\mathbf{r}_j-\mathbf{r}_{j+1})/\alpha_{j+1}$ is orthogonal to $\mathbf{r}_n$ by (2), and the second by induction. For $j=n-1$, $\mathbf{r}_n^{\mathsf T}A\mathbf{p}_{n-1}=-\mathbf{r}_n^{\mathsf T}\mathbf{r}_n/\alpha_n$ and $\mathbf{p}_{n-1}^{\mathsf T}A\mathbf{p}_{n-1}=\mathbf{r}_{n-1}^{\mathsf T}\mathbf{r}_{n-1}/\alpha_n$, so the choice of $\beta_n$ makes the sum zero.

4. *Optimality.* $\mathbf{r}_n=A\mathbf{e}_n$, so (2) says $\mathbf{e}_n^{\mathsf T}A\mathbf{v}=0$ for all $\mathbf{v}\in\mathcal K_n$: the error is $A$-orthogonal to $\mathcal K_n$. For any other $\mathbf{x}=\mathbf{x}_n-\mathbf{v}$ with $\mathbf{v}\in\mathcal K_n$, $\lVert\mathbf{x}_*-\mathbf{x}\rVert_A^2=\lVert\mathbf{e}_n\rVert_A^2+\lVert\mathbf{v}\rVert_A^2\ge\lVert\mathbf{e}_n\rVert_A^2$, with equality only for $\mathbf{v}=\mathbf{0}$.

5. The spaces $\mathcal K_n$ are nested, so $\lVert\mathbf{e}_n\rVert_A$ is nonincreasing; it decreases strictly while $\mathbf{r}_n\ne\mathbf{0}$ because $\mathcal K_{n+1}$ then contains the new direction $\mathbf{p}_n$ with $\mathbf{p}_n^{\mathsf T}\mathbf{r}_n=\mathbf{r}_n^{\mathsf T}\mathbf{r}_n>0$. As $\dim\mathcal K_n\le m$, after at most $m$ steps $\mathcal K_n=\mathcal K_{n+1}$ and $\mathbf{e}_n=\mathbf{0}$.

:::

::: {#fig-conjugate-gradient-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.85]
\foreach \s in {0.5,1,1.5,2,2.5} {\draw[faint, rotate=30] (0,0) ellipse ({1.6*\s} and {0.6*\s});}
\fill (0,0) circle (1.6pt) node[lab, below right] {$\mathbf{x}_*$};
\coordinate (a) at (-3.4,1.2);
\coordinate (b) at (-1.72,-1.03);
\draw[emph, ->] (a) -- (b);
\draw[hl, ->] (b) -- (0,0);
\fill (a) circle (1.6pt) node[lab, above left] {$\mathbf{x}_0$};
\fill (b) circle (1.6pt) node[lab, below left] {$\mathbf{x}_1$};
\draw[faint, dashed, ->] (b) -- (-0.76,-0.31);
\node[note] at (1.0,-2.2) {dashed: next steepest-descent direction};
\end{tikzpicture}
\end{center}
```

CG on a $2\times2$ problem, drawn over the level curves of $\varphi$ (ellipses). The first step goes along the residual to the minimum on that line; the second direction is $A$-conjugate to the first, not orthogonal, and reaches $\mathbf{x}_*$ exactly. Steepest descent would instead turn by a right angle (dashed) and zigzag.

:::

::: {#rmk-conjugate-gradient-1 .remark name="CG is Lanczos"}

CG and the Lanczos iteration (@def-lanczos-iteration) on $(A,\mathbf{b})$ generate the same Krylov spaces, and the residuals are multiples of the Lanczos vectors: $\mathbf{r}_n=\pm\lVert\mathbf{r}_n\rVert\mathbf{q}_{n+1}$. The CG coefficients $\alpha_n,\beta_n$ determine the tridiagonal $T_n$, and CG amounts to solving $T_n\mathbf{y}=\lVert\mathbf{b}\rVert\mathbf{e}_1$ by an $LDL^{\mathsf T}$ factorization updated one step at a time. In floating point CG inherits Lanczos' loss of orthogonality (@sec-math-numerical-krylov-methods-lanczos-and-restarting); the effect is a delay in convergence, not a wrong answer, so finite termination is not observed in practice and CG is used as an iterative method.

:::
