---
title: "Adjoint Methods for Sensitivity Analysis"
sources: [mit18335-26, mit18335-27]
requires: [math/optimization/algorithms/trust-region-methods, math/optimization/algorithms/structured-linear-equations]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 26 and 27 (adjoint methods; adjoint methods for eigenproblems and recurrence relations) and the notes on adjoint methods and sensitivity analysis, in our own wording; proofs written out in steps; the example was checked against finite differences in Python. -->

Gradient-based optimization of a design described by many parameters $p\in\mathbb{R}^P$ needs $dg/dp$, where the objective $g$ depends on $p$ through the solution $x$ of a large system. Differentiating the system once per parameter costs $P$ solves. The *adjoint method* gets the whole gradient with one extra solve, whatever $P$ is; reverse-mode automatic differentiation and backpropagation are the same idea.

::: {#def-adjoint-linear .definition name="Adjoint for a linear system"}

Let $x(p)\in\mathbb{R}^m$ solve $A(p)x=b(p)$ with $A$ invertible, and let $g(x,p)$ be a scalar objective. The *adjoint* (or Lagrange multiplier) vector $\lambda\in\mathbb{R}^m$ solves
$$A^{\mathsf T}\lambda=\Bigl(\frac{\partial g}{\partial x}\Bigr)^{\mathsf T}.$$

:::

::: {#thm-adjoint-gradient .theorem name="The adjoint gradient formula"}

With $\lambda$ as in @def-adjoint-linear,
$$\frac{dg}{dp_k}=\frac{\partial g}{\partial p_k}+\lambda^{\mathsf T}\Bigl(\frac{\partial b}{\partial p_k}-\frac{\partial A}{\partial p_k}x\Bigr),\qquad k=1,\dots,P .$$
Computing all $P$ components costs one solve with $A$ (for $x$), one with $A^{\mathsf T}$ (for $\lambda$), and $P$ cheap evaluations of the bracket; the direct method costs $P$ solves with $A$.

:::

::: {.proof}

1. By the chain rule, $\dfrac{dg}{dp_k}=\dfrac{\partial g}{\partial p_k}+\dfrac{\partial g}{\partial x}\dfrac{\partial x}{\partial p_k}$.

2. Differentiating $Ax=b$: $\dfrac{\partial A}{\partial p_k}x+A\dfrac{\partial x}{\partial p_k}=\dfrac{\partial b}{\partial p_k}$, so $\dfrac{\partial x}{\partial p_k}=A^{-1}\Bigl(\dfrac{\partial b}{\partial p_k}-\dfrac{\partial A}{\partial p_k}x\Bigr)$.

3. Substituting, the second term is $\dfrac{\partial g}{\partial x}A^{-1}(\cdots)$. The row vector $\dfrac{\partial g}{\partial x}A^{-1}$ does not depend on $k$; it is $\lambda^{\mathsf T}$ with $A^{\mathsf T}\lambda=(\partial g/\partial x)^{\mathsf T}$. Associating the product this way round is the whole trick.

4. *Cost.* Computing $\partial x/\partial p_k$ for every $k$ needs $P$ solves; computing $\lambda$ once needs one solve with $A^{\mathsf T}$, which can reuse the factorization of $A$.

:::

::: {#fig-adjoint-methods-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] (p) at (0,0) {$p\in\mathbb{R}^P$};
\node[box] (x) at (3.3,0) {$x\in\mathbb{R}^m$};
\node[box] (g) at (6.4,0) {$g\in\mathbb{R}$};
\draw[map] (p) -- (x) node[midway, note, above] {$A(p)x=b(p)$};
\draw[map] (x) -- (g);
\draw[map, hl] (g) to[bend left=35] node[note, below] {$A^{\mathsf T}\lambda=\partial g/\partial x$: one solve} (x);
\draw[map, hl] (x) to[bend left=35] node[note, below] {$P$ cheap products} (p);
\end{tikzpicture}
\end{center}
```

Forward, the parameters determine $x$ and then $g$. The adjoint method propagates the derivative of the single output backwards: one solve with $A^{\mathsf T}$ carries $\partial g/\partial x$ back to the level of $x$, after which each $dg/dp_k$ is an inner product.

:::

::: {#exm-adjoint-two-by-two .example name="A two-parameter example"}

Let $A(p)=\begin{bmatrix}2+p_1&1\\1&3+p_2\end{bmatrix}$, $b=(1,0)$ and $g=x_1^2+x_2$, at $p=0$. Then $x=(0.6,-0.2)$, $\partial g/\partial x=(1.2,1)$, and $A^{\mathsf T}\lambda=(1.2,1)$ gives $\lambda=(0.52,0.16)$. Since $\partial A/\partial p_1=\mathbf{e}_1\mathbf{e}_1^{\mathsf T}$ and $\partial A/\partial p_2=\mathbf{e}_2\mathbf{e}_2^{\mathsf T}$,
$$\frac{dg}{dp_1}=-\lambda_1x_1=-0.312,\qquad\frac{dg}{dp_2}=-\lambda_2x_2=0.032,$$
which agree with finite differences to seven digits.

:::

::: {#thm-adjoint-nonlinear .theorem name="Adjoints for nonlinear equations"}

Let $x(p)$ solve $f(x,p)=0$ with $f:\mathbb{R}^m\times\mathbb{R}^P\to\mathbb{R}^m$ and invertible Jacobian $f_x$. If $f_x^{\mathsf T}\lambda=(\partial g/\partial x)^{\mathsf T}$, then
$$\frac{dg}{dp}=\frac{\partial g}{\partial p}-\lambda^{\mathsf T}\frac{\partial f}{\partial p}.$$

:::

::: {.proof}

1. By the implicit function theorem, $f_x\,\partial x/\partial p+\partial f/\partial p=0$, so $\partial x/\partial p=-f_x^{-1}\,\partial f/\partial p$.

2. $\dfrac{dg}{dp}=\dfrac{\partial g}{\partial p}+\dfrac{\partial g}{\partial x}\dfrac{\partial x}{\partial p}=\dfrac{\partial g}{\partial p}-\Bigl(\dfrac{\partial g}{\partial x}f_x^{-1}\Bigr)\dfrac{\partial f}{\partial p}$, and the bracket is $\lambda^{\mathsf T}$.

3. The linear case is $f=A(p)x-b(p)$, with $f_x=A$ and $\partial f/\partial p_k=(\partial A/\partial p_k)x-\partial b/\partial p_k$.

:::

If $x$ was found by Newton's method, the factorization of $f_x$ from its last step can be reused for the adjoint solve, so the gradient costs less than one more Newton step.

::: {#prp-eigenvalue-sensitivity .proposition name="Derivative of a simple eigenvalue (Hellmann–Feynman)"}

Let $A(p)$ be real symmetric with a simple eigenvalue $\mu(p)$ and unit eigenvector $v(p)$. Then
$$\frac{d\mu}{dp_k}=v^{\mathsf T}\frac{\partial A}{\partial p_k}v .$$
For a non-symmetric $A$ with right eigenvector $v$ and left eigenvector $u$ ($u^{\mathsf T}A=\mu u^{\mathsf T}$), $d\mu/dp_k=u^{\mathsf T}(\partial A/\partial p_k)v/(u^{\mathsf T}v)$: the left eigenvector plays the role of the adjoint.

:::

::: {.proof}

1. Differentiate $Av=\mu v$: $A_kv+Av_k=\mu_kv+\mu v_k$, with subscripts denoting $\partial/\partial p_k$.

2. Multiply on the left by $u^{\mathsf T}$: $u^{\mathsf T}A_kv+u^{\mathsf T}Av_k=\mu_ku^{\mathsf T}v+\mu u^{\mathsf T}v_k$. Since $u^{\mathsf T}A=\mu u^{\mathsf T}$, the terms with $v_k$ cancel.

3. So $\mu_k=u^{\mathsf T}A_kv/(u^{\mathsf T}v)$; $u^{\mathsf T}v\ne0$ for a simple eigenvalue. In the symmetric case $u=v$ and $v^{\mathsf T}v=1$.

:::

::: {#prp-adjoint-recurrence .proposition name="Adjoints for recurrences (backpropagation)"}

Let $x_n=F_n(x_{n-1},p)$ for $n=1,\dots,N$ with $x_0$ fixed, and $g=g(x_N)$. Define $\lambda_N=(\partial g/\partial x_N)^{\mathsf T}$ and, backwards, $\lambda_{n-1}=\bigl(\partial F_n/\partial x_{n-1}\bigr)^{\mathsf T}\lambda_n$. Then
$$\frac{dg}{dp}=\sum_{n=1}^N\lambda_n^{\mathsf T}\frac{\partial F_n}{\partial p}.$$
The backward sweep costs about as much as the forward one, independently of the number of parameters, but needs the forward states $x_n$ (stored or recomputed).

:::

::: {.proof}

1. Let $J_n=\partial F_n/\partial x_{n-1}$ and $G_n=\partial F_n/\partial p$. Differentiating the recurrence, $\dfrac{dx_n}{dp}=J_n\dfrac{dx_{n-1}}{dp}+G_n$ with $dx_0/dp=0$.

2. Unrolling, $\dfrac{dx_N}{dp}=\sum_{n=1}^NJ_NJ_{N-1}\cdots J_{n+1}G_n$.

3. Multiply on the left by $\partial g/\partial x_N=\lambda_N^{\mathsf T}$; by the definition of the $\lambda$'s, $\lambda_N^{\mathsf T}J_N\cdots J_{n+1}=\lambda_n^{\mathsf T}$. This gives the sum.

4. Evaluating the products from the left (vector–matrix products) rather than from the right (matrix–matrix products with $P$ columns) is again the saving.

:::

::: {#fig-adjoint-methods-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.9cm]
\foreach \i/\l in {0/x_0,1/x_1,2/x_2,3/x_3} {\node[box] (x\i) at (\i,0) {$\l$};}
\node[box] (g) at (4,0) {$g$};
\foreach \i/\j in {0/1,1/2,2/3} {\draw[map] (x\i) -- (x\j) node[midway, note, above] {$F$};}
\draw[map] (x3) -- (g);
\foreach \i in {1,2,3} {\node[hl box] (l\i) at (\i,-1.4) {$\lambda_{\i}$};}
\draw[map, hl] (g) |- (l3);
\draw[map, hl] (l3) -- (l2) node[midway, note, below] {$J_3^{\mathsf T}$};
\draw[map, hl] (l2) -- (l1) node[midway, note, below] {$J_2^{\mathsf T}$};
\node[note] at (2,0.75) {forward sweep: states};
\node[note] at (2,-2.2) {backward sweep: adjoints, $\tfrac{dg}{dp}=\sum_n\lambda_n^{\mathsf T}G_n$};
\end{tikzpicture}
\end{center}
```

Adjoints for a recurrence: the forward sweep computes and stores the states; the backward sweep carries $\lambda$ from the output to the input with transposed Jacobians. In a neural network the states are layer activations and this is backpropagation.

:::
