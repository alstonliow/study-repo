---
title: "Line Integrals, Gradient Fields and Curl in Space"
sources: [mit1802-30, mit1802n-V11, mit1802n-V12]
requires: [math/calculus/multivariable/line-integrals/gradient-fields-and-potentials]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 30 and Supplementary Notes V11, V12, in our own wording. Numbers checked in Python (sympy). -->

For $\mathbf{F}=\langle P,Q,R\rangle$ and a curve $C$ in space, $d\mathbf{r}=\langle dx,dy,dz\rangle$ and the work is
$$\int_C\mathbf{F}\cdot d\mathbf{r}=\int_CP\,dx+Q\,dy+R\,dz,$$
computed, as in the plane (@def-line-integral-work), by expressing $x,y,z$ in terms of one parameter. The fundamental theorem $\int_C\nabla f\cdot d\mathbf{r}=f(P_1)-f(P_0)$ and the equivalence of conservative, path independent and gradient fields (@thm-conservative-equivalences) hold in space with the same proofs.

::: {#exm-work-in-space .example name="Two paths, same work"}

$\mathbf{F}=\langle yz,xz,xy\rangle$.

- Along $x=t^3$, $y=t^2$, $z=t$, $0\le t\le1$: $\int_0^1\big(t^3\cdot3t^2+t^4\cdot2t+t^5\big)dt=\int_0^16t^5\,dt=1$.
- Along the segments $(0,0,0)\to(1,0,0)\to(1,1,0)\to(1,1,1)$: in the plane $z=0$, $\mathbf{F}=xy\,\mathbf{k}$ is perpendicular to the path, so no work; on the last segment $x=y=1$, $\mathbf{F}\cdot d\mathbf{r}=dz$, giving $1$.

The answers agree because $\mathbf{F}=\nabla(xyz)$, and $xyz$ changes from $0$ to $1$.

:::

::: {#fig-line-integrals-in-space-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->, faint] (0,0) -- (-0.8,-0.51) node[lab, below left] {$x$};
\draw[->, faint] (0,0) -- (1.6,0) node[lab, right] {$y$};
\draw[->, faint] (0,0) -- (0,1.6) node[lab, above] {$z$};
\draw[hl] (0,0) -- (0,0.03) -- (0,0.05) -- (0.01,0.08) -- (0.01,0.1) -- (0.02,0.13) -- (0.02,0.15) -- (0.03,0.18) -- (0.04,0.2) -- (0.05,0.23) -- (0.06,0.25) -- (0.07,0.27) -- (0.08,0.3) -- (0.09,0.32) -- (0.11,0.34) -- (0.12,0.37) -- (0.13,0.39) -- (0.15,0.41) -- (0.16,0.43) -- (0.18,0.45) -- (0.2,0.47) -- (0.21,0.49) -- (0.23,0.51) -- (0.25,0.52) -- (0.26,0.54) -- (0.28,0.56) -- (0.3,0.57) -- (0.31,0.59) -- (0.33,0.6) -- (0.35,0.61) -- (0.36,0.62) -- (0.38,0.63) -- (0.4,0.64) -- (0.41,0.65) -- (0.43,0.66) -- (0.44,0.67) -- (0.46,0.67) -- (0.47,0.68) -- (0.49,0.68) -- (0.5,0.68);
\draw[emph, dashed] (0,0) -- (-0.5,-0.32) -- (0.5,-0.32) -- (0.5,0.68);
\fill[ink] (0.5,0.68) circle[pt] node[lab, above right] {$(1,1,1)$};
\fill[ink] (0,0) circle[pt];
\end{tikzpicture}
\end{center}
```

Two paths from the origin to $(1,1,1)$: the twisted cubic $(t^3,t^2,t)$ (thick) and three segments parallel to the axes (dashed). For $\mathbf F=\nabla(xyz)$ the work along both is $1$.

:::

::: {#def-curl-space .definition name="Curl"}

The **curl** of $\mathbf{F}=\langle P,Q,R\rangle$ is
$$\operatorname{curl}\mathbf{F}=\nabla\times\mathbf{F}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\\partial_x&\partial_y&\partial_z\\P&Q&R\end{vmatrix}=\langle R_y-Q_z,\ P_z-R_x,\ Q_x-P_y\rangle .$$
For a plane field ($R=0$, $P,Q$ independent of $z$) it is $(Q_x-P_y)\,\mathbf{k}$, the plane curl of @def-curl-plane times $\mathbf{k}$.

:::

::: {#thm-gradient-field-criterion-space .theorem name="Criterion for gradient fields in space"}

Let $\mathbf{F}=\langle P,Q,R\rangle$ have continuous partial derivatives.

1. If $\mathbf{F}=\nabla f$ then $\operatorname{curl}\mathbf{F}=\mathbf{0}$, i.e. $P_y=Q_x$, $P_z=R_x$, $Q_z=R_y$.
2. Conversely, if $\operatorname{curl}\mathbf{F}=\mathbf{0}$ in all of space (or in a simply connected region), then $\mathbf{F}$ is a gradient field.

:::

::: {.proof}

1. $P=f_x$, $Q=f_y$, $R=f_z$, and the mixed partials of $f$ are equal (@thm-symmetry-mixed-partials): $P_y=f_{xy}=f_{yx}=Q_x$, and likewise for the other two pairs.

2. The converse is proved with Stokes' theorem (@thm-curl-free-conservative).

:::

::: {#exm-potential-in-space .example name="Finding a potential in space"}

For which $a,b$ is $\mathbf{F}=axy\,\mathbf{i}+(x^2+z^3)\,\mathbf{j}+(byz^2-4z^3)\,\mathbf{k}$ a gradient field? $P_y=ax=Q_x=2x$ gives $a=2$; $P_z=0=R_x$; $Q_z=3z^2=R_y=bz^2$ gives $b=3$. Then:

1. $f_x=2xy$, so $f=x^2y+g(y,z)$.
2. $f_y=x^2+g_y=x^2+z^3$, so $g_y=z^3$ and $g=yz^3+h(z)$.
3. $f_z=3yz^2+h'(z)=3yz^2-4z^3$, so $h=-z^4+c$.

So $f=x^2y+yz^3-z^4+c$. Alternatively, integrate $\mathbf{F}$ from the origin along three segments parallel to the axes.

:::

::: {#fig-line-integrals-in-space-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->, faint] (0,0) -- (-0.9,-0.58) node[lab, below left] {$x$};
\draw[->, faint] (0,0) -- (1.8,0) node[lab, right] {$y$};
\draw[->, faint] (0,0) -- (0,1.6) node[lab, above] {$z$};
\draw[hl] (0,0) -- (-0.6,-0.38);
\draw[hl] (-0.6,-0.38) -- (0.5,-0.38);
\draw[hl] (0.5,-0.38) -- (0.5,0.52);
\draw[faint, dashed] (0.5,0.52) -- (0.5,-0.38) -- (1.1,0);
\fill[accent] (0.5,0.52) circle[pt] node[lab, above right] {$(x,y,z)$};
\node[lab, below] at (-0.3,-0.19) {$1$};
\node[lab, below] at (-0.05,-0.38) {$2$};
\node[lab, right] at (0.5,0.07) {$3$};
\end{tikzpicture}
\end{center}
```

Finding a potential by integrating from the origin along segments parallel to the axes: (1) along the $x$-axis, (2) parallel to the $y$-axis, (3) parallel to the $z$-axis. On each segment only one component of $\mathbf F$ does work.

:::

::: {#exm-curl-rotation .example name="Curl of a rotation"}

The velocity field of a rotation about the $z$-axis with angular velocity $\omega$ is $\mathbf{v}=\langle-\omega y,\omega x,0\rangle$, and $\nabla\times\mathbf{v}=\langle0,0,2\omega\rangle$. In general the curl of a velocity field measures its rotating part: its direction is the axis of rotation and its length is twice the angular velocity.

:::

::: {#fig-line-integrals-in-space-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->] (-2.4,0) -- (2.4,0) node[lab, right] {$x$};
\draw[->] (0,-2.4) -- (0,2.4) node[lab, above] {$y$};
\draw[faint] (0,0) circle (0.9); \draw[faint] (0,0) circle (1.8);
\foreach \ang in {0,60,...,300} \draw[->, accent, emph] (\ang:0.9) -- ++(\ang+90:0.3);
\foreach \ang in {0,36,...,324} \draw[->, accent, emph] (\ang:1.8) -- ++(\ang+90:0.6);
\node[hollow dot, scale=1.6] at (0,0) {}; \fill[ink] (0,0) circle[pt];
\node[lab, below right] at (0.1,-0.05) {$\nabla\times\mathbf v$};
\end{tikzpicture}
\end{center}
```

The rotation field $\mathbf v=\langle-\omega y,\omega x,0\rangle$ seen from above (@exm-curl-rotation). The speed grows with the distance from the axis, and $\nabla\times\mathbf v=\langle0,0,2\omega\rangle$ points out of the page, along the axis of rotation.

:::
