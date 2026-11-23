---
title: "Quasi-Newton Methods and BFGS"
sources: [mit18335-30, mit18335-31]
requires: [math/optimization/algorithms/newtons-method-for-minimization]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 30 and 31 (quasi-Newton methods and the BFGS algorithm; derivation of the BFGS update) and the note on quasi-Newton optimization, in our own wording; proofs written out in steps; the Rosenbrock runs were done in Python with a backtracking line search. -->

Newton's method converges quadratically but needs the Hessian and a linear solve with it at every step. Quasi-Newton methods build an approximation of the Hessian (or its inverse) from the gradients already computed, updating it by a low-rank correction at each step. They need only gradients, cost $O(n^2)$ per step, and still converge superlinearly. BFGS is the standard example. In this note vectors are plain lowercase letters, as elsewhere in the optimization notes.

::: {#def-secant-condition .definition name="Secant condition"}

After a step $s_k=x_{k+1}-x_k$, set $y_k=\nabla f(x_{k+1})-\nabla f(x_k)$. A new Hessian approximation $B_{k+1}$ satisfies the *secant condition* if
$$B_{k+1}s_k=y_k,$$
which is what the true Hessian satisfies to first order, $\nabla^2f\,s_k\approx y_k$. Equivalently the inverse approximation $H_{k+1}=B_{k+1}^{-1}$ satisfies $H_{k+1}y_k=s_k$. For $n>1$ the condition does not determine $B_{k+1}$; quasi-Newton methods choose the update closest to $B_k$ in a suitable sense.

:::

::: {#fig-quasi-newton-methods-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->, faint] (-0.4,0) -- (2.4,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.6) -- (0,1.8) node[lab, above] {$f'(x)$};
\draw[emph] (-0.2,0.14) -- (-0.16,0.13) -- (-0.13,0.12) -- (-0.09,0.12) -- (-0.05,0.11) -- (-0.02,0.1) -- (0.02,0.1) -- (0.06,0.09) -- (0.09,0.08) -- (0.13,0.07) -- (0.17,0.07) -- (0.2,0.06) -- (0.24,0.06) -- (0.28,0.05) -- (0.31,0.05) -- (0.35,0.04) -- (0.39,0.04) -- (0.42,0.04) -- (0.46,0.04) -- (0.5,0.04) -- (0.53,0.04) -- (0.57,0.04) -- (0.61,0.05) -- (0.64,0.05) -- (0.68,0.06) -- (0.72,0.07) -- (0.75,0.08) -- (0.79,0.09) -- (0.83,0.1) -- (0.86,0.12) -- (0.9,0.14) -- (0.94,0.16) -- (0.97,0.18) -- (1.01,0.21) -- (1.05,0.23) -- (1.08,0.26) -- (1.12,0.3) -- (1.16,0.33) -- (1.19,0.37) -- (1.23,0.41) -- (1.27,0.46) -- (1.3,0.5) -- (1.34,0.55) -- (1.38,0.61) -- (1.41,0.66) -- (1.45,0.72) -- (1.49,0.79) -- (1.52,0.86) -- (1.56,0.93) -- (1.6,1) -- (1.63,1.08) -- (1.67,1.16) -- (1.71,1.25) -- (1.74,1.34) -- (1.78,1.44) -- (1.82,1.54) -- (1.85,1.64) -- (1.89,1.75);
\draw[hl] (0.2,-0.34) -- (1.1,0.53) -- (2,1.39);
\fill[ink] (0.6,0.04) circle[pt] node[lab, below right] {$x_k$};
\fill[ink] (1.6,1.01) circle[pt] node[lab, left] {$x_{k+1}$};
\draw[faint] (0.6,0.04) -- (1.6,0.04) node[lab, midway, below] {$s$} -- (1.6,1.01) node[lab, midway, right] {$y$};
\end{tikzpicture}
\end{center}
```

The secant condition in one variable: the new curvature estimate $B_{k+1}$ is the slope of the chord of $f'$ between $x_k$ and $x_{k+1}$, so $B_{k+1}s=y$ with $s=x_{k+1}-x_k$ and $y=f'(x_{k+1})-f'(x_k)$. Quasi-Newton methods impose the same condition on a matrix.

:::

::: {#def-bfgs .definition name="BFGS method"}

Start from $x_0$ and a symmetric positive definite $H_0$ (often $I$). At step $k$: set the direction $d_k=-H_k\nabla f(x_k)$, choose a step $t_k$ by a line search, put $x_{k+1}=x_k+t_kd_k$, $s_k=t_kd_k$, $y_k=\nabla f(x_{k+1})-\nabla f(x_k)$, $\rho_k=1/(y_k^{\mathsf T}s_k)$, and update
$$H_{k+1}=(I-\rho_ks_ky_k^{\mathsf T})\,H_k\,(I-\rho_ky_ks_k^{\mathsf T})+\rho_ks_ks_k^{\mathsf T}.$$
The corresponding update of $B_k=H_k^{-1}$ is the rank-two formula $B_{k+1}=B_k-\dfrac{B_ks_ks_k^{\mathsf T}B_k}{s_k^{\mathsf T}B_ks_k}+\dfrac{y_ky_k^{\mathsf T}}{y_k^{\mathsf T}s_k}$.

:::

```{=latex}
\begin{algorithm}
\caption{BFGS with a line search}
\begin{algorithmic}
\INPUT $f$, $\nabla f$, $x_0$; $H\gets I$
\FOR{$k=0,1,2,\dots$ until $\lVert\nabla f(x_k)\rVert$ is small}
    \STATE $d\gets-H\nabla f(x_k)$
    \STATE choose $t$ by a line search (Wolfe conditions ensure $y^{\mathsf T}s>0$)
    \STATE $s\gets td$; \quad $x_{k+1}\gets x_k+s$; \quad $y\gets\nabla f(x_{k+1})-\nabla f(x_k)$; \quad $\rho\gets1/(y^{\mathsf T}s)$
    \STATE $H\gets(I-\rho sy^{\mathsf T})H(I-\rho ys^{\mathsf T})+\rho ss^{\mathsf T}$ \COMMENT{$O(n^2)$}
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#thm-bfgs-update-properties .theorem name="The BFGS update keeps the secant condition and positive definiteness"}

If $H_k$ is symmetric positive definite and $y_k^{\mathsf T}s_k>0$ (the *curvature condition*), then $H_{k+1}$ is symmetric positive definite and $H_{k+1}y_k=s_k$. In particular $d_{k+1}$ is a descent direction.

:::

::: {.proof}

1. *Secant condition.* $(I-\rho ys^{\mathsf T})y=y-\rho y(s^{\mathsf T}y)=0$, so the first term of $H_{k+1}y$ vanishes and $H_{k+1}y=\rho s(s^{\mathsf T}y)=s$.

2. *Symmetry* is clear from the form $V^{\mathsf T}H_kV+\rho ss^{\mathsf T}$ with $V=I-\rho ys^{\mathsf T}$.

3. *Positive definiteness.* For $z\ne0$, $z^{\mathsf T}H_{k+1}z=(Vz)^{\mathsf T}H_k(Vz)+\rho(s^{\mathsf T}z)^2$. Both terms are $\ge0$ because $H_k\succ0$ and $\rho>0$.

4. If both vanish then $s^{\mathsf T}z=0$ and $Vz=0$; but $Vz=z-\rho y(s^{\mathsf T}z)=z$, so $z=0$. Hence $z^{\mathsf T}H_{k+1}z>0$.

5. Then $\nabla f^{\mathsf T}d_{k+1}=-\nabla f^{\mathsf T}H_{k+1}\nabla f<0$ whenever $\nabla f\ne0$.

:::

::: {#prp-curvature-condition .proposition name="When the curvature condition holds"}

If $f$ is strictly convex, $y_k^{\mathsf T}s_k>0$ for every step $s_k\ne0$. For general $f$ it holds whenever $t_k$ satisfies the *Wolfe curvature condition* $\nabla f(x_{k+1})^{\mathsf T}d_k\ge c_2\nabla f(x_k)^{\mathsf T}d_k$ with $c_2<1$ and $d_k$ is a descent direction.

:::

::: {.proof}

1. *Convex case.* $y_k^{\mathsf T}s_k=(\nabla f(x_{k+1})-\nabla f(x_k))^{\mathsf T}(x_{k+1}-x_k)>0$ by strict monotonicity of the gradient of a strictly convex function.

2. *Wolfe case.* $y_k^{\mathsf T}s_k=t_k\bigl(\nabla f(x_{k+1})-\nabla f(x_k)\bigr)^{\mathsf T}d_k\ge t_k(c_2-1)\nabla f(x_k)^{\mathsf T}d_k>0$, since $c_2<1$ and $\nabla f(x_k)^{\mathsf T}d_k<0$.

:::

::: {#rmk-quasi-newton-methods-1 .remark name="Where the formula comes from"}

Among all symmetric $H$ with $Hy_k=s_k$, the BFGS update is the one closest to $H_k$ in the weighted Frobenius norm $\lVert W^{1/2}(H-H_k)W^{1/2}\rVert_F$, for any $W$ with $Ws_k=y_k$ (for instance the average Hessian along the step). This makes it invariant under linear changes of variables. Swapping the roles of $s$ and $y$ gives the DFP update, which works less well in practice. With exact line searches on a strictly convex quadratic, BFGS terminates in at most $n$ steps and its directions are conjugate, like CG (@thm-cg-properties). On general smooth problems with a positive definite Hessian at the minimiser it converges *superlinearly*: $\lVert x_{k+1}-x_*\rVert/\lVert x_k-x_*\rVert\to0$ (Dennis–Moré). *L-BFGS* stores only the last $m$ pairs $(s_k,y_k)$ ($m\approx5$–$20$) and applies $H_k$ by a two-loop recursion in $O(mn)$ operations, which makes it usable with millions of variables.

:::

::: {#exm-bfgs-rosenbrock .example name="The Rosenbrock function"}

Minimise $f(x)=(1-x_1)^2+100(x_2-x_1^2)^2$, whose minimum $f=0$ at $(1,1)$ lies at the end of a long curved valley along $x_2=x_1^2$. From $(-1.2,1)$ with backtracking line searches, BFGS ($H_0=I$) follows the valley and reaches $f<10^{-12}$ in $33$ iterations; the last few steps show the superlinear speed-up ($f$ drops from $10^{-2.3}$ to $10^{-4.6}$ to $10^{-12.7}$ in six steps). Gradient descent with the same line search needs about $5000$ iterations to reach $f\approx10^{-6}$.

:::

::: {#fig-quasi-newton-methods-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.4cm, y=2.4cm]
\draw[->, faint] (-1.45,0) -- (1.35,0) node[lab, right] {$x_1$};
\draw[->, faint] (0,-0.2) -- (0,1.35) node[lab, above] {$x_2$};
\draw[faint, dashed, domain=-1.12:1.12, samples=50] plot (\x,{\x*\x});
\node[note] at (-1.25,1.3) {valley $x_2=x_1^2$};
\draw[hl] plot coordinates {(-1.2,1.0) (-0.99,1.09) (-0.77,0.57) (-0.74,0.52) (-0.46,0.14) (-0.5,0.27) (-0.38,0.13) (-0.3,0.06) (-0.26,0.04) (-0.12,0.0) (-0.03,-0.03) (0.13,-0.02) (0.18,0.06) (0.35,0.09) (0.29,0.09) (0.36,0.12) (0.46,0.18) (0.44,0.18) (0.48,0.23) (0.64,0.38) (0.6,0.36) (0.66,0.43) (0.75,0.55) (0.76,0.57) (0.84,0.7) (0.89,0.78) (0.92,0.85) (0.97,0.93) (0.98,0.97) (1.0,1.0)};
\fill (-1.2,1.0) circle (1.4pt) node[lab, left] {$x_0$};
\fill[accent] (1,1) circle (1.8pt) node[lab, right] {$x_*=(1,1)$};
\end{tikzpicture}
\end{center}
```

The BFGS iterates of @exm-bfgs-rosenbrock follow the curved valley of the Rosenbrock function (dashed) from $(-1.2,1)$ to the minimiser $(1,1)$.

:::

::: {#fig-quasi-newton-methods-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.32cm, y=0.32cm]
\draw[->, faint] (0,2) -- (36.5,2) node[lab, right] {$k$};
\draw[->, faint] (0,2) -- (0,-13.5) node[lab, below] {$\log_{10}f(x_k)$};
\foreach \x in {10,20,30} {\draw[faint] (\x,1.8) -- (\x,2.2); \node[tick, above] at (\x,2.2) {$\x$};}
\foreach \y in {-4,-8,-12} {\draw[faint] (-0.25,\y) -- (0.25,\y); \node[tick, left] at (-0.25,\y) {$\y$};}
\draw[hl] plot coordinates {(0,1.4) (3,0.5) (6,0.3) (9,0.1) (12,-0.1) (15,-0.4) (18,-0.6) (21,-0.9) (24,-1.5) (27,-2.3) (30,-4.6) (33,-12.7)};
\draw[emph] plot coordinates {(0,1.38) (6,0.61) (12,0.61) (18,0.6) (24,0.6) (30,0.6) (36,-1.01)};
\node[lab] at (24,-5.5) {BFGS};
\node[note, anchor=west] at (9,-0.9) {gradient descent};
\end{tikzpicture}
\end{center}
```

Function values in @exm-bfgs-rosenbrock: BFGS creeps along the valley, then converges superlinearly; gradient descent stalls near $f\approx4$ for many steps and has only reached $f\approx0.1$ after $36$.

:::
