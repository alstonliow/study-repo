---
title: "Periodicity and Convergence"
sources: [cs70-21]
requires: [math/probability/markov-chains/invariant-distributions, math/discrete/number-theory/extended-euclidean-algorithm]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 21 (cs70-21 and its appendix), in our own wording; proofs written out in steps. -->

For an irreducible chain, the *fraction of time* in each state converges (@thm-markov-fraction-of-time), but $\Pr(X_n=i)$ itself need not. The two-state chain with $a=1$ switches at every step: started at $0$, $\Pr(X_n=0)$ is $1$ for even $n$ and $0$ for odd $n$. The obstacle is periodicity.

::: {#def-period .definition name="Period, aperiodic"}

For a state $i$ let $S(i)=\{n\ge1:P^n(i,i)>0\}$, the lengths of the possible returns to $i$, and let $d(i)=\gcd S(i)$ be the *period* of $i$. An irreducible chain is *aperiodic* if $d(i)=1$ for some (by @prp-period-class, every) state $i$, and *periodic with period $d$* otherwise.

:::

::: {#fig-periodicity-and-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=2.2cm]
\draw[->, muted] (0,0) -- (7.2,0) node[lab, right] {$n$};
\draw[->, muted] (0,0) -- (0,1.25);
\draw[gridline, dashed] (0,0.5) -- (7,0.5);
\node[tick, left] at (0,1) {$1$}; \node[tick, left] at (0,0.5) {$\frac12$}; \node[tick, left] at (0,0) {$0$};
\foreach \n in {0,2,...,12} \node[tick, below] at (\n*0.55,0) {$\n$};
\fill[accent] (0.00,1) circle[pt]; \fill[accent] (0.55,0) circle[pt]; \fill[accent] (1.10,1) circle[pt]; \fill[accent] (1.65,0) circle[pt]; \fill[accent] (2.20,1) circle[pt]; \fill[accent] (2.75,0) circle[pt]; \fill[accent] (3.30,1) circle[pt]; \fill[accent] (3.85,0) circle[pt]; \fill[accent] (4.40,1) circle[pt]; \fill[accent] (4.95,0) circle[pt]; \fill[accent] (5.50,1) circle[pt]; \fill[accent] (6.05,0) circle[pt]; \fill[accent] (6.60,1) circle[pt];
\fill[primary] (0.00,1.0000) circle[pt]; \fill[primary] (0.55,0.7000) circle[pt]; \fill[primary] (1.10,0.5800) circle[pt]; \fill[primary] (1.65,0.5320) circle[pt]; \fill[primary] (2.20,0.5128) circle[pt]; \fill[primary] (2.75,0.5051) circle[pt]; \fill[primary] (3.30,0.5020) circle[pt]; \fill[primary] (3.85,0.5008) circle[pt]; \fill[primary] (4.40,0.5003) circle[pt]; \fill[primary] (4.95,0.5001) circle[pt]; \fill[primary] (5.50,0.5001) circle[pt]; \fill[primary] (6.05,0.5000) circle[pt]; \fill[primary] (6.60,0.5000) circle[pt];
\node[lab, accent, anchor=west] at (7.3,1) {$a=1$};
\node[lab, primary, anchor=west] at (7.3,0.5) {$a=0.3$};
\end{tikzpicture}
\end{center}
```

$\Pr(X_n=0)$ for the two-state chain started at $0$. With $a=1$ (period $2$) it alternates between $1$ and $0$; with $a=0.3$ (aperiodic) it converges to $\frac12$.

:::

The two-state chain with $a=1$ has $S(0)=\{2,4,6,\dots\}$, so $d(0)=2$. With $0<a<1$, $S(0)=\{1,2,3,\dots\}$ and $d(0)=1$. In @exm-web-chain-invariant, $A$ returns to itself in $2$ steps ($A\to D\to A$) and in $3$ steps ($A\to B\to C\to A$), so $d(A)=1$.

::: {#prp-period-class .proposition name="All states have the same period"}

In an irreducible chain, $d(i)=d(j)$ for all states $i,j$.

:::

::: {.proof}

1. $S(i)$ is closed under addition: two returns to $i$ in a row form a return, and $P^{m+n}(i,i)\ge P^m(i,i)P^n(i,i)$.

2. By irreducibility there are $a,b\ge1$ with $P^a(j,i)>0$ and $P^b(i,j)>0$. Going $j\to i\to j$ gives $a+b\in S(j)$; going $j\to i$, then a return to $i$ of length $n\in S(i)$, then $i\to j$, gives $a+n+b\in S(j)$.

3. $d(j)$ divides every element of $S(j)$, so it divides $a+b$ and $a+n+b$, hence their difference $n$. This holds for every $n\in S(i)$, so $d(j)$ divides $d(i)$.

4. Exchanging $i$ and $j$, $d(i)$ divides $d(j)$. Both are positive, so $d(i)=d(j)$.

:::

::: {#lem-aperiodic-all-large-returns .lemma name="Aperiodic states return at all large times"}

If $d(i)=1$, there is an $N$ such that every $n\ge N$ lies in $S(i)$.

:::

::: {.proof}

1. The gcd of the first $r$ elements of $S(i)$ decreases as $r$ grows and stays a positive integer, so it is eventually equal to $d(i)=1$: some finite $s_1,\dots,s_r\in S(i)$ have gcd $1$.

2. Applying @thm-bezout repeatedly ($\gcd(s_1,\dots,s_r)=\gcd(\gcd(s_1,\dots,s_{r-1}),s_r)$), there are integers $c_1,\dots,c_r$ with $\sum_k c_ks_k=1$.

3. Let $A=\sum_{c_k>0}c_ks_k$ and $B=\sum_{c_k<0}(-c_k)s_k$, so $A-B=1$. If $B=0$, then $1=A\in S(i)$ and, by closure under addition, $S(i)$ contains every $n\ge1$. Otherwise $k=B$ and $k+1=A$ are both in $S(i)$, by closure under addition.

4. Let $n\ge k^2$ and divide: $n=qk+r$ with $0\le r<k$. Then $q\ge k>r$, and
   $$n=(q-r)k+r(k+1)$$
   is a sum of elements of $S(i)$ with $q-r\ge1$, so $n\in S(i)$. Take $N=k^2$.

:::

::: {#thm-markov-convergence .theorem name="Convergence to the invariant distribution"}

Let a finite Markov chain be irreducible and aperiodic, with invariant distribution $\pi$. Then for every initial distribution,
$$\Pr(X_n=i)\to\pi(i)\qquad\text{as }n\to\infty,\ \text{for every state }i.$$

:::

::: {#rmk-markov-convergence-coupling .remark name="Why it is true: coupling (sketch)"}

1. Fix a state $i$. By @lem-aperiodic-all-large-returns for every state and irreducibility, there is a single $k$ such that from *every* state $j$ the chain can be at $i$ after exactly $k$ steps ($j\to i$ in some number of steps, padded by returns to $j$ of every large length).

2. Run two independent copies: $X_n$ started from $\pi$, and $Z_n$ started from $\pi_0$. In each block of $k$ steps both copies are at $i$ at the end with probability at least some $p>0$, so the meeting time $\tau=\min\{n:X_n=Z_n\}$ satisfies $\Pr(\tau>km)\le(1-p)^m\to0$.

3. Let $Y_n=Z_n$ for $n<\tau$ and $Y_n=X_n$ for $n\ge\tau$. By the Markov property $Y$ is again a chain with matrix $P$ and initial distribution $\pi_0$, and $|\Pr(Y_n=i)-\Pr(X_n=i)|\le\Pr(\tau>n)\to0$.

4. $\Pr(X_n=i)=\pi(i)$ for all $n$ (@thm-invariant-iff-constant), so $\Pr(Y_n=i)\to\pi(i)$.

:::

So in @exm-web-chain-invariant, $\Pr(X_n=A)\to\frac{12}{39}$ from any starting page, even though computing $\pi_0P^n$ by hand is hard.
