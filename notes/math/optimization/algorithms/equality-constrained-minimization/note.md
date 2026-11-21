---
title: "Equality Constrained Minimization"
sources: [ee364a-11]
requires: [math/optimization/algorithms/newtons-method-for-minimization, math/optimization/duality/kkt-conditions, math/optimization/algorithms/structured-linear-equations]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on equality constrained minimization, in our own wording; proofs written out in steps. -->

Minimizing a convex function subject to linear equations reduces to solving the KKT system. Newton's method extends by taking steps that keep the equations satisfied, or that move towards satisfying them from an infeasible start.

::: {#def-equality-constrained-problem .definition name="Equality constrained minimization"}

The problem is
$$\text{minimize }f(x)\quad\text{subject to }Ax=b,$$
with $f$ convex and twice differentiable and $A\in\mathbb{R}^{p\times n}$ of rank $p$. By @thm-kkt, $x^\star$ is optimal iff there is $\nu^\star$ with
$$Ax^\star=b,\qquad\nabla f(x^\star)+A^{\mathsf T}\nu^\star=0.$$

:::

::: {#exm-equality-constrained-qp .example name="Equality constrained quadratic minimization"}

For $f(x)=\frac12x^{\mathsf T}Px+q^{\mathsf T}x+r$ with $P\succeq0$, the optimality conditions are the linear KKT system
$$\begin{bmatrix}P&A^{\mathsf T}\\A&0\end{bmatrix}\begin{bmatrix}x^\star\\\nu^\star\end{bmatrix}=\begin{bmatrix}-q\\b\end{bmatrix}.$$
The KKT matrix is nonsingular iff $Ax=0$, $x\ne0$ imply $x^{\mathsf T}Px>0$.

:::

::: {.proof}

1. If the matrix is singular, take $(x,\nu)\ne0$ in its null space: $Px+A^{\mathsf T}\nu=0$, $Ax=0$. Then $x^{\mathsf T}Px=-x^{\mathsf T}A^{\mathsf T}\nu=0$. If $x=0$ then $A^{\mathsf T}\nu=0$, so $\nu=0$ by full rank, impossible; so $x\ne0$ is in $\operatorname{null}A$ with $x^{\mathsf T}Px=0$.

2. Conversely, if $x\ne0$, $Ax=0$ and $x^{\mathsf T}Px=0$, then $P^{1/2}x=0$, so $Px=0$ and $(x,0)$ is in the null space.

:::

::: {#def-newton-step-equality .definition name="Newton step with equality constraints"}

At a feasible $x$, the Newton step $\Delta x_{\rm nt}$ minimizes the second-order model subject to $A(x+v)=b$; it solves
$$\begin{bmatrix}\nabla^2f(x)&A^{\mathsf T}\\A&0\end{bmatrix}\begin{bmatrix}\Delta x_{\rm nt}\\w\end{bmatrix}=\begin{bmatrix}-\nabla f(x)\\0\end{bmatrix}.$$
The Newton decrement is $\lambda(x)=(\Delta x_{\rm nt}^{\mathsf T}\nabla^2f(x)\Delta x_{\rm nt})^{1/2}$. Newton's method with equality constraints is @def-damped-newton with this step, started at a feasible point; every iterate stays feasible since $A\Delta x_{\rm nt}=0$.

:::

::: {#prp-newton-elimination .proposition name="Newton's method and elimination"}

Let $\{x\mid Ax=b\}=\{Fz+\hat x\}$ with $F$ of full column rank. Newton's method for $f$ with equality constraints, started at $x^{(0)}=Fz^{(0)}+\hat x$, produces $x^{(k)}=Fz^{(k)}+\hat x$, where $z^{(k)}$ are the Newton iterates for the unconstrained $\tilde f(z)=f(Fz+\hat x)$.

:::

::: {.proof}

1. The Newton step of $\tilde f$ is $\Delta z=-(F^{\mathsf T}\nabla^2fF)^{-1}F^{\mathsf T}\nabla f$.

2. Put $v=F\Delta z$. Then $Av=0$ (as $AF=0$), and $F^{\mathsf T}(\nabla^2fv+\nabla f)=0$, so $\nabla^2fv+\nabla f\in\operatorname{null}F^{\mathsf T}=\operatorname{range}A^{\mathsf T}$: there is $w$ with $\nabla^2fv+A^{\mathsf T}w=-\nabla f$.

3. So $(v,w)$ solves the KKT system of @def-newton-step-equality, and $v=\Delta x_{\rm nt}$. The decrements and line searches agree, as $\tilde f(z+t\Delta z)=f(x+tv)$.

:::

::: {#def-infeasible-start-newton .definition name="Infeasible start Newton method"}

From any $x\in\operatorname{dom}f$ and any $\nu$, linearize the optimality conditions: find $(\Delta x,\Delta\nu)$ with
$$\begin{bmatrix}\nabla^2f(x)&A^{\mathsf T}\\A&0\end{bmatrix}\begin{bmatrix}\Delta x\\\Delta\nu\end{bmatrix}=-\begin{bmatrix}\nabla f(x)+A^{\mathsf T}\nu\\Ax-b\end{bmatrix}=-r(x,\nu).$$
Choose $t$ by backtracking on the residual norm: $t:=\beta t$ while $\lVert r(x+t\Delta x,\nu+t\Delta\nu)\rVert_2>(1-\alpha t)\lVert r(x,\nu)\rVert_2$. Stop when $Ax=b$ and $\lVert r\rVert_2\le\epsilon$.

:::

```{=latex}
\begin{algorithm}
\caption{Infeasible start Newton method}
\begin{algorithmic}
\INPUT $x\in\operatorname{dom}f$, $\nu$, tolerance $\epsilon>0$, $\alpha\in(0,\frac12)$, $\beta\in(0,1)$
\REPEAT
  \STATE solve the KKT system for $(\Delta x,\Delta\nu)$
  \STATE $t\gets1$
  \WHILE{$\lVert r(x+t\Delta x,\nu+t\Delta\nu)\rVert_2>(1-\alpha t)\lVert r(x,\nu)\rVert_2$}
    \STATE $t\gets\beta t$
  \ENDWHILE
  \STATE $x\gets x+t\Delta x$; $\nu\gets\nu+t\Delta\nu$
\UNTIL{$Ax=b$ and $\lVert r(x,\nu)\rVert_2\le\epsilon$}
\RETURN $(x,\nu)$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-infeasible-start-residual .proposition name="Primal residual after a step"}

After a step of size $t$ in @def-infeasible-start-newton, the primal residual is scaled by $1-t$: $A(x+t\Delta x)-b=(1-t)(Ax-b)$. Once a full step $t=1$ is taken, all later iterates are feasible.

:::

::: {.proof}

1. The second block row says $A\Delta x=-(Ax-b)$, so $A(x+t\Delta x)-b=(Ax-b)-t(Ax-b)$.

2. If $t=1$ once, the residual becomes $0$ and stays $0$ since it is only ever multiplied.

:::

::: {#exm-optimal-allocation .example name="Network flow and resource allocation"}

Minimize $\sum_{i=1}^n\phi_i(x_i)$ subject to $\mathbf 1^{\mathsf T}x=b$, with $\phi_i$ strictly convex. The Hessian $H=\operatorname{diag}(\phi_i''(x_i))$ is diagonal, so the Newton system $H\Delta x+\mathbf 1w=-g$, $\mathbf 1^{\mathsf T}\Delta x=0$ (with $g=\nabla f(x)$) is solved by block elimination (@thm-block-elimination) in $O(n)$ flops: $\Delta x=-H^{-1}(g+\mathbf 1w)$ and $\mathbf 1^{\mathsf T}\Delta x=0$ give
$$w=-\frac{\mathbf 1^{\mathsf T}H^{-1}g}{\mathbf 1^{\mathsf T}H^{-1}\mathbf 1}.$$

:::

::: {#rmk-equality-constrained-minimization-1 .remark name="Three methods, same cost"}

Elimination, the feasible Newton method and the infeasible start method cost about the same per step when the KKT system is solved with its structure; the choice depends on whether a feasible start is known and whether elimination destroys sparsity.

:::

::: {#rmk-equality-constrained-minimization-2 .remark editor="No figure: the steps live in the combined primal-dual space, and in two dimensions with one equation the feasible method reduces to the one-variable Newton picture."}

The infeasible start method is Newton's method for the nonlinear equations $r(x,\nu)=0$; the backtracking on $\lVert r\rVert_2$ makes it converge from any start in $\operatorname{dom}f$ under mild conditions.

:::
