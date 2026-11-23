---
title: "One-Step Methods for Ordinary Differential Equations"
sources: [mit18335-6]
requires: [math/numerical/floating-point/stability-and-backward-error, math/analysis/metric-spaces/picard-lindelof]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 6 (numerical methods for ordinary differential equations; guest slides on modern differential-equation solver software), in our own wording; proofs written out in steps; the convergence data were computed in Python for y' = y. -->

An initial value problem $y'=f(t,y)$, $y(t_0)=y_0$, has a unique solution when $f$ is Lipschitz in $y$ (@thm-picard-lindelof). A numerical method replaces it by a recurrence for approximations $y_k\approx y(t_k)$ on a grid $t_k=t_0+kh$. One-step methods compute $y_{k+1}$ from $y_k$ alone; their accuracy is measured by an order $p$, and a method of order $p$ has global error $O(h^p)$.

::: {#def-one-step-method .definition name="One-step method, local error and order"}

A *one-step method* is a recurrence $y_{k+1}=y_k+h\,\Phi(t_k,y_k,h)$ with an *increment function* $\Phi$. Its *local truncation error* at a point is
$$\tau(t,h)=\frac{y(t+h)-y(t)}{h}-\Phi(t,y(t),h),$$
the defect when the exact solution is inserted. The method has *order* $p$ if $\tau=O(h^p)$ for smooth solutions. Examples:

1. *forward Euler*: $\Phi=f(t,y)$, order $1$;

2. *explicit midpoint* (a second-order Runge–Kutta method): $\Phi=f\bigl(t+\tfrac h2,\ y+\tfrac h2f(t,y)\bigr)$, order $2$;

3. *classical Runge–Kutta* (RK4): with $k_1=f(t,y)$, $k_2=f(t+\tfrac h2,y+\tfrac h2k_1)$, $k_3=f(t+\tfrac h2,y+\tfrac h2k_2)$, $k_4=f(t+h,y+hk_3)$, $\Phi=\tfrac16(k_1+2k_2+2k_3+k_4)$, order $4$.

:::

```{=latex}
\begin{algorithm}
\caption{Classical Runge--Kutta method (RK4)}
\begin{algorithmic}
\INPUT $f$, $t_0$, $y_0$, step $h$, number of steps $N$
\FOR{$k=0,\dots,N-1$}
    \STATE $k_1\gets f(t_k,y_k)$; \quad $k_2\gets f(t_k+\tfrac h2,y_k+\tfrac h2k_1)$
    \STATE $k_3\gets f(t_k+\tfrac h2,y_k+\tfrac h2k_2)$; \quad $k_4\gets f(t_k+h,y_k+hk_3)$
    \STATE $y_{k+1}\gets y_k+\tfrac h6(k_1+2k_2+2k_3+k_4)$; \quad $t_{k+1}\gets t_k+h$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#prp-euler-midpoint-order .proposition name="Orders of Euler and midpoint"}

Forward Euler has order $1$ and the explicit midpoint method has order $2$.

:::

::: {.proof}

1. *Euler.* $y(t+h)=y(t)+hy'(t)+\tfrac{h^2}2y''(\xi)$ and $y'=f(t,y)$, so $\tau=\tfrac h2y''(\xi)=O(h)$.

2. *Midpoint.* Along the solution, $y''=f_t+f_yf$. Expanding, $f(t+\tfrac h2,y+\tfrac h2f)=f+\tfrac h2(f_t+f_yf)+O(h^2)=y'+\tfrac h2y''+O(h^2)$.

3. Also $\frac{y(t+h)-y(t)}h=y'+\tfrac h2y''+O(h^2)$. Subtracting, $\tau=O(h^2)$.

:::

::: {#thm-one-step-convergence .theorem name="Convergence of one-step methods"}

Suppose $\Phi$ is Lipschitz in $y$ with constant $L$ and the method has order $p$, $\lvert\tau\rvert\le Ch^p$. Then on $[t_0,T]$ the global error $e_k=y(t_k)-y_k$ satisfies
$$\lvert e_k\rvert\le\frac{Ch^p}{L}\bigl(e^{L(t_k-t_0)}-1\bigr)=O(h^p).$$

:::

::: {.proof}

1. By the definition of $\tau$, $y(t_{k+1})=y(t_k)+h\Phi(t_k,y(t_k),h)+h\tau_k$. Subtracting the recurrence, $e_{k+1}=e_k+h\bigl(\Phi(t_k,y(t_k),h)-\Phi(t_k,y_k,h)\bigr)+h\tau_k$.

2. The Lipschitz bound gives $\lvert e_{k+1}\rvert\le(1+hL)\lvert e_k\rvert+Ch^{p+1}$, with $e_0=0$.

3. Unrolling, $\lvert e_k\rvert\le Ch^{p+1}\sum_{j<k}(1+hL)^j=Ch^{p+1}\frac{(1+hL)^k-1}{hL}$.

4. Since $1+hL\le e^{hL}$ and $kh=t_k-t_0$, $(1+hL)^k\le e^{L(t_k-t_0)}$, which gives the bound.

:::

::: {#fig-one-step-methods-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=3.2cm, y=1.6cm]
\draw[->, faint] (-0.05,0) -- (1.15,0) node[lab, right] {$t$};
\draw[->, faint] (0,-0.05) -- (0,2.9) node[lab, above] {$y$};
\draw[emph, domain=0:1, samples=50] plot (\x,{exp(\x)});
\node[lab] at (1.06,2.75) {$e^t$};
\draw[hl] (0,1) -- (0.25,1.25) -- (0.5,1.5625) -- (0.75,1.9531) -- (1,2.4414);
\foreach \p in {(0,1),(0.25,1.25),(0.5,1.5625),(0.75,1.9531),(1,2.4414)} {\fill[accent] \p circle (1.6pt);}
\draw[faint, <->] (1.02,2.4414) -- (1.02,2.718) node[midway, lab, right] {global error};
\foreach \x in {0.25,0.5,0.75,1} {\draw[faint] (\x,-0.04) -- (\x,0.04);}
\node[tick, below] at (0.25,-0.04) {$h$};
\end{tikzpicture}
\end{center}
```

Forward Euler for $y'=y$, $y(0)=1$, with $h=\tfrac14$: each step follows the tangent of the solution through the current point, and $y_4=(1+\tfrac14)^4=2.44$ falls short of $e$. The local errors accumulate into a global error of order $h$.

:::

::: {#exm-ode-orders .example name="Observed orders"}

For $y'=y$ on $[0,1]$ the errors at $t=1$ for $h=\tfrac14,\tfrac18,\dots,\tfrac1{128}$ fall by factors $2$ (Euler), $4$ (midpoint) and $16$ (RK4) per halving of $h$: with $h=\tfrac1{128}$ they are $1.0\times10^{-2}$, $2.8\times10^{-5}$ and $8.3\times10^{-11}$. RK4 costs four evaluations of $f$ per step against one for Euler, but for the same accuracy it needs vastly fewer steps.

:::

::: {#fig-one-step-methods-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.5cm, y=0.45cm]
\draw[->, faint] (1.8,0) -- (7.4,0) node[lab, right] {$\log_2(1/h)$};
\draw[->, faint] (1.8,0) -- (1.8,-10.8) node[lab, below] {$\log_{10}\lvert y_N-e\rvert$};
\foreach \x in {2,...,7} {\draw[faint] (\x,-0.12) -- (\x,0.12); \node[tick, above] at (\x,0.12) {$\x$};}
\foreach \y in {-2,-4,-6,-8,-10} {\draw[faint] (1.77,\y) -- (1.83,\y); \node[tick, left] at (1.77,\y) {$\y$};}
\draw[emph] plot coordinates {(2,-0.56) (3,-0.82) (4,-1.09) (5,-1.38) (6,-1.68) (7,-1.98)};
\draw[emph, dashed] plot coordinates {(2,-1.63) (3,-2.19) (4,-2.77) (5,-3.36) (6,-3.96) (7,-4.56)};
\draw[hl] plot coordinates {(2,-4.14) (3,-5.3) (4,-6.48) (5,-7.68) (6,-8.88) (7,-10.08)};
\node[lab] at (6.8,-1.2) {Euler};
\node[lab] at (6.8,-3.6) {midpoint};
\node[lab] at (6.5,-9.9) {RK4};
\end{tikzpicture}
\end{center}
```

Errors of @exm-ode-orders: straight lines of slopes $-p\log_{10}2$ with $p=1,2,4$.

:::

::: {#rmk-one-step-methods-1 .remark name="What production solvers do"}

Practical solvers choose the step size adaptively. *Embedded* Runge–Kutta pairs (Dormand–Prince 5(4), Tsitouras 5(4), Verner's high-order pairs) compute two solutions of orders $p$ and $p-1$ from the same stages; their difference estimates the local error, and the step is shrunk or grown to keep it near a tolerance (with a PI controller to avoid oscillating step sizes). *Linear multistep* methods (Adams–Bashforth and Adams–Moulton) reuse previous values of $f$ and need fewer evaluations per step, but are harder to restart and adapt. For non-stiff problems high-order adaptive Runge–Kutta methods are the usual default; for stiff problems explicit methods fail, as the next note shows (@sec-math-numerical-ordinary-differential-equations-stiffness-and-implicit-methods).

:::
