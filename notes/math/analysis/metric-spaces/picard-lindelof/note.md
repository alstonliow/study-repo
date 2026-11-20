---
title: "The Picard–Lindelöf Theorem"
sources: [camib-at-a3, camib-at-a5]
requires: [math/analysis/metric-spaces/contraction-mapping, math/analysis/real/integration/fundamental-theorem-of-calculus]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 3.2 (integrals of vector-valued functions) and 5.6 (Picard-Lindelöf), in our own wording; the Picard iterates for x'=x were computed by us; proofs written out in steps. -->

An initial value problem $x'(t)=F(t,x(t))$, $x(a)=x_0$, is equivalent to an integral equation, and the integral equation says that $x$ is a fixed point of a map on a space of functions. The contraction mapping theorem then gives existence and uniqueness.

## Integrals of vector-valued functions

::: {#def-vector-valued-integral .definition name="Integral of a vector-valued function"}

A function $f=(f_1,\dots,f_n):[a,b]\to\mathbb R^n$ is *Riemann integrable* if each component $f_i$ is, and then
$$\int_a^bf=\Bigl(\int_a^bf_1,\dots,\int_a^bf_n\Bigr)\in\mathbb R^n.$$

:::

Linearity, additivity over intervals and the fundamental theorem of calculus hold componentwise.

::: {#prp-norm-of-integral .proposition name="The norm of an integral"}

If $f:[a,b]\to\mathbb R^n$ is continuous, then
$$\Bigl\|\int_a^bf\Bigr\|_2\le\int_a^b\|f(t)\|_2\,dt.$$

:::

::: {.proof}

1. Let $v=\int_a^bf$. If $v=0$ there is nothing to prove.

2. By linearity, $\|v\|_2^2=\sum_iv_i\int_a^bf_i=\int_a^b\langle v,f(t)\rangle\,dt$.

3. By @thm-cauchy-schwarz-inner-product and monotonicity of the integral (@prp-integral-monotone), this is at most $\int_a^b\|v\|_2\|f(t)\|_2\,dt=\|v\|_2\int_a^b\|f\|_2$. Divide by $\|v\|_2>0$.

:::

(The integral on the right exists because $t\mapsto\|f(t)\|_2$ is continuous.)

## Existence and uniqueness

::: {#thm-picard-lindelof .theorem name="Picard–Lindelöf theorem"}

Let $x_0\in\mathbb R^n$, $R>0$, $a<b$, and let $\overline B=\{x\in\mathbb R^n:\|x-x_0\|_2\le R\}$. Let $F:[a,b]\times\overline B\to\mathbb R^n$ be continuous and *Lipschitz in $x$*: there is $K$ with
$$\|F(t,x)-F(t,y)\|_2\le K\|x-y\|_2\qquad\text{for all }t\in[a,b],\ x,y\in\overline B.$$
Let $M=\sup\|F\|_2$ and suppose $M(b-a)\le R$. Then there is exactly one differentiable $x:[a,b]\to\overline B$ with
$$x'(t)=F(t,x(t))\quad(t\in[a,b]),\qquad x(a)=x_0.$$

:::

::: {.proof}

1. *The space.* Let $Y=\{x\in C([a,b];\mathbb R^n):x(t)\in\overline B\text{ for all }t\}$ with $\|\cdot\|_\infty$. $C([a,b];\mathbb R^n)$ is complete (@thm-bounded-functions-complete), and $Y$ is closed in it: a uniform limit of functions with values in the closed set $\overline B$ has values in $\overline B$. By @thm-closed-subspace-complete, $Y$ is complete; it is non-empty since it contains the constant $x_0$.

2. *The map.* For $x\in Y$ define $(Tx)(t)=x_0+\int_a^tF(s,x(s))\,ds$. The integrand is continuous, so $Tx$ is continuous, and by @prp-norm-of-integral $\|(Tx)(t)-x_0\|_2\le M(t-a)\le M(b-a)\le R$. So $T:Y\to Y$.

3. *Fixed points are the solutions.* If $Tx=x$, then $x(a)=x_0$ and, by the fundamental theorem of calculus (@thm-ftc-continuous-integrand) in each component, $x'(t)=F(t,x(t))$. Conversely, a solution $x$ has continuous derivative $F(t,x(t))$, so by @thm-ftc-integrable-derivative $x(t)=x_0+\int_a^tx'=(Tx)(t)$, and $x\in Y$ by assumption.

4. *Iterates of $T$ contract.* We show by induction on $m$ that for $x,y\in Y$ and $t\in[a,b]$,
$$\|(T^mx)(t)-(T^my)(t)\|_2\le\frac{K^m(t-a)^m}{m!}\|x-y\|_\infty.$$
The case $m=0$ is clear. If it holds for $m$, then by @prp-norm-of-integral and the Lipschitz condition
$$\|(T^{m+1}x)(t)-(T^{m+1}y)(t)\|_2\le\int_a^tK\|(T^mx)(s)-(T^my)(s)\|_2\,ds\le\int_a^t\frac{K^{m+1}(s-a)^m}{m!}\,ds\,\|x-y\|_\infty,$$
and the integral equals $\frac{K^{m+1}(t-a)^{m+1}}{(m+1)!}$.

5. *Conclusion.* So $\|T^mx-T^my\|_\infty\le\frac{(K(b-a))^m}{m!}\|x-y\|_\infty$, and $\frac{c^m}{m!}\to0$ for every $c$, so $T^m$ is a contraction for large $m$. By @cor-contraction-iterate, $T$ has exactly one fixed point, which by step 3 is the unique solution.

:::

::: {#exm-picard-iterates-exponential .example name="Picard iteration for $x'=x$"}

Take $F(t,x)=x$, $x(0)=1$, so $(Tx)(t)=1+\int_0^tx(s)\,ds$. Starting from $x_0(t)=1$, the iterates are
$$x_1(t)=1+t,\qquad x_2(t)=1+t+\tfrac{t^2}2,\qquad\dots,\qquad x_m(t)=\sum_{k=0}^m\frac{t^k}{k!},$$
the partial sums of the exponential series (@def-exponential-series), converging uniformly on bounded intervals to the solution $e^t$.

:::

::: {#rmk-picard-lindelof-hypotheses .remark name="The Lipschitz condition"}

Without it, uniqueness fails. $x'=2\sqrt{|x|}$, $x(0)=0$ has the solutions $x(t)=0$ and $x(t)=t^2$ for $t\ge0$; the function $2\sqrt{|x|}$ is continuous but not Lipschitz near $0$. The bound $M(b-a)\le R$ keeps the solution inside the region where $F$ is defined; it limits how long the solution is guaranteed to exist, as for $x'=x^2$, $x(0)=1$, whose solution $\frac1{1-t}$ blows up at $t=1$.

:::
