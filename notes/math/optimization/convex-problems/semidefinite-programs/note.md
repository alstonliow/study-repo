---
title: "Semidefinite Programs"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/second-order-cone-programs, math/optimization/convex-sets/generalized-inequalities]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. -->

Replacing componentwise inequalities by generalized inequalities gives conic problems. With the semidefinite cone this is semidefinite programming, which contains LP and SOCP and handles eigenvalue and matrix norm problems.

::: {#def-conic-problem .definition name="Problems with generalized inequality constraints"}

A convex problem with generalized inequality constraints is
$$\begin{array}{ll}\text{minimize}&f_0(x)\\ \text{subject to}&f_i(x)\preceq_{K_i}0,\quad i=1,\dots,m,\\ &Ax=b,\end{array}$$
with $f_0$ convex, proper cones $K_i$ and $f_i$ $K_i$-convex (@def-k-convex). A *conic form problem* has affine objective and constraints: minimize $c^{\mathsf T}x$ subject to $Fx+g\preceq_K0$, $Ax=b$.

:::

::: {#def-sdp .definition name="Semidefinite program"}

A *semidefinite program* (SDP) is
$$\begin{array}{ll}\text{minimize}&c^{\mathsf T}x\\ \text{subject to}&x_1F_1+x_2F_2+\cdots+x_nF_n+G\preceq0,\\ &Ax=b,\end{array}$$
with $F_i,G\in\mathbb S^k$. The constraint is a *linear matrix inequality* (LMI); several LMIs can be combined into one block-diagonal LMI.

:::

::: {#prp-lp-socp-as-sdp .proposition name="LP and SOCP as SDP"}

1. The LP constraint $Ax\preceq b$ is the LMI $\operatorname{diag}(Ax-b)\preceq0$.

2. The second-order cone constraint $\lVert Ax+b\rVert_2\le c^{\mathsf T}x+d$ is the LMI
$$\begin{bmatrix}(c^{\mathsf T}x+d)I&Ax+b\\(Ax+b)^{\mathsf T}&c^{\mathsf T}x+d\end{bmatrix}\succeq0.$$

:::

::: {.proof}

1. A diagonal matrix is negative semidefinite iff its diagonal entries are nonpositive.

2. Write $t=c^{\mathsf T}x+d$, $u=Ax+b$ and $M=\begin{bmatrix}tI&u\\u^{\mathsf T}&t\end{bmatrix}$. If $t>0$, the Schur complement criterion says $M\succeq0$ iff $t-u^{\mathsf T}u/t\ge0$, that is, $\lVert u\rVert_2\le t$.

3. If $t=0$, $M\succeq0$ forces $u=0$ (look at $z^{\mathsf T}Mz$ with $z=(su,1)$, which is $2s\lVert u\rVert_2^2$ and can be made negative), matching $\lVert u\rVert_2\le0$. If $t<0$ both sides fail.

:::

::: {#exm-eigenvalue-minimization .example name="Eigenvalue and matrix norm minimization"}

1. Minimize $\lambda_{\max}(A(x))$ with $A(x)=A_0+x_1A_1+\cdots+x_nA_n$, $A_i\in\mathbb S^k$: equivalently minimize $t$ subject to $A(x)\preceq tI$, since $\lambda_{\max}(A)\le t\iff A\preceq tI$.

2. Minimize $\lVert A(x)\rVert_2$ with $A(x)\in\mathbb{R}^{p\times q}$ affine in $x$: equivalently minimize $t$ subject to $\begin{bmatrix}tI&A(x)\\A(x)^{\mathsf T}&tI\end{bmatrix}\succeq0$, because $\lVert A\rVert_2\le t\iff A^{\mathsf T}A\preceq t^2I$ (with $t\ge0$), which is the Schur complement condition.

:::

::: {#rmk-semidefinite-programs-1 .remark name="Why semidefinite programming matters"}

SDPs can be solved by interior-point methods (@sec-math-optimization-algorithms-phase-one-and-complexity) almost as efficiently as LPs, and many nonconvex problems have SDP relaxations that give useful bounds (for instance two-way partitioning, @exm-two-way-partitioning-dual).

:::
