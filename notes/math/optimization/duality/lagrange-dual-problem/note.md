---
title: "The Dual Problem and Strong Duality"
sources: [ee364a-5]
requires: [math/optimization/duality/lagrange-dual-function, math/optimization/convex-sets/separating-hyperplanes]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on duality, in our own wording; proofs written out in steps. The proof of Slater's theorem is the separating-hyperplane argument. LP duality as an algorithmic statement is in @sec-cs-algorithm-design-linear-programming. -->

The best lower bound from the dual function is itself an optimization problem, always convex. For convex problems that satisfy a mild condition, its value equals the primal optimal value.

::: {#def-lagrange-dual-problem .definition name="Lagrange dual problem"}

The *Lagrange dual problem* is
$$\begin{array}{ll}\text{maximize}&g(\lambda,\nu)\\ \text{subject to}&\lambda\succeq0,\end{array}$$
with optimal value $d^\star$. It is a convex problem (maximizing a concave function over a convex set) even when the primal is not. $(\lambda,\nu)$ is *dual feasible* if $\lambda\succeq0$ and $g(\lambda,\nu)>-\infty$.

:::

::: {#thm-weak-strong-duality .theorem name="Weak duality" related="thm-weak-duality"}

$d^\star\le p^\star$ always. The difference $p^\star-d^\star$ is the *optimal duality gap*; *strong duality* means $d^\star=p^\star$.

:::

::: {.proof}

1. Take the supremum of @thm-dual-lower-bound over $\lambda\succeq0$ and $\nu$.

:::

::: {#thm-slater .theorem name="Slater's theorem"}

Consider a convex problem (@def-convex-optimization-problem). If there is a *strictly feasible* point $\tilde x\in\operatorname{relint}\mathcal D$ with
$$f_i(\tilde x)<0,\ i=1,\dots,m,\qquad A\tilde x=b,$$
then strong duality holds, and if $p^\star>-\infty$ the dual optimum is attained. Affine inequalities need not hold strictly.

:::

::: {.proof}

We prove the case $\operatorname{int}\mathcal D\ni\tilde x$ with $A$ of full row rank and $p^\star$ finite, all inequalities strict at $\tilde x$.

1. Let $\mathcal A=\{(u,v,t)\mid\exists x\in\mathcal D:\ f_i(x)\le u_i,\ Ax-b=v,\ f_0(x)\le t\}$, a convex set by convexity of the $f_i$, and $\mathcal B=\{(0,0,s)\mid s<p^\star\}$. They are disjoint, since a point in both would give a feasible $x$ with $f_0(x)<p^\star$.

2. By @thm-separating-hyperplane there is $(\tilde\lambda,\tilde\nu,\mu)\ne0$ and $\alpha$ with
$$\tilde\lambda^{\mathsf T}u+\tilde\nu^{\mathsf T}v+\mu t\ge\alpha\ \text{on}\ \mathcal A,\qquad \mu t\le\alpha\ \text{on}\ \mathcal B.$$

3. $\mathcal A$ is unbounded above in each $u_i$ and in $t$, so $\tilde\lambda\succeq0$ and $\mu\ge0$. From $\mathcal B$, $\mu s\le\alpha$ for all $s<p^\star$, so $\mu p^\star\le\alpha$.

4. Suppose $\mu>0$. Dividing by $\mu$ and taking $(u,v,t)=(f(x),Ax-b,f_0(x))$ gives $L(x,\tilde\lambda/\mu,\tilde\nu/\mu)\ge p^\star$ for all $x\in\mathcal D$, so $g(\tilde\lambda/\mu,\tilde\nu/\mu)\ge p^\star$. With weak duality, $d^\star=p^\star$ and the dual optimum is attained.

5. Suppose $\mu=0$. Then $\tilde\lambda^{\mathsf T}f(x)+\tilde\nu^{\mathsf T}(Ax-b)\ge0$ for all $x\in\mathcal D$. At $\tilde x$ this reads $\tilde\lambda^{\mathsf T}f(\tilde x)\ge0$ with $f_i(\tilde x)<0$, so $\tilde\lambda=0$. Then $\tilde\nu\ne0$ and $\tilde\nu^{\mathsf T}(Ax-b)\ge0$ on $\mathcal D$. Near $\tilde x$ (an interior point with $A\tilde x-b=0$) $x$ can be moved so that $\tilde\nu^{\mathsf T}(Ax-b)<0$, unless $A^{\mathsf T}\tilde\nu=0$, which full row rank excludes. So $\mu=0$ is impossible.

:::

::: {#exm-dual-inequality-lp .example name="Inequality form LP"}

Minimize $c^{\mathsf T}x$ subject to $Ax\preceq b$. The dual function is $g(\lambda)=-b^{\mathsf T}\lambda$ if $A^{\mathsf T}\lambda+c=0$ and $-\infty$ otherwise, so the dual problem is
$$\text{maximize }-b^{\mathsf T}\lambda\quad\text{s.t. }A^{\mathsf T}\lambda+c=0,\ \lambda\succeq0.$$
By Slater's theorem for affine inequalities, $p^\star=d^\star$ whenever the primal is feasible; in fact for LPs strong duality holds unless both problems are infeasible (@thm-strong-duality).

:::

::: {#exm-dual-qp .example name="Quadratic program"}

Minimize $x^{\mathsf T}Px$ subject to $Ax\preceq b$, with $P\succ0$. Minimizing $x^{\mathsf T}Px+\lambda^{\mathsf T}(Ax-b)$ at $x=-\frac12P^{-1}A^{\mathsf T}\lambda$ gives the dual
$$\text{maximize }-\tfrac14\lambda^{\mathsf T}AP^{-1}A^{\mathsf T}\lambda-b^{\mathsf T}\lambda\quad\text{s.t. }\lambda\succeq0.$$
Strong duality holds whenever the primal is feasible.

:::

::: {#exm-nonconvex-strong-duality .example name="A nonconvex problem with strong duality"}

Minimize $x^{\mathsf T}Ax+2b^{\mathsf T}x$ subject to $x^{\mathsf T}x\le1$, with $A$ possibly indefinite. Its dual is
$$\text{maximize }-t-\lambda\quad\text{s.t. }\lambda\ge0,\ \begin{bmatrix}A+\lambda I&b\\b^{\mathsf T}&t\end{bmatrix}\succeq0,$$
and strong duality holds even though the primal is not convex (the S-procedure: a single quadratic constraint).

:::

::: {#rmk-lagrange-dual-problem-1 .remark name="Geometric picture"}

With one inequality, let $\mathcal G=\{(f_1(x),f_0(x))\mid x\in\mathcal D\}$. For $\lambda\ge0$, $g(\lambda)=\inf_{(u,t)\in\mathcal G}(t+\lambda u)$ is where the supporting line of slope $-\lambda$ crosses the $t$-axis. The dual problem looks for the highest such crossing; $p^\star$ is the lowest point of $\mathcal G$ with $u\le0$. A gap appears when $\mathcal G$ is not convex near that point.

:::
