---
title: "Newton's Method for Systems and Implicit Differentiation"
sources: [mit18s096-6]
requires: [math/calculus/matrix/computing-derivatives/finite-difference-checks, math/calculus/single-variable/applications-of-derivatives/newtons-method]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 6 (Newton's method for scalar and multidimensional functions, nonlinear and engineering optimization, reverse-mode adjoint differentiation of linear and nonlinear equations) and the Newton slides of Lecture 4, in our own wording; the matrix square-root example is ours, run in Python; proofs written out in steps. The adjoint part of the chapter is @def-adjoint-linear, @thm-adjoint-gradient and @thm-adjoint-nonlinear (from MIT 18.335), not repeated here. -->

Linearization is not only for analysing functions: it is the basic step of the most important algorithm for solving nonlinear equations. Newton's method replaces $f(x)=0$ by its linearization, solves that linear equation, and repeats. With derivatives written as linear operators, the same method solves equations whose unknowns are matrices.

::: {#def-newton-systems .definition name="Newton's method for systems" related="def-newtons-method"}

Let $f:V\to V$ be differentiable, $V$ a finite-dimensional space. Starting from a guess $x_0$, *Newton's method* sets

$$
x_{k+1}=x_k+\delta x_k,\qquad\text{where}\quad f'(x_k)[\delta x_k]=-f(x_k).
$$

For $V=\mathbb{R}^n$ each step solves the linear system $J(x_k)\,\delta x_k=-f(x_k)$ with the Jacobian matrix $J$; one never forms $J^{-1}$.

:::

```{=latex}
\begin{algorithm}
\caption{Newton's method for a system $f(x)=0$}
\begin{algorithmic}
\INPUT $f$, its derivative $f'$, starting guess $x$, tolerance $\epsilon>0$
\WHILE{$\lVert f(x)\rVert>\epsilon$}
  \STATE solve the linear equation $f'(x)[\delta x]=-f(x)$ for $\delta x$
  \STATE $x\gets x+\delta x$
\ENDWHILE
\RETURN $x$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-newtons-method-for-systems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm, y=0.8cm]
\draw[->] (0,0) -- (4.3,0) node[lab, right] {$x$};
\draw[->] (0,-1) -- (0,4.6) node[lab, above] {$f(x)$};
\draw[domain=1.1:4, samples=40] plot (\x, {0.35*\x*\x-1});
\draw[hl] (4,4.6) -- (2.357,0);
\draw[hl] (2.357,0.944) -- (1.8,0);
\draw[faint, dashed] (4,0) -- (4,4.6); \draw[faint, dashed] (2.357,0) -- (2.357,0.944);
\fill (4,4.6) circle (1.5pt); \fill (2.357,0.944) circle (1.5pt);
\node[lab, below] at (4,0) {$x_0$}; \node[lab, below] at (2.357,0) {$x_1$}; \node[lab, below] at (1.8,0) {$x_2$};
\fill[hl] (1.69,0) circle (1.5pt);
\end{tikzpicture}
\end{center}
```

Each Newton step follows the tangent, the linearization of $f$ at $x_k$, to its zero. Near a root the linearization is very accurate, so the steps home in quickly.

:::

::: {#thm-newton-systems-quadratic .theorem name="Local quadratic convergence"}

Let $f:\mathbb{R}^n\to\mathbb{R}^n$ have $f(x^*)=0$, with $J(x^*)$ invertible and $J$ Lipschitz near $x^*$: $\lVert J(x)-J(y)\rVert\le L\lVert x-y\rVert$. Then there are $r>0$ and $C$ such that for $\lVert x_0-x^*\rVert<r$ Newton's method converges to $x^*$ and

$$
\lVert x_{k+1}-x^*\rVert\le C\,\lVert x_k-x^*\rVert^2 .
$$

:::

::: {.proof}

1. Write $e_k=x_k-x^*$. Since $f(x^*)=0$, $f(x_k)=\int_0^1J(x^*+te_k)\,e_k\,dt$, so $f(x_k)-J(x_k)e_k=\int_0^1\bigl(J(x^*+te_k)-J(x_k)\bigr)e_k\,dt$.

2. The Lipschitz bound gives $\lVert J(x^*+te_k)-J(x_k)\rVert\le L(1-t)\lVert e_k\rVert$, so $\lVert f(x_k)-J(x_k)e_k\rVert\le\tfrac L2\lVert e_k\rVert^2$.

3. From the Newton step, $e_{k+1}=e_k-J(x_k)^{-1}f(x_k)=-J(x_k)^{-1}\bigl(f(x_k)-J(x_k)e_k\bigr)$.

4. $J$ is invertible at $x^*$ and continuous, so on a small ball $\lVert J(x)^{-1}\rVert\le M$. Hence $\lVert e_{k+1}\rVert\le\tfrac{ML}2\lVert e_k\rVert^2$, which is the bound with $C=ML/2$.

5. If moreover $r\le1/(2C)$, then $\lVert e_{k+1}\rVert\le\tfrac12\lVert e_k\rVert$, so every iterate stays in the ball and $e_k\to0$.

:::

::: {#exm-newton-matrix-square-root .example name="A matrix square root by Newton's method"}

Solve $f(X)=X^2-A=0$ for $A=\begin{bmatrix}5&4\\4&5\end{bmatrix}$. By @exm-differential-quadratic-form, $f'(X)[\delta X]=X\,\delta X+\delta X\,X$, so each step solves the linear matrix equation

$$
X_k\,\delta X+\delta X\,X_k=A-X_k^2,
$$

which, by @exm-matrix-square-jacobian, is the $4\times4$ system $(I\otimes X_k+X_k^{\mathsf T}\otimes I)\operatorname{vec}\delta X=\operatorname{vec}(A-X_k^2)$. From $X_0=I$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| $(X_k)_{12}$ | $0$ | $2$ | $1.2$ | $1.0118$ | $1.000046$ | $1.0000000$ |
| $\lVert A-X_k^2\rVert_F$ | $8$ | $16$ | $2.56$ | $0.142$ | $5.5\cdot10^{-4}$ | $8.4\cdot10^{-9}$ |

The iterates approach $\begin{bmatrix}2&1\\1&2\end{bmatrix}$, and once close the residual is roughly squared at each step.

:::

::: {#prp-implicit-differentiation .proposition name="Differentiating the solution of an equation" related="thm-adjoint-nonlinear"}

Let $x(p)$ solve $f(x,p)=0$, where $f$ is differentiable and its partial derivative $f_x=\partial f/\partial x$ is invertible at the solution. Then

$$
dx=-f_x^{-1}f_p\,dp .
$$

:::

::: {.proof}

1. Differentiate the identity $f(x(p),p)=0$: $f_x\,dx+f_p\,dp=0$.

2. Solve for $dx$ using the invertibility of $f_x$. (That $x(p)$ exists and is differentiable is the implicit function theorem.)

:::

::: {#rmk-newtons-method-for-systems-1 .remark name="Newton, optimization and adjoints"}

1. *Optimization.* Minimizing a smooth $g$ means solving $\nabla g(x)=0$; Newton's method for this system uses the Jacobian of $\nabla g$, the Hessian (@def-hessian-matrix), and is @sec-math-optimization-algorithms-newtons-method-for-minimization.

2. *Large parameter counts.* When an objective $g(x(p))$ depends on many parameters $p$ through the solution of $f(x,p)=0$, applying @prp-implicit-differentiation once per parameter is expensive. Grouping $\tfrac{\partial g}{\partial x}f_x^{-1}$ first needs one solve with $f_x^{\mathsf T}$, the adjoint method (@sec-math-optimization-algorithms-adjoint-methods): the reverse order of @prp-chain-rule-cost.

3. *Reusing Newton.* The matrix $f_x$ is exactly the Newton matrix at the converged solution, so its factorization can be reused for the adjoint solve.

:::

::: {#fig-newtons-method-for-systems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=0.38cm]
\draw[->] (0,-9) -- (5.6,-9) node[lab, right] {$k$};
\draw[->] (0,-9) -- (0,2) node[lab, above] {$\log_{10}\lVert A-X_k^2\rVert_F$};
\foreach \k in {0,...,5}{\draw (\k,-9) -- (\k,-9.3) node[lab, below] {$\k$};}
\foreach \e in {-8,-4,0}{\draw (0,\e) -- (-0.12,\e) node[lab, left] {$\e$};}
\draw[hl] plot coordinates {(0,0.90) (1,1.20) (2,0.41) (3,-0.85) (4,-3.26) (5,-8.08)};
\foreach \p in {(0,0.90),(1,1.20),(2,0.41),(3,-0.85),(4,-3.26),(5,-8.08)}{\fill[hl] \p circle (2.5pt);}
\end{tikzpicture}
\end{center}
```

Residuals of @exm-newton-matrix-square-root on a log scale. The first step overshoots; afterwards the number of correct digits roughly doubles at each step, the signature of quadratic convergence.

:::
