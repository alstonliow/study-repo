---
title: "Change of Variables and the Jacobian"
sources: [mit1802-18, mit1802n-CV]
requires: [math/calculus/multivariable/multiple-integrals/polar-double-integrals]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 18 and Supplementary Notes CV, in our own wording. Numbers checked in Python (sympy). -->

::: {#exm-ellipse-area-substitution .example name="Area of an ellipse"}

With $u=x/a$, $v=y/b$ we have $du=dx/a$, $dv=dy/b$, so $dx\,dy=ab\,du\,dv$ and
$$\iint_{(x/a)^2+(y/b)^2\le1}dx\,dy=ab\iint_{u^2+v^2\le1}du\,dv=\pi ab .$$

:::

::: {#fig-change-of-variables-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-1.4,0) -- (1.6,0) node[lab, right] {$u$};
\draw[->, faint] (0,-1.4) -- (0,1.6) node[lab, above] {$v$};
\fill[tintA] (1,0) -- (1,0.09) -- (0.98,0.17) -- (0.97,0.26) -- (0.94,0.34) -- (0.91,0.42) -- (0.87,0.5) -- (0.82,0.57) -- (0.77,0.64) -- (0.71,0.71) -- (0.64,0.77) -- (0.57,0.82) -- (0.5,0.87) -- (0.42,0.91) -- (0.34,0.94) -- (0.26,0.97) -- (0.17,0.98) -- (0.09,1) -- (0,1) -- (-0.09,1) -- (-0.17,0.98) -- (-0.26,0.97) -- (-0.34,0.94) -- (-0.42,0.91) -- (-0.5,0.87) -- (-0.57,0.82) -- (-0.64,0.77) -- (-0.71,0.71) -- (-0.77,0.64) -- (-0.82,0.57) -- (-0.87,0.5) -- (-0.91,0.42) -- (-0.94,0.34) -- (-0.97,0.26) -- (-0.98,0.17) -- (-1,0.09) -- (-1,0) -- (-1,-0.09) -- (-0.98,-0.17) -- (-0.97,-0.26) -- (-0.94,-0.34) -- (-0.91,-0.42) -- (-0.87,-0.5) -- (-0.82,-0.57) -- (-0.77,-0.64) -- (-0.71,-0.71) -- (-0.64,-0.77) -- (-0.57,-0.82) -- (-0.5,-0.87) -- (-0.42,-0.91) -- (-0.34,-0.94) -- (-0.26,-0.97) -- (-0.17,-0.98) -- (-0.09,-1) -- (0,-1) -- (0.09,-1) -- (0.17,-0.98) -- (0.26,-0.97) -- (0.34,-0.94) -- (0.42,-0.91) -- (0.5,-0.87) -- (0.57,-0.82) -- (0.64,-0.77) -- (0.71,-0.71) -- (0.77,-0.64) -- (0.82,-0.57) -- (0.87,-0.5) -- (0.91,-0.42) -- (0.94,-0.34) -- (0.97,-0.26) -- (0.98,-0.17) -- (1,-0.09) -- cycle;
\draw[emph] (1,0) -- (1,0.09) -- (0.98,0.17) -- (0.97,0.26) -- (0.94,0.34) -- (0.91,0.42) -- (0.87,0.5) -- (0.82,0.57) -- (0.77,0.64) -- (0.71,0.71) -- (0.64,0.77) -- (0.57,0.82) -- (0.5,0.87) -- (0.42,0.91) -- (0.34,0.94) -- (0.26,0.97) -- (0.17,0.98) -- (0.09,1) -- (0,1) -- (-0.09,1) -- (-0.17,0.98) -- (-0.26,0.97) -- (-0.34,0.94) -- (-0.42,0.91) -- (-0.5,0.87) -- (-0.57,0.82) -- (-0.64,0.77) -- (-0.71,0.71) -- (-0.77,0.64) -- (-0.82,0.57) -- (-0.87,0.5) -- (-0.91,0.42) -- (-0.94,0.34) -- (-0.97,0.26) -- (-0.98,0.17) -- (-1,0.09) -- (-1,0) -- (-1,-0.09) -- (-0.98,-0.17) -- (-0.97,-0.26) -- (-0.94,-0.34) -- (-0.91,-0.42) -- (-0.87,-0.5) -- (-0.82,-0.57) -- (-0.77,-0.64) -- (-0.71,-0.71) -- (-0.64,-0.77) -- (-0.57,-0.82) -- (-0.5,-0.87) -- (-0.42,-0.91) -- (-0.34,-0.94) -- (-0.26,-0.97) -- (-0.17,-0.98) -- (-0.09,-1) -- (0,-1) -- (0.09,-1) -- (0.17,-0.98) -- (0.26,-0.97) -- (0.34,-0.94) -- (0.42,-0.91) -- (0.5,-0.87) -- (0.57,-0.82) -- (0.64,-0.77) -- (0.71,-0.71) -- (0.77,-0.64) -- (0.82,-0.57) -- (0.87,-0.5) -- (0.91,-0.42) -- (0.94,-0.34) -- (0.97,-0.26) -- (0.98,-0.17) -- (1,-0.09) -- cycle;
\node[lab] at (0,-1.75) {$u^2+v^2\le1$, area $\pi$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-2.4,0) -- (2.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.4) -- (0,1.6) node[lab, above] {$y$};
\fill[tintA] (2,0) -- (1.99,0.09) -- (1.97,0.17) -- (1.93,0.26) -- (1.88,0.34) -- (1.81,0.42) -- (1.73,0.5) -- (1.64,0.57) -- (1.53,0.64) -- (1.41,0.71) -- (1.29,0.77) -- (1.15,0.82) -- (1,0.87) -- (0.85,0.91) -- (0.68,0.94) -- (0.52,0.97) -- (0.35,0.98) -- (0.17,1) -- (0,1) -- (-0.17,1) -- (-0.35,0.98) -- (-0.52,0.97) -- (-0.68,0.94) -- (-0.85,0.91) -- (-1,0.87) -- (-1.15,0.82) -- (-1.29,0.77) -- (-1.41,0.71) -- (-1.53,0.64) -- (-1.64,0.57) -- (-1.73,0.5) -- (-1.81,0.42) -- (-1.88,0.34) -- (-1.93,0.26) -- (-1.97,0.17) -- (-1.99,0.09) -- (-2,0) -- (-1.99,-0.09) -- (-1.97,-0.17) -- (-1.93,-0.26) -- (-1.88,-0.34) -- (-1.81,-0.42) -- (-1.73,-0.5) -- (-1.64,-0.57) -- (-1.53,-0.64) -- (-1.41,-0.71) -- (-1.29,-0.77) -- (-1.15,-0.82) -- (-1,-0.87) -- (-0.85,-0.91) -- (-0.68,-0.94) -- (-0.52,-0.97) -- (-0.35,-0.98) -- (-0.17,-1) -- (0,-1) -- (0.17,-1) -- (0.35,-0.98) -- (0.52,-0.97) -- (0.68,-0.94) -- (0.85,-0.91) -- (1,-0.87) -- (1.15,-0.82) -- (1.29,-0.77) -- (1.41,-0.71) -- (1.53,-0.64) -- (1.64,-0.57) -- (1.73,-0.5) -- (1.81,-0.42) -- (1.88,-0.34) -- (1.93,-0.26) -- (1.97,-0.17) -- (1.99,-0.09) -- cycle;
\draw[emph] (2,0) -- (1.99,0.09) -- (1.97,0.17) -- (1.93,0.26) -- (1.88,0.34) -- (1.81,0.42) -- (1.73,0.5) -- (1.64,0.57) -- (1.53,0.64) -- (1.41,0.71) -- (1.29,0.77) -- (1.15,0.82) -- (1,0.87) -- (0.85,0.91) -- (0.68,0.94) -- (0.52,0.97) -- (0.35,0.98) -- (0.17,1) -- (0,1) -- (-0.17,1) -- (-0.35,0.98) -- (-0.52,0.97) -- (-0.68,0.94) -- (-0.85,0.91) -- (-1,0.87) -- (-1.15,0.82) -- (-1.29,0.77) -- (-1.41,0.71) -- (-1.53,0.64) -- (-1.64,0.57) -- (-1.73,0.5) -- (-1.81,0.42) -- (-1.88,0.34) -- (-1.93,0.26) -- (-1.97,0.17) -- (-1.99,0.09) -- (-2,0) -- (-1.99,-0.09) -- (-1.97,-0.17) -- (-1.93,-0.26) -- (-1.88,-0.34) -- (-1.81,-0.42) -- (-1.73,-0.5) -- (-1.64,-0.57) -- (-1.53,-0.64) -- (-1.41,-0.71) -- (-1.29,-0.77) -- (-1.15,-0.82) -- (-1,-0.87) -- (-0.85,-0.91) -- (-0.68,-0.94) -- (-0.52,-0.97) -- (-0.35,-0.98) -- (-0.17,-1) -- (0,-1) -- (0.17,-1) -- (0.35,-0.98) -- (0.52,-0.97) -- (0.68,-0.94) -- (0.85,-0.91) -- (1,-0.87) -- (1.15,-0.82) -- (1.29,-0.77) -- (1.41,-0.71) -- (1.53,-0.64) -- (1.64,-0.57) -- (1.73,-0.5) -- (1.81,-0.42) -- (1.88,-0.34) -- (1.93,-0.26) -- (1.97,-0.17) -- (1.99,-0.09) -- cycle;
\node[lab] at (0,-1.75) {$x=au,\ y=bv$: area $\pi ab$};
\end{tikzpicture}
\end{center}
```

The substitution $x=au$, $y=bv$ (here $a=2$, $b=1$) stretches the unit disk into the ellipse and multiplies every area by $ab$, the Jacobian.

:::

In general we need the factor relating $du\,dv$ and $dx\,dy$.

::: {#def-jacobian .definition name="Jacobian"}

For a change of variables $u=u(x,y)$, $v=v(x,y)$, the **Jacobian** is the determinant
$$\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}u_x&u_y\\v_x&v_y\end{vmatrix}.$$
For three variables it is the $3\times3$ determinant of the partial derivatives of $u,v,w$ with respect to $x,y,z$.

:::

::: {#thm-change-of-variables .theorem name="Change of variables in a double integral"}

If $(x,y)\mapsto(u,v)$ maps the region $R$ one-to-one onto the region $G$, with continuous partial derivatives and non-zero Jacobian, then
$$du\,dv=\left\lvert\frac{\partial(u,v)}{\partial(x,y)}\right\rvert dx\,dy,\qquad
\iint_Rf\,dx\,dy=\iint_Gf\,\left\lvert\frac{\partial(x,y)}{\partial(u,v)}\right\rvert du\,dv,$$
where $\frac{\partial(x,y)}{\partial(u,v)}=1\Big/\frac{\partial(u,v)}{\partial(x,y)}$ and $f$ is written in terms of $u,v$.

:::

::: {.proof}

1. (Sketch.) Take a small rectangle with sides $\Delta x,\Delta y$ at $(x,y)$. By linear approximation, $\Delta u\approx u_x\Delta x+u_y\Delta y$ and $\Delta v\approx v_x\Delta x+v_y\Delta y$: in the $uv$-plane the rectangle becomes nearly the parallelogram with sides $\langle u_x,v_x\rangle\Delta x$ and $\langle u_y,v_y\rangle\Delta y$.

2. Its area is $\lvert\det\rvert\,\Delta x\Delta y=\left\lvert\frac{\partial(u,v)}{\partial(x,y)}\right\rvert\Delta x\Delta y$ (@thm-plane-determinant-area). Absolute value, because an area is positive.

3. Summing $f\,\Delta A$ over the pieces in either plane and passing to the limit gives the formula. The two Jacobians are reciprocal because the matrices of partial derivatives of inverse changes of variables are inverse matrices (chain rule), and $\det(M^{-1})=1/\det M$.

:::

::: {#fig-change-of-variables-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
\draw[->] (-0.2,0) -- (2.4,0) node[lab, right] {$x$};
\draw[->] (0,-0.2) -- (0,2.2) node[lab, above] {$y$};
\fill[tintA] (0.8,0.7) rectangle (1.6,1.4);
\draw[emph, primary] (0.8,0.7) rectangle (1.6,1.4);
\node[lab, below] at (1.2,0.7) {$\Delta x$};
\node[lab, left] at (0.8,1.05) {$\Delta y$};
\draw[->, muted] (2.6,1.1) to[bend left=20] node[lab, above] {$(u,v)$} (3.6,1.1);
\begin{scope}[xshift=4cm]
\draw[->] (-0.2,0) -- (2.8,0) node[lab, right] {$u$};
\draw[->] (0,-0.2) -- (0,2.2) node[lab, above] {$v$};
\fill[tintB] (0.5,0.5) -- (1.6,0.85) -- (2.0,1.8) -- (0.9,1.45) -- cycle;
\draw[emph, accent] (0.5,0.5) -- (1.6,0.85) -- (2.0,1.8) -- (0.9,1.45) -- cycle;
\draw[->, ink] (0.5,0.5) -- (1.6,0.85); \draw[->, ink] (0.5,0.5) -- (0.9,1.45);
\node[lab, below right] at (1.05,0.65) {$\langle u_x,v_x\rangle\Delta x$};
\node[lab, above] at (0.9,1.45) {$\langle u_y,v_y\rangle\Delta y$};
\end{scope}
\end{tikzpicture}
\end{center}
```

A small rectangle of area $\Delta x\,\Delta y$ is mapped by $(u,v)$ to approximately a parallelogram spanned by $\langle u_x,v_x\rangle\Delta x$ and $\langle u_y,v_y\rangle\Delta y$. Its area is the absolute value of the Jacobian times $\Delta x\,\Delta y$, which is @thm-change-of-variables.

:::

::: {#exm-linear-change-of-variables .example name="A linear change"}

$u=3x-2y$, $v=x+y$: $\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}3&-2\\1&1\end{vmatrix}=5$, so $du\,dv=5\,dx\,dy$: the unit square goes to a parallelogram of area $5$.

:::

::: {#exm-polar-jacobian .example name="Polar coordinates"}

$x=r\cos\theta$, $y=r\sin\theta$: $\dfrac{\partial(x,y)}{\partial(r,\theta)}=\begin{vmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{vmatrix}=r$, so $dx\,dy=r\,dr\,d\theta$, as in @thm-polar-area-element.

:::

::: {#prp-change-of-variables-method .proposition name="Method"}

1. Compute the Jacobian and the area element ($dx\,dy$ in terms of $du\,dv$).
2. Express the integrand in $u,v$.
3. Find the limits by drawing the region in the $uv$-plane, or by describing the curves $u=\text{const}$ or $v=\text{const}$ in the $xy$-plane.

:::

::: {#exm-change-of-variables-hyperbolas .example name="Slicing a square by hyperbolas"}

$\int_0^1\!\int_0^1x^2y\,dx\,dy$ with $u=x$, $v=xy$. Jacobian $\begin{vmatrix}1&0\\y&x\end{vmatrix}=x$, so $dx\,dy=\frac1x\,du\,dv$ and $x^2y\,dx\,dy=xy\,du\,dv=v\,du\,dv$. The square $0\le x,y\le1$ becomes the triangle $0\le v\le u\le1$ (the edge $y=1$ becomes $u=v$, the edge $x=1$ becomes $u=1$):
$$\int_0^1\!\!\int_v^1v\,du\,dv=\int_0^1v(1-v)\,dv=\frac16,$$
which agrees with $\int_0^1x^2dx\int_0^1y\,dy=\frac13\cdot\frac12$.

:::

::: {#fig-change-of-variables-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.6]
\draw[->, faint] (-0.2,0) -- (1.5,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,1.5) node[lab, above] {$y$};
\fill[tintA] (0,0) -- (1,0) -- (1,1) -- (0,1) -- cycle;
\draw[emph] (0,0) -- (1,0) -- (1,1) -- (0,1) -- cycle;
\draw[hl] (0.2,1) -- (0.22,0.91) -- (0.24,0.83) -- (0.26,0.77) -- (0.28,0.71) -- (0.3,0.67) -- (0.32,0.62) -- (0.34,0.59) -- (0.36,0.56) -- (0.38,0.53) -- (0.4,0.5) -- (0.42,0.48) -- (0.44,0.45) -- (0.46,0.43) -- (0.48,0.42) -- (0.5,0.4) -- (0.52,0.38) -- (0.54,0.37) -- (0.56,0.36) -- (0.58,0.34) -- (0.6,0.33) -- (0.62,0.32) -- (0.64,0.31) -- (0.66,0.3) -- (0.68,0.29) -- (0.7,0.29) -- (0.72,0.28) -- (0.74,0.27) -- (0.76,0.26) -- (0.78,0.26) -- (0.8,0.25) -- (0.82,0.24) -- (0.84,0.24) -- (0.86,0.23) -- (0.88,0.23) -- (0.9,0.22) -- (0.92,0.22) -- (0.94,0.21) -- (0.96,0.21) -- (0.98,0.2) -- (1,0.2);
\draw[hl] (0.4,1) -- (0.42,0.96) -- (0.43,0.93) -- (0.45,0.9) -- (0.46,0.87) -- (0.48,0.84) -- (0.49,0.82) -- (0.51,0.79) -- (0.52,0.77) -- (0.54,0.75) -- (0.55,0.73) -- (0.56,0.71) -- (0.58,0.69) -- (0.59,0.67) -- (0.61,0.66) -- (0.62,0.64) -- (0.64,0.62) -- (0.66,0.61) -- (0.67,0.6) -- (0.69,0.58) -- (0.7,0.57) -- (0.72,0.56) -- (0.73,0.55) -- (0.74,0.54) -- (0.76,0.53) -- (0.78,0.52) -- (0.79,0.51) -- (0.8,0.5) -- (0.82,0.49) -- (0.83,0.48) -- (0.85,0.47) -- (0.86,0.46) -- (0.88,0.45) -- (0.9,0.45) -- (0.91,0.44) -- (0.93,0.43) -- (0.94,0.43) -- (0.95,0.42) -- (0.97,0.41) -- (0.98,0.41) -- (1,0.4);
\draw[hl] (0.6,1) -- (0.61,0.98) -- (0.62,0.97) -- (0.63,0.95) -- (0.64,0.94) -- (0.65,0.92) -- (0.66,0.91) -- (0.67,0.9) -- (0.68,0.88) -- (0.69,0.87) -- (0.7,0.86) -- (0.71,0.85) -- (0.72,0.83) -- (0.73,0.82) -- (0.74,0.81) -- (0.75,0.8) -- (0.76,0.79) -- (0.77,0.78) -- (0.78,0.77) -- (0.79,0.76) -- (0.8,0.75) -- (0.81,0.74) -- (0.82,0.73) -- (0.83,0.72) -- (0.84,0.71) -- (0.85,0.71) -- (0.86,0.7) -- (0.87,0.69) -- (0.88,0.68) -- (0.89,0.67) -- (0.9,0.67) -- (0.91,0.66) -- (0.92,0.65) -- (0.93,0.65) -- (0.94,0.64) -- (0.95,0.63) -- (0.96,0.62) -- (0.97,0.62) -- (0.98,0.61) -- (0.99,0.61) -- (1,0.6);
\draw[hl] (0.8,1) -- (0.81,0.99) -- (0.81,0.99) -- (0.82,0.98) -- (0.82,0.98) -- (0.83,0.97) -- (0.83,0.96) -- (0.84,0.96) -- (0.84,0.95) -- (0.85,0.95) -- (0.85,0.94) -- (0.85,0.94) -- (0.86,0.93) -- (0.86,0.92) -- (0.87,0.92) -- (0.88,0.91) -- (0.88,0.91) -- (0.89,0.9) -- (0.89,0.9) -- (0.9,0.89) -- (0.9,0.89) -- (0.91,0.88) -- (0.91,0.88) -- (0.92,0.87) -- (0.92,0.87) -- (0.93,0.86) -- (0.93,0.86) -- (0.94,0.86) -- (0.94,0.85) -- (0.95,0.85) -- (0.95,0.84) -- (0.96,0.84) -- (0.96,0.83) -- (0.97,0.83) -- (0.97,0.82) -- (0.97,0.82) -- (0.98,0.82) -- (0.98,0.81) -- (0.99,0.81) -- (0.99,0.8) -- (1,0.8);
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}[scale=1.6]
\draw[->, faint] (-0.2,0) -- (1.5,0) node[lab, right] {$u$};
\draw[->, faint] (0,-0.2) -- (0,1.5) node[lab, above] {$v$};
\fill[tintA] (0,0) -- (1,0) -- (1,1) -- cycle;
\draw[emph] (0,0) -- (1,0) -- (1,1) -- cycle;
\draw[hl] (0.2,0.2) -- (1,0.2);
\draw[hl] (0.4,0.4) -- (1,0.4);
\draw[hl] (0.6,0.6) -- (1,0.6);
\draw[hl] (0.8,0.8) -- (1,0.8);
\end{tikzpicture}
\end{center}
```

With $u=x$, $v=xy$ the unit square (left) is sliced by the hyperbolas $xy=v$ (thick), which become horizontal segments in the $uv$-plane (right); the square becomes the triangle $0\le v\le u\le1$, and the edge $y=1$ becomes the diagonal $v=u$.

:::
