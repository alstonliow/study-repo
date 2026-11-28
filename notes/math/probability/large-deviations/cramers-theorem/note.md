---
title: "Large Deviations: Cramér's Theorem"
sources: [camiii-ap-6]
requires: [math/probability/joint-distributions/transforms, math/probability/measure-theoretic/weak-convergence]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 6, in our own wording; proofs written out in steps. -->

The law of large numbers and the central limit theorem describe typical behaviour of $S_n=X_1+\dots+X_n$. Here we ask how fast $\Pr(S_n\ge an)$ tends to $0$ for $a>\bar x=E[X_1]$: exponentially, with an explicit rate. Throughout $X_i$ are i.i.d. real, integrable, with mean $\bar x$.

::: {#def-rate-function .definition name="Moment generating function and rate function"}

Let $M(\lambda)=E[e^{\lambda X_1}]\in(0,\infty]$, $\psi(\lambda)=\log M(\lambda)$ and, for $a\in\mathbb R$,

$$
\psi^*(a)=\sup_{\lambda\ge0}\big(a\lambda-\psi(\lambda)\big)\in[0,\infty]
$$

(the one-sided Legendre transform). $\psi^*\ge0$ because $\lambda=0$ gives $-\psi(0)=0$.

:::

::: {#lem-fekete .lemma name="Fekete's lemma"}

If $(b_n)$ is a non-negative sub-additive sequence, $b_{m+n}\le b_m+b_n$, then $\lim_nb_n/n$ exists (and equals $\inf_nb_n/n$).

:::

::: {#prp-exponential-decay .proposition name="Exponential decay"}

For $a>\bar x$, $\lim_n\frac1n\log\Pr(S_n\ge an)$ exists in $[-\infty,0]$.

:::

::: {.proof}

$\Pr(S_{m+n}\ge a(m+n))\ge\Pr(S_m\ge am)\Pr(S_{m+n}-S_m\ge an)=\Pr(S_m\ge am)\Pr(S_n\ge an)$: the sequence is super-multiplicative, so $b_n=-\log\Pr(S_n\ge an)$ is sub-additive, and non-negative; Fekete applies. (If some $\Pr(S_n\ge an)=0$ then $b_n=\infty$ eventually and the limit is $-\infty$.)

:::

::: {#thm-cramer .theorem name="Cramér's theorem"}

For $a>\bar x$,

$$
\lim_{n\to\infty}\frac1n\log\Pr(S_n\ge an)=-\psi^*(a).
$$

:::

::: {.proof}

*Upper bound.*

1. For any $\lambda\ge0$, by Markov's inequality and independence, $\Pr(S_n\ge an)=\Pr(e^{\lambda S_n}\ge e^{\lambda an})\le e^{-\lambda an}M(\lambda)^n=e^{-n(\lambda a-\psi(\lambda))}$.

2. Optimising over $\lambda\ge0$ gives $\Pr(S_n\ge an)\le e^{-n\psi^*(a)}$, hence $\limsup\frac1n\log\Pr(S_n\ge an)\le-\psi^*(a)$.

*Lower bound.* Replace $X_i$ by $X_i-a$: then $a=0$, $\bar x<0$ and we must show $\liminf\frac1n\log\Pr(S_n\ge0)\ge\inf_{\lambda\ge0}\psi(\lambda)$.

3. *Case $\Pr(X_1\le0)=1$.* Then $\Pr(S_n\ge0)=\Pr(X_1=0)^n$, and $\Pr(X_1=0)=\lim_{\lambda\to\infty}E[e^{\lambda X_1}]=\lim_\lambda M(\lambda)\ge\inf_\lambda M(\lambda)$ by monotone convergence. So the bound holds with equality.

4. *Case $\Pr(X_1>0)>0$ and $|X_1|\le K$ a.s.* For $\theta\ge0$ define the tilted law $d\mu_\theta/d\mu=e^{\theta x}/M(\theta)$ and its mean $g(\theta)=\int x\,d\mu_\theta=\frac{\int xe^{\theta x}d\mu}{\int e^{\theta x}d\mu}$. $g$ is continuous (dominated convergence), $g(0)=\bar x<0$, and $\limsup_{\theta\to\infty}g(\theta)>0$ because $X_1>0$ has positive probability. By the intermediate value theorem there is $\theta_0$ with $g(\theta_0)=0$.

5. Let $\mu^n_{\theta_0}$ be the law of the sum of $n$ i.i.d. variables with law $\mu_{\theta_0}$. For $\varepsilon>0$, $\Pr(S_n\ge0)\ge\Pr(S_n\in[0,\varepsilon n])\ge E\big[e^{\theta_0(S_n-\varepsilon n)}\mathbf 1_{\{S_n\in[0,\varepsilon n]\}}\big]$ since $e^{\theta_0(S_n-\varepsilon n)}\le1$ on that event. Changing measure, this equals $M(\theta_0)^ne^{-\theta_0\varepsilon n}\mu^n_{\theta_0}(S_n\in[0,\varepsilon n])$.

6. The tilted variables have mean $0$ and finite variance, so by the central limit theorem $\mu^n_{\theta_0}(S_n\in[0,\varepsilon n])\ge\mu^n_{\theta_0}(S_n/\sqrt n\in[0,\varepsilon\sqrt n])\to\frac12$, since $\varepsilon\sqrt n\to\infty$. Hence $\liminf\frac1n\log\Pr(S_n\ge0)\ge\psi(\theta_0)-\theta_0\varepsilon$. Let $\varepsilon\to0$: the bound is $\ge\psi(\theta_0)\ge\inf_\lambda\psi(\lambda)$.

7. *General case $\Pr(X_1>0)>0$.* Let $\nu$ be the law of $X_1$ conditioned on $\{|X_1|\le K\}$ ($K$ large enough that $\nu$ has negative mean) and $\psi_K(\lambda)=\log\int_{-K}^Ke^{\lambda x}d\mu$. Then $\Pr(S_n\ge0)\ge\nu^{*n}([0,\infty))\,\Pr(|X_1|\le K)^n$, and step 4 applied to $\nu$ gives $\liminf\frac1n\log\Pr(S_n\ge0)\ge\log\Pr(|X_1|\le K)+\inf_\lambda\psi^\nu(\lambda)=\inf_\lambda\psi_K(\lambda)=:J_K$.

8. $J_K$ increases with $K$ to some $J$. Each $\psi_K$ is continuous, so the sets $\{\lambda:\psi_K(\lambda)\le J\}$ are non-empty, compact and nested; by Cantor's intersection theorem there is $\lambda_0$ in all of them. Then $J\ge\sup_K\psi_K(\lambda_0)=\psi(\lambda_0)\ge\inf_\lambda\psi(\lambda)$ (monotone convergence), which proves the lower bound.

:::

::: {#fig-cramers-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (7,0) node[lab, right] {$a$};
\draw[->] (0,-0.2) -- (0,3.2);
\draw[emph] (1.0,2.9) .. controls (2.2,0.6) and (2.8,0.1) .. (3.2,0.0) .. controls (3.8,0.1) and (4.8,0.8) .. (6.4,2.9);
\node[small vertex] at (3.2,0.0) {};
\node[tick] at (3.2,-0.3) {$\bar x$};
\draw[hl] (5.0,0.0) -- (5.0,1.25);
\node[tick] at (5.0,-0.3) {$a$};
\node[lab, text=accent] at (5.8,1.5) {$\psi^*(a)$};
\node[lab, text=accent] at (1.9,1.8) {$\psi^*$};
\end{tikzpicture}
\end{center}
```

The rate function $\psi^*$ vanishes at the mean $\bar x$ and grows away from it; $\Pr(S_n\ge an)\approx e^{-n\psi^*(a)}$.

:::

::: {#exm-cramer-coin .example name="Fair coin tosses"}

For $X_i=\pm1$ with probability $\tfrac12$, $M(\lambda)=\cosh\lambda$ and the supremum in $\psi^*(a)=\sup_\lambda(a\lambda-\log\cosh\lambda)$ is at $\tanh\lambda=a$, giving $\psi^*(a)=\frac{1+a}2\log(1+a)+\frac{1-a}2\log(1-a)$ for $|a|<1$. For example $\Pr(S_n\ge0.2n)\approx e^{-n\psi^*(0.2)}$ with $\psi^*(0.2)=0.6\log1.2+0.4\log0.8\approx0.0201$, which is the relative entropy of a $0.6$-biased coin against a fair one.

:::
