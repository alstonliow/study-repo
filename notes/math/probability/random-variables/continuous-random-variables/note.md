---
title: "Continuous Random Variables"
sources: [cs70-20.1, cs70-20.2, mit1805-6]
requires: [math/probability/random-variables/expectation-and-variance]
aliases: [math/probability/continuous/continuous-random-variables]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 20 (cs70-20.1, cs70-20.2), in our own wording; proofs written out in steps. -->

## Probability on an interval

A pointer that stops at a uniformly random point of $[0,\ell]$ cannot give each point a positive probability: infinitely many equal positive numbers do not sum to $1$. So every single point has probability $0$, and probabilities are given to intervals instead. Uniformity means that the probability of an interval is proportional to its length:
$$\Pr([a,b])=\frac{b-a}{\ell}\qquad(0\le a\le b\le\ell).$$
A finite or countable union of disjoint intervals gets the sum of their probabilities, as in the discrete case. For example, the pointer lands in the first or the third quarter of the wheel with probability $\frac14+\frac14=\frac12$.

::: {#rmk-continuous-random-variables-measure}

Which subsets of $\mathbb R$ can be given a probability at all is the subject of measure theory. Unions of intervals are all we need here.

:::

## Densities

::: {#def-probability-density .definition name="Probability density function"}

A *probability density function* (p.d.f.) is a function $f:\mathbb R\to\mathbb R$ with $f(x)\ge0$ for all $x$ and $\int_{-\infty}^{\infty}f(x)\,dx=1$. A random variable $X$ has density $f$ (and is called *continuous*) if
$$\Pr(a\le X\le b)=\int_a^b f(x)\,dx\qquad\text{for all }a\le b.$$

:::

::: {#fig-continuous-random-variables-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm,y=5cm]
\fill[shade, domain=1:2.5, samples=40] (1,0) -- plot (\x,{\x*exp(-\x)}) -- (2.5,0) -- cycle;
\draw[->, muted] (-0.2,0) -- (5.3,0) node[lab, right] {$x$};
\draw[->, muted] (0,-0.03) -- (0,0.5);
\draw[emph, primary, domain=0:5, samples=80] plot (\x,{\x*exp(-\x)});
\node[tick, below] at (1,0) {$a$}; \node[tick, below] at (2.5,0) {$b$};
\node[lab, primary] at (0.8,0.43) {$f$};
\node[lab] at (3.6,0.3) {area $=\Pr(a\le X\le b)$};
\draw[muted] (3.0,0.27) -- (1.9,0.12);
\end{tikzpicture}
\end{center}
```

A probability is an area under the density: $\Pr(a\le X\le b)=\int_a^bf(x)\,dx$. The total area under $f$ is $1$.

:::

::: {#rmk-continuous-random-variables-density}

1. Taking $a=b$ gives $\Pr(X=a)=0$, so it does not matter whether the endpoints are included: $\Pr(a<X<b)=\Pr(a\le X\le b)$.

2. $f(x)$ is not a probability and may exceed $1$. For small $dx$, $\Pr(x\le X\le x+dx)\approx f(x)\,dx$, so $f(x)$ is the *probability per unit length* near $x$.

:::

::: {#def-cumulative-distribution-function .definition name="Cumulative distribution function"}

The *cumulative distribution function* (c.d.f.) of $X$ is $F(x)=\Pr(X\le x)$. If $X$ has density $f$, then
$$F(x)=\int_{-\infty}^x f(z)\,dz,$$
and, by the fundamental theorem of calculus, $F'(x)=f(x)$ at every point where $f$ is continuous.

:::

::: {#fig-continuous-random-variables-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.4,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {};
\draw[emph, domain=0:5.2, samples=80, smooth, variable=\x] plot ({\x}, {3.2*\x*exp(-\x)});
\draw[hl, domain=0:5.2, samples=80, smooth, variable=\x] plot ({\x}, {2*(1-exp(-\x)*(1+\x))});
\node[tick] at (1.0,1.55) {$f(x)$};
\node[tick, text=accent] at (4.6,2.25) {$F(x)$};
\draw (0,2) -- (-0.08,2) node[tick, left] {$1$};
\draw[faint, dashed] (0,2) -- (5.2,2);
\end{tikzpicture}
\end{center}
```

A density $f$ and its distribution function $F(x)=\int_{-\infty}^xf(t)\,dt$. $F$ rises fastest where $f$ is largest and levels off at $1$

:::

::: {#def-continuous-expectation .definition name="Expectation and variance"}

If $X$ has density $f$, its *expectation* and *variance* are
$$E[X]=\int_{-\infty}^{\infty}x f(x)\,dx,\qquad \mathrm{Var}(X)=E\bigl[(X-E[X])^2\bigr]=\int_{-\infty}^{\infty}x^2f(x)\,dx-E[X]^2,$$
when the integrals converge. More generally $E[g(X)]=\int_{-\infty}^{\infty}g(x)f(x)\,dx$. The integral replaces the sum in @def-expectation, and linearity (@thm-linearity-of-expectation) and the rules for $\mathrm{Var}(aX+b)$ hold as before.

:::

::: {#def-continuous-uniform-distribution .definition name="Uniform distribution on an interval"}

$X$ is *uniform* on $[a,b]$ ($a<b$), written $X\sim U[a,b]$, if it has density $f(x)=\frac1{b-a}$ for $a\le x\le b$ and $f(x)=0$ otherwise.

:::

::: {#prp-continuous-uniform-mean-variance .proposition name="Mean and variance of the uniform distribution"}

If $X\sim U[0,\ell]$, then $E[X]=\dfrac\ell2$ and $\mathrm{Var}(X)=\dfrac{\ell^2}{12}$.

:::

::: {.proof}

1. $f$ is a density: $f\ge0$ and $\int_0^\ell\frac1\ell\,dx=1$.

2. $E[X]=\int_0^\ell \frac x\ell\,dx=\frac1\ell\cdot\frac{\ell^2}2=\frac\ell2$.

3. $E[X^2]=\int_0^\ell\frac{x^2}\ell\,dx=\frac{\ell^2}3$, so $\mathrm{Var}(X)=\frac{\ell^2}3-\frac{\ell^2}4=\frac{\ell^2}{12}$.

:::

::: {#fig-continuous-random-variables-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1.6cm]
\begin{scope}
\draw[->, muted] (-0.8,0) -- (3.6,0) node[lab, right] {$x$};
\draw[->, muted] (0,-0.1) -- (0,1.4);
\draw[emph, primary] (-0.8,0) -- (0,0); \draw[emph, primary] (0,1) -- (2.5,1); \draw[emph, primary] (2.5,0) -- (3.4,0);
\draw[faint, dashed] (2.5,0) -- (2.5,1);
\node[tick, below] at (2.5,0) {$\ell$}; \node[tick, left] at (0,1) {$\frac1\ell$};
\node[lab] at (1.25,1.3) {density $f$};
\end{scope}
\begin{scope}[xshift=5cm]
\draw[->, muted] (-0.8,0) -- (3.6,0) node[lab, right] {$x$};
\draw[->, muted] (0,-0.1) -- (0,1.4);
\draw[emph, primary] (-0.8,0) -- (0,0) -- (2.5,1) -- (3.4,1);
\draw[faint, dashed] (2.5,0) -- (2.5,1);
\node[tick, below] at (2.5,0) {$\ell$}; \node[tick, left] at (0,1) {$1$};
\node[lab] at (1.25,1.3) {c.d.f. $F$};
\end{scope}
\end{tikzpicture}
\end{center}
```

The uniform distribution on $[0,\ell]$: its density is constant on $[0,\ell]$, and its c.d.f. rises linearly from $0$ to $1$ there.

:::

## Several continuous random variables

::: {#def-joint-density .definition name="Joint density"}

A *joint density* is a function $f:\mathbb R^2\to\mathbb R$ with $f\ge0$ and $\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x,y)\,dx\,dy=1$. Random variables $X,Y$ have joint density $f$ if
$$\Pr(a\le X\le b,\ c\le Y\le d)=\int_c^d\int_a^b f(x,y)\,dx\,dy\qquad\text{for all }a\le b,\ c\le d.$$
Then $f(x,y)\,dx\,dy$ is approximately the probability of the small rectangle $[x,x+dx]\times[y,y+dy]$, and $\Pr((X,Y)\in A)=\iint_A f$ for regions $A$ built from rectangles.

:::

::: {#def-continuous-independence .definition name="Independent continuous random variables"}

Continuous random variables $X,Y$ are *independent* if for all $a\le b$ and $c\le d$,
$$\Pr(a\le X\le b,\ c\le Y\le d)=\Pr(a\le X\le b)\Pr(c\le Y\le d).$$

:::

::: {#thm-independent-joint-density .theorem name="Joint density of independent variables"}

If $X$ and $Y$ are independent with densities $f_X$ and $f_Y$, then $f(x,y)=f_X(x)f_Y(y)$ is a joint density of $X$ and $Y$.

:::

::: {.proof}

1. $f\ge0$, since $f_X,f_Y\ge0$.

2. For a product of a function of $x$ and a function of $y$, the double integral over a rectangle splits into a product (Fubini):
   $$\int_c^d\int_a^b f_X(x)f_Y(y)\,dx\,dy=\int_a^b f_X(x)\,dx\cdot\int_c^d f_Y(y)\,dy.$$

3. The right side is $\Pr(a\le X\le b)\Pr(c\le Y\le d)$, which equals $\Pr(a\le X\le b,\ c\le Y\le d)$ by independence. Letting $a,c\to-\infty$ and $b,d\to\infty$ also gives total integral $1$.

4. So $f$ gives every rectangle its correct probability, as @def-joint-density requires.

:::

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Class 6, in our own wording. -->

::: {#def-quantile .definition name="Quantile, median"}

Let $X$ have a continuous, strictly increasing c.d.f. $F$ on the interval where its density is positive, and let $0<p<1$. The *$p$-quantile* of $X$ is the number $q_p$ with
$$F(q_p)=\Pr(X\le q_p)=p .$$
The $0.5$-quantile is the *median*; $q_{0.25}$ and $q_{0.75}$ are the *quartiles*. For a general c.d.f. one takes $q_p=\min\{x:F(x)\ge p\}$.

:::

::: {#fig-continuous-random-variables-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.4,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,2.4) node[lab, above] {$F(x)$};
\draw[emph, domain=0:5.2, samples=80, smooth, variable=\x] plot ({\x}, {2*(1-exp(-\x)*(1+\x))});
\draw[faint, dashed] (0,2) -- (5.2,2);
\draw[hl, ->] (0,1.5) -- (2.674,1.5) -- (2.674,0);
\draw (0,1.5) -- (-0.08,1.5) node[tick, left] {$u$};
\draw (0,2) -- (-0.08,2) node[tick, left] {$1$};
\draw (2.674,0) -- (2.674,-0.08) node[tick, below] {$F^{-1}(u)$};
\end{tikzpicture}
\end{center}
```

The $u$-quantile is read off the distribution function: go across from height $u$ to the curve, then down to the axis

:::

::: {#exm-quantiles .example name="Quantiles of two distributions"}

1. For $X\sim\operatorname{Exp}(\lambda)$, $F(x)=1-e^{-\lambda x}$, so $q_p=-\ln(1-p)/\lambda$; the median is $\ln2/\lambda\approx0.693/\lambda$, below the mean $1/\lambda$.

2. For the standard normal $Z$, $q_{0.9}\approx1.28$, $q_{0.95}\approx1.645$ and $q_{0.975}\approx1.96$. By symmetry $q_{1-p}=-q_p$, so $\Pr(-1.96\le Z\le1.96)\approx0.95$.

:::
