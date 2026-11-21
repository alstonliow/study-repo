---
title: "Geometric Programs"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/equivalent-problems]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. Numbers checked in Python. -->

Geometric programs look nonconvex, being built from monomials and posynomials of positive variables, but a logarithmic change of variables turns them into convex problems with log-sum-exp constraints.

::: {#def-monomial-posynomial .definition name="Monomial, posynomial"}

For $x\in\mathbb{R}^n_{++}$, a *monomial* is $f(x)=c\,x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n}$ with $c>0$ and real exponents $a_i$. A *posynomial* is a sum of monomials, $f(x)=\sum_{k=1}^Kc_kx_1^{a_{1k}}\cdots x_n^{a_{nk}}$.

:::

::: {#def-geometric-program .definition name="Geometric program"}

A *geometric program* (GP) is
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\le1,\quad i=1,\dots,m,\\ &h_i(x)=1,\quad i=1,\dots,p,\end{array}$$
with $f_0,\dots,f_m$ posynomials, $h_1,\dots,h_p$ monomials, and implicit constraint $x\succ0$.

:::

::: {#thm-gp-convex-form .theorem name="Geometric programs in convex form"}

With $y_i=\log x_i$, the GP of @def-geometric-program is equivalent to the convex problem
$$\begin{array}{ll}\text{minimize}&\log\sum_ke^{a_{0k}^{\mathsf T}y+b_{0k}}\\ \text{subject to}&\log\sum_ke^{a_{ik}^{\mathsf T}y+b_{ik}}\le0,\quad i=1,\dots,m,\\ &Gy+d=0,\end{array}$$
where $b_{ik}=\log c_{ik}$ and each monomial $h_i$ becomes the affine equation $g_i^{\mathsf T}y+d_i=0$.

:::

::: {.proof}

1. A monomial becomes $c\,e^{a^{\mathsf T}y}=e^{a^{\mathsf T}y+\log c}$, so $\log$ of a monomial is affine in $y$ and $h_i(x)=1$ iff that affine function is $0$.

2. A posynomial becomes $\sum_ke^{a_k^{\mathsf T}y+b_k}$; since $\log$ is increasing and $\log1=0$, $f_i(x)\le1$ iff $\log\sum_ke^{a_k^{\mathsf T}y+b_k}\le0$, and minimizing $f_0$ is the same as minimizing $\log f_0$.

3. Log-sum-exp is convex (@exm-convex-by-hessian) and composing it with an affine map keeps it convex (@prp-nonnegative-sum-affine-composition). The map $x\mapsto y$ is a bijection from $\mathbb{R}^n_{++}$ to $\mathbb{R}^n$.

:::

::: {#exm-box-design-gp .example name="Designing a box"}

Maximize the volume $hwd$ of a box with wall area $2(hw+hd)\le A_{\rm wall}$ and floor area $wd\le A_{\rm flr}$. As a GP: minimize $h^{-1}w^{-1}d^{-1}$ subject to $\frac{2}{A_{\rm wall}}hw+\frac{2}{A_{\rm wall}}hd\le1$ and $\frac{1}{A_{\rm flr}}wd\le1$. For $A_{\rm wall}=100$ and $A_{\rm flr}=10$ the optimum can be found by hand: the wall constraint gives $h\le50/(w+d)$, so the volume is at most $50\,wd/(w+d)\le50\sqrt{wd}/2\le25\sqrt{10}\approx79.06$ (using $w+d\ge2\sqrt{wd}$ and $wd\le10$), attained at $w=d=\sqrt{10}$, $h=25/\sqrt{10}\approx7.91$.

:::

::: {#exm-spectral-radius-gp .example name="Spectral radius of a positive matrix"}

For an elementwise positive matrix $A(x)$ whose entries are posynomials in $x$, the Perron–Frobenius eigenvalue satisfies $\lambda_{\rm pf}(A(x))\le\lambda$ iff $A(x)v\preceq\lambda v$ for some $v\succ0$, that is, $\sum_jA(x)_{ij}v_j/(\lambda v_i)\le1$ for all $i$, a set of posynomial constraints in $(x,v,\lambda)$. So minimizing the spectral radius is a GP.

:::

::: {#rmk-geometric-programs-1 .remark name="What is and is not a GP"}

Posynomials are closed under sums, products and multiplication by positive constants, and a posynomial divided by a monomial is a posynomial. A ratio of two posynomials is in general not a posynomial, and a constraint $f(x)\ge1$ with $f$ a posynomial is not allowed.

:::
