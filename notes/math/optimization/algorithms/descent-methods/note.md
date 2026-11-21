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

::: {#rmk-descent-methods-1 .remark name="Choosing the norm"}

Steepest descent in $\lVert\cdot\rVert_P$ converges fast when $P$ makes the sublevel sets of $f$ nearly round in the new variables, that is, when $P^{-1/2}\nabla^2f(x^\star)P^{-1/2}$ is well conditioned. Taking $P=\nabla^2f(x)$ at each step gives Newton's method (@sec-math-optimization-algorithms-newtons-method-for-minimization).

:::
