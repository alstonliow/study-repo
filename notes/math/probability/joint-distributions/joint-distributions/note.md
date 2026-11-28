---
title: "Joint Distributions"
sources: [eecs126hw-3]
requires: [math/probability/distributions/exponential-distribution, math/probability/random-variables/covariance-and-correlation]
aliases: [math/probability/continuous/joint-distributions]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), Homework 3, in our own wording; proofs written out in steps. -->

Several continuous random variables defined on the same experiment are described together by one joint density (@def-joint-density). This note adds marginals, conditioning and changes of variables.

::: {#def-marginal-conditional-density .definition name="Marginal and conditional densities"}

Let $X,Y$ have joint density $f_{X,Y}$ (@def-joint-density). The *marginal* densities are
$$f_X(x)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dy,\qquad f_Y(y)=\int_{-\infty}^{\infty}f_{X,Y}(x,y)\,dx,$$
and where $f_X(x)>0$ the *conditional density* of $Y$ given $X=x$ is
$$f_{Y\mid X}(y\mid x)=\frac{f_{X,Y}(x,y)}{f_X(x)}.$$

:::

::: {#fig-joint-distributions-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.4,0) node[lab, right] {$x$};
\draw[->] (0,0) -- (0,3.4) node[lab, above] {$y$};
\draw[faint, rotate around={30:(2.2,1.7)}] (2.2,1.7) ellipse (0.49 and 0.28);
\draw[faint, rotate around={30:(2.2,1.7)}] (2.2,1.7) ellipse (0.98 and 0.56);
\draw[faint, rotate around={30:(2.2,1.7)}] (2.2,1.7) ellipse (1.47 and 0.84);
\draw[hl, domain=0.3:4.2, samples=80, smooth, variable=\x] plot ({\x}, {1.4*exp(-((\x-2.2)^2)/(2*0.62^2))/(0.62*sqrt(2*pi))});
\draw[hl, domain=0.3:3.2, smooth, variable=\y] plot ({1.1*exp(-((\y-1.7)^2)/(2*0.52^2))/(0.52*sqrt(2*pi))}, {\y});
\node[tick, text=accent] at (3.6,0.75) {$f_X$};
\node[tick, text=accent] at (0.95,3.1) {$f_Y$};
\end{tikzpicture}
\end{center}
```

Contours of a joint density with its two marginals drawn along the axes: $f_X$ integrates out $y$ and $f_Y$ integrates out $x$

:::

$X$ and $Y$ are independent (@def-continuous-independence) exactly when $f_{X,Y}(x,y)=f_X(x)f_Y(y)$ for (almost) all $x,y$. Expectations are computed as in the discrete case with sums replaced by integrals: $E[g(X,Y)]=\iint g(x,y)f_{X,Y}(x,y)\,dx\,dy$.

::: {#exm-joint-density-triangle .example name="Uniform on a triangle"}

Let $(X,Y)$ be uniform on the triangle $0\le y\le x\le1$, which has area $\tfrac12$, so $f_{X,Y}=2$ there. Then $f_X(x)=\int_0^x2\,dy=2x$ on $[0,1]$, and given $X=x$ the conditional density of $Y$ is $2/(2x)=1/x$ on $[0,x]$: $Y$ is uniform on $[0,x]$, and $E[Y\mid X]=X/2$.

:::

::: {#fig-joint-distributions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=2.6]
\fill[tintA] (0,0) -- (1,0) -- (1,1) -- cycle;
\draw[emph, primary] (0,0) -- (1,0) -- (1,1) -- cycle;
\draw[->] (-0.1,0) -- (1.25,0) node[lab, right] {$x$};
\draw[->] (0,-0.1) -- (0,1.2) node[lab, above] {$y$};
\draw[hl] (0.65,0) -- (0.65,0.65);
\node[tick, below] at (0.65,0) {$x$}; \node[tick, below] at (1,0) {$1$}; \node[tick, left] at (0,1) {$1$};
\node[lab, right] at (0.67,0.42) {$Y\mid X=x$};
\node[lab, primary] at (0.62,0.82) {$y=x$};
\node[lab] at (0.8,0.2) {$f=2$};
\end{tikzpicture}
\end{center}
```

The joint density of @exm-joint-density-triangle is $2$ on the triangle. Given $X=x$, the slice (highlighted) is the segment $0\le y\le x$, and $Y$ is uniform on it, so $E[Y\mid X=x]=x/2$.

:::

::: {#thm-change-of-variables-density .theorem name="Change of variables"}

Let $(X,Y)$ have joint density $f_{X,Y}$ supported on an open set $D$, and let $g:D\to g(D)$ be one-to-one and continuously differentiable with non-zero Jacobian determinant $J_g$. Then $(U,V)=g(X,Y)$ has density
$$f_{U,V}(u,v)=\frac{f_{X,Y}\bigl(g^{-1}(u,v)\bigr)}{\bigl|J_g\bigl(g^{-1}(u,v)\bigr)\bigr|},\qquad(u,v)\in g(D).$$

:::

::: {.proof}

1. For a set $B\subseteq g(D)$, $\Pr((U,V)\in B)=\Pr((X,Y)\in g^{-1}(B))=\iint_{g^{-1}(B)}f_{X,Y}(x,y)\,dx\,dy$.

2. Substitute $(x,y)=g^{-1}(u,v)$. The multivariable substitution rule multiplies by $|J_{g^{-1}}(u,v)|=1/|J_g(g^{-1}(u,v))|$, so the integral equals $\iint_Bf_{X,Y}(g^{-1}(u,v))/|J_g(g^{-1}(u,v))|\,du\,dv$.

3. This holds for every $B$, so the integrand is the density of $(U,V)$.

:::

::: {#prp-min-of-exponentials .proposition name="Minimum of independent exponentials"}

Let $X_1,\dots,X_n$ be independent with $X_i\sim\operatorname{Exp}(\lambda_i)$, and $\lambda=\sum_i\lambda_i$. Then $M=\min_iX_i\sim\operatorname{Exp}(\lambda)$, and the index $I$ of the minimum satisfies $\Pr(I=i)=\lambda_i/\lambda$, independently of $M$.

:::

::: {.proof}

1. $\Pr(M>t)=\prod_i\Pr(X_i>t)=\prod_ie^{-\lambda_it}=e^{-\lambda t}$, so $M\sim\operatorname{Exp}(\lambda)$.

2. Let $Y=\min_{j\ne i}X_j$, which is $\operatorname{Exp}(\lambda-\lambda_i)$ by step 1 and independent of $X_i$. Then
   $$\Pr(I=i,\,M>t)=\Pr(Y>X_i>t)=\int_t^\infty\lambda_ie^{-\lambda_ix}e^{-(\lambda-\lambda_i)x}\,dx=\frac{\lambda_i}{\lambda}e^{-\lambda t}.$$

3. Hence $\Pr(I=i,M>t)=\Pr(I=i)\Pr(M>t)$ with $\Pr(I=i)=\lambda_i/\lambda$ (take $t=0$).

:::

::: {#fig-joint-distributions-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {$t$};
\draw[emph] (0,1.4) -- (4.6,1.4);
\node[dot] at (4.6,1.4) {};
\node[tick, right] at (4.70,1.4) {$X_1\sim\operatorname{Exp}(\lambda_1)$};
\draw[emph] (0,0.8) -- (2.2,0.8);
\node[hl dot] at (2.2,0.8) {};
\node[tick, right] at (2.30,0.8) {$X_2\sim\operatorname{Exp}(\lambda_2)$};
\draw[emph] (0,0.2) -- (3.5,0.2);
\node[dot] at (3.5,0.2) {};
\node[tick, right] at (3.6,0.2) {$X_3\sim\operatorname{Exp}(\lambda_3)$};
\draw[hl, dashed] (2.2,1.7) -- (2.2,0) node[tick, below] {$\min_iX_i$};
\end{tikzpicture}
\end{center}
```

A race of independent exponential clocks: the first ring $\min_iX_i$ is exponential with rate $\sum_i\lambda_i$, and clock $j$ wins with probability $\lambda_j/\sum_i\lambda_i$

:::

This is the basic "race of exponential clocks" behind Poisson processes and continuous-time Markov chains (@sec-math-probability-markov-chains-poisson-process).
