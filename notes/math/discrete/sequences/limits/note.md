---
title: "Limits of infinite sequences"
sources: [fit1058-cn-6.8]
requires: [math/discrete/sequences/basic-sequences, math/discrete/logic/predicate/multiple-quantifiers, math/discrete/proof/induction-examples]
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
 \fill[primarySoft] (0,1.1) rectangle (9,1.9);
 \draw[dashed,muted] (0,1.9) -- (9,1.9) node[right] {$\ell+\varepsilon$};
 \draw[dashed,muted] (0,1.1) -- (9,1.1) node[right] {$\ell-\varepsilon$};
 \draw[dashed] (4.3,0) -- (4.3,2.6);
 \node[below] at (4.3,0) {$N$};
 \foreach \x/\y in {0.5/-1.2, 1.1/2.4, 1.8/-0.6, 2.5/2.0, 3.2/0.4, 3.9/1.9}
   \fill (\x,\y) circle[pt];
 \foreach \x/\y in {4.6/1.65, 5.2/1.35, 5.8/1.55, 6.4/1.42, 7.0/1.58, 7.6/1.48, 8.2/1.53}
   \fill (\x,\y) circle[pt];
 \node[align=center,lbl] at (2.1,-1.4) {terms with $n<N$:\\ may lie outside the band};
 \node[align=center,lbl] at (6.4,-1.4) {terms with $n\ge N$:\\ all lie within $(\ell-\varepsilon,\ell+\varepsilon)$};
\end{tikzpicture}
\end{center}
```

::: {#rmk-limits-1 .remark name="Reading the quantifiers"}

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

<!-- Added 2026-11-15 from CN §6.8 (own wording and proofs). -->

## Basic limits and limit laws

::: {#thm-limit-geometric .theorem name="Limit of $r^n$"}

If $-1 < r < 1$, then
$$\lim_{n\to\infty} r^n = 0.$$

:::

::: {.proof}

1. If $r = 0$, every term is $0$. Otherwise write $|r| = \frac{1}{1+h}$ with $h > 0$.

2. By Bernoulli's inequality (@exm-bernoulli-s-inequality-extra), $(1+h)^n \ge 1 + nh > nh$.

3. So $|r^n - 0| = \frac{1}{(1+h)^n} < \frac{1}{nh}$.

4. Given $\varepsilon > 0$, take an integer $N > \frac{1}{h\varepsilon}$. For $n \ge N$, $|r^n| < \frac{1}{nh} \le \frac{1}{Nh} < \varepsilon$.

:::

::: {#prp-limit-laws .proposition name="Limit laws"}

If $\lim_{n\to\infty} a_n = a$ and $\lim_{n\to\infty} b_n = b$, then
$$\lim_{n\to\infty}(a_n + b_n) = a + b, \qquad \lim_{n\to\infty}(a_n - b_n) = a - b, \qquad \lim_{n\to\infty} a_n b_n = ab,$$
and, if $b_n \ne 0$ for all $n$ and $b \ne 0$,
$$\lim_{n\to\infty} \frac{a_n}{b_n} = \frac{a}{b}.$$

:::

::: {.proof}

1. Sum: given $\varepsilon > 0$, choose $N_1$ with $|a_n - a| < \varepsilon/2$ for $n \ge N_1$, and $N_2$ with $|b_n - b| < \varepsilon/2$ for $n \ge N_2$.

2. For $n \ge \max(N_1, N_2)$, the triangle inequality gives $|(a_n + b_n) - (a+b)| \le |a_n - a| + |b_n - b| < \varepsilon$.

3. The difference is the same argument. The product and quotient laws are proved in the same spirit, with more careful bounds; we use them without proof.

:::

::: {#thm-limit-nth-root .theorem name="Limit of the $n$-th root"}

If $r > 0$, then
$$\lim_{n\to\infty} r^{1/n} = 1.$$
Here $r^{1/n}$ is the positive $n$-th root of $r$.

:::

::: {.proof}

1. Case $r \ge 1$. Write $r^{1/n} = 1 + d_n$ with $d_n \ge 0$.

2. By Bernoulli's inequality, $r = (1 + d_n)^n \ge 1 + n d_n$, so $0 \le d_n \le \frac{r-1}{n}$.

3. Given $\varepsilon > 0$, take an integer $N > \frac{r-1}{\varepsilon}$. For $n \ge N$, $|r^{1/n} - 1| = d_n \le \frac{r-1}{N} < \varepsilon$.

4. Case $0 < r < 1$. Then $1/r > 1$, so $(1/r)^{1/n} \to 1$ by the first case. Since $r^{1/n} = \frac{1}{(1/r)^{1/n}}$, the quotient law (@prp-limit-laws) gives $r^{1/n} \to \frac{1}{1} = 1$.

:::

::: {#rmk-limits-2 .remark name="Why $r > 0$"}

For $r < 0$ an $n$-th root may not be a positive real number, or not real at all, so the statement is restricted to $r > 0$.

:::

::: {#exm-limits-combined .example}

$$\lim_{n\to\infty}\left(5^{1/n} + \left(\tfrac{2}{3}\right)^n\right) = \lim_{n\to\infty} 5^{1/n} + \lim_{n\to\infty}\left(\tfrac{2}{3}\right)^n = 1 + 0 = 1,$$
by the sum law, @thm-limit-nth-root and @thm-limit-geometric.

:::

## Infinite limits

::: {#def-infinite-limit .definition name="Infinite limit"}

$(a_n)$ *tends to infinity*, written $\lim_{n\to\infty} a_n = \infty$, if
$$\forall M\ \exists N\in\mathbb{N}\ \forall n\ge N\quad a_n > M.$$
Similarly, $\lim_{n\to\infty} a_n = -\infty$ if $\forall M\ \exists N\ \forall n\ge N\ \ a_n < M$.

:::

::: {#exm-limits-infinite .example}

$\lim_{n\to\infty} n^2 = \infty$ and $\lim_{n\to\infty} (-n^2) = -\infty$. Such sequences are still divergent: they have no finite limit.

:::

::: {#rmk-limits-3 .remark name="Why we need more than \"$= \infty$\""}

Running times of algorithms usually grow without bound, but very differently:
$$\log n,\quad \sqrt n,\quad n,\quad n\log n,\quad n^2,\quad 2^n,\quad n!,\quad 2^{2^n}$$
all tend to $\infty$. Saying only that the limit is $\infty$ hides these differences. Big-O notation (@sec-math-discrete-sequences-big-o) describes *how fast* a sequence grows.

:::

