---
title: "Functions of a Random Variable and Spread"
sources: [cs70-16.1]
requires: [math/probability/discrete/indicator-variables]
status: draft
---

<!-- Split from math/probability/discrete/covariance-and-correlation on 2026-11-17 (block ids unchanged). Added from CS70 Note 16 (cs70-16.1), in our own wording; proofs written out in steps. -->

## Functions of a random variable

::: {#prp-expectation-of-function .proposition name="Expectation of a function of X"}

For any function $f$ on the values of $X$,
$$E[f(X)]=\sum_x f(x)\Pr(X=x).$$
This is sometimes called the *law of the unconscious statistician*.

:::

::: {.proof}

1. Let $Y=f(X)$. The event $Y=y$ is the disjoint union of the events $X=x$ with $f(x)=y$, so $\Pr(Y=y)=\sum_{x:\,f(x)=y}\Pr(X=x)$.

2. By @def-expectation,
   $$E[Y]=\sum_y y\Pr(Y=y)=\sum_y\ \sum_{x:\,f(x)=y} f(x)\Pr(X=x).$$

3. Every value $x$ appears in exactly one inner sum, the one with $y=f(x)$, so the double sum is $\sum_x f(x)\Pr(X=x)$.

:::

## Spread: the random walk

::: {#prp-random-walk-square .proposition name="Squared distance of a random walk"}

A particle starts at $0$ and makes $n$ independent moves, each $+1$ or $-1$ with probability $\frac12$. Its position is $S_n=X_1+\cdots+X_n$. Then $E[S_n]=0$ and $E[S_n^2]=n$.

:::

::: {.proof}

1. $E[X_i]=\frac12\cdot1+\frac12\cdot(-1)=0$, so $E[S_n]=0$ by linearity.

2. Expanding the square, $S_n^2=\sum_i X_i^2+\sum_{i\ne j}X_iX_j$.

3. $X_i^2=1$ always, so $E[X_i^2]=1$.

4. For $i\ne j$, $X_i$ and $X_j$ are independent, so $E[X_iX_j]=E[X_i]E[X_j]=0$ (@thm-expectation-of-product).

5. By linearity, $E[S_n^2]=n\cdot1+0=n$.

:::

::: {#rmk-covariance-and-correlation-1 .remark name="Typical distance"}

$E[S_n]=0$ says nothing about how far the particle wanders, because moves to the left and right cancel. The squared distance has mean $n$, which suggests a typical distance of about $\sqrt n$. This is the idea behind the variance, $E[(X-\mu)^2]$ (@def-variance-standard-deviation).

:::

::: {#fig-functions-of-random-variables-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$n$};
\draw[->] (0,-2.6) -- (0,2.4) node[lab, above] {position};
\draw[faint, dashed] plot[domain=0:6, samples=50] (\x,{0.2*sqrt(10*\x)});
\draw[faint, dashed] plot[domain=0:6, samples=50] (\x,{-0.2*sqrt(10*\x)});
\node[tick, right] at (6,1.55) {$\sqrt n$}; \node[tick, right] at (6,-1.55) {$-\sqrt n$};
\draw[primary] (0.0,0.0) -- (0.1,0.2) -- (0.2,0.0) -- (0.3,0.2) -- (0.4,0.0) -- (0.5,-0.2) -- (0.6,-0.4) -- (0.7,-0.2) -- (0.8,-0.4) -- (0.9,-0.6) -- (1.0,-0.8) -- (1.1,-1.0) -- (1.2,-0.8) -- (1.3,-0.6) -- (1.4,-0.8) -- (1.5,-1.0) -- (1.6,-1.2) -- (1.7,-1.0) -- (1.8,-1.2) -- (1.9,-1.4) -- (2.0,-1.6) -- (2.1,-1.8) -- (2.2,-1.6) -- (2.3,-1.8) -- (2.4,-2.0) -- (2.5,-2.2) -- (2.6,-2.4) -- (2.7,-2.2) -- (2.8,-2.0) -- (2.9,-2.2) -- (3.0,-2.4) -- (3.1,-2.2) -- (3.2,-2.4) -- (3.3,-2.6) -- (3.4,-2.8) -- (3.5,-2.6) -- (3.6,-2.8) -- (3.7,-3.0) -- (3.8,-3.2) -- (3.9,-3.4) -- (4.0,-3.2) -- (4.1,-3.0) -- (4.2,-2.8) -- (4.3,-2.6) -- (4.4,-2.4) -- (4.5,-2.2) -- (4.6,-2.0) -- (4.7,-2.2) -- (4.8,-2.4) -- (4.9,-2.6) -- (5.0,-2.8) -- (5.1,-2.6) -- (5.2,-2.4) -- (5.3,-2.2) -- (5.4,-2.0) -- (5.5,-1.8) -- (5.6,-2.0) -- (5.7,-2.2) -- (5.8,-2.0) -- (5.9,-2.2) -- (6.0,-2.0);
\draw[accent] (0.0,0.0) -- (0.1,-0.2) -- (0.2,0.0) -- (0.3,0.2) -- (0.4,0.0) -- (0.5,-0.2) -- (0.6,0.0) -- (0.7,0.2) -- (0.8,0.4) -- (0.9,0.6) -- (1.0,0.8) -- (1.1,0.6) -- (1.2,0.4) -- (1.3,0.6) -- (1.4,0.8) -- (1.5,0.6) -- (1.6,0.4) -- (1.7,0.6) -- (1.8,0.8) -- (1.9,1.0) -- (2.0,1.2) -- (2.1,1.4) -- (2.2,1.2) -- (2.3,1.4) -- (2.4,1.6) -- (2.5,1.4) -- (2.6,1.2) -- (2.7,1.4) -- (2.8,1.2) -- (2.9,1.0) -- (3.0,1.2) -- (3.1,1.0) -- (3.2,0.8) -- (3.3,1.0) -- (3.4,1.2) -- (3.5,1.4) -- (3.6,1.2) -- (3.7,1.0) -- (3.8,1.2) -- (3.9,1.4) -- (4.0,1.6) -- (4.1,1.4) -- (4.2,1.6) -- (4.3,1.8) -- (4.4,2.0) -- (4.5,2.2) -- (4.6,2.4) -- (4.7,2.2) -- (4.8,2.0) -- (4.9,1.8) -- (5.0,1.6) -- (5.1,1.4) -- (5.2,1.2) -- (5.3,1.0) -- (5.4,0.8) -- (5.5,1.0) -- (5.6,0.8) -- (5.7,1.0) -- (5.8,1.2) -- (5.9,1.0) -- (6.0,0.8);
\draw[secondary] (0.0,0.0) -- (0.1,0.2) -- (0.2,0.4) -- (0.3,0.6) -- (0.4,0.4) -- (0.5,0.2) -- (0.6,0.4) -- (0.7,0.6) -- (0.8,0.8) -- (0.9,1.0) -- (1.0,1.2) -- (1.1,1.0) -- (1.2,1.2) -- (1.3,1.4) -- (1.4,1.2) -- (1.5,1.0) -- (1.6,0.8) -- (1.7,0.6) -- (1.8,0.8) -- (1.9,0.6) -- (2.0,0.4) -- (2.1,0.6) -- (2.2,0.4) -- (2.3,0.2) -- (2.4,0.0) -- (2.5,-0.2) -- (2.6,-0.4) -- (2.7,-0.2) -- (2.8,-0.4) -- (2.9,-0.6) -- (3.0,-0.8) -- (3.1,-0.6) -- (3.2,-0.8) -- (3.3,-0.6) -- (3.4,-0.4) -- (3.5,-0.2) -- (3.6,0.0) -- (3.7,-0.2) -- (3.8,-0.4) -- (3.9,-0.2) -- (4.0,0.0) -- (4.1,0.2) -- (4.2,0.4) -- (4.3,0.6) -- (4.4,0.4) -- (4.5,0.2) -- (4.6,0.0) -- (4.7,0.2) -- (4.8,0.4) -- (4.9,0.6) -- (5.0,0.4) -- (5.1,0.2) -- (5.2,0.0) -- (5.3,0.2) -- (5.4,0.0) -- (5.5,-0.2) -- (5.6,0.0) -- (5.7,-0.2) -- (5.8,0.0) -- (5.9,0.2) -- (6.0,0.0);
\end{tikzpicture}
\end{center}
```

Three random walks of $60$ steps of $\pm1$. The mean position stays $0$, but the mean squared distance after $n$ steps is $n$ (@prp-random-walk-square), so typical distances grow like $\sqrt n$ (dashed).

:::

::: {#prp-fixed-points-variance .proposition name="Variance of the number of fixed points"}

For the number $X_n$ of fixed points of a random permutation of $n\ge2$ elements, $\mathrm{Var}(X_n)=1$.

:::

::: {.proof}

1. Write $X_n=I_1+\cdots+I_n$ as in @thm-expected-fixed-points, so $E[X_n]=1$.

2. $E[X_n^2]=\sum_i E[I_i^2]+\sum_{i\ne j}E[I_iI_j]$ by expanding the square and linearity.

3. $I_i^2=I_i$, so $E[I_i^2]=\frac1n$.

4. For $i\ne j$, $I_iI_j$ indicates "both $i$ and $j$ are fixed". There are $(n-2)!$ such permutations, so $E[I_iI_j]=\frac{(n-2)!}{n!}=\frac1{n(n-1)}$.

5. The second sum has $n(n-1)$ terms, so $E[X_n^2]=n\cdot\frac1n+n(n-1)\cdot\frac1{n(n-1)}=2$.

6. By @prp-expectation-and-variance-1, $\mathrm{Var}(X_n)=2-1^2=1$.

:::
