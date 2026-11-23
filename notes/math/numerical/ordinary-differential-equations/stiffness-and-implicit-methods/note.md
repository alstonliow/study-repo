---
title: "Stability Regions, Stiffness and Implicit Methods"
sources: [mit18335-6]
requires: [math/numerical/ordinary-differential-equations/one-step-methods]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 6 (numerical methods for ordinary differential equations; guest slides on stiff solvers), in our own wording; proofs written out in steps; the stability boundary of RK4 and the stiff example were computed in Python. -->

Convergence (@thm-one-step-convergence) is a statement about $h\to0$. With a fixed, reasonable step size a method can still blow up, when the problem has rapidly decaying components that the method cannot follow. Such problems are called *stiff*, and they require implicit methods.

::: {#def-absolute-stability .definition name="Stability function and region of absolute stability"}

Apply a one-step method to the *test equation* $y'=\lambda y$ with $\lambda\in\mathbb{C}$. For Runge–Kutta methods the result has the form $y_{k+1}=R(z)\,y_k$ with $z=h\lambda$; $R$ is the *stability function*. The *region of absolute stability* is $S=\{z\in\mathbb{C}:\lvert R(z)\rvert\le1\}$: for $h\lambda\in S$ the numerical solution does not grow, as the exact solution $e^{\lambda t}$ does not grow when $\operatorname{Re}\lambda\le0$. A method is *A-stable* if $S$ contains the whole left half-plane.

:::

::: {#prp-stability-functions .proposition name="Stability functions of four methods"}

1. Forward Euler: $R(z)=1+z$; $S$ is the disk $\lvert z+1\rvert\le1$.

2. RK4: $R(z)=1+z+\tfrac{z^2}2+\tfrac{z^3}6+\tfrac{z^4}{24}$, the Taylor polynomial of $e^z$; $S$ is bounded and meets the negative real axis in $[-2.79,0]$.

3. *Backward Euler* $y_{k+1}=y_k+hf(t_{k+1},y_{k+1})$: $R(z)=1/(1-z)$; it is A-stable.

4. *Trapezoidal rule* $y_{k+1}=y_k+\tfrac h2\bigl(f(t_k,y_k)+f(t_{k+1},y_{k+1})\bigr)$: $R(z)=(1+z/2)/(1-z/2)$; $S$ is exactly the closed left half-plane, so it is A-stable.

:::

::: {.proof}

1. Euler gives $y_{k+1}=y_k+h\lambda y_k$.

2. For RK4 with $f=\lambda y$: $k_1=\lambda y$, $k_2=\lambda(1+\tfrac z2)y$, $k_3=\lambda(1+\tfrac z2+\tfrac{z^2}4)y$, $k_4=\lambda(1+z+\tfrac{z^2}2+\tfrac{z^3}4)y$, and $\tfrac h6(k_1+2k_2+2k_3+k_4)$ collects to $(z+\tfrac{z^2}2+\tfrac{z^3}6+\tfrac{z^4}{24})y$. A polynomial is unbounded, so $S$ is bounded; the real endpoint $-2.785$ is the real root of $R(z)=1$ other than $0$, i.e. of $1+\tfrac z2+\tfrac{z^2}6+\tfrac{z^3}{24}=0$, found numerically.

3. Backward Euler gives $y_{k+1}=y_k+zy_{k+1}$, so $y_{k+1}=y_k/(1-z)$. For $\operatorname{Re}z\le0$, $\lvert1-z\rvert\ge1$.

4. The trapezoidal rule gives $(1-\tfrac z2)y_{k+1}=(1+\tfrac z2)y_k$. $\lvert1+\tfrac z2\rvert\le\lvert1-\tfrac z2\rvert$ iff $z$ is at least as close to $-2$ as to $2$, i.e. iff $\operatorname{Re}z\le0$.

:::

::: {#fig-stiffness-and-implicit-methods-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.75]
\fill[tintC] (0,2.83) -- (-0.31,2.94) -- (-0.61,2.87) -- (-0.87,2.69) -- (-1.1,2.46) -- (-1.31,2.27) -- (-1.54,2.12) -- (-1.79,1.99) -- (-2.04,1.83) -- (-2.27,1.65) -- (-2.46,1.42) -- (-2.61,1.16) -- (-2.7,0.88) -- (-2.76,0.59) -- (-2.78,0.29) -- (-2.79,0) -- (-2.78,-0.29) -- (-2.76,-0.59) -- (-2.7,-0.88) -- (-2.61,-1.16) -- (-2.46,-1.42) -- (-2.27,-1.65) -- (-2.04,-1.83) -- (-1.79,-1.99) -- (-1.54,-2.12) -- (-1.31,-2.27) -- (-1.1,-2.46) -- (-0.87,-2.69) -- (-0.61,-2.87) -- (-0.31,-2.94) -- (0,-2.83) -- cycle;
\draw[emph] (0,2.83) -- (-0.31,2.94) -- (-0.61,2.87) -- (-0.87,2.69) -- (-1.1,2.46) -- (-1.31,2.27) -- (-1.54,2.12) -- (-1.79,1.99) -- (-2.04,1.83) -- (-2.27,1.65) -- (-2.46,1.42) -- (-2.61,1.16) -- (-2.7,0.88) -- (-2.76,0.59) -- (-2.78,0.29) -- (-2.79,0) -- (-2.78,-0.29) -- (-2.76,-0.59) -- (-2.7,-0.88) -- (-2.61,-1.16) -- (-2.46,-1.42) -- (-2.27,-1.65) -- (-2.04,-1.83) -- (-1.79,-1.99) -- (-1.54,-2.12) -- (-1.31,-2.27) -- (-1.1,-2.46) -- (-0.87,-2.69) -- (-0.61,-2.87) -- (-0.31,-2.94) -- (0,-2.83);
\fill[tintA] (-1,0) circle (1); \draw[hl] (-1,0) circle (1);
\draw[faint, ->] (-3.6,0) -- (3.2,0) node[lab, right] {$\operatorname{Re}z$};
\draw[faint, ->] (0,-3.3) -- (0,3.4) node[lab, above] {$\operatorname{Im}z$};
\node[lab] at (-1,-0.45) {Euler};
\node[lab] at (-2.0,2.4) {RK4};
\begin{scope}[xshift=8.2cm]
\fill[tintB] (-3.3,-3.2) rectangle (3.0,3.2);
\fill[white] (1,0) circle (1); \draw[hl] (1,0) circle (1);
\draw[faint, ->] (-3.6,0) -- (3.2,0) node[lab, right] {$\operatorname{Re}z$};
\draw[faint, ->] (0,-3.3) -- (0,3.4) node[lab, above] {$\operatorname{Im}z$};
\node[lab] at (-1.8,1.8) {backward Euler};
\node[note] at (1,-1.4) {unstable};
\end{scope}
\end{tikzpicture}
\end{center}
```

Regions of absolute stability (shaded). Left: forward Euler (the disk $\lvert z+1\rvert\le1$) and RK4 (the larger bounded region, reaching $-2.79$ on the real axis and $\pm2.83i$ on the imaginary axis). Right: backward Euler is stable everywhere except the disk $\lvert z-1\rvert<1$, in particular in the whole left half-plane.

:::

::: {#def-stiffness .definition name="Stiff problem"}

A system $y'=f(t,y)$ is *stiff* on an interval when the Jacobian $\partial f/\partial y$ has eigenvalues with large negative real part, $\lvert\lambda\rvert$ much larger than $1/$ (time scale of the solution of interest). Then an explicit method must take $h=O(1/\lvert\lambda\rvert)$ to keep $h\lambda$ in its bounded stability region, even though the solution itself is smooth and accuracy alone would allow much larger steps.

:::

::: {#exm-stiff-equation .example name="Relaxation to a moving target"}

$y'=-50\,(y-\cos t)$, $y(0)=0$, has solution $y\approx\cos t$ after a transient that decays like $e^{-50t}$. Forward Euler with $h=0.05$ has $h\lambda=-2.5$, outside its stability disk: the iterates are $2.5,\,-1.25,\,4.37,\,-4.08,\dots$ and reach $-1.9\times10^5$ at $t=1.5$. With $h=0.03$ ($h\lambda=-1.5$, inside) it is stable but oscillates for several steps. Backward Euler with the much larger $h=0.1$ gives $0.83,\,0.96,\,0.96,\,0.93,\,0.89,\dots$, following $\cos t$ with an error of a few percent, the size expected of a first-order method.

:::

::: {#fig-stiffness-and-implicit-methods-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=5cm, y=1.6cm]
\draw[->, faint] (0,0) -- (1.6,0) node[lab, right] {$t$};
\draw[->, faint] (0,-1.5) -- (0,1.7) node[lab, above] {$y$};
\draw[faint, domain=0:1.5, samples=60] plot (\x,{cos(\x r)});
\node[note] at (1.45,0.35) {$\cos t$};
\draw[hl] plot coordinates {(0,0) (0.1,0.829) (0.2,0.955) (0.3,0.955) (0.4,0.927) (0.5,0.886) (0.6,0.835) (0.7,0.777) (0.8,0.71) (0.9,0.636) (1.0,0.556) (1.1,0.471) (1.2,0.38) (1.3,0.286) (1.4,0.189) (1.5,0.091)};
\foreach \p in {(0.1,0.829),(0.2,0.955),(0.3,0.955),(0.4,0.927),(0.5,0.886),(0.6,0.835),(0.7,0.777),(0.8,0.71),(0.9,0.636),(1.0,0.556),(1.1,0.471),(1.2,0.38),(1.3,0.286),(1.4,0.189),(1.5,0.091)} {\fill[accent] \p circle (1.5pt);}
\draw[emph] (0,0) -- (0.05,1.5) -- (0.1,-1.253) -- (0.13,-1.5);
\node[note, anchor=west] at (0.14,-1.3) {forward Euler, $h=0.05$: $2.5,\,-1.25,\,4.37,\dots\to\infty$};
\draw[emph, dashed] plot coordinates {(0,0) (0.03,1.5) (0.06,0.749) (0.09,1.123) (0.12,0.933) (0.15,1.023) (0.18,0.972) (0.21,0.99) (0.24,0.972) (0.27,0.971) (0.3,0.96) (0.33,0.953)};
\node[note, anchor=west] at (0.36,1.35) {forward Euler, $h=0.03$ (dashed)};
\node[note, anchor=west] at (0.75,0.95) {backward Euler, $h=0.1$};
\end{tikzpicture}
\end{center}
```

The stiff problem of @exm-stiff-equation. Forward Euler with $h=0.05$ leaves the picture after one step (the first value $2.5$ is clipped at $1.5$) and diverges; with $h=0.03$ it settles after oscillating. Backward Euler with a step twice as large tracks the smooth solution.

:::

::: {#rmk-stiffness-and-implicit-methods-1 .remark name="The price of implicitness"}

An implicit method must solve a nonlinear system $y_{k+1}-h\,f(t_{k+1},y_{k+1})=y_k$ at every step, usually by Newton's method, whose linear systems involve $I-h\,\partial f/\partial y$. For large systems this is done with sparse direct solvers or preconditioned Krylov methods, reusing the Jacobian and its factorization across steps. Higher-order A-stable or nearly A-stable choices include the backward differentiation formulas (BDF, used in stiff solvers since Gear), implicit Runge–Kutta methods such as Radau IIA, and Rosenbrock methods, which replace Newton iterations by one linear solve per stage. No explicit Runge–Kutta or linear multistep method is A-stable, and an A-stable linear multistep method has order at most $2$ (Dahlquist's second barrier).

:::
