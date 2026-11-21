---
title: "Goodness of Fit: Kolmogorov–Smirnov Tests and QQ Plots"
sources: [mit18650-6]
requires: [math/statistics/inference/parametric-tests, math/statistics/frequentist/bootstrap]
status: draft
---

<!-- Added 2026-11-21 from MIT 18.650 (Fall 2016), Chapter 6 (empirical CDF, Glivenko-Cantelli and Donsker theorems, Kolmogorov-Smirnov test and its computation, pivotal statistics and simulated quantiles, other distances, Kolmogorov-Lilliefors test, QQ plots; the chi-square test with estimated parameters is in the parametric-tests note), in our own wording. The proofs, the numerical example and the remark on reading QQ plots are our own. -->

A goodness-of-fit test asks whether the data come from a given distribution, such as $N(0,1)$ or $U[0,1]$, without assuming a parametric family for the alternative. For finitely many values the chi-square test does this (@thm-pearson-chi-square-limit). For continuous data the natural object to compare is the CDF, which characterises the distribution.

::: {#def-empirical-cdf .definition name="Empirical CDF" related="def-empirical-distribution"}

The *empirical CDF* of real observations $X_1,\dots,X_n$ is the CDF of their empirical distribution,

$$
F_n(t)=\frac1n\sum_{i=1}^n\mathbf 1\{X_i\le t\}=\frac{\#\{i:X_i\le t\}}{n},\qquad t\in\mathbb{R}.
$$

It is a step function that jumps by $1/n$ at each observation. We write $X_{(1)}\le\dots\le X_{(n)}$ for the sorted sample (the *order statistics*).

:::

For each fixed $t$, $nF_n(t)\sim\operatorname{Bin}(n,F(t))$, where $F$ is the true CDF. So $F_n(t)\to F(t)$ almost surely by the strong law of large numbers, and $\sqrt n(F_n(t)-F(t))\xrightarrow{d}N\bigl(0,F(t)(1-F(t))\bigr)$ by the central limit theorem. Much more is true.

::: {#thm-glivenko-cantelli .theorem name="Glivenko–Cantelli theorem"}

If $X_1,X_2,\dots$ are independent with CDF $F$, then

$$
\sup_{t\in\mathbb{R}}\bigl|F_n(t)-F(t)\bigr|\to0\qquad\text{almost surely.}
$$

:::

::: {.proof}

We give the proof for continuous $F$; the general case uses left limits $F(t^-)$ at the grid points in the same way.

1. Fix an integer $k\ge1$. Since $F$ is continuous and increases from $0$ to $1$, there are points $-\infty=t_0<t_1<\dots<t_{k-1}<t_k=+\infty$ with $F(t_j)=j/k$ (take $t_j$ to be a $j/k$-quantile).

2. For $t\in[t_{j-1},t_j]$, monotonicity of $F_n$ and $F$ gives
   $$F_n(t)-F(t)\le F_n(t_j)-F(t_{j-1})=F_n(t_j)-F(t_j)+\tfrac1k,$$
   $$F_n(t)-F(t)\ge F_n(t_{j-1})-F(t_j)=F_n(t_{j-1})-F(t_{j-1})-\tfrac1k .$$

3. Hence $\sup_t|F_n(t)-F(t)|\le\max_{0\le j\le k}|F_n(t_j)-F(t_j)|+1/k$ (at $t_0,t_k$ the difference is $0$).

4. By the strong law, $F_n(t_j)\to F(t_j)$ almost surely for each of the finitely many $j$, so the maximum tends to $0$ almost surely and $\limsup_n\sup_t|F_n-F|\le1/k$ almost surely.

5. Intersecting these probability-one events over $k=1,2,\dots$ gives the claim.

:::

The fluctuations of the whole curve are also known. *Donsker's theorem* (stated without proof) says that if $F$ is continuous,
$$\sqrt n\,\sup_t|F_n(t)-F(t)|\xrightarrow{d}\sup_{0\le u\le1}|B(u)|,$$
where $B$ is a *Brownian bridge*, a continuous Gaussian process on $[0,1]$ with $B(0)=B(1)=0$ and $\operatorname{Cov}(B(u),B(v))=\min(u,v)-uv$. The limit law, the *Kolmogorov distribution*, does not depend on $F$.

::: {#lem-probability-integral-transform .lemma name="Probability integral transform"}

If $X$ has a continuous CDF $F$, then $U=F(X)$ is uniform on $[0,1]$. Moreover $\{X\le t\}$ and $\{U\le F(t)\}$ differ by an event of probability $0$.

:::

::: {.proof}

1. Let $u\in(0,1)$ and let $x_u=\max\{x:F(x)=u\}$, which exists because $F$ is continuous with limits $0$ and $1$ (the set is closed, non-empty by the intermediate value theorem, and bounded above).

2. Since $F$ is non-decreasing, $F(X)\le u$ if and only if $X\le x_u$. So $\Pr(U\le u)=\Pr(X\le x_u)=F(x_u)=u$, the uniform CDF.

3. For the second claim, $\{X\le t\}\subseteq\{F(X)\le F(t)\}$, and the difference is the event that $X$ lies in an interval $(t,s]$ on which $F$ is constant, which has probability $F(s)-F(t)=0$.

:::

::: {#def-kolmogorov-smirnov-test .definition name="Kolmogorov–Smirnov test"}

Let $X_1,\dots,X_n$ be independent with unknown CDF $F$, and $F^0$ a given continuous CDF. To test $H_0:F=F^0$ against $H_1:F\ne F^0$, the *Kolmogorov–Smirnov (KS) statistic* is

$$
T_n=\sqrt n\,\sup_{t\in\mathbb{R}}\bigl|F_n(t)-F^0(t)\bigr| ,
$$

and the KS test of level $\alpha$ is $\mathbf 1\{T_n>q_\alpha\}$, where $q_\alpha$ is the $(1-\alpha)$-quantile of the null distribution of $T_n$ (exact, from tables or simulation), or of the Kolmogorov distribution for an asymptotic test.

:::

::: {#prp-ks-computation .proposition name="Computing the KS statistic and its null law"}

1. $T_n=\sqrt n\displaystyle\max_{1\le i\le n}\max\Bigl(\frac in-F^0(X_{(i)}),\ F^0(X_{(i)})-\frac{i-1}n\Bigr)$.
2. Under $H_0$, $T_n$ has the same distribution as $\sqrt n\sup_{0\le u\le1}|G_n(u)-u|$, where $G_n$ is the empirical CDF of $n$ independent $U[0,1]$ variables. So $T_n$ is *pivotal*: its null distribution is the same for every continuous $F^0$.

:::

::: {.proof}

1. Assume the $X_i$ are distinct (true with probability $1$ under a continuous $F$). On $[X_{(i)},X_{(i+1)})$ the step function $F_n$ equals $i/n$ while $F^0$ increases, so $F_n-F^0$ is largest at the left end and $F^0-F_n$ approaches its supremum at the right end, where it tends to $F^0(X_{(i+1)})-i/n$. Below $X_{(1)}$ only $F^0-F_n=F^0\le F^0(X_{(1)})$ matters, and above $X_{(n)}$ only $F_n-F^0=1-F^0\le1-F^0(X_{(n)})$. Collecting the candidates gives the formula.

2. Let $U_i=F^0(X_i)$. Under $H_0$ these are independent and uniform (@lem-probability-integral-transform), and $\mathbf 1\{X_i\le t\}=\mathbf 1\{U_i\le F^0(t)\}$ with probability $1$. So $F_n(t)=G_n(F^0(t))$ for all $t$, and $\sup_t|F_n(t)-F^0(t)|=\sup_{u\in F^0(\mathbb{R})}|G_n(u)-u|$.

3. Since $F^0$ is continuous, $F^0(\mathbb{R})$ contains $(0,1)$, and $G_n(u)-u$ is right-continuous, so the supremum over $(0,1)$ equals that over $[0,1]$ (at $0$ and $1$ the difference is $0$ with probability $1$).

:::

::: {#exm-ks-uniform .example name="A small KS test"}

Test whether $0.08,\ 0.27,\ 0.35,\ 0.62,\ 0.71$ come from $U[0,1]$, so $F^0(t)=t$ on $[0,1]$. The values $i/n-X_{(i)}$ are $0.12,0.13,0.25,0.18,0.29$ and the values $X_{(i)}-(i-1)/n$ are $0.08,0.07,-0.05,0.02,-0.09$. The largest is $0.29$, at $X_{(5)}=0.71$, so $T_5=\sqrt5\cdot0.29\approx0.65$. The exact p-value is about $0.70$: five points are far too few to reject uniformity, even though none exceeds $0.71$.

:::

::: {#fig-goodness-of-fit-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.30,0) node[lab, right] {$t$};
\draw[->] (0,0) -- (0,5.30) node[lab, above] {};
\draw (0.000,0) -- (0.000,-0.07) node[lab, tick, below] {0};
\draw (5.000,0) -- (5.000,-0.07) node[lab, tick, below] {1};
\draw (1.750,0) -- (1.750,-0.07) node[lab, tick, below] {0.35};
\draw (3.550,0) -- (3.550,-0.07) node[lab, tick, below] {0.71};
\draw (0,5.000) -- (-0.07,5.000) node[lab, tick, left] {1};
\draw[emph, primary] (0.000,0.000) -- (5.000,5.000);
\node[lab, primary, anchor=west] at (3.10,2.50) {$F^0(t)=t$};
\draw[bold] (0.000,0.000) -- (0.400,0.000);
\node[dot] at (0.400,1.000) {};
\node[hollow dot] at (0.400,0.000) {};
\draw[bold] (0.400,1.000) -- (1.350,1.000);
\node[dot] at (1.350,2.000) {};
\node[hollow dot] at (1.350,1.000) {};
\draw[bold] (1.350,2.000) -- (1.750,2.000);
\node[dot] at (1.750,3.000) {};
\node[hollow dot] at (1.750,2.000) {};
\draw[bold] (1.750,3.000) -- (3.100,3.000);
\node[dot] at (3.100,4.000) {};
\node[hollow dot] at (3.100,3.000) {};
\draw[bold] (3.100,4.000) -- (3.550,4.000);
\node[dot] at (3.550,5.000) {};
\node[hollow dot] at (3.550,4.000) {};
\draw[bold] (3.550,5.000) -- (5.000,5.000);
\draw[hl] (3.550,3.550) -- (3.550,5.000);
\node[lab, anchor=east] at (3.500,4.300) {$0.29$};
\node[lab, anchor=west] at (0.25,4.60) {$F_5(t)$};
\end{tikzpicture}
\end{center}
```

The empirical CDF of the five observations (steps) against the uniform CDF $F^0(t)=t$. The largest vertical gap, $0.29$, is just after the jump at $X_{(5)}=0.71$, where $F_5=1$; so $T_5=\sqrt5\cdot0.29$.

:::

::: {#def-simulated-null-quantile .definition name="Quantiles of a pivotal statistic by simulation"}

Let $T_n$ be pivotal with a null distribution that can be sampled (for KS: compute $\sqrt n\sup_u|G_n(u)-u|$ from $n$ simulated uniforms). For a large $M$:

1. simulate $M$ independent copies $T_n^{(1)},\dots,T_n^{(M)}$ of $T_n$ under $H_0$;
2. take $\hat q_\alpha$ to be the empirical $(1-\alpha)$-quantile of $T_n^{(1)},\dots,T_n^{(M)}$;
3. reject $H_0$ when $T_n>\hat q_\alpha$; the approximate p-value is $\#\{m:T_n^{(m)}>T_n\}/M$.

The approximation error comes only from the simulation and tends to $0$ as $M\to\infty$, for every fixed $n$.

:::

```{=latex}
\begin{algorithm}
\caption{Simulated critical value and p-value of a pivotal test statistic}
\begin{algorithmic}
\INPUT observed statistic $t$; sample size $n$; level $\alpha$; number of simulations $M$
\FOR{$m=1,\dots,M$}
    \STATE draw $U_1,\dots,U_n$ independent uniform on $[0,1]$
    \STATE $T^{(m)}\gets$ the statistic computed from $U_1,\dots,U_n$ \COMMENT{for KS: $\sqrt n\max_i\max(\frac in-U_{(i)},U_{(i)}-\frac{i-1}n)$}
\ENDFOR
\STATE $\hat q_\alpha\gets$ the $\lceil(1-\alpha)M\rceil$-th smallest of $T^{(1)},\dots,T^{(M)}$
\STATE \textbf{return} reject if $t>\hat q_\alpha$; p-value $\approx\#\{m:T^{(m)}>t\}/M$
\end{algorithmic}
\end{algorithm}
```

::: {#rmk-other-distances .remark name="Other distances between CDFs"}

The KS statistic measures $\sup_t|F_n-F^0|$. Two other common choices weight the whole curve: the *Cramér–von Mises* distance $\int\bigl(F_n(t)-F^0(t)\bigr)^2\,dF^0(t)$ and the *Anderson–Darling* distance $\int\frac{(F_n(t)-F^0(t))^2}{F^0(t)(1-F^0(t))}\,dF^0(t)$, which gives more weight to the tails. Both are pivotal by the same argument.

:::

::: {#rmk-kolmogorov-lilliefors .remark name="Estimated parameters: the Kolmogorov–Lilliefors test"}

To test "the data are Gaussian" with unknown mean and variance, it is tempting to plug in $\hat\mu=\bar X_n$ and $\hat\sigma^2$ and use the KS quantiles for $\sup_t|F_n(t)-\Phi((t-\hat\mu)/\hat\sigma)|$. This is wrong: the fitted CDF has been pulled towards the data, so the statistic is stochastically smaller than under a fixed $F^0$ and the test rejects too rarely. But the statistic is again pivotal: with $Z_i=(X_i-\bar X_n)/\hat\sigma$, it equals $\sup_t|\tilde F_n(t)-\Phi(t)|$ for the empirical CDF $\tilde F_n$ of the $Z_i$, and the law of $(Z_1,\dots,Z_n)$ does not depend on $(\mu,\sigma^2)$. Its quantiles, computed once by simulating standard normal samples, give the *Kolmogorov–Lilliefors test*.

:::

::: {#def-qq-plot .definition name="Quantile–quantile plot"}

The *QQ plot* of a sample against a continuous, strictly increasing CDF $F$ is the set of points
$$\Bigl(F^{-1}\bigl(\tfrac in\bigr),\ X_{(i)}\Bigr),\qquad i=1,\dots,n-1,$$
comparing the quantiles of $F$ with the corresponding empirical quantiles, $F_n^{-1}(i/n):=X_{(i)}$. If the sample comes from $F$, the points lie near the line $y=x$; for a *normal QQ plot* ($F=\Phi$), data from $N(\mu,\sigma^2)$ lie near the line $y=\mu+\sigma x$. Plotting positions such as $(i-\tfrac12)/n$ are also used, so that the $n$th point can be included.

:::

::: {#rmk-reading-qq-plots .remark name="Reading a QQ plot"}

A QQ plot is an informal check, not a test. The shape of the departure from a straight line shows how the data differ from $F$. If the right end bends upwards and the left end downwards (an S lying on its side, steep at both ends), the data have *heavier tails* than $F$: extreme order statistics are further out than the reference quantiles. The opposite bend (flat at both ends) means *lighter tails*, as for uniform data against a normal. A curve that bends the same way at both ends, convex or concave, indicates *skewness*, for example exponential data against a normal.

:::

::: {#fig-goodness-of-fit-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0.000,0.000) rectangle (3.040,3.040);
\draw[faint, dashed] (0.000,0.000) -- (3.040,3.040);
\node[hollow dot] at (0.668,0.000) {};
\node[dot] at (0.843,0.501) {};
\node[dot] at (0.937,0.717) {};
\node[dot] at (1.005,0.848) {};
\node[dot] at (1.059,0.941) {};
\node[dot] at (1.105,1.014) {};
\node[dot] at (1.146,1.074) {};
\node[dot] at (1.183,1.125) {};
\node[dot] at (1.217,1.170) {};
\node[dot] at (1.249,1.210) {};
\node[dot] at (1.278,1.247) {};
\node[dot] at (1.307,1.282) {};
\node[dot] at (1.334,1.314) {};
\node[dot] at (1.361,1.344) {};
\node[dot] at (1.386,1.373) {};
\node[dot] at (1.411,1.401) {};
\node[dot] at (1.436,1.428) {};
\node[dot] at (1.460,1.455) {};
\node[dot] at (1.484,1.481) {};
\node[dot] at (1.508,1.507) {};
\node[dot] at (1.532,1.533) {};
\node[dot] at (1.556,1.559) {};
\node[dot] at (1.580,1.585) {};
\node[dot] at (1.604,1.612) {};
\node[dot] at (1.629,1.639) {};
\node[dot] at (1.654,1.667) {};
\node[dot] at (1.679,1.696) {};
\node[dot] at (1.706,1.726) {};
\node[dot] at (1.733,1.758) {};
\node[dot] at (1.762,1.793) {};
\node[dot] at (1.791,1.830) {};
\node[dot] at (1.823,1.870) {};
\node[dot] at (1.857,1.915) {};
\node[dot] at (1.894,1.966) {};
\node[dot] at (1.935,2.026) {};
\node[dot] at (1.981,2.099) {};
\node[dot] at (2.035,2.192) {};
\node[dot] at (2.103,2.323) {};
\node[dot] at (2.197,2.539) {};
\node[hollow dot] at (2.372,3.040) {};
\node[lab] at (1.52,3.34) {$t_3$: heavy tails};
\node[lab, tick] at (1.52,-0.3) {normal quantile};
\draw[faint] (4.000,0.000) rectangle (7.040,3.040);
\draw[faint, dashed] (4.000,0.000) -- (7.040,3.040);
\node[dot] at (4.668,1.145) {};
\node[dot] at (4.843,1.155) {};
\node[dot] at (4.937,1.165) {};
\node[dot] at (5.005,1.175) {};
\node[dot] at (5.059,1.185) {};
\node[dot] at (5.105,1.196) {};
\node[dot] at (5.146,1.207) {};
\node[dot] at (5.183,1.219) {};
\node[dot] at (5.217,1.231) {};
\node[dot] at (5.249,1.243) {};
\node[dot] at (5.278,1.256) {};
\node[dot] at (5.307,1.269) {};
\node[dot] at (5.334,1.282) {};
\node[dot] at (5.361,1.296) {};
\node[dot] at (5.386,1.311) {};
\node[dot] at (5.411,1.326) {};
\node[dot] at (5.436,1.342) {};
\node[dot] at (5.460,1.359) {};
\node[dot] at (5.484,1.376) {};
\node[dot] at (5.508,1.394) {};
\node[dot] at (5.532,1.413) {};
\node[dot] at (5.556,1.433) {};
\node[dot] at (5.580,1.454) {};
\node[dot] at (5.604,1.476) {};
\node[dot] at (5.629,1.500) {};
\node[dot] at (5.654,1.526) {};
\node[dot] at (5.679,1.553) {};
\node[dot] at (5.706,1.582) {};
\node[dot] at (5.733,1.614) {};
\node[dot] at (5.762,1.648) {};
\node[dot] at (5.791,1.686) {};
\node[dot] at (5.823,1.729) {};
\node[dot] at (5.857,1.776) {};
\node[dot] at (5.894,1.830) {};
\node[dot] at (5.935,1.894) {};
\node[dot] at (5.981,1.970) {};
\node[dot] at (6.035,2.066) {};
\node[dot] at (6.103,2.194) {};
\node[dot] at (6.197,2.388) {};
\node[dot] at (6.372,2.805) {};
\node[lab] at (5.52,3.34) {exponential: skewed};
\node[lab, tick] at (5.52,-0.3) {normal quantile};
\end{tikzpicture}
\end{center}
```

Normal QQ plots of the population quantiles of two distributions at $40$ plotting positions $(i-\tfrac12)/40$, against the line $y=x$ (dashed). Left: Student's $t_3$, steep at both ends (heavy tails); hollow dots are off the scale. Right: an exponential shifted to mean $0$, bent the same way at both ends (right skew).

:::
