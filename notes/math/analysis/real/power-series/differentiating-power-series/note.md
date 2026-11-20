---
title: "Differentiating Power Series"
sources: [cama1-6]
requires: [math/analysis/real/power-series/radius-of-convergence, math/analysis/real/differentiability/differentiability-and-inverses]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 6.2, in our own wording; proofs written out in steps. -->

A polynomial is differentiated term by term. Inside its disc of convergence a power series can be too, but this needs proof: the sum rule covers finite sums only. The proof below bounds the error directly; with uniform convergence (in a later course) it becomes shorter.

::: {#lem-power-difference .lemma name="An algebraic identity"}

For $a,b\in\mathbb C$ and $n\ge2$,
$$b^n-a^n-n(b-a)a^{n-1}=(b-a)^2\sum_{k=1}^{n-1}k\,a^{k-1}b^{n-1-k}.$$

:::

::: {.proof}

1. $b^n-a^n=(b-a)\sum_{j=0}^{n-1}a^jb^{n-1-j}$, so the left side is $(b-a)\sum_{j=0}^{n-1}a^j\bigl(b^{n-1-j}-a^{n-1-j}\bigr)$.

2. Apply the same factorisation to each bracket: $b^{m}-a^{m}=(b-a)\sum_{i=0}^{m-1}a^ib^{m-1-i}$ with $m=n-1-j$.

3. The left side becomes $(b-a)^2\sum_{j}\sum_{i}a^{i+j}b^{n-2-i-j}$. For fixed $k-1=i+j$ (from $0$ to $n-2$) there are $k$ pairs $(i,j)$, which gives the right side.

:::

With $a=z$, $b=z+h$ this reads
$$(z+h)^n-z^n-nhz^{n-1}=h^2\sum_{k=1}^{n-1}k\,z^{k-1}(z+h)^{n-1-k}.\tag{1}$$

::: {#lem-derived-series-converges .lemma name="The derived series has the same disc"}

If $\sum a_nz^n$ has radius of convergence $R$ and $|z|<R$, then $\sum na_nz^{n-1}$ and $\sum\binom n2a_nz^{n-2}$ converge absolutely.

:::

::: {.proof}

1. Choose $r$ with $|z|<r<R$. Then $\sum|a_n|r^n$ converges (@thm-radius-of-convergence), so $|a_n|r^n\le C$ for all $n$.

2. Hence $n|a_nz^{n-1}|\le\frac Cr\,n\left(\frac{|z|}r\right)^{n-1}$, and $\sum n\rho^{n-1}$ converges for $0\le\rho<1$ by the ratio test (@exm-convergence-tests-1). Comparison gives the first claim.

3. Apply step 2 to the series $\sum na_nz^{n-1}$ itself, whose radius is at least $R$ by step 2: $\sum n(n-1)a_nz^{n-2}$ converges absolutely; divide by $2$.

:::

::: {#thm-power-series-differentiable .theorem name="Term-by-term differentiation"}

Let $\sum a_nz^n$ have radius of convergence $R$. On $|z|<R$ the function $f(z)=\sum_{n\ge0}a_nz^n$ is differentiable, and
$$f'(z)=\sum_{n=1}^\infty na_nz^{n-1}.$$

:::

::: {.proof}

1. Let $g(z)$ be the right side, which converges by @lem-derived-series-converges. By @prp-derivative-little-o we must show $f(z+h)-f(z)-hg(z)=o(h)$.

2. For $|z+h|<R$, the three series converge, and the terms with $n=0,1$ cancel, so by (1)
$$f(z+h)-f(z)-hg(z)=\sum_{n\ge2}a_n\bigl((z+h)^n-z^n-nhz^{n-1}\bigr)=h^2\sum_{n\ge2}a_n\sum_{k=1}^{n-1}k\,z^{k-1}(z+h)^{n-1-k}.$$

3. Fix $r$ with $|z|<r<R$ and take $h$ so small that $|z+h|\le r$. Each inner sum then has modulus at most $\sum_{k=1}^{n-1}k\,r^{n-2}=\binom n2r^{n-2}$.

4. So the modulus of the outer sum is at most $M=\sum_{n\ge2}|a_n|\binom n2r^{n-2}$, which is finite by @lem-derived-series-converges (applied at $r<R$) and does not depend on $h$.

5. Hence $|f(z+h)-f(z)-hg(z)|\le M|h|^2$, which is $o(h)$.

:::

Applying the theorem repeatedly, a power series is infinitely differentiable inside its disc of convergence, and $a_n=f^{(n)}(0)/n!$; this justifies @thm-taylor-coefficients.
