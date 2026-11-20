---
title: "The Inverse Function Theorem"
sources: [camib-at-a6]
requires: [math/analysis/differentiation/chain-rule-and-mean-value, math/analysis/metric-spaces/contraction-mapping]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 6.4, in our own wording; the proof via the contraction mapping theorem is written out in steps with our own constants; examples ours. -->

A linear map is invertible when its matrix is. The inverse function theorem says the same holds locally for a $C^1$ map: if its derivative at a point is invertible, the map is invertible near that point, and the inverse is again $C^1$. It generalizes @thm-local-inverse-function.

::: {#lem-perturbation-of-identity .lemma name="Small perturbations of the identity are invertible"}

If $B\in L(\mathbb R^n;\mathbb R^n)$ and $\|I-B\|<1$ in the operator norm, then $B$ is invertible.

:::

::: {.proof}

1. If $Bx=0$, then $\|x\|=\|(I-B)x\|\le\|I-B\|\|x\|$, which forces $x=0$.

2. So $B$ is injective, hence invertible, since $\mathbb R^n$ is finite-dimensional.

:::

::: {#thm-inverse-function .theorem name="Inverse function theorem" generalizes="thm-local-inverse-function"}

Let $U\subseteq\mathbb R^n$ be open, $f:U\to\mathbb R^n$ a $C^1$ map (@def-c1-map), and $a\in U$ with $Df(a)$ invertible. Then there are open sets $V\subseteq U$ containing $a$ and $W\subseteq\mathbb R^n$ containing $f(a)$ such that $f|_V:V\to W$ is a bijection whose inverse $g:W\to V$ is $C^1$, with
$$Dg(y)=\bigl(Df(g(y))\bigr)^{-1}\qquad(y\in W).$$
That is, $f|_V$ is a diffeomorphism.

:::

::: {.proof}

1. *Reduction.* Let $A=Df(a)$ and $\tilde f(x)=A^{-1}\bigl(f(a+x)-f(a)\bigr)$, defined on the open set $U-a$. By the chain rule (@thm-chain-rule-several-variables) $\tilde f$ is $C^1$ with $\tilde f(0)=0$ and $D\tilde f(0)=I$. If the theorem holds for $\tilde f$ at $0$, it holds for $f$ at $a$, since $f(x)=f(a)+A\tilde f(x-a)$ is $\tilde f$ composed with invertible affine maps. So assume $a=0$, $f(0)=0$ and $Df(0)=I$.

2. *A ball where $Df$ is close to $I$.* Since $Df$ is continuous, choose $r>0$ with $\overline B_r(0)\subseteq U$ and $\|Df(x)-I\|\le\frac12$ for $\|x\|\le r$. By @lem-perturbation-of-identity, $Df(x)$ is invertible for these $x$.

3. *$f$ is injective on $\overline B_r(0)$.* Let $\varphi(x)=x-f(x)$; then $\|D\varphi(x)\|=\|I-Df(x)\|\le\frac12$ on the convex set $\overline B_r(0)$, so by @thm-mean-value-inequality $\|\varphi(x)-\varphi(x')\|\le\frac12\|x-x'\|$. Hence
$$\|f(x)-f(x')\|\ge\|x-x'\|-\|\varphi(x)-\varphi(x')\|\ge\tfrac12\|x-x'\|.\qquad(1)$$

4. *Solving $f(x)=y$ for small $y$.* Let $W=B_{r/2}(0)$ and $y\in W$. Define $T(x)=x-f(x)+y=\varphi(x)+y$ on the closed ball $\overline B_r(0)$, which is complete (@thm-closed-subspace-complete). Since $\varphi(0)=0$, $\|T(x)\|\le\|\varphi(x)\|+\|y\|\le\frac r2+\frac r2=r$, so $T$ maps the ball into itself, and it is a contraction with constant $\frac12$. By @thm-contraction-mapping it has a unique fixed point $x$, that is, $f(x)=y$. Moreover $\|x\|=\|T(x)\|\le\frac12\|x\|+\|y\|$ gives $\|x\|\le2\|y\|<r$.

5. *The sets $V$ and $W$.* Let $V=B_r(0)\cap f^{-1}(W)$, open because $f$ is continuous, and containing $0$. By step 4 every $y\in W$ is $f(x)$ for some $x\in V$, and by step 3 this $x$ is unique. So $f|_V:V\to W$ is a bijection; let $g$ be its inverse.

6. *$g$ is Lipschitz.* By (1), $\|g(y)-g(y')\|\le2\|y-y'\|$.

7. *$g$ is differentiable.* Fix $y\in W$, $x=g(y)$ and $B=Df(x)$, invertible by step 2. For small $k$, let $h=g(y+k)-x$, so $f(x+h)=y+k$ and $\|h\|\le2\|k\|$ by step 6. Differentiability of $f$ at $x$ gives $k=Bh+\varepsilon(h)\|h\|$ with $\varepsilon(h)\to0$ as $h\to0$. Applying $B^{-1}$,
$$\|g(y+k)-g(y)-B^{-1}k\|=\|h-B^{-1}k\|=\|B^{-1}\varepsilon(h)\|\|h\|\le2\|B^{-1}\|\,\|\varepsilon(h)\|\,\|k\|.$$
As $k\to0$, $h\to0$ by step 6, so $\varepsilon(h)\to0$. Hence $Dg(y)=B^{-1}=Df(g(y))^{-1}$.

8. *$g$ is $C^1$.* $y\mapsto Dg(y)$ is the composite of $g$ (continuous), $Df$ (continuous) and matrix inversion on invertible matrices, which is continuous because by Cramer's rule the entries of $M^{-1}$ are polynomials in the entries of $M$ divided by $\det M\ne0$. With @prp-operator-norm-properties (part 4), $Dg$ is continuous.

:::

The proof finds $g(y)$ by fixed-point iteration $x\mapsto x-A^{-1}(f(x)-y)$, a simplified Newton's method that keeps the derivative fixed at $a$.

::: {#exm-polar-coordinates-local-inverse .example name="Polar coordinates"}

Let $f(r,\theta)=(r\cos\theta,r\sin\theta)$ on $U=\{r>0\}$. Then $\det Df(r,\theta)=\det\begin{pmatrix}\cos\theta&-r\sin\theta\\\sin\theta&r\cos\theta\end{pmatrix}=r\ne0$, so $f$ is a local diffeomorphism near every point. It is not injective on $U$, since $f(r,\theta+2\pi)=f(r,\theta)$: the theorem is local. On $V=\{r>0,\ -\pi<\theta<\pi\}$ it is a diffeomorphism onto the plane minus the closed negative $x$-axis.

:::

::: {#rmk-inverse-function-hypotheses .remark name="The hypotheses"}

1. *Invertibility of $Df(a)$ is needed for a differentiable inverse.* $f(x)=x^3$ is a bijection of $\mathbb R$, but $f'(0)=0$ and its inverse $\sqrt[3]{y}$ is not differentiable at $0$; indeed if $g\circ f=\mathrm{id}$ with $g$ differentiable, the chain rule forces $Dg(f(a))Df(a)=I$.
2. *Continuity of $Df$ is needed.* $f(x)=x+2x^2\sin\frac1x$ ($f(0)=0$) has $f'(0)=1$, but $f'$ takes negative values arbitrarily close to $0$, so $f$ is not injective on any interval around $0$.

:::
