---
title: "Matrix Derivatives"
sources: [cs229-1]
requires: [math/linear-algebra/determinants/determinant-formulas]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 1 (matrix derivatives, normal equations) and Chapter 4 (gradient of the log determinant, used for Gaussian maximum likelihood), in our own wording; proofs written out in steps. -->

Many learning objectives are scalar functions of a vector or a matrix of parameters. Arranging the partial derivatives in the shape of the argument gives compact rules that turn "set the gradient to zero" into a matrix equation.

::: {#def-matrix-gradient .definition name="Gradient with respect to a matrix"}

For $f:\mathbb{R}^{m\times n}\to\mathbb{R}$, the *gradient* of $f$ at $A$ is the $m\times n$ matrix of partial derivatives

$$
\nabla_A f(A)=\begin{bmatrix}\dfrac{\partial f}{\partial A_{11}}&\cdots&\dfrac{\partial f}{\partial A_{1n}}\\ \vdots&\ddots&\vdots\\ \dfrac{\partial f}{\partial A_{m1}}&\cdots&\dfrac{\partial f}{\partial A_{mn}}\end{bmatrix},\qquad \bigl(\nabla_A f(A)\bigr)_{ij}=\frac{\partial f}{\partial A_{ij}}.
$$

For $n=1$ this is the usual gradient of a function of a vector. If $f$ is differentiable, then for a small change $\Delta$,

$$
f(A+\Delta)=f(A)+\operatorname{tr}\bigl(\nabla_A f(A)^{\mathsf T}\Delta\bigr)+o(\lVert\Delta\rVert),
$$

since $\operatorname{tr}(G^{\mathsf T}\Delta)=\sum_{i,j}G_{ij}\Delta_{ij}$.

:::

::: {#exm-matrix-gradient-1 .example name="A two by two case"}

Let $f(A)=\tfrac32A_{11}+5A_{12}^2+A_{21}A_{22}$ on $\mathbb{R}^{2\times2}$. Then

$$
\nabla_A f(A)=\begin{bmatrix}\tfrac32&10A_{12}\\ A_{22}&A_{21}\end{bmatrix}.
$$

:::

::: {#fig-matrix-derivatives-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0.0) rectangle (1.1,0.8); \node[lab] at (0.55,0.4) {$A_{11}$};
\draw[hl cell] (1.1,0.0) rectangle (2.2,0.8); \node[lab] at (1.65,0.4) {$A_{12}$};
\draw[cell frame] (0.0,-0.8) rectangle (1.1,0.0); \node[lab] at (0.55,-0.4) {$A_{21}$};
\draw[cell frame] (1.1,-0.8) rectangle (2.2,0.0); \node[lab] at (1.65,-0.4) {$A_{22}$};
\draw[cell frame] (3.6,0.0) rectangle (4.7,0.8); \node[lab] at (4.15,0.4) {$\frac32$};
\draw[hl cell] (4.7,0.0) rectangle (5.80,0.8); \node[lab] at (5.25,0.4) {$10A_{12}$};
\draw[cell frame] (3.6,-0.8) rectangle (4.7,0.0); \node[lab] at (4.15,-0.4) {$A_{22}$};
\draw[cell frame] (4.7,-0.8) rectangle (5.80,0.0); \node[lab] at (5.25,-0.4) {$A_{21}$};
\node[lab, above] at (1.1,0.85) {$A$}; \node[lab, above] at (4.7,0.85) {$\nabla_Af(A)$};
\draw[map] (2.3,0) -- node[lab, above] {$\partial f/\partial A_{ij}$} (3.5,0);
\end{tikzpicture}
\end{center}
```

The gradient with respect to a matrix has the shape of the matrix: entry $(i,j)$ is $\partial f/\partial A_{ij}$. Here the highlighted entry $A_{12}$ enters $f$ as $5A_{12}^2$, giving $10A_{12}$.

:::

::: {#prp-matrix-gradient-rules .proposition name="Gradients of traces, quadratic forms and log determinants"}

1. For $A\in\mathbb{R}^{m\times n}$ and a fixed $B\in\mathbb{R}^{n\times m}$,

   $$
   \nabla_A\operatorname{tr}(AB)=B^{\mathsf T}.
   $$

2. For $\mathbf{x}\in\mathbb{R}^n$ and a fixed $\mathbf{b}\in\mathbb{R}^n$ and $B\in\mathbb{R}^{n\times n}$,

   $$
   \nabla_{\mathbf{x}}\,\mathbf{b}^{\mathsf T}\mathbf{x}=\mathbf{b},\qquad \nabla_{\mathbf{x}}\,\mathbf{x}^{\mathsf T}B\mathbf{x}=(B+B^{\mathsf T})\mathbf{x},
   $$

   which is $2B\mathbf{x}$ when $B$ is symmetric.

3. On the open set of $A\in\mathbb{R}^{n\times n}$ with $\det A>0$,

   $$
   \nabla_A\log\det A=(A^{-1})^{\mathsf T}.
   $$

:::

::: {.proof}

1. $\operatorname{tr}(AB)=\sum_{k=1}^m\sum_{l=1}^nA_{kl}B_{lk}$, so $\partial/\partial A_{ij}$ of it is $B_{ji}=(B^{\mathsf T})_{ij}$.

2. $\mathbf{b}^{\mathsf T}\mathbf{x}=\sum_kb_kx_k$ has $\partial/\partial x_i$ equal to $b_i$. For the quadratic form, $\mathbf{x}^{\mathsf T}B\mathbf{x}=\sum_{k,l}x_kB_{kl}x_l$; differentiating in $x_i$ picks the terms with $k=i$ and those with $l=i$, giving $\sum_lB_{il}x_l+\sum_kx_kB_{ki}=(B\mathbf{x})_i+(B^{\mathsf T}\mathbf{x})_i$.

3. Fix $i,j$ and expand $\det A$ along row $i$ by cofactors: $\det A=\sum_kA_{ik}C_{ik}$, where the cofactors $C_{ik}$ do not involve row $i$ of $A$. So $\partial\det A/\partial A_{ij}=C_{ij}$.

4. The inverse is $A^{-1}=C^{\mathsf T}/\det A$, where $C$ is the matrix of cofactors, so $C_{ij}=\det A\,(A^{-1})_{ji}$.

5. By the chain rule, $\partial\log\det A/\partial A_{ij}=C_{ij}/\det A=(A^{-1})_{ji}$, which is the $(i,j)$ entry of $(A^{-1})^{\mathsf T}$.

:::

::: {#exm-matrix-derivatives-normal-equations .example name="The normal equations by differentiation"}

Stack $N$ training inputs as the rows of $X\in\mathbb{R}^{N\times d}$ and their targets in $\mathbf{y}\in\mathbb{R}^N$, and let

$$
J(\boldsymbol\theta)=\tfrac12\lVert X\boldsymbol\theta-\mathbf{y}\rVert^2=\tfrac12\bigl(\boldsymbol\theta^{\mathsf T}X^{\mathsf T}X\boldsymbol\theta-2\,(X^{\mathsf T}\mathbf{y})^{\mathsf T}\boldsymbol\theta+\mathbf{y}^{\mathsf T}\mathbf{y}\bigr).
$$

By part 2 of @prp-matrix-gradient-rules with the symmetric matrix $X^{\mathsf T}X$,

$$
\nabla_{\boldsymbol\theta}J=X^{\mathsf T}X\boldsymbol\theta-X^{\mathsf T}\mathbf{y}.
$$

Setting it to zero gives the normal equations $X^{\mathsf T}X\boldsymbol\theta=X^{\mathsf T}\mathbf{y}$ of @thm-least-squares-normal-equations, and when $X^{\mathsf T}X$ is invertible the minimizer is $\boldsymbol\theta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}\mathbf{y}$. For instance, the points $(0,1),(1,2),(2,4)$ with a column of ones for the intercept give $X^{\mathsf T}X=\begin{bmatrix}3&3\\3&5\end{bmatrix}$, $X^{\mathsf T}\mathbf{y}=\begin{bmatrix}7\\10\end{bmatrix}$ and $\boldsymbol\theta=\bigl(\tfrac56,\tfrac32\bigr)$: the line $y=\tfrac56+\tfrac32x$.

:::

::: {#rmk-matrix-derivatives-1 .remark name="The trace trick"}

A scalar equals its own trace, and $\operatorname{tr}(ABC)=\operatorname{tr}(CAB)=\operatorname{tr}(BCA)$. So a quadratic expression such as $\mathbf{x}^{\mathsf T}\Sigma^{-1}\mathbf{x}$ can be rewritten as $\operatorname{tr}(\Sigma^{-1}\mathbf{x}\mathbf{x}^{\mathsf T})$, which is linear in $\Sigma^{-1}$; part 1 of @prp-matrix-gradient-rules then differentiates it. Together with part 3 this is how the maximum likelihood estimate of a Gaussian covariance is found (@thm-gda-mle).

:::
