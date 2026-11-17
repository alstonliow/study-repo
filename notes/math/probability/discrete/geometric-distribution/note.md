---
title: "Geometric Distribution"
sources: [fit1058-cn-10.10, cs70-19.1.1]
requires: [math/probability/discrete/expectation-and-variance]
aliases: [math/probability/geometric-distribution]   # old ids (moved)
status: draft
---

<!-- Split from math/probability/standard-distributions on 2026-11-16 (SPEC §2.6); block ids unchanged. -->
<!-- Migrated from 1058note notes/chapters/09-probability.tex: Geometric distribution. -->
<!-- Proof written out in steps; it follows CS70 Note 19 (cs70-19.1.1), in our own wording. -->

::: {#def-geometric-distribution .definition name="Geometric distribution"}

$X\sim\mathrm{Geom}(p)$ is the number of independent Bernoulli trials, each with success probability $p$, up to and including the first success:
$$\Pr(X=k) = (1-p)^{k-1}p, \qquad k=1,2,3,\dots$$

:::

```{=latex}
\begin{tikzpicture}[x=0.75cm, y=11cm, every node/.style={note}]
  \foreach \y in {0.1,0.2,0.3} {\draw[rule] (-0.6,\y) -- (10.6,\y); \node[left] at (-0.6,\y) {\y};}
  \draw (-0.6,0) -- (10.6,0);
  \foreach \k/\p in {1/0.300, 2/0.210, 3/0.147, 4/0.103, 5/0.072, 6/0.050, 7/0.035, 8/0.025, 9/0.017, 10/0.012} \fill[primaryStrong] (\k-0.32,0) rectangle (\k+0.32,\p);
  \foreach \k in {0,...,10} \node[below] at (\k,0) {\k};
  \draw[accent, dashed] (3.333,0) -- (3.333,0.31) node[above] {$E[X]=\tfrac{10}{3}$};
  \node[anchor=south, heading] at (5,0.36) {$\mathrm{Geom}(0.3)$ (continues past $10$)};
\end{tikzpicture}
```

::: {#rmk-standard-distributions-4 .remark name="Two conventions"}

Some books instead count the failures *before* the first success, which is $X-1$. Check which one is meant.

:::

::: {#exm-standard-distributions-1-4 .example}

For $p=0.3$:  $\Pr(X=6)=(0.7)^5\cdot0.3\approx0.050$.

:::

::: {#prp-standard-distributions-1-4 .proposition}

If $X\sim\mathrm{Geom}(p)$, then $E[X] = \dfrac1p$ and $\mathrm{Var}(X)=\dfrac{1-p}{p^2}$.

:::

::: {.proof}

Write $q=1-p$, so $0\le q<1$.

1. **Tails.** For $i\ge1$, the event $X\ge i$ means that the first $i-1$ trials all fail. The trials are independent, so
   $$\Pr(X\ge i)=q^{\,i-1}.$$

2. **Tail sum formula.** If $X$ takes values in $\{1,2,3,\dots\}$, then $E[X]=\sum_{i\ge1}\Pr(X\ge i)$. Indeed, write $j=\sum_{i=1}^{j}1$ and swap the order of summation (@exm-swapping-the-order-of-a):
   $$E[X]=\sum_{j\ge1}j\Pr(X=j)=\sum_{j\ge1}\sum_{i=1}^{j}\Pr(X=j)=\sum_{i\ge1}\sum_{j\ge i}\Pr(X=j)=\sum_{i\ge1}\Pr(X\ge i).$$
   All terms are non-negative, so swapping the order of an infinite double sum does not change its value.

3. **Expectation.** By steps 1–2 and @thm-convergence-condition (with ratio $q$, $|q|<1$),
   $$E[X]=\sum_{i\ge1}q^{\,i-1}=\frac1{1-q}=\frac1p.$$

4. **Second moment.** In the same way, write $j^2=\sum_{i=1}^{j}(2i-1)$ (the sum of the first $j$ odd numbers) and swap the order of summation:
   $$E[X^2]=\sum_{j\ge1}j^2\Pr(X=j)=\sum_{i\ge1}(2i-1)\Pr(X\ge i)=2\sum_{i\ge1}i\,q^{\,i-1}-\sum_{i\ge1}q^{\,i-1}.$$

5. **The remaining series.** By @def-geometric-distribution,
   $$E[X]=\sum_{i\ge1}i\,q^{\,i-1}p,$$
   so $\sum_{i\ge1}i\,q^{\,i-1}=\frac{E[X]}p=\frac1{p^2}$. In particular this series converges. Together with $\sum_{i\ge1}q^{\,i-1}=\frac1p$ from step 3,
   $$E[X^2]=\frac2{p^2}-\frac1p.$$

6. **Variance.** By @prp-expectation-and-variance-1,
   $$\mathrm{Var}(X)=E[X^2]-E[X]^2=\frac2{p^2}-\frac1p-\frac1{p^2}=\frac{1-p}{p^2}.$$

:::

::: {#rmk-geometric-distribution-first-step .remark name="The expectation from the first trial"}

There is a quick way to see $E[X]=\frac1p$. If the first trial succeeds, $X=1$. If it fails, one trial is used up and the process starts again, so on average $1+E[X]$ trials are needed. Hence
$$E[X]=p\cdot1+(1-p)\bigl(1+E[X]\bigr),$$
which gives $pE[X]=1$. This argument assumes that $E[X]$ is finite; the proof above shows that it is.

:::

::: {#rmk-standard-distributions-5 .remark name="Memoryless property"}

Given that the first $t$ trials have all failed, the number of further trials needed is again $\mathrm{Geom}(p)$: past failures do not make success “due”. Examples include the number of loop iterations until a random stopping condition holds, the number of time intervals until a component fails, and the number of balls a cricket batter faces.

:::
