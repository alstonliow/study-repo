---
title: "Partial Differential Equations"
sources: [mit1802-15, mit1802n-P]
requires: [math/calculus/multivariable/differentiation/differentials-and-chain-rule]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 15 and Supplementary Notes P, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-partial-differential-equation .definition name="Partial differential equation"}

A **partial differential equation** (PDE) is an equation involving an unknown function of several variables and some of its partial derivatives. A **solution** is a differentiable function satisfying it.

:::

A PDE usually has very many solutions (for example $xw_x=yw_y$ is solved by $w=x^ny^n$ for every $n$); one looks for the solution meeting extra **boundary** or **initial conditions**. Here we only meet the basic equations of physics and check solutions.

::: {#def-classical-pdes .definition name="Laplace, wave and heat equations"}

With $\nabla^2w=w_{xx}+w_{yy}+w_{zz}$ (drop $w_{zz}$ in two dimensions):

- **Laplace equation** $\nabla^2w=0$: satisfied by steady-state temperatures, and by gravitational and electrostatic potentials away from masses and charges. Its solutions are called **harmonic** functions.
- **Poisson equation** $\nabla^2w=f$: steady state with given sources and sinks.
- **Wave equation** $w_{xx}=\dfrac1{c^2}w_{tt}$ (in one space dimension), $c$ the speed of the wave.
- **Heat or diffusion equation** $w_t=k\,\nabla^2w$, $k>0$: temperature in a conductor, concentration of a diffusing substance.

:::

::: {#exm-laplace-solutions .example name="Harmonic functions"}

- $w=\ln r=\frac12\ln(x^2+y^2)$ satisfies the two-dimensional Laplace equation away from the origin: $w_{xx}=\dfrac{y^2-x^2}{(x^2+y^2)^2}$ and $w_{yy}=\dfrac{x^2-y^2}{(x^2+y^2)^2}$.
- $w=1/\rho=(x^2+y^2+z^2)^{-1/2}$ satisfies the three-dimensional Laplace equation away from the origin; it is the potential of a point mass.
- $w=x^2-y^2$ and $w=xy$ are harmonic in the whole plane.

:::

::: {#prp-wave-equation-travelling .proposition name="Travelling waves"}

For any twice differentiable functions $f$ and $g$ of one variable,
$$w=f(x+ct)+g(x-ct)$$
solves the wave equation $w_{xx}=\frac1{c^2}w_{tt}$.

:::

::: {.proof}

1. Put $u=x-ct$. By the chain rule $\frac{\partial}{\partial x}g(u)=g'(u)$ and $\frac{\partial}{\partial t}g(u)=-c\,g'(u)$, so $g(x-ct)_{xx}=g''(u)$ and $g(x-ct)_{tt}=c^2g''(u)$.

2. In the same way $f(x+ct)_{xx}=f''$ and $f(x+ct)_{tt}=c^2f''$.

3. Adding, $w_{tt}=c^2w_{xx}$.

:::

::: {#fig-partial-differential-equations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
\draw[->] (-0.6,0) -- (5.4,0) node[lab, right] {$x$};
\draw[emph, primary] plot[domain=-0.5:2.6, samples=60] (\x, {1.3*exp(-3*(\x-1)^2)});
\draw[emph, accent] plot[domain=1.7:4.8, samples=60] (\x, {1.3*exp(-3*(\x-3.2)^2)});
\node[lab, primary] at (1,1.6) {$t=0$};
\node[lab, accent] at (3.2,1.6) {time $t$};
\draw[->, muted] (1.25,0.7) -- node[lab, above] {$ct$} (2.95,0.7);
\draw[faint, dashed] (1,0) -- (1,1.3); \draw[faint, dashed] (3.2,0) -- (3.2,1.3);
\end{tikzpicture}
\end{center}
```

A travelling wave $w=g(x-ct)$: the graph at time $t$ is the graph at time $0$ shifted right by $ct$, so the profile moves with speed $c$ without changing shape.

:::

The graph of $g(x-ct)$ at time $t$ is the graph of $g$ shifted by $ct$: a wave moving right with speed $c$; $f(x+ct)$ moves left.

::: {#exm-heat-equation-solution .example name="A decaying temperature"}

$w=e^{-kn^2t}\sin(nx)$ solves $w_t=k\,w_{xx}$: both sides equal $-kn^2e^{-kn^2t}\sin(nx)$. It is a temperature profile along a rod whose ends at $x=0$ and $x=\pi$ are kept at $0$; it dies away faster for larger $n$.

:::
