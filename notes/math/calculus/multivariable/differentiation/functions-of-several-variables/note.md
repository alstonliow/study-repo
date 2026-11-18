---
title: "Functions of Several Variables, Graphs and Level Curves"
sources: [mit1802-8]
requires: [math/calculus/multivariable/vectors/lines-and-planes]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 8, in our own wording. -->

Multivariable calculus is about quantities that depend on several parameters, such as $w=f(x,y)$ or $w=f(x,y,z)$.

::: {#def-graph-level-curve .definition name="Graph, level curves, contour plot"}

Let $f$ be a function of two variables.

- Its **graph** is the surface $z=f(x,y)$ in space.
- For a constant $c$, the **level curve** $f(x,y)=c$ is the set of points of the plane where $f$ takes the value $c$; it is the horizontal slice $z=c$ of the graph, seen from above.
- A **contour plot** draws level curves for equally spaced values of $c$.

For $w=f(x,y,z)$ the sets $f(x,y,z)=c$ are **level surfaces**.

:::

A topographic map (height) and a weather map (temperature) are contour plots. Where the level curves are close together, $f$ changes quickly.

::: {#exm-graphs-by-slices .example name="Drawing graphs by slices"}

- $z=-y$: every slice $x=\text{const}$ is the same line of slope $-1$, so the graph is a plane through the $x$-axis; the level curves are the horizontal lines $y=-c$.
- $z=1-x^2-y^2$: the slices $x=0$ and $y=0$ are downward parabolas, and the level curves $x^2+y^2=1-c$ are circles ($c\le1$). The graph is a paraboloid with top at $(0,0,1)$.
- $z=x^2+y^2$ (level curves circles) has a bowl-shaped graph; $z=y^2-x^2$ (level curves hyperbolas $y^2-x^2=c$, and the two lines $y=\pm x$ for $c=0$) has a saddle-shaped graph.

:::

::: {#fig-functions-of-several-variables-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
\draw[->, faint] (-2.3,0) -- (2.5,0) node[lab, right] {$x$};
\draw[->, faint] (0,-2.3) -- (0,2.5) node[lab, above] {$y$};
\draw[emph, domain=-1.9:1.9, samples=40] plot (\x,{sqrt(\x*\x+0.5)});
\draw[emph, domain=-1.9:1.9, samples=40] plot (\x,{-sqrt(\x*\x+0.5)});
\draw[hl, domain=-1.9:1.9, samples=40] plot ({sqrt(\x*\x+0.5)},\x);
\draw[hl, domain=-1.9:1.9, samples=40] plot ({-sqrt(\x*\x+0.5)},\x);
\draw[emph, domain=-1.9:1.9, samples=40] plot (\x,{sqrt(\x*\x+1.5)});
\draw[emph, domain=-1.9:1.9, samples=40] plot (\x,{-sqrt(\x*\x+1.5)});
\draw[hl, domain=-1.9:1.9, samples=40] plot ({sqrt(\x*\x+1.5)},\x);
\draw[hl, domain=-1.9:1.9, samples=40] plot ({-sqrt(\x*\x+1.5)},\x);
\draw[emph, domain=-1.9:1.9, samples=40] plot (\x,{sqrt(\x*\x+2.5)});
\draw[emph, domain=-1.9:1.9, samples=40] plot (\x,{-sqrt(\x*\x+2.5)});
\draw[hl, domain=-1.9:1.9, samples=40] plot ({sqrt(\x*\x+2.5)},\x);
\draw[hl, domain=-1.9:1.9, samples=40] plot ({-sqrt(\x*\x+2.5)},\x);
\draw[faint, dashed] (-2,-2) -- (2,2); \draw[faint, dashed] (-2,2) -- (2,-2);
\node[lab] at (0.45,1.95) {$c>0$}; \node[lab] at (2.1,0.35) {$c<0$};
\end{tikzpicture}
\end{center}
```

Level curves $y^2-x^2=c$ of the saddle $z=y^2-x^2$ for $c=\pm0.5,\pm1.5,\pm2.5$: hyperbolas opening up and down for $c>0$, left and right for $c<0$; the dashed lines $y=\pm x$ are the level curve $c=0$.

:::

::: {#rmk-functions-of-several-variables-1 .remark name="Reading a contour plot"}

Moving across a contour plot tells how $f$ changes with the variables: if moving to the right crosses the level curves towards higher values, $f$ increases with $x$ there. Partial derivatives (@sec-math-calculus-multivariable-differentiation-partial-derivatives) make this quantitative.

:::
