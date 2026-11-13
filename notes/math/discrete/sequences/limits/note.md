---
title: "Limits of infinite sequences"
sources: [fit1058-cn-6.8]
requires: [math/discrete/logic/predicate/multiple-quantifiers]
status: draft
---

<!-- Migrated from 1058note notes/chapters/06-sequences-series.tex: Limits of infinite sequences. -->

::: {#def-limit-of-a-sequence .definition name="Limit of a sequence"}

$(a_n)$ has *limit* $\ell$, written $\lim_{n\to\infty}a_n=\ell$ or $a_n\to\ell$, if
$$\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\ge N\quad |a_n-\ell|<\varepsilon.$$
If such an $\ell$ exists, $(a_n)$ is *convergent*; otherwise it is *divergent*.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1]
 \draw[-{Latex}] (0,0) -- (9,0) node[right] {$n$};
 \draw[-{Latex}] (0,-1.6) -- (0,2.6) node[above] {$a_n$};
 \draw[dashed] (0,1.5) -- (9,1.5) node[right] {$\ell$};
 \fill[gray!15] (0,1.1) rectangle (9,1.9);
 \draw[dashed,gray] (0,1.9) -- (9,1.9) node[right] {$\ell+\varepsilon$};
 \draw[dashed,gray] (0,1.1) -- (9,1.1) node[right] {$\ell-\varepsilon$};
 \draw[dashed] (4.3,0) -- (4.3,2.6);
 \node[below] at (4.3,0) {$N$};
 \foreach \x/\y in {0.5/-1.2, 1.1/2.4, 1.8/-0.6, 2.5/2.0, 3.2/0.4, 3.9/1.9}
   \fill (\x,\y) circle (2pt);
 \foreach \x/\y in {4.6/1.65, 5.2/1.35, 5.8/1.55, 6.4/1.42, 7.0/1.58, 7.6/1.48, 8.2/1.53}
   \fill (\x,\y) circle (2pt);
 \node[align=center,font=\small] at (2.1,-1.4) {terms with $n<N$:\\ may lie outside the band};
 \node[align=center,font=\small] at (6.4,-1.4) {terms with $n\ge N$:\\ all lie within $(\ell-\varepsilon,\ell+\varepsilon)$};
\end{tikzpicture}
\end{center}
```

::: {.remark name="Reading the quantifiers"}

However narrow a band $(\ell-\varepsilon,\ell+\varepsilon)$ is chosen, from some point $N$ onwards *all* terms lie inside it. The order of quantifiers matters (@sec-math-discrete-logic-predicate-multiple-quantifiers): $N$ may depend on $\varepsilon$. This is exactly the Limit Game of Exercise 6.10: Una picks $\varepsilon$, then Lim picks $N$.

:::

::: {#exm-limits-1 .example}

$\lim_{n\to\infty} \frac1n = 0$: given $\varepsilon>0$, take an integer $N>1/\varepsilon$. Then for $n\ge N$, $|1/n-0|\le1/N<\varepsilon$.

:::

::: {#exm-limits-2 .example}

$\lim_{n\to\infty}\frac{n}{n+1}=1$: given $\varepsilon>0$, we have $\left|\frac{n}{n+1}-1\right| = \frac{1}{n+1} < \varepsilon$ whenever $n > \frac1\varepsilon-1$, so take any integer $N>\frac1\varepsilon-1$.

:::

::: {#exm-limits-3 .example}

$(-1)^n$ is divergent: its terms alternate between $-1$ and $1$, so no band of width less than $2$ contains all terms from some point on.

:::
