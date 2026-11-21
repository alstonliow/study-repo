---
title: "Second-Order Cone Programs"
sources: [ee364a-4]
requires: [math/optimization/convex-problems/linear-and-quadratic-programs]
status: draft
---

<!-- Added 2026-11-21 from Stanford EE364A (CVX101, Winter 2014), slides on convex optimization problems, in our own wording; proofs written out in steps. -->

A second-order cone program has affine objective and constraints saying that an affine function lies in a second-order cone. It covers QCQPs and handles linear programs whose data are uncertain.

::: {#def-socp .definition name="Second-order cone program"}

A *second-order cone program* (SOCP) is
$$\begin{array}{ll}\text{minimize}&f^{\mathsf T}x\\ \text{subject to}&\lVert A_ix+b_i\rVert_2\le c_i^{\mathsf T}x+d_i,\quad i=1,\dots,m,\\ &Fx=g.\end{array}$$
Each inequality says $(A_ix+b_i,\,c_i^{\mathsf T}x+d_i)$ lies in the second-order cone (@def-norm-ball-norm-cone). With $A_i=0$ it is an LP; with $c_i=0$ it is a QCQP after squaring.

:::

::: {#prp-qcqp-as-socp .proposition name="Convex quadratic constraints are second-order cone constraints"}

For $P=L^{\mathsf T}L\succeq0$,
$$x^{\mathsf T}Px+q^{\mathsf T}x+r\le0\iff\left\lVert\begin{bmatrix}2Lx\\ 1+q^{\mathsf T}x+r\end{bmatrix}\right\rVert_2\le1-q^{\mathsf T}x-r.$$

:::

::: {.proof}

1. Put $s=q^{\mathsf T}x+r$ and $w=x^{\mathsf T}Px=\lVert Lx\rVert_2^2$. The left side is $w\le-s$.

2. The right side is $4w+(1+s)^2\le(1-s)^2$ together with $1-s\ge0$. Expanding, $4w+1+2s+s^2\le1-2s+s^2$, that is, $w\le-s$.

3. If $w\le-s$ then $-s\ge0$, so $1-s\ge1>0$ holds automatically.

:::

::: {#def-robust-lp .definition name="Robust linear program"}

Consider an LP with uncertain constraint vectors, $a_i\in\mathcal E_i=\{\bar a_i+P_iu\mid\lVert u\rVert_2\le1\}$. The *robust LP* requires every constraint for every possible $a_i$:
$$\text{minimize }c^{\mathsf T}x\quad\text{s.t. }a_i^{\mathsf T}x\le b_i\ \text{for all}\ a_i\in\mathcal E_i.$$
It is the SOCP
$$\text{minimize }c^{\mathsf T}x\quad\text{s.t. }\bar a_i^{\mathsf T}x+\lVert P_i^{\mathsf T}x\rVert_2\le b_i,$$
since $\sup_{\lVert u\rVert_2\le1}(\bar a_i+P_iu)^{\mathsf T}x=\bar a_i^{\mathsf T}x+\lVert P_i^{\mathsf T}x\rVert_2$ by Cauchy–Schwarz (equality at $u=P_i^{\mathsf T}x/\lVert P_i^{\mathsf T}x\rVert_2$).

:::

::: {#exm-chance-constrained-lp .example name="Chance constraints with Gaussian data"}

If instead $a_i\sim\mathcal N(\bar a_i,\Sigma_i)$, then $a_i^{\mathsf T}x\sim\mathcal N(\bar a_i^{\mathsf T}x,\,x^{\mathsf T}\Sigma_ix)$ and
$$\operatorname{P}(a_i^{\mathsf T}x\le b_i)\ge\eta\iff\bar a_i^{\mathsf T}x+\Phi^{-1}(\eta)\lVert\Sigma_i^{1/2}x\rVert_2\le b_i,$$
with $\Phi$ the standard normal distribution function (@def-normal-distribution). For $\eta\ge\frac12$, $\Phi^{-1}(\eta)\ge0$ and this is a second-order cone constraint.

:::

::: {#rmk-second-order-cone-programs-1 .remark name="Norms in the objective"}

Objectives such as $\sum_i\lVert A_ix+b_i\rVert_2$ or $\max_i\lVert A_ix+b_i\rVert_2$ become SOCPs in epigraph form: minimize $\sum_it_i$ (or $t$) subject to $\lVert A_ix+b_i\rVert_2\le t_i$ (or $\le t$).

:::
