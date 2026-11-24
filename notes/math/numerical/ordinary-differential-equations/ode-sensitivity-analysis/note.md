---
title: "Sensitivity Analysis of ODE Solutions"
sources: [mit18s096-9]
requires: [math/numerical/ordinary-differential-equations/stiffness-and-implicit-methods, math/calculus/matrix/computing-derivatives/reverse-mode-automatic-differentiation]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 9 (ODEs, sensitivity analysis of ODE solutions, forward and reverse/adjoint sensitivity, an example) and the slides "An Introduction to (Local) Sensitivity Analysis" (derivation of the continuous adjoint), in our own wording; the example is ours, checked in Python with numerical quadrature; proofs written out in steps. The discrete analogue is @thm-adjoint-gradient. -->

Many models are ODEs $\partial u/\partial t=f(u,p,t)$ whose right-hand side depends on parameters $p\in\mathbb{R}^N$: reaction rates, masses, or the weights of a neural network inside $f$. Fitting $p$ to data needs the derivative of the solution with respect to $p$. Both ways of computing it solve *another* ODE: forward sensitivity integrates forward together with $u$, the adjoint method integrates a single ODE backwards in time.

::: {#def-forward-sensitivity .definition name="Forward sensitivity equations"}

Let $u(p,t)\in\mathbb{R}^n$ solve $\partial u/\partial t=f(u,p,t)$ with $u(p,0)=u_0(p)$, where $f$ and $u_0$ are differentiable. The *sensitivity matrix* $s=\partial u/\partial p$ ($n\times N$) satisfies

$$
\frac{\partial s}{\partial t}=f_u\,s+f_p,\qquad s(0)=\frac{\partial u_0}{\partial p},
$$

where $f_u=\partial f/\partial u$ and $f_p=\partial f/\partial p$ are evaluated along the solution $u(p,t)$.

:::

The equation follows by differentiating the ODE with respect to $p$ and exchanging the $t$ and $p$ derivatives (allowed when $f$ is continuously differentiable): $\partial_t(du)=f_u\,du+f_p\,dp$. It has $nN$ unknowns, so it is practical only for few parameters.

::: {#fig-ode-sensitivity-analysis-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.6cm, y=3cm]
\draw[->] (0,0) -- (2.15,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,1.1) node[lab, above] {$u$};
\draw[domain=0:2, samples=40] plot (\x, {exp(-\x)});
\draw[hl, domain=0:2, samples=40] plot (\x, {exp(-1.2*\x)});
\draw[emph] (1,0.3679) -- (1,0.3012);
\node[lab, right] at (1.02,0.36) {$\delta u\approx s\,\delta p$};
\node[lab] at (1.75,0.27) {$p=1$}; \node[lab] at (1.55,0.02) {$p=1.2$};
\foreach \t in {0,1,2}{\draw (\t,0) -- (\t,-0.03) node[lab, below] {$\t$};}
\end{tikzpicture}
\end{center}
```

Solutions of $u'=-pu$, $u(0)=1$, for two values of $p$. The sensitivity $s=\partial u/\partial p=-te^{-pt}$ measures how far the curve moves per unit change of $p$; it is zero at $t=0$ because the initial value does not depend on $p$.

:::

::: {#thm-ode-adjoint-sensitivity .theorem name="Adjoint sensitivity of an integral objective"}

With $u$ as in @def-forward-sensitivity, let $G(p)=\int_0^Tg(u(p,t),p,t)\,dt$ for a differentiable scalar $g$. Let $\lambda(t)\in\mathbb{R}^n$ solve the *adjoint equation* backwards from $t=T$:

$$
\frac{d\lambda}{dt}=-f_u^{\mathsf T}\lambda-g_u^{\mathsf T},\qquad \lambda(T)=0 .
$$

Then

$$
\nabla G=\int_0^T\bigl(g_p^{\mathsf T}+f_p^{\mathsf T}\lambda\bigr)\,dt+\Bigl(\frac{\partial u_0}{\partial p}\Bigr)^{\mathsf T}\lambda(0).
$$

:::

```{=latex}
\begin{algorithm}
\caption{Adjoint sensitivity of $G(p)=\int_0^Tg\,dt$}
\begin{algorithmic}
\INPUT $f$, $g$, $u_0(p)$, final time $T$
\STATE solve $u'=f(u,p,t)$ from $u(0)=u_0(p)$ to $t=T$; store $u(t)$ or checkpoints
\STATE $\lambda(T)\gets0$; $\gamma\gets0$
\STATE solve backwards from $T$ to $0$: $\lambda'=-f_u^{\mathsf T}\lambda-g_u^{\mathsf T}$ and $\gamma'=-(g_p^{\mathsf T}+f_p^{\mathsf T}\lambda)$, $\gamma(T)=0$
\RETURN $\nabla G=\gamma(0)+(\partial u_0/\partial p)^{\mathsf T}\lambda(0)$
\end{algorithmic}
\end{algorithm}
```

::: {.proof}

1. By the chain rule under the integral, $dG=\int_0^T\bigl(g_u\,du+g_p\,dp\bigr)dt$, where $du=s\,dp$ solves $\partial_t(du)=f_u\,du+f_p\,dp$.

2. For any $\lambda(t)$, $\int_0^T\lambda^{\mathsf T}\bigl(\partial_t(du)-f_u\,du-f_p\,dp\bigr)dt=0$. Integrate the first term by parts: $\int_0^T\lambda^{\mathsf T}\partial_t(du)\,dt=\lambda(T)^{\mathsf T}du(T)-\lambda(0)^{\mathsf T}du(0)-\int_0^T\dot\lambda^{\mathsf T}du\,dt$.

3. Add the zero of step 2, with the sign reversed, to $dG$:

   $$dG=\int_0^T\bigl(g_u+\dot\lambda^{\mathsf T}+\lambda^{\mathsf T}f_u\bigr)du\,dt+\int_0^T\bigl(g_p+\lambda^{\mathsf T}f_p\bigr)dp\,dt-\lambda(T)^{\mathsf T}du(T)+\lambda(0)^{\mathsf T}du(0).$$

4. The adjoint equation makes the first bracket zero and $\lambda(T)=0$ removes the boundary term at $T$, so the unknown $du(t)$ disappears except at $t=0$, where $du(0)=\frac{\partial u_0}{\partial p}dp$.

5. Reading off the coefficient of $dp$ gives the formula.

:::

::: {#exm-ode-sensitivity-analysis-1 .example name="Exponential decay"}

Let $u'=-pu$, $u(0)=1$ and $G(p)=\int_0^Tu\,dt=(1-e^{-pT})/p$. Here $f_u=-p$, $f_p=-u$, $g_u=1$, $g_p=0$.

1. *Forward:* $s'=-ps-u$, $s(0)=0$ gives $s=-te^{-pt}$, so at $p=1$, $T=2$ the final value moves by $\partial u(2)/\partial p=-2e^{-2}=-0.2707$.

2. *Adjoint:* $\lambda'=p\lambda-1$, $\lambda(T)=0$ gives $\lambda(t)=\bigl(1-e^{p(t-T)}\bigr)/p$. Then $dG/dp=\int_0^T\lambda(t)\,(-u(t))\,dt=-0.59399$ at $p=1$, $T=2$, matching the derivative of the closed form, also $-0.59399$.

:::

::: {#fig-ode-sensitivity-analysis-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[map] (0,0.6) -- node[lab, above] {solve for $u(t)$, store or checkpoint} (7,0.6);
\draw[map, hl] (7,-0.6) -- node[lab, below] {solve for $\lambda(t)$ from $\lambda(T)=0$, accumulate $\int f_p^{\mathsf T}\lambda\,dt$} (0,-0.6);
\node[lab, left] at (-0.1,0) {$t=0$}; \node[lab, right] at (7.1,0) {$t=T$};
\end{tikzpicture}
\end{center}
```

The adjoint method needs one forward solve of size $n$ and one backward solve of size $n$, whatever the number $N$ of parameters; the backward solve needs $u(t)$ again, which is stored, recomputed from checkpoints, or re-integrated backwards.

:::

::: {#rmk-ode-sensitivity-analysis-1 .remark name="Forward or adjoint"}

Forward sensitivity costs about $N$ extra solves of the original size and gives the whole Jacobian $\partial u/\partial p$; the adjoint method costs about one extra solve and gives the gradient of one scalar objective. This is the forward-versus-reverse trade-off of @prp-forward-versus-reverse in continuous time. An objective at a single time, $g(u(p,T))$, corresponds to $\lambda(T)=g_u^{\mathsf T}$ and no source term. Differentiating the steps of a numerical solver by reverse-mode AD instead gives the discrete adjoint (backpropagation through time); it agrees with the continuous adjoint only up to discretization error. Neural ODEs, where $f$ is a neural network with millions of parameters, are trained with the adjoint method.

:::
