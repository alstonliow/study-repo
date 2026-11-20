---
title: "The Weierstrass Approximation Theorem"
sources: [camib-at-a3]
requires: [math/analysis/real/uniform-convergence/uniform-convergence, math/analysis/real/integration/integrable-functions]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 3.3 (non-examinable), in our own wording; proof by Bernstein polynomials written out in steps; the moment identities and the example were checked numerically. -->

Polynomials are dense among continuous functions on a closed interval, in the sense of uniform convergence. The proof below is constructive: it writes down the approximating polynomials.

::: {#def-bernstein-polynomial .definition name="Bernstein polynomials"}

For $f:[0,1]\to\mathbb R$ and $n\ge1$, the $n$-th *Bernstein polynomial* of $f$ is
$$B_nf(x)=\sum_{k=0}^nf\!\left(\tfrac kn\right)p_{n,k}(x),\qquad p_{n,k}(x)=\binom nkx^k(1-x)^{n-k}.$$

:::

For $x\in[0,1]$ the numbers $p_{n,k}(x)$ are the probabilities of $k$ successes in $n$ independent trials of success probability $x$ (@def-binomial-distribution). So $B_nf(x)$ averages the values of $f$ at the grid points $\frac kn$, with weights concentrated near $k\approx nx$.

::: {#lem-bernstein-moments .lemma name="Moments of the Bernstein weights"}

For every $x\in[0,1]$ and $n\ge1$,
$$\sum_{k=0}^np_{n,k}(x)=1,\qquad\sum_{k=0}^nk\,p_{n,k}(x)=nx,\qquad\sum_{k=0}^n(k-nx)^2p_{n,k}(x)=nx(1-x).$$

:::

::: {.proof}

1. The first identity is the binomial theorem: $\sum_k\binom nkx^k(1-x)^{n-k}=(x+(1-x))^n=1$.

2. Using $k\binom nk=n\binom{n-1}{k-1}$, $\sum_kk\,p_{n,k}(x)=nx\sum_{j=0}^{n-1}p_{n-1,j}(x)=nx$ by step 1.

3. Likewise $k(k-1)\binom nk=n(n-1)\binom{n-2}{k-2}$ gives $\sum_kk(k-1)p_{n,k}(x)=n(n-1)x^2$. Hence $\sum_kk^2p_{n,k}=n(n-1)x^2+nx$.

4. Expanding, $\sum_k(k-nx)^2p_{n,k}=\sum k^2p_{n,k}-2nx\sum kp_{n,k}+n^2x^2\sum p_{n,k}=n(n-1)x^2+nx-2n^2x^2+n^2x^2=nx-nx^2$.

:::

In probabilistic terms these are the total probability, the mean $nx$ and the variance $nx(1-x)$ of the binomial distribution.

::: {#thm-weierstrass-approximation .theorem name="Weierstrass approximation theorem"}

If $f:[0,1]\to\mathbb R$ is continuous, then $B_nf\to f$ uniformly on $[0,1]$. Hence for every continuous $f:[a,b]\to\mathbb R$ and every $\varepsilon>0$ there is a polynomial $p$ with
$$\sup_{x\in[a,b]}|f(x)-p(x)|<\varepsilon.$$

:::

::: {.proof}

1. *Setup.* $f$ is bounded, say $|f|\le M$ (@thm-extreme-value-proof), and uniformly continuous (@thm-uniform-continuity-compact). Let $\varepsilon>0$ and choose $\delta>0$ with $|f(s)-f(t)|<\frac\varepsilon2$ whenever $|s-t|<\delta$.

2. *Write the error as an average.* By the first identity of @lem-bernstein-moments,
$$|B_nf(x)-f(x)|=\Bigl|\sum_{k=0}^n\bigl(f(\tfrac kn)-f(x)\bigr)p_{n,k}(x)\Bigr|\le\sum_{k=0}^n\bigl|f(\tfrac kn)-f(x)\bigr|p_{n,k}(x).$$

3. *Near terms.* The terms with $|\frac kn-x|<\delta$ contribute at most $\frac\varepsilon2\sum_kp_{n,k}(x)=\frac\varepsilon2$.

4. *Far terms.* If $|\frac kn-x|\ge\delta$, then $|f(\frac kn)-f(x)|\le2M$ and $1\le\frac{(k-nx)^2}{n^2\delta^2}$. So by the third identity these terms contribute at most
$$2M\sum_{k}\frac{(k-nx)^2}{n^2\delta^2}p_{n,k}(x)=\frac{2M\,x(1-x)}{n\delta^2}\le\frac{M}{2n\delta^2}.$$

5. *Uniform bound.* For $n>\frac M{\varepsilon\delta^2}$ the far terms contribute less than $\frac\varepsilon2$, so $|B_nf(x)-f(x)|<\varepsilon$ for every $x\in[0,1]$. The bound does not depend on $x$, so the convergence is uniform.

6. *Other intervals.* For continuous $f$ on $[a,b]$, the function $g(t)=f(a+t(b-a))$ is continuous on $[0,1]$. Take $n$ with $|B_ng-g|<\varepsilon$ on $[0,1]$; then $p(x)=B_ng\bigl(\frac{x-a}{b-a}\bigr)$ is a polynomial with $|p-f|<\varepsilon$ on $[a,b]$.

:::

::: {#exm-bernstein-absolute-value .example name="Approximating a corner"}

Let $f(x)=|x-\frac12|$ on $[0,1]$. Its Bernstein polynomials are smooth, so they cannot match the corner exactly; at $x=\frac12$ the error is $B_nf(\frac12)=\sum_k|\frac kn-\frac12|\binom nk2^{-n}$, which is $0.1875$ for $n=4$, about $0.098$ for $n=16$ and about $0.040$ for $n=100$. It decays like $\frac1{\sqrt{2\pi n}}$, much more slowly than the $O(\frac1n)$ achieved for smooth $f$; the theorem gives uniform convergence but no rate.

:::

::: {#fig-weierstrass-approximation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.32,0) node[lab, anchor=west] {$x$};
\draw[->] (0,0) -- (0,2.40);
\node[lab,tick, anchor=north] at (4.00,0) {$1$};
\node[lab,tick, anchor=north east] at (0,0) {$0$};
\node[lab,tick, anchor=east] at (0,2.00) {$\tfrac12$};
\draw[emph] (0.000,2.000) -- (0.067,1.933) -- (0.133,1.867) -- (0.200,1.800) -- (0.267,1.733) -- (0.333,1.667) -- (0.400,1.600) -- (0.467,1.533) -- (0.533,1.467) -- (0.600,1.400) -- (0.667,1.333) -- (0.733,1.267) -- (0.800,1.200) -- (0.867,1.133) -- (0.933,1.067) -- (1.000,1.000) -- (1.067,0.933) -- (1.133,0.867) -- (1.200,0.800) -- (1.267,0.733) -- (1.333,0.667) -- (1.400,0.600) -- (1.467,0.533) -- (1.533,0.467) -- (1.600,0.400) -- (1.667,0.333) -- (1.733,0.267) -- (1.800,0.200) -- (1.867,0.133) -- (1.933,0.067) -- (2.000,0.000) -- (2.067,0.067) -- (2.133,0.133) -- (2.200,0.200) -- (2.267,0.267) -- (2.333,0.333) -- (2.400,0.400) -- (2.467,0.467) -- (2.533,0.533) -- (2.600,0.600) -- (2.667,0.667) -- (2.733,0.733) -- (2.800,0.800) -- (2.867,0.867) -- (2.933,0.933) -- (3.000,1.000) -- (3.067,1.067) -- (3.133,1.133) -- (3.200,1.200) -- (3.267,1.267) -- (3.333,1.333) -- (3.400,1.400) -- (3.467,1.467) -- (3.533,1.533) -- (3.600,1.600) -- (3.667,1.667) -- (3.733,1.733) -- (3.800,1.800) -- (3.867,1.867) -- (3.933,1.933) -- (4.000,2.000) node[lab, anchor=west] {$f$};
\draw[emph, accent] (0.000,2.000) -- (0.067,1.933) -- (0.133,1.867) -- (0.200,1.801) -- (0.267,1.736) -- (0.333,1.671) -- (0.400,1.608) -- (0.467,1.545) -- (0.533,1.484) -- (0.600,1.425) -- (0.667,1.367) -- (0.733,1.311) -- (0.800,1.258) -- (0.867,1.206) -- (0.933,1.156) -- (1.000,1.109) -- (1.067,1.065) -- (1.133,1.023) -- (1.200,0.984) -- (1.267,0.947) -- (1.333,0.914) -- (1.400,0.883) -- (1.467,0.855) -- (1.533,0.831) -- (1.600,0.810) -- (1.667,0.791) -- (1.733,0.777) -- (1.800,0.765) -- (1.867,0.757) -- (1.933,0.752) -- (2.000,0.750) -- (2.067,0.752) -- (2.133,0.757) -- (2.200,0.765) -- (2.267,0.777) -- (2.333,0.791) -- (2.400,0.810) -- (2.467,0.831) -- (2.533,0.855) -- (2.600,0.883) -- (2.667,0.914) -- (2.733,0.947) -- (2.800,0.984) -- (2.867,1.023) -- (2.933,1.065) -- (3.000,1.109) -- (3.067,1.156) -- (3.133,1.206) -- (3.200,1.258) -- (3.267,1.311) -- (3.333,1.367) -- (3.400,1.425) -- (3.467,1.484) -- (3.533,1.545) -- (3.600,1.608) -- (3.667,1.671) -- (3.733,1.736) -- (3.800,1.801) -- (3.867,1.867) -- (3.933,1.933) -- (4.000,2.000);
\draw[emph, primary] (0.000,2.000) -- (0.067,1.933) -- (0.133,1.867) -- (0.200,1.800) -- (0.267,1.733) -- (0.333,1.667) -- (0.400,1.600) -- (0.467,1.533) -- (0.533,1.467) -- (0.600,1.400) -- (0.667,1.334) -- (0.733,1.267) -- (0.800,1.201) -- (0.867,1.135) -- (0.933,1.070) -- (1.000,1.005) -- (1.067,0.941) -- (1.133,0.878) -- (1.200,0.817) -- (1.267,0.758) -- (1.333,0.702) -- (1.400,0.649) -- (1.467,0.599) -- (1.533,0.554) -- (1.600,0.513) -- (1.667,0.477) -- (1.733,0.447) -- (1.800,0.424) -- (1.867,0.407) -- (1.933,0.396) -- (2.000,0.393) -- (2.067,0.396) -- (2.133,0.407) -- (2.200,0.424) -- (2.267,0.447) -- (2.333,0.477) -- (2.400,0.513) -- (2.467,0.554) -- (2.533,0.599) -- (2.600,0.649) -- (2.667,0.702) -- (2.733,0.758) -- (2.800,0.817) -- (2.867,0.878) -- (2.933,0.941) -- (3.000,1.005) -- (3.067,1.070) -- (3.133,1.135) -- (3.200,1.201) -- (3.267,1.267) -- (3.333,1.334) -- (3.400,1.400) -- (3.467,1.467) -- (3.533,1.533) -- (3.600,1.600) -- (3.667,1.667) -- (3.733,1.733) -- (3.800,1.800) -- (3.867,1.867) -- (3.933,1.933) -- (4.000,2.000);
\node[lab, accent] at (2.0,2.1) {$B_4f$};
\node[lab, primary] at (2.0,1.75) {$B_{16}f$};
\end{tikzpicture}
\end{center}
```

The Bernstein polynomials $B_4f$ and $B_{16}f$ of $f(x)=|x-\frac12|$: they converge uniformly to $f$, most slowly at the corner.

:::

::: {#rmk-weierstrass-approximation-1 .remark name="Why it matters"}

The theorem says that the polynomials are dense in $C[a,b]$ with the uniform norm (@sec-math-analysis-metric-spaces-normed-spaces). Combined with @thm-uniform-limit-integral, a statement about integrals of continuous functions can often be checked on polynomials alone.

:::
