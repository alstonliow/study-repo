---
title: "Derived Distributions"
sources: [mit6041-10, mit6041-11]
requires: [math/probability/continuous/joint-distributions]
status: draft
---

<!-- Added 2026-11-20 from MIT 6.041 (Fall 2010), Lectures 10 and 11, in our own wording; proofs written out in steps. -->

A *derived distribution* is the distribution of $Y=g(X)$ when the distribution of $X$ is known. For a discrete $X$ simply add up: $p_Y(y)=\sum_{x:\,g(x)=y}p_X(x)$. For a continuous $X$ work through the CDF.

::: {#rmk-derived-distributions-cdf-method .remark name="The CDF method"}

To find the density of $Y=g(X)$:

1. compute $F_Y(y)=\Pr(g(X)\le y)$ by integrating $f_X$ over the set $\{x:g(x)\le y\}$;
2. differentiate: $f_Y(y)=F_Y'(y)$.

It works for any $g$, monotone or not, and also for functions of several variables.

:::

::: {#exm-derived-square .example name="Square of a random variable"}

Let $Y=X^2$ with $X$ continuous. For $y>0$,
$$F_Y(y)=\Pr(-\sqrt y\le X\le\sqrt y)=F_X(\sqrt y)-F_X(-\sqrt y),$$
so
$$f_Y(y)=\frac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y},\qquad y>0.$$
For $X$ uniform on $[-1,1]$ this gives $f_Y(y)=\frac1{2\sqrt y}$ on $(0,1]$.

:::

::: {#fig-derived-distributions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.8,0) node[lab, right] {$y$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$f_Y(y)$};
\draw[emph, domain=0.15:4.0, samples=80, smooth, variable=\x] plot ({\x}, {0.5/sqrt(\x/4)/2});
\draw[faint, dashed] (0,0.5) -- (4,0.5);
\draw (4,0) -- (4,-0.08) node[tick, below] {$1$};
\draw (0,0.5) -- (-0.08,0.5) node[tick, left] {$\tfrac12$};
\end{tikzpicture}
\end{center}
```

For $X$ uniform on $[0,1]$ the formula of @exm-derived-square gives $f_Y(y)=\frac1{2\sqrt y}$ on $(0,1]$: squaring crowds values towards $0$, and the density blows up there

:::

::: {#thm-derived-density-monotone .theorem name="Density of a monotone function"}

Let $X$ have density $f_X$, and let $g$ be strictly monotone and differentiable on an interval containing the values of $X$, with inverse $h=g^{-1}$. Then $Y=g(X)$ has density
$$f_Y(y)=f_X\bigl(h(y)\bigr)\,\lvert h'(y)\rvert$$
for $y$ in the range of $g$, and $f_Y(y)=0$ elsewhere.

:::

::: {.proof}

1. Suppose $g$ is increasing. Then $g(X)\le y$ exactly when $X\le h(y)$, so $F_Y(y)=F_X(h(y))$.

2. Differentiate with the chain rule: $f_Y(y)=f_X(h(y))\,h'(y)$, and $h'(y)\ge0$.

3. Suppose $g$ is decreasing. Then $g(X)\le y$ exactly when $X\ge h(y)$, so $F_Y(y)=1-F_X(h(y))$.

4. Differentiating gives $f_Y(y)=-f_X(h(y))\,h'(y)$, and now $h'(y)\le0$. Both cases read $f_X(h(y))\lvert h'(y)\rvert$.

:::

::: {#fig-derived-distributions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,3.4) node[lab, above] {$y$};
\draw[emph, domain=0:4.3, samples=80, smooth, variable=\x] plot ({\x}, {0.2+0.55*\x+0.08*\x*\x});
\path[shade] (2.0,0) rectangle (2.4,1.620);
\path[hl cell] (0,1.620) rectangle (2.0,1.981);
\draw[faint, dashed] (2.4,0) -- (2.4,1.981) -- (0,1.981);
\draw (2.2,0) -- (2.2,-0.08) node[tick, below] {$dx$};
\draw (0,1.8004) -- (-0.08,1.8004) node[tick, left] {$dy$};
\node[tick] at (3.7,3.0) {$y=g(x)$};
\end{tikzpicture}
\end{center}
```

A monotone $g$ maps a short interval of length $dx$ onto one of length $dy\approx|g'(x)|\,dx$ with the same probability, so $f_Y(y)=f_X(x)/|g'(x)|$

:::

::: {#exm-derived-linear .example name="Linear functions" related="lem-normal-standardize"}

For $Y=aX+b$ with $a\ne0$, $h(y)=(y-b)/a$ and
$$f_Y(y)=\frac1{\lvert a\rvert}\,f_X\Bigl(\frac{y-b}a\Bigr).$$
In particular a linear function of a normal random variable is normal. If $X\sim\operatorname{Exp}(\lambda)$ and $a>0$, then $aX\sim\operatorname{Exp}(\lambda/a)$.

:::

::: {#thm-convolution-density .theorem name="Density of a sum of independent variables" related="thm-convolution-rule"}

If $X$ and $Y$ are independent with densities $f_X$ and $f_Y$, then $Z=X+Y$ has the *convolution*
$$f_Z(z)=\int_{-\infty}^{\infty}f_X(x)\,f_Y(z-x)\,dx.$$

:::

::: {.proof}

1. Condition on $X=x$. By independence, $Z=x+Y$ given $X=x$ has CDF $\Pr(Y\le z-x)=F_Y(z-x)$.

2. By the law of total probability for densities, $F_Z(z)=\int f_X(x)F_Y(z-x)\,dx$.

3. Differentiate under the integral sign in $z$: $f_Z(z)=\int f_X(x)f_Y(z-x)\,dx$.

:::

The discrete version is the same formula with sums: $p_Z(z)=\sum_xp_X(x)p_Y(z-x)$.

::: {#exm-sum-of-uniforms .example name="Sum of two uniforms"}

Let $X,Y$ be independent and uniform on $[0,1]$. The integrand $f_X(x)f_Y(z-x)$ is $1$ when $0\le x\le1$ and $0\le z-x\le1$, so $f_Z(z)$ is the length of $[\max(0,z-1),\min(1,z)]$:
$$f_Z(z)=\begin{cases}z,&0\le z\le1,\\2-z,&1\le z\le2,\\0,&\text{otherwise,}\end{cases}$$
a triangle (@fig-derived-distributions-1).

:::

::: {#fig-derived-distributions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.6]
\draw[->] (-0.3,0) -- (2.5,0) node[lab, right] {$z$};
\draw[->] (0,-0.1) -- (0,1.3) node[lab, above] {$f_Z(z)$};
\draw[emph, primary] (-0.3,0) -- (0,0) -- (1,1) -- (2,0) -- (2.4,0);
\draw[faint, dashed] (1,0) -- (1,1) -- (0,1);
\node[lab, below] at (1,0) {$1$};
\node[lab, below] at (2,0) {$2$};
\node[lab, left] at (0,1) {$1$};
\end{tikzpicture}
\end{center}
```

The density of the sum of two independent uniforms on $[0,1]$.

:::
