---
title: "Series of Functions and the Weierstrass M-test"
sources: [camib-at-a2]
requires: [math/analysis/real/uniform-convergence/limits-integrals-derivatives, math/analysis/real/power-series/differentiating-power-series]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 2, in our own wording; examples ours; proofs written out in steps. Term-by-term differentiation of power series is already proved in math/analysis/real/power-series/differentiating-power-series and is only cited. -->

A series of functions $\sum g_n$ is a sequence of partial sums $f_n=\sum_{k=1}^ng_k$, so the results on uniform convergence apply to it. All definitions and results of @sec-math-analysis-real-uniform-convergence-uniform-convergence hold verbatim for complex-valued functions, with $|\cdot|$ the modulus, because $\mathbb C$ is complete too.

::: {#def-uniform-convergence-series .definition name="Convergence of a series of functions"}

Let $g_n:E\to\mathbb R$ (or $\mathbb C$) and $f_n=\sum_{k=1}^ng_k$. The series $\sum g_n$

1. *converges pointwise*, *uniformly*, or is *uniformly Cauchy* on $E$ if $(f_n)$ has that property;
2. *converges absolutely* on $E$ if $\sum|g_n(x)|$ converges for every $x\in E$;
3. *converges absolutely uniformly* on $E$ if $\sum|g_n|$ converges uniformly on $E$.

:::

::: {#thm-weierstrass-m-test .theorem name="Weierstrass M-test"}

Let $g_n:E\to\mathbb R$ (or $\mathbb C$) and suppose there are constants $M_n\ge0$ with
$$|g_n(x)|\le M_n\quad\text{for all }x\in E,\qquad\sum_{n=1}^\infty M_n<\infty.$$
Then $\sum g_n$ converges absolutely uniformly on $E$, and in particular uniformly.

:::

::: {.proof}

1. Let $\varepsilon>0$. Since $\sum M_n$ converges, its partial sums are Cauchy, so there is $N$ with $\sum_{k=n+1}^mM_k<\varepsilon$ for all $m>n\ge N$.

2. For such $m,n$ and every $x\in E$,
$$\Bigl|\sum_{k=n+1}^mg_k(x)\Bigr|\le\sum_{k=n+1}^m|g_k(x)|\le\sum_{k=n+1}^mM_k<\varepsilon.$$

3. So both $\sum g_n$ and $\sum|g_n|$ are uniformly Cauchy on $E$, and @thm-uniform-cauchy-criterion makes them uniformly convergent.

:::

::: {#exm-series-of-functions-1 .example name="A continuous function defined by a series"}

$f(x)=\sum_{n=1}^\infty\frac{\sin(nx)}{n^2}$ converges uniformly on $\mathbb R$ by the M-test with $M_n=\frac1{n^2}$. Each partial sum is continuous, so $f$ is continuous (@thm-uniform-limit-continuous), and by @thm-uniform-limit-integral
$$\int_0^\pi f(x)\,dx=\sum_{n=1}^\infty\frac1{n^2}\int_0^\pi\sin(nx)\,dx=\sum_{n\text{ odd}}\frac2{n^3}.$$
The series of derivatives $\sum\frac{\cos(nx)}n$ diverges at $x=0$, so @thm-uniform-limit-derivative cannot be applied term by term.

:::

## Power series

::: {#thm-power-series-uniform .theorem name="Power series converge uniformly inside the disc"}

Let $\sum a_nz^n$ have radius of convergence $R>0$ (@def-radius-of-convergence) and let $0<r<R$. Then $\sum a_nz^n$ converges absolutely uniformly on the closed disc $\{|z|\le r\}$. Consequently its sum $f(z)$ is continuous on the open disc $\{|z|<R\}$.

:::

::: {.proof}

1. Pick $\rho$ with $r<\rho<R$. By @thm-radius-of-convergence, $\sum a_n\rho^n$ converges, so its terms are bounded: $|a_n|\rho^n\le C$ for all $n$.

2. For $|z|\le r$, $|a_nz^n|\le|a_n|r^n\le C\left(\frac r\rho\right)^n=:M_n$, and $\sum M_n$ is a convergent geometric series since $\frac r\rho<1$.

3. By @thm-weierstrass-m-test the series converges absolutely uniformly on $\{|z|\le r\}$.

4. *Continuity.* Given $|z_0|<R$, choose $r$ with $|z_0|<r<R$. The partial sums are polynomials, hence continuous, and converge uniformly on $\{|z|\le r\}$, a set containing all points near $z_0$. By @thm-uniform-limit-continuous, $f$ is continuous at $z_0$.

:::

::: {#exm-power-series-not-uniform .example name="Not uniform on the whole disc"}

$\sum_{n\ge0}x^n=\frac1{1-x}$ has radius $1$ but does not converge uniformly on $(-1,1)$: the partial sums $f_n$ are bounded on $(-1,1)$ (by $n+1$) while $\frac1{1-x}$ is not, so $\sup_{(-1,1)}\bigl|f_n(x)-\frac1{1-x}\bigr|=\infty$ for every $n$.

:::

::: {#cor-power-series-termwise-integration .corollary name="Term-by-term integration"}

If $\sum a_nx^n$ has radius $R>0$ and $|x|<R$, then
$$\int_0^x\sum_{n=0}^\infty a_nt^n\,dt=\sum_{n=0}^\infty\frac{a_n}{n+1}x^{n+1}.$$

:::

::: {.proof}

1. Choose $r$ with $|x|<r<R$. By @thm-power-series-uniform the partial sums converge uniformly on $[-r,r]$, an interval containing $0$ and $x$.

2. Apply @thm-uniform-limit-integral on the interval between $0$ and $x$, and integrate each polynomial partial sum term by term.

:::

::: {#rmk-series-of-functions-1 .remark name="Term-by-term differentiation, again"}

For real power series, differentiability of the sum inside $(-R,R)$ also follows from @thm-uniform-limit-derivative: the derived series has the same radius (@lem-derived-series-converges), so on $[-r,r]$ with $r<R$ it converges uniformly by @thm-power-series-uniform, and the original series converges at $0$. This is a second route to @thm-power-series-differentiable, which is proved directly and holds for complex power series too.

:::
