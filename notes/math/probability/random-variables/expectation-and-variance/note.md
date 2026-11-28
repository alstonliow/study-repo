---
title: "Expectation, Median, Mode and Variance"
sources: [fit1058-cn-10.3, fit1058-cn-10.4, fit1058-cn-10.5, fit1058-cn-10.6]
requires: [math/probability/random-variables/random-variables]
aliases: [math/probability/expectation-and-variance, math/probability/discrete/expectation-and-variance]   # old ids (moved)
status: draft
---

<!-- Migrated from 1058note notes/chapters/09-probability.tex: Expectation; Median; Mode; Variance. -->

## Expectation

::: {#def-expectation .definition name="Expectation"}

The *expectation* (or *expected value*, or *mean*) of $X$ is
$$E[X] = \sum_{u\in U} X(u)\Pr(u) = \sum_k k\cdot\Pr(X=k).$$

:::

::: {#exm-expectation-and-variance-1 .example}

For one fair die, $E[X]=(1+2+3+4+5+6)/6=21/6=3.5$. The expectation need not be a possible value of $X$.

:::

::: {#fig-expectation-and-variance-1}

```{=latex}
\begin{tikzpicture}[x=0.8cm, y=8cm]
  \draw (0.4,0) -- (6.6,0);
  \foreach \k in {1,...,6} {
    \fill[primaryStrong] (\k-0.3,0) rectangle (\k+0.3,1/6);
    \node[below, tick] at (\k,-0.012) {$\k$};
  }
  \filldraw[fill=accent, draw=accent] (3.5,-0.005) -- (3.2,-0.07) -- (3.8,-0.07) -- cycle;
  \node[text=accent, lbl, anchor=north] at (3.5,-0.075) {$E[X]=3.5$};
\end{tikzpicture}
```

The distribution of one fair die balances at its mean $E[X]=3.5$, even though $3.5$ is not a possible value

:::

::: {#thm-linearity-of-expectation .theorem name="Linearity of expectation"}

For any random variables $X,Y$ and constants $a,b$,
$$E[aX+b] = aE[X]+b, \qquad E[X+Y] = E[X]+E[Y].$$

:::

::: {.proof}

$E[X+Y] = \sum_{u}(X(u)+Y(u))\Pr(u) = \sum_u X(u)\Pr(u) + \sum_u Y(u)\Pr(u) = E[X]+E[Y]$. The first identity is proved the same way.

:::

::: {#rmk-expectation-and-variance-1 .remark name="No independence required"}

Linearity holds for *any* $X,Y$: the proof never uses independence. For example, the expected total of two dice is $3.5+3.5=7$.

:::

<!-- Added 2026-11-15 from CN §10.3 (own wording and proof). -->

::: {#thm-expectation-of-product .theorem name="Expectation of an independent product"}

If $X$ and $Y$ are independent (@def-independent-random-variables), then
$$E[XY] = E[X]\,E[Y].$$

:::

::: {.proof}

1. By the definition of expectation, $E[XY] = \sum_{r}\sum_{s} rs\,\Pr(X=r, Y=s)$, summing over all values $r$ of $X$ and $s$ of $Y$.

2. By independence, $\Pr(X=r, Y=s) = \Pr(X=r)\Pr(Y=s)$.

3. So the double sum factorises:
$$E[XY] = \left(\sum_r r\Pr(X=r)\right)\left(\sum_s s\Pr(Y=s)\right) = E[X]\,E[Y].$$

:::

::: {#rmk-expectation-and-variance-2 .remark name="Independence is needed here"}

Unlike linearity, this can fail without independence. If $X$ is $\pm1$ with probability $\frac12$ each and $Y = X$, then $E[XY] = E[X^2] = 1$, but $E[X]E[Y] = 0$.

:::

## Median

::: {#def-median .definition name="Median"}

$m$ is a *median* of $X$ if $\Pr(X\le m)\ge\tfrac12$ and $\Pr(X\ge m)\ge\tfrac12$.

:::

::: {#exm-expectation-and-variance-1-2 .example}

For one die, every $m$ between $3$ and $4$ satisfies the definition; when the median falls in a gap like this we take the middle, $3.5$. For the points $X$ on a random Scrabble tile, $\Pr(X=0)=0.02$, $\Pr(X=1)=0.68$, $\Pr(X\ge2)=0.3$, so $\Pr(X\le1)=0.7$ and $\Pr(X\ge1)=0.98$, and the median is $1$.

:::

::: {#rmk-expectation-and-variance-3 .remark name="Median vs.\ mean"}

The median is less affected by rare extreme values. For a lottery ticket, the prize money has median $0$, even though a huge but very unlikely prize can make the mean much larger.

:::

## Mode

::: {#def-mode .definition name="Mode"}

A *mode* of $X$ is a value $k$ that maximises $\Pr(X=k)$.

:::

::: {#fig-expectation-and-variance-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.0,0) node[lab, right] {$k$};
\draw[->] (0,0) -- (0,2.2) node[lab, above] {$\Pr(X=k)$};
\path[bar] (0.150,0) rectangle (0.650,0.600);
\node[tick, below] at (0.400,0) {$0$};
\path[hl cell] (0.950,0) rectangle (1.450,1.800);
\node[tick, below] at (1.200,0) {$1$};
\path[bar] (1.750,0) rectangle (2.250,1.500);
\node[tick, below] at (2.000,0) {$2$};
\path[bar] (2.550,0) rectangle (3.050,0.900);
\node[tick, below] at (2.800,0) {$3$};
\path[bar] (3.350,0) rectangle (3.850,0.600);
\node[tick, below] at (3.600,0) {$4$};
\path[bar] (4.150,0) rectangle (4.650,0.360);
\node[tick, below] at (4.400,0) {$5$};
\path[bar] (4.950,0) rectangle (5.450,0.240);
\node[tick, below] at (5.200,0) {$6$};
\draw[hl] (2.15,0) -- (2.15,-0.5) node[lab, below] {mean $2.19$};
\node[lab, above] at (1.2,1.80) {mode};
\node[lab, right] at (2.0,1.95) {median $2$};
\draw[faint, dashed] (2.0,0) -- (2.0,1.95);
\end{tikzpicture}
\end{center}
```

A right-skewed distribution: the mode is $1$, the median is $2$ (half the mass is at or below it), and the long right tail pulls the mean to about $2.2$

:::

::: {#exm-expectation-and-variance-1-3 .example}

The total of two dice has mode $7$. A fair die has every value $1,\dots,6$ as a mode, so a mode need not be unique.

:::

## Variance

<!-- Added 2026-11-15 from CN §10.6 (own wording). -->

::: {#rmk-expectation-and-variance-4 .remark name="Measuring spread"}

To measure how far $X$ typically is from $\mu = E[X]$, the plain average $E[X-\mu]$ is useless: it is always $E[X]-\mu = 0$, because positive and negative deviations cancel. The *mean absolute deviation* $E\big[|X-\mu|\big]$ avoids this and is in the units of $X$, but it has weaker mathematical properties. The variance squares the deviations instead.

:::

::: {#def-variance-standard-deviation .definition name="Variance, standard deviation"}

With $\mu=E[X]$, the *variance* of $X$ is $\mathrm{Var}(X) = E\big[(X-\mu)^2\big]$, and the *standard deviation* is $\sigma_X = \sqrt{\mathrm{Var}(X)}$.

:::

::: {#fig-expectation-and-variance-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[xshift=0.0cm]
\draw[->] (0,0) -- (3.4,0) node[lab, right] {};
\path[bar] (0.075,0) rectangle (0.525,0.000);
\node[tick, below] at (0.300,0) {$0$};
\path[bar] (0.775,0) rectangle (1.225,0.200);
\node[tick, below] at (1.000,0) {$1$};
\path[bar] (1.475,0) rectangle (1.925,1.600);
\node[tick, below] at (1.700,0) {$2$};
\path[bar] (2.175,0) rectangle (2.625,0.200);
\node[tick, below] at (2.400,0) {$3$};
\path[bar] (2.875,0) rectangle (3.325,0.000);
\node[tick, below] at (3.100,0) {$4$};
\draw[hl] (1.7,0) -- (1.7,1.8);
\node[lab] at (1.7,2.1) {small variance};
\end{scope}
\begin{scope}[xshift=4.2cm]
\draw[->] (0,0) -- (3.4,0) node[lab, right] {};
\path[bar] (0.075,0) rectangle (0.525,0.400);
\node[tick, below] at (0.300,0) {$0$};
\path[bar] (0.775,0) rectangle (1.225,0.400);
\node[tick, below] at (1.000,0) {$1$};
\path[bar] (1.475,0) rectangle (1.925,0.400);
\node[tick, below] at (1.700,0) {$2$};
\path[bar] (2.175,0) rectangle (2.625,0.400);
\node[tick, below] at (2.400,0) {$3$};
\path[bar] (2.875,0) rectangle (3.325,0.400);
\node[tick, below] at (3.100,0) {$4$};
\draw[hl] (1.7,0) -- (1.7,1.8);
\node[lab] at (1.7,2.1) {large variance};
\end{scope}
\end{tikzpicture}
\end{center}
```

Two distributions with the same mean $2$ (vertical line). The variance measures the spread around it: $0.2$ on the left, $2$ on the right

:::

::: {#rmk-expectation-and-variance-5 .remark name="Units"}

The variance is in the square of the units of $X$; the standard deviation is back in the units of $X$, which makes it easier to interpret as a typical distance from the mean.

:::

::: {#prp-expectation-and-variance-1 .proposition}

$\mathrm{Var}(X) = E[X^2] - E[X]^2$.

:::

::: {.proof}

Let $\mu=E[X]$. By linearity, $E[(X-\mu)^2] = E[X^2]-2\mu E[X]+\mu^2 = E[X^2]-\mu^2$.

:::

::: {#exm-expectation-and-variance-1-4 .example}

For one die, $E[X^2]=(1+4+9+16+25+36)/6=91/6$, so $\mathrm{Var}(X)=\frac{91}6-3.5^2=\frac{35}{12}\approx2.92$ and $\sigma_X\approx1.71$.

:::

::: {#thm-variance-of-an-independent-sum .theorem name="Variance of an independent sum"}

If $X,Y$ are independent, then $\mathrm{Var}(X+Y) = \mathrm{Var}(X)+\mathrm{Var}(Y)$.

:::

::: {.proof}

First, independence gives $E[XY]=E[X]E[Y]$: in $E[XY]=\sum_{r,s}rs\Pr(X=r,Y=s)$, replace $\Pr(X=r,Y=s)$ by $\Pr(X=r)\Pr(Y=s)$ and factor the double sum. Then
$$\mathrm{Var}(X+Y) = E[X^2]+2E[XY]+E[Y^2] - (E[X]+E[Y])^2 = \big(E[X^2]-E[X]^2\big)+\big(E[Y^2]-E[Y]^2\big).$$

:::

::: {#exm-expectation-and-variance-2 .example}

The total of two dice has variance $\frac{35}{12}+\frac{35}{12}=\frac{35}6$.

:::

::: {#thm-chebyshev-s-inequality .theorem name="Chebyshev's inequality"}

For any $a>0$,  $\Pr\big(|X-E[X]|\ge a\big) \le \dfrac{\mathrm{Var}(X)}{a^2}$.

:::

::: {.proof}

Let $\mu=E[X]$. Dropping the terms with $|k-\mu|<a$, and then using $(k-\mu)^2\ge a^2$ in the rest,
$$\mathrm{Var}(X) = \sum_k (k-\mu)^2\Pr(X=k) \ge \sum_{k:\,|k-\mu|\ge a} (k-\mu)^2\Pr(X=k) \ge a^2\Pr(|X-\mu|\ge a).$$
Divide by $a^2$.

:::

::: {#fig-expectation-and-variance-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.4,0) node[lab, right] {$x$};
\draw[emph, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {4.6*exp(-((\x-3.5)^2)/(2*1^2))/(1*sqrt(2*pi))});
\fill[shade, domain=0:1.5, variable=\x] (0,0) -- plot ({\x}, {4.6*exp(-((\x-3.5)^2)/(2*1^2))/(1*sqrt(2*pi))}) -- (1.5,0) -- cycle;
\fill[shade, domain=5.5:7, variable=\x] (5.5,0) -- plot ({\x}, {4.6*exp(-((\x-3.5)^2)/(2*1^2))/(1*sqrt(2*pi))}) -- (7,0) -- cycle;
\draw (1.5,0) -- (1.5,-0.08) node[tick, below] {$\mu-k\sigma$};
\draw (3.5,0) -- (3.5,-0.08) node[tick, below] {$\mu$};
\draw (5.5,0) -- (5.5,-0.08) node[tick, below] {$\mu+k\sigma$};
\draw[<->] (1.5,2.0) -- node[lab, above] {within $k\sigma$} (5.5,2.0);
\end{tikzpicture}
\end{center}
```

Chebyshev's inequality bounds the shaded mass beyond $k$ standard deviations from the mean by $1/k^2$, whatever the shape of the distribution

:::

::: {#rmk-expectation-and-variance-6 .remark name="Any distribution"}

Chebyshev’s inequality holds for every distribution, with no assumption about its shape. Taking $a=c\sigma$ gives $\Pr(|X-\mu|\ge c\sigma)\le1/c^2$: e.g. at most $\frac14$ of the probability lies two or more standard deviations from the mean.

:::
