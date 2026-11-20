---
title: "The Exponential and Trigonometric Functions"
sources: [cama1-6]
requires: [math/analysis/real/power-series/differentiating-power-series]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Sections 6.1–6.3, in our own wording; proofs written out in steps. Earlier notes use $e^x$, $\sin$ and $\cos$ with their familiar properties; here they are defined by power series and those properties are proved, including the definition of $\pi$. -->

## Products of series

::: {#thm-cauchy-product .theorem name="Cauchy product"}

Let $\sum_{n\ge0}a_n$ and $\sum_{n\ge0}b_n$ converge absolutely, and let $c_n=\sum_{k=0}^na_kb_{n-k}$. Then $\sum c_n$ converges absolutely and
$$\sum_{n=0}^\infty c_n=\Bigl(\sum_{n=0}^\infty a_n\Bigr)\Bigl(\sum_{n=0}^\infty b_n\Bigr).$$

:::

::: {.proof}

1. Let $S,T$ be the two sums and $U=\sum|a_n|$, $V=\sum|b_n|$. Consider the series $(*)$ whose terms are all the products $a_jb_k$, listed in "square shells": first $a_0b_0$, then the products with $\max(j,k)=1$, then those with $\max(j,k)=2$, and so on.

2. The first $(N+1)^2$ terms of $(*)$ are exactly the products with $j,k\le N$. So their moduli add up to $\bigl(\sum_{n\le N}|a_n|\bigr)\bigl(\sum_{n\le N}|b_n|\bigr)\le UV$. Every partial sum of the moduli is below such a square partial sum, so $(*)$ converges absolutely.

3. The same partial sums of $(*)$ itself are $\bigl(\sum_{n\le N}a_n\bigr)\bigl(\sum_{n\le N}b_n\bigr)\to ST$. A convergent series has the limit of any subsequence of its partial sums, so $(*)$ sums to $ST$.

4. Listing the same products in "diagonals" $j+k=0,1,2,\dots$ is a rearrangement of $(*)$, so by @thm-absolute-iff-unconditional it converges absolutely to $ST$ as well. Its partial sum through the diagonal $j+k=N$ is $c_0+\cdots+c_N$; hence $\sum c_n=ST$, and $\sum|c_n|$ converges because $|c_n|\le\sum_{j+k=n}|a_jb_k|$.

:::

Applied to $a_nz^n$ and $b_nz^n$: inside both discs of convergence, $\bigl(\sum a_nz^n\bigr)\bigl(\sum b_nz^n\bigr)=\sum c_nz^n$, as when multiplying polynomials.

## The exponential function

::: {#def-exponential-series .definition name="Exponential function" related="def-number-e"}

For $z\in\mathbb C$,
$$e^z=\exp(z)=\sum_{n=0}^\infty\frac{z^n}{n!}.$$

:::

The ratio of consecutive terms is $\frac{|z|}{n+1}\to0$, so the series converges absolutely for every $z$ (radius $\infty$).

::: {#thm-exponential-properties .theorem name="Properties of the exponential"}

For all $z,w\in\mathbb C$:

1. $e^{z+w}=e^ze^w$; in particular $e^z\ne0$ and $e^{-z}=1/e^z$;
2. $\exp$ is differentiable with $\dfrac{d}{dz}e^z=e^z$.

:::

::: {.proof}

1. By @thm-cauchy-product, $e^ze^w=\sum_nc_n$ with
$$c_n=\sum_{k=0}^n\frac{z^k}{k!}\frac{w^{n-k}}{(n-k)!}=\frac1{n!}\sum_{k=0}^n\binom nkz^kw^{n-k}=\frac{(z+w)^n}{n!}$$
by the binomial theorem (@thm-binomial-theorem). So $e^ze^w=e^{z+w}$. Taking $w=-z$ gives $e^ze^{-z}=e^0=1$.

2. Differentiating term by term (@thm-power-series-differentiable), $\sum_{n\ge1}\frac{nz^{n-1}}{n!}=\sum_{m\ge0}\frac{z^m}{m!}=e^z$.

:::

By @exm-taylors-theorem-1, $e^x$ is the only differentiable $f:\mathbb R\to\mathbb R$ with $f'=f$ and $f(0)=1$. For real $x$, $e^x>0$: for $x\ge0$ every term is non-negative and the first is $1$, and $e^{-x}=1/e^x$.

## Sine and cosine

::: {#def-sine-cosine-series .definition name="Sine and cosine"}

For $z\in\mathbb C$,
$$\cos z=\frac{e^{iz}+e^{-iz}}2=\sum_{n=0}^\infty\frac{(-1)^nz^{2n}}{(2n)!},\qquad \sin z=\frac{e^{iz}-e^{-iz}}{2i}=\sum_{n=0}^\infty\frac{(-1)^nz^{2n+1}}{(2n+1)!}.$$

:::

The series follow from $e^{\pm iz}$: the powers $i^n$ make the odd terms cancel in the first combination and the even terms in the second. By definition $e^{iz}=\cos z+i\sin z$. For real $x$ the series have real coefficients, so $\cos x$ and $\sin x$ are real.

::: {#prp-sine-cosine-identities .proposition name="Basic identities"}

For all $z,w\in\mathbb C$:
$$\frac{d}{dz}\sin z=\cos z,\qquad\frac d{dz}\cos z=-\sin z,\qquad\sin^2z+\cos^2z=1,$$
$$\cos(z+w)=\cos z\cos w-\sin z\sin w,\qquad\sin(z+w)=\sin z\cos w+\cos z\sin w.$$
In particular $|\sin x|\le1$ and $|\cos x|\le1$ for real $x$.

:::

::: {.proof}

1. *Derivatives.* By the chain rule and $(e^z)'=e^z$, $(\sin z)'=\frac{ie^{iz}+ie^{-iz}}{2i}=\cos z$ and $(\cos z)'=\frac{ie^{iz}-ie^{-iz}}{2}=-\sin z$.

2. *Pythagoras.* $\cos^2z=\frac{e^{2iz}+2+e^{-2iz}}4$ and $\sin^2z=-\frac{e^{2iz}-2+e^{-2iz}}4$; they add up to $1$. For real $x$ both squares are non-negative, so each is at most $1$.

3. *Addition formula for $\cos$.* Expand
$$\cos z\cos w-\sin z\sin w=\frac{(e^{iz}+e^{-iz})(e^{iw}+e^{-iw})+(e^{iz}-e^{-iz})(e^{iw}-e^{-iw})}4.$$
The mixed terms $e^{i(z-w)}$ and $e^{-i(z-w)}$ cancel, leaving $\frac{2e^{i(z+w)}+2e^{-i(z+w)}}4=\cos(z+w)$.

4. *Addition formula for $\sin$.* Differentiate the identity of step 3 with respect to $z$, keeping $w$ fixed: $-\sin z\cos w-\cos z\sin w=-\sin(z+w)$.

:::

## The number $\pi$

::: {#lem-sine-cosine-bounds .lemma name="Polynomial bounds"}

For real $x\ge0$:
$$\sin x\le x,\qquad\cos x\ge1-\frac{x^2}2,\qquad\sin x\ge x-\frac{x^3}6,\qquad\cos x\le1-\frac{x^2}2+\frac{x^4}{24}.$$

:::

::: {.proof}

Each difference $D$ below vanishes at $0$ and has $D'\ge0$ on $[0,\infty)$, so $D\ge0$ there by @cor-sign-of-derivative.

1. $D_1=x-\sin x$: $D_1'=1-\cos x\ge0$ since $\cos x\le1$.

2. $D_2=\cos x-1+\frac{x^2}2$: $D_2'=x-\sin x=D_1\ge0$.

3. $D_3=\sin x-x+\frac{x^3}6$: $D_3'=\cos x-1+\frac{x^2}2=D_2\ge0$.

4. $D_4=1-\frac{x^2}2+\frac{x^4}{24}-\cos x$: $D_4'=-x+\frac{x^3}6+\sin x=D_3\ge0$.

:::

The same argument continues: truncating the series of $\sin x$ or $\cos x$ ($x\ge0$) after a positive term gives an upper bound, after a negative term a lower bound.

::: {#def-pi .definition name="The number $\pi$"}

$\pi/2$ is the smallest positive zero of $\cos$ on $\mathbb R$.

:::

This makes sense. By @lem-sine-cosine-bounds, $\cos x\ge1-\frac{x^2}2>0$ on $[0,1]$, and $\cos2\le1-2+\frac{16}{24}=-\frac13<0$. By the intermediate value theorem (@thm-intermediate-value-proof) $\cos$ has a zero in $(1,2)$. The set of zeros in $[1,2]$ is non-empty; its infimum $c$ is again a zero, since by continuity $\cos c$ is the limit of $\cos$ at zeros approaching $c$. So $1<\pi/2<2$.

::: {#prp-sine-cosine-periodic .proposition name="Shifts and periodicity"}

$\sin\frac\pi2=1$, and for all $z\in\mathbb C$
$$\cos\Bigl(z+\frac\pi2\Bigr)=-\sin z,\quad\sin\Bigl(z+\frac\pi2\Bigr)=\cos z,\quad\cos(z+\pi)=-\cos z,\quad\sin(z+\pi)=-\sin z,$$
so $\sin$ and $\cos$ have period $2\pi$, and $e^{z+2\pi i}=e^z$.

:::

::: {.proof}

1. On $[0,\frac\pi2)$, $\cos>0$, so $\sin$ is strictly increasing there (@cor-sign-of-derivative) and $\sin\frac\pi2>\sin0=0$. Since $\sin^2\frac\pi2=1-\cos^2\frac\pi2=1$, we get $\sin\frac\pi2=1$.

2. By the addition formulas with $w=\frac\pi2$: $\cos(z+\frac\pi2)=\cos z\cdot0-\sin z\cdot1=-\sin z$ and $\sin(z+\frac\pi2)=\sin z\cdot0+\cos z\cdot1=\cos z$.

3. Applying step 2 twice gives the shifts by $\pi$, and applying those twice gives period $2\pi$.

4. $e^{2\pi i}=\cos2\pi+i\sin2\pi=1$, so $e^{z+2\pi i}=e^ze^{2\pi i}=e^z$.

:::

## Hyperbolic functions

The *hyperbolic cosine and sine* (@def-hyperbolic-functions) are
$$\cosh z=\frac{e^z+e^{-z}}2=\sum_{n\ge0}\frac{z^{2n}}{(2n)!},\qquad\sinh z=\frac{e^z-e^{-z}}2=\sum_{n\ge0}\frac{z^{2n+1}}{(2n+1)!}.$$
The same calculations as above (compare @prp-hyperbolic-identities) give $(\cosh z)'=\sinh z$, $(\sinh z)'=\cosh z$ and $\cosh^2z-\sinh^2z=1$, and comparing definitions, $\cosh(iz)=\cos z$ and $\sinh(iz)=i\sin z$. Over $\mathbb C$, trigonometric and hyperbolic functions are the same functions rotated by $i$.
