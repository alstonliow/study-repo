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

::: {#fig-newtons-method-for-minimization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.1,0) -- (2.9,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {$y$};
\draw[emph] (0.2,1.81) -- (0.24,1.66) -- (0.29,1.54) -- (0.33,1.44) -- (0.37,1.36) -- (0.42,1.29) -- (0.46,1.24) -- (0.5,1.19) -- (0.55,1.15) -- (0.59,1.12) -- (0.63,1.09) -- (0.68,1.07) -- (0.72,1.05) -- (0.76,1.03) -- (0.81,1.02) -- (0.85,1.01) -- (0.89,1.01) -- (0.94,1) -- (0.98,1) -- (1.02,1) -- (1.07,1) -- (1.11,1.01) -- (1.15,1.01) -- (1.2,1.02) -- (1.24,1.02) -- (1.28,1.03) -- (1.33,1.04) -- (1.37,1.06) -- (1.41,1.07) -- (1.46,1.08) -- (1.5,1.09) -- (1.54,1.11) -- (1.59,1.13) -- (1.63,1.14) -- (1.67,1.16) -- (1.72,1.18) -- (1.76,1.19) -- (1.8,1.21) -- (1.85,1.23) -- (1.89,1.25) -- (1.93,1.27) -- (1.98,1.3) -- (2.02,1.32) -- (2.06,1.34) -- (2.11,1.36) -- (2.15,1.38) -- (2.19,1.41) -- (2.24,1.43) -- (2.28,1.46) -- (2.32,1.48) -- (2.37,1.51) -- (2.41,1.53) -- (2.45,1.56) -- (2.5,1.58) -- (2.54,1.61) -- (2.58,1.63) -- (2.63,1.66) -- (2.67,1.69) -- (2.71,1.72) -- (2.76,1.74) -- (2.8,1.77);
\draw[hl, dashed] (0.1,1.91) -- (0.12,1.85) -- (0.15,1.79) -- (0.17,1.73) -- (0.2,1.67) -- (0.23,1.62) -- (0.25,1.57) -- (0.28,1.52) -- (0.3,1.47) -- (0.33,1.43) -- (0.35,1.39) -- (0.38,1.35) -- (0.4,1.31) -- (0.43,1.28) -- (0.45,1.25) -- (0.47,1.22) -- (0.5,1.19) -- (0.53,1.17) -- (0.55,1.15) -- (0.57,1.13) -- (0.6,1.11) -- (0.62,1.1) -- (0.65,1.09) -- (0.67,1.08) -- (0.7,1.07) -- (0.72,1.07) -- (0.75,1.07) -- (0.78,1.07) -- (0.8,1.07) -- (0.82,1.08) -- (0.85,1.09) -- (0.88,1.1) -- (0.9,1.11) -- (0.92,1.13) -- (0.95,1.15) -- (0.97,1.17) -- (1,1.19) -- (1.03,1.22) -- (1.05,1.25) -- (1.07,1.28) -- (1.1,1.31) -- (1.12,1.35) -- (1.15,1.39) -- (1.18,1.43) -- (1.2,1.47) -- (1.23,1.52) -- (1.25,1.57) -- (1.28,1.62) -- (1.3,1.67) -- (1.33,1.73) -- (1.35,1.79) -- (1.38,1.85) -- (1.4,1.91) -- (1.43,1.98) -- (1.45,2.05) -- (1.48,2.12) -- (1.5,2.19) -- (1.53,2.27);
\fill[ink] (0.5,1.19) circle[pt] node[lab, above left] {$x$};
\fill[accent] (0.75,1.07) circle[pt];
\fill[ink] (0.75,1.04) circle[pt] node[lab, below right] {$x+\Delta x_{\rm nt}$};
\draw[faint] (0.75,0) -- (0.75,1.04);
\node[lab, above] at (2.5,1.58) {$f$};
\node[lab, left] at (0.35,2.2) {$\hat f$};
\end{tikzpicture}
\end{center}
```

The Newton step minimizes the second-order model $\hat f$ (dashed) of $f$ at $x$. Here $f(x)=x-\log x$, $x=0.5$: the model's minimizer is $x+\Delta x_{\rm nt}=0.75$, already close to the true minimizer $1$.

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

::: {#fig-newtons-method-for-minimization-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0.77,0) -- (0.77,0.03) -- (0.76,0.05) -- (0.75,0.08) -- (0.73,0.11) -- (0.7,0.13) -- (0.67,0.16) -- (0.63,0.18) -- (0.59,0.2) -- (0.55,0.22) -- (0.5,0.24) -- (0.44,0.26) -- (0.39,0.27) -- (0.33,0.29) -- (0.26,0.3) -- (0.2,0.31) -- (0.13,0.31) -- (0.07,0.32) -- (0,0.32) -- (-0.07,0.32) -- (-0.13,0.31) -- (-0.2,0.31) -- (-0.26,0.3) -- (-0.33,0.29) -- (-0.39,0.27) -- (-0.44,0.26) -- (-0.5,0.24) -- (-0.55,0.22) -- (-0.59,0.2) -- (-0.63,0.18) -- (-0.67,0.16) -- (-0.7,0.13) -- (-0.73,0.11) -- (-0.75,0.08) -- (-0.76,0.05) -- (-0.77,0.03) -- (-0.77,0) -- (-0.77,-0.03) -- (-0.76,-0.05) -- (-0.75,-0.08) -- (-0.73,-0.11) -- (-0.7,-0.13) -- (-0.67,-0.16) -- (-0.63,-0.18) -- (-0.59,-0.2) -- (-0.55,-0.22) -- (-0.5,-0.24) -- (-0.44,-0.26) -- (-0.39,-0.27) -- (-0.33,-0.29) -- (-0.26,-0.3) -- (-0.2,-0.31) -- (-0.13,-0.31) -- (-0.07,-0.32) -- (0,-0.32) -- (0.07,-0.32) -- (0.13,-0.31) -- (0.2,-0.31) -- (0.26,-0.3) -- (0.33,-0.29) -- (0.39,-0.27) -- (0.44,-0.26) -- (0.5,-0.24) -- (0.55,-0.22) -- (0.59,-0.2) -- (0.63,-0.18) -- (0.67,-0.16) -- (0.7,-0.13) -- (0.73,-0.11) -- (0.75,-0.08) -- (0.76,-0.05) -- (0.77,-0.03) -- (0.77,0) -- cycle;
\draw[faint] (1.41,0) -- (1.41,0.05) -- (1.39,0.1) -- (1.37,0.15) -- (1.33,0.2) -- (1.28,0.24) -- (1.22,0.29) -- (1.16,0.33) -- (1.08,0.37) -- (1,0.41) -- (0.91,0.44) -- (0.81,0.47) -- (0.71,0.5) -- (0.6,0.52) -- (0.48,0.54) -- (0.37,0.56) -- (0.25,0.57) -- (0.12,0.58) -- (0,0.58) -- (-0.12,0.58) -- (-0.25,0.57) -- (-0.37,0.56) -- (-0.48,0.54) -- (-0.6,0.52) -- (-0.71,0.5) -- (-0.81,0.47) -- (-0.91,0.44) -- (-1,0.41) -- (-1.08,0.37) -- (-1.16,0.33) -- (-1.22,0.29) -- (-1.28,0.24) -- (-1.33,0.2) -- (-1.37,0.15) -- (-1.39,0.1) -- (-1.41,0.05) -- (-1.41,0) -- (-1.41,-0.05) -- (-1.39,-0.1) -- (-1.37,-0.15) -- (-1.33,-0.2) -- (-1.28,-0.24) -- (-1.22,-0.29) -- (-1.16,-0.33) -- (-1.08,-0.37) -- (-1,-0.41) -- (-0.91,-0.44) -- (-0.81,-0.47) -- (-0.71,-0.5) -- (-0.6,-0.52) -- (-0.48,-0.54) -- (-0.37,-0.56) -- (-0.25,-0.57) -- (-0.12,-0.58) -- (0,-0.58) -- (0.12,-0.58) -- (0.25,-0.57) -- (0.37,-0.56) -- (0.48,-0.54) -- (0.6,-0.52) -- (0.71,-0.5) -- (0.81,-0.47) -- (0.91,-0.44) -- (1,-0.41) -- (1.08,-0.37) -- (1.16,-0.33) -- (1.22,-0.29) -- (1.28,-0.24) -- (1.33,-0.2) -- (1.37,-0.15) -- (1.39,-0.1) -- (1.41,-0.05) -- (1.41,0) -- cycle;
\draw[faint] (2,0) -- (1.99,0.07) -- (1.97,0.14) -- (1.93,0.21) -- (1.88,0.28) -- (1.81,0.35) -- (1.73,0.41) -- (1.64,0.47) -- (1.53,0.52) -- (1.41,0.58) -- (1.29,0.63) -- (1.15,0.67) -- (1,0.71) -- (0.85,0.74) -- (0.68,0.77) -- (0.52,0.79) -- (0.35,0.8) -- (0.17,0.81) -- (0,0.82) -- (-0.17,0.81) -- (-0.35,0.8) -- (-0.52,0.79) -- (-0.68,0.77) -- (-0.85,0.74) -- (-1,0.71) -- (-1.15,0.67) -- (-1.29,0.63) -- (-1.41,0.58) -- (-1.53,0.52) -- (-1.64,0.47) -- (-1.73,0.41) -- (-1.81,0.35) -- (-1.88,0.28) -- (-1.93,0.21) -- (-1.97,0.14) -- (-1.99,0.07) -- (-2,0) -- (-1.99,-0.07) -- (-1.97,-0.14) -- (-1.93,-0.21) -- (-1.88,-0.28) -- (-1.81,-0.35) -- (-1.73,-0.41) -- (-1.64,-0.47) -- (-1.53,-0.52) -- (-1.41,-0.58) -- (-1.29,-0.63) -- (-1.15,-0.67) -- (-1,-0.71) -- (-0.85,-0.74) -- (-0.68,-0.77) -- (-0.52,-0.79) -- (-0.35,-0.8) -- (-0.17,-0.81) -- (0,-0.82) -- (0.17,-0.81) -- (0.35,-0.8) -- (0.52,-0.79) -- (0.68,-0.77) -- (0.85,-0.74) -- (1,-0.71) -- (1.15,-0.67) -- (1.29,-0.63) -- (1.41,-0.58) -- (1.53,-0.52) -- (1.64,-0.47) -- (1.73,-0.41) -- (1.81,-0.35) -- (1.88,-0.28) -- (1.93,-0.21) -- (1.97,-0.14) -- (1.99,-0.07) -- (2,0) -- cycle;
\fill[ink] (-1.7,0.5) circle[pt] node[lab, left] {$x$};
\draw[->] (-1.7,0.5) -- (-1.21,-0.37) node[lab, right] {$-\nabla f$};
\draw[->, hl] (-1.7,0.5) -- (0,0) node[lab, above] {$\Delta x_{\rm nt}$};
\fill[accent] (0,0) circle[pt];
\end{tikzpicture}
\end{center}
```

On the badly conditioned quadratic $\tfrac12(x_1^2+6x_2^2)$, the negative gradient points across the narrow valley, while the Newton step points straight at the minimizer and reaches it in one step: Newton's method does not see the conditioning.

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

::: {#fig-newtons-method-for-minimization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[bar] (0,0) rectangle (0.45,0.15);
\node[lab, tick] at (0.23,-0.2) {0};
\node[lab, tick, above] at (0.23,0.15) {0.3};
\fill[bar] (0.7,0) rectangle (1.15,0.3);
\node[lab, tick] at (0.92,-0.2) {1};
\node[lab, tick, above] at (0.92,0.3) {0.6};
\fill[bar] (1.4,0) rectangle (1.85,0.6);
\node[lab, tick] at (1.62,-0.2) {2};
\node[lab, tick, above] at (1.62,0.6) {1.2};
\fill[bar] (2.1,0) rectangle (2.55,1.2);
\node[lab, tick] at (2.32,-0.2) {3};
\node[lab, tick, above] at (2.32,1.2) {2.4};
\fill[bar] (2.8,0) rectangle (3.25,2.41);
\node[lab, tick] at (3.02,-0.2) {4};
\node[lab, tick, above] at (3.02,2.41) {4.8};
\draw[faint] (-0.1,0) -- (3.5,0);
\node[lab] at (1.6,-0.55) {iteration $k$};
\end{tikzpicture}
\end{center}
```

Correct digits $-\log_{10}(1-x^{(k)})$ for Newton's method on $x-\log x$ from $x^{(0)}=0.5$. The relation $1-x^+=(1-x)^2$ doubles them at every step: quadratic convergence.

:::

::: {#rmk-newtons-method-for-minimization-1 .remark name="Cost per step"}

Each step solves $\nabla^2f(x)\,\Delta x=-\nabla f(x)$, which costs $\frac13n^3$ flops by Cholesky for dense Hessians, and far less when the Hessian is sparse or banded (@sec-math-optimization-algorithms-structured-linear-equations). Gradient descent steps are cheap but many; Newton steps are expensive but few.

:::

::: {#rmk-newtons-method-for-minimization-2 .remark}

On a convex quadratic the second-order model is exact, so a single full Newton step from any point lands on the minimizer; this is the extreme case of affine invariance.

:::
