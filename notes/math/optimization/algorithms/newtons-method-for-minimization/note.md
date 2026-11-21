---
title: "Newton's Method for Minimization"
sources: [ee364a-10]
requires: [math/optimization/algorithms/descent-methods, math/calculus/single-variable/applications-of-derivatives/newtons-method]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on unconstrained minimization, in our own wording; proofs written out in steps. Newton's method for root finding in one variable is in @sec-math-calculus-single-variable-applications-of-derivatives-newtons-method. Iterates in the example computed in Python. -->

Newton's method minimizes the second-order Taylor model at each step. It is affine invariant, and near the minimum it converges quadratically; far away, a line search keeps it safe.

::: {#def-newton-step .definition name="Newton step and Newton decrement" related="def-newtons-method"}

For $f$ with $\nabla^2f(x)\succ0$, the *Newton step* and *Newton decrement* are
$$\Delta x_{\rm nt}=-\nabla^2f(x)^{-1}\nabla f(x),\qquad\lambda(x)=\big(\nabla f(x)^{\mathsf T}\nabla^2f(x)^{-1}\nabla f(x)\big)^{1/2}.$$
$x+\Delta x_{\rm nt}$ minimizes the second-order approximation $\hat f(x+v)=f(x)+\nabla f(x)^{\mathsf T}v+\frac12v^{\mathsf T}\nabla^2f(x)v$, and $f(x)-\inf_v\hat f(x+v)=\frac12\lambda(x)^2$. Also $\nabla f(x)^{\mathsf T}\Delta x_{\rm nt}=-\lambda(x)^2$, so $\Delta x_{\rm nt}$ is a descent direction.

:::

::: {.proof}

1. $\hat f(x+v)$ is a strictly convex quadratic in $v$ with gradient $\nabla f(x)+\nabla^2f(x)v$, which vanishes at $v=\Delta x_{\rm nt}$.

2. Substituting, $\hat f(x+\Delta x_{\rm nt})=f(x)-\nabla f^{\mathsf T}(\nabla^2f)^{-1}\nabla f+\frac12\nabla f^{\mathsf T}(\nabla^2f)^{-1}\nabla f=f(x)-\frac12\lambda(x)^2$.

3. $\nabla f^{\mathsf T}\Delta x_{\rm nt}=-\nabla f^{\mathsf T}(\nabla^2f)^{-1}\nabla f=-\lambda^2<0$ unless $\nabla f(x)=0$.

:::

::: {#def-damped-newton .definition name="Newton's method"}

Given $x\in\operatorname{dom}f$ and tolerance $\epsilon>0$, repeat: compute $\Delta x_{\rm nt}$ and $\lambda^2$; stop if $\lambda^2/2\le\epsilon$; choose $t$ by backtracking line search (@def-descent-method); set $x:=x+t\Delta x_{\rm nt}$.

:::

```{=latex}
\begin{algorithm}
\caption{Newton's method}
\begin{algorithmic}
\INPUT starting point $x\in\operatorname{dom}f$, tolerance $\epsilon>0$
\STATE $\Delta x_{\rm nt}\gets-\nabla^2f(x)^{-1}\nabla f(x)$; $\lambda^2\gets-\nabla f(x)^{\mathsf T}\Delta x_{\rm nt}$
\WHILE{$\lambda^2/2>\epsilon$}
  \STATE choose $t$ by backtracking line search
  \STATE $x\gets x+t\Delta x_{\rm nt}$
  \STATE $\Delta x_{\rm nt}\gets-\nabla^2f(x)^{-1}\nabla f(x)$; $\lambda^2\gets-\nabla f(x)^{\mathsf T}\Delta x_{\rm nt}$
\ENDWHILE
\RETURN $x$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-newton-affine-invariance .proposition name="Affine invariance"}

If $T$ is invertible and $\bar f(y)=f(Ty)$, then the Newton steps correspond: $\Delta y_{\rm nt}=T^{-1}\Delta x_{\rm nt}$ at $x=Ty$, and $\lambda$ is the same. So Newton's method started at $y^{(0)}$ for $\bar f$ produces $y^{(k)}=T^{-1}x^{(k)}$.

:::

::: {.proof}

1. $\nabla\bar f(y)=T^{\mathsf T}\nabla f(x)$ and $\nabla^2\bar f(y)=T^{\mathsf T}\nabla^2f(x)T$.

2. Hence $\Delta y_{\rm nt}=-(T^{\mathsf T}\nabla^2fT)^{-1}T^{\mathsf T}\nabla f=-T^{-1}(\nabla^2f)^{-1}\nabla f=T^{-1}\Delta x_{\rm nt}$, and $\nabla\bar f^{\mathsf T}\Delta y_{\rm nt}=\nabla f^{\mathsf T}\Delta x_{\rm nt}$.

3. The backtracking test compares the same numbers in both coordinates, so the step sizes agree too.

:::

::: {#thm-newton-classical-convergence .theorem name="Classical convergence analysis"}

Assume $mI\preceq\nabla^2f\preceq MI$ on the initial sublevel set and $\nabla^2f$ is Lipschitz there with constant $L$: $\lVert\nabla^2f(x)-\nabla^2f(y)\rVert_2\le L\lVert x-y\rVert_2$. There are $\eta\in(0,m^2/L]$ and $\gamma>0$ such that

1. (damped phase) if $\lVert\nabla f(x)\rVert_2\ge\eta$, then $f(x^+)-f(x)\le-\gamma$;

2. (quadratic phase) if $\lVert\nabla f(x)\rVert_2<\eta$, then the line search takes $t=1$ and
$$\frac{L}{2m^2}\lVert\nabla f(x^+)\rVert_2\le\Big(\frac L{2m^2}\lVert\nabla f(x)\rVert_2\Big)^2.$$

Consequently the number of iterations until $f(x)-p^\star\le\epsilon$ is at most $\frac{f(x^{(0)})-p^\star}{\gamma}+\log_2\log_2(\epsilon_0/\epsilon)$, with $\epsilon_0=2m^3/L^2$.

:::

::: {.proof}

We prove the quadratic phase bound for a full step $t=1$; the damped phase constant and the claim that $t=1$ is accepted are stated without proof.

1. Write $H=\nabla^2f(x)$, $g=\nabla f(x)$, $\Delta=\Delta x_{\rm nt}=-H^{-1}g$. Then
$$\nabla f(x+\Delta)=\nabla f(x+\Delta)-g-H\Delta=\int_0^1\big(\nabla^2f(x+s\Delta)-H\big)\Delta\,ds.$$

2. The Lipschitz condition bounds the integrand by $Ls\lVert\Delta\rVert_2^2$, so $\lVert\nabla f(x^+)\rVert_2\le\frac L2\lVert\Delta\rVert_2^2$.

3. $\lVert\Delta\rVert_2\le\lVert H^{-1}\rVert_2\lVert g\rVert_2\le\frac1m\lVert g\rVert_2$, so $\lVert\nabla f(x^+)\rVert_2\le\frac{L}{2m^2}\lVert g\rVert_2^2$, which is the stated inequality after multiplying by $\frac L{2m^2}$.

4. Iterating, once $\frac L{2m^2}\lVert\nabla f\rVert_2\le\frac12$ the quantity is at most $(\frac12)^{2^k}$ after $k$ more steps; combine with @cor-strong-convexity-gap to get the $\log_2\log_2$ count.

:::

::: {#exm-newton-one-variable .example name="Quadratic convergence on a line"}

Minimize $f(x)=x-\log x$ on $x>0$, with minimum $p^\star=1$ at $x=1$. The Newton step is $-f'(x)/f''(x)=-(1-1/x)x^2=x-x^2$, so $x^+=2x-x^2$ and $1-x^+=(1-x)^2$. From $x^{(0)}=0.5$ the errors $1-x^{(k)}$ are $0.5,0.25,0.0625,0.0039,1.5\times10^{-5}$: the number of correct digits doubles each step.

:::

::: {#rmk-newtons-method-for-minimization-1 .remark name="Cost per step"}

Each step solves $\nabla^2f(x)\,\Delta x=-\nabla f(x)$, which costs $\frac13n^3$ flops by Cholesky for dense Hessians, and far less when the Hessian is sparse or banded (@sec-math-optimization-algorithms-structured-linear-equations). Gradient descent steps are cheap but many; Newton steps are expensive but few.

:::

::: {#rmk-newtons-method-for-minimization-2 .remark editor="No figure: on the quadratic of the gradient descent figure Newton reaches the minimum in one step, and the error sequence of the one-variable example already shows the quadratic phase."}

On a convex quadratic the second-order model is exact, so a single full Newton step from any point lands on the minimizer; this is the extreme case of affine invariance.

:::
