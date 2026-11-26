---
title: "Sieve of Eratosthenes"
sources: []
requires: [math/discrete/number-theory/divisibility-and-primes]
status: draft
---

<!-- Added 2026-11-26 for the CSES number-theory problems, in our own wording. TODO: add a source. -->

To find all primes up to $N$, testing each number by trial division costs about $N\sqrt N$ operations. The sieve of Eratosthenes crosses out multiples instead.

::: {#def-sieve .definition name="Sieve of Eratosthenes"}

Start with the list $2,3,\dots,N$, all unmarked. For $p=2,3,\dots,\lfloor\sqrt N\rfloor$: if $p$ is unmarked, mark the numbers $p^2,\,p^2+p,\,p^2+2p,\dots\le N$. The unmarked numbers at the end are the primes up to $N$.

:::

::: {#thm-sieve .theorem name="Correctness and cost of the sieve"}

The unmarked numbers are exactly the primes in $[2,N]$, and the sieve takes $O(N\log\log N)$ time and $O(N)$ memory.

:::

::: {.proof}

1. *Primes stay unmarked.* A number is only marked as a multiple $kp$ with $k\ge p\ge2$ of some $p$, so it has a divisor $1<p<kp$ and is composite.

2. *Composites get marked.* Let $n\le N$ be composite and $p$ its smallest prime factor. As in the proof that a composite $n$ has a prime divisor at most $\sqrt n$ (see @thm-primefactexists), $p\le\sqrt n\le\sqrt N$, and $n=p\cdot k$ with $k\ge p$ because every prime factor of $k$ is at least $p$. Hence $n\ge p^2$ is among the multiples marked from $p^2$. The number $p$ itself is unmarked when its turn comes, by step 1 and induction on the smaller primes.

3. *Time.* A prime $p\le\sqrt N$ marks at most $N/p$ numbers, so the total is at most $N\sum_{p\le N}1/p=O(N\log\log N)$ by Mertens' estimate of the sum of reciprocals of primes.

:::

::: {#exm-sieve-1 .example name="Primes up to 30"}

Mark from $4$ (multiples of $2$), then $9$ (multiples of $3$), then $25$ (multiples of $5$). The unmarked numbers are $2,3,5,7,11,13,17,19,23,29$. Since $7^2=49>30$ the loop stops at $5$.

:::

::: {#fig-sieve-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.62cm,y=0.62cm]
\foreach \n in {2,...,30} {
  \pgfmathtruncatemacro{\r}{int((\n-2)/10)}
  \pgfmathtruncatemacro{\c}{mod(\n-2,10)}
  \draw[cell frame] (\c,-\r) rectangle +(1,1);
  \node[lab] at (\c+0.5,-\r+0.5) {$\n$};
}
\foreach \n in {2,3,5,7,11,13,17,19,23,29} {
  \pgfmathtruncatemacro{\r}{int((\n-2)/10)}
  \pgfmathtruncatemacro{\c}{mod(\n-2,10)}
  \draw[hl cell] (\c,-\r) rectangle +(1,1);
  \node[lab] at (\c+0.5,-\r+0.5) {$\n$};
}
\end{tikzpicture}
\end{center}
```

@exm-sieve-1: the numbers that survive the sieve for $N=30$ are highlighted.

:::

::: {#rmk-sieve-1 .remark name="Smallest prime factor table"}

Storing in each cell the prime that first marked it gives the smallest prime factor $\operatorname{spf}(n)$ of every $n\le N$. Then $n$ factorises in $O(\log n)$ divisions by repeatedly dividing by $\operatorname{spf}(n)$, and from the factorisation $n=\prod p_i^{e_i}$ the number of divisors is $\prod(e_i+1)$. Another use: for the number of multiples counted by value, $\sum_{d} \lfloor N/d\rfloor$ steps take $O(N\log N)$ in total, which makes "for every $d$, look at all multiples of $d$" feasible for $N$ up to about $10^6$ to $10^7$.

:::
