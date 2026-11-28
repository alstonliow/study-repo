---
title: "Iterated Expectations and Random Sums"
sources: [mit6041-12]
requires: [math/probability/joint-distributions/transforms]
aliases: [math/probability/continuous/iterated-expectations]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-20 from MIT 6.041 (Fall 2010), Lecture 12, in our own wording; proofs written out in steps. -->

The conditional expectation given an event (@def-conditional-expectation) becomes a random variable once the event is "$Y$ takes its observed value".

::: {#def-conditional-expectation-random-variable .definition name="Conditional expectation and variance given a random variable"}

For random variables $X$ and $Y$ let $g(y)=E[X\mid Y=y]$. The *conditional expectation of $X$ given $Y$* is the random variable
$$E[X\mid Y]=g(Y).$$
Likewise $\mathrm{Var}(X\mid Y)$ is the random variable $v(Y)$, where $v(y)=E\bigl[(X-g(y))^2\mid Y=y\bigr]$.

:::

::: {#fig-iterated-expectations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.2,0) node[lab, right] {$y$};
\draw[->] (0,0) -- (0,3.2) node[lab, above] {$x$};
\node[dot] at (1.14,1.01) {};
\node[dot] at (0.88,0.86) {};
\node[dot] at (1.10,0.85) {};
\node[dot] at (0.94,0.38) {};
\node[dot] at (1.03,0.54) {};
\node[dot] at (0.90,0.61) {};
\node[dot] at (0.98,0.46) {};
\node[dot] at (1.15,1.25) {};
\node[dot] at (1.13,0.53) {};
\draw[hl] (0.65,0.9) -- (1.35,0.9);
\node[dot] at (2.13,1.90) {};
\node[dot] at (2.06,2.39) {};
\node[dot] at (2.15,2.07) {};
\node[dot] at (2.16,2.33) {};
\node[dot] at (2.22,1.73) {};
\node[dot] at (2.12,2.31) {};
\node[dot] at (2.09,2.05) {};
\node[dot] at (2.20,2.52) {};
\node[dot] at (2.10,2.00) {};
\draw[hl] (1.85,2.0) -- (2.55,2.0);
\node[dot] at (3.52,1.57) {};
\node[dot] at (3.52,0.85) {};
\node[dot] at (3.48,1.48) {};
\node[dot] at (3.54,1.08) {};
\node[dot] at (3.54,1.71) {};
\node[dot] at (3.46,1.90) {};
\node[dot] at (3.39,1.00) {};
\node[dot] at (3.53,1.32) {};
\node[dot] at (3.40,1.56) {};
\draw[hl] (3.05,1.4) -- (3.75,1.4);
\node[dot] at (4.61,2.11) {};
\node[dot] at (4.62,1.96) {};
\node[dot] at (4.63,2.51) {};
\node[dot] at (4.57,2.15) {};
\node[dot] at (4.45,2.42) {};
\node[dot] at (4.56,2.78) {};
\node[dot] at (4.43,3.06) {};
\node[dot] at (4.62,2.08) {};
\node[dot] at (4.56,3.22) {};
\draw[hl] (4.15,2.4) -- (4.85,2.4);
\node[tick, text=accent, right] at (4.85,2.4) {$E[X\mid Y]$};
\end{tikzpicture}
\end{center}
```

$E[X\mid Y]$ is a random variable: for each value of $Y$ it is the mean of $X$ over that slice (bars)

:::

::: {#thm-iterated-expectations .theorem name="Law of iterated expectations" generalizes="thm-total-expectation"}

$$E\bigl[E[X\mid Y]\bigr]=E[X].$$

:::

::: {.proof}

1. For discrete $Y$, $E[g(Y)]=\sum_yg(y)\,p_Y(y)=\sum_yE[X\mid Y=y]\Pr(Y=y)$.

2. The events $\{Y=y\}$ partition the sample space, so the law of total expectation (@thm-total-expectation) gives $E[X]$.

3. For continuous $Y$ the same computation with integrals reads $\int E[X\mid Y=y]f_Y(y)\,dy=\iint xf_{X\mid Y}(x\mid y)f_Y(y)\,dx\,dy=\iint xf_{X,Y}(x,y)\,dx\,dy=E[X]$.

:::

::: {#thm-total-variance .theorem name="Law of total variance"}

$$\mathrm{Var}(X)=E\bigl[\mathrm{Var}(X\mid Y)\bigr]+\mathrm{Var}\bigl(E[X\mid Y]\bigr).$$

:::

::: {.proof}

1. Given $Y=y$, $\mathrm{Var}(X\mid Y=y)=E[X^2\mid Y=y]-g(y)^2$, so $\mathrm{Var}(X\mid Y)=E[X^2\mid Y]-g(Y)^2$.

2. Take expectations and use @thm-iterated-expectations: $E[\mathrm{Var}(X\mid Y)]=E[X^2]-E[g(Y)^2]$.

3. Also $\mathrm{Var}(g(Y))=E[g(Y)^2]-(E[g(Y)])^2=E[g(Y)^2]-(E[X])^2$.

4. Adding the two lines, $E[g(Y)^2]$ cancels and the sum is $E[X^2]-(E[X])^2=\mathrm{Var}(X)$.

:::

::: {#fig-iterated-expectations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.6,0) node[lab, right] {group};
\draw[->] (0,0) -- (0,3.2) node[lab, above] {$x$};
\draw[emph] (1.0,0.30) -- (1.0,1.50);
\draw (0.88,0.30) -- (1.12,0.30) (0.88,1.50) -- (1.12,1.50);
\node[hl dot] at (1.0,0.9) {};
\draw[emph] (2.6,1.40) -- (2.6,3.20);
\draw (2.48,1.40) -- (2.72,1.40) (2.48,3.20) -- (2.72,3.20);
\node[hl dot] at (2.6,2.3) {};
\draw[emph] (4.2,1.00) -- (4.2,2.00);
\draw (4.08,1.00) -- (4.32,1.00) (4.08,2.00) -- (4.32,2.00);
\node[hl dot] at (4.2,1.5) {};
\draw[faint, dashed] (0,1.57) -- (5.2,1.57) node[tick, right] {$E[X]$};
\end{tikzpicture}
\end{center}
```

The law of total variance: the spread of $X$ splits into the spread within each group (bars, $E[\operatorname{Var}(X\mid Y)]$) and the spread of the group means (dots, $\operatorname{Var}(E[X\mid Y])$)

:::

In words: total spread = average spread within the groups $\{Y=y\}$ + spread of the group means.

::: {#exm-stick-breaking .example name="Breaking a stick twice"}

Break a stick of length $\ell$ at a uniform point $Y$, keep the piece $[0,Y]$, and break it again at a uniform point $X$ of $[0,Y]$. Given $Y$, $X$ is uniform on $[0,Y]$, so $E[X\mid Y]=Y/2$ and $\mathrm{Var}(X\mid Y)=Y^2/12$. Hence
$$E[X]=E[Y]/2=\ell/4,\qquad\mathrm{Var}(X)=\frac{E[Y^2]}{12}+\frac{\mathrm{Var}(Y)}4=\frac{\ell^2}{36}+\frac{\ell^2}{48}=\frac{7\ell^2}{144}.$$

:::

::: {#fig-iterated-expectations-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,1) -- (6,1);
\draw[emph] (0,0) -- (3.8,0);
\node[tick, left] at (0,1) {stick};
\node[hl dot] at (3.8,1) {};
\node[tick, above] at (3.8,1) {$Y$};
\node[hl dot] at (1.5,0) {};
\node[tick, below] at (1.5,0) {$X$};
\node[tick, above] at (6,1) {$\ell$};
\draw[faint, dashed] (3.8,1) -- (3.8,0);
\node[tick, right] at (3.9,0) {kept piece $[0,Y]$};
\end{tikzpicture}
\end{center}
```

Breaking a stick twice: $Y$ is uniform on $[0,\ell]$ and, given $Y$, $X$ is uniform on $[0,Y]$, so $E[X]=E[E[X\mid Y]]=E[Y/2]=\ell/4$

:::

::: {#thm-random-sum .theorem name="Sum of a random number of random variables"}

Let $X_1,X_2,\dots$ be independent and identically distributed with mean $\mu$, variance $\sigma^2$ and transform $M_X$, and let $N$ be a nonnegative integer random variable independent of them. Then $Y=X_1+\dots+X_N$ satisfies
$$E[Y]=E[N]\,\mu,\qquad\mathrm{Var}(Y)=E[N]\,\sigma^2+\mu^2\,\mathrm{Var}(N),\qquad M_Y(s)=E\bigl[M_X(s)^N\bigr].$$

:::

::: {.proof}

1. Given $N=n$, $Y$ is a sum of $n$ fixed independent terms, so $E[Y\mid N]=N\mu$, $\mathrm{Var}(Y\mid N)=N\sigma^2$ and $E[e^{sY}\mid N]=M_X(s)^N$ (@thm-transform-properties).

2. Iterated expectations (@thm-iterated-expectations) give $E[Y]=E[N\mu]=E[N]\mu$ and $M_Y(s)=E[M_X(s)^N]$.

3. Total variance (@thm-total-variance) gives $\mathrm{Var}(Y)=E[N\sigma^2]+\mathrm{Var}(N\mu)=E[N]\sigma^2+\mu^2\mathrm{Var}(N)$.

:::

The transform is the transform of $N$ with $e^s$ replaced by $M_X(s)$: write $M_N(s)=E[e^{sN}]$; then $M_Y(s)=M_N(\ln M_X(s))$.

::: {#exm-geometric-sum-of-exponentials .example name="A geometric number of exponentials"}

Let $N\sim\mathrm{Geom}(p)$ and $X_i\sim\operatorname{Exp}(\lambda)$. Then $E[z^N]=\frac{pz}{1-(1-p)z}$ and $M_X(s)=\frac{\lambda}{\lambda-s}$ for $s<\lambda$, so
$$M_Y(s)=\frac{p\lambda/(\lambda-s)}{1-(1-p)\lambda/(\lambda-s)}=\frac{p\lambda}{p\lambda-s},$$
the transform of $\operatorname{Exp}(p\lambda)$. A geometric number of exponential waits is again exponential, with mean $\frac1p\cdot\frac1\lambda$.

:::
