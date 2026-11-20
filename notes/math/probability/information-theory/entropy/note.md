---
title: "Entropy and Mutual Information"
sources: [eecs126-7]
requires: [math/probability/discrete/conditional-expectation]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Information Theory Introduction", Section 1, in our own wording; proofs written out in steps. -->

Entropy measures the uncertainty of a random variable, in bits: the average number of yes/no questions needed to learn its value (@sec-math-probability-information-theory-source-coding makes this precise). Logarithms are base $2$, and $0\log\frac10=0$.

::: {#def-entropy .definition name="Entropy"}

The *entropy* of a discrete random variable $X$ with PMF $p$ is
$$H(X)=\sum_xp(x)\log_2\frac{1}{p(x)}=E\Bigl[\log_2\frac{1}{p(X)}\Bigr].$$
The *joint entropy* $H(X,Y)$ is the entropy of the pair, and the *conditional entropy* is
$$H(Y\mid X)=\sum_xp(x)\,H(Y\mid X=x)=E\Bigl[\log_2\frac{1}{p(Y\mid X)}\Bigr].$$

:::

::: {#exm-entropy-small .example name="Three outcomes"}

If $X$ takes three values with probabilities $\tfrac12,\tfrac14,\tfrac14$, then $H(X)=\tfrac12\cdot1+2\cdot\tfrac14\cdot2=1.5$ bits. Asking "is it the first value?" and, if not, "is it the second?" uses $1.5$ questions on average. A fair coin has entropy $1$ bit; a $\operatorname{Bernoulli}(p)$ variable has $h(p)=p\log_2\frac1p+(1-p)\log_2\frac1{1-p}$.

:::

::: {#fig-entropy-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=3]
\draw[->] (0,0) -- (1.15,0) node[lab, right] {$p$};
\draw[->] (0,0) -- (0,1.2) node[lab, above] {$h(p)$};
\draw[emph, primary] plot[domain=0.001:0.999, samples=100] (\x,{-(\x*ln(\x)+(1-\x)*ln(1-\x))/ln(2)});
\draw[faint, dashed] (0.5,0) -- (0.5,1) -- (0,1);
\node[tick, below] at (0.5,0) {$\frac12$}; \node[tick, below] at (1,0) {$1$}; \node[tick, left] at (0,1) {$1$};
\node[hl dot] at (0.5,1) {};
\end{tikzpicture}
\end{center}
```

The binary entropy $h(p)$ of a $\operatorname{Bernoulli}(p)$ variable, in bits. It is $0$ when the outcome is certain and largest, $1$ bit, for a fair coin.

:::

::: {#def-relative-entropy .definition name="Relative entropy, mutual information"}

The *relative entropy* (Kullback–Leibler divergence) between PMFs $p$ and $q$ is
$$D(p\,\|\,q)=\sum_xp(x)\log_2\frac{p(x)}{q(x)}.$$
The *mutual information* of $X$ and $Y$ is
$$I(X;Y)=D\bigl(p_{X,Y}\,\|\,p_Xp_Y\bigr)=\sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{p(x)p(y)}.$$

:::

<!-- Merged 2026-11-19 (owner decision): the former block thm-relative-entropy-nonnegative now lives in @thm-gibbs-inequality (Softmax and Cross Entropy), which states both forms. -->

Relative entropy is never negative: $D(p\,\|\,q)\ge0$, with equality if and only if $p=q$. This is Gibbs' inequality (@thm-gibbs-inequality), since $D(p\,\|\,q)=H(p,q)-H(p)$ with $H(p,q)$ the cross entropy; the base of the logarithm does not matter.

::: {#thm-entropy-properties .theorem name="Properties of entropy"}

For discrete $X,Y$ with $X$ taking at most $n$ values:

1. $0\le H(X)\le\log_2n$, with the upper bound attained exactly by the uniform distribution;
2. (chain rule) $H(X,Y)=H(X)+H(Y\mid X)$;
3. $I(X;Y)=H(Y)-H(Y\mid X)=H(X)+H(Y)-H(X,Y)\ge0$, so conditioning reduces entropy, $H(Y\mid X)\le H(Y)$, and $H(X,Y)\le H(X)+H(Y)$, with equality if and only if $X$ and $Y$ are independent.

:::

::: {.proof}

1. Each term $p\log\frac1p$ is non-negative. With $u$ uniform on the $n$ values, $D(p\,\|\,u)=\log_2n-H(X)\ge0$ by @thm-gibbs-inequality, with equality only for $p=u$.

2. $\log\frac1{p(x,y)}=\log\frac1{p(x)}+\log\frac1{p(y\mid x)}$; take expectations.

3. $\log\frac{p(x,y)}{p(x)p(y)}=\log\frac1{p(y)}-\log\frac1{p(y\mid x)}$; taking expectations gives $I(X;Y)=H(Y)-H(Y\mid X)$, and the chain rule gives the second form. $I(X;Y)\ge0$ by @thm-gibbs-inequality, with equality iff $p_{X,Y}=p_Xp_Y$.

:::

$I(X;Y)$ is the reduction in uncertainty about $Y$ from learning $X$, and it is symmetric in $X$ and $Y$.
