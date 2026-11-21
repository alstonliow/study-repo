---
title: "Hypergeometric Distribution"
sources: [cs70-15.2]
requires: [math/probability/discrete/binomial-distribution]
aliases: [math/probability/hypergeometric-distribution]   # old ids (moved)
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

::: {#fig-hypergeometric-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=8cm]
\fill[bar] (-0.3,0) rectangle (0,0.0511);
\draw[cell frame] (0,0) rectangle (0.3,0.0778);
\node[tick, below] at (0,0) {$0$};
\fill[bar] (0.7,0) rectangle (1,0.2554);
\draw[cell frame] (1,0) rectangle (1.3,0.2592);
\node[tick, below] at (1,0) {$1$};
\fill[bar] (1.7,0) rectangle (2,0.3973);
\draw[cell frame] (2,0) rectangle (2.3,0.3456);
\node[tick, below] at (2,0) {$2$};
\fill[bar] (2.7,0) rectangle (3,0.2384);
\draw[cell frame] (3,0) rectangle (3.3,0.2304);
\node[tick, below] at (3,0) {$3$};
\fill[bar] (3.7,0) rectangle (4,0.0542);
\draw[cell frame] (4,0) rectangle (4.3,0.0768);
\node[tick, below] at (4,0) {$4$};
\fill[bar] (4.7,0) rectangle (5,0.0036);
\draw[cell frame] (5,0) rectangle (5.3,0.0102);
\node[tick, below] at (5,0) {$5$};
\draw[muted] (-0.6,0) -- (5.6,0);
\fill[bar] (3.6,0.4) rectangle (3.85,0.43); \node[lab, anchor=west] at (3.9,0.415) {without replacement};
\draw[cell frame] (3.6,0.34) rectangle (3.85,0.37); \node[lab, anchor=west] at (3.9,0.355) {with replacement};
\end{tikzpicture}
\end{center}
```

Drawing $n=5$ balls from $N=20$, of which $B=8$ are black: $\mathrm{Hypergeometric}(20,8,5)$ without replacement, and $\mathrm{Bin}(5,0.4)$ with replacement. Without replacement the count is more concentrated around the mean $2$.

:::

::: {#rmk-hypergeometric-distribution-2 .remark name="Counting view"}

The formula also follows by counting sets: there are $\binom Nn$ equally likely sets of $n$ balls, and $\binom Bk\binom{N-B}{n-k}$ of them contain exactly $k$ black balls. $\Pr(Y=k)>0$ only when $\max(0,n+B-N)\le k\le\min(n,B)$.

:::

::: {#prp-hypergeometric-mean-variance .proposition name="Mean and variance of the hypergeometric distribution"}

If $Y\sim\mathrm{Hypergeometric}(N,B,n)$ and $p=\frac BN$, then
$$E[Y]=np,\qquad \mathrm{Var}(Y)=np(1-p)\,\frac{N-n}{N-1}.$$

:::

::: {.proof}

1. Number the draws $1,\dots,n$ and let $I_i$ indicate that draw $i$ is black, so $Y=I_1+\dots+I_n$. By symmetry each draw is equally likely to be any of the $N$ balls, so $\Pr(I_i=1)=p$, and $E[Y]=np$ by @thm-linearity-of-expectation.

2. For $i\ne j$, draws $i$ and $j$ are both black with probability $\frac BN\cdot\frac{B-1}{N-1}$. So
   $$\mathrm{Cov}(I_i,I_j)=\frac{B(B-1)}{N(N-1)}-p^2=-\frac{p(1-p)}{N-1}.$$

3. Expanding $\mathrm{Var}(Y)$ as the sum of all covariances $\mathrm{Cov}(I_i,I_j)$ (@prp-covariance-properties), with $\mathrm{Var}(I_i)=p(1-p)$:
   $$\mathrm{Var}(Y)=np(1-p)-n(n-1)\frac{p(1-p)}{N-1}=np(1-p)\,\frac{N-n}{N-1}.$$

:::

::: {#fig-hypergeometric-distribution-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (5.6,0) node[lab, right] {$k$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$\Pr(X=k)$};
\path[bar] (0.20,0) rectangle (0.50,0.307);
\path[hl cell] (0.50,0) rectangle (0.80,0.467);
\node[tick, below] at (0.5,0) {$0$};
\path[bar] (1.10,0) rectangle (1.40,1.533);
\path[hl cell] (1.40,0) rectangle (1.70,1.555);
\node[tick, below] at (1.4,0) {$1$};
\path[bar] (2.00,0) rectangle (2.30,2.384);
\path[hl cell] (2.30,0) rectangle (2.60,2.074);
\node[tick, below] at (2.3,0) {$2$};
\path[bar] (2.90,0) rectangle (3.20,1.430);
\path[hl cell] (3.20,0) rectangle (3.50,1.382);
\node[tick, below] at (3.2,0) {$3$};
\path[bar] (3.80,0) rectangle (4.10,0.325);
\path[hl cell] (4.10,0) rectangle (4.40,0.461);
\node[tick, below] at (4.1,0) {$4$};
\path[bar] (4.70,0) rectangle (5.00,0.022);
\path[hl cell] (5.00,0) rectangle (5.30,0.061);
\node[tick, below] at (5.0,0) {$5$};
\path[bar] (3.6,2.3) rectangle (3.8,2.45);
\node[tick, right] at (3.8,2.37) {hypergeometric};
\path[hl cell] (3.6,1.95) rectangle (3.8,2.1);
\node[tick, right] at (3.8,2.02) {$\operatorname{Bin}(5,0.4)$};
\end{tikzpicture}
\end{center}
```

Drawing $5$ of $20$ balls ($8$ black) without replacement (dark) against with replacement (light): both have mean $2$, but without replacement the spread is smaller by the factor $\tfrac{N-n}{N-1}=\tfrac{15}{19}$

:::

The factor $\frac{N-n}{N-1}<1$ (for $n>1$) is why drawing without replacement is more concentrated than the binomial $\mathrm{Bin}(n,p)$, and for $N$ much larger than $n$ the two distributions are almost the same.
