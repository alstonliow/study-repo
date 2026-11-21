---
title: "Fourier Inversion and Plancherel's Theorem"
sources: [camii-pm-5]
requires: [math/analysis/measure-theory/fourier-transform]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Sections 5.3 and 5.4, in our own wording; proofs written out in steps. The density lemma is proved here (the source leaves it to the example sheet). Surjectivity of the L^2 Fourier transform is stated without proof. -->

The plan: inversion is explicit for Gaussians (@cor-gaussian-inversion), hence for Gaussian smoothings $f*g_t$; letting $t\to0$ recovers $f$. The limit needs an approximation lemma.

::: {#lem-cc-dense-lp .lemma name="Continuous functions of compact support are dense"}

For $1\le p<\infty$ the continuous functions of compact support are dense in $L^p(\mathbb R^d)$. Consequently translation is continuous in $L^p$: $\|f(\cdot+h)-f\|_p\to0$ as $h\to0$.

:::

::: {.proof}

1. Splitting into real and imaginary, positive and negative parts, take $f\ge0$ in $L^p$. The truncated dyadic approximations $f_n\uparrow f$ of @prp-dyadic-approximation, multiplied by $\mathbf 1_{\{|x|\le n\}}$, are simple, and $|f-f_n|^p\le f^p$ is dominated; so $f_n\to f$ in $L^p$ by dominated convergence. It suffices to approximate $\mathbf 1_A$ for Borel $A$ of finite measure.

2. By the construction of Lebesgue measure as an outer measure (@thm-caratheodory-extension), for $\varepsilon>0$ there are boxes $B_k$ with $A\subseteq\bigcup_kB_k$ and $\sum_k\lambda(B_k)\le\lambda(A)+\varepsilon$. Taking finitely many, $B=B_1\cup\dots\cup B_K$ satisfies $\lambda(A\triangle B)\le2\varepsilon$, so $\|\mathbf 1_A-\mathbf 1_B\|_p\le(2\varepsilon)^{1/p}$.

3. A box $\prod_j(a_j,b_j]$ has indicator $\prod_j\mathbf 1_{(a_j,b_j]}(x_j)$; each factor is the pointwise limit of continuous piecewise linear functions with values in $[0,1]$, supported in $[a_j-1,b_j+1]$. By dominated convergence the products converge to the box indicator in $L^p$. Finite sums of such approximations handle $B$.

4. For translation: given $\varepsilon$, pick continuous $g$ of compact support with $\|f-g\|_p\le\varepsilon$. Then $\|f(\cdot+h)-f\|_p\le2\varepsilon+\|g(\cdot+h)-g\|_p$, and the last term tends to $0$ by uniform continuity of $g$ and dominated convergence on a fixed compact set.

:::

::: {#lem-gaussian-approximate-identity .lemma name="Gaussian smoothing converges"}

For $f\in L^p$, $1\le p<\infty$: $\|f*g_t-f\|_p\to0$ as $t\to0$.

:::

::: {.proof}

1. $f*g_t(x)-f(x)=E\big[f(x-\sqrt tZ)-f(x)\big]$ with $Z$ standard Gaussian. By Jensen and Tonelli as in @prp-convolution-properties,
$$\|f*g_t-f\|_p^p\le E\big[\|f(\cdot-\sqrt tZ)-f\|_p^p\big].$$

2. For each value of $Z$ the integrand tends to $0$ as $t\to0$ by @lem-cc-dense-lp, and it is at most $(2\|f\|_p)^p$. Bounded convergence (@cor-bounded-convergence-finite-measure) finishes the proof.

:::

::: {#fig-fourier-inversion-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-3.0,0) -- (3.2,0) node[lab, right] {$x$};
\draw[->] (0,-0.1) -- (0,2.2) node[lab, above] {};
\draw[emph] (-2.8,0) -- (-1,0) -- (-1,1.6) -- (1,1.6) -- (1,0) -- (2.8,0);
\draw[hl] (-2.800,0.000) -- (-2.750,0.000) -- (-2.700,0.000) -- (-2.650,0.000) -- (-2.600,0.000) -- (-2.550,0.000) -- (-2.500,0.000) -- (-2.450,0.000) -- (-2.400,0.000) -- (-2.350,0.000) -- (-2.300,0.000) -- (-2.250,0.000) -- (-2.200,0.000) -- (-2.150,0.000) -- (-2.100,0.000) -- (-2.050,0.000) -- (-2.000,0.000) -- (-1.950,0.000) -- (-1.900,0.000) -- (-1.850,0.000) -- (-1.800,0.000) -- (-1.750,0.001) -- (-1.700,0.001) -- (-1.650,0.003) -- (-1.600,0.006) -- (-1.550,0.011) -- (-1.500,0.020) -- (-1.450,0.035) -- (-1.400,0.059) -- (-1.350,0.094) -- (-1.300,0.144) -- (-1.250,0.211) -- (-1.200,0.297) -- (-1.150,0.402) -- (-1.100,0.524) -- (-1.050,0.658) -- (-1.000,0.800) -- (-0.950,0.942) -- (-0.900,1.076) -- (-0.850,1.198) -- (-0.800,1.303) -- (-0.750,1.389) -- (-0.700,1.456) -- (-0.650,1.506) -- (-0.600,1.541) -- (-0.550,1.565) -- (-0.500,1.580) -- (-0.450,1.589) -- (-0.400,1.594) -- (-0.350,1.597) -- (-0.300,1.599) -- (-0.250,1.599) -- (-0.200,1.600) -- (-0.150,1.600) -- (-0.100,1.600) -- (-0.050,1.600) -- (0.000,1.600) -- (0.050,1.600) -- (0.100,1.600) -- (0.150,1.600) -- (0.200,1.600) -- (0.250,1.599) -- (0.300,1.599) -- (0.350,1.597) -- (0.400,1.594) -- (0.450,1.589) -- (0.500,1.580) -- (0.550,1.565) -- (0.600,1.541) -- (0.650,1.506) -- (0.700,1.456) -- (0.750,1.389) -- (0.800,1.303) -- (0.850,1.198) -- (0.900,1.076) -- (0.950,0.942) -- (1.000,0.800) -- (1.050,0.658) -- (1.100,0.524) -- (1.150,0.402) -- (1.200,0.297) -- (1.250,0.211) -- (1.300,0.144) -- (1.350,0.094) -- (1.400,0.059) -- (1.450,0.035) -- (1.500,0.020) -- (1.550,0.011) -- (1.600,0.006) -- (1.650,0.003) -- (1.700,0.001) -- (1.750,0.001) -- (1.800,0.000) -- (1.850,0.000) -- (1.900,0.000) -- (1.950,0.000) -- (2.000,0.000) -- (2.050,0.000) -- (2.100,0.000) -- (2.150,0.000) -- (2.200,0.000) -- (2.250,0.000) -- (2.300,0.000) -- (2.350,0.000) -- (2.400,0.000) -- (2.450,0.000) -- (2.500,0.000) -- (2.550,0.000) -- (2.600,0.000) -- (2.650,0.000) -- (2.700,0.000) -- (2.750,0.000) -- (2.800,0.000);
\draw[faint] (-2.800,0.004) -- (-2.750,0.005) -- (-2.700,0.006) -- (-2.650,0.007) -- (-2.600,0.009) -- (-2.550,0.011) -- (-2.500,0.014) -- (-2.450,0.017) -- (-2.400,0.021) -- (-2.350,0.026) -- (-2.300,0.032) -- (-2.250,0.038) -- (-2.200,0.046) -- (-2.150,0.055) -- (-2.100,0.066) -- (-2.050,0.077) -- (-2.000,0.091) -- (-1.950,0.106) -- (-1.900,0.124) -- (-1.850,0.143) -- (-1.800,0.165) -- (-1.750,0.189) -- (-1.700,0.215) -- (-1.650,0.243) -- (-1.600,0.274) -- (-1.550,0.308) -- (-1.500,0.343) -- (-1.450,0.381) -- (-1.400,0.422) -- (-1.350,0.464) -- (-1.300,0.508) -- (-1.250,0.554) -- (-1.200,0.601) -- (-1.150,0.649) -- (-1.100,0.699) -- (-1.050,0.749) -- (-1.000,0.799) -- (-0.950,0.849) -- (-0.900,0.898) -- (-0.850,0.947) -- (-0.800,0.995) -- (-0.750,1.041) -- (-0.700,1.086) -- (-0.650,1.129) -- (-0.600,1.169) -- (-0.550,1.207) -- (-0.500,1.242) -- (-0.450,1.275) -- (-0.400,1.304) -- (-0.350,1.331) -- (-0.300,1.353) -- (-0.250,1.373) -- (-0.200,1.389) -- (-0.150,1.402) -- (-0.100,1.411) -- (-0.050,1.416) -- (0.000,1.418) -- (0.050,1.416) -- (0.100,1.411) -- (0.150,1.402) -- (0.200,1.389) -- (0.250,1.373) -- (0.300,1.353) -- (0.350,1.331) -- (0.400,1.304) -- (0.450,1.275) -- (0.500,1.242) -- (0.550,1.207) -- (0.600,1.169) -- (0.650,1.129) -- (0.700,1.086) -- (0.750,1.041) -- (0.800,0.995) -- (0.850,0.947) -- (0.900,0.898) -- (0.950,0.849) -- (1.000,0.799) -- (1.050,0.749) -- (1.100,0.699) -- (1.150,0.649) -- (1.200,0.601) -- (1.250,0.554) -- (1.300,0.508) -- (1.350,0.464) -- (1.400,0.422) -- (1.450,0.381) -- (1.500,0.343) -- (1.550,0.308) -- (1.600,0.274) -- (1.650,0.243) -- (1.700,0.215) -- (1.750,0.189) -- (1.800,0.165) -- (1.850,0.143) -- (1.900,0.124) -- (1.950,0.106) -- (2.000,0.091) -- (2.050,0.077) -- (2.100,0.066) -- (2.150,0.055) -- (2.200,0.046) -- (2.250,0.038) -- (2.300,0.032) -- (2.350,0.026) -- (2.400,0.021) -- (2.450,0.017) -- (2.500,0.014) -- (2.550,0.011) -- (2.600,0.009) -- (2.650,0.007) -- (2.700,0.006) -- (2.750,0.005) -- (2.800,0.004);
\node[lab] at (1.9,1.5) {$f=\mathbf 1_{[-1,1]}$};
\node[lab, text=accent] at (-2.0,1.0) {$f*g_t$};
\end{tikzpicture}
\end{center}
```

Gaussian smoothing $f*g_t$ of an indicator for $t=0.4$ (grey) and $t=0.05$ (red). As $t\to0$ it converges to $f$ in $L^1$; the inversion formula holds exactly for every smoothing and passes to the limit.

:::

::: {#thm-fourier-inversion .theorem name="Fourier inversion formula"}

Let $f\in L^1(\mathbb R^d)$ with $\hat f\in L^1(\mathbb R^d)$. Then for almost every $x$

$$
f(x)=(2\pi)^{-d}\int_{\mathbb R^d}\hat f(u)\,e^{-i\langle u,x\rangle}\,du ,
$$

and the right-hand side is a bounded continuous function, so $f$ has a continuous version.

:::

::: {.proof}

1. *Gaussian smoothings.* By Fubini (the integrand $|f(y)|e^{-t|u|^2/2}$ is integrable in $(y,u)$) and @cor-gaussian-inversion,
$$(2\pi)^{-d}\!\int\hat f(u)e^{-t|u|^2/2}e^{-i\langle u,x\rangle}du=\int f(y)\Big[(2\pi)^{-d}\!\int\hat g_t(u)e^{-i\langle u,x-y\rangle}du\Big]dy=\int f(y)g_t(x-y)\,dy=f*g_t(x).$$

2. *Limit of the left side.* As $t\to0$ the integrand tends to $\hat f(u)e^{-i\langle u,x\rangle}$ and is dominated by $|\hat f|\in L^1$. So the left side tends to $F(x)=(2\pi)^{-d}\int\hat f(u)e^{-i\langle u,x\rangle}du$ for every $x$.

3. *Limit of the right side.* By @lem-gaussian-approximate-identity with $p=1$, $f*g_t\to f$ in $L^1$, so along some sequence $t_n\to0$, $f*g_{t_n}\to f$ a.e. (@thm-lp-complete).

4. Hence $f=F$ a.e. $F$ is bounded by $(2\pi)^{-d}\|\hat f\|_1$ and continuous by @prp-fourier-bounded-continuous applied to $\hat f$.

:::

::: {#cor-fourier-uniqueness .corollary name="The Fourier transform is injective"}

If $f\in L^1$ and $\hat f=0$, then $f=0$ a.e.

:::

::: {.proof}

$\hat f=0$ is integrable, so by @thm-fourier-inversion $f$ equals $(2\pi)^{-d}\int0\,du=0$ almost everywhere.

:::

## The Fourier transform on $L^2$

::: {#thm-plancherel .theorem name="Plancherel's theorem"}

For $f\in L^1\cap L^2$, $\hat f\in L^2$ and

$$
\|\hat f\|_2^2=(2\pi)^d\,\|f\|_2^2 .
$$

Hence $f\mapsto(2\pi)^{-d/2}\hat f$ extends uniquely to a linear isometry $\mathcal F:L^2\to L^2$.

:::

::: {.proof}

1. Let $\tilde f(x)=\overline{f(-x)}$ and $h=f*\tilde f$, i.e. $h(x)=\int f(x+y)\overline{f(y)}\,dy$ after substituting. Then $h\in L^1$, and $|h(x)-h(x')|\le\|f(\cdot+x)-f(\cdot+x')\|_2\|f\|_2$ by Cauchy–Schwarz, so $h$ is bounded and continuous by @lem-cc-dense-lp, with $h(0)=\|f\|_2^2$.

2. $\hat{\tilde f}=\overline{\hat f}$, so $\hat h=\hat f\,\overline{\hat f}=|\hat f|^2$ (@prp-convolution-properties, extended to $L^1$ functions by linearity).

3. Step 1 of the inversion proof, applied to $h$ at $x=0$, gives
$$(2\pi)^{-d}\int|\hat f(u)|^2e^{-t|u|^2/2}\,du=(h*g_t)(0)=E\big[h(-\sqrt tZ)\big].$$

4. As $t\downarrow0$ the left side increases to $(2\pi)^{-d}\|\hat f\|_2^2$ by monotone convergence; the right side tends to $h(0)=\|f\|_2^2$ by bounded convergence, $h$ being bounded and continuous. This proves the identity.

5. $L^1\cap L^2$ is dense in $L^2$ (it contains the continuous functions of compact support, @lem-cc-dense-lp). A linear map that is isometric on a dense subspace extends uniquely by continuity: for $f_n\to f$ in $L^2$ the images form a Cauchy sequence, whose limit does not depend on the chosen sequence, and the norm identity passes to the limit.

:::

::: {#rmk-fourier-inversion-l2 .remark name="The $L^2$ transform is onto"}

The isometry $\mathcal F$ is in fact a bijection of $L^2$ onto itself, with inverse given by the same construction with $e^{-i\langle u,x\rangle}$ (a unitary map, after taking complex inner products). We state this without proof. Transform pairs can then be manipulated freely in $L^2$, as in the example sheets.

:::
