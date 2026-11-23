---
title: "Differentials and the Chain Rule"
sources: [mit1802-11]
requires: [math/calculus/multivariable/differentiation/partial-derivatives]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 11, in our own wording. Numbers checked in Python (sympy). -->

::: {#def-total-differential .definition name="Total differential"}

For $w=f(x,y,z)$ the **total differential** is
$$dw=f_x\,dx+f_y\,dy+f_z\,dz .$$

:::

::: {#fig-differentials-and-chain-rule-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,2.6) node[lab, above] {$y$};
\draw[faint] (0.42,2.4) -- (0.46,2.18) -- (0.5,1.99) -- (0.55,1.83) -- (0.59,1.7) -- (0.63,1.58) -- (0.68,1.48) -- (0.72,1.39) -- (0.76,1.31) -- (0.8,1.24) -- (0.85,1.18) -- (0.89,1.12) -- (0.93,1.07) -- (0.98,1.02) -- (1.02,0.98) -- (1.06,0.94) -- (1.11,0.9) -- (1.15,0.87) -- (1.19,0.84) -- (1.23,0.81) -- (1.28,0.78) -- (1.32,0.76) -- (1.36,0.73) -- (1.41,0.71) -- (1.45,0.69) -- (1.49,0.67) -- (1.54,0.65) -- (1.58,0.63) -- (1.62,0.62) -- (1.67,0.6) -- (1.71,0.59) -- (1.75,0.57) -- (1.79,0.56) -- (1.84,0.54) -- (1.88,0.53) -- (1.92,0.52) -- (1.97,0.51) -- (2.01,0.5) -- (2.05,0.49) -- (2.1,0.48) -- (2.14,0.47) -- (2.18,0.46) -- (2.23,0.45) -- (2.27,0.44) -- (2.31,0.43) -- (2.35,0.42) -- (2.4,0.42) -- (2.44,0.41) -- (2.48,0.4) -- (2.53,0.4) -- (2.57,0.39) -- (2.61,0.38) -- (2.66,0.38) -- (2.7,0.37) -- (2.74,0.36) -- (2.78,0.36) -- (2.83,0.35) -- (2.87,0.35) -- (2.91,0.34) -- (2.96,0.34) -- (3,0.33);
\draw[faint] (0.83,2.4) -- (0.87,2.3) -- (0.91,2.21) -- (0.94,2.12) -- (0.98,2.05) -- (1.01,1.97) -- (1.05,1.9) -- (1.09,1.84) -- (1.12,1.78) -- (1.16,1.73) -- (1.19,1.67) -- (1.23,1.63) -- (1.27,1.58) -- (1.3,1.54) -- (1.34,1.49) -- (1.38,1.45) -- (1.41,1.42) -- (1.45,1.38) -- (1.48,1.35) -- (1.52,1.32) -- (1.56,1.29) -- (1.59,1.26) -- (1.63,1.23) -- (1.66,1.2) -- (1.7,1.18) -- (1.74,1.15) -- (1.77,1.13) -- (1.81,1.11) -- (1.84,1.08) -- (1.88,1.06) -- (1.92,1.04) -- (1.95,1.02) -- (1.99,1.01) -- (2.02,0.99) -- (2.06,0.97) -- (2.1,0.95) -- (2.13,0.94) -- (2.17,0.92) -- (2.21,0.91) -- (2.24,0.89) -- (2.28,0.88) -- (2.31,0.86) -- (2.35,0.85) -- (2.39,0.84) -- (2.42,0.83) -- (2.46,0.81) -- (2.49,0.8) -- (2.53,0.79) -- (2.57,0.78) -- (2.6,0.77) -- (2.64,0.76) -- (2.67,0.75) -- (2.71,0.74) -- (2.75,0.73) -- (2.78,0.72) -- (2.82,0.71) -- (2.86,0.7) -- (2.89,0.69) -- (2.93,0.68) -- (2.96,0.67) -- (3,0.67);
\draw[faint] (1.25,2.4) -- (1.28,2.35) -- (1.31,2.29) -- (1.34,2.24) -- (1.37,2.2) -- (1.4,2.15) -- (1.43,2.11) -- (1.45,2.06) -- (1.48,2.02) -- (1.51,1.98) -- (1.54,1.95) -- (1.57,1.91) -- (1.6,1.88) -- (1.63,1.84) -- (1.66,1.81) -- (1.69,1.78) -- (1.72,1.75) -- (1.75,1.72) -- (1.77,1.69) -- (1.8,1.66) -- (1.83,1.64) -- (1.86,1.61) -- (1.89,1.59) -- (1.92,1.56) -- (1.95,1.54) -- (1.98,1.52) -- (2.01,1.49) -- (2.04,1.47) -- (2.07,1.45) -- (2.1,1.43) -- (2.12,1.41) -- (2.15,1.39) -- (2.18,1.37) -- (2.21,1.36) -- (2.24,1.34) -- (2.27,1.32) -- (2.3,1.3) -- (2.33,1.29) -- (2.36,1.27) -- (2.39,1.26) -- (2.42,1.24) -- (2.45,1.23) -- (2.48,1.21) -- (2.5,1.2) -- (2.53,1.18) -- (2.56,1.17) -- (2.59,1.16) -- (2.62,1.14) -- (2.65,1.13) -- (2.68,1.12) -- (2.71,1.11) -- (2.74,1.1) -- (2.77,1.08) -- (2.8,1.07) -- (2.83,1.06) -- (2.85,1.05) -- (2.88,1.04) -- (2.91,1.03) -- (2.94,1.02) -- (2.97,1.01) -- (3,1);
\draw[faint] (1.67,2.4) -- (1.69,2.37) -- (1.71,2.34) -- (1.73,2.31) -- (1.76,2.28) -- (1.78,2.25) -- (1.8,2.22) -- (1.82,2.2) -- (1.84,2.17) -- (1.87,2.14) -- (1.89,2.12) -- (1.91,2.09) -- (1.93,2.07) -- (1.96,2.05) -- (1.98,2.02) -- (2,2) -- (2.02,1.98) -- (2.04,1.96) -- (2.07,1.94) -- (2.09,1.91) -- (2.11,1.89) -- (2.13,1.88) -- (2.16,1.86) -- (2.18,1.84) -- (2.2,1.82) -- (2.22,1.8) -- (2.24,1.78) -- (2.27,1.76) -- (2.29,1.75) -- (2.31,1.73) -- (2.33,1.71) -- (2.36,1.7) -- (2.38,1.68) -- (2.4,1.67) -- (2.42,1.65) -- (2.44,1.64) -- (2.47,1.62) -- (2.49,1.61) -- (2.51,1.59) -- (2.53,1.58) -- (2.56,1.57) -- (2.58,1.55) -- (2.6,1.54) -- (2.62,1.53) -- (2.64,1.51) -- (2.67,1.5) -- (2.69,1.49) -- (2.71,1.48) -- (2.73,1.46) -- (2.76,1.45) -- (2.78,1.44) -- (2.8,1.43) -- (2.82,1.42) -- (2.84,1.41) -- (2.87,1.4) -- (2.89,1.38) -- (2.91,1.37) -- (2.93,1.36) -- (2.96,1.35) -- (2.98,1.34) -- (3,1.33);
\draw[faint] (2.08,2.4) -- (2.1,2.38) -- (2.11,2.37) -- (2.13,2.35) -- (2.14,2.33) -- (2.16,2.32) -- (2.18,2.3) -- (2.19,2.28) -- (2.21,2.27) -- (2.22,2.25) -- (2.24,2.24) -- (2.25,2.22) -- (2.27,2.21) -- (2.28,2.19) -- (2.3,2.18) -- (2.31,2.16) -- (2.33,2.15) -- (2.34,2.13) -- (2.36,2.12) -- (2.37,2.11) -- (2.39,2.09) -- (2.4,2.08) -- (2.42,2.07) -- (2.43,2.05) -- (2.45,2.04) -- (2.47,2.03) -- (2.48,2.02) -- (2.5,2) -- (2.51,1.99) -- (2.53,1.98) -- (2.54,1.97) -- (2.56,1.96) -- (2.57,1.94) -- (2.59,1.93) -- (2.6,1.92) -- (2.62,1.91) -- (2.63,1.9) -- (2.65,1.89) -- (2.66,1.88) -- (2.68,1.87) -- (2.69,1.86) -- (2.71,1.85) -- (2.73,1.83) -- (2.74,1.82) -- (2.76,1.81) -- (2.77,1.8) -- (2.79,1.79) -- (2.8,1.78) -- (2.82,1.78) -- (2.83,1.77) -- (2.85,1.76) -- (2.86,1.75) -- (2.88,1.74) -- (2.89,1.73) -- (2.91,1.72) -- (2.92,1.71) -- (2.94,1.7) -- (2.95,1.69) -- (2.97,1.68) -- (2.98,1.68) -- (3,1.67);
\draw[->, hl] (1,1) -- (1.9,1) node[lab, midway, below] {$\Delta x$};
\draw[->, hl] (1.9,1) -- (1.9,1.7) node[lab, midway, right] {$\Delta y$};
\fill[ink] (1,1) circle[pt] node[lab, below left] {$P$};
\node[lab, right] at (2.9,0.42) {$f=1$};
\node[lab, right] at (2.9,1.7) {$f=5$};
\end{tikzpicture}
\end{center}
```

Level curves of $f=xy$. Going from $P$ by $\Delta x$ then by $\Delta y$ crosses level curves at rates $f_x$ and $f_y$, so $\Delta f\approx f_x\,\Delta x+f_y\,\Delta y$, the total differential.

:::

The differential $dw$ is not the same thing as the increment $\Delta w$. It is a formal expression recording how variations of $w$ are tied to variations of $x,y,z$, and it is used in two ways: as a template for the approximation $\Delta w\approx f_x\Delta x+f_y\Delta y+f_z\Delta z$ (@thm-continuous-partials-differentiable), and, divided by $dt$, as the chain rule.

<!-- Merged 2026-11-20 (owner): the block thm-multivariable-chain-rule (three variables, continuous partial derivatives, proof by increments) was removed in favour of thm-chain-rule-several-variables in math/analysis/differentiation/chain-rule-and-mean-value, which needs only differentiability. -->

**Chain rule.** If $w=f(x,y,z)$ has continuous partial derivatives (or is just differentiable) and $x,y,z$ are differentiable functions of $t$, then
$$\frac{dw}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}+f_z\frac{dz}{dt}.$$
This is @thm-chain-rule-several-variables for $t\mapsto(x,y,z)\mapsto w$: the derivative of the composite is the row $(f_x,f_y,f_z)$ times the column $(\frac{dx}{dt},\frac{dy}{dt},\frac{dz}{dt})$.

::: {#exm-chain-rule-check .example name="Checking against substitution"}

$w=x^2y+z$ with $x=t$, $y=e^t$, $z=\sin t$. The chain rule gives
$$\frac{dw}{dt}=2xy\cdot1+x^2\cdot e^t+1\cdot\cos t=2te^t+t^2e^t+\cos t,$$
the same as differentiating $w=t^2e^t+\sin t$ directly.

:::

::: {#exm-product-rule-from-chain-rule .example name="Product and quotient rules"}

With $f(u,v)=uv$ and $u,v$ functions of $t$, the chain rule gives $\frac{d}{dt}(uv)=f_uu'+f_vv'=vu'+uv'$. With $g(u,v)=u/v$, $g_u=1/v$ and $g_v=-u/v^2$ give $\frac{d}{dt}(u/v)=\frac{u'v-uv'}{v^2}$.

:::

::: {#thm-chain-rule-several-parameters .theorem name="Chain rule with several parameters"}

If $w=f(x,y)$ with $x=x(u,v)$ and $y=y(u,v)$, then
$$\frac{\partial w}{\partial u}=f_x\frac{\partial x}{\partial u}+f_y\frac{\partial y}{\partial u},\qquad
\frac{\partial w}{\partial v}=f_x\frac{\partial x}{\partial v}+f_y\frac{\partial y}{\partial v}.$$

:::

::: {.proof}

1. Hold $v$ fixed: then $x,y$ are functions of the single variable $u$, and @thm-chain-rule-several-variables gives the first formula. Holding $u$ fixed gives the second.

2. In the language of differentials: substitute $dx=x_u\,du+x_v\,dv$ and $dy=y_u\,du+y_v\,dv$ into $dw=f_x\,dx+f_y\,dy$ and read off the coefficients of $du$ and $dv$.

:::

::: {#fig-differentials-and-chain-rule-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (w) at (0,0) {$w$};
\node[box] (x) at (-1.6,-1.4) {$x$};
\node[box] (y) at (1.6,-1.4) {$y$};
\node[box] (u1) at (-2.4,-2.8) {$u$};
\node[box] (v1) at (-0.8,-2.8) {$v$};
\node[box] (u2) at (0.8,-2.8) {$u$};
\node[box] (v2) at (2.4,-2.8) {$v$};
\draw[hl] (w) -- node[edge label, left=2pt] {$f_x$} (x);
\draw[hl] (w) -- node[edge label, right=2pt] {$f_y$} (y);
\draw[hl] (x) -- node[edge label, left=2pt] {$\frac{\partial x}{\partial u}$} (u1);
\draw (x) -- (v1);
\draw[hl] (y) -- node[edge label, left=2pt] {$\frac{\partial y}{\partial u}$} (u2);
\draw (y) -- (v2);
\end{tikzpicture}
\end{center}
```

Dependency diagram for $w=f(x,y)$ with $x=x(u,v)$, $y=y(u,v)$. Each path from $w$ down to $u$ contributes the product of the derivatives along it; the two highlighted paths add up to $\partial w/\partial u=f_x\,\partial x/\partial u+f_y\,\partial y/\partial u$.

:::

The $\partial x$'s in these formulas may not be "cancelled": $\frac{\partial w}{\partial x}\frac{\partial x}{\partial u}$ alone is not $\frac{\partial w}{\partial u}$.

::: {#exm-chain-rule-polar .example name="Polar coordinates"}

With $x=r\cos\theta$, $y=r\sin\theta$:
$$f_r=f_x\cos\theta+f_y\sin\theta,\qquad f_\theta=-f_x\,r\sin\theta+f_y\,r\cos\theta .$$
For $f=x^2+y^2=r^2$ this gives $f_r=2x\cos\theta+2y\sin\theta=2r$ and $f_\theta=0$, as it should.

:::

::: {#fig-differentials-and-chain-rule-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.3,0) -- (2.8,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.3) -- (0,2.4) node[lab, above] {$y$};
\draw[faint] (0.6,0) arc[start angle=0, end angle=90, radius=0.6];
\draw[faint] (1.2,0) arc[start angle=0, end angle=90, radius=1.2];
\draw[faint] (1.8,0) arc[start angle=0, end angle=90, radius=1.8];
\draw[faint] (2.4,0) arc[start angle=0, end angle=90, radius=2.4];
\draw[faint] (0,0) -- (2.41,0.65);
\draw[faint] (0,0) -- (2.17,1.25);
\draw[faint] (0,0) -- (1.77,1.77);
\draw[faint] (0,0) -- (1.25,2.17);
\draw[faint] (0,0) -- (0.65,2.41);
\fill[accent] (1.31,0.92) circle[pt];
\draw[->, hl] (1.31,0.92) -- (1.8,1.26) node[lab, right] {$\partial/\partial r$};
\draw[->, hl] (1.31,0.92) -- (0.97,1.41) node[lab, above] {$\partial/\partial\theta$};
\node[lab] at (0.5,0.17) {$\theta$};
\end{tikzpicture}
\end{center}
```

Polar coordinates: $w_r$ is the rate of change of $w$ along the ray (fixed $\theta$), $w_\theta$ the rate along the circle (fixed $r$). The chain rule $w_r=w_x\cos\theta+w_y\sin\theta$, $w_\theta=-w_xr\sin\theta+w_yr\cos\theta$ projects $\nabla w$ onto these directions; along the circle, distance is $r\,d\theta$.

:::
