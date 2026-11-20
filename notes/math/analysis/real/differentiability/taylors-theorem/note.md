---
title: "Local Inverses and Taylor's Theorem"
sources: [cama1-5, mit1801-37]
requires: [math/analysis/real/differentiability/differentiability-and-inverses, math/calculus/single-variable/applications-of-derivatives/mean-value-theorem]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 5.3, in our own wording; proofs written out in steps. Rolle's theorem, the mean value theorem and its consequences are already proved in @sec-math-calculus-single-variable-applications-of-derivatives-mean-value-theorem; Merged 2026-11-20 (owner): Taylor's formula with remainder from MIT 18.01 Lecture 37 (former id thm-taylor-remainder, no proof) was removed; @thm-taylor-lagrange is the single version, with the 18.01 $R_n$ notation added after it. -->

The mean value theorem (@thm-mean-value) is the bridge from information about $f'$ to information about $f$: for instance $f'>0$ on an interval makes $f$ strictly increasing (@cor-sign-of-derivative). This note uses it twice more: to invert functions locally, and, through a higher-order Rolle's theorem, to prove Taylor's theorem.

## Local inverses

::: {#thm-local-inverse-function .theorem name="Inverse function theorem in one variable"}

Let $f$ have a continuous derivative on $(a,b)$, and let $x\in(a,b)$ with $f'(x)\ne0$. Then there is an open interval $I\ni x$ such that $f$ restricted to $I$ is injective, and its inverse $g:f(I)\to I$ is differentiable with
$$g'(f(z))=\frac1{f'(z)}\quad\text{for all }z\in I.$$

:::

::: {.proof}

1. Say $f'(x)>0$ (otherwise use $-f$). Since $f'$ is continuous, there is $\delta>0$ with $f'>0$ on $(x-\delta,x+\delta)$.

2. By @cor-sign-of-derivative, $f$ is strictly increasing on $(x-\delta,x+\delta)$; it is continuous there by @thm-differentiable-continuous.

3. Let $I=(x-\delta/2,x+\delta/2)$. On the closed interval $[x-\delta/2,x+\delta/2]$, $f$ is continuous, strictly increasing and has non-zero derivative inside, so @thm-inverse-differentiable gives the inverse and its derivative at every point of $f(I)$.

:::

Continuity of $f'$ is needed. The function $f(x)=x+2x^2\sin(1/x)$, $f(0)=0$, has $f'(0)=1$, but $f'$ takes negative values in every interval around $0$, so $f$ is not injective near $0$.

## Taylor's theorem

::: {#thm-higher-order-rolle .theorem name="Higher-order Rolle's theorem"}

Let $f$ be $n$ times differentiable on an open interval containing $[a,b]$, with
$$f(a)=f'(a)=\cdots=f^{(n-1)}(a)=0\quad\text{and}\quad f(b)=0.$$
Then $f^{(n)}(x)=0$ for some $x\in(a,b)$.

:::

::: {.proof}

1. Let $x_0=b$. We find $b=x_0>x_1>\cdots>x_n>a$ with $f^{(k)}(x_k)=0$ for each $k$.

2. Given $x_k$ with $k<n$: $f^{(k)}(a)=0=f^{(k)}(x_k)$, and $f^{(k)}$ is differentiable (hence continuous) on $[a,x_k]$. Rolle's theorem (@thm-rolle) gives $x_{k+1}\in(a,x_k)$ with $f^{(k+1)}(x_{k+1})=0$.

3. After $n$ steps, $x=x_n$ works.

:::

The polynomial $Q_k(x)=\frac{(x-a)^k}{k!}$ satisfies $Q_k^{(j)}(a)=1$ if $j=k$ and $0$ if $j\ne k$. Hence
$$P(x)=\sum_{k=0}^{n-1}f^{(k)}(a)\frac{(x-a)^k}{k!}$$
has the same first $n-1$ derivatives at $a$ as $f$, and the same value. It is the *Taylor polynomial* of degree $n-1$ of $f$ at $a$.

::: {#thm-taylor-lagrange .theorem name="Taylor's theorem with Lagrange remainder"}

Let $f$ be $n$ times differentiable on an open interval containing $a$ and $a+h$ ($h\ne0$). Then
$$f(a+h)=\sum_{k=0}^{n-1}\frac{f^{(k)}(a)}{k!}h^k+\frac{f^{(n)}(x)}{n!}h^n$$
for some $x$ strictly between $a$ and $a+h$.

:::

::: {.proof}

1. Take $h>0$ and write $b=a+h$. With $P$ the Taylor polynomial above, define
$$p(t)=P(t)+\frac{(t-a)^n}{(b-a)^n}\bigl(f(b)-P(b)\bigr).$$
The added term has derivatives of order $<n$ equal to $0$ at $a$, so $p^{(k)}(a)=f^{(k)}(a)$ for $k<n$, and $p(b)=f(b)$.

2. Apply @thm-higher-order-rolle to $f-p$: there is $x\in(a,b)$ with $f^{(n)}(x)=p^{(n)}(x)$.

3. $P$ has degree $n-1$, so $p^{(n)}$ is the constant $\frac{n!}{(b-a)^n}\bigl(f(b)-P(b)\bigr)$. Hence $f(b)=P(b)+\frac{(b-a)^n}{n!}f^{(n)}(x)$, which is the claim.

4. For $h<0$, apply steps 1–3 to $t\mapsto f(-t)$ at the point $-a$, whose $k$-th derivative is $(-1)^kf^{(k)}(-t)$.

:::

With $n+1$ in place of $n$ and $x=a+h$, this is the form used in single-variable calculus: $f(x)=\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x)$ with $R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ for some $c$ between $a$ and $x$.

If $|f^{(n)}|\le C$ near $a$, the remainder is at most $\frac{C}{n!}|h|^n$, which is $o(h^{n-1})$: the Taylor polynomial is then the best polynomial approximation of degree $n-1$ near $a$. Whether the full Taylor series converges to $f$ depends on how the remainder behaves as $n\to\infty$.

::: {#exm-taylors-theorem-1 .example name="A function equal to its derivative"}

Suppose $f:\mathbb R\to\mathbb R$ is differentiable with $f'=f$ and $f(0)=1$. Then for every $x$,
$$f(x)=\sum_{k=0}^\infty\frac{x^k}{k!}.$$
We cannot simply differentiate the series term by term: the sum rule covers finite sums only. Instead:

1. $f'=f$ is differentiable, so $f''=f'=f$, and inductively $f^{(n)}=f$ exists for all $n$, with $f^{(n)}(0)=1$.

2. By @thm-taylor-lagrange, $f(x)=\sum_{k=0}^{n-1}\frac{x^k}{k!}+\frac{f(u_n)}{n!}x^n$ for some $u_n$ between $0$ and $x$.

3. $f$ is continuous, hence bounded on the closed interval between $0$ and $x$, say by $C$ (@thm-extreme-value-proof). So the remainder is at most $\frac{C|x|^n}{n!}$.

4. $\frac{|x|^n}{n!}\to0$ for fixed $x$: once $n\ge2|x|$ each further factor $\frac{|x|}{n}$ is at most $\frac12$. So the partial sums converge to $f(x)$.

Whether such an $f$ exists is a separate question, answered in @sec-math-analysis-real-power-series-exponential-and-trigonometric-functions.

:::
