---
title: "Pivotal Quantities and Exact Confidence Intervals"
sources: [camib-st-5, camib-sts-1-q5, camib-sts-1-q6]
requires: [math/probability/distributions/gamma-distribution, math/statistics/frequentist/confidence-intervals]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 5 and Example Sheet 1 (questions 5, 6), in our own wording; proofs written out in steps. The normal-data intervals and the duality with tests are in math/statistics/frequentist/confidence-intervals and are not repeated. -->

A confidence interval with exact coverage needs a random quantity whose law is known although $\theta$ is not. Such a quantity is called a pivot, and it gives a recipe that works whenever one can be found.

::: {#def-pivot .definition name="Pivotal quantity"}

A function $R(X,\theta)$ of the data and the parameter is a *pivotal quantity* (a *pivot*) if its distribution under $P_\theta$ does not depend on $\theta$.

:::

::: {#thm-pivot-recipe .theorem name="Recipe for a confidence interval"}

Let $R(X,\theta)$ be a pivot and $\alpha\in(0,1)$. Choose $c_1<c_2$ with $P(c_1\le R(X,\theta)\le c_2)=1-\alpha$ (for instance two quantiles of the pivot's law). If the inequalities $c_1\le R(x,\theta)\le c_2$ can be solved for $\theta$ as $L(x)\le\theta\le U(x)$, then $[L(X),U(X)]$ is a $(1-\alpha)$ confidence interval:
$$P_\theta\bigl(L(X)\le\theta\le U(X)\bigr)=1-\alpha\quad\text{for all }\theta .$$

:::

::: {.proof}

The event $\{c_1\le R(X,\theta)\le c_2\}$ is by construction the same event as $\{L(X)\le\theta\le U(X)\}$. The pivot's law is the same for every $\theta$, so the probability of this event is $1-\alpha$ for every $\theta$.

:::

::: {#exm-pivot-normal-mean .example name="The normal location problem"}

For $X_1,\dots,X_n$ iid $N(\theta,1)$, $R=\sqrt n(\bar X-\theta)\sim N(0,1)$ is a pivot. Splitting $\alpha=\alpha_1+\alpha_2$ with $P(Z>z_{\alpha})=\alpha$, the interval $[\bar X-z_{\alpha_1}/\sqrt n,\ \bar X+z_{\alpha_2}/\sqrt n]$ has level $1-\alpha$. The equal split $\alpha_1=\alpha_2=\alpha/2$ gives the shortest interval centred at $\bar X$; for $\alpha=0.05$, $z_{\alpha/2}\approx1.96$.

:::

::: {#prp-interval-monotone .proposition name="Monotone transformations of an interval"}

If $[L(X),U(X)]$ is a $(1-\alpha)$ confidence interval for $\theta$ and $h$ is increasing on $\Theta$, then $[h(L(X)),h(U(X))]$ is a $(1-\alpha)$ confidence interval for $h(\theta)$.

:::

::: {.proof}

Since $h$ is increasing, $L\le\theta\le U$ if and only if $h(L)\le h(\theta)\le h(U)$, so the two events coincide and have probability $1-\alpha$.

:::

::: {#exm-pivot-uniform .example name="One-sided interval for the endpoint of a uniform distribution"}

Let $X_1,\dots,X_n$ be iid $\mathrm{Unif}[0,\theta]$, with maximum likelihood estimator $\hat\theta=\max_iX_i$.

1. For $0\le s\le1$, $P(\hat\theta/\theta\le s)=P(X_1\le s\theta)^n=s^n$; this does not depend on $\theta$, so $\hat\theta/\theta$ is a pivot.

2. Choose $c=\alpha^{1/n}$, so that $P(\hat\theta/\theta\le c)=\alpha$. Then $P(c\le\hat\theta/\theta\le1)=1-\alpha$.

3. Solving $c\le\hat\theta/\theta\le1$ for $\theta$ gives the interval $\bigl[\hat\theta,\ \alpha^{-1/n}\hat\theta\bigr]$, a $100(1-\alpha)\%$ interval whose lower end is the observed maximum (which $\theta$ cannot be below).

:::

::: {#fig-pivotal-quantities-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=6cm,y=1.2cm]
\draw[->, muted] (0,0) -- (1.1,0) node[lab, right] {$s$};
\draw[->, muted] (0,0) -- (0,2.4);
\foreach \x in {0.5,1} \node[tick, below] at (\x,0) {$\x$};
\node[tick, left] at (0,2) {$1$};
\draw[emph, primary, domain=0:1, samples=60] plot (\x,{2*\x^5});
\draw[faint] (0.8,0) -- (0.8,{2*0.8^5});
\draw[hl] (0.8,0) -- (1,0);
\fill[hl, opacity=0.3] (0.8,0) -- (1,0) -- (1,2) -- (0.8,0.655) -- cycle;
\node[lab] at (0.5,2.2) {CDF of $\hat\theta/\theta$ for $n=5$};
\node[lab, below] at (0.9,-0.35) {$c=\alpha^{1/n}$};
\end{tikzpicture}
\end{center}
```

The distribution function $s^n$ of the pivot $\hat\theta/\theta$ for $n=5$. The shaded region marks the range $c\le\hat\theta/\theta\le1$, which has probability $1-\alpha$.

:::

::: {#exm-pivot-exponential .example name="Exponential data"}

Let $X_1,\dots,X_n$ be iid $\mathrm{Exp}(\theta)$ with rate $\theta$.

1. By @thm-gamma-additivity $\sum_iX_i\sim\mathrm{Gamma}(n,\theta)$, and by scaling (@prp-gamma-properties) $\theta\sum_iX_i\sim\mathrm{Gamma}(n,1)$. So $R=\theta\sum_iX_i$ is a pivot.

2. With $g_{\beta}$ the $\beta$ quantile of $\mathrm{Gamma}(n,1)$, the interval $\bigl[g_{\alpha/2}/\sum X_i,\ g_{1-\alpha/2}/\sum X_i\bigr]$ has level $1-\alpha$.

3. For $n=5$, $\sum x_i=10$ and $\alpha=0.1$ the quantiles are $g_{0.05}=1.970$ and $g_{0.95}=9.154$, giving the $90\%$ interval $[0.197,\,0.915]$ for $\theta$.

:::

::: {#exm-confidence-sets-shapes .example name="Two confidence sets for a plane parameter"}

Let $X_1\sim N(\theta_1,1)$ and $X_2\sim N(\theta_2,1)$ be independent. The pivots are $Z_1=X_1-\theta_1$ and $Z_2=X_2-\theta_2$, independent standard normals, and two regions of $(Z_1,Z_2)$ with probability $0.95$ give two confidence sets for $(\theta_1,\theta_2)$:

1. the square $|Z_1|\le\sqrt5,\ |Z_2|\le\sqrt5$ has probability $\bigl(2\Phi(\sqrt5)-1\bigr)^2=0.9499\approx0.95$;

2. the disc $Z_1^2+Z_2^2\le5.991$ has probability $0.95$, as $Z_1^2+Z_2^2\sim\chi^2_2$ and $5.991$ is its $95\%$ quantile.

Both have the same coverage, so the level does not decide between them. A natural further criterion is size: the square has area $4\cdot5=20$ and the disc $\pi\cdot5.991\approx18.8$, so the disc is smaller.

:::
