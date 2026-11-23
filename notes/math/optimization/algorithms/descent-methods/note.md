---
title: "Descent Methods for Unconstrained Minimization"
sources: [ee364a-10]
requires: [math/optimization/convex-problems/optimization-problems]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on unconstrained minimization, in our own wording; proofs written out in steps. Gradient descent with a fixed step is in @sec-ai-machine-learning-gradient-descent; this note adds line searches and the linear convergence rate under strong convexity. Iterates in the figure computed in Python. -->

A descent method moves from $x$ along a direction $\Delta x$ that decreases $f$, with a step size chosen by a line search. Under strong convexity, gradient descent with a backtracking line search converges linearly, with a rate governed by the condition number.

::: {#def-strong-convexity .definition name="Strong convexity"}

A twice differentiable convex $f$ is *strongly convex* on a set $S$ if there are $0<m\le M$ with
$$mI\preceq\nabla^2f(x)\preceq MI\qquad\text{for all }x\in S.$$
Then, for $x,y\in S$ (with $S$ convex),
$$f(y)\ge f(x)+\nabla f(x)^{\mathsf T}(y-x)+\tfrac m2\lVert y-x\rVert_2^2,\qquad f(y)\le f(x)+\nabla f(x)^{\mathsf T}(y-x)+\tfrac M2\lVert y-x\rVert_2^2.$$

:::

::: {.proof}

1. By Taylor's theorem with remainder, $f(y)=f(x)+\nabla f(x)^{\mathsf T}(y-x)+\frac12(y-x)^{\mathsf T}\nabla^2f(z)(y-x)$ for some $z$ on the segment.

2. The bounds on $\nabla^2f(z)$ give the two inequalities.

:::

::: {#fig-descent-methods-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-2.4,0) -- (2.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.4) -- (0,3) node[lab, above] {$y$};
\draw[emph] (-2.2,2.76) -- (-2.12,2.61) -- (-2.05,2.46) -- (-1.97,2.32) -- (-1.89,2.18) -- (-1.82,2.05) -- (-1.74,1.92) -- (-1.66,1.8) -- (-1.59,1.69) -- (-1.51,1.57) -- (-1.43,1.47) -- (-1.36,1.37) -- (-1.28,1.28) -- (-1.2,1.2) -- (-1.13,1.12) -- (-1.05,1.05) -- (-0.97,0.99) -- (-0.9,0.94) -- (-0.82,0.89) -- (-0.74,0.85) -- (-0.67,0.83) -- (-0.59,0.8) -- (-0.51,0.79) -- (-0.44,0.79) -- (-0.36,0.79) -- (-0.28,0.8) -- (-0.21,0.82) -- (-0.13,0.84) -- (-0.05,0.87) -- (0.02,0.91) -- (0.1,0.95) -- (0.18,1) -- (0.25,1.06) -- (0.33,1.11) -- (0.41,1.18) -- (0.48,1.24) -- (0.56,1.31) -- (0.64,1.39) -- (0.71,1.47) -- (0.79,1.55) -- (0.87,1.63) -- (0.94,1.72) -- (1.02,1.82) -- (1.1,1.91) -- (1.17,2.01) -- (1.25,2.12) -- (1.33,2.22) -- (1.4,2.34) -- (1.48,2.46) -- (1.56,2.58) -- (1.63,2.71) -- (1.71,2.85);
\draw[faint] (-2.2,1.02) -- (-2.14,0.98) -- (-2.08,0.94) -- (-2.03,0.9) -- (-1.97,0.87) -- (-1.91,0.84) -- (-1.86,0.8) -- (-1.8,0.78) -- (-1.74,0.75) -- (-1.68,0.72) -- (-1.63,0.7) -- (-1.57,0.68) -- (-1.51,0.66) -- (-1.45,0.65) -- (-1.4,0.63) -- (-1.34,0.62) -- (-1.28,0.61) -- (-1.22,0.6) -- (-1.17,0.59) -- (-1.11,0.59) -- (-1.05,0.59) -- (-0.99,0.58) -- (-0.94,0.59) -- (-0.88,0.59) -- (-0.82,0.59) -- (-0.76,0.6) -- (-0.71,0.61) -- (-0.65,0.62) -- (-0.59,0.63) -- (-0.53,0.65) -- (-0.48,0.67) -- (-0.42,0.69) -- (-0.36,0.71) -- (-0.3,0.73) -- (-0.25,0.76) -- (-0.19,0.78) -- (-0.13,0.81) -- (-0.07,0.84) -- (-0.02,0.88) -- (0.04,0.91) -- (0.1,0.95) -- (0.16,0.99) -- (0.21,1.03) -- (0.27,1.07) -- (0.33,1.11) -- (0.39,1.16) -- (0.44,1.21) -- (0.5,1.26) -- (0.56,1.31) -- (0.62,1.37) -- (0.67,1.43) -- (0.73,1.48) -- (0.79,1.54) -- (0.85,1.61) -- (0.9,1.67) -- (0.96,1.74) -- (1.02,1.81) -- (1.08,1.88) -- (1.13,1.95) -- (1.19,2.03) -- (1.25,2.1) -- (1.31,2.18) -- (1.36,2.26) -- (1.42,2.34) -- (1.48,2.43) -- (1.54,2.51) -- (1.59,2.6) -- (1.65,2.69) -- (1.71,2.79) -- (1.77,2.88);
\draw[faint, dashed] (-1.86,2.84) -- (-1.8,2.71) -- (-1.74,2.58) -- (-1.68,2.46) -- (-1.63,2.34) -- (-1.57,2.23) -- (-1.51,2.12) -- (-1.45,2.02) -- (-1.4,1.92) -- (-1.34,1.83) -- (-1.28,1.74) -- (-1.22,1.65) -- (-1.17,1.57) -- (-1.11,1.5) -- (-1.05,1.43) -- (-0.99,1.36) -- (-0.94,1.3) -- (-0.88,1.24) -- (-0.82,1.19) -- (-0.76,1.14) -- (-0.71,1.1) -- (-0.65,1.06) -- (-0.59,1.03) -- (-0.53,1) -- (-0.48,0.97) -- (-0.42,0.95) -- (-0.36,0.94) -- (-0.3,0.93) -- (-0.25,0.92) -- (-0.19,0.92) -- (-0.13,0.92) -- (-0.07,0.93) -- (-0.02,0.94) -- (0.04,0.96) -- (0.1,0.98) -- (0.16,1.01) -- (0.21,1.04) -- (0.27,1.08) -- (0.33,1.12) -- (0.39,1.16) -- (0.44,1.21) -- (0.5,1.27) -- (0.56,1.32) -- (0.62,1.39) -- (0.67,1.46) -- (0.73,1.53) -- (0.79,1.61) -- (0.85,1.69) -- (0.9,1.77) -- (0.96,1.87) -- (1.02,1.96) -- (1.08,2.06) -- (1.13,2.17) -- (1.19,2.28) -- (1.25,2.39) -- (1.31,2.51) -- (1.36,2.63) -- (1.42,2.76) -- (1.48,2.89);
\fill[ink] (0.4,1.17) circle[pt] node[lab, below right] {$x$};
\end{tikzpicture}
\end{center}
```

Strong convexity with $mI\preceq\nabla^2f\preceq MI$: at every $x$ the graph lies between two quadratics touching it there, one of curvature $m$ (below, thin) and one of curvature $M$ (above, dashed). These bounds drive the convergence analysis of descent methods.

:::

::: {#cor-strong-convexity-gap .corollary name="Suboptimality from the gradient"}

Under @def-strong-convexity on the sublevel set $S=\{x\mid f(x)\le f(x^{(0)})\}$,
$$f(x)-p^\star\le\frac{1}{2m}\lVert\nabla f(x)\rVert_2^2.$$

:::

::: {.proof}

1. The lower bound of @def-strong-convexity, as a function of $y$, is minimized at $y=x-\frac1m\nabla f(x)$, with value $f(x)-\frac1{2m}\lVert\nabla f(x)\rVert_2^2$.

2. So $p^\star\ge f(x)-\frac1{2m}\lVert\nabla f(x)\rVert_2^2$.

:::

::: {#def-descent-method .definition name="General descent method, backtracking line search"}

A *descent method* repeats: choose a descent direction $\Delta x$ ($\nabla f(x)^{\mathsf T}\Delta x<0$); choose a step $t>0$; set $x:=x+t\Delta x$; until a stopping criterion holds. *Exact line search* takes $t=\operatorname{argmin}_{s>0}f(x+s\Delta x)$. *Backtracking line search* with parameters $\alpha\in(0,\frac12)$, $\beta\in(0,1)$ starts at $t=1$ and repeats $t:=\beta t$ while
$$f(x+t\Delta x)>f(x)+\alpha t\nabla f(x)^{\mathsf T}\Delta x.$$
*Gradient descent* uses $\Delta x=-\nabla f(x)$ and stops when $\lVert\nabla f(x)\rVert_2\le\epsilon$.

:::

::: {#fig-descent-methods-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (2.4,0) node[lab, right] {$t$};
\draw[->, faint] (0,-0.4) -- (0,1.8) node[lab, above] {};
\draw[emph] (0,1.6) -- (0.04,1.49) -- (0.07,1.39) -- (0.11,1.3) -- (0.15,1.21) -- (0.18,1.12) -- (0.22,1.04) -- (0.26,0.96) -- (0.29,0.89) -- (0.33,0.82) -- (0.37,0.76) -- (0.4,0.69) -- (0.44,0.64) -- (0.48,0.59) -- (0.51,0.54) -- (0.55,0.5) -- (0.59,0.46) -- (0.62,0.42) -- (0.66,0.39) -- (0.7,0.37) -- (0.73,0.34) -- (0.77,0.33) -- (0.81,0.31) -- (0.84,0.31) -- (0.88,0.3) -- (0.92,0.3) -- (0.95,0.3) -- (0.99,0.31) -- (1.03,0.33) -- (1.06,0.34) -- (1.1,0.36) -- (1.14,0.39) -- (1.17,0.42) -- (1.21,0.45) -- (1.25,0.49) -- (1.28,0.54) -- (1.32,0.58) -- (1.36,0.63) -- (1.39,0.69) -- (1.43,0.75) -- (1.47,0.81) -- (1.5,0.88) -- (1.54,0.96) -- (1.58,1.03) -- (1.61,1.11) -- (1.65,1.2) -- (1.69,1.29) -- (1.72,1.38) -- (1.76,1.48) -- (1.8,1.59) -- (1.83,1.69);
\draw[faint] (0,1.6) -- (0.3,0.73) -- (0.6,-0.13);
\draw[emph, dashed] (0,1.6) -- (1.1,0.65) -- (2.2,-0.3);
\draw[hl] (0,0) -- (1.26,0);
\draw[faint] (1.26,0) -- (1.26,0.51);
\node[lab, right] at (2.2,-0.3) {$f(x)+\alpha t\nabla f^{\mathsf T}\Delta x$};
\node[lab] at (0.63,-0.25) {accepted $t$};
\node[lab, right] at (1.9,1.9) {$f(x+t\Delta x)$};
\end{tikzpicture}
\end{center}
```

Backtracking line search: a step $t$ is accepted when $f(x+t\Delta x)$ lies below the line $f(x)+\alpha t\nabla f(x)^{\mathsf T}\Delta x$ (dashed), a fraction $\alpha$ of the tangent's decrease. Starting at $t=1$ and multiplying by $\beta$, the search stops inside the thick interval.

:::

```{=latex}
\begin{algorithm}
\caption{Gradient descent with backtracking line search}
\begin{algorithmic}
\INPUT starting point $x\in\operatorname{dom}f$, tolerance $\epsilon>0$, $\alpha\in(0,\frac12)$, $\beta\in(0,1)$
\WHILE{$\lVert\nabla f(x)\rVert_2>\epsilon$}
  \STATE $\Delta x\gets-\nabla f(x)$
  \STATE $t\gets1$
  \WHILE{$f(x+t\Delta x)>f(x)+\alpha t\nabla f(x)^{\mathsf T}\Delta x$}
    \STATE $t\gets\beta t$
  \ENDWHILE
  \STATE $x\gets x+t\Delta x$
\ENDWHILE
\RETURN $x$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-gradient-descent-linear-convergence .theorem name="Linear convergence of gradient descent"}

Under @def-strong-convexity on the initial sublevel set, gradient descent with backtracking line search satisfies
$$f(x^{(k)})-p^\star\le c^k\big(f(x^{(0)})-p^\star\big),\qquad c=1-\min\{2m\alpha,\,2\beta\alpha m/M\}<1.$$

:::

::: {.proof}

1. Along $\Delta x=-\nabla f(x)$, the upper bound of @def-strong-convexity gives $f(x-t\nabla f(x))\le f(x)-t\lVert\nabla f(x)\rVert_2^2+\frac{Mt^2}2\lVert\nabla f(x)\rVert_2^2$.

2. For $0\le t\le1/M$, $-t+\frac{Mt^2}{2}\le-\frac t2\le-\alpha t$ (as $\alpha<\frac12$), so the backtracking condition stops: $f(x-t\nabla f(x))\le f(x)-\alpha t\lVert\nabla f(x)\rVert_2^2$.

3. Hence backtracking ends with $t=1$ or with some $t\ge\beta/M$, so $t\ge\min\{1,\beta/M\}$ and
$$f(x^+)\le f(x)-\min\{\alpha,\beta\alpha/M\}\lVert\nabla f(x)\rVert_2^2.$$

4. By @cor-strong-convexity-gap, $\lVert\nabla f(x)\rVert_2^2\ge2m(f(x)-p^\star)$. Subtracting $p^\star$:
$$f(x^+)-p^\star\le\big(1-\min\{2m\alpha,2\beta\alpha m/M\}\big)(f(x)-p^\star).$$

5. Iterates stay in the initial sublevel set since $f$ decreases, so the bounds keep applying; induct on $k$.

:::

::: {#exm-gradient-descent-quadratic .example name="A badly conditioned quadratic"}

Minimize $f(x)=\frac12(x_1^2+\gamma x_2^2)$ with $\gamma>0$ by gradient descent with exact line search from $x^{(0)}=(\gamma,1)$. The iterates are
$$x^{(k)}=\Big(\frac{\gamma-1}{\gamma+1}\Big)^k\big(\gamma,\,(-1)^k\big),$$
so convergence is fast when $\gamma\approx1$ and very slow, zigzagging, when $\gamma\gg1$ or $\gamma\ll1$. For $\gamma=10$ the factor is $9/11\approx0.82$ per step.

:::

::: {#fig-descent-methods-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.32cm,y=1.6cm]
\draw[faint] (0,0) ellipse (10.488 and 3.317);
\draw[faint] (0,0) ellipse (8.581 and 2.714);
\draw[faint] (0,0) ellipse (7.021 and 2.220);
\draw[faint] (0,0) ellipse (5.744 and 1.817);
\draw[faint] (0,0) ellipse (4.700 and 1.486);
\draw[faint] (0,0) ellipse (3.845 and 1.216);
\draw[faint,->] (-11,0) -- (11,0);
\draw[faint,->] (0,-1.2) -- (0,1.2);
\draw[hl] (10.000,1.000) -- (8.182,-0.818) -- (6.694,0.669) -- (5.477,-0.548) -- (4.481,0.448) -- (3.666,-0.367) -- (3.000,0.300) -- (2.454,-0.245);
\node[dot] at (10.000,1.000) {};
\node[dot] at (8.182,-0.818) {};
\node[dot] at (6.694,0.669) {};
\node[dot] at (5.477,-0.548) {};
\node[dot] at (4.481,0.448) {};
\node[dot] at (3.666,-0.367) {};
\node[dot] at (3.000,0.300) {};
\node[dot] at (2.454,-0.245) {};
\node[lab,above right] at (10,1) {$x^{(0)}$};
\node[lab,below] at (0,-1.2) {$x_1$};
\end{tikzpicture}
\end{center}
```

Gradient descent with exact line search on $\frac12(x_1^2+10x_2^2)$ from $(10,1)$: the iterates zigzag and shrink by the factor $9/11$ per step. The $x_2$-axis is stretched for visibility.

:::

::: {#def-steepest-descent .definition name="Steepest descent direction"}

For a norm $\lVert\cdot\rVert$, the *normalized steepest descent direction* is
$$\Delta x_{\rm nsd}=\operatorname*{argmin}\{\nabla f(x)^{\mathsf T}v\mid\lVert v\rVert=1\}.$$
For the Euclidean norm it is $-\nabla f(x)/\lVert\nabla f(x)\rVert_2$; for the quadratic norm $\lVert v\rVert_P=(v^{\mathsf T}Pv)^{1/2}$, $P\succ0$, the unnormalized direction is $-P^{-1}\nabla f(x)$, gradient descent after the change of variables $\bar x=P^{1/2}x$; for the $\ell_1$-norm it moves along the coordinate with the largest $\lvert\partial f/\partial x_i\rvert$.

:::

::: {#fig-descent-methods-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.5]
\draw[->, faint] (-1.6,0) -- (1.9,0) node[lab, right] {};
\draw[->, faint] (0,-1.6) -- (0,1.6) node[lab, above] {};
\draw[faint] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
\draw[faint] (0,0) circle (1);
\draw[faint, dashed] (1.32,0.48) -- (1.29,0.53) -- (1.26,0.57) -- (1.22,0.61) -- (1.17,0.64) -- (1.11,0.67) -- (1.04,0.7) -- (0.96,0.72) -- (0.88,0.73) -- (0.79,0.74) -- (0.69,0.74) -- (0.59,0.74) -- (0.48,0.73) -- (0.37,0.71) -- (0.26,0.69) -- (0.14,0.67) -- (0.03,0.64) -- (-0.09,0.6) -- (-0.21,0.56) -- (-0.32,0.52) -- (-0.43,0.47) -- (-0.54,0.42) -- (-0.64,0.37) -- (-0.74,0.31) -- (-0.84,0.25) -- (-0.92,0.19) -- (-1,0.12) -- (-1.08,0.06) -- (-1.14,-0) -- (-1.2,-0.07) -- (-1.24,-0.13) -- (-1.28,-0.2) -- (-1.31,-0.26) -- (-1.32,-0.32) -- (-1.33,-0.37) -- (-1.33,-0.43) -- (-1.32,-0.48) -- (-1.29,-0.53) -- (-1.26,-0.57) -- (-1.22,-0.61) -- (-1.17,-0.64) -- (-1.11,-0.67) -- (-1.04,-0.7) -- (-0.96,-0.72) -- (-0.88,-0.73) -- (-0.79,-0.74) -- (-0.69,-0.74) -- (-0.59,-0.74) -- (-0.48,-0.73) -- (-0.37,-0.71) -- (-0.26,-0.69) -- (-0.14,-0.67) -- (-0.03,-0.64) -- (0.09,-0.6) -- (0.21,-0.56) -- (0.32,-0.52) -- (0.43,-0.47) -- (0.54,-0.42) -- (0.64,-0.37) -- (0.74,-0.31) -- (0.84,-0.25) -- (0.92,-0.19) -- (1,-0.12) -- (1.08,-0.06) -- (1.14,0) -- (1.2,0.07) -- (1.24,0.13) -- (1.28,0.2) -- (1.31,0.26) -- (1.32,0.32) -- (1.33,0.37) -- (1.33,0.43) -- (1.32,0.48) -- cycle;
\draw[->] (0,0) -- (1.37,0.62) node[lab, above] {$-\nabla f$};
\fill[accent] (1,0) circle[pt] node[lab, below right] {$\ell_1$};
\fill[accent] (0.91,0.41) circle[pt] node[lab, above left] {$\ell_2$};
\fill[accent] (1.31,0.5) circle[pt] node[lab, below right] {$P$};
\end{tikzpicture}
\end{center}
```

Normalized steepest descent directions: the point of each unit ball (diamond $\ell_1$, circle $\ell_2$, dashed ellipse a quadratic norm $\lVert\cdot\rVert_P$) furthest in the direction $-\nabla f$. For $\ell_1$ it is a coordinate direction, giving coordinate descent; for $\ell_2$ it is $-\nabla f$ itself.

:::

::: {#rmk-descent-methods-1 .remark name="Choosing the norm"}

Steepest descent in $\lVert\cdot\rVert_P$ converges fast when $P$ makes the sublevel sets of $f$ nearly round in the new variables, that is, when $P^{-1/2}\nabla^2f(x^\star)P^{-1/2}$ is well conditioned. Taking $P=\nabla^2f(x)$ at each step gives Newton's method (@sec-math-optimization-algorithms-newtons-method-for-minimization).

:::
