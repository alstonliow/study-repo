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
