---
title: "Double Integrals in Polar Coordinates"
sources: [mit1802-17, mit1802n-I]
requires: [math/calculus/multivariable/multiple-integrals/double-integrals, math/calculus/single-variable/applications-of-integrals/polar-coordinates]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 17 and Supplementary Notes I.2, in our own wording. Numbers checked in Python (sympy). -->

Polar coordinates $x=r\cos\theta$, $y=r\sin\theta$ (@def-polar-coordinates) help when the region or the integrand is simpler in $r$ and $\theta$, typically when it involves $x^2+y^2=r^2$.

::: {#fig-polar-double-integrals-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (3.3,0) node[lab, right] {$x$}; \draw[->, faint] (0,-0.3) -- (0,3.3) node[lab, above] {$y$};
\fill[tintA] (30:2) arc (30:45:2) -- (45:2.6) arc (45:30:2.6) -- cycle;
\draw[emph] (30:2) arc (30:45:2) -- (45:2.6) arc (45:30:2.6) -- cycle;
\draw[faint] (0,0) -- (30:2); \draw[faint] (0,0) -- (45:2);
\node[lab] at (37.5:3) {$\Delta A\approx r\,\Delta r\,\Delta\theta$};
\draw[faint] (30:0.7) arc (30:45:0.7) node[lab, right] at (37.5:0.7) {$\Delta\theta$};
\end{tikzpicture}
\end{center}
```

The polar area element is almost a rectangle with sides $\Delta r$ and $r\,\Delta\theta$.

:::

::: {#thm-polar-area-element .theorem name="Area element in polar coordinates"}

$$dA=r\,dr\,d\theta,\qquad\text{so}\qquad\iint_Rf\,dA=\iint_Rf(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta .$$

:::

::: {.proof}

1. The small region $r\le r'\le r+\Delta r$, $\theta\le\theta'\le\theta+\Delta\theta$ is nearly a rectangle with sides $\Delta r$ (radial) and $r\Delta\theta$ (an arc of the circle of radius $r$).

2. So $\Delta A\approx r\,\Delta r\,\Delta\theta$, and the sums defining the integral become sums of $f\,r\,\Delta r\,\Delta\theta$. (Exactly: the region is the difference of two sectors, of area $\frac12\big((r+\Delta r)^2-r^2\big)\Delta\theta=(r+\frac12\Delta r)\Delta r\Delta\theta$.)

:::

To set up the limits for $dr\,d\theta$: fix $\theta$ and follow the ray from the origin at angle $\theta$; it enters $R$ at $r_1(\theta)$ and leaves at $r_2(\theta)$. Then let $\theta$ run over the angles of the rays that meet $R$.

::: {#exm-polar-quarter-disk .example name="The quarter disk again"}

For @exm-double-integral-quarter-disk: $0\le r\le1$, $0\le\theta\le\pi/2$, and
$$\int_0^{\pi/2}\!\!\int_0^1(1-r^2)\,r\,dr\,d\theta=\int_0^{\pi/2}\Big[\frac{r^2}2-\frac{r^4}4\Big]_0^1d\theta=\frac\pi2\cdot\frac14=\frac\pi8 .$$

:::

::: {#fig-polar-double-integrals-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=2]
\draw[->, faint] (-0.2,0) -- (1.4,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,1.4) node[lab, above] {$y$};
\draw[faint] (0.25,0) arc[start angle=0, end angle=90, radius=0.25];
\draw[faint] (0.5,0) arc[start angle=0, end angle=90, radius=0.5];
\draw[faint] (0.75,0) arc[start angle=0, end angle=90, radius=0.75];
\draw[faint] (1.0,0) arc[start angle=0, end angle=90, radius=1.0];
\draw[faint] (0,0) -- (1,0);
\draw[faint] (0,0) -- (0.92,0.38);
\draw[faint] (0,0) -- (0.71,0.71);
\draw[faint] (0,0) -- (0.38,0.92);
\draw[faint] (0,0) -- (0,1);
\fill[accentLight] (0.46,0.19) arc[start angle=22.5, end angle=45, radius=0.5] -- (0.53,0.53) arc[start angle=45, end angle=22.5, radius=0.75] -- cycle;
\draw[emph] (1,0) arc[start angle=0, end angle=90, radius=1];
\end{tikzpicture}
\end{center}
```

The quarter disk in polar coordinates is the rectangle $0\le r\le1$, $0\le\theta\le\pi/2$: the limits are constants, and each polar element (one shaded) has area about $r\,\Delta r\,\Delta\theta$.

:::

::: {#exm-gaussian-integral .example name="The bell-curve integral"}

Let $I=\int_{-\infty}^\infty e^{-x^2}dx$. Then
$$I^2=\iint_{\mathbb{R}^2}e^{-x^2-y^2}\,dA=\int_0^{2\pi}\!\!\int_0^\infty e^{-r^2}r\,dr\,d\theta=2\pi\cdot\frac12=\pi,$$
so $I=\sqrt\pi$. (The improper double integral is the limit over larger and larger disks.)

:::

::: {#fig-polar-double-integrals-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (2.4,0) node[lab, right] {$x$};
\draw[->, faint] (0,-2.2) -- (0,2.4) node[lab, above] {$y$};
\fill[tintA] (1.84,0) -- (1.83,0.16) -- (1.81,0.32) -- (1.78,0.48) -- (1.73,0.63) -- (1.67,0.78) -- (1.59,0.92) -- (1.51,1.05) -- (1.41,1.18) -- (1.3,1.3) -- (1.18,1.41) -- (1.05,1.51) -- (0.92,1.59) -- (0.78,1.67) -- (0.63,1.73) -- (0.48,1.78) -- (0.32,1.81) -- (0.16,1.83) -- (0,1.84) -- (-0.16,1.83) -- (-0.32,1.81) -- (-0.48,1.78) -- (-0.63,1.73) -- (-0.78,1.67) -- (-0.92,1.59) -- (-1.05,1.51) -- (-1.18,1.41) -- (-1.3,1.3) -- (-1.41,1.18) -- (-1.51,1.05) -- (-1.59,0.92) -- (-1.67,0.78) -- (-1.73,0.63) -- (-1.78,0.48) -- (-1.81,0.32) -- (-1.83,0.16) -- (-1.84,0) -- (-1.83,-0.16) -- (-1.81,-0.32) -- (-1.78,-0.48) -- (-1.73,-0.63) -- (-1.67,-0.78) -- (-1.59,-0.92) -- (-1.51,-1.05) -- (-1.41,-1.18) -- (-1.3,-1.3) -- (-1.18,-1.41) -- (-1.05,-1.51) -- (-0.92,-1.59) -- (-0.78,-1.67) -- (-0.63,-1.73) -- (-0.48,-1.78) -- (-0.32,-1.81) -- (-0.16,-1.83) -- (0,-1.84) -- (0.16,-1.83) -- (0.32,-1.81) -- (0.48,-1.78) -- (0.63,-1.73) -- (0.78,-1.67) -- (0.92,-1.59) -- (1.05,-1.51) -- (1.18,-1.41) -- (1.3,-1.3) -- (1.41,-1.18) -- (1.51,-1.05) -- (1.59,-0.92) -- (1.67,-0.78) -- (1.73,-0.63) -- (1.78,-0.48) -- (1.81,-0.32) -- (1.83,-0.16) -- cycle;
\fill[tintC] (-1.3,-1.3) -- (1.3,-1.3) -- (1.3,1.3) -- (-1.3,1.3) -- cycle;
\fill[tintB] (1.3,0) -- (1.3,0.11) -- (1.28,0.23) -- (1.26,0.34) -- (1.22,0.44) -- (1.18,0.55) -- (1.13,0.65) -- (1.06,0.75) -- (1,0.84) -- (0.92,0.92) -- (0.84,1) -- (0.75,1.06) -- (0.65,1.13) -- (0.55,1.18) -- (0.44,1.22) -- (0.34,1.26) -- (0.23,1.28) -- (0.11,1.3) -- (0,1.3) -- (-0.11,1.3) -- (-0.23,1.28) -- (-0.34,1.26) -- (-0.44,1.22) -- (-0.55,1.18) -- (-0.65,1.13) -- (-0.75,1.06) -- (-0.84,1) -- (-0.92,0.92) -- (-1,0.84) -- (-1.06,0.75) -- (-1.13,0.65) -- (-1.18,0.55) -- (-1.22,0.44) -- (-1.26,0.34) -- (-1.28,0.23) -- (-1.3,0.11) -- (-1.3,0) -- (-1.3,-0.11) -- (-1.28,-0.23) -- (-1.26,-0.34) -- (-1.22,-0.44) -- (-1.18,-0.55) -- (-1.13,-0.65) -- (-1.06,-0.75) -- (-1,-0.84) -- (-0.92,-0.92) -- (-0.84,-1) -- (-0.75,-1.06) -- (-0.65,-1.13) -- (-0.55,-1.18) -- (-0.44,-1.22) -- (-0.34,-1.26) -- (-0.23,-1.28) -- (-0.11,-1.3) -- (0,-1.3) -- (0.11,-1.3) -- (0.23,-1.28) -- (0.34,-1.26) -- (0.44,-1.22) -- (0.55,-1.18) -- (0.65,-1.13) -- (0.75,-1.06) -- (0.84,-1) -- (0.92,-0.92) -- (1,-0.84) -- (1.06,-0.75) -- (1.13,-0.65) -- (1.18,-0.55) -- (1.22,-0.44) -- (1.26,-0.34) -- (1.28,-0.23) -- (1.3,-0.11) -- cycle;
\draw[faint] (1.84,0) -- (1.83,0.16) -- (1.81,0.32) -- (1.78,0.48) -- (1.73,0.63) -- (1.67,0.78) -- (1.59,0.92) -- (1.51,1.05) -- (1.41,1.18) -- (1.3,1.3) -- (1.18,1.41) -- (1.05,1.51) -- (0.92,1.59) -- (0.78,1.67) -- (0.63,1.73) -- (0.48,1.78) -- (0.32,1.81) -- (0.16,1.83) -- (0,1.84) -- (-0.16,1.83) -- (-0.32,1.81) -- (-0.48,1.78) -- (-0.63,1.73) -- (-0.78,1.67) -- (-0.92,1.59) -- (-1.05,1.51) -- (-1.18,1.41) -- (-1.3,1.3) -- (-1.41,1.18) -- (-1.51,1.05) -- (-1.59,0.92) -- (-1.67,0.78) -- (-1.73,0.63) -- (-1.78,0.48) -- (-1.81,0.32) -- (-1.83,0.16) -- (-1.84,0) -- (-1.83,-0.16) -- (-1.81,-0.32) -- (-1.78,-0.48) -- (-1.73,-0.63) -- (-1.67,-0.78) -- (-1.59,-0.92) -- (-1.51,-1.05) -- (-1.41,-1.18) -- (-1.3,-1.3) -- (-1.18,-1.41) -- (-1.05,-1.51) -- (-0.92,-1.59) -- (-0.78,-1.67) -- (-0.63,-1.73) -- (-0.48,-1.78) -- (-0.32,-1.81) -- (-0.16,-1.83) -- (0,-1.84) -- (0.16,-1.83) -- (0.32,-1.81) -- (0.48,-1.78) -- (0.63,-1.73) -- (0.78,-1.67) -- (0.92,-1.59) -- (1.05,-1.51) -- (1.18,-1.41) -- (1.3,-1.3) -- (1.41,-1.18) -- (1.51,-1.05) -- (1.59,-0.92) -- (1.67,-0.78) -- (1.73,-0.63) -- (1.78,-0.48) -- (1.81,-0.32) -- (1.83,-0.16) -- cycle;
\draw[emph] (-1.3,-1.3) -- (1.3,-1.3) -- (1.3,1.3) -- (-1.3,1.3) -- cycle;
\draw[faint] (1.3,0) -- (1.3,0.11) -- (1.28,0.23) -- (1.26,0.34) -- (1.22,0.44) -- (1.18,0.55) -- (1.13,0.65) -- (1.06,0.75) -- (1,0.84) -- (0.92,0.92) -- (0.84,1) -- (0.75,1.06) -- (0.65,1.13) -- (0.55,1.18) -- (0.44,1.22) -- (0.34,1.26) -- (0.23,1.28) -- (0.11,1.3) -- (0,1.3) -- (-0.11,1.3) -- (-0.23,1.28) -- (-0.34,1.26) -- (-0.44,1.22) -- (-0.55,1.18) -- (-0.65,1.13) -- (-0.75,1.06) -- (-0.84,1) -- (-0.92,0.92) -- (-1,0.84) -- (-1.06,0.75) -- (-1.13,0.65) -- (-1.18,0.55) -- (-1.22,0.44) -- (-1.26,0.34) -- (-1.28,0.23) -- (-1.3,0.11) -- (-1.3,0) -- (-1.3,-0.11) -- (-1.28,-0.23) -- (-1.26,-0.34) -- (-1.22,-0.44) -- (-1.18,-0.55) -- (-1.13,-0.65) -- (-1.06,-0.75) -- (-1,-0.84) -- (-0.92,-0.92) -- (-0.84,-1) -- (-0.75,-1.06) -- (-0.65,-1.13) -- (-0.55,-1.18) -- (-0.44,-1.22) -- (-0.34,-1.26) -- (-0.23,-1.28) -- (-0.11,-1.3) -- (0,-1.3) -- (0.11,-1.3) -- (0.23,-1.28) -- (0.34,-1.26) -- (0.44,-1.22) -- (0.55,-1.18) -- (0.65,-1.13) -- (0.75,-1.06) -- (0.84,-1) -- (0.92,-0.92) -- (1,-0.84) -- (1.06,-0.75) -- (1.13,-0.65) -- (1.18,-0.55) -- (1.22,-0.44) -- (1.26,-0.34) -- (1.28,-0.23) -- (1.3,-0.11) -- cycle;
\node[lab, right] at (1.4,-0.25) {$R$};
\node[lab, right] at (1.3,1.6) {$R\sqrt2$};
\end{tikzpicture}
\end{center}
```

Squeezing the square: the integral of $e^{-x^2-y^2}$ over the square $[-R,R]^2$, which is $\big(\int_{-R}^Re^{-x^2}dx\big)^2$, lies between its integrals over the inner and outer discs, $\pi(1-e^{-R^2})$ and $\pi(1-e^{-2R^2})$. Both tend to $\pi$, so $\int_{-\infty}^\infty e^{-x^2}dx=\sqrt\pi$.

:::
