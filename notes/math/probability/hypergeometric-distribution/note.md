---
title: "Hypergeometric Distribution"
sources: [cs70-15.2]
requires: [math/probability/binomial-distribution]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 15 §2 (cs70-15.2), in our own wording; the proof is written out in steps. -->

## Sampling with and without replacement

::: {#rmk-hypergeometric-distribution-1 .remark name="With replacement: binomial"}

An urn holds $N$ balls, $B$ black and $N-B$ white. Draw $n$ balls *with* replacement and let $X$ be the number of black balls drawn. Every draw is black with probability $\frac BN$, independently of the others, so $X\sim\mathrm{Bin}\bigl(n,\frac BN\bigr)$ (@def-binomial-distribution). Without replacement the draws are no longer independent, and the distribution changes.

:::

::: {#def-hypergeometric-distribution .definition name="Hypergeometric distribution"}

Draw $n\le N$ balls *without* replacement from an urn with $B$ black and $N-B$ white balls, all orders equally likely. The number $Y$ of black balls drawn has the *hypergeometric distribution*, $Y\sim\mathrm{Hypergeometric}(N,B,n)$:
$$\Pr(Y=k)=\frac{\binom Bk\binom{N-B}{n-k}}{\binom Nn},\qquad k=0,1,\dots,n,$$
where $\binom mj=0$ when $j>m$.

:::

::: {.proof}

1. Consider one sequence of $n$ draws with $k$ black balls first and then $n-k$ white ones. By the product rule (@thm-chain-rule),
   $$\Pr=\frac{B}{N}\cdot\frac{B-1}{N-1}\cdots\frac{B-k+1}{N-k+1}\cdot\frac{N-B}{N-k}\cdots\frac{N-B-(n-k)+1}{N-n+1}=\frac{(B)_k\,(N-B)_{n-k}}{(N)_n},$$
   using falling factorials (@def-falling-factorial).

2. Any other sequence with $k$ black and $n-k$ white balls has the same probability. Its numerators are the same factors in a different order, and its denominators are again $N,N-1,\dots,N-n+1$.

3. There are $\binom nk$ such sequences, one for each choice of the $k$ draws that are black. They are mutually exclusive, so
   $$\Pr(Y=k)=\binom nk\frac{(B)_k\,(N-B)_{n-k}}{(N)_n}.$$

4. Writing $(m)_j=j!\binom mj$ (@prp-binomial-formula),
   $$\binom nk\frac{k!\binom Bk\,(n-k)!\binom{N-B}{n-k}}{n!\binom Nn}=\frac{\binom Bk\binom{N-B}{n-k}}{\binom Nn},$$
   since $\binom nk\,k!\,(n-k)!=n!$.

:::

::: {#rmk-hypergeometric-distribution-2 .remark name="Counting view"}

The formula also follows by counting sets: there are $\binom Nn$ equally likely sets of $n$ balls, and $\binom Bk\binom{N-B}{n-k}$ of them contain exactly $k$ black balls. $\Pr(Y=k)>0$ only when $\max(0,n+B-N)\le k\le\min(n,B)$.

:::
