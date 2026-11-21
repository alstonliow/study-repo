---
title: "Duality, Reformulations and Generalized Inequalities"
sources: [ee364a-5]
requires: [math/optimization/duality/lagrange-dual-problem, math/optimization/convex-problems/semidefinite-programs]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on duality, in our own wording; proofs written out in steps. -->

Equivalent problems can have very different duals. Introducing variables, making constraints explicit or implicit, and allowing generalized inequalities all change the dual, often making it more useful.

::: {#exm-dual-new-variables .example name="Introducing new variables"}

Unconstrained $\min_x f_0(Ax+b)$ has the trivial dual $g=p^\star$. Rewrite it as minimize $f_0(y)$ subject to $Ax+b-y=0$. Then
$$g(\nu)=\inf_{x,y}\big(f_0(y)-\nu^{\mathsf T}y+\nu^{\mathsf T}Ax+b^{\mathsf T}\nu\big)=\begin{cases}b^{\mathsf T}\nu-f_0^*(\nu)&\text{if }A^{\mathsf T}\nu=0,\\-\infty&\text{otherwise.}\end{cases}$$
For norm approximation, minimize $\lVert Ax-b\rVert$, this gives the dual: maximize $b^{\mathsf T}\nu$ subject to $A^{\mathsf T}\nu=0$, $\lVert\nu\rVert_*\le1$.

:::

::: {#exm-dual-implicit-constraints .example name="Implicit constraints"}

The LP with box constraints, minimize $c^{\mathsf T}x$ subject to $Ax=b$, $-\mathbf 1\preceq x\preceq\mathbf 1$, has dual maximize $-b^{\mathsf T}\nu-\mathbf 1^{\mathsf T}\lambda_1-\mathbf 1^{\mathsf T}\lambda_2$ subject to $c+A^{\mathsf T}\nu+\lambda_1-\lambda_2=0$, $\lambda_1,\lambda_2\succeq0$. Making the box implicit, $f_0(x)=c^{\mathsf T}x$ on $\operatorname{dom}f_0=\{-\mathbf 1\preceq x\preceq\mathbf 1\}$, gives
$$g(\nu)=\inf_{-\mathbf 1\preceq x\preceq\mathbf 1}(c^{\mathsf T}x+\nu^{\mathsf T}(Ax-b))=-b^{\mathsf T}\nu-\lVert A^{\mathsf T}\nu+c\rVert_1,$$
an unconstrained dual.

:::

::: {#def-dual-generalized-inequalities .definition name="Duality for generalized inequalities"}

For minimize $f_0(x)$ subject to $f_i(x)\preceq_{K_i}0$, $h_i(x)=0$, the Lagrangian is
$$L(x,\lambda_1,\dots,\lambda_m,\nu)=f_0(x)+\sum_i\lambda_i^{\mathsf T}f_i(x)+\sum_i\nu_ih_i(x),$$
and the dual problem maximizes $g=\inf_xL$ subject to $\lambda_i\succeq_{K_i^*}0$ (@def-dual-cone). The lower bound property, weak duality and, for convex problems with a strictly feasible point ($f_i(x)\prec_{K_i}0$), strong duality hold as before.

:::

::: {.proof}

1. Lower bound: for feasible $\tilde x$, $-f_i(\tilde x)\in K_i$ and $\lambda_i\in K_i^*$, so $\lambda_i^{\mathsf T}f_i(\tilde x)\le0$. Then $g\le L(\tilde x,\dots)\le f_0(\tilde x)$ as in @thm-dual-lower-bound.

:::

::: {#exm-sdp-dual .example name="Semidefinite program"}

The SDP minimize $c^{\mathsf T}x$ subject to $x_1F_1+\cdots+x_nF_n\preceq G$ has Lagrangian $c^{\mathsf T}x+\operatorname{tr}\big(Z(\sum_ix_iF_i-G)\big)$ with $Z\succeq0$ (the semidefinite cone is self-dual, @exm-dual-cones). It is affine in $x$, so the dual is
$$\text{maximize }-\operatorname{tr}(GZ)\quad\text{s.t. }Z\succeq0,\ \operatorname{tr}(F_iZ)+c_i=0,\ i=1,\dots,n.$$
Strong duality holds if the primal LMI is strictly feasible.

:::

::: {#rmk-duality-and-reformulations-1 .remark name="No rule for the best form"}

There is no general rule for which equivalent form has the most useful dual. Common tricks: introduce variables for arguments of functions, move simple constraints into the domain, and replace the objective by an increasing function of it (for example minimize $\frac12\lVert y\rVert_2^2$ instead of $\lVert y\rVert_2$).

:::
