---
title: "First-Order Linear Systems"
sources: [mit1803-32]
requires: [math/differential-equations/second-order-linear/second-order-linear-equations, math/linear-algebra/systems/matrix-multiplication]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.03SC Differential Equations (Fall 2011), Session 32 (first-order linear systems, matrix notation, the companion matrix), in our own wording; examples are ours, checked in Python; proofs written out in steps. -->

Several interacting quantities give several coupled first-order equations. In matrix form they look exactly like one first-order linear equation, and every higher-order equation can be rewritten this way.

::: {#def-first-order-linear-system .definition name="First-order linear system"}
A *first-order linear system* for $\mathbf x(t)\in\mathbb R^n$ is
$$
\mathbf x'=A(t)\,\mathbf x+\mathbf F(t),
$$
with an $n\times n$ coefficient matrix $A(t)$ and an input vector $\mathbf F(t)$. It is *homogeneous* if $\mathbf F=\mathbf0$ and has *constant coefficients* if $A$ is constant. Superposition (@thm-superposition-linear) holds with the same proof.
:::

::: {#fig-first-order-systems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (x) at (0,0) {room $x$};
\node[box] (y) at (3,0) {room $y$};
\draw[<->, accent, emph] (x) -- (y) node[midway, above, lab, note] {$y-x$};
\draw[->, primary] (0,-0.6) -- (0,-1.3) node[below, lab, note] {$-x$}; \draw[->, primary] (3,-0.6) -- (3,-1.3) node[below, lab, note] {$-y$};
\node[lab, note, muted] at (1.5,-1.55) {outside $0^\circ$};
\end{tikzpicture}
\end{center}
```

Heat flows between the rooms and to the outside, each at a rate proportional to the temperature difference: a coupled linear system.

:::

::: {#exm-two-rooms .example name="Heat flow between two rooms"}
Two rooms at temperatures $x$ and $y$ exchange heat with each other and with the outside at $0^\circ$, each at rate $1$ per hour per degree of difference:
$$
x'=-x+(y-x),\qquad y'=-y+(x-y),\qquad\text{that is}\quad \mathbf x'=\begin{pmatrix}-2&1\\1&-2\end{pmatrix}\mathbf x .
$$
:::

::: {#fig-first-order-systems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm, y=0.3cm]
\draw[->] (0,0) -- (4.3,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,11) node[lab, above] {$^\circ$C};
\draw[emph, primary] (0,10) -- (0.051,9.049) -- (0.101,8.209) -- (0.152,7.465) -- (0.203,6.807) -- (0.253,6.221) -- (0.304,5.7) -- (0.354,5.234) -- (0.405,4.818) -- (0.456,4.444) -- (0.506,4.108) -- (0.557,3.805) -- (0.608,3.531) -- (0.658,3.283) -- (0.709,3.057) -- (0.759,2.852) -- (0.81,2.664) -- (0.861,2.492) -- (0.911,2.335) -- (0.962,2.19) -- (1.013,2.056) -- (1.063,1.932) -- (1.114,1.818) -- (1.165,1.712) -- (1.215,1.614) -- (1.266,1.522) -- (1.316,1.437) -- (1.367,1.357) -- (1.418,1.282) -- (1.468,1.213) -- (1.519,1.147) -- (1.57,1.086) -- (1.62,1.028) -- (1.671,0.974) -- (1.722,0.923) -- (1.772,0.874) -- (1.823,0.829) -- (1.873,0.786) -- (1.924,0.746) -- (1.975,0.707) -- (2.025,0.671) -- (2.076,0.637) -- (2.127,0.605) -- (2.177,0.574) -- (2.228,0.545) -- (2.278,0.518) -- (2.329,0.492) -- (2.38,0.467) -- (2.43,0.443) -- (2.481,0.421) -- (2.532,0.4) -- (2.582,0.38) -- (2.633,0.361) -- (2.684,0.343) -- (2.734,0.326) -- (2.785,0.31) -- (2.835,0.294) -- (2.886,0.28) -- (2.937,0.266) -- (2.987,0.253) -- (3.038,0.24) -- (3.089,0.228) -- (3.139,0.217) -- (3.19,0.206) -- (3.241,0.196) -- (3.291,0.186) -- (3.342,0.177) -- (3.392,0.168) -- (3.443,0.16) -- (3.494,0.152) -- (3.544,0.145) -- (3.595,0.137) -- (3.646,0.131) -- (3.696,0.124) -- (3.747,0.118) -- (3.797,0.112) -- (3.848,0.107) -- (3.899,0.101) -- (3.949,0.096) -- (4,0.092);
\draw[emph, accent] (0,0) -- (0.051,0.458) -- (0.101,0.828) -- (0.152,1.125) -- (0.203,1.36) -- (0.253,1.542) -- (0.304,1.68) -- (0.354,1.781) -- (0.405,1.851) -- (0.456,1.896) -- (0.506,1.919) -- (0.557,1.924) -- (0.608,1.915) -- (0.658,1.895) -- (0.709,1.865) -- (0.759,1.827) -- (0.81,1.784) -- (0.861,1.736) -- (0.911,1.685) -- (0.962,1.632) -- (1.013,1.577) -- (1.063,1.521) -- (1.114,1.464) -- (1.165,1.408) -- (1.215,1.353) -- (1.266,1.298) -- (1.316,1.244) -- (1.367,1.191) -- (1.418,1.14) -- (1.468,1.09) -- (1.519,1.042) -- (1.57,0.996) -- (1.62,0.951) -- (1.671,0.907) -- (1.722,0.865) -- (1.772,0.825) -- (1.823,0.787) -- (1.873,0.75) -- (1.924,0.715) -- (1.975,0.681) -- (2.025,0.648) -- (2.076,0.617) -- (2.127,0.588) -- (2.177,0.56) -- (2.228,0.533) -- (2.278,0.507) -- (2.329,0.482) -- (2.38,0.459) -- (2.43,0.437) -- (2.481,0.415) -- (2.532,0.395) -- (2.582,0.376) -- (2.633,0.357) -- (2.684,0.34) -- (2.734,0.323) -- (2.785,0.308) -- (2.835,0.292) -- (2.886,0.278) -- (2.937,0.264) -- (2.987,0.251) -- (3.038,0.239) -- (3.089,0.227) -- (3.139,0.216) -- (3.19,0.206) -- (3.241,0.195) -- (3.291,0.186) -- (3.342,0.177) -- (3.392,0.168) -- (3.443,0.16) -- (3.494,0.152) -- (3.544,0.144) -- (3.595,0.137) -- (3.646,0.13) -- (3.696,0.124) -- (3.747,0.118) -- (3.797,0.112) -- (3.848,0.107) -- (3.899,0.101) -- (3.949,0.096) -- (4,0.092);
\draw (0,10) -- (-0.08,10) node[left, lab, tick] {$10$};
\node[lab, note, primary] at (0.6,7.6) {room $x$}; \node[lab, note, accent] at (1.2,3.2) {room $y$};
\end{tikzpicture}
\end{center}
```

The two rooms starting at $10^\circ$ and $0^\circ$: their difference evens out quickly (mode $e^{-3t}$), then both cool together (mode $e^{-t}$).

:::

::: {#prp-companion-matrix .proposition name="Companion matrix"}
The equation $y''+by'+cy=f(t)$ is equivalent to the system
$$
\mathbf x'=\begin{pmatrix}0&1\\-c&-b\end{pmatrix}\mathbf x+\begin{pmatrix}0\\f(t)\end{pmatrix},\qquad \mathbf x=\begin{pmatrix}y\\y'\end{pmatrix},
$$
and the characteristic polynomial $\det(\lambda I-A)$ of this *companion matrix* is $\lambda^2+b\lambda+c$, the characteristic polynomial of the equation.
:::

::: {.proof}
1. If $y$ solves the equation, $\mathbf x=(y,y')$ satisfies $x_1'=x_2$ and $x_2'=y''=-cx_1-bx_2+f$, which is the system.

2. Conversely, if $\mathbf x$ solves the system, the first row says $x_2=x_1'$, and the second then says $x_1''+bx_1'+cx_1=f$.

3. $\det\begin{pmatrix}\lambda&-1\\c&\lambda+b\end{pmatrix}=\lambda(\lambda+b)+c=\lambda^2+b\lambda+c$.
:::

::: {#rmk-first-order-systems-1 .remark name="Why first order suffices"}
In the same way, an equation of order $n$ becomes a system of $n$ first-order equations for $(y,y',\dots,y^{(n-1)})$. Theory and numerical methods are therefore developed once, for first-order systems.
:::
