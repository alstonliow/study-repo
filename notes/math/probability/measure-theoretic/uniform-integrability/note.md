---
title: "Uniform Integrability and Convergence in L1"
sources: [camii-pm-4]
requires: [math/analysis/measure-theory/lp-spaces, math/analysis/measure-theory/convergence-in-measure, math/probability/measure-theoretic/probability-spaces-and-independence]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 4.4, in our own wording; proofs written out in steps. -->

When does convergence in probability give convergence of expectations? The sequence $X_n=n\mathbf 1_{(0,1/n)}$ on $((0,1),\mathcal B,\lambda)$ tends to $0$ almost surely, yet $E[X_n]=1$: its mass concentrates on ever smaller events. Uniform integrability forbids exactly this. All random variables are real, on $(\Omega,\mathcal F,\Pr)$.

::: {#thm-bounded-convergence-probability .theorem name="Bounded convergence in probability"}

If $|X_n|\le C$ for a constant $C$ and $X_n\to X$ in probability, then $E|X_n-X|\to0$.

:::

::: {.proof}

1. For $\varepsilon>0$, $\Pr(|X|>C+\varepsilon)\le\Pr(|X-X_n|>\varepsilon)+\Pr(|X_n|>C)\to0$. So $|X|\le C$ a.s.

2. Split on the event $\{|X_n-X|>\varepsilon\}$: $E|X_n-X|\le\varepsilon+2C\,\Pr(|X_n-X|>\varepsilon)$, which is at most $2\varepsilon$ for large $n$.

:::

::: {#def-uniform-integrability .definition name="Uniform integrability"}

A family $\mathcal X$ of random variables is *uniformly integrable* (UI) if it is bounded in $L^1$, $\sup_{X\in\mathcal X}E|X|<\infty$, and

$$
I_{\mathcal X}(\delta)=\sup\big\{E[|X|\mathbf 1_A]:\ X\in\mathcal X,\ A\in\mathcal F,\ \Pr(A)\le\delta\big\}\to0\qquad(\delta\to0).
$$

:::

::: {#fig-uniform-integrability-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (4.6,0) node[lab, right] {$\omega$};
\draw[->] (0,-0.2) -- (0,3.6) node[lab, above] {};
\draw[faint] (0,0.40) -- (4.00,0.40) -- (4.00,0);
\draw[faint] (0,0.80) -- (2.00,0.80) -- (2.00,0);
\draw[emph] (0,1.60) -- (1.00,1.60) -- (1.00,0);
\draw[hl] (0,3.20) -- (0.50,3.20) -- (0.50,0);
\node[tick] at (4.0,-0.25) {$1$};
\node[lab, text=accent] at (2.2,3.2) {$X_8=8\cdot\mathbf 1_{(0,1/8)}$};
\end{tikzpicture}
\end{center}
```

$X_n=n\mathbf 1_{(0,1/n)}$ for $n=1,2,4,8$: each has expectation $1$, all of it on an event of probability $1/n$. Uniform integrability rules out exactly this concentration of mass on small events.

:::

::: {#lem-uniform-integrability-tails .lemma name="UI means uniformly small tails"}

$\mathcal X$ is uniformly integrable if and only if

$$
\sup_{X\in\mathcal X}E\big[|X|\mathbf 1_{\{|X|>K\}}\big]\to0\qquad(K\to\infty).
$$

:::

::: {.proof}

1. Suppose $\mathcal X$ is UI and $\sup E|X|=M$. By Markov's inequality (@thm-markov-inequality-measure) $\Pr(|X|>K)\le M/K$ for every $X\in\mathcal X$, so $E[|X|\mathbf 1_{\{|X|>K\}}]\le I_{\mathcal X}(M/K)\to0$.

2. Conversely, suppose the tail condition holds. Choose $K$ with all tails below $1$; then $E|X|\le K+1$, so $\mathcal X$ is $L^1$-bounded.

3. For any $A$ with $\Pr(A)\le\delta$ and any $K$,
$$E[|X|\mathbf 1_A]\le E[|X|\mathbf 1_{\{|X|>K\}}]+K\Pr(A)\le\sup_{Y\in\mathcal X}E[|Y|\mathbf 1_{\{|Y|>K\}}]+K\delta .$$
Given $\varepsilon$, pick $K$ to make the first term $\le\varepsilon/2$, then $\delta\le\varepsilon/(2K)$.

:::

::: {#prp-uniform-integrability-examples .proposition name="Sources of uniform integrability"}

1. A single integrable $X$, and any finite family of integrable variables, is UI.
2. If $\sup_{X\in\mathcal X}E|X|^p<\infty$ for some $p>1$, then $\mathcal X$ is UI.
3. If $|X|\le Y$ for all $X\in\mathcal X$ with $Y$ integrable, then $\mathcal X$ is UI.

:::

::: {.proof}

1. For one $X$, $|X|\mathbf 1_{\{|X|>K\}}\to0$ a.s. as $K\to\infty$ and is dominated by $|X|$, so its expectation tends to $0$ (@thm-dominated-convergence). For finitely many take the maximum.

2. On $\{|X|>K\}$, $|X|\le|X|^pK^{1-p}$, so $E[|X|\mathbf 1_{\{|X|>K\}}]\le K^{1-p}\sup E|X|^p\to0$.

3. $E[|X|\mathbf 1_{\{|X|>K\}}]\le E[Y\mathbf 1_{\{Y>K\}}]\to0$ by part 1.

:::

$L^1$-boundedness alone is not enough: the example $n\mathbf 1_{(0,1/n)}$ has $E|X_n|=1$ but $E[X_n\mathbf 1_{\{X_n>K\}}]=1$ for $n>K$.

::: {#thm-l1-convergence-ui .theorem name="Convergence in $L^1$ and uniform integrability"}

Let $X_n,X$ be random variables. The following are equivalent:

1. $X_n$ and $X$ are integrable and $E|X_n-X|\to0$;
2. $\{X_n\}$ is uniformly integrable and $X_n\to X$ in probability.

:::

::: {.proof}

1. *(1 ⇒ 2).* Markov gives $\Pr(|X_n-X|>\varepsilon)\le E|X_n-X|/\varepsilon\to0$. The family is $L^1$-bounded because $E|X_n|\le E|X|+E|X_n-X|$.

2. For UI, fix $\varepsilon$ and $N$ with $E|X_n-X|\le\varepsilon$ for $n>N$. The finite family $\{X,X_1,\dots,X_N\}$ is UI (@prp-uniform-integrability-examples), so there is $\delta$ with $E[|Y|\mathbf 1_A]\le\varepsilon$ for $Y$ in it and $\Pr(A)\le\delta$. For $n>N$, $E[|X_n|\mathbf 1_A]\le E[|X|\mathbf 1_A]+E|X_n-X|\le2\varepsilon$.

3. *(2 ⇒ 1).* By @thm-ae-and-in-measure a subsequence $X_{n_k}\to X$ a.s., so Fatou gives $E|X|\le\liminf_kE|X_{n_k}|<\infty$.

4. Truncate: $\phi_K(x)=\max(-K,\min(x,K))$, which is $1$-Lipschitz. Then
$$E|X_n-X|\le E|X_n-\phi_K(X_n)|+E|\phi_K(X_n)-\phi_K(X)|+E|\phi_K(X)-X| .$$

5. The first and last terms are at most $E[|X_n|\mathbf 1_{\{|X_n|>K\}}]$ and $E[|X|\mathbf 1_{\{|X|>K\}}]$, which are $\le\varepsilon$ for all $n$ once $K$ is large (@lem-uniform-integrability-tails, the family $\{X\}\cup\{X_n\}$ being UI).

6. $\phi_K(X_n)\to\phi_K(X)$ in probability and $|\phi_K(X_n)|\le K$, so the middle term tends to $0$ by @thm-bounded-convergence-probability. Hence $\limsup_nE|X_n-X|\le2\varepsilon$.

:::

In particular, if $X_n\to X$ in probability and $\sup_nE|X_n|^p<\infty$ for some $p>1$, then $E[X_n]\to E[X]$; this complements the remark on expectations in @sec-math-probability-continuous-modes-of-convergence.
