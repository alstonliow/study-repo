---
title: "Curve Sketching"
sources: [mit1801-10]
requires: [math/calculus/single-variable/differentiation/exponentials-and-logarithms]
aliases: [math/calculus/applications-of-derivatives/curve-sketching]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-18 from MIT 18.01 (Fall 2006), Lecture 10, in our own wording. Monotonicity and concavity tests are proved in the mean value theorem note. -->

::: {#def-critical-point .definition name="Critical point, inflection point"}

$x_0$ is a critical point of $f$ if $f'(x_0)=0$; then $f(x_0)$ is a critical value. An inflection point is a point where $f''$ changes sign, i.e. where the graph changes from concave up ($f''>0$) to concave down ($f''<0$) or back.

:::

::: {#prp-sign-tests .proposition name="What the signs of $f'$ and $f''$ say"}

On an interval: if $f'>0$ then $f$ is increasing, and if $f'<0$ it is decreasing; if $f''>0$ the graph is concave up (slope increasing), and if $f''<0$ it is concave down.

:::

These follow from the mean value theorem; the proof is in the note on that theorem. At a critical point, $f'$ changing from $+$ to $-$ gives a local maximum and from $-$ to $+$ a local minimum. If $f''(x_0)>0$ at a critical point the point is a local minimum, and if $f''(x_0)<0$ a local maximum (second derivative test).

::: {#def-curve-sketching-plan .definition name="A plan for sketching $y=f(x)$"}

1. Plot discontinuities, especially infinite ones, and the behaviour as $x\to\pm\infty$.
2. Solve $f'(x)=0$; plot critical points and values.
3. Decide the sign of $f'$ on each interval between critical points and discontinuities (increasing or decreasing).
4. Find where $f''$ changes sign: concavity and inflection points.
5. Plot a few easy values (intercepts, symmetry) if it is quick.

:::

::: {#exm-sketch-cubic .example name="A cubic"}

$y=3x-x^3$ is odd. $y'=3-3x^2=0$ at $x=\pm1$, with values $\mp2$. $y'<0$ for $\lvert x\rvert>1$ and $y'>0$ for $\lvert x\rvert<1$, so $(-1,-2)$ is a local minimum and $(1,2)$ a local maximum. $y''=-6x$: concave up for $x<0$, down for $x>0$, inflection at the origin. As $x\to\pm\infty$, $y\to\mp\infty$.

:::

::: {#fig-curve-sketching-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.4,0) -- (2.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-2.6) -- (0,2.8) node[lab, above] {$y$};
\draw[emph, domain=-2.15:2.15, samples=80] plot (\x,{3*\x-\x*\x*\x});
\fill (1,2) circle (1.5pt) node[lab, above] {$(1,2)$ max};
\fill (-1,-2) circle (1.5pt) node[lab, below] {$(-1,-2)$ min};
\fill (0,0) circle (1.5pt) node[lab, below right] {inflection};
\end{tikzpicture}
\end{center}
```

$y=3x-x^3$: local minimum at $(-1,-2)$, local maximum at $(1,2)$, inflection point at the origin.

:::

::: {#exm-sketch-rational .example name="A rational function"}

$y=\dfrac{x+1}{x+2}$ has an infinite discontinuity at $x=-2$ ($y\to-\infty$ from the right, $+\infty$ from the left) and $y\to1$ as $x\to\pm\infty$. $y'=\dfrac1{(x+2)^2}>0$, so there are no critical points and the function increases on each side of $-2$. $y''=-\dfrac2{(x+2)^3}$: concave up for $x<-2$ and down for $x>-2$, but there is no inflection point, since $-2$ is not in the domain.

:::

::: {#exm-sketch-log .example name="$x/\ln x$"}

On $x>1$, $y=x/\ln x$ has $y'=\dfrac{\ln x-1}{(\ln x)^2}$, zero at $x=e$, with $y(e)=e$: a minimum, since $y\to\infty$ both as $x\to1^+$ and as $x\to\infty$.

:::
