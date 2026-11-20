---
title: "Extreme and Intermediate Values"
sources: [cama1-4]
requires: [math/analysis/real/continuity/continuous-functions, math/analysis/real/sequences/monotone-sequences]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 4.1, in our own wording; proofs written out in steps. The extreme and intermediate value theorems are stated without proof in @sec-math-calculus-single-variable-limits-continuity; here they are proved from completeness. -->

Both theorems fail over $\mathbb Q$: $f(x)=x^2-2$ is continuous on $[0,2]\cap\mathbb Q$, negative at $0$ and positive at $2$, yet never $0$ there; and $1/(x^2-2)$ is continuous on $[0,2]\cap\mathbb Q$ but unbounded. So their proofs must use completeness, through Bolzano–Weierstrass or suprema.

::: {#thm-extreme-value-proof .theorem name="Extreme value theorem" related="thm-extreme-value"}

If $f:[a,b]\to\mathbb R$ is continuous, then $f$ is bounded and attains its bounds: there are $x,y\in[a,b]$ with
$$f(x)=\sup_{[a,b]}f,\qquad f(y)=\inf_{[a,b]}f.$$

:::

::: {.proof}

1. *Bounded above.* If not, for each $n$ pick $x_n\in[a,b]$ with $f(x_n)\ge n$. By @thm-bolzano-weierstrass a subsequence $x_{n_k}$ converges, to some $x$, and $x\in[a,b]$ because $a\le x_{n_k}\le b$ (@lem-limit-preserves-inequality).

2. By @thm-sequential-continuity, $f(x_{n_k})\to f(x)$, so $(f(x_{n_k}))$ is bounded (@lem-convergent-bounded). But $f(x_{n_k})\ge n_k\ge k$, a contradiction.

3. *Supremum attained.* Let $C=\sup f$, which exists by step 1. For each $n$ pick $x_n$ with $C-\frac1n<f(x_n)\le C$ (possible since $C-\frac1n$ is not an upper bound).

4. Again a subsequence $x_{n_k}\to x\in[a,b]$, and $f(x_{n_k})\to f(x)$. By the sandwich rule, $f(x_{n_k})\to C$ as well. Limits are unique (@thm-limit-unique), so $f(x)=C$.

5. For the infimum apply steps 1–4 to $-f$.

:::

Both hypotheses are needed: $f(x)=1/x$ is continuous on $(0,1]$ but unbounded; $f(x)=x$ on $[0,1)$ is bounded but never reaches $\sup f=1$.

::: {#thm-intermediate-value-proof .theorem name="Intermediate value theorem" related="thm-intermediate-value"}

If $f:[a,b]\to\mathbb R$ is continuous and $f(a)<c<f(b)$ (or $f(a)>c>f(b)$), then $f(x)=c$ for some $x\in(a,b)$.

:::

::: {.proof}

1. Replacing $f$ by $f-c$, and by $-f$ if needed, we may assume $f(a)<0<f(b)$ and must find a zero.

2. Let $A=\{x\in[a,b]:f(x)<0\}$. It contains $a$ and is bounded above by $b$, so $s=\sup A$ exists and $a\le s\le b$.

3. *$f(s)<0$ is impossible.* Then $s\ne b$, and continuity with $\varepsilon=-f(s)$ gives $\delta>0$ such that $f(y)<0$ for all $y\in[a,b]$ with $|y-s|<\delta$. Some point $y\in(s,s+\delta)\cap[a,b]$ then lies in $A$, contradicting that $s$ is an upper bound of $A$.

4. *$f(s)>0$ is impossible.* Then $s\ne a$, and continuity gives $\delta>0$ with $f(y)>0$ for all $y\in[a,b]$ with $|y-s|<\delta$. So no point of $(s-\delta,s]$ lies in $A$, and $s-\delta$ is a smaller upper bound of $A$, a contradiction.

5. Hence $f(s)=0$, and $s\ne a,b$ because $f(a)<0<f(b)$.

:::

::: {#rmk-extreme-and-intermediate-values-1 .remark name="A proof by bisection"}

The intermediate value theorem can also be proved like @thm-bolzano-weierstrass. Start with $[a_0,b_0]=[a,b]$ and keep the half of the current interval on which $f$ is negative at the left end and non-negative at the right end. By @thm-nested-intervals some $x$ lies in all the intervals, and $a_n,b_n\to x$ as their lengths halve. Then $f(a_n)<0$ gives $f(x)\le0$, and $f(b_n)\ge0$ gives $f(x)\ge0$. This is the bisection method for locating roots numerically (@exm-ivt-root).

:::

## Continuous inverses

::: {#thm-continuous-inverse .theorem name="Inverse of a continuous increasing function"}

Let $f:[a,b]\to[c,d]$ be continuous and strictly increasing with $f(a)=c$ and $f(b)=d$. Then $f$ is a bijection and its inverse $g:[c,d]\to[a,b]$ is continuous (and strictly increasing).

:::

::: {.proof}

1. *Injective.* If $x<y$, then $f(x)<f(y)$, so $f(x)\ne f(y)$.

2. *Surjective.* $c$ and $d$ are values; every $y\in(c,d)$ is a value by @thm-intermediate-value-proof. So $f$ has an inverse $g$, which is strictly increasing because $f$ is.

3. *Continuous.* Let $y\in[c,d]$, $x=g(y)$ and $\varepsilon>0$. Suppose first $a<x<b$, and shrink $\varepsilon$ so that $[x-\varepsilon,x+\varepsilon]\subseteq[a,b]$. Put $u=f(x-\varepsilon)$ and $v=f(x+\varepsilon)$; then $u<y<v$.

4. Let $\delta=\min(y-u,v-y)>0$. If $|z-y|<\delta$, then $u<z<v$, so $x-\varepsilon<g(z)<x+\varepsilon$ because $g$ is increasing; that is, $|g(z)-g(y)|<\varepsilon$.

5. At an endpoint, say $x=a$ (so $y=c$), use only $v=f(a+\varepsilon)$ and $\delta=v-c$; for $x=b$ use only $u$.

:::

For example $x\mapsto x^n$ is continuous and strictly increasing on $[0,R]$ for every $R$, so the $n$-th root $x\mapsto\sqrt[n]x$ is continuous on $[0,\infty)$.
