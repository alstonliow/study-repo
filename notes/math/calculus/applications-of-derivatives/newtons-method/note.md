---
title: "Newton's Method"
sources: [mit1801-13]
requires: [math/calculus/applications-of-derivatives/linear-and-quadratic-approximation]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 13, in our own wording. Numbers checked in Python. -->

::: {#def-newtons-method .definition name="Newton's method"}

To solve $f(x)=0$, start from a guess $x_0$ and repeat
$$x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)} .$$
Each step replaces $f$ by its tangent line at $x_k$ (@def-linear-approximation) and takes the tangent line's root.

:::

::: {#fig-newtons-method-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[xscale=1.8]
\draw[->, faint] (-0.2,0) -- (3.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.4) -- (0,2.8) node[lab, above] {$y$};
\draw[emph, domain=0.3:3.3, samples=60] plot (\x,{0.4*(\x*\x-3)});
\draw[faint, dashed] (3.0,0) -- (3.0,2.40);
\draw[hl] (3.0,2.40) -- (2.0,0);
\fill (3.0,0) circle (1.3pt) node[lab, below] {$x_0$};
\draw[faint, dashed] (2.0,0) -- (2.0,0.4);
\draw[hl] (2.0,0.4) -- (1.75,0);
\fill (2.0,0) circle (1.3pt) node[lab, below] {$x_1$};
\fill (1.75,0) circle (1.3pt) node[lab, below left] {$x_2$};
\draw[faint, dashed] (1.75,0) -- (1.75,0.025);
\end{tikzpicture}
\end{center}
```

Newton's method for $x^2-3=0$ from $x_0=3$: each tangent line meets the axis at the next point, $x_1=2$, $x_2=1.75$, already close to $\sqrt3\approx1.732$ (vertical scale compressed).

:::

::: {#exm-newton-square-root .example name="Square root of 3"}

For $f(x)=x^2-3$ the step is $x_{k+1}=x_k-\dfrac{x_k^2-3}{2x_k}=\dfrac12\Big(x_k+\dfrac3{x_k}\Big)$. From $x_0=1$: $x_1=2$, $x_2=1.75$, $x_3=1.732142\ldots$, $x_4=1.7320508100\ldots$, against $\sqrt3=1.7320508075\ldots$ The errors are about $0.27$, $0.018$, $9\times10^{-5}$, $2.5\times10^{-9}$.

:::

::: {#thm-newton-quadratic-convergence .theorem name="Quadratic convergence"}

Let $f(r)=0$, with $f''$ continuous near $r$ and $f'(r)\neq0$. If $x_0$ is close enough to $r$, the errors $E_k=\lvert x_k-r\rvert$ satisfy $E_{k+1}\le C E_k^2$ for a constant $C$: the number of correct digits roughly doubles at each step.

:::

::: {.proof}

1. By the quadratic approximation with remainder (Taylor's formula), $0=f(r)=f(x_k)+f'(x_k)(r-x_k)+\tfrac12f''(\xi)(r-x_k)^2$ for some $\xi$ between $x_k$ and $r$.

2. Divide by $f'(x_k)$ and use $x_{k+1}=x_k-f(x_k)/f'(x_k)$: $r-x_{k+1}=-\dfrac{f''(\xi)}{2f'(x_k)}(r-x_k)^2$.

3. Near $r$, $\lvert f''\rvert\le M$ and $\lvert f'\rvert\ge m>0$, so $E_{k+1}\le\dfrac{M}{2m}E_k^2$. If $E_0<2m/M$ the errors decrease and the bound holds at every step.

:::

::: {#rmk-newton-failures .remark name="When it fails"}

The method can fail if $f'(x_k)$ is $0$ or tiny (the tangent is flat and $x_{k+1}$ flies away), if the start is far from the root (it may converge to another root, or cycle), or if $f'(r)=0$ (convergence slows to linear). For $f(x)=x^{1/3}$ every step doubles the distance: $x_{k+1}=-2x_k$.

:::
