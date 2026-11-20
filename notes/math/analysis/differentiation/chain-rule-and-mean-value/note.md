---
title: "The Operator Norm, the Chain Rule and the Mean Value Inequality"
sources: [camib-at-a6, mit1802-11]
requires: [math/analysis/differentiation/derivative-of-maps, math/analysis/topology/connectedness]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Sections 6.2-6.3, in our own wording; examples ours; proofs written out in steps. The calculus chain rule (math/calculus/multivariable/differentiation/differentials-and-chain-rule) is proved there informally for continuous partial derivatives; the version here carries related= and merged 2026-11-20 (owner): thm-chain-rule-several-variables replaces the calculus block thm-multivariable-chain-rule (MIT 18.02, Lecture 11); the coordinate form after it comes from that block. -->

To estimate $f(b)-f(a)$ from bounds on $Df$, we need a size for linear maps. The operator norm measures how much a linear map can stretch a vector.

Throughout, $\mathbb R^n$ carries the Euclidean norm $\|\cdot\|=\|\cdot\|_2$.

::: {#def-operator-norm .definition name="Operator norm"}

The *operator norm* of $A\in L(\mathbb R^n;\mathbb R^m)$ is
$$\|A\|=\sup\{\|Ax\|:x\in\mathbb R^n,\ \|x\|\le1\}.$$

:::

::: {#prp-operator-norm-properties .proposition name="Properties of the operator norm"}

1. $\|A\|$ is finite, and $\|Ax\|\le\|A\|\,\|x\|$ for all $x$; $\|A\|$ is the least constant with this property.
2. $\|\cdot\|$ is a norm on $L(\mathbb R^n;\mathbb R^m)$.
3. If $B\in L(\mathbb R^m;\mathbb R^p)$, then $\|BA\|\le\|B\|\,\|A\|$.
4. If $A=(a_{ij})$, then $\max_{i,j}|a_{ij}|\le\|A\|\le\bigl(\sum_{i,j}a_{ij}^2\bigr)^{1/2}$.

:::

::: {.proof}

1. By @thm-linear-maps-continuous, $\|Ax\|\le C\|x\|$ for some $C$, so $\|A\|\le C$. For $x\ne0$, $\frac x{\|x\|}$ has norm $1$, so $\|Ax\|=\|x\|\bigl\|A\frac x{\|x\|}\bigr\|\le\|A\|\|x\|$. Conversely any constant $C$ with $\|Ax\|\le C\|x\|$ bounds the supremum.

2. If $\|A\|=0$ then $Ax=0$ for all $x$. Homogeneity is clear, and $\|(A+B)x\|\le\|Ax\|+\|Bx\|\le(\|A\|+\|B\|)\|x\|$ gives the triangle inequality by part 1.

3. $\|BAx\|\le\|B\|\|Ax\|\le\|B\|\|A\|\|x\|$; apply part 1.

4. $|a_{ij}|=|(Ae_j)_i|\le\|Ae_j\|\le\|A\|$. For the upper bound, by @thm-cauchy-schwarz-inner-product $(Ax)_i^2=\bigl(\sum_ja_{ij}x_j\bigr)^2\le\bigl(\sum_ja_{ij}^2\bigr)\|x\|^2$; sum over $i$.

:::

By part 4, a sequence of matrices converges in the operator norm if and only if every entry converges; so a map $x\mapsto Df(x)$ is continuous in the operator norm if and only if every partial derivative is continuous. For a diagonal matrix, $\|\operatorname{diag}(d_1,\dots,d_n)\|=\max_i|d_i|$, while $\bigl(\sum d_i^2\bigr)^{1/2}$ can be $\sqrt n$ times larger, so the bounds in part 4 are not equalities in general.

## The chain rule

::: {#thm-chain-rule-several-variables .theorem name="Chain rule" related="thm-derivative-chain-rule"}

Let $U\subseteq\mathbb R^n$ and $V\subseteq\mathbb R^m$ be open, $f:U\to V$ differentiable at $a$, and $g:V\to\mathbb R^p$ differentiable at $f(a)$. Then $g\circ f$ is differentiable at $a$ and
$$D(g\circ f)(a)=Dg(f(a))\,Df(a).$$

:::

::: {.proof}

1. *Error terms.* Write $b=f(a)$, $A=Df(a)$, $B=Dg(b)$, and
$$f(a+h)=b+Ah+\varepsilon(h)\|h\|,\qquad g(b+k)=g(b)+Bk+\eta(k)\|k\|,$$
where $\varepsilon(h)\to0$ as $h\to0$ and $\eta(k)\to0$ as $k\to0$; set $\varepsilon(0)=0$, $\eta(0)=0$ so that $\eta$ is continuous at $0$.

2. *Substitute.* Put $k=k(h)=f(a+h)-b=Ah+\varepsilon(h)\|h\|$. Then
$$g(f(a+h))=g(b)+BAh+B\varepsilon(h)\|h\|+\eta(k)\|k\|.$$

3. *The first error.* $\|B\varepsilon(h)\|h\|\|\le\|B\|\,\|\varepsilon(h)\|\,\|h\|=o(\|h\|)$ by @prp-operator-norm-properties.

4. *The second error.* $\|k\|\le(\|A\|+\|\varepsilon(h)\|)\|h\|$, so $\frac{\|k\|}{\|h\|}$ stays bounded as $h\to0$, and $k\to0$. Hence $\eta(k)\to0$ and $\eta(k)\|k\|=o(\|h\|)$.

5. So $g(f(a+h))=g(f(a))+BAh+o(\|h\|)$, which says $D(g\circ f)(a)=BA$.

:::

In coordinates this is the familiar sum: $\frac{\partial(g\circ f)_i}{\partial x_j}=\sum_k\frac{\partial g_i}{\partial y_k}\frac{\partial f_k}{\partial x_j}$. Only differentiability is needed, not continuous partial derivatives. For a curve $t\mapsto(x(t),y(t),z(t))$ followed by $w=f(x,y,z)$ it reads $\frac{dw}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}+f_z\frac{dz}{dt}$, the form used in @sec-math-calculus-multivariable-differentiation-differentials-and-chain-rule.

## Mean value inequalities

There is no mean value *equation* for vector-valued maps: $f(t)=(\cos t,\sin t)$ has $f(2\pi)-f(0)=0$ but $f'(t)\ne0$ for all $t$. An inequality survives.

::: {#thm-mean-value-inequality-curves .theorem name="Mean value inequality for curves"}

Let $f:[a,b]\to\mathbb R^m$ be continuous, differentiable on $(a,b)$, with $\|f'(t)\|\le M$ there. Then $\|f(b)-f(a)\|\le M(b-a)$.

:::

::: {.proof}

1. Let $v=f(b)-f(a)$ and $g(t)=v\cdot f(t)$, a real function, continuous on $[a,b]$ and differentiable on $(a,b)$ with $g'(t)=v\cdot f'(t)$.

2. By @thm-mean-value, $g(b)-g(a)=(b-a)\,v\cdot f'(t)$ for some $t\in(a,b)$. The left side is $v\cdot v=\|v\|^2$.

3. By @thm-cauchy-schwarz-inner-product, $\|v\|^2\le(b-a)\|v\|\|f'(t)\|\le(b-a)M\|v\|$. Divide by $\|v\|$ if $v\ne0$.

:::

::: {#thm-mean-value-inequality .theorem name="Mean value inequality"}

Let $U\subseteq\mathbb R^n$ be open and $f:U\to\mathbb R^m$ differentiable. If the segment $\{x+t(y-x):0\le t\le1\}$ lies in $U$ and $\|Df\|\le M$ on it, then
$$\|f(y)-f(x)\|\le M\|y-x\|.$$
In particular, on a convex set (such as a ball) where $\|Df\|\le M$, $f$ is Lipschitz with constant $M$.

:::

::: {.proof}

1. Let $\gamma(t)=x+t(y-x)$ and $\varphi=f\circ\gamma:[0,1]\to\mathbb R^m$. By @thm-chain-rule-several-variables, $\varphi'(t)=Df(\gamma(t))(y-x)$.

2. So $\|\varphi'(t)\|\le\|Df(\gamma(t))\|\|y-x\|\le M\|y-x\|$, and @thm-mean-value-inequality-curves gives $\|\varphi(1)-\varphi(0)\|\le M\|y-x\|$.

:::

::: {#cor-zero-derivative-constant .corollary name="Zero derivative means constant"}

If $U\subseteq\mathbb R^n$ is open and connected and $f:U\to\mathbb R^m$ has $Df(x)=0$ for all $x\in U$, then $f$ is constant.

:::

::: {.proof}

1. If $U$ is empty there is nothing to show. Otherwise fix $x_0\in U$ and let $S=\{x\in U:f(x)=f(x_0)\}$, which contains $x_0$.

2. *Locally constant.* Every $x\in U$ has a ball $B_r(x)\subseteq U$; by @thm-mean-value-inequality with $M=0$, $f$ is constant on it.

3. So $S$ is open (a ball around a point of $S$ lies in $S$) and $U\setminus S$ is open (a ball around a point outside $S$ misses $S$). Since $U$ is connected (@def-connected), $S=U$.

:::

Connectedness is needed: on $U=\mathbb R\setminus\{0\}$ the function equal to $0$ for $x<0$ and $1$ for $x>0$ has zero derivative.

## Continuously differentiable maps

::: {#def-c1-map .definition name="$C^1$ map, diffeomorphism"}

$f:U\to\mathbb R^m$ is *continuously differentiable*, or $C^1$, on $U$ if it is differentiable on $U$ and $x\mapsto Df(x)$ is continuous from $U$ to $L(\mathbb R^n;\mathbb R^m)$ with the operator norm. A *diffeomorphism* between open sets $U,U'\subseteq\mathbb R^n$ is a $C^1$ bijection $U\to U'$ whose inverse is $C^1$.

:::

::: {#prp-c1-iff-continuous-partials .proposition name="$C^1$ means continuous partial derivatives"}

$f:U\to\mathbb R^m$ is $C^1$ if and only if all partial derivatives $D_jf_i$ exist and are continuous on $U$.

:::

::: {.proof}

1. If $f$ is $C^1$, the partial derivatives exist and are the entries of $Df$ (@prp-derivative-partials-jacobian); each entry is continuous because $|a_{ij}|\le\|A\|$ (@prp-operator-norm-properties, part 4).

2. Conversely, continuous partial derivatives make $f$ differentiable on $U$ (@thm-continuous-partials-differentiable), and $\|Df(x)-Df(y)\|\le\bigl(\sum_{i,j}(D_jf_i(x)-D_jf_i(y))^2\bigr)^{1/2}$ by part 4, which tends to $0$ as $y\to x$.

:::
