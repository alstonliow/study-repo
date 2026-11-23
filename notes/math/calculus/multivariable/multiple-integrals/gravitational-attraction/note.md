---
title: "Gravitational Attraction"
sources: [mit1802-26, mit1802n-G]
requires: [math/calculus/multivariable/multiple-integrals/spherical-coordinates]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lecture 26 and Supplementary Notes G, in our own wording. Numbers checked in Python (sympy). -->

A mass $\Delta M$ at the point $(x,y,z)$, at distance $\rho$ from a mass $m$ at the origin, attracts it with a force of magnitude $G\,m\,\Delta M/\rho^2$ ($G$ the gravitational constant) directed towards $(x,y,z)$:
$$\mathbf{F}=\frac{G\,m\,\Delta M}{\rho^2}\cdot\frac{\langle x,y,z\rangle}{\rho}=\frac{G\,m\,\Delta M}{\rho^3}\langle x,y,z\rangle .$$

::: {#prp-attraction-of-solid .proposition name="Attraction of a solid"}

A solid $D$ of density $\delta$ attracts a mass $m$ at the origin with the force
$$\mathbf{F}=Gm\iiint_D\frac{\langle x,y,z\rangle}{\rho^3}\,\delta\,dV .$$
If $D$ is symmetric about the $z$-axis, then $\mathbf{F}=\langle0,0,F_z\rangle$ with
$$F_z=Gm\iiint_D\frac{z}{\rho^3}\,\delta\,dV=Gm\iiint_D\delta\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta .$$

:::

::: {.proof}

1. Add up the forces of the small pieces $\Delta M=\delta\,\Delta V$ and pass to the limit.

2. With symmetry about the $z$-axis, the horizontal components of pieces placed symmetrically cancel.

3. In spherical coordinates $z/\rho^3=\cos\phi/\rho^2$, and $dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$, so the $\rho^2$ cancels.

:::

::: {#fig-gravitational-attraction-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0,-0.3) -- (0,2.8) node[lab, above] {$z$};
\fill[ink] (0,0) circle[pt] node[lab, below] {$m$ at origin};
\fill[tintA] (0.9,1.6) -- (0.9,1.68) -- (0.89,1.76) -- (0.87,1.83) -- (0.85,1.91) -- (0.82,1.98) -- (0.78,2.05) -- (0.74,2.12) -- (0.69,2.18) -- (0.64,2.24) -- (0.58,2.29) -- (0.52,2.34) -- (0.45,2.38) -- (0.38,2.42) -- (0.31,2.45) -- (0.23,2.47) -- (0.16,2.49) -- (0.08,2.5) -- (0,2.5) -- (-0.08,2.5) -- (-0.16,2.49) -- (-0.23,2.47) -- (-0.31,2.45) -- (-0.38,2.42) -- (-0.45,2.38) -- (-0.52,2.34) -- (-0.58,2.29) -- (-0.64,2.24) -- (-0.69,2.18) -- (-0.74,2.12) -- (-0.78,2.05) -- (-0.82,1.98) -- (-0.85,1.91) -- (-0.87,1.83) -- (-0.89,1.76) -- (-0.9,1.68) -- (-0.9,1.6) -- (-0.9,1.52) -- (-0.89,1.44) -- (-0.87,1.37) -- (-0.85,1.29) -- (-0.82,1.22) -- (-0.78,1.15) -- (-0.74,1.08) -- (-0.69,1.02) -- (-0.64,0.96) -- (-0.58,0.91) -- (-0.52,0.86) -- (-0.45,0.82) -- (-0.38,0.78) -- (-0.31,0.75) -- (-0.23,0.73) -- (-0.16,0.71) -- (-0.08,0.7) -- (0,0.7) -- (0.08,0.7) -- (0.16,0.71) -- (0.23,0.73) -- (0.31,0.75) -- (0.38,0.78) -- (0.45,0.82) -- (0.52,0.86) -- (0.58,0.91) -- (0.64,0.96) -- (0.69,1.02) -- (0.74,1.08) -- (0.78,1.15) -- (0.82,1.22) -- (0.85,1.29) -- (0.87,1.37) -- (0.89,1.44) -- (0.9,1.52) -- cycle;
\draw[emph] (0.9,1.6) -- (0.9,1.68) -- (0.89,1.76) -- (0.87,1.83) -- (0.85,1.91) -- (0.82,1.98) -- (0.78,2.05) -- (0.74,2.12) -- (0.69,2.18) -- (0.64,2.24) -- (0.58,2.29) -- (0.52,2.34) -- (0.45,2.38) -- (0.38,2.42) -- (0.31,2.45) -- (0.23,2.47) -- (0.16,2.49) -- (0.08,2.5) -- (0,2.5) -- (-0.08,2.5) -- (-0.16,2.49) -- (-0.23,2.47) -- (-0.31,2.45) -- (-0.38,2.42) -- (-0.45,2.38) -- (-0.52,2.34) -- (-0.58,2.29) -- (-0.64,2.24) -- (-0.69,2.18) -- (-0.74,2.12) -- (-0.78,2.05) -- (-0.82,1.98) -- (-0.85,1.91) -- (-0.87,1.83) -- (-0.89,1.76) -- (-0.9,1.68) -- (-0.9,1.6) -- (-0.9,1.52) -- (-0.89,1.44) -- (-0.87,1.37) -- (-0.85,1.29) -- (-0.82,1.22) -- (-0.78,1.15) -- (-0.74,1.08) -- (-0.69,1.02) -- (-0.64,0.96) -- (-0.58,0.91) -- (-0.52,0.86) -- (-0.45,0.82) -- (-0.38,0.78) -- (-0.31,0.75) -- (-0.23,0.73) -- (-0.16,0.71) -- (-0.08,0.7) -- (0,0.7) -- (0.08,0.7) -- (0.16,0.71) -- (0.23,0.73) -- (0.31,0.75) -- (0.38,0.78) -- (0.45,0.82) -- (0.52,0.86) -- (0.58,0.91) -- (0.64,0.96) -- (0.69,1.02) -- (0.74,1.08) -- (0.78,1.15) -- (0.82,1.22) -- (0.85,1.29) -- (0.87,1.37) -- (0.89,1.44) -- (0.9,1.52) -- cycle;
\fill[accent] (0.5,1.9) circle (0.07);
\draw[hl] (0,0) -- (0.5,1.9);
\node[lab, right] at (0.32,0.9) {$\rho$};
\draw[faint] (0,0.55) arc[start angle=90, end angle=75.3, radius=0.55];
\node[lab, above] at (0.12,0.66) {$\phi$};
\node[lab, right] at (0.55,2) {$\delta\,dV$};
\end{tikzpicture}
\end{center}
```

Attraction of a solid on a mass $m$ at the origin: a piece of mass $\delta\,dV$ at distance $\rho$ pulls with strength $Gm\,\delta\,dV/\rho^2$; by symmetry only the component along the axis, $\cos\phi$ times that, survives the integration.

:::

The usual set-up: put the test mass at the origin and the axis of symmetry of the solid along the $z$-axis.

::: {#thm-newton-shell .theorem name="Newton's theorem"}

A uniform solid ball of mass $M$ and radius $a$ attracts a mass $m$ outside it as if all its mass were at its centre. For a mass on its surface, the force has magnitude $GMm/a^2$.

:::

::: {.proof}

1. We treat the case of a mass $m$ at the origin on the surface. Place the ball with centre $(0,0,a)$, so it is tangent to the $xy$-plane at the origin.

2. In the vertical plane through the $z$-axis at angle $\theta$, a ray from the origin at angle $\phi$ from the $z$-axis meets the sphere again at distance $\rho=2a\cos\phi$ (the triangle from the origin to the far pole to the point is right-angled at the point, with hypotenuse $2a$). The ray meets the ball for $0\le\phi\le\pi/2$.

3. By @prp-attraction-of-solid,
$$F_z=Gm\delta\int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^{2a\cos\phi}\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta=Gm\delta\cdot2\pi\cdot2a\int_0^{\pi/2}\cos^2\phi\sin\phi\,d\phi=\frac43\pi a\,G\,m\,\delta .$$

4. With $M=\frac43\pi a^3\delta$ this is $GMm/a^2$, the attraction of a point mass $M$ at the centre, distance $a$ away. (The case of a mass at distance greater than $a$ is similar, with harder limits.)

:::

::: {#fig-gravitational-attraction-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1,0) -- (1,0.09) -- (0.98,0.17) -- (0.97,0.26) -- (0.94,0.34) -- (0.91,0.42) -- (0.87,0.5) -- (0.82,0.57) -- (0.77,0.64) -- (0.71,0.71) -- (0.64,0.77) -- (0.57,0.82) -- (0.5,0.87) -- (0.42,0.91) -- (0.34,0.94) -- (0.26,0.97) -- (0.17,0.98) -- (0.09,1) -- (0,1) -- (-0.09,1) -- (-0.17,0.98) -- (-0.26,0.97) -- (-0.34,0.94) -- (-0.42,0.91) -- (-0.5,0.87) -- (-0.57,0.82) -- (-0.64,0.77) -- (-0.71,0.71) -- (-0.77,0.64) -- (-0.82,0.57) -- (-0.87,0.5) -- (-0.91,0.42) -- (-0.94,0.34) -- (-0.97,0.26) -- (-0.98,0.17) -- (-1,0.09) -- (-1,0) -- (-1,-0.09) -- (-0.98,-0.17) -- (-0.97,-0.26) -- (-0.94,-0.34) -- (-0.91,-0.42) -- (-0.87,-0.5) -- (-0.82,-0.57) -- (-0.77,-0.64) -- (-0.71,-0.71) -- (-0.64,-0.77) -- (-0.57,-0.82) -- (-0.5,-0.87) -- (-0.42,-0.91) -- (-0.34,-0.94) -- (-0.26,-0.97) -- (-0.17,-0.98) -- (-0.09,-1) -- (0,-1) -- (0.09,-1) -- (0.17,-0.98) -- (0.26,-0.97) -- (0.34,-0.94) -- (0.42,-0.91) -- (0.5,-0.87) -- (0.57,-0.82) -- (0.64,-0.77) -- (0.71,-0.71) -- (0.77,-0.64) -- (0.82,-0.57) -- (0.87,-0.5) -- (0.91,-0.42) -- (0.94,-0.34) -- (0.97,-0.26) -- (0.98,-0.17) -- (1,-0.09) -- cycle;
\draw[emph] (1,0) -- (1,0.09) -- (0.98,0.17) -- (0.97,0.26) -- (0.94,0.34) -- (0.91,0.42) -- (0.87,0.5) -- (0.82,0.57) -- (0.77,0.64) -- (0.71,0.71) -- (0.64,0.77) -- (0.57,0.82) -- (0.5,0.87) -- (0.42,0.91) -- (0.34,0.94) -- (0.26,0.97) -- (0.17,0.98) -- (0.09,1) -- (0,1) -- (-0.09,1) -- (-0.17,0.98) -- (-0.26,0.97) -- (-0.34,0.94) -- (-0.42,0.91) -- (-0.5,0.87) -- (-0.57,0.82) -- (-0.64,0.77) -- (-0.71,0.71) -- (-0.77,0.64) -- (-0.82,0.57) -- (-0.87,0.5) -- (-0.91,0.42) -- (-0.94,0.34) -- (-0.97,0.26) -- (-0.98,0.17) -- (-1,0.09) -- (-1,0) -- (-1,-0.09) -- (-0.98,-0.17) -- (-0.97,-0.26) -- (-0.94,-0.34) -- (-0.91,-0.42) -- (-0.87,-0.5) -- (-0.82,-0.57) -- (-0.77,-0.64) -- (-0.71,-0.71) -- (-0.64,-0.77) -- (-0.57,-0.82) -- (-0.5,-0.87) -- (-0.42,-0.91) -- (-0.34,-0.94) -- (-0.26,-0.97) -- (-0.17,-0.98) -- (-0.09,-1) -- (0,-1) -- (0.09,-1) -- (0.17,-0.98) -- (0.26,-0.97) -- (0.34,-0.94) -- (0.42,-0.91) -- (0.5,-0.87) -- (0.57,-0.82) -- (0.64,-0.77) -- (0.71,-0.71) -- (0.77,-0.64) -- (0.82,-0.57) -- (0.87,-0.5) -- (0.91,-0.42) -- (0.94,-0.34) -- (0.97,-0.26) -- (0.98,-0.17) -- (1,-0.09) -- cycle;
\fill[ink] (2.2,0) circle[pt] node[lab, above] {$m$};
\draw[->, hl] (2.2,0) -- (1.5,0);
\node[lab] at (0,-1.3) {ball of mass $M$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\fill[ink] (0,0) circle[pt] node[lab, above] {$M$};
\fill[ink] (2.2,0) circle[pt] node[lab, above] {$m$};
\draw[->, hl] (2.2,0) -- (1.5,0);
\draw[faint, dashed] (0,0) circle (1);
\node[lab] at (0,-1.3) {point mass $M$};
\end{tikzpicture}
\end{center}
```

Newton's theorem: outside a ball with spherically symmetric density, the attraction is the same as if the whole mass $M$ sat at the centre.

:::

::: {#fig-gravitational-attraction-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
\fill[tintA] (0,1.5) circle (1.5);
\draw[emph, primary] (0,1.5) circle (1.5);
\draw[->] (-2.2,0) -- (2.2,0);
\draw[->] (0,0) -- (0,3.6) node[lab, above] {$z$};
\fill[ink] (0,1.5) circle[pt];
\draw[faint] (0,1.5) -- node[lab, above, pos=0.6] {$a$} (-1.5,1.5);
\draw[hl] (0,0) -- node[lab, below right, pos=0.55] {$\rho=2a\cos\phi$} (1.409,2.013);
\draw[dashed] (1.409,2.013) -- (0,3);
\fill[ink] (0,3) circle[pt];
\draw (0,0.6) arc[start angle=90, end angle=55, radius=0.6];
\node[lab] at (0.2,0.85) {$\phi$};
\node[hl dot] at (0,0) {};
\node[lab, below left] at (0,0) {$m$};
\end{tikzpicture}
\end{center}
```

Cross-section of the proof of @thm-newton-shell. The ball of radius $a$ sits on the $xy$-plane with the mass $m$ at the origin; a ray at angle $\phi$ from the $z$-axis leaves the ball at $\rho=2a\cos\phi$, because the triangle with the top pole has a right angle at the far point.

:::
