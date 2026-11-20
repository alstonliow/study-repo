---
title: "Reversible Markov Chains"
sources: [eecs126-4]
requires: [math/probability/markov-chains/invariant-distributions]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Reversible Markov Chains", in our own wording; proofs written out in steps. -->

Solving $\pi P=\pi$ (@def-invariant-distribution) means solving one equation per state, each involving all its neighbours. Many chains satisfy a stronger, edge-by-edge balance that is much easier to solve.

::: {#def-detailed-balance .definition name="Detailed balance, reversible chain"}

A distribution $\pi$ satisfies the *detailed balance equations* for the transition matrix $P$ if
$$\pi(i)P(i,j)=\pi(j)P(j,i)\quad\text{for all states }i,j.$$
A chain started from such a $\pi$ is called *reversible*.

:::

::: {#thm-detailed-balance-invariant .theorem name="Detailed balance implies invariance"}

If $\pi$ satisfies the detailed balance equations, then $\pi$ is an invariant distribution, and the chain started from $\pi$ has the same law run forwards and backwards in time:
$$\Pr(X_0=i_0,\dots,X_n=i_n)=\Pr(X_0=i_n,\dots,X_n=i_0).$$

:::

::: {.proof}

1. Summing detailed balance over $i$: $\sum_i\pi(i)P(i,j)=\pi(j)\sum_iP(j,i)=\pi(j)$, so $\pi P=\pi$.

2. By @prp-markov-path-probability, $\Pr(X_0=i_0,\dots,X_n=i_n)=\pi(i_0)P(i_0,i_1)\cdots P(i_{n-1},i_n)$.

3. Apply detailed balance to the first factor pair, $\pi(i_0)P(i_0,i_1)=\pi(i_1)P(i_1,i_0)$, then to $\pi(i_1)P(i_1,i_2)$, and so on along the path. After $n$ steps the product is $\pi(i_n)P(i_n,i_{n-1})\cdots P(i_1,i_0)$, the probability of the reversed path.

:::

::: {#thm-kolmogorov-criterion .theorem name="Kolmogorov's criterion"}

An irreducible chain with an invariant distribution is reversible if and only if for every cycle of states $i_0,i_1,\dots,i_n=i_0$
$$P(i_0,i_1)P(i_1,i_2)\cdots P(i_{n-1},i_0)=P(i_0,i_{n-1})\cdots P(i_2,i_1)P(i_1,i_0).$$

:::

::: {.proof}

1. *Only if.* Multiply detailed balance along the cycle as in @thm-detailed-balance-invariant; the factors $\pi(i_0)=\pi(i_n)$ cancel.

2. *If.* Fix a state $o$. For each $j$ choose a path $o=j_0,\dots,j_m=j$ with positive probabilities and set $\pi(j)\propto\prod_kP(j_k,j_{k+1})/P(j_{k+1},j_k)$. The cycle condition says this does not depend on the chosen path (two paths form a cycle); the reverse probabilities are positive because, by the cycle condition, a positive forward cycle has a positive reverse cycle.

3. For neighbours $i,j$, extend the path to $i$ by the step $i\to j$: $\pi(j)=\pi(i)P(i,j)/P(j,i)$, which is detailed balance. If $P(i,j)=0$, the cycle condition forces $P(j,i)=0$ too. Normalising gives the invariant distribution.

:::

::: {#exm-random-walk-on-graph .example name="Random walk on a graph"}

On a connected undirected graph, move from a vertex $v$ to a uniformly random neighbour, $P(u,v)=1/\deg u$ for each edge $uv$. Then $\pi(v)=\deg v/(2|E|)$ satisfies detailed balance: $\pi(u)P(u,v)=1/(2|E|)=\pi(v)P(v,u)$. On a star with centre $c$ and three leaves, $\pi(c)=\tfrac36=\tfrac12$ and each leaf has $\tfrac16$.

:::

::: {#fig-reversible-markov-chains-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hl ball] (c) at (0,0) {$c$};
\foreach \a/\n in {90/1,210/2,330/3} \node[small vertex] (l\n) at (\a:1.8) {};
\foreach \n in {1,2,3} { \draw[->] (c) to[bend left=12] (l\n); \draw[->] (l\n) to[bend left=12] (c); }
\node[lab, left] at (-0.45,0.35) {$\pi(c)=\frac12$};
\foreach \a/\n in {90/1,210/2,330/3} \node[lab] at (\a:2.45) {$\frac16$};
\node[edge label] at (0.55,1.0) {$\frac13$}; \node[edge label] at (-0.05,1.1) {$1$};
\end{tikzpicture}
\end{center}
```

Random walk on a star with three leaves (@exm-random-walk-on-graph). From the centre each leaf is chosen with probability $\frac13$; from a leaf the walk returns with probability $1$. The stationary probabilities are proportional to the degrees: $\frac36$ for the centre and $\frac16$ for each leaf.

:::

::: {#rmk-reversible-markov-chains-trees .remark name="Trees and birth–death chains"}

Every chain whose transition graph (edges where $P(i,j)>0$) is a tree is reversible: a tree has no cycles of length more than two, so Kolmogorov's criterion holds trivially. Birth–death chains (@exm-birth-death-chain) are the main example; this is why their balance equations reduce to $\pi(i)p_i=\pi(i+1)q_{i+1}$.

:::
