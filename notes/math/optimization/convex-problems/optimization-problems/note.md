---
title: "Optimization Problems and Convex Problems"
sources: [ee364a-4]
requires: [math/optimization/convex-functions/convex-functions]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on the introduction and on convex optimization problems, in our own wording; proofs written out in steps. -->

An optimization problem asks for the least value of an objective over the points that satisfy some constraints. When the objective and the inequality constraints are convex and the equality constraints affine, every local solution is global and optimality has a simple first-order description.

::: {#def-optimization-problem .definition name="Optimization problem in standard form"}

An optimization problem in standard form is
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\le0,\quad i=1,\dots,m,\\ &h_i(x)=0,\quad i=1,\dots,p,\end{array}$$
with variable $x\in\mathbb{R}^n$, objective $f_0$, inequality constraints $f_i$ and equality constraints $h_i$. Its *domain* is $\mathcal D=\bigcap_i\operatorname{dom}f_i\cap\bigcap_i\operatorname{dom}h_i$; a point of $\mathcal D$ satisfying all constraints is *feasible*. The *optimal value* is
$$p^\star=\inf\{f_0(x)\mid x\text{ feasible}\},$$
with $p^\star=+\infty$ if no point is feasible and $p^\star=-\infty$ if the problem is *unbounded below*. A feasible $x$ with $f_0(x)=p^\star$ is *optimal*; $x$ is *locally optimal* if it is optimal for the problem with the extra constraint $\lVert z-x\rVert_2\le R$ for some $R>0$.

:::

::: {#exm-optimal-values .example name="Optimal values on the line"}

1. $f_0(x)=1/x$ on $x>0$: $p^\star=0$, not attained.

2. $f_0(x)=-\log x$ on $x>0$: $p^\star=-\infty$.

3. $f_0(x)=x\log x$ on $x>0$: $p^\star=-1/e$, attained at $x=1/e$.

4. $f_0(x)=x^3-3x$: $p^\star=-\infty$; $x=1$ is locally optimal.

:::

::: {#fig-optimization-problems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (0.05,0) -- (3,0) node[lab, right] {};
\draw[->, faint] (0,-0.4) -- (0,2.4) node[lab, above] {};
\draw[emph] (0.42,2.38) -- (0.44,2.27) -- (0.46,2.16) -- (0.48,2.07) -- (0.51,1.98) -- (0.53,1.9) -- (0.55,1.83) -- (0.57,1.76) -- (0.59,1.69) -- (0.61,1.64) -- (0.63,1.58) -- (0.65,1.53) -- (0.68,1.48) -- (0.7,1.44) -- (0.72,1.39) -- (0.74,1.35) -- (0.76,1.32) -- (0.78,1.28) -- (0.8,1.25) -- (0.82,1.21) -- (0.84,1.18) -- (0.87,1.15) -- (0.89,1.13) -- (0.91,1.1) -- (0.93,1.08) -- (0.95,1.05) -- (0.97,1.03) -- (0.99,1.01) -- (1.02,0.99) -- (1.04,0.97) -- (1.06,0.95) -- (1.08,0.93) -- (1.1,0.91) -- (1.12,0.89) -- (1.14,0.88) -- (1.16,0.86) -- (1.19,0.84) -- (1.21,0.83) -- (1.23,0.81) -- (1.25,0.8) -- (1.27,0.79) -- (1.29,0.77) -- (1.31,0.76) -- (1.33,0.75) -- (1.35,0.74) -- (1.38,0.73) -- (1.4,0.72) -- (1.42,0.7) -- (1.44,0.69) -- (1.46,0.68) -- (1.48,0.67) -- (1.5,0.67) -- (1.52,0.66) -- (1.55,0.65) -- (1.57,0.64) -- (1.59,0.63) -- (1.61,0.62) -- (1.63,0.61) -- (1.65,0.61) -- (1.67,0.6) -- (1.69,0.59) -- (1.72,0.58) -- (1.74,0.58) -- (1.76,0.57) -- (1.78,0.56) -- (1.8,0.56) -- (1.82,0.55) -- (1.84,0.54) -- (1.86,0.54) -- (1.89,0.53) -- (1.91,0.52) -- (1.93,0.52) -- (1.95,0.51) -- (1.97,0.51) -- (1.99,0.5) -- (2.01,0.5) -- (2.04,0.49) -- (2.06,0.49) -- (2.08,0.48) -- (2.1,0.48) -- (2.12,0.47) -- (2.14,0.47) -- (2.16,0.46) -- (2.18,0.46) -- (2.21,0.45) -- (2.23,0.45) -- (2.25,0.44) -- (2.27,0.44) -- (2.29,0.44) -- (2.31,0.43) -- (2.33,0.43) -- (2.35,0.42) -- (2.37,0.42) -- (2.4,0.42) -- (2.42,0.41) -- (2.44,0.41) -- (2.46,0.41) -- (2.48,0.4) -- (2.5,0.4) -- (2.52,0.4) -- (2.54,0.39) -- (2.57,0.39) -- (2.59,0.39) -- (2.61,0.38) -- (2.63,0.38) -- (2.65,0.38) -- (2.67,0.37) -- (2.69,0.37) -- (2.71,0.37) -- (2.74,0.37) -- (2.76,0.36) -- (2.78,0.36) -- (2.8,0.36);
\draw[faint, dashed] (0,0) -- (2.8,0);
\node[lab] at (1.52,-0.75) {$1/x$: $p^\star=0$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-0.08,0) -- (3,0) node[lab, right] {};
\draw[->, faint] (0,-1.2) -- (0,2.2) node[lab, above] {};
\draw[emph] (0.12,2.12) -- (0.14,1.95) -- (0.16,1.8) -- (0.19,1.68) -- (0.21,1.56) -- (0.23,1.46) -- (0.25,1.37) -- (0.28,1.29) -- (0.3,1.21) -- (0.32,1.14) -- (0.34,1.07) -- (0.37,1.01) -- (0.39,0.95) -- (0.41,0.89) -- (0.43,0.84) -- (0.45,0.79) -- (0.48,0.74) -- (0.5,0.69) -- (0.52,0.65) -- (0.54,0.61) -- (0.57,0.57) -- (0.59,0.53) -- (0.61,0.49) -- (0.63,0.46) -- (0.66,0.42) -- (0.68,0.39) -- (0.7,0.36) -- (0.72,0.32) -- (0.75,0.29) -- (0.77,0.26) -- (0.79,0.24) -- (0.81,0.21) -- (0.83,0.18) -- (0.86,0.15) -- (0.88,0.13) -- (0.9,0.1) -- (0.92,0.08) -- (0.95,0.06) -- (0.97,0.03) -- (0.99,0.01) -- (1.01,-0.01) -- (1.04,-0.04) -- (1.06,-0.06) -- (1.08,-0.08) -- (1.1,-0.1) -- (1.12,-0.12) -- (1.15,-0.14) -- (1.17,-0.16) -- (1.19,-0.18) -- (1.21,-0.19) -- (1.24,-0.21) -- (1.26,-0.23) -- (1.28,-0.25) -- (1.3,-0.27) -- (1.33,-0.28) -- (1.35,-0.3) -- (1.37,-0.32) -- (1.39,-0.33) -- (1.42,-0.35) -- (1.44,-0.36) -- (1.46,-0.38) -- (1.48,-0.39) -- (1.5,-0.41) -- (1.53,-0.42) -- (1.55,-0.44) -- (1.57,-0.45) -- (1.59,-0.47) -- (1.62,-0.48) -- (1.64,-0.49) -- (1.66,-0.51) -- (1.68,-0.52) -- (1.71,-0.53) -- (1.73,-0.55) -- (1.75,-0.56) -- (1.77,-0.57) -- (1.79,-0.59) -- (1.82,-0.6) -- (1.84,-0.61) -- (1.86,-0.62) -- (1.88,-0.63) -- (1.91,-0.65) -- (1.93,-0.66) -- (1.95,-0.67) -- (1.97,-0.68) -- (2,-0.69) -- (2.02,-0.7) -- (2.04,-0.71) -- (2.06,-0.72) -- (2.09,-0.73) -- (2.11,-0.75) -- (2.13,-0.76) -- (2.15,-0.77) -- (2.17,-0.78) -- (2.2,-0.79) -- (2.22,-0.8) -- (2.24,-0.81) -- (2.26,-0.82) -- (2.29,-0.83) -- (2.31,-0.84) -- (2.33,-0.85) -- (2.35,-0.86) -- (2.38,-0.87) -- (2.4,-0.87) -- (2.42,-0.88) -- (2.44,-0.89) -- (2.46,-0.9) -- (2.49,-0.91) -- (2.51,-0.92) -- (2.53,-0.93) -- (2.55,-0.94) -- (2.58,-0.95) -- (2.6,-0.96) -- (2.62,-0.96) -- (2.64,-0.97) -- (2.67,-0.98) -- (2.69,-0.99) -- (2.71,-1) -- (2.73,-1.01) -- (2.76,-1.01) -- (2.78,-1.02) -- (2.8,-1.03);
\node[lab] at (1.46,-1.55) {$-\log x$: $p^\star=-\infty$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-0.18,0) -- (2.4,0) node[lab, right] {};
\draw[->, faint] (0,-0.8) -- (0,2) node[lab, above] {};
\draw[emph] (0.02,-0.08) -- (0.04,-0.12) -- (0.06,-0.16) -- (0.07,-0.19) -- (0.09,-0.22) -- (0.11,-0.24) -- (0.13,-0.26) -- (0.15,-0.28) -- (0.17,-0.3) -- (0.18,-0.31) -- (0.2,-0.32) -- (0.22,-0.33) -- (0.24,-0.34) -- (0.26,-0.35) -- (0.27,-0.35) -- (0.29,-0.36) -- (0.31,-0.36) -- (0.33,-0.37) -- (0.35,-0.37) -- (0.37,-0.37) -- (0.38,-0.37) -- (0.4,-0.37) -- (0.42,-0.36) -- (0.44,-0.36) -- (0.46,-0.36) -- (0.47,-0.35) -- (0.49,-0.35) -- (0.51,-0.34) -- (0.53,-0.34) -- (0.55,-0.33) -- (0.57,-0.32) -- (0.58,-0.31) -- (0.6,-0.31) -- (0.62,-0.3) -- (0.64,-0.29) -- (0.66,-0.28) -- (0.67,-0.27) -- (0.69,-0.25) -- (0.71,-0.24) -- (0.73,-0.23) -- (0.75,-0.22) -- (0.76,-0.21) -- (0.78,-0.19) -- (0.8,-0.18) -- (0.82,-0.16) -- (0.84,-0.15) -- (0.86,-0.13) -- (0.87,-0.12) -- (0.89,-0.1) -- (0.91,-0.09) -- (0.93,-0.07) -- (0.95,-0.05) -- (0.96,-0.03) -- (0.98,-0.02) -- (1,0) -- (1.02,0.02) -- (1.04,0.04) -- (1.06,0.06) -- (1.07,0.08) -- (1.09,0.1) -- (1.11,0.12) -- (1.13,0.14) -- (1.15,0.16) -- (1.16,0.18) -- (1.18,0.2) -- (1.2,0.22) -- (1.22,0.24) -- (1.24,0.26) -- (1.26,0.29) -- (1.27,0.31) -- (1.29,0.33) -- (1.31,0.35) -- (1.33,0.38) -- (1.35,0.4) -- (1.36,0.42) -- (1.38,0.45) -- (1.4,0.47) -- (1.42,0.5) -- (1.44,0.52) -- (1.46,0.55) -- (1.47,0.57) -- (1.49,0.6) -- (1.51,0.62) -- (1.53,0.65) -- (1.55,0.67) -- (1.56,0.7) -- (1.58,0.73) -- (1.6,0.75) -- (1.62,0.78) -- (1.64,0.81) -- (1.66,0.83) -- (1.67,0.86) -- (1.69,0.89) -- (1.71,0.92) -- (1.73,0.94) -- (1.75,0.97) -- (1.76,1) -- (1.78,1.03) -- (1.8,1.06) -- (1.82,1.09) -- (1.84,1.12) -- (1.85,1.15) -- (1.87,1.18) -- (1.89,1.21) -- (1.91,1.23) -- (1.93,1.26) -- (1.95,1.3) -- (1.96,1.33) -- (1.98,1.36) -- (2,1.39) -- (2.02,1.42) -- (2.04,1.45) -- (2.05,1.48) -- (2.07,1.51) -- (2.09,1.54) -- (2.11,1.57) -- (2.13,1.61) -- (2.15,1.64) -- (2.16,1.67) -- (2.18,1.7) -- (2.2,1.73);
\fill[accent] (0.37,-0.37) circle[pt];
\node[lab] at (1.11,-1.15) {$x\log x$: $p^\star=-1/e$};
\end{tikzpicture}
\hspace{1.2em}
\begin{tikzpicture}
\draw[->, faint] (-2.2,0) -- (2.2,0) node[lab, right] {};
\draw[->, faint] (0,-1.6) -- (0,1.6) node[lab, above] {};
\draw[emph] (-2,-1) -- (-1.97,-0.85) -- (-1.93,-0.71) -- (-1.9,-0.58) -- (-1.87,-0.45) -- (-1.83,-0.33) -- (-1.8,-0.22) -- (-1.77,-0.11) -- (-1.73,-0) -- (-1.7,0.09) -- (-1.67,0.19) -- (-1.63,0.27) -- (-1.6,0.35) -- (-1.57,0.43) -- (-1.53,0.5) -- (-1.5,0.56) -- (-1.47,0.62) -- (-1.43,0.68) -- (-1.4,0.73) -- (-1.37,0.77) -- (-1.33,0.81) -- (-1.3,0.85) -- (-1.27,0.88) -- (-1.23,0.91) -- (-1.2,0.94) -- (-1.17,0.96) -- (-1.13,0.97) -- (-1.1,0.98) -- (-1.07,0.99) -- (-1.03,1) -- (-1,1) -- (-0.97,1) -- (-0.93,0.99) -- (-0.9,0.99) -- (-0.87,0.97) -- (-0.83,0.96) -- (-0.8,0.94) -- (-0.77,0.92) -- (-0.73,0.9) -- (-0.7,0.88) -- (-0.67,0.85) -- (-0.63,0.82) -- (-0.6,0.79) -- (-0.57,0.76) -- (-0.53,0.72) -- (-0.5,0.69) -- (-0.47,0.65) -- (-0.43,0.61) -- (-0.4,0.57) -- (-0.37,0.53) -- (-0.33,0.48) -- (-0.3,0.44) -- (-0.27,0.39) -- (-0.23,0.34) -- (-0.2,0.3) -- (-0.17,0.25) -- (-0.13,0.2) -- (-0.1,0.15) -- (-0.07,0.1) -- (-0.03,0.05) -- (0,0) -- (0.03,-0.05) -- (0.07,-0.1) -- (0.1,-0.15) -- (0.13,-0.2) -- (0.17,-0.25) -- (0.2,-0.3) -- (0.23,-0.34) -- (0.27,-0.39) -- (0.3,-0.44) -- (0.33,-0.48) -- (0.37,-0.53) -- (0.4,-0.57) -- (0.43,-0.61) -- (0.47,-0.65) -- (0.5,-0.69) -- (0.53,-0.72) -- (0.57,-0.76) -- (0.6,-0.79) -- (0.63,-0.82) -- (0.67,-0.85) -- (0.7,-0.88) -- (0.73,-0.9) -- (0.77,-0.92) -- (0.8,-0.94) -- (0.83,-0.96) -- (0.87,-0.97) -- (0.9,-0.99) -- (0.93,-0.99) -- (0.97,-1) -- (1,-1) -- (1.03,-1) -- (1.07,-0.99) -- (1.1,-0.98) -- (1.13,-0.97) -- (1.17,-0.96) -- (1.2,-0.94) -- (1.23,-0.91) -- (1.27,-0.88) -- (1.3,-0.85) -- (1.33,-0.81) -- (1.37,-0.77) -- (1.4,-0.73) -- (1.43,-0.68) -- (1.47,-0.62) -- (1.5,-0.56) -- (1.53,-0.5) -- (1.57,-0.43) -- (1.6,-0.35) -- (1.63,-0.27) -- (1.67,-0.19) -- (1.7,-0.09) -- (1.73,0) -- (1.77,0.11) -- (1.8,0.22) -- (1.83,0.33) -- (1.87,0.45) -- (1.9,0.58) -- (1.93,0.71) -- (1.97,0.85) -- (2,1);
\fill[accent] (1,-1) circle[pt];
\node[lab] at (0,-1.95) {$x^3-3x$ (scaled)};
\end{tikzpicture}
\end{center}
```

The four objectives: $1/x$ approaches $0$ but never reaches it; $-\log x$ is unbounded below; $x\log x$ attains $-1/e$ at $x=1/e$; $x^3-3x$ has a local minimum at $x=1$ (dot) but is unbounded below.

:::

::: {#def-convex-optimization-problem .definition name="Convex optimization problem"}

A *convex optimization problem* is a problem in standard form whose objective $f_0$ and inequality constraint functions $f_1,\dots,f_m$ are convex and whose equality constraints are affine:
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\le0,\quad i=1,\dots,m,\\ &Ax=b.\end{array}$$
Its feasible set is convex, as an intersection of sublevel sets of convex functions and an affine set. A *feasibility problem* is the special case $f_0=0$, where $p^\star$ is $0$ or $+\infty$.

:::

::: {#rmk-optimization-problems-1 .remark name="Convexity depends on the description"}

The problem of minimizing $x_1^2+x_2^2$ subject to $x_1/(1+x_2^2)\le0$ and $(x_1+x_2)^2=0$ is not a convex problem as written, although its feasible set $\{x\mid x_1=-x_2\le0\}$ is convex. Replacing the constraints by $x_1\le0$ and $x_1+x_2=0$ gives an equivalent convex problem.

:::

::: {#thm-convex-local-global .theorem name="Local optima of convex problems are global"}

For a convex optimization problem, every locally optimal point is optimal.

:::

::: {.proof}

1. Let $x$ be locally optimal with radius $R$ and suppose a feasible $y$ has $f_0(y)<f_0(x)$. Then $\lVert y-x\rVert_2>R$.

2. Put $z=(1-\theta)x+\theta y$ with $\theta=\frac{R}{2\lVert y-x\rVert_2}\in(0,\tfrac12)$. Then $z$ is feasible (the feasible set is convex) and $\lVert z-x\rVert_2=R/2$.

3. Convexity of $f_0$ gives $f_0(z)\le(1-\theta)f_0(x)+\theta f_0(y)<f_0(x)$, contradicting local optimality.

:::

::: {#thm-convex-optimality-criterion .theorem name="Optimality criterion for differentiable objectives"}

Let $f_0$ be differentiable in a convex problem with feasible set $X$. Then $x\in X$ is optimal if and only if
$$\nabla f_0(x)^{\mathsf T}(y-x)\ge0\qquad\text{for all }y\in X.$$
Special cases: unconstrained, $\nabla f_0(x)=0$; with only $Ax=b$, there is $\nu$ with $\nabla f_0(x)+A^{\mathsf T}\nu=0$; on $x\succeq0$, $\nabla f_0(x)\succeq0$ and $x_i(\nabla f_0(x))_i=0$ for each $i$.

:::

::: {.proof}

1. If the condition holds, the first-order condition (@thm-first-order-convexity) gives $f_0(y)\ge f_0(x)+\nabla f_0(x)^{\mathsf T}(y-x)\ge f_0(x)$ for $y\in X$.

2. Conversely, if $\nabla f_0(x)^{\mathsf T}(y-x)<0$ for some $y\in X$, the points $z(t)=x+t(y-x)$, $0<t\le1$, are feasible and $\frac{d}{dt}f_0(z(t))\big|_{t=0}<0$, so $f_0(z(t))<f_0(x)$ for small $t$.

3. Unconstrained: take $y=x-t\nabla f_0(x)$ to get $-t\lVert\nabla f_0(x)\rVert_2^2\ge0$.

4. Equality constraints: $y-x$ ranges over $\operatorname{null}A$, a subspace, so $\nabla f_0(x)^{\mathsf T}v\ge0$ for $\pm v$ forces $\nabla f_0(x)\perp\operatorname{null}A$, that is, $\nabla f_0(x)\in\operatorname{range}A^{\mathsf T}$.

5. Nonnegative orthant: $\nabla f_0(x)^{\mathsf T}y\ge\nabla f_0(x)^{\mathsf T}x$ for all $y\succeq0$ forces $\nabla f_0(x)\succeq0$ (else let one $y_i\to\infty$) and then, with $y=0$, $\nabla f_0(x)^{\mathsf T}x\le0$, a sum of nonnegative terms, so each term is $0$.

:::

::: {#fig-optimization-problems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) -- (2,-0.2) -- (2.6,1.2) -- (1.4,2) -- (0,1.4) -- cycle;
\draw[emph] (0,0) -- (2,-0.2) -- (2.6,1.2) -- (1.4,2) -- (0,1.4) -- cycle;
\node[lab] at (1,0.7) {$X$};
\begin{scope}\clip (-0.5,-0.6) rectangle (4.4,3.4); \draw[faint] (3.6,2.8) circle (1.89); \end{scope}
\begin{scope}\clip (-0.5,-0.6) rectangle (4.4,3.4); \draw[faint] (3.6,2.8) circle (2.39); \end{scope}
\begin{scope}\clip (-0.5,-0.6) rectangle (4.4,3.4); \draw[faint] (3.6,2.8) circle (2.89); \end{scope}
\fill[ink] (3.6,2.8) circle[pt] node[lab, right] {$\text{argmin}\,f_0$};
\fill[accent] (2.55,1.23) circle[pt] node[lab, below right] {$x$};
\draw[->, hl] (2.55,1.23) -- (3,1.9) node[lab, above left] {$-\nabla f_0(x)$};
\draw[emph, dashed] (1.47,1.95) -- (3.64,0.51);
\end{tikzpicture}
\end{center}
```

The optimality criterion: at the optimal $x$, the hyperplane through $x$ normal to $\nabla f_0(x)$ (dashed) supports the feasible set $X$, so $\nabla f_0(x)^{\mathsf T}(y-x)\ge0$ for every feasible $y$. Circles are level curves of $f_0$.

:::

::: {#exm-optimality-criterion-box .example name="A one-variable check"}

Minimize $(x-2)^2$ over $X=[0,1]$. At $x=1$, $f_0'(1)=-2$ and $f_0'(1)(y-1)=-2(y-1)\ge0$ for every $y\le1$, so $x=1$ is optimal. At $x=0.5$ the choice $y=1$ gives $-3\cdot0.5<0$, so it is not.

:::

::: {#fig-optimization-problems-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.6,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,4.4) node[lab, above] {$y$};
\draw[emph] (-0.05,4.2) -- (0,3.99) -- (0.05,3.78) -- (0.11,3.58) -- (0.16,3.39) -- (0.21,3.2) -- (0.26,3.02) -- (0.31,2.84) -- (0.36,2.67) -- (0.42,2.51) -- (0.47,2.35) -- (0.52,2.19) -- (0.57,2.04) -- (0.62,1.9) -- (0.68,1.76) -- (0.73,1.62) -- (0.78,1.49) -- (0.83,1.37) -- (0.88,1.25) -- (0.93,1.14) -- (0.99,1.03) -- (1.04,0.93) -- (1.09,0.83) -- (1.14,0.74) -- (1.19,0.65) -- (1.24,0.57) -- (1.29,0.5) -- (1.35,0.43) -- (1.4,0.36) -- (1.45,0.3) -- (1.5,0.25) -- (1.55,0.2) -- (1.6,0.16) -- (1.66,0.12) -- (1.71,0.09) -- (1.76,0.06) -- (1.81,0.04) -- (1.86,0.02) -- (1.92,0.01) -- (1.97,0) -- (2.02,0) -- (2.07,0) -- (2.12,0.01) -- (2.17,0.03) -- (2.23,0.05) -- (2.28,0.08) -- (2.33,0.11) -- (2.38,0.14) -- (2.43,0.19) -- (2.48,0.23) -- (2.53,0.29) -- (2.59,0.34) -- (2.64,0.41) -- (2.69,0.48) -- (2.74,0.55) -- (2.79,0.63) -- (2.85,0.71) -- (2.9,0.8) -- (2.95,0.9) -- (3,1);
\draw[hl] (0,0) -- (1,0);
\node[lab] at (0.5,-0.3) {$X$};
\draw[faint] (0.3,2.4) -- (0.95,1.1) -- (1.6,-0.2);
\fill[accent] (1,1) circle[pt] node[lab, below left] {$x=1$};
\fill[ink] (0.5,2.25) circle[pt] node[lab, left] {$x=0.5$};
\end{tikzpicture}
\end{center}
```

Minimizing $(x-2)^2$ over $X=[0,1]$: the slope at $x=1$ is $-2$, so every feasible move ($y\le1$) goes uphill; at $x=0.5$ moving right goes downhill, so $0.5$ is not optimal.

:::
