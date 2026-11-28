---
title: "Hitting Times and Hitting Probabilities"
sources: [cs70-21]
requires: [math/probability/markov-chains/finite-markov-chains, math/probability/random-variables/expectation-and-variance]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 21 (cs70-21), in our own wording; proofs written out in steps. -->

Many questions about a Markov chain ask how long it takes to reach a set of states, or which of two sets it reaches first. Both are answered by conditioning on the first step.

::: {#def-hitting-time .definition name="Hitting time"}

For a set of states $A\subseteq\mathcal X$, the *hitting time* of $A$ is $T_A=\min\{n\ge0:X_n\in A\}$ (and $T_A=\infty$ if the chain never enters $A$). Write $\Pr_i$ and $E_i$ for probabilities and expectations when the chain starts at $X_0=i$, and let
$$\beta(i)=E_i[T_A]$$
be the *mean hitting time* from $i$.

:::

::: {#prp-markov-fresh-start .proposition name="Fresh start after one step"}

Let $j$ be a state with $P(i,j)>0$. Given $X_0=i$ and $X_1=j$, the process $X_1,X_2,\dots$ has the same distribution as the chain started at $j$: for all states $i_2,\dots,i_n$,
$$\Pr_i(X_2=i_2,\dots,X_n=i_n\mid X_1=j)=\Pr_j(X_1=i_2,\dots,X_{n-1}=i_n).$$

:::

::: {.proof}

1. By @prp-markov-path-probability with $\pi_0(i)=1$, the probability of $X_1=j,X_2=i_2,\dots,X_n=i_n$ is $P(i,j)P(j,i_2)\cdots P(i_{n-1},i_n)$, and $\Pr_i(X_1=j)=P(i,j)$.

2. Dividing, the conditional probability is $P(j,i_2)\cdots P(i_{n-1},i_n)$, which is the probability of the path $j,i_2,\dots,i_n$ for the chain started at $j$ (@prp-markov-path-probability again).

:::

::: {#thm-first-step-hitting-time .theorem name="First step equations for mean hitting times"}

If $\beta(i)<\infty$ for every state $i$, then
$$\beta(i)=0\quad(i\in A),\qquad \beta(i)=1+\sum_{j}P(i,j)\beta(j)\quad(i\notin A).$$

:::

::: {.proof}

1. If $i\in A$, then $T_A=0$ when $X_0=i$.

2. Let $i\notin A$. Then $T_A\ge1$, and $T_A=1+T'$, where $T'$ is the number of further steps after time $1$ until the chain enters $A$.

3. Split according to $X_1$ (@thm-law-of-total-probability): for each $t$,
   $$\Pr_i(T'=t)=\sum_{j:\,P(i,j)>0}P(i,j)\Pr_i(T'=t\mid X_1=j).$$

4. By @prp-markov-fresh-start, given $X_1=j$, $T'$ has the distribution of $T_A$ for the chain started at $j$. So $\Pr_i(T'=t\mid X_1=j)=\Pr_j(T_A=t)$.

5. Multiply step 3 by $t$ and sum over $t$; all terms are non-negative, so the sums may be exchanged:
   $$E_i[T']=\sum_jP(i,j)\sum_t t\Pr_j(T_A=t)=\sum_jP(i,j)\beta(j).$$

6. By linearity (@thm-linearity-of-expectation), $\beta(i)=1+E_i[T']=1+\sum_jP(i,j)\beta(j)$.

:::

::: {#fig-hitting-times-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (i) at (0,0) {$i$};
\node[box] (j0) at (3.6,1.3) {$h_{j_1}$};
\draw[map] (i) -- node[edge label] {$P_{ij_1}$} (j0.west);
\node[box] (j1) at (3.6,0) {$h_{j_2}$};
\draw[map] (i) -- node[edge label] {$P_{ij_2}$} (j1.west);
\node[box] (j2) at (3.6,-1.3) {$h_{j_3}$};
\draw[map] (i) -- node[edge label] {$P_{ij_3}$} (j2.west);
\node[tick, below] at (0,-0.4) {one step};
\end{tikzpicture}
\end{center}
```

First-step analysis: from $i$ the chain spends one step, then continues from a neighbour $j$ with expected remaining time $h_j$, so $h_i=1+\sum_jP_{ij}h_j$

:::

::: {#thm-first-step-hitting-probability .theorem name="First step equations for hitting probabilities"}

Let $A,B\subseteq\mathcal X$ be disjoint, and let $\alpha(i)$ be the probability, starting from $i$, that the chain enters $A$ before it enters $B$. Then
$$\alpha(i)=1\ (i\in A),\qquad\alpha(i)=0\ (i\in B),\qquad \alpha(i)=\sum_jP(i,j)\alpha(j)\ \ (i\notin A\cup B).$$

:::

::: {.proof}

1. If $i\in A$, the chain is already in $A$; if $i\in B$, it entered $B$ first.

2. Let $i\notin A\cup B$, and let $W$ be the event "enters $A$ before $B$". By @thm-law-of-total-probability,
   $$\alpha(i)=\Pr_i(W)=\sum_{j:\,P(i,j)>0}P(i,j)\Pr_i(W\mid X_1=j).$$

3. Since $X_0=i$ is in neither set, $W$ depends only on $X_1,X_2,\dots$. By @prp-markov-fresh-start, $\Pr_i(W\mid X_1=j)=\alpha(j)$.

:::

::: {#rmk-hitting-times-solving}

1. The first step equations are linear, so one solves them like any linear system; often symmetry or a recurrence shortens the work (@exm-two-heads, @exm-gamblers-ruin).

2. @thm-first-step-hitting-time assumes the means are finite. For a finite chain from which $A$ is reachable from every state, this holds, and the equations then have exactly one solution; we do not prove this here.

:::
