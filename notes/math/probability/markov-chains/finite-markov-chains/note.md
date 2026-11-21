---
title: "Finite Markov Chains"
sources: [cs70-21]
requires: [math/probability/discrete/random-variables]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 21 (cs70-21), in our own wording; proofs written out in steps. -->

A Markov chain is a random motion in a set of *states* in which the next step depends only on the current state, not on how the chain got there. Many questions have this form: how long until two heads in a row, how likely a gambler is to reach a target before going broke, how often a random web surfer sees a given page.

::: {#def-markov-chain .definition name="Finite Markov chain"}

Let $\mathcal X=\{1,\dots,K\}$ be a finite *state space*. A *transition probability matrix* is a $K\times K$ matrix $P$ with $P(i,j)\ge0$ and $\sum_{j}P(i,j)=1$ for every $i$ (each row is a distribution). An *initial distribution* is a row vector $\pi_0$ with $\pi_0(i)\ge0$ and $\sum_i\pi_0(i)=1$.

A sequence of random variables $X_0,X_1,X_2,\dots$ with values in $\mathcal X$ is a *Markov chain* with initial distribution $\pi_0$ and transition matrix $P$ if $\Pr(X_0=i)=\pi_0(i)$ and, for all $n\ge0$ and all states,
$$\Pr(X_{n+1}=j\mid X_n=i,\ X_{n-1}=i_{n-1},\dots,X_0=i_0)=P(i,j)$$
whenever the conditioning event has positive probability (the *Markov property*). $X_n$ is the *state at time $n$*.

:::

::: {#fig-finite-markov-chains-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,-0.3) -- (6.5,-0.3) node[lab, right] {$n$};
\draw[faint] (0,0.0) -- (6.2,0.0);
\node[tick, left] at (0,0.0) {$1$};
\draw[faint] (0,0.6) -- (6.2,0.6);
\node[tick, left] at (0,0.6) {$2$};
\draw[faint] (0,1.2) -- (6.2,1.2);
\node[tick, left] at (0,1.2) {$3$};
\draw[hl] (0.000,0.000) -- (0.250,0.000) -- (0.250,0.600) -- (0.500,0.600) -- (0.500,1.200) -- (0.750,1.200) -- (0.750,0.600) -- (1.000,0.600) -- (1.000,0.600) -- (1.250,0.600) -- (1.250,0.000) -- (1.500,0.000) -- (1.500,0.600) -- (1.750,0.600) -- (1.750,0.600) -- (2.000,0.600) -- (2.000,1.200) -- (2.250,1.200) -- (2.250,0.600) -- (2.500,0.600) -- (2.500,1.200) -- (2.750,1.200) -- (2.750,0.000) -- (3.000,0.000) -- (3.000,0.600) -- (3.250,0.600) -- (3.250,1.200) -- (3.500,1.200) -- (3.500,0.600) -- (3.750,0.600) -- (3.750,0.600) -- (4.000,0.600) -- (4.000,0.600) -- (4.250,0.600) -- (4.250,0.000) -- (4.500,0.000) -- (4.500,0.000) -- (4.750,0.000) -- (4.750,0.600) -- (5.000,0.600) -- (5.000,0.600) -- (5.250,0.600) -- (5.250,1.200) -- (5.500,1.200) -- (5.500,1.200) -- (5.750,1.200) -- (5.750,1.200) -- (6.000,1.200) -- (6.000,0.600) -- (6.200,0.600);
\end{tikzpicture}
\end{center}
```

A sample path of a three-state Markov chain: at each step the next state is drawn from the row of $P$ of the current state, ignoring the earlier history

:::

::: {#rmk-finite-markov-chains-diagram}

A Markov chain is drawn as its *state transition diagram*: a directed graph on $\mathcal X$ with an arrow $i\to j$, labelled $P(i,j)$, whenever $P(i,j)>0$. One way to run the chain: on arriving at state $i$, draw the next state from row $i$ of $P$, independently of everything before.

:::

::: {#prp-markov-path-probability .proposition name="Probability of a path"}

For all states $i_0,\dots,i_n$,
$$\Pr(X_0=i_0,X_1=i_1,\dots,X_n=i_n)=\pi_0(i_0)P(i_0,i_1)P(i_1,i_2)\cdots P(i_{n-1},i_n).$$

:::

::: {.proof}

1. By the product rule (@thm-chain-rule), the left side is
   $$\Pr(X_0=i_0)\prod_{m=1}^{n}\Pr(X_m=i_m\mid X_{m-1}=i_{m-1},\dots,X_0=i_0).$$

2. By @def-markov-chain, the first factor is $\pi_0(i_0)$ and the $m$-th conditional probability is $P(i_{m-1},i_m)$.

3. If some conditioning event has probability $0$, take the first $m$ for which $\Pr(X_0=i_0,\dots,X_m=i_m)=0$. By steps 1–2 for the path up to $m$, one of $\pi_0(i_0),P(i_0,i_1),\dots,P(i_{m-1},i_m)$ is $0$, so both sides are $0$.

:::

::: {#thm-markov-distribution-at-time-n .theorem name="Distribution at time $n$"}

Let $\pi_n$ be the distribution of $X_n$, as a row vector: $\pi_n(i)=\Pr(X_n=i)$. Then
$$\pi_n=\pi_0P^n\qquad(n\ge0).$$
In particular, $\Pr(X_n=j\mid X_0=i)=P^n(i,j)$ when $\pi_0(i)>0$.

:::

::: {.proof}

1. The event $X_n=i_n$ is the disjoint union, over all $i_0,\dots,i_{n-1}$, of the paths $X_0=i_0,\dots,X_n=i_n$. By @prp-markov-path-probability,
   $$\pi_n(i_n)=\sum_{i_0,\dots,i_{n-1}}\pi_0(i_0)P(i_0,i_1)\cdots P(i_{n-1},i_n).$$

2. By the definition of the matrix product, this sum is the entry $i_n$ of the row vector $\pi_0P\cdots P=\pi_0P^n$.

3. If $\pi_0(i)>0$, the same computation with the paths that start at $i$ gives $\Pr(X_0=i,X_n=j)=\pi_0(i)P^n(i,j)$; divide by $\pi_0(i)$.

:::

::: {#fig-finite-markov-chains-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\path[bar] (0.00,0) rectangle (0.45,2.000);
\path[hl cell] (0.00,2.000) rectangle (0.45,2);
\node[tick, below] at (0.22,0) {$0$};
\path[bar] (0.70,0) rectangle (1.15,1.400);
\path[hl cell] (0.70,1.400) rectangle (1.15,2);
\node[tick, below] at (0.92,0) {$1$};
\path[bar] (1.40,0) rectangle (1.85,1.040);
\path[hl cell] (1.40,1.040) rectangle (1.85,2);
\node[tick, below] at (1.62,0) {$2$};
\path[bar] (2.10,0) rectangle (2.55,0.824);
\path[hl cell] (2.10,0.824) rectangle (2.55,2);
\node[tick, below] at (2.32,0) {$3$};
\path[bar] (2.80,0) rectangle (3.25,0.694);
\path[hl cell] (2.80,0.694) rectangle (3.25,2);
\node[tick, below] at (3.02,0) {$4$};
\path[bar] (3.50,0) rectangle (3.95,0.617);
\path[hl cell] (3.50,0.617) rectangle (3.95,2);
\node[tick, below] at (3.72,0) {$5$};
\path[bar] (4.20,0) rectangle (4.65,0.570);
\path[hl cell] (4.20,0.570) rectangle (4.65,2);
\node[tick, below] at (4.42,0) {$6$};
\path[bar] (4.90,0) rectangle (5.35,0.542);
\path[hl cell] (4.90,0.542) rectangle (5.35,2);
\node[tick, below] at (5.12,0) {$7$};
\path[bar] (5.60,0) rectangle (6.05,0.525);
\path[hl cell] (5.60,0.525) rectangle (6.05,2);
\node[tick, below] at (5.82,0) {$8$};
\draw[faint, dashed] (-0.2,0.5) -- (6.3,0.5) node[tick, right] {$\pi_0=\frac{b}{a+b}$};
\node[lab, below] at (2.9,-0.35) {$n$};
\end{tikzpicture}
\end{center}
```

The distribution $\pi_n=\pi_0P^n$ of the two-state chain with $a=0.3$, $b=0.1$, started in state $0$: the dark part is $\Pr(X_n=0)$ and the light part $\Pr(X_n=1)$. It settles at $b/(a+b)=\tfrac14$

:::

::: {#fig-finite-markov-chains-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (0) at (0,0) {$0$};
\node[vertex] (1) at (3,0) {$1$};
\draw[->] (0) to[bend left=25] node[edge label] {$a$} (1);
\draw[->] (1) to[bend left=25] node[edge label] {$a$} (0);
\draw[->] (0) to[loop left] node[edge label] {$1-a$} (0);
\draw[->] (1) to[loop right] node[edge label] {$1-a$} (1);
\end{tikzpicture}
\end{center}
```

The state transition diagram of the two-state chain.

:::

::: {#prp-two-state-chain .proposition name="The two-state chain"}

On $\{0,1\}$, let $P=\begin{pmatrix}1-a&a\\a&1-a\end{pmatrix}$ with $0\le a\le1$: at each step the chain switches state with probability $a$. Then for $n\ge0$,
$$P^n=\begin{pmatrix}\frac12+\frac12(1-2a)^n&\frac12-\frac12(1-2a)^n\\[2pt]\frac12-\frac12(1-2a)^n&\frac12+\frac12(1-2a)^n\end{pmatrix}.$$
If $0<a<1$, then $|1-2a|<1$, so $P^n\to\begin{pmatrix}\frac12&\frac12\\\frac12&\frac12\end{pmatrix}$ and $\pi_n\to\bigl(\frac12,\frac12\bigr)$ for every $\pi_0$.

:::

::: {.proof}

1. $n=0$: both sides are the identity matrix.

2. Write $\alpha_n=\frac12-\frac12(1-2a)^n$, so the claim is $P^n=\begin{pmatrix}1-\alpha_n&\alpha_n\\\alpha_n&1-\alpha_n\end{pmatrix}$. Suppose this holds for $n$. Multiplying by $P$ gives a matrix of the same symmetric form, with off-diagonal entry
   $$(1-\alpha_n)a+\alpha_n(1-a)=a+(1-2a)\alpha_n=a+\tfrac12(1-2a)-\tfrac12(1-2a)^{n+1}=\alpha_{n+1}.$$

3. By induction the formula holds for all $n$. The limits follow from $(1-2a)^n\to0$ and @thm-markov-distribution-at-time-n.

:::

For $a$ small the chain stays in one state for long stretches; for $a$ close to $1$ it switches almost every step. By symmetry, in the long run it spends half of the time in each state.
