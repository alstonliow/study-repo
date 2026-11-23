---
title: "Trust-Region Methods and CCSA"
sources: [mit18335-28, mit18335-25]
requires: [math/optimization/algorithms/quasi-newton-methods, math/optimization/duality/lagrange-dual-problem]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 25 (overview of optimization algorithms) and 28 (trust-region methods and the CCSA algorithm), in our own wording; proofs written out in steps. -->

A line-search method picks a direction from a model and then decides how far to go. A trust-region method reverses the order: it decides how far it trusts its model and then minimises the model within that distance. The same idea, with a model that is guaranteed to lie above the function, gives the CCSA algorithm for nonlinear constrained problems with many variables.

::: {#def-trust-region-method .definition name="Trust-region method"}

At the iterate $x_k$, with a quadratic model $m_k(\delta)=f(x_k)+\nabla f(x_k)^{\mathsf T}\delta+\tfrac12\delta^{\mathsf T}B_k\delta$ ($B_k$ the Hessian or a quasi-Newton approximation) and a radius $\Delta_k>0$:

1. compute a step $\delta_k$ that (approximately) solves $\min_\delta m_k(\delta)$ subject to $\lVert\delta\rVert\le\Delta_k$;

2. compute the ratio of actual to predicted reduction $\rho_k=\dfrac{f(x_k)-f(x_k+\delta_k)}{m_k(0)-m_k(\delta_k)}$;

3. if $\rho_k>\eta$ (say $\eta=0.1$) accept, $x_{k+1}=x_k+\delta_k$, else stay at $x_k$;

4. if $\rho_k<\tfrac14$ shrink, $\Delta_{k+1}=\tfrac14\Delta_k$; if $\rho_k>\tfrac34$ and the step reached the boundary, expand, $\Delta_{k+1}=2\Delta_k$; otherwise keep $\Delta_k$.

:::

```{=latex}
\begin{algorithm}
\caption{Trust-region method}
\begin{algorithmic}
\INPUT $f$, $\nabla f$, model Hessians $B_k$, $x_0$, $\Delta_0$, $0<\eta<\tfrac14$
\FOR{$k=0,1,2,\dots$}
    \STATE $\delta_k\gets$ approximate minimiser of $m_k(\delta)$ over $\lVert\delta\rVert\le\Delta_k$
    \STATE $\rho_k\gets\bigl(f(x_k)-f(x_k+\delta_k)\bigr)/\bigl(m_k(0)-m_k(\delta_k)\bigr)$
    \STATE \textbf{if} $\rho_k>\eta$ \textbf{then} $x_{k+1}\gets x_k+\delta_k$ \textbf{else} $x_{k+1}\gets x_k$
    \STATE \textbf{if} $\rho_k<\tfrac14$ \textbf{then} $\Delta_{k+1}\gets\Delta_k/4$ \textbf{else if} $\rho_k>\tfrac34$ and $\lVert\delta_k\rVert=\Delta_k$ \textbf{then} $\Delta_{k+1}\gets2\Delta_k$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

::: {#prp-trust-region-subproblem .proposition name="The trust-region subproblem"}

$\delta^*$ solves $\min m(\delta)=g^{\mathsf T}\delta+\tfrac12\delta^{\mathsf T}B\delta$ over $\lVert\delta\rVert_2\le\Delta$ if and only if there is $\lambda\ge0$ with
$$(B+\lambda I)\delta^*=-g,\qquad\lambda(\Delta-\lVert\delta^*\rVert)=0,\qquad B+\lambda I\succeq0 .$$
So the trust-region step is a Newton step with a Levenberg–Marquardt shift $\lambda$; it is well defined even when $B$ is indefinite.

:::

::: {.proof}

1. *Sufficiency.* Suppose the three conditions hold and let $\|\delta\|\le\Delta$. Since $B+\lambda I\succeq0$, the convex quadratic $\hat m(\delta)=m(\delta)+\tfrac\lambda2\lVert\delta\rVert^2$ is minimised where its gradient $(B+\lambda I)\delta+g$ vanishes, at $\delta^*$. So $m(\delta)\ge m(\delta^*)+\tfrac\lambda2(\lVert\delta^*\rVert^2-\lVert\delta\rVert^2)$.

2. If $\lambda=0$ the last term is $0$; if $\lambda>0$ then $\lVert\delta^*\rVert=\Delta\ge\lVert\delta\rVert$ and the term is $\ge0$. Either way $m(\delta)\ge m(\delta^*)$.

3. *Necessity* (sketch). The first two conditions are the KKT conditions for the constraint $\tfrac12\lVert\delta\rVert^2\le\tfrac12\Delta^2$ (@sec-math-optimization-duality-kkt-conditions), and the constraint qualification holds for a ball. The semidefiniteness follows by comparing $m(\delta^*)$ with $m$ at other points of the sphere $\lVert\delta\rVert=\lVert\delta^*\rVert$, which is the extra fact special to this problem (Moré–Sorensen).

:::

::: {#fig-trust-region-methods-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\foreach \s in {0.6,1.2,1.8,2.4} {\draw[faint, rotate around={25:(2.3,1.4)}] (2.3,1.4) ellipse ({1.0*\s} and {0.45*\s});}
\fill[accent] (2.3,1.4) circle (1.5pt) node[lab, right] {model minimiser (Newton step)};
\draw[regionA] (0,0) circle (1.2);
\fill (0,0) circle (1.5pt) node[lab, below left] {$x_k$};
\draw[hl, ->] (0,0) -- (1.00,0.66);
\fill[accent] (1.00,0.66) circle (1.4pt);
\node[lab] at (0.25,0.75) {$\delta_k$};
\node[note] at (-0.6,-1.45) {trust region $\lVert\delta\rVert\le\Delta_k$};
\draw[faint, dashed] (0,0) -- (2.3,1.4);
\end{tikzpicture}
\end{center}
```

A trust-region step: the model's unconstrained minimiser lies outside the region, so the step stops on the boundary where a level curve of the model touches the circle. Its direction bends from the Newton direction (dashed) towards the steepest-descent direction as $\Delta_k$ shrinks.

:::

::: {#def-ccsa .definition name="CCSA (conservative convex separable approximations)"}

For $\min f_0(x)$ subject to $f_i(x)\le0$ ($i=1,\dots,m$) and bounds on $x$, Svanberg's CCSA method forms at $x_k$ approximations
$$g_i(x)=f_i(x_k)+\nabla f_i(x_k)^{\mathsf T}(x-x_k)+\frac{\rho_i}2\sum_j\Bigl(\frac{x_j-x_{k,j}}{\sigma_j}\Bigr)^2,$$
which are *convex* and *separable* (a sum of functions of one variable each), with per-coordinate scales $\sigma_j$ (a trust-region radius) and penalty weights $\rho_i>0$. The inner step minimises $g_0$ subject to $g_i\le0$ and $\lvert x_j-x_{k,j}\rvert\le\sigma_j$; separability makes its Lagrange dual (@def-lagrange-dual-problem) an easy problem in $m$ variables. If the candidate is *not conservative*, i.e. some $g_i(x_{\text{new}})<f_i(x_{\text{new}})$, the corresponding $\rho_i$ is increased and the inner step repeated. Between outer iterations $\sigma_j$ grows or shrinks depending on whether $x_j$ moves monotonically or oscillates.

:::

::: {#prp-ccsa-conservative .proposition name="Conservative steps keep feasibility and decrease the objective"}

If the inner step returns $x_{k+1}$ with $g_i(x_{k+1})\ge f_i(x_{k+1})$ for all $i=0,\dots,m$, and $x_k$ is feasible, then $x_{k+1}$ is feasible and $f_0(x_{k+1})\le f_0(x_k)$.

:::

::: {.proof}

1. $x_{k+1}$ satisfies the approximate constraints, so $f_i(x_{k+1})\le g_i(x_{k+1})\le0$: it is feasible.

2. $x_k$ itself is feasible for the inner problem because $g_i(x_k)=f_i(x_k)\le0$, so the inner minimiser satisfies $g_0(x_{k+1})\le g_0(x_k)=f_0(x_k)$.

3. Conservativeness of $g_0$ gives $f_0(x_{k+1})\le g_0(x_{k+1})\le f_0(x_k)$.

:::

Increasing $\rho_i$ makes $g_i$ larger away from $x_k$, so for large enough $\rho_i$ every approximation becomes conservative near $x_k$ (by Taylor's theorem with a bounded Hessian); the inner loop therefore terminates, and the method converges to a KKT point from any feasible start. It is used for large design problems (topology optimisation) with many variables and few constraints, where each function evaluation is expensive but gradients come cheaply from adjoint methods (@sec-math-optimization-algorithms-adjoint-methods).

::: {#fig-trust-region-methods-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.5cm, y=1.2cm]
\draw[->, faint] (-0.2,0) -- (4.3,0) node[lab, right] {$x$};
\draw[emph, domain=0:4, samples=80] plot (\x,{0.6+0.35*sin(1.7*\x r)+0.12*(\x-2)*(\x-2)});
\node[lab] at (4.1,1.4) {$f$};
\draw[hl, domain=0.6:3.4, samples=60] plot (\x,{0.8252-0.614*(\x-1.5)+0.9*(\x-1.5)*(\x-1.5)});
\node[lab] at (3.0,3.0) {$g$, conservative};
\draw[faint, dashed, domain=0.9:3.8, samples=60] plot (\x,{0.8252-0.614*(\x-1.5)+0.15*(\x-1.5)*(\x-1.5)});
\node[note] at (3.95,2.15) {$\rho$ too small};
\fill (1.5,0.8252) circle (1.6pt) node[lab, below right] {$x_k$};
\end{tikzpicture}
\end{center}
```

A one-dimensional picture of CCSA: the approximation $g$ (thick) matches $f$ and its slope at $x_k$ and lies above $f$, so minimising $g$ cannot increase $f$. With a smaller penalty $\rho$ (dashed) the approximation dips below $f$, is not conservative, and $\rho$ is increased.

:::

::: {#rmk-trust-region-methods-1 .remark name="A map of optimization algorithms"}

Lecture 25 of the course classifies methods by what they use: *derivative-free* methods (@sec-math-optimization-algorithms-derivative-free-optimization) use only values of $f$; *first-order* methods use gradients (gradient descent, CG, quasi-Newton, CCSA), *second-order* methods also Hessians (Newton, trust-region Newton). Constraints are handled by penalty and barrier methods (@sec-math-optimization-algorithms-barrier-method), by duality, or by sequential approximations such as SQP and CCSA. Local methods find local optima; global optimisation of nonconvex functions needs multistart, branch-and-bound or stochastic search, and for large $n$ one settles for good local optima. Convexity, when present, makes local optima global.

:::
