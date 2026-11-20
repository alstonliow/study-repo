---
title: "The Derivative of a Map between Euclidean Spaces"
sources: [camib-at-a6, mit1802-8, mit1802-9, mit1802n-TA]
requires: [math/analysis/metric-spaces/continuous-maps, math/analysis/real/differentiability/differentiability-and-inverses, math/calculus/multivariable/differentiation/partial-derivatives]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 6.1, in our own wording; the examples are ours (checked symbolically); proofs written out in steps. The calculus notes state linear approximation for two variables with an informal proof; the rigorous versions here carry related= and merged 2026-11-20 (owner): thm-continuous-partials-differentiable replaces the calculus block thm-linear-approximation-two-variables (MIT 18.02, Lectures 8-9 and Supplementary Notes TA); its proof is the calculus two-step mean value argument extended to n coordinates. -->

In one variable, $f$ is differentiable at $a$ when $f(a+h)=f(a)+\lambda h+o(h)$ (@prp-derivative-little-o). In several variables the number $\lambda$ becomes a linear map, and this is the definition.

Throughout, $U\subseteq\mathbb R^n$ is open, so that $a+h\in U$ for all small $h$, and $\|\cdot\|$ is any norm; by @thm-norms-equivalent-finite-dimension the choice does not affect the definitions. $L(\mathbb R^n;\mathbb R^m)$ is the space of linear maps $\mathbb R^n\to\mathbb R^m$, identified with $m\times n$ matrices.

::: {#def-derivative-several-variables .definition name="Derivative of a map" related="prp-derivative-little-o"}

A map $f:U\to\mathbb R^m$ is *differentiable* at $a\in U$ if there is a linear map $A\in L(\mathbb R^n;\mathbb R^m)$ with
$$\lim_{h\to0}\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}=0,$$
that is, $f(a+h)=f(a)+Ah+o(\|h\|)$. Then $A$ is the *derivative* $Df(a)$. $f$ is differentiable on $U$ if it is differentiable at every point of $U$.

:::

::: {#prp-derivative-several-variables-basic .proposition name="Basic properties of the derivative"}

Let $f,g:U\to\mathbb R^m$ and $a\in U$.

1. The derivative, if it exists, is unique.
2. If $f$ is differentiable at $a$, it is continuous at $a$.
3. $f=(f_1,\dots,f_m)$ is differentiable at $a$ if and only if every component $f_i$ is, and then the $i$-th row of $Df(a)$ is $Df_i(a)$.
4. If $f,g$ are differentiable at $a$, so is $\lambda f+\mu g$, with $D(\lambda f+\mu g)(a)=\lambda Df(a)+\mu Dg(a)$.
5. A linear map $A$ is differentiable everywhere with $DA(a)=A$; a constant map has derivative $0$.

:::

::: {.proof}

1. If $A$ and $B$ both qualify, then $\frac{\|(A-B)h\|}{\|h\|}\le\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}+\frac{\|f(a+h)-f(a)-Bh\|}{\|h\|}\to0$. Put $h=tv$ for a fixed $v\ne0$ and $t\to0^+$: the left side is the constant $\frac{\|(A-B)v\|}{\|v\|}$, so $(A-B)v=0$ for all $v$.

2. $\|f(a+h)-f(a)\|\le\|f(a+h)-f(a)-Df(a)h\|+\|Df(a)h\|$. The first term is $o(\|h\|)$, and the second tends to $0$ because linear maps are continuous (@thm-linear-maps-continuous).

3. Use $\|\cdot\|_\infty$ on $\mathbb R^m$: a vector tends to $0$ if and only if each component does.

4. The error term of $\lambda f+\mu g$ is $\lambda$ times that of $f$ plus $\mu$ times that of $g$.

5. For linear $A$ the error $A(a+h)-Aa-Ah$ is identically $0$.

:::

## Partial derivatives

::: {#def-directional-derivative-several .definition name="Directional and partial derivatives" related="def-directional-derivative def-partial-derivative"}

For $f:U\to\mathbb R^m$, $a\in U$ and $v\in\mathbb R^n$, the *directional derivative* is
$$D_vf(a)=\lim_{t\to0}\frac{f(a+tv)-f(a)}t$$
when the limit exists. With $e_1,\dots,e_n$ the standard basis, $D_jf(a)=D_{e_j}f(a)=\frac{\partial f}{\partial x_j}(a)$ is the $j$-th *partial derivative*.

:::

::: {#prp-derivative-partials-jacobian .proposition name="The derivative determines the partial derivatives"}

If $f:U\to\mathbb R^m$ is differentiable at $a$, then every directional derivative exists and $D_vf(a)=Df(a)v$. In particular $Df(a)$ is the matrix of partial derivatives (the *Jacobian matrix*)
$$Df(a)=\Bigl(\frac{\partial f_i}{\partial x_j}(a)\Bigr)_{1\le i\le m,\ 1\le j\le n},$$
and for $m=1$, $Df(a)v=\nabla f(a)\cdot v$ with $\nabla f(a)$ the gradient (@def-gradient).

:::

::: {.proof}

1. For $v\ne0$ put $h=tv$: $\Bigl\|\frac{f(a+tv)-f(a)}t-Df(a)v\Bigr\|=\frac{\|f(a+tv)-f(a)-Df(a)(tv)\|}{\|tv\|}\|v\|\to0$ as $t\to0$. For $v=0$ both sides are $0$.

2. The $j$-th column of a matrix is its value on $e_j$, which is $D_jf(a)$; its $i$-th entry is $D_jf_i(a)$.

:::

The converse fails badly: partial derivatives, even all directional derivatives, may exist without $f$ being differentiable.

::: {#exm-partials-without-derivative .example name="Partial derivatives are not enough"}

1. Let $f(x,y)=\frac{xy}{x^2+y^2}$ for $(x,y)\ne0$ and $f(0)=0$. Since $f=0$ on both axes, $D_1f(0)=D_2f(0)=0$. But $f(t,t)=\frac12$ for $t\ne0$, so $f$ is not even continuous at $0$, hence not differentiable there.
2. Let $g(x,y)=\frac{x^2y}{x^2+y^2}$ for $(x,y)\ne0$ and $g(0)=0$. It is continuous ($|g|\le|y|$), and for $v=(v_1,v_2)\ne0$, $\frac{g(tv)}t=\frac{v_1^2v_2}{v_1^2+v_2^2}$, so every $D_vg(0)$ exists. But $v\mapsto D_vg(0)$ is not linear ($D_{e_1}g(0)=D_{e_2}g(0)=0$ while $D_{(1,1)}g(0)=\frac12$), so by @prp-derivative-partials-jacobian $g$ is not differentiable at $0$.

:::

::: {#thm-continuous-partials-differentiable .theorem name="Continuous partial derivatives imply differentiability"}

Let $f:U\to\mathbb R^m$ and $a\in U$. If all partial derivatives $D_jf$ exist on a neighbourhood of $a$ and are continuous at $a$, then $f$ is differentiable at $a$.

:::

::: {.proof}

1. By @prp-derivative-several-variables-basic we may assume $m=1$. Let $A$ be the linear map with matrix $(D_1f(a),\dots,D_nf(a))$; we show $f(a+h)-f(a)-Ah=o(\|h\|)$, using $\|\cdot\|_2$.

2. *Move along the axes.* For small $h$, put $p_0=a$ and $p_j=a+h_1e_1+\dots+h_je_j$, so $p_n=a+h$ and all $p_j$ lie in a ball around $a$ on which the partial derivatives exist. Then
$$f(a+h)-f(a)=\sum_{j=1}^n\bigl(f(p_j)-f(p_{j-1})\bigr).$$

3. *Mean value theorem on each segment.* $p_j$ and $p_{j-1}$ differ only in coordinate $j$, so $t\mapsto f(p_{j-1}+te_j)$ is differentiable on $[0,h_j]$ with derivative $D_jf(p_{j-1}+te_j)$. By @thm-mean-value there is $q_j$ on the segment from $p_{j-1}$ to $p_j$ with $f(p_j)-f(p_{j-1})=h_jD_jf(q_j)$.

4. *Estimate.* Hence
$$|f(a+h)-f(a)-Ah|=\Bigl|\sum_jh_j\bigl(D_jf(q_j)-D_jf(a)\bigr)\Bigr|\le\|h\|_2\sum_j|D_jf(q_j)-D_jf(a)|.$$
As $h\to0$, every $q_j\to a$ (it lies within $\|h\|_2$ of $a$), so by continuity of $D_jf$ at $a$ the sum tends to $0$. So the error is $o(\|h\|_2)$.

:::

For example, $f(x,y)=(e^x\cos y,\ e^x\sin y)$ has continuous partial derivatives everywhere, so it is differentiable with
$$Df(x,y)=\begin{pmatrix}e^x\cos y&-e^x\sin y\\e^x\sin y&e^x\cos y\end{pmatrix}.$$
