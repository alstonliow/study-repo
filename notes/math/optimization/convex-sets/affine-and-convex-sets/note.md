---
title: "Affine and Convex Sets"
sources: [ee364a-2, mit18065-21]
requires: [math/linear-algebra/vector-spaces/solving-ax-b]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex sets, in our own wording; proofs written out in steps. -->
<!-- Merged 2026-11-21 (owner approval): def-convex-set moved here from @sec-ai-machine-learning-convex-optimization (MIT 18.065, Lecture 21); wording from 18.065, display form and notation of this part from EE364A. -->

Convex optimization studies sets and functions that behave well under averaging. This note fixes the three basic kinds of set: affine sets (closed under lines), convex sets (closed under segments) and convex cones (closed under nonnegative combinations).

::: {#def-affine-set .definition name="Affine set, affine hull"}

A set $C\subseteq\mathbb{R}^n$ is *affine* if it contains the whole line through any two of its points:
$$x_1,x_2\in C,\ \theta\in\mathbb{R}\ \Longrightarrow\ \theta x_1+(1-\theta)x_2\in C.$$
An *affine combination* of $x_1,\dots,x_k$ is $\sum_i\theta_ix_i$ with $\sum_i\theta_i=1$. The *affine hull* $\operatorname{aff}C$ is the set of all affine combinations of points of $C$.

:::

::: {#fig-affine-and-convex-sets-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.6,-0.2) -- (4,2.1);
\draw[hl] (0.6,0.4) -- (2.6,1.4);
\fill[ink] (3.6,1.9) circle[pt] node[lab, below right] {$\theta=-0.5$};
\fill[accent] (2.6,1.4) circle[pt] node[lab, below right] {$\theta=0$};
\fill[accent] (1.8,1) circle[pt] node[lab, below right] {$\theta=0.4$};
\fill[accent] (0.6,0.4) circle[pt] node[lab, below right] {$\theta=1$};
\fill[ink] (-0.4,-0.1) circle[pt] node[lab, below right] {$\theta=1.5$};
\node[lab] at (0.6,0.75) {$x_1$};
\node[lab] at (2.6,1.75) {$x_2$};
\end{tikzpicture}
\end{center}
```

The line through $x_1$ and $x_2$ is the set of points $\theta x_1+(1-\theta)x_2$ for all real $\theta$; an affine set contains every such line. Values $0\le\theta\le1$ give the segment between them (thick), which is all a convex set must contain.

:::

::: {#prp-affine-set-subspace .proposition name="Affine sets are shifted subspaces"}

A nonempty set $C$ is affine if and only if, for one (equivalently every) $x_0\in C$, the set $V=C-x_0=\{x-x_0\mid x\in C\}$ is a subspace. Every affine set is the solution set $\{x\mid Ax=b\}$ of a system of linear equations, and conversely.

:::

::: {.proof}

1. Suppose $C$ is affine and $x_0\in C$. For $v_1=x_1-x_0$, $v_2=x_2-x_0$ in $V$ and scalars $\alpha,\beta$, the point $\alpha x_1+\beta x_2+(1-\alpha-\beta)x_0$ is an affine combination of three points of $C$.

2. An affine set contains every affine combination of its points: induct on the number of points, writing $\sum_{i\le k}\theta_ix_i=\theta_kx_k+(1-\theta_k)\sum_{i<k}\frac{\theta_i}{1-\theta_k}x_i$ when $\theta_k\ne1$ (some $\theta_i\ne1$ exists if $k\ge2$, so reorder).

3. Hence $\alpha v_1+\beta v_2=\big(\alpha x_1+\beta x_2+(1-\alpha-\beta)x_0\big)-x_0\in V$, so $V$ is a subspace. Conversely, if $V$ is a subspace then $\theta x_1+(1-\theta)x_2=x_0+\theta v_1+(1-\theta)v_2\in C$.

4. Choose a matrix $A$ whose null space is $V$ and put $b=Ax_0$. Then $Ax=b$ iff $x-x_0\in V$ iff $x\in C$. Conversely, the solution set of $Ax=b$ is $x_0+\operatorname{null}A$ for any solution $x_0$, a shifted subspace.

:::

::: {#def-convex-set .definition name="Convex set"}

A set $C\subseteq\mathbb{R}^n$ is *convex* if it contains the segment between any two of its points:
$$x_1,x_2\in C,\ 0\le\theta\le1\ \Longrightarrow\ \theta x_1+(1-\theta)x_2\in C.$$

:::

::: {#fig-affine-and-convex-sets-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (1.26,0.34) -- (1.23,0.41) -- (1.2,0.48) -- (1.15,0.55) -- (1.1,0.61) -- (1.04,0.67) -- (0.97,0.73) -- (0.9,0.77) -- (0.81,0.82) -- (0.72,0.85) -- (0.63,0.88) -- (0.53,0.91) -- (0.43,0.92) -- (0.32,0.93) -- (0.21,0.93) -- (0.1,0.93) -- (-0.01,0.91) -- (-0.12,0.9) -- (-0.23,0.87) -- (-0.34,0.84) -- (-0.45,0.8) -- (-0.55,0.75) -- (-0.65,0.7) -- (-0.74,0.65) -- (-0.83,0.58) -- (-0.91,0.52) -- (-0.99,0.45) -- (-1.05,0.38) -- (-1.11,0.3) -- (-1.16,0.22) -- (-1.2,0.14) -- (-1.24,0.06) -- (-1.26,-0.02) -- (-1.27,-0.1) -- (-1.28,-0.18) -- (-1.27,-0.26) -- (-1.26,-0.34) -- (-1.23,-0.41) -- (-1.2,-0.48) -- (-1.15,-0.55) -- (-1.1,-0.61) -- (-1.04,-0.67) -- (-0.97,-0.73) -- (-0.9,-0.77) -- (-0.81,-0.82) -- (-0.72,-0.85) -- (-0.63,-0.88) -- (-0.53,-0.91) -- (-0.43,-0.92) -- (-0.32,-0.93) -- (-0.21,-0.93) -- (-0.1,-0.93) -- (0.01,-0.91) -- (0.12,-0.9) -- (0.23,-0.87) -- (0.34,-0.84) -- (0.45,-0.8) -- (0.55,-0.75) -- (0.65,-0.7) -- (0.74,-0.65) -- (0.83,-0.58) -- (0.91,-0.52) -- (0.99,-0.45) -- (1.05,-0.38) -- (1.11,-0.3) -- (1.16,-0.22) -- (1.2,-0.14) -- (1.24,-0.06) -- (1.26,0.02) -- (1.27,0.1) -- (1.28,0.18) -- (1.27,0.26) -- cycle;
\draw[emph] (1.26,0.34) -- (1.23,0.41) -- (1.2,0.48) -- (1.15,0.55) -- (1.1,0.61) -- (1.04,0.67) -- (0.97,0.73) -- (0.9,0.77) -- (0.81,0.82) -- (0.72,0.85) -- (0.63,0.88) -- (0.53,0.91) -- (0.43,0.92) -- (0.32,0.93) -- (0.21,0.93) -- (0.1,0.93) -- (-0.01,0.91) -- (-0.12,0.9) -- (-0.23,0.87) -- (-0.34,0.84) -- (-0.45,0.8) -- (-0.55,0.75) -- (-0.65,0.7) -- (-0.74,0.65) -- (-0.83,0.58) -- (-0.91,0.52) -- (-0.99,0.45) -- (-1.05,0.38) -- (-1.11,0.3) -- (-1.16,0.22) -- (-1.2,0.14) -- (-1.24,0.06) -- (-1.26,-0.02) -- (-1.27,-0.1) -- (-1.28,-0.18) -- (-1.27,-0.26) -- (-1.26,-0.34) -- (-1.23,-0.41) -- (-1.2,-0.48) -- (-1.15,-0.55) -- (-1.1,-0.61) -- (-1.04,-0.67) -- (-0.97,-0.73) -- (-0.9,-0.77) -- (-0.81,-0.82) -- (-0.72,-0.85) -- (-0.63,-0.88) -- (-0.53,-0.91) -- (-0.43,-0.92) -- (-0.32,-0.93) -- (-0.21,-0.93) -- (-0.1,-0.93) -- (0.01,-0.91) -- (0.12,-0.9) -- (0.23,-0.87) -- (0.34,-0.84) -- (0.45,-0.8) -- (0.55,-0.75) -- (0.65,-0.7) -- (0.74,-0.65) -- (0.83,-0.58) -- (0.91,-0.52) -- (0.99,-0.45) -- (1.05,-0.38) -- (1.11,-0.3) -- (1.16,-0.22) -- (1.2,-0.14) -- (1.24,-0.06) -- (1.26,0.02) -- (1.27,0.1) -- (1.28,0.18) -- (1.27,0.26) -- cycle;
\draw[hl] (-0.8,-0.3) -- (0.7,0.5);
\fill[ink] (-0.8,-0.3) circle[pt];
\fill[ink] (0.7,0.5) circle[pt];
\node[lab] at (0,-1.25) {convex};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\fill[tintA] (1.3,-0) -- (1.3,0.05) -- (1.29,0.1) -- (1.28,0.15) -- (1.27,0.2) -- (1.26,0.25) -- (1.24,0.29) -- (1.21,0.34) -- (1.19,0.38) -- (1.16,0.42) -- (1.13,0.47) -- (1.09,0.5) -- (1.05,0.54) -- (1.01,0.56) -- (0.97,0.59) -- (0.92,0.6) -- (0.87,0.61) -- (0.82,0.61) -- (0.76,0.6) -- (0.71,0.58) -- (0.65,0.56) -- (0.59,0.52) -- (0.53,0.47) -- (0.47,0.42) -- (0.4,0.36) -- (0.34,0.31) -- (0.27,0.26) -- (0.2,0.21) -- (0.14,0.18) -- (0.07,0.16) -- (0,0.15) -- (-0.07,0.16) -- (-0.14,0.18) -- (-0.2,0.21) -- (-0.27,0.26) -- (-0.34,0.31) -- (-0.4,0.36) -- (-0.47,0.42) -- (-0.53,0.47) -- (-0.59,0.52) -- (-0.65,0.56) -- (-0.71,0.58) -- (-0.76,0.6) -- (-0.82,0.61) -- (-0.87,0.61) -- (-0.92,0.6) -- (-0.97,0.59) -- (-1.01,0.56) -- (-1.05,0.54) -- (-1.09,0.5) -- (-1.13,0.47) -- (-1.16,0.42) -- (-1.19,0.38) -- (-1.21,0.34) -- (-1.24,0.29) -- (-1.26,0.25) -- (-1.27,0.2) -- (-1.28,0.15) -- (-1.29,0.1) -- (-1.3,0.05) -- (-1.3,-0) -- (-1.3,-0.05) -- (-1.29,-0.1) -- (-1.28,-0.15) -- (-1.27,-0.2) -- (-1.26,-0.25) -- (-1.24,-0.29) -- (-1.21,-0.34) -- (-1.19,-0.39) -- (-1.16,-0.43) -- (-1.13,-0.48) -- (-1.09,-0.52) -- (-1.05,-0.56) -- (-1.01,-0.6) -- (-0.97,-0.64) -- (-0.92,-0.67) -- (-0.87,-0.71) -- (-0.82,-0.74) -- (-0.76,-0.77) -- (-0.71,-0.8) -- (-0.65,-0.82) -- (-0.59,-0.85) -- (-0.53,-0.87) -- (-0.47,-0.89) -- (-0.4,-0.9) -- (-0.34,-0.92) -- (-0.27,-0.93) -- (-0.2,-0.94) -- (-0.14,-0.94) -- (-0.07,-0.95) -- (0,-0.95) -- (0.07,-0.95) -- (0.14,-0.94) -- (0.2,-0.94) -- (0.27,-0.93) -- (0.34,-0.92) -- (0.4,-0.9) -- (0.47,-0.89) -- (0.53,-0.87) -- (0.59,-0.85) -- (0.65,-0.82) -- (0.71,-0.8) -- (0.76,-0.77) -- (0.82,-0.74) -- (0.87,-0.71) -- (0.92,-0.67) -- (0.97,-0.64) -- (1.01,-0.6) -- (1.05,-0.56) -- (1.09,-0.52) -- (1.13,-0.47) -- (1.16,-0.43) -- (1.19,-0.39) -- (1.21,-0.34) -- (1.24,-0.29) -- (1.26,-0.25) -- (1.27,-0.2) -- (1.28,-0.15) -- (1.29,-0.1) -- (1.3,-0.05) -- cycle;
\draw[emph] (1.3,-0) -- (1.3,0.05) -- (1.29,0.1) -- (1.28,0.15) -- (1.27,0.2) -- (1.26,0.25) -- (1.24,0.29) -- (1.21,0.34) -- (1.19,0.38) -- (1.16,0.42) -- (1.13,0.47) -- (1.09,0.5) -- (1.05,0.54) -- (1.01,0.56) -- (0.97,0.59) -- (0.92,0.6) -- (0.87,0.61) -- (0.82,0.61) -- (0.76,0.6) -- (0.71,0.58) -- (0.65,0.56) -- (0.59,0.52) -- (0.53,0.47) -- (0.47,0.42) -- (0.4,0.36) -- (0.34,0.31) -- (0.27,0.26) -- (0.2,0.21) -- (0.14,0.18) -- (0.07,0.16) -- (0,0.15) -- (-0.07,0.16) -- (-0.14,0.18) -- (-0.2,0.21) -- (-0.27,0.26) -- (-0.34,0.31) -- (-0.4,0.36) -- (-0.47,0.42) -- (-0.53,0.47) -- (-0.59,0.52) -- (-0.65,0.56) -- (-0.71,0.58) -- (-0.76,0.6) -- (-0.82,0.61) -- (-0.87,0.61) -- (-0.92,0.6) -- (-0.97,0.59) -- (-1.01,0.56) -- (-1.05,0.54) -- (-1.09,0.5) -- (-1.13,0.47) -- (-1.16,0.42) -- (-1.19,0.38) -- (-1.21,0.34) -- (-1.24,0.29) -- (-1.26,0.25) -- (-1.27,0.2) -- (-1.28,0.15) -- (-1.29,0.1) -- (-1.3,0.05) -- (-1.3,-0) -- (-1.3,-0.05) -- (-1.29,-0.1) -- (-1.28,-0.15) -- (-1.27,-0.2) -- (-1.26,-0.25) -- (-1.24,-0.29) -- (-1.21,-0.34) -- (-1.19,-0.39) -- (-1.16,-0.43) -- (-1.13,-0.48) -- (-1.09,-0.52) -- (-1.05,-0.56) -- (-1.01,-0.6) -- (-0.97,-0.64) -- (-0.92,-0.67) -- (-0.87,-0.71) -- (-0.82,-0.74) -- (-0.76,-0.77) -- (-0.71,-0.8) -- (-0.65,-0.82) -- (-0.59,-0.85) -- (-0.53,-0.87) -- (-0.47,-0.89) -- (-0.4,-0.9) -- (-0.34,-0.92) -- (-0.27,-0.93) -- (-0.2,-0.94) -- (-0.14,-0.94) -- (-0.07,-0.95) -- (0,-0.95) -- (0.07,-0.95) -- (0.14,-0.94) -- (0.2,-0.94) -- (0.27,-0.93) -- (0.34,-0.92) -- (0.4,-0.9) -- (0.47,-0.89) -- (0.53,-0.87) -- (0.59,-0.85) -- (0.65,-0.82) -- (0.71,-0.8) -- (0.76,-0.77) -- (0.82,-0.74) -- (0.87,-0.71) -- (0.92,-0.67) -- (0.97,-0.64) -- (1.01,-0.6) -- (1.05,-0.56) -- (1.09,-0.52) -- (1.13,-0.47) -- (1.16,-0.43) -- (1.19,-0.39) -- (1.21,-0.34) -- (1.24,-0.29) -- (1.26,-0.25) -- (1.27,-0.2) -- (1.28,-0.15) -- (1.29,-0.1) -- (1.3,-0.05) -- cycle;
\draw[hl] (-0.8,0.45) -- (0.8,0.45);
\fill[ink] (-0.8,0.45) circle[pt];
\fill[ink] (0.8,0.45) circle[pt];
\node[lab] at (0,-1.25) {not convex};
\end{tikzpicture}
\end{center}
```

Left: every segment between two points of the set stays inside, so the set is convex. Right: the notch lets a segment between two points of the set leave it, so the set is not convex.

:::

::: {#def-convex-combination .definition name="Convex combination, convex hull"}

A *convex combination* of $x_1,\dots,x_k$ is a point
$$\theta_1x_1+\cdots+\theta_kx_k,\qquad \theta_i\ge0,\quad \theta_1+\cdots+\theta_k=1.$$
The *convex hull* $\operatorname{conv}C$ of a set $C$ is the set of all convex combinations of points of $C$.

:::

::: {#fig-affine-and-convex-sets-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (1.6,-0.3) -- (2.4,0.8) -- (1.9,1.8) -- (0.5,1.6) -- (-0.3,0.9) -- cycle;
\draw[hl] (0,0) -- (1.6,-0.3) -- (2.4,0.8) -- (1.9,1.8) -- (0.5,1.6) -- (-0.3,0.9) -- cycle;
\fill[ink] (0,0) circle[pt];
\fill[ink] (1.6,-0.3) circle[pt];
\fill[ink] (2.4,0.8) circle[pt];
\fill[ink] (1.9,1.8) circle[pt];
\fill[ink] (0.5,1.6) circle[pt];
\fill[ink] (-0.3,0.9) circle[pt];
\fill[ink] (1,0.7) circle[pt];
\fill[ink] (1.5,1) circle[pt];
\fill[ink] (0.6,0.3) circle[pt];
\node[lab, above] at (1.1,0.95) {$\operatorname{conv}S$};
\end{tikzpicture}
\end{center}
```

The convex hull of nine points: the smallest convex polygon containing them. Its corners are points of $S$; every other point of the hull is a convex combination of them.

:::

::: {#prp-convex-hull-smallest .proposition name="The convex hull is the smallest convex superset"}

A set is convex (@def-convex-set) if and only if it contains every convex combination of its points. Consequently $\operatorname{conv}C$ is convex, and it is contained in every convex set that contains $C$.

:::

::: {.proof}

1. If a set contains all convex combinations of its points, it contains those with two points, so it is convex.

2. Conversely let $C$ be convex; induct on $k$. For $k=2$ this is the definition. For $k>2$ and $\theta_k<1$ write
$$\sum_{i=1}^k\theta_ix_i=(1-\theta_k)\,y+\theta_kx_k,\qquad y=\sum_{i<k}\frac{\theta_i}{1-\theta_k}x_i,$$
where $y\in C$ by induction (its weights are nonnegative and sum to $1$); then the two-point case applies. If $\theta_k=1$ the combination is $x_k$.

3. A convex combination of two convex combinations of points of $C$ is again a convex combination of points of $C$, so $\operatorname{conv}C$ is convex. Any convex $D\supseteq C$ contains all convex combinations of points of $C$ by step 2, so $D\supseteq\operatorname{conv}C$.

:::

::: {#def-convex-cone .definition name="Cone, convex cone, conic hull"}

A set $C$ is a *cone* if $x\in C$ and $\theta\ge0$ imply $\theta x\in C$. It is a *convex cone* if it is convex and a cone, equivalently if
$$x_1,x_2\in C,\ \theta_1,\theta_2\ge0\ \Longrightarrow\ \theta_1x_1+\theta_2x_2\in C.$$
A *conic combination* is $\sum_i\theta_ix_i$ with all $\theta_i\ge0$; the *conic hull* of $C$ is the set of all conic combinations of its points.

:::

::: {.proof}

1. The two descriptions agree. If $C$ is a convex cone and $\theta_1+\theta_2>0$, then $\theta_1x_1+\theta_2x_2=(\theta_1+\theta_2)\big(\tfrac{\theta_1}{\theta_1+\theta_2}x_1+\tfrac{\theta_2}{\theta_1+\theta_2}x_2\big)$ is a nonnegative multiple of a point of $C$; if $\theta_1=\theta_2=0$ it is $0=0\cdot x_1\in C$.

2. Conversely the displayed property with $\theta_2=0$ gives the cone property, and with $\theta_1+\theta_2=1$ gives convexity.

:::

::: {#fig-affine-and-convex-sets-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (3,0.75) -- (3,2.6) -- (1.06,2.6) -- cycle;
\draw[emph] (3,0.75) -- (0,0) -- (1.06,2.6);
\draw[->, hl] (0,0) -- (1.2,0.3) node[lab, below right] {$x_1$};
\draw[->, hl] (0,0) -- (0.45,1.1) node[lab, left] {$x_2$};
\draw[faint, dashed] (1.2,0.3) -- (1.65,1.4) -- (0.45,1.1);
\fill[ink] (1.65,1.4) circle[pt] node[lab, above right] {$\theta_1x_1+\theta_2x_2$};
\fill[ink] (0,0) circle[pt] node[lab, below left] {$0$};
\end{tikzpicture}
\end{center}
```

The conic hull of $x_1$ and $x_2$: all combinations $\theta_1x_1+\theta_2x_2$ with $\theta_1,\theta_2\ge0$ fill the wedge between the two rays from the origin.

:::

::: {#exm-hulls-in-plane .example name="Three hulls of two points"}

For $x_1=(1,0)$ and $x_2=(0,1)$ in $\mathbb{R}^2$: the affine hull is the line $u+v=1$; the convex hull is the segment between them; the conic hull is the quadrant $u,v\ge0$. Adding the origin as a third point makes the convex hull the triangle with vertices $0,x_1,x_2$ and leaves the conic hull unchanged.

:::

::: {#rmk-affine-and-convex-sets-1 .remark name="Each kind contains the next"}

Every subspace is an affine set and a convex cone; every affine set and every convex cone is convex. A set is a subspace exactly when it is both affine and a cone.

:::
