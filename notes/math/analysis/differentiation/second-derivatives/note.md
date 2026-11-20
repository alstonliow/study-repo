---
title: "Second Derivatives and Taylor's Theorem in Several Variables"
sources: [camib-at-a6, mit1802-8, mit1802-9, mit1802-10, mit1802n-TA, mit1802n-SD, mit1806-27]
requires: [math/analysis/differentiation/chain-rule-and-mean-value, math/analysis/real/differentiability/taylors-theorem, math/linear-algebra/positive-definite/positive-definite-matrices]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 6.5, in our own wording; the counterexample to symmetry was checked symbolically; the second derivative test is our own addition from the second-order Taylor theorem; proofs written out in steps. The calculus notes state the equality of mixed partials and the second derivative test for two variables with informal proofs; the rigorous versions here carry related= and merged 2026-11-20 (owner): thm-symmetry-mixed-partials replaces the calculus block thm-mixed-partials (MIT 18.02, Lecture 8-9, Supplementary Notes TA); thm-second-derivative-test-several replaces the calculus block thm-second-derivative-test-two-variables (MIT 18.02, Lectures 9-10, Supplementary Notes SD: part 4, the AC-B^2 form) and the linear-algebra block thm-second-derivative-test (MIT 18.06, Lecture 27: the smallest-eigenvalue bound in step 1). -->

The derivative $Df$ of a map is again a map, from $U$ to the space of linear maps. Differentiating it once more gives a symmetric bilinear form, the Hessian, which controls the second-order behaviour of $f$ and decides the nature of critical points.

Throughout, $U\subseteq\mathbb R^n$ is open, and $D_iD_jf=D_i(D_jf)$ means: first the partial derivative in direction $e_j$, then in direction $e_i$.

::: {#def-second-derivative-several .definition name="Second derivative" related="def-higher-partial-derivatives"}

Let $f:U\to\mathbb R^m$ be differentiable. $f$ is *twice differentiable* at $a$ if $Df:U\to L(\mathbb R^n;\mathbb R^m)$ is differentiable at $a$. Its derivative $D^2f(a)$ is a linear map $\mathbb R^n\to L(\mathbb R^n;\mathbb R^m)$, which we identify with the bilinear map
$$D^2f(a)(u,v)=\bigl(D^2f(a)u\bigr)v=\sum_{i,j=1}^nu_iv_j\,D_iD_jf(a).$$
$f$ is $C^2$ on $U$ if all second partial derivatives $D_iD_jf$ exist and are continuous on $U$.

:::

The formula holds because $D^2f(a)u$ is the derivative of $Df$ in the direction $u$ (@prp-derivative-partials-jacobian, applied to $Df$ entry by entry). The $j$-th column of $Df$ is $D_jf$, and its derivative in the direction $u$ is $\sum_iu_iD_iD_jf(a)$; applying the resulting linear map to $v=\sum_jv_je_j$ gives the double sum. By @thm-continuous-partials-differentiable applied to the partial derivatives $D_jf$, a $C^2$ map is twice differentiable at every point.

## Symmetry of mixed partial derivatives

::: {#exm-mixed-partials-differ .example name="Mixed partial derivatives can differ"}

Let $f(x,y)=\frac{xy(x^2-y^2)}{x^2+y^2}$ for $(x,y)\ne0$ and $f(0)=0$. One computes $D_1f(0,y)=-y$ and $D_2f(x,0)=x$ for all $x,y$. Hence $D_2D_1f(0)=-1$ but $D_1D_2f(0)=1$. The second partial derivatives exist everywhere but are not continuous at $0$.

:::

::: {#thm-symmetry-mixed-partials .theorem name="Symmetry of mixed partial derivatives"}

Let $f:U\to\mathbb R^m$, $a\in U$ and $i\ne j$. If $D_iD_jf$ and $D_jD_if$ exist on a neighbourhood of $a$ and are continuous at $a$, then $D_iD_jf(a)=D_jD_if(a)$. In particular, if $f$ is $C^2$ then $D^2f(a)$ is a symmetric bilinear form.

:::

::: {.proof}

1. *Reduce to two real variables.* Working component by component we may take $m=1$, and only the coordinates $i,j$ vary, so we may take $n=2$, $i=1$, $j=2$, $a=0$. The hypotheses include that $D_1f$ and $D_2f$ exist near $0$.

2. *A second difference.* For small $h,k\ne0$ let
$$\Delta(h,k)=f(h,k)-f(h,0)-f(0,k)+f(0,0).$$

3. *First way.* Let $\alpha(s)=f(s,k)-f(s,0)$, so $\Delta=\alpha(h)-\alpha(0)$. By @thm-mean-value, $\Delta=h\,\alpha'(s)=h\bigl(D_1f(s,k)-D_1f(s,0)\bigr)$ for some $s$ between $0$ and $h$. Applying the mean value theorem to $t\mapsto D_1f(s,t)$ gives $\Delta=hk\,D_2D_1f(s,t)$ for some $t$ between $0$ and $k$.

4. *Second way.* Starting from $\beta(t)=f(h,t)-f(0,t)$ in the same way gives $\Delta=hk\,D_1D_2f(s',t')$ for some $s'$ between $0$ and $h$ and $t'$ between $0$ and $k$.

5. *Let $h,k\to0$.* So $D_2D_1f(s,t)=D_1D_2f(s',t')$, where both points tend to $0$ as $(h,k)\to0$. By continuity at $0$, $D_2D_1f(0)=D_1D_2f(0)$.

6. If $f$ is $C^2$, all mixed partials are equal in pairs, so $D^2f(a)(u,v)=D^2f(a)(v,u)$ by the formula in @def-second-derivative-several.

:::

For $f:U\to\mathbb R$ of class $C^2$, the symmetric matrix $H_f(a)=\bigl(D_iD_jf(a)\bigr)_{i,j}$ is the *Hessian*; $D^2f(a)(u,v)=u^{\mathsf T}H_f(a)v$.

## Taylor's theorem and critical points

::: {#thm-taylor-second-order .theorem name="Second-order Taylor theorem"}

Let $f:U\to\mathbb R$ be $C^2$, $a\in U$ and $B_r(a)\subseteq U$. Then for $\|h\|<r$,
$$f(a+h)=f(a)+Df(a)h+\tfrac12D^2f(a)(h,h)+E(h),\qquad\frac{E(h)}{\|h\|^2}\to0\text{ as }h\to0.$$

:::

::: {.proof}

1. *Restrict to a line.* Fix $h$ with $0<\|h\|<r$ and let $g(t)=f(a+th)$ for $t$ in an open interval containing $[0,1]$. By the chain rule (@thm-chain-rule-several-variables), $g'(t)=Df(a+th)h=\sum_jh_jD_jf(a+th)$.

2. *Differentiate again.* Each $D_jf$ has continuous partial derivatives, hence is differentiable (@thm-continuous-partials-differentiable), so by the chain rule $g''(t)=\sum_{i,j}h_ih_jD_iD_jf(a+th)=D^2f(a+th)(h,h)$.

3. *One-variable Taylor.* By @thm-taylor-lagrange with $n=2$, $g(1)=g(0)+g'(0)+\frac12g''(s)$ for some $s\in(0,1)$. That is, the formula holds with
$$E(h)=\tfrac12\sum_{i,j}h_ih_j\bigl(D_iD_jf(a+sh)-D_iD_jf(a)\bigr).$$

4. *Estimate.* Since $|h_ih_j|\le\|h\|^2$, $\frac{|E(h)|}{\|h\|^2}\le\frac12\sum_{i,j}|D_iD_jf(a+sh)-D_iD_jf(a)|$, which tends to $0$ as $h\to0$ by continuity of the second partial derivatives at $a$.

:::

::: {#thm-second-derivative-test-several .theorem name="Second derivative test"}

Let $f:U\to\mathbb R$ be $C^2$ and $Df(a)=0$.

1. If $H_f(a)$ is positive definite (@def-positive-definite), $f$ has a strict local minimum at $a$.
2. If $H_f(a)$ is negative definite, $f$ has a strict local maximum at $a$.
3. If $u^{\mathsf T}H_f(a)u>0>v^{\mathsf T}H_f(a)v$ for some $u,v$ (indefinite), $f$ has neither at $a$.
4. For $n=2$, with $A=D_1D_1f(a)$, $B=D_1D_2f(a)$, $C=D_2D_2f(a)$: if $AC-B^2>0$ and $A>0$ there is a strict local minimum, if $AC-B^2>0$ and $A<0$ a strict local maximum, and if $AC-B^2<0$ neither (a saddle point). If $AC-B^2=0$ the test gives no conclusion.

:::

::: {.proof}

1. *A uniform lower bound.* The unit sphere $S=\{\|u\|=1\}$ is closed and bounded, hence sequentially compact (@thm-heine-borel-rn), and $u\mapsto u^{\mathsf T}H_f(a)u$ is continuous and positive on it. By @cor-extreme-value-compact it attains a minimum $\mu>0$. By homogeneity, $h^{\mathsf T}H_f(a)h\ge\mu\|h\|^2$ for all $h$. (Alternatively, $\mu$ is the smallest eigenvalue of $H_f(a)$, positive by @thm-positive-definite-tests.)

2. *Positive definite.* By @thm-taylor-second-order with $Df(a)=0$,
$$f(a+h)-f(a)=\tfrac12h^{\mathsf T}H_f(a)h+E(h)\ge\Bigl(\frac\mu2-\frac{|E(h)|}{\|h\|^2}\Bigr)\|h\|^2.$$
Choose $\rho>0$ with $\frac{|E(h)|}{\|h\|^2}<\frac\mu2$ for $0<\|h\|<\rho$. Then $f(a+h)>f(a)$ for those $h$.

3. *Negative definite:* apply part 1 to $-f$.

4. *Indefinite.* For small $t\ne0$, $f(a+tu)-f(a)=t^2\bigl(\frac12u^{\mathsf T}H_f(a)u+\frac{E(tu)}{t^2}\bigr)$, and $\frac{E(tu)}{t^2}=\frac{E(tu)}{\|tu\|^2}\|u\|^2\to0$, so this is positive for small $t$. In the same way $f(a+tv)<f(a)$ for small $t\ne0$. So every neighbourhood of $a$ contains points with larger and with smaller values.

5. *Two variables.* $H_f(a)=\begin{pmatrix}A&B\\B&C\end{pmatrix}$ has determinant $AC-B^2$, the product of its two eigenvalues. If $AC-B^2>0$ the eigenvalues have the same sign, which is the sign of $A$ (the trace $A+C$ has the sign of $A$, since $AC>B^2\ge0$ forces $A$ and $C$ to have the same sign): positive definite if $A>0$, negative definite if $A<0$, so parts 1 and 2 apply. If $AC-B^2<0$ the eigenvalues have opposite signs and part 3 applies with eigenvectors as $u,v$.

6. *No conclusion when $AC-B^2=0$*: see the examples after the proof.

:::

When $H_f(a)$ is only semidefinite the test is silent: $x^4+y^4$, $-x^4-y^4$ and $x^4-y^4$ all have $Df(0)=0$ and $H_f(0)=0$, with a minimum, a maximum and neither at $0$.
