---
title: "Minimal Sufficient Statistics"
sources: [camib-st-3, camib-sts-1-q3, camib-sts-1-q4, camib-sts-1-q11]
requires: [math/statistics/inference/sufficient-statistics]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 3 and Example Sheet 1 (questions 3, 4, 11), in our own wording; proof written out in steps for the discrete case. -->

The whole data and the order statistic are sufficient but compress nothing, or little. A sufficient statistic is *minimal* if it compresses as much as any sufficient statistic can.

::: {#def-minimal-sufficient .definition name="Minimal sufficient statistic"}

A sufficient statistic $T(X)$ is *minimal sufficient* if it is a function of every other sufficient statistic $S(X)$: whenever $S(x)=S(y)$ we have $T(x)=T(y)$.

:::

::: {#thm-minimal-sufficiency-criterion .theorem name="Ratio criterion"}

Suppose $T$ satisfies: $T(x)=T(y)$ if and only if $p(x;\theta)=c(x,y)\,p(y;\theta)$ for all $\theta$, for some $c(x,y)>0$ not depending on $\theta$ (when the ratio $p(x;\theta)/p(y;\theta)$ is defined, this says that the ratio does not depend on $\theta$). Then $T$ is minimal sufficient.

:::

::: {.proof}

We write the discrete case, assuming that every point $x$ has $p(x;\theta)>0$ for some $\theta$.

1. *$T$ is sufficient.* Choose one representative $x_t$ in each level set $\{T=t\}$. For $x$ with $T(x)=t$ the hypothesis gives $p(x;\theta)=c(x,x_t)\,p(x_t;\theta)$. So
$$p(x;\theta)=g\bigl(T(x),\theta\bigr)h(x),\qquad g(t,\theta)=p(x_t;\theta),\quad h(x)=c(x,x_{T(x)}),$$
and $T$ is sufficient by @thm-factorisation-criterion.

2. *$T$ is minimal.* Let $S$ be sufficient and $S(x)=S(y)$. By factorisation $p(x;\theta)=g'(S(x),\theta)h'(x)$ and $p(y;\theta)=g'(S(y),\theta)h'(y)$, where $h'(x),h'(y)>0$ because $x,y$ have positive probability for some $\theta$. Since $S(x)=S(y)$,
$$p(x;\theta)=\frac{h'(x)}{h'(y)}\,p(y;\theta)\quad\text{for all }\theta.$$

3. Hence the ratio does not depend on $\theta$, so $T(x)=T(y)$ by the hypothesis. Thus $T$ is a function of $S$.

:::

::: {#exm-minimal-normal .example name="Normal sample with unknown mean and variance"}

Let $X_1,\dots,X_n$ be iid $N(\mu,\sigma^2)$ with both parameters unknown. Then
$$\frac{p(x;\mu,\sigma^2)}{p(y;\mu,\sigma^2)}=\exp\Bigl\{-\frac{1}{2\sigma^2}\Bigl(\sum x_i^2-\sum y_i^2\Bigr)+\frac{\mu}{\sigma^2}\Bigl(\sum x_i-\sum y_i\Bigr)\Bigr\}$$
is free of $(\mu,\sigma^2)$ if and only if $\sum x_i=\sum y_i$ and $\sum x_i^2=\sum y_i^2$. By @thm-minimal-sufficiency-criterion, $\bigl(\sum X_i,\sum X_i^2\bigr)$ is minimal sufficient, and so is the equivalent pair $(\bar X,S^2)$ with $S^2=\sum(X_i-\bar X)^2/(n-1)$, as $\sum x_i^2=(n-1)s^2+n\bar x^2$ is a bijective recoding.

:::

::: {#exm-minimal-uniform-theta-2theta .example name="Uniform on $(\theta,2\theta)$"}

For iid $\mathrm{Unif}(\theta,2\theta)$ data the density is
$$p(x;\theta)=\theta^{-n}\mathbf 1\Bigl\{\tfrac12\max_ix_i\le\theta\le\min_ix_i\Bigr\}.$$
Two samples $x,y$ give a ratio that is constant in $\theta$ (and nonzero) exactly when the intervals $[\tfrac12\max x_i,\min x_i]$ and $[\tfrac12\max y_i,\min y_i]$ coincide, that is when the pairs $(\min,\max)$ coincide. So $(\min_iX_i,\max_iX_i)$ is minimal sufficient: two numbers for a one-dimensional parameter, and no single real statistic is sufficient.

:::

::: {#exm-minimal-bernoulli-poisson .example name="Bernoulli and Poisson samples"}

For iid Bernoulli$(\theta)$ the ratio $p(x;\theta)/p(y;\theta)=(\theta/(1-\theta))^{\sum x_i-\sum y_i}$ is free of $\theta$ iff $\sum x_i=\sum y_i$, so $\sum X_i$ is minimal sufficient. For iid Poisson$(\lambda)$ the ratio is $\lambda^{\sum x_i-\sum y_i}\prod y_i!/\prod x_i!$, again free of $\lambda$ iff the sums agree, so $\sum X_i$ is minimal sufficient.

:::

::: {#fig-minimal-sufficiency-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[box] (X) at (0,0) {data $x$};
\node[box] (S) at (3.4,0.9) {$S(x)$ sufficient};
\node[hl box] (T) at (6.8,0) {$T(x)$ minimal};
\draw[->, emph] (X) -- (S);
\draw[->, emph] (S) -- (T);
\draw[->, faint] (X) -- (T);
\end{tikzpicture}
\end{center}
```

Every sufficient statistic $S$ can be further reduced to the minimal sufficient statistic $T$, which is a function of it; the data themselves reach $T$ directly.

:::
