---
title: "Which Functions Are Integrable"
sources: [cama1-7]
requires: [math/analysis/real/integration/properties-of-the-integral, math/analysis/real/continuity/extreme-and-intermediate-values]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 7.1, in our own wording; proofs written out in steps. Uniform continuity is a starred (non-examinable) part of the source; it is kept as its own block because later courses use it constantly. -->

Riemann's criterion (@thm-riemann-criterion) reduces integrability to making $U_D(f)-L_D(f)$ small. This works for continuous functions, monotone functions, and functions that are badly behaved only at a few points.

## Continuous functions

::: {#def-uniform-continuity .definition name="Uniform continuity"}

$f:A\to\mathbb R$ is *uniformly continuous* if
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x,y\in A\quad |x-y|<\delta\Rightarrow|f(x)-f(y)|<\varepsilon.$$

:::

The difference from continuity (@def-continuity-epsilon-delta) is the order of quantifiers: here one $\delta$ must serve every point at once. $f(x)=1/x$ is continuous on $(0,1]$ but not uniformly continuous: near $0$, points within any fixed $\delta$ of each other can have values arbitrarily far apart.

::: {#thm-uniform-continuity-compact .theorem name="Continuous on a closed interval implies uniformly continuous"}

Every continuous $f:[a,b]\to\mathbb R$ is uniformly continuous.

:::

::: {.proof}

1. Suppose not. Then there is $\varepsilon>0$ such that for every $n$ there are $x_n,y_n\in[a,b]$ with $|x_n-y_n|<\frac1n$ and $|f(x_n)-f(y_n)|\ge\varepsilon$.

2. By @thm-bolzano-weierstrass some subsequence $x_{n_k}\to x$, and $x\in[a,b]$. Since $|x_{n_k}-y_{n_k}|<\frac1{n_k}$, also $y_{n_k}\to x$.

3. By continuity at $x$ (@thm-sequential-continuity), $f(x_{n_k})\to f(x)$ and $f(y_{n_k})\to f(x)$, so $f(x_{n_k})-f(y_{n_k})\to0$, contradicting $|f(x_{n_k})-f(y_{n_k})|\ge\varepsilon$.

:::

::: {#thm-continuous-integrable .theorem name="Continuous functions are integrable"}

Every continuous $f:[a,b]\to\mathbb R$ is Riemann integrable.

:::

::: {.proof}

1. Let $\varepsilon>0$. By @thm-uniform-continuity-compact there is $\delta>0$ with $|f(x)-f(y)|<\frac{\varepsilon}{b-a}$ whenever $|x-y|<\delta$.

2. Take a dissection $D$ of mesh less than $\delta$. On each subinterval $f$ attains its supremum and infimum (@thm-extreme-value-proof) at points less than $\delta$ apart, so $M_i-m_i<\frac\varepsilon{b-a}$.

3. Hence $U_D(f)-L_D(f)=\sum(x_i-x_{i-1})(M_i-m_i)<\frac{\varepsilon}{b-a}(b-a)=\varepsilon$, and @thm-riemann-criterion applies.

:::

So $\int_a^be^{-x^2}dx$ exists, although $e^{-x^2}$ has no elementary antiderivative.

## Monotone functions

::: {#thm-monotone-integrable .theorem name="Monotone functions are integrable"}

Every monotone $f:[a,b]\to\mathbb R$ is Riemann integrable.

:::

::: {.proof}

1. Say $f$ is increasing and $f(b)>f(a)$ (if $f(b)=f(a)$, $f$ is constant). Let $\varepsilon>0$ and take a dissection of mesh less than $\delta=\frac{\varepsilon}{f(b)-f(a)}$.

2. On $[x_{i-1},x_i]$, $M_i=f(x_i)$ and $m_i=f(x_{i-1})$. So
$$U_D(f)-L_D(f)=\sum_{i=1}^n(x_i-x_{i-1})\bigl(f(x_i)-f(x_{i-1})\bigr)<\delta\sum_{i=1}^n\bigl(f(x_i)-f(x_{i-1})\bigr)=\delta\bigl(f(b)-f(a)\bigr)=\varepsilon.$$

:::

A monotone function can have infinitely many jumps. For example, $f(0)=0$ and $f(x)=\frac1k$ on $\left(\frac1{2^{k}},\frac1{2^{k-1}}\right]$ is increasing on $[0,1]$ with a jump at every $\frac1{2^k}$, and is integrable by the theorem.

## Isolated bad points

::: {#thm-bounded-continuous-interior-integrable .theorem name="Bounded and continuous inside"}

If $f:[a,b]\to\mathbb R$ is bounded and continuous on $(a,b)$, then $f$ is integrable on $[a,b]$.

:::

::: {.proof}

1. Let $|f|\le C$ and $\varepsilon>0$. Choose $a<x_1<z<b$ with $x_1-a<\frac{\varepsilon}{8C}$ and $b-z<\frac\varepsilon{8C}$.

2. $f$ is continuous on $[x_1,z]$, hence integrable there (@thm-continuous-integrable), so some dissection $x_1<x_2<\cdots<x_{n-1}=z$ of $[x_1,z]$ has upper and lower sums differing by less than $\frac\varepsilon2$.

3. Add the points $a$ and $b$. The two end pieces each contribute at most $\frac{\varepsilon}{8C}\cdot2C=\frac\varepsilon4$ to $U-L$, since $M_i-m_i\le2C$. So $U_D(f)-L_D(f)<\frac\varepsilon4+\frac\varepsilon2+\frac\varepsilon4=\varepsilon$.

:::

::: {#cor-piecewise-continuous-integrable .corollary name="Piecewise continuous functions"}

A bounded function on $[a,b]$ that is continuous except at finitely many points is integrable.

:::

::: {.proof}

1. Split $[a,b]$ at the points of discontinuity into finitely many closed intervals, on whose interiors $f$ is continuous.

2. On each, $f$ is integrable by @thm-bounded-continuous-interior-integrable, so on $[a,b]$ by @thm-integral-additive.

:::

::: {#exm-integrable-functions-1 .example}

$f(x)=\sin(1/x)$ for $x\ne0$, $f(0)=0$, is integrable on $[-1,1]$: it is bounded by $1$ and discontinuous only at $0$, although it oscillates infinitely often near $0$. So is $g$ on $[0,2]$ with $g(x)=x$ for $x\le1$ and $g(x)=x^2+1$ for $x>1$, which jumps at $1$.

:::
