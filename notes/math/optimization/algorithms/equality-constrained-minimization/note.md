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

::: {#fig-equality-constrained-minimization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.8,0) -- (2.4,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-1) -- (0,2.6) node[lab, above] {$x_2$};
\draw[emph] (-0.6,1.6) -- (2,-1) node[lab, right] {$Ax=b$};
\draw[faint] (-0.57,2) -- (-0.59,1.95) -- (-0.6,1.89) -- (-0.6,1.84) -- (-0.59,1.78) -- (-0.58,1.72) -- (-0.56,1.66) -- (-0.53,1.6) -- (-0.5,1.53) -- (-0.46,1.47) -- (-0.41,1.41) -- (-0.35,1.35) -- (-0.29,1.3) -- (-0.23,1.24) -- (-0.16,1.19) -- (-0.08,1.14) -- (-0.01,1.1) -- (0.08,1.06) -- (0.16,1.02) -- (0.24,0.99) -- (0.33,0.96) -- (0.42,0.93) -- (0.51,0.92) -- (0.59,0.9) -- (0.68,0.9) -- (0.76,0.89) -- (0.84,0.9) -- (0.92,0.9) -- (0.99,0.92) -- (1.06,0.94) -- (1.12,0.96) -- (1.18,0.99) -- (1.23,1.02) -- (1.28,1.06) -- (1.31,1.1) -- (1.35,1.15) -- (1.37,1.2) -- (1.39,1.25) -- (1.4,1.31) -- (1.4,1.36) -- (1.39,1.42) -- (1.38,1.48) -- (1.36,1.54) -- (1.33,1.6) -- (1.3,1.67) -- (1.26,1.73) -- (1.21,1.79) -- (1.15,1.85) -- (1.09,1.9) -- (1.03,1.96) -- (0.96,2.01) -- (0.88,2.06) -- (0.81,2.1) -- (0.72,2.14) -- (0.64,2.18) -- (0.56,2.21) -- (0.47,2.24) -- (0.38,2.27) -- (0.29,2.28) -- (0.21,2.3) -- (0.12,2.3) -- (0.04,2.31) -- (-0.04,2.3) -- (-0.12,2.3) -- (-0.19,2.28) -- (-0.26,2.26) -- (-0.32,2.24) -- (-0.38,2.21) -- (-0.43,2.18) -- (-0.48,2.14) -- (-0.51,2.1) -- (-0.55,2.05) -- (-0.57,2) -- cycle;
\draw[faint] (-1.04,2.2) -- (-1.07,2.12) -- (-1.08,2.04) -- (-1.08,1.95) -- (-1.07,1.87) -- (-1.06,1.78) -- (-1.03,1.68) -- (-0.98,1.59) -- (-0.93,1.5) -- (-0.87,1.41) -- (-0.8,1.32) -- (-0.72,1.24) -- (-0.63,1.15) -- (-0.53,1.07) -- (-0.43,0.99) -- (-0.32,0.92) -- (-0.2,0.85) -- (-0.08,0.79) -- (0.04,0.74) -- (0.17,0.69) -- (0.3,0.65) -- (0.43,0.61) -- (0.56,0.59) -- (0.68,0.57) -- (0.81,0.55) -- (0.93,0.55) -- (1.05,0.56) -- (1.17,0.57) -- (1.27,0.59) -- (1.37,0.62) -- (1.47,0.65) -- (1.55,0.69) -- (1.63,0.74) -- (1.7,0.8) -- (1.76,0.86) -- (1.8,0.93) -- (1.84,1) -- (1.87,1.08) -- (1.88,1.16) -- (1.88,1.25) -- (1.87,1.33) -- (1.86,1.42) -- (1.83,1.52) -- (1.78,1.61) -- (1.73,1.7) -- (1.67,1.79) -- (1.6,1.88) -- (1.52,1.96) -- (1.43,2.05) -- (1.33,2.13) -- (1.23,2.21) -- (1.12,2.28) -- (1,2.35) -- (0.88,2.41) -- (0.76,2.46) -- (0.63,2.51) -- (0.5,2.55) -- (0.37,2.59) -- (0.24,2.61) -- (0.12,2.63) -- (-0.01,2.65) -- (-0.13,2.65) -- (-0.25,2.64) -- (-0.37,2.63) -- (-0.47,2.61) -- (-0.57,2.58) -- (-0.67,2.55) -- (-0.75,2.51) -- (-0.83,2.46) -- (-0.9,2.4) -- (-0.96,2.34) -- (-1,2.27) -- (-1.04,2.2) -- cycle;
\draw[faint] (-1.54,2.4) -- (-1.58,2.3) -- (-1.6,2.19) -- (-1.6,2.08) -- (-1.59,1.96) -- (-1.56,1.84) -- (-1.52,1.71) -- (-1.47,1.59) -- (-1.4,1.47) -- (-1.31,1.35) -- (-1.22,1.23) -- (-1.11,1.11) -- (-0.99,0.99) -- (-0.86,0.89) -- (-0.72,0.78) -- (-0.57,0.68) -- (-0.41,0.59) -- (-0.25,0.51) -- (-0.08,0.44) -- (0.09,0.37) -- (0.26,0.31) -- (0.44,0.27) -- (0.61,0.23) -- (0.78,0.21) -- (0.95,0.19) -- (1.12,0.19) -- (1.28,0.19) -- (1.43,0.21) -- (1.58,0.24) -- (1.71,0.27) -- (1.84,0.32) -- (1.96,0.38) -- (2.06,0.45) -- (2.15,0.52) -- (2.23,0.61) -- (2.29,0.7) -- (2.34,0.8) -- (2.38,0.9) -- (2.4,1.01) -- (2.4,1.12) -- (2.39,1.24) -- (2.36,1.36) -- (2.32,1.49) -- (2.27,1.61) -- (2.2,1.73) -- (2.11,1.85) -- (2.02,1.97) -- (1.91,2.09) -- (1.79,2.21) -- (1.66,2.31) -- (1.52,2.42) -- (1.37,2.52) -- (1.21,2.61) -- (1.05,2.69) -- (0.88,2.76) -- (0.71,2.83) -- (0.54,2.89) -- (0.36,2.93) -- (0.19,2.97) -- (0.02,2.99) -- (-0.15,3.01) -- (-0.32,3.01) -- (-0.48,3.01) -- (-0.63,2.99) -- (-0.78,2.96) -- (-0.91,2.93) -- (-1.04,2.88) -- (-1.16,2.82) -- (-1.26,2.75) -- (-1.35,2.68) -- (-1.43,2.59) -- (-1.49,2.5) -- (-1.54,2.4) -- cycle;
\fill[ink] (0.4,1.6) circle[pt];
\fill[ink] (1.6,-0.6) circle[pt] node[lab, left] {$x$};
\draw[->, hl] (1.6,-0.6) -- (-0.35,1.35) node[lab, midway, right] {$\Delta x_{\rm nt}$};
\fill[accent] (-0.35,1.35) circle[pt] node[lab, above right] {$x^\star$};
\draw[->] (-0.35,1.35) -- (-0.77,0.93) node[lab, below left] {$\nabla f$};
\end{tikzpicture}
\end{center}
```

For a quadratic $f$ the Newton step with equality constraints (thick) runs along the line $Ax=b$ from a feasible $x$ straight to the constrained minimizer $x^\star$, where $\nabla f(x^\star)=-A^{\mathsf T}\nu^\star$ is normal to the line.

:::

::: {#prp-newton-elimination .proposition name="Newton's method and elimination"}

Let $\{x\mid Ax=b\}=\{Fz+\hat x\}$ with $F$ of full column rank. Newton's method for $f$ with equality constraints, started at $x^{(0)}=Fz^{(0)}+\hat x$, produces $x^{(k)}=Fz^{(k)}+\hat x$, where $z^{(k)}$ are the Newton iterates for the unconstrained $\tilde f(z)=f(Fz+\hat x)$.

:::

::: {.proof}

1. The Newton step of $\tilde f$ is $\Delta z=-(F^{\mathsf T}\nabla^2fF)^{-1}F^{\mathsf T}\nabla f$.

2. Put $v=F\Delta z$. Then $Av=0$ (as $AF=0$), and $F^{\mathsf T}(\nabla^2fv+\nabla f)=0$, so $\nabla^2fv+\nabla f\in\operatorname{null}F^{\mathsf T}=\operatorname{range}A^{\mathsf T}$: there is $w$ with $\nabla^2fv+A^{\mathsf T}w=-\nabla f$.

3. So $(v,w)$ solves the KKT system of @def-newton-step-equality, and $v=\Delta x_{\rm nt}$. The decrements and line searches agree, as $\tilde f(z+t\Delta z)=f(x+tv)$.

:::

::: {#fig-equality-constrained-minimization-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.4,0) -- (1.6,0) node[lab, right] {$z$};
\fill[ink] (0,0) circle[pt] node[lab, below] {$0$};
\draw[->, hl] (0,0) -- (0.8,0) node[lab, below] {$1$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-0.8,0) -- (2.2,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-1) -- (0,1.8) node[lab, above] {$x_2$};
\draw[emph] (-0.6,1.6) -- (2,-1);
\fill[ink] (0,1) circle[pt] node[lab, above right] {$\hat x$};
\draw[->, hl] (0,1) -- (0.8,0.2) node[lab, above right] {$F$};
\node[lab, right] at (1.5,-0.2) {$\{Fz+\hat x\}$};
\end{tikzpicture}
\end{center}
```

Elimination: the feasible set $\{x\mid Ax=b\}$ is parametrized as $x=Fz+\hat x$, with $\hat x$ one solution and the columns of $F$ a basis of the null space of $A$. Newton on $\tilde f(z)=f(Fz+\hat x)$ produces the same iterates as Newton with equality constraints.

:::

::: {#def-infeasible-start-newton .definition name="Infeasible start Newton method"}

From any $x\in\operatorname{dom}f$ and any $\nu$, linearize the optimality conditions: find $(\Delta x,\Delta\nu)$ with
$$\begin{bmatrix}\nabla^2f(x)&A^{\mathsf T}\\A&0\end{bmatrix}\begin{bmatrix}\Delta x\\\Delta\nu\end{bmatrix}=-\begin{bmatrix}\nabla f(x)+A^{\mathsf T}\nu\\Ax-b\end{bmatrix}=-r(x,\nu).$$
Choose $t$ by backtracking on the residual norm: $t:=\beta t$ while $\lVert r(x+t\Delta x,\nu+t\Delta\nu)\rVert_2>(1-\alpha t)\lVert r(x,\nu)\rVert_2$. Stop when $Ax=b$ and $\lVert r\rVert_2\le\epsilon$.

:::

::: {#fig-equality-constrained-minimization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.8,0) -- (2.4,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-0.4) -- (0,2.4) node[lab, above] {$x_2$};
\draw[emph] (-0.4,1.4) -- (1.6,-0.6) node[lab, right] {$Ax=b$};
\draw[hl] (1.8,1.8) -- (1.03,1.27) -- (-0.07,1.07) -- (-0.22,1.22) -- (-0.22,1.22) -- (-0.22,1.22) -- (-0.22,1.22);
\fill[ink] (1.8,1.8) circle[pt];
\fill[ink] (1.03,1.27) circle[pt];
\fill[ink] (-0.07,1.07) circle[pt];
\node[lab, right] at (1.8,1.8) {$x^{(0)}$};
\node[lab, right] at (1.03,1.27) {$t=\tfrac12$};
\fill[accent] (-0.22,1.22) circle[pt] node[lab, below left] {$x^\star$};
\end{tikzpicture}
\end{center}
```

The infeasible start Newton method from $x^{(0)}$ off the line: a damped step $t=\tfrac12$ halves the residual $Ax-b$, and the next full step lands on $Ax=b$, after which every iterate stays feasible.

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

::: {#rmk-equality-constrained-minimization-2 .remark}

The infeasible start method is Newton's method for the nonlinear equations $r(x,\nu)=0$; the backtracking on $\lVert r\rVert_2$ makes it converge from any start in $\operatorname{dom}f$ under mild conditions.

:::
