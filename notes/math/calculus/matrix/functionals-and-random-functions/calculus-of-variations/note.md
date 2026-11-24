---
title: "Calculus of Variations"
sources: [mit18s096-10]
requires: [math/calculus/matrix/derivatives/hessians-and-bilinear-maps]
status: draft
---

<!-- Added 2026-11-24 from MIT 18.S096 Matrix Calculus (IAP 2023), course notes Chapter 10 (functionals, inner products of functions, minimizing arc length, the Euler-Lagrange equations), in our own wording; the second example is ours; proofs written out in steps. Differential equations are used only to state the result; solving them is beyond this note. -->

A *functional* maps a function to a number, for example the length of a curve or the energy of a field. Since functions form a vector space, a functional has a derivative like any other map, and with the $L^2$ inner product it has a gradient, which is again a function. Setting that gradient to zero gives the Euler–Lagrange equation.

::: {#def-functional-gradient .definition name="Functional and its gradient" related="def-function-inner-product"}

Let $V$ be a vector space of functions $u:[a,b]\to\mathbb{R}$ with a norm, and $f:V\to\mathbb{R}$ a *functional*. Its derivative $f'(u)$ is a linear functional, $df=f'(u)[du]$. With the $L^2$ inner product

$$
\langle v,w\rangle=\int_a^bv(x)\,w(x)\,dx,
$$

the *gradient* $\nabla f(u)$ is the function with $df=\langle\nabla f(u),du\rangle$ for all admissible changes $du$, when such a function exists.

:::

::: {#exm-calculus-of-variations-1 .example name="An integral of the function"}

Let $f(u)=\int_a^b\sin u(x)\,dx$. Then $df=\int_a^b\cos u(x)\,du(x)\,dx=\langle\cos u,du\rangle$, so $\nabla f(u)=\cos u$: the gradient is computed pointwise, just as for $\sum_i\sin x_i$ on $\mathbb{R}^n$.

:::

::: {#thm-euler-lagrange .theorem name="Euler–Lagrange equation"}

Let $F(u,v,x)$ be twice continuously differentiable and

$$
f(u)=\int_a^bF\bigl(u(x),u'(x),x\bigr)\,dx
$$

on twice continuously differentiable $u$ with fixed end values $u(a)=\alpha$, $u(b)=\beta$, so that admissible changes satisfy $du(a)=du(b)=0$. Then

$$
\nabla f(u)=\frac{\partial F}{\partial u}-\frac{d}{dx}\Bigl(\frac{\partial F}{\partial u'}\Bigr),
$$

where $\partial F/\partial u'$ means $\partial F/\partial v$ evaluated at $v=u'(x)$. A minimizer $u$ satisfies the *Euler–Lagrange equation* $\nabla f(u)=0$.

:::

::: {.proof}

1. Change $u$ by $du$; then $u'$ changes by $(du)'$. By the chain rule under the integral, $df=\int_a^b\bigl(F_u\,du+F_{u'}\,(du)'\bigr)dx$.

2. Integrate the second term by parts: $\int_a^bF_{u'}(du)'\,dx=\bigl[F_{u'}\,du\bigr]_a^b-\int_a^b\frac{d}{dx}\bigl(F_{u'}\bigr)du\,dx$.

3. The boundary term vanishes because $du(a)=du(b)=0$. Hence $df=\bigl\langle F_u-\frac{d}{dx}F_{u'},du\bigr\rangle$, which identifies the gradient.

4. If $u$ minimizes $f$ and $\nabla f(u)$ were nonzero somewhere, then by continuity it would be nonzero, say positive, on an interval; a smooth bump $du\ge0$ supported there with $du(a)=du(b)=0$ would give $df>0$, and $-du$ would decrease $f$ to first order. So $\nabla f(u)=0$.

:::

::: {#fig-calculus-of-variations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm, y=1.3cm]
\draw[->] (-0.2,0) -- (4.4,0) node[lab, right] {$x$};
\draw (0,1) .. controls (1.2,2.2) and (2.6,0.4) .. (4,1.8);
\draw[hl] (0,1) .. controls (1.2,2.6) and (2.6,0.8) .. (4,1.8);
\fill (0,1) circle (1.5pt) node[lab, left] {$\alpha$};
\fill (4,1.8) circle (1.5pt) node[lab, right] {$\beta$};
\node[lab] at (2.3,0.95) {$u$}; \node[lab] at (2.3,1.65) {$u+du$};
\draw[faint, dashed] (0,0) -- (0,1); \draw[faint, dashed] (4,0) -- (4,1.8);
\node[lab, below] at (0,0) {$a$}; \node[lab, below] at (4,0) {$b$};
\end{tikzpicture}
\end{center}
```

An admissible change $du$ keeps the end values fixed. That is exactly what removes the boundary term in step 3 of the proof.

:::

::: {#exm-calculus-of-variations-2 .example name="The shortest curve is a straight line"}

The length of the graph of $u$ is $f(u)=\int_a^b\sqrt{1+u'(x)^2}\,dx$, so $F=\sqrt{1+v^2}$ with $F_u=0$ and $F_{u'}=u'/\sqrt{1+u'^2}$.

1. The Euler–Lagrange equation says $\frac{d}{dx}\bigl(u'/\sqrt{1+u'^2}\bigr)=0$, so $u'/\sqrt{1+u'^2}$ is constant.

2. The map $v\mapsto v/\sqrt{1+v^2}$ is strictly increasing, so $u'$ is constant and $u$ is the straight line through $(a,\alpha)$ and $(b,\beta)$.

:::

::: {#exm-calculus-of-variations-3 .example name="A balance between slope and size"}

Let $f(u)=\int_0^1\bigl(u'^2+u^2\bigr)dx$ with $u(0)=0$, $u(1)=1$. Then $F_u=2u$ and $F_{u'}=2u'$, so the Euler–Lagrange equation is $2u-2u''=0$, that is $u''=u$. The solution with these end values is $u(x)=\sinh x/\sinh1$; one checks directly that $u''=u$, $u(0)=0$ and $u(1)=1$.

:::

::: {#fig-calculus-of-variations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=4cm, y=2.6cm]
\draw[->] (0,0) -- (1.1,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,1.15) node[lab, above] {$u$};
\draw[faint] (0,0) -- (1,1);
\draw[hl, domain=0:1, samples=30] plot (\x, {(exp(\x)-exp(-\x))/(exp(1)-exp(-1))});
\node[lab] at (0.4,0.55) {line};
\node[lab] at (0.72,0.42) {$\sinh x/\sinh1$};
\foreach \t in {0,1}{\draw (\t,0) -- (\t,-0.03) node[lab, below] {$\t$};}
\end{tikzpicture}
\end{center}
```

The minimizer of $\int_0^1(u'^2+u^2)\,dx$ sags below the straight line: the term $u^2$ rewards staying small, the term $u'^2$ rewards a gentle slope, and the Euler–Lagrange equation balances the two.

:::

::: {#rmk-calculus-of-variations-1 .remark name="Discretize, then differentiate"}

Sampling $u$ at $n$ points and replacing integrals by sums turns $f$ into a function on $\mathbb{R}^n$. Its ordinary gradient divided by the grid spacing approximates the $L^2$ gradient of @thm-euler-lagrange; the factor is the weight in the discrete inner product $h\sum_iv_iw_i\approx\int vw$, an instance of @prp-weighted-gradient.

:::
