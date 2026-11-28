---
title: "Sufficient Statistics"
sources: [camib-st-3, camib-sts-1-q3, camib-sts-1-q8]
requires: [math/statistics/inference/statistical-models]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part IB Statistics (Lent 2025, lecturer's notes), Lecture 3 and Example Sheet 1 (questions 3, 8), in our own wording; proofs written out in steps for the discrete case. -->

Data usually contain more detail than is needed to say anything about the parameter. A *sufficient statistic* is a summary that discards only detail that is irrelevant to $\theta$.

::: {#def-sufficient-statistic .definition name="Sufficient statistic"}

Let $X$ have probability mass or density function $p(x;\theta)$, $\theta\in\Theta$. A statistic $T=T(X)$ is *sufficient* for $\theta$ if the conditional distribution of $X$ given $T(X)=t$ does not depend on $\theta$, for every $t$.

:::

::: {#fig-sufficient-statistics-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[emph] (0,0) rectangle (6,3);
\foreach \x in {1,2,3,4,5} \draw[faint] (\x,0) -- (\x,3);
\foreach \x/\l in {0.5/1,1.5/2,2.5/3,3.5/4,4.5/5,5.5/6} \node[tick] at (\x,-0.3) {$t=\l$};
\node[hl dot] at (2.5,1.4) {};
\node[lab, right] at (2.6,1.4) {$x$};
\node[lab] at (3,3.4) {sample space of $X$, cut into the level sets of $T$};
\end{tikzpicture}
\end{center}
```

The statistic $T$ cuts the sample space into level sets. Sufficiency means that inside each level set the conditional law of $X$ is the same for every $\theta$: once $T=t$ is known, the position of $x$ within its strip carries no information about $\theta$.

:::

::: {#thm-factorisation-criterion .theorem name="Factorisation criterion"}

A statistic $T$ is sufficient for $\theta$ if and only if the density factorises as
$$
p(x;\theta)=g\bigl(T(x),\theta\bigr)\,h(x)
$$
for some functions $g$ and $h$, where $h$ does not depend on $\theta$.

:::

::: {.proof}

We prove the discrete case.

1. ($\Rightarrow$) If $T$ is sufficient put $h(x)=P(X=x\mid T=T(x))$, which does not depend on $\theta$, and $g(t,\theta)=P_\theta(T=t)$. Since $\{X=x\}\subseteq\{T=T(x)\}$,
$$p(x;\theta)=P_\theta(T=T(x))\,P(X=x\mid T=T(x))=g(T(x),\theta)h(x).$$

2. ($\Leftarrow$) Suppose $p(x;\theta)=g(T(x),\theta)h(x)$. For a value $t$ of $T$, summing over $\{x:T(x)=t\}$ gives
$$P_\theta(T=t)=g(t,\theta)H(t),\qquad H(t)=\sum_{x:\,T(x)=t}h(x).$$

3. For $x$ with $T(x)=t$ and $P_\theta(T=t)>0$,
$$P_\theta(X=x\mid T=t)=\frac{p(x;\theta)}{P_\theta(T=t)}=\frac{g(t,\theta)h(x)}{g(t,\theta)H(t)}=\frac{h(x)}{H(t)},$$
which does not depend on $\theta$.

:::

::: {#exm-sufficient-bernoulli .example name="Bernoulli trials"}

For $X_1,\dots,X_n$ independent Bernoulli$(\theta)$,
$$p(x;\theta)=\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}=(1-\theta)^n\Bigl(\frac\theta{1-\theta}\Bigr)^{\sum x_i}\cdot1 ,$$
so $T=\sum_iX_i$ is sufficient with $h\equiv1$: the number of successes tells as much about $\theta$ as the whole sequence.

:::

::: {#exm-sufficient-uniform .example name="Uniform on $[0,\theta]$"}

For $X_1,\dots,X_n$ independent $\mathrm{Unif}[0,\theta]$,
$$p(x;\theta)=\theta^{-n}\mathbf 1\{\max_ix_i\le\theta\}\cdot\mathbf 1\{\min_ix_i\ge0\},$$
which depends on $\theta$ only through $\max_ix_i$; so $T=\max_iX_i$ is sufficient with $h(x)=\mathbf 1\{\min x_i\ge0\}$.

:::

::: {#exm-sufficient-poisson-weighted .example name="Poisson counts with different means"}

Let $X_i\sim\mathrm{Poisson}(i\theta)$ be independent for $i=1,\dots,n$. Then
$$p(x;\theta)=\prod_{i=1}^n\frac{e^{-i\theta}(i\theta)^{x_i}}{x_i!}=e^{-\theta n(n+1)/2}\theta^{\sum x_i}\cdot\prod_i\frac{i^{x_i}}{x_i!},$$
so $T=\sum_iX_i$ is sufficient; it is Poisson$(\theta\,n(n+1)/2)$ because independent Poisson variables add.

:::

::: {#prp-order-statistics-sufficient .proposition name="Order statistics"}

For independent identically distributed data the order statistic $(X_{(1)},\dots,X_{(n)})$ is sufficient for every model.

:::

::: {.proof}

For iid data $p(x;\theta)=\prod_ip(x_i;\theta)$ is unchanged by permuting the $x_i$, so it is a function of the sorted values, and the factorisation holds with $h\equiv1$.

:::

::: {#prp-mle-sufficient .proposition name="Likelihood methods use only a sufficient statistic"}

Let $T$ be sufficient for $\theta$.

1. If the maximum likelihood estimator $\hat\theta(X)$ is unique, it is a function of $T(X)$.
2. For any prior $\pi$, the posterior $\pi(\theta\mid x)$ depends on $x$ only through $T(x)$; hence so does every Bayes estimator (@def-bayes-estimator).

:::

::: {.proof}

1. By @thm-factorisation-criterion the likelihood is $L(\theta)=g(T(x),\theta)h(x)$ with $h(x)>0$ for observed $x$. Maximising over $\theta$ is the same as maximising $g(T(x),\theta)$, and this depends on $x$ only through $T(x)$; the unique maximiser is therefore a function of $T(x)$.

2. By Bayes' theorem
$$\pi(\theta\mid x)=\frac{\pi(\theta)g(T(x),\theta)h(x)}{\int\pi(\vartheta)g(T(x),\vartheta)h(x)\,d\vartheta}=\frac{\pi(\theta)g(T(x),\theta)}{\int\pi(\vartheta)g(T(x),\vartheta)\,d\vartheta},$$
since $h(x)$ cancels. A Bayes estimator minimises the posterior expected loss, which is computed from the posterior, so it is a function of $T(x)$.

:::

::: {#rmk-sufficiency-principle .remark name="The sufficiency principle"}

The *sufficiency principle* says: if $T$ is sufficient and two experiments give data $x,y$ with $T(x)=T(y)$, the evidence about $\theta$ is the same. This is a principle about how to use data, not a theorem. The stronger *likelihood principle* says that all the evidence in an experiment is carried by the likelihood function.

:::
