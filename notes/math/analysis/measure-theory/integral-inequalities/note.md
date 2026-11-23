---
title: "Markov, Jensen, Hölder and Minkowski"
sources: [camii-pm-4]
requires: [math/analysis/measure-theory/lebesgue-integral]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 4.1, in our own wording; proofs written out in steps. Markov's and Jensen's inequalities already appear for random variables (math/probability/tail-bounds/concentration-inequalities, math/optimization/convex-functions/convex-functions); here they are stated for general measures and integrable random variables. -->

Four inequalities do most of the work in analysis with integrals. $(E,\mathcal E,\mu)$ is a measure space; for $1\le p<\infty$ write $\|f\|_p=\mu(|f|^p)^{1/p}$ and $\|f\|_\infty=\inf\{c\ge0:\ |f|\le c\text{ a.e.}\}$.

::: {#thm-markov-inequality-measure .theorem name="Markov's inequality for measures" generalizes="thm-markov-inequality"}

For measurable $f\ge0$ and $\lambda>0$,

$$
\mu(\{f\ge\lambda\})\le\frac{\mu(f)}{\lambda}.
$$

Consequently $\mu(\{|f|\ge\lambda\})\le\lambda^{-p}\|f\|_p^p$ for every $p\in[1,\infty)$ (Chebyshev's inequality is $p=2$ applied to $f-\mu(f)$ on a probability space).

:::

::: {.proof}

1. $\lambda\mathbf 1_{\{f\ge\lambda\}}\le f$ pointwise. Integrate.

2. Apply step 1 to $|f|^p$ and the level $\lambda^p$.

:::

::: {#lem-convex-supporting-line .lemma name="Convex functions lie above their supporting lines"}

Let $c:I\to\mathbb R$ be convex on an open interval $I$ and $m\in I$. There are $a,b\in\mathbb R$ with $c(x)\ge ax+b$ for all $x\in I$ and $c(m)=am+b$. Hence $c$ is the supremum of countably many affine functions, $c(x)=\sup_n(a_nx+b_n)$.

:::

::: {.proof}

1. For $x<m<y$ in $I$, convexity with $m=\theta x+(1-\theta)y$ rearranges to the slope inequality
$$\frac{c(m)-c(x)}{m-x}\le\frac{c(y)-c(m)}{y-m}.$$

2. Let $a=\sup_{x<m}\frac{c(m)-c(x)}{m-x}$; by step 1, $a$ is finite and at most every right slope. So $c(x)\ge c(m)+a(x-m)$ for $x<m$ (by definition of $a$) and for $x>m$ (by step 1). Take $b=c(m)-am$.

3. Doing this at every rational $m\in I$ gives countably many affine minorants. Their supremum is $\le c$; it equals $c$ because a convex function on an open interval is continuous, so $c(x)=\lim c(m_k)$ along rationals $m_k\to x$, and the supporting lines at $m_k$ have bounded slopes near $x$.

:::

::: {#fig-integral-inequalities-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (5.6,0) node[lab, right] {$x$};
\draw[->] (0,-0.6) -- (0,3.6) node[lab, above] {};
\draw[emph] (0.100,2.022) -- (0.150,1.966) -- (0.200,1.910) -- (0.250,1.856) -- (0.300,1.802) -- (0.350,1.751) -- (0.400,1.700) -- (0.450,1.651) -- (0.500,1.603) -- (0.550,1.556) -- (0.600,1.510) -- (0.650,1.466) -- (0.700,1.422) -- (0.750,1.381) -- (0.800,1.340) -- (0.850,1.301) -- (0.900,1.263) -- (0.950,1.226) -- (1.000,1.190) -- (1.050,1.156) -- (1.100,1.123) -- (1.150,1.091) -- (1.200,1.060) -- (1.250,1.031) -- (1.300,1.002) -- (1.350,0.976) -- (1.400,0.950) -- (1.450,0.926) -- (1.500,0.902) -- (1.550,0.881) -- (1.600,0.860) -- (1.650,0.841) -- (1.700,0.822) -- (1.750,0.806) -- (1.800,0.790) -- (1.850,0.776) -- (1.900,0.762) -- (1.950,0.751) -- (2.000,0.740) -- (2.050,0.731) -- (2.100,0.722) -- (2.150,0.716) -- (2.200,0.710) -- (2.250,0.706) -- (2.300,0.703) -- (2.350,0.701) -- (2.400,0.700) -- (2.450,0.701) -- (2.500,0.703) -- (2.550,0.706) -- (2.600,0.710) -- (2.650,0.716) -- (2.700,0.723) -- (2.750,0.731) -- (2.800,0.740) -- (2.850,0.751) -- (2.900,0.763) -- (2.950,0.776) -- (3.000,0.790) -- (3.050,0.806) -- (3.100,0.823) -- (3.150,0.841) -- (3.200,0.860) -- (3.250,0.881) -- (3.300,0.903) -- (3.350,0.926) -- (3.400,0.950) -- (3.450,0.976) -- (3.500,1.003) -- (3.550,1.031) -- (3.600,1.060) -- (3.650,1.091) -- (3.700,1.123) -- (3.750,1.156) -- (3.800,1.190) -- (3.850,1.226) -- (3.900,1.263) -- (3.950,1.301) -- (4.000,1.340) -- (4.050,1.381) -- (4.100,1.422) -- (4.150,1.466) -- (4.200,1.510) -- (4.250,1.556) -- (4.300,1.603) -- (4.350,1.651) -- (4.400,1.700) -- (4.450,1.751) -- (4.500,1.803) -- (4.550,1.856) -- (4.600,1.910) -- (4.650,1.966) -- (4.700,2.023) -- (4.750,2.081) -- (4.800,2.140) -- (4.850,2.201) -- (4.900,2.263) -- (4.950,2.326) -- (5.000,2.390) -- (5.050,2.456);
\draw[hl] (0.600,0.300) -- (5.200,1.220);
\fill (2.8,0.740) circle (1.8pt);
\draw[faint, dashed] (2.8,0.740) -- (2.8,0) node[lab, below] {$m=E[X]$};
\node[lab] at (4.9,3.2) {$c$};
\node[lab, text=accent] at (5.2,1.0) {$ax+b$};
\end{tikzpicture}
\end{center}
```

A convex function lies above its supporting line at $m$. Applying $c(X)\ge aX+b$ and taking expectations at $m=E[X]$ gives Jensen's inequality $E[c(X)]\ge c(E[X])$.

:::

::: {#thm-jensen-integrable .theorem name="Jensen's inequality for integrable random variables" generalizes="thm-jensen-inequality"}

Let $X$ be an integrable random variable with values in an open interval $I$ and $c:I\to\mathbb R$ convex. Then $E[c(X)]$ is well defined in $(-\infty,\infty]$ and

$$
c\big(E[X]\big)\le E\big[c(X)\big].
$$

:::

::: {.proof}

1. $m=E[X]$ lies in $I$: if, say, $I=(\alpha,\beta)$ and $m=\beta$, then $\beta-X>0$ has integral $0$, which is impossible (@thm-integral-linear-monotone).

2. Take the supporting line at $m$ from @lem-convex-supporting-line: $c(X)\ge aX+b$. The right side is integrable, so $c(X)^-\le|aX+b|$ is integrable and $E[c(X)]$ makes sense.

3. Integrate: $E[c(X)]\ge aE[X]+b=am+b=c(m)$.

:::

Jensen needs a probability measure: for $c(x)=x^2$ it says $\|f\|_1\le\|f\|_2$ when $\mu(E)=1$, which fails for Lebesgue measure on $[0,2]$ and $f=1$.

::: {#thm-holder-inequality .theorem name="Hölder's inequality"}

Let $p,q\in[1,\infty]$ be *conjugate*, $\frac1p+\frac1q=1$. For measurable $f,g$,

$$
\mu(|fg|)\le\|f\|_p\,\|g\|_q .
$$

The case $p=q=2$ is the Cauchy–Schwarz inequality.

:::

::: {.proof}

1. If $p=1$, $q=\infty$: $|fg|\le|f|\,\|g\|_\infty$ a.e.; integrate. Now let $1<p<\infty$. If $\|f\|_p$ or $\|g\|_q$ is $0$, then $fg=0$ a.e.; if one is $\infty$ there is nothing to prove. Scaling $f$ and $g$, assume $\|f\|_p=\|g\|_q=1$.

2. For $a,b\ge0$, concavity of $\log$ gives Young's inequality
$$ab=\exp\big(\tfrac1p\log a^p+\tfrac1q\log b^q\big)\le\tfrac1pa^p+\tfrac1qb^q$$
(trivial if $a$ or $b$ is $0$).

3. Apply it pointwise with $a=|f(x)|$, $b=|g(x)|$ and integrate: $\mu(|fg|)\le\frac1p\|f\|_p^p+\frac1q\|g\|_q^q=\frac1p+\frac1q=1$.

:::

::: {#thm-minkowski-inequality .theorem name="Minkowski's inequality"}

For $p\in[1,\infty]$ and measurable $f,g$,

$$
\|f+g\|_p\le\|f\|_p+\|g\|_p .
$$

:::

::: {.proof}

1. The cases $p=1$ and $p=\infty$ follow from $|f+g|\le|f|+|g|$. Let $1<p<\infty$ and $q=\frac p{p-1}$; assume $\|f\|_p,\|g\|_p<\infty$.

2. Then $\|f+g\|_p<\infty$, because $|f+g|^p\le(2\max(|f|,|g|))^p\le2^p(|f|^p+|g|^p)$.

3. Write $|f+g|^p\le|f|\,|f+g|^{p-1}+|g|\,|f+g|^{p-1}$ and apply Hölder to each term, using $\big\||f+g|^{p-1}\big\|_q=\mu(|f+g|^p)^{1/q}=\|f+g\|_p^{p-1}$:
$$\|f+g\|_p^p\le\big(\|f\|_p+\|g\|_p\big)\,\|f+g\|_p^{p-1}.$$

4. If $\|f+g\|_p=0$ we are done; otherwise divide by the finite number $\|f+g\|_p^{p-1}$.

:::
