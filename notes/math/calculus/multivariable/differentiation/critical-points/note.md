---
title: "Critical Points and the Second Derivative Test"
sources: [mit1802-9, mit1802-10, mit1802n-SD]
requires: [math/calculus/multivariable/differentiation/partial-derivatives, math/calculus/single-variable/applications-of-derivatives/optimization]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 9-10 and Supplementary Notes SD, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-critical-point-two-variables .definition name="Critical point"}

A point $(x_0,y_0)$ is a **critical point** of $f(x,y)$ if $f_x(x_0,y_0)=0$ and $f_y(x_0,y_0)=0$, i.e. the tangent plane there is horizontal.

:::

::: {#prp-local-extremum-critical .proposition name="Local extrema are critical points"}

If $f$ has a local maximum or minimum at an interior point $(x_0,y_0)$ where $f_x,f_y$ exist, then $(x_0,y_0)$ is a critical point.

:::

::: {.proof}

1. The one-variable function $g(x)=f(x,y_0)$ has a local extremum at $x_0$, so $g'(x_0)=f_x(x_0,y_0)=0$.

2. In the same way $h(y)=f(x_0,y)$ gives $f_y(x_0,y_0)=0$.

:::

A critical point may be a local minimum ($w=x^2+y^2$ at the origin), a local maximum ($w=-x^2-y^2$) or a **saddle point** ($w=y^2-x^2$), where $f$ increases in some directions and decreases in others.

::: {#exm-critical-point-completing-square .example name="Completing the square"}

$f=x^2-2xy+3y^2+2x-2y$ has $f_x=2x-2y+2$, $f_y=-2x+6y-2$, whose only common zero is $(-1,0)$. Since
$$f=(x-y+1)^2+2y^2-1\ \ge\ -1=f(-1,0),$$
the critical point is a minimum (in fact the global minimum).

:::

::: {#thm-quadratic-form-two-variables .theorem name="Quadratic functions"}

Let $w=ax^2+bxy+cy^2$, whose only critical point is $(0,0)$ when $4ac-b^2\ne0$.

1. If $4ac-b^2>0$: a minimum if $a>0$, a maximum if $a<0$.
2. If $4ac-b^2<0$: a saddle.
3. If $4ac-b^2=0$: degenerate (the graph is a trough along a line).

:::

::: {.proof}

1. If $a\ne0$, complete the square:
$$w=a\Big(x+\frac b{2a}y\Big)^2+\Big(c-\frac{b^2}{4a}\Big)y^2=\frac1{4a}\Big(4a^2\Big(x+\frac b{2a}y\Big)^2+(4ac-b^2)y^2\Big).$$

2. If $4ac-b^2>0$ the bracket is a sum of two squares with positive coefficients, positive except at the origin; so $w$ has the sign of $a$ away from $0$.

3. If $4ac-b^2<0$ the bracket is positive on the line $y=0$ ($x\ne0$) and negative on the line $x=-\frac b{2a}y$ ($y\ne0$): $w$ takes both signs, a saddle.

4. If $4ac-b^2=0$, $w=a(x+\frac b{2a}y)^2$ vanishes on a whole line. If $a=0$ but $c\ne0$, exchange $x$ and $y$; if $a=c=0$ then $w=bxy$, a saddle when $b\ne0$, and $4ac-b^2=-b^2<0$ agrees.

:::

::: {#fig-critical-points-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r in {0.4,0.8,1.2} \draw[emph] (0,0) circle (\r);
\fill[ink] (0,0) circle[pt]; \node[lab] at (0,-1.6) {minimum: $x^2+y^2$};
\begin{scope}[xshift=4cm]
\foreach \c in {0.3,0.9} {\draw[emph, domain=-1:1, samples=30] plot ({sqrt(\c+\x*\x)},\x); \draw[emph, domain=-1:1, samples=30] plot ({-sqrt(\c+\x*\x)},\x);
\draw[hl, domain=-1:1, samples=30] plot (\x,{sqrt(\c+\x*\x)}); \draw[hl, domain=-1:1, samples=30] plot (\x,{-sqrt(\c+\x*\x)});}
\fill[ink] (0,0) circle[pt]; \node[lab] at (0,-1.6) {saddle: $x^2-y^2$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Level curves near a critical point: closed ovals around a minimum, hyperbolas through a saddle (positive levels solid, negative levels highlighted).

:::

<!-- Merged 2026-11-20 (owner): the block thm-second-derivative-test-two-variables (with a sketched proof) was removed in favour of thm-second-derivative-test-several in math/analysis/differentiation/second-derivatives, which keeps its AC-B^2 form as part 4 and its x^4 +- y^4 examples. -->

**Second derivative test.** Let $(x_0,y_0)$ be a critical point of $f$, whose second partial derivatives are continuous, and put
$$A=f_{xx}(x_0,y_0),\qquad B=f_{xy}(x_0,y_0),\qquad C=f_{yy}(x_0,y_0).$$
If $AC-B^2>0$ and $A>0$ there is a local minimum; if $AC-B^2>0$ and $A<0$ a local maximum; if $AC-B^2<0$ a saddle point; if $AC-B^2=0$ the test gives no conclusion. The quadratic approximation $\Delta f\approx\frac12A\Delta x^2+B\Delta x\Delta y+\frac12C\Delta y^2$ is the quadratic function of @thm-quadratic-form-two-variables with $4ac-b^2=AC-B^2$; that it decides the behaviour of $f$ is proved, for any number of variables, in @thm-second-derivative-test-several.


::: {#exm-second-derivative-test .example name="Minimum on the open quadrant"}

$f=x+y+\dfrac1{xy}$ for $x,y>0$. $f_x=1-\dfrac1{x^2y}$ and $f_y=1-\dfrac1{xy^2}$ vanish when $x^2y=xy^2=1$, i.e. only at $(1,1)$. There $A=\dfrac2{x^3y}=2$, $B=\dfrac1{x^2y^2}=1$, $C=\dfrac2{xy^3}=2$, so $AC-B^2=3>0$, $A>0$: a local minimum, $f(1,1)=3$.

:::

::: {#rmk-critical-points-1 .remark name="Global extrema: check the boundary"}

The largest and smallest values of $f$ on a region may occur at critical points, on the boundary of the region, or "at infinity". In @exm-second-derivative-test, $f\to\infty$ as $x\to0^+$, $y\to0^+$ or $x+y\to\infty$; so $3$ is the global minimum and there is no maximum.

:::
