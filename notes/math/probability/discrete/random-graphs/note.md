---
title: "Random Graphs"
sources: [eecs126-5]
requires: [math/probability/discrete/concentration-inequalities]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Random Graphs", in our own wording; proofs written out in steps. -->

The Erdős–Rényi random graph is the simplest model of a random network. Many of its properties switch on abruptly as the edge probability crosses a threshold.

::: {#def-erdos-renyi-graph .definition name="Erdős–Rényi random graph"}

$G(n,p)$ is the random graph on vertices $\{1,\dots,n\}$ in which each of the $\binom n2$ possible edges is present with probability $p$, independently of the others.

:::

Each vertex has $\operatorname{Bin}(n-1,p)$ neighbours, so the mean degree is $(n-1)p$, and the expected number of edges is $\binom n2p$.

::: {#lem-second-moment-method .lemma name="First and second moment methods"}

Let $Z\ge0$ be an integer-valued random variable.

1. $\Pr(Z>0)\le E[Z]$.
2. If $E[Z]>0$, then $\Pr(Z=0)\le\dfrac{\operatorname{Var}(Z)}{E[Z]^2}$.

:::

::: {.proof}

1. $\mathbf 1\{Z>0\}\le Z$; take expectations (or use Markov's inequality, @thm-markov-inequality).

2. If $Z=0$ then $|Z-E[Z]|\ge E[Z]$, so Chebyshev's inequality (@thm-chebyshev-s-inequality) gives $\Pr(Z=0)\le\operatorname{Var}(Z)/E[Z]^2$.

:::

::: {#thm-connectivity-threshold .theorem name="Sharp threshold for connectivity"}

Let $p=p(n)=\lambda\dfrac{\ln n}{n}$ for a constant $\lambda>0$.

1. If $\lambda>1$, then $\Pr(G(n,p)\text{ is connected})\to1$.
2. If $\lambda<1$, then $\Pr(G(n,p)\text{ is connected})\to0$.

:::

We prove part 2 and the matching statement for isolated vertices, which is the heart of part 1: when $\lambda>1$ there are no isolated vertices, and one shows separately (by bounding the expected number of small components) that no other obstacle to connectivity survives.

::: {.proof}

1. Let $Z$ be the number of isolated vertices, $Z=\sum_v\mathbf 1_{A_v}$ with $A_v$ the event that $v$ has no neighbour. Then $\Pr(A_v)=(1-p)^{n-1}$ and $E[Z]=n(1-p)^{n-1}$.

2. Since $\ln(1-p)=-p+O(p^2)$ and $np^2\to0$, $E[Z]=n\,e^{-(n-1)p+O(np^2)}=n^{1-\lambda+o(1)}$. For $\lambda>1$ this tends to $0$, so by the first moment method there are no isolated vertices with probability tending to $1$.

3. For $\lambda<1$, $E[Z]\to\infty$. For $u\ne v$, $\Pr(A_u\cap A_v)=(1-p)^{2n-3}$ (the edge $uv$ is counted once), so
   $$E[Z^2]=E[Z]+n(n-1)(1-p)^{2n-3},\qquad\operatorname{Var}(Z)\le E[Z]+E[Z]^2\Bigl(\frac{1}{1-p}-1\Bigr).$$

4. Hence $\operatorname{Var}(Z)/E[Z]^2\le1/E[Z]+p/(1-p)\to0$, and by the second moment method $\Pr(Z=0)\to0$. A graph with an isolated vertex (and $n\ge2$) is disconnected, which proves part 2.

:::

::: {#exm-random-graphs-isolated .example name="A thousand vertices"}

With $n=1000$ and $\lambda=2$, $p=2\ln1000/1000\approx0.0138$, the mean degree is about $13.8$ and the expected number of isolated vertices is $1000(1-p)^{999}\approx9.2\times10^{-4}$. With $\lambda=\tfrac12$, $p\approx0.0035$ and the expected number of isolated vertices is about $31$.

:::

::: {#rmk-random-graphs-giant .remark name="Other thresholds"}

Thresholds are typical of $G(n,p)$. With $p=c/n$, if $c<1$ all components have $O(\ln n)$ vertices, while if $c>1$ one *giant component* has a constant fraction of the vertices; the size of that fraction is found from a branching-process (Poisson offspring) approximation of the neighbourhood of a vertex.

:::
