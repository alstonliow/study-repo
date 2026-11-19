---
title: "The Viterbi Algorithm"
sources: [eecs126-12]
requires: [ai/temporal-models/hidden-markov-models]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Hidden Markov Models", in our own wording; proofs written out in steps. -->

Filtering (@thm-forward-algorithm) gives the distribution of the current state. Often we want instead the single most likely *sequence* of hidden states given all the evidence, for example the transmitted bits behind a noisy signal or the words behind an audio recording.

::: {#def-most-likely-sequence .definition name="Most likely explanation"}

In a hidden Markov model (@def-hmm) with evidence $e_{1:T}$, the *most likely explanation* is
$$\hat x_{1:T}=\arg\max_{x_{1:T}}P(x_{1:T},e_{1:T})=\arg\max_{x_{1:T}}P(x_1)P(e_1\mid x_1)\prod_{t=2}^{T}P(x_t\mid x_{t-1})P(e_t\mid x_t).$$

:::

Trying all $|X|^T$ sequences is hopeless. The product has the structure of a path weight in a layered graph (one layer of $|X|$ nodes per time step), so dynamic programming finds the best path.

::: {#thm-viterbi .theorem name="The Viterbi recursion"}

Let $m_t(x)=\max_{x_{1:t-1}}P(x_{1:t-1},X_t=x,e_{1:t})$, the probability of the best path ending in state $x$ at time $t$. Then
$$m_1(x)=P(x)P(e_1\mid x),\qquad m_{t}(x)=P(e_t\mid x)\max_{x'}P(x\mid x')\,m_{t-1}(x').$$
The most likely explanation ends in $\hat x_T=\arg\max_xm_T(x)$, and for $t<T$, $\hat x_t$ is the maximising $x'$ in the recursion for $m_{t+1}(\hat x_{t+1})$.

:::

::: {.proof}

1. By the factorisation in @def-most-likely-sequence, $P(x_{1:t},e_{1:t})=P(x_{1:t-1},e_{1:t-1})\,P(x_t\mid x_{t-1})\,P(e_t\mid x_t)$.

2. Fix $x_t=x$ and $x_{t-1}=x'$. Only the first factor depends on $x_{1:t-2}$, and its maximum over $x_{1:t-2}$ is $m_{t-1}(x')$. Maximising over $x'$ gives the recursion.

3. The best full path ends in the state maximising $m_T$. Its prefix ending at $x_{t}$ must itself be a best path ending at $x_t$ (otherwise replacing it would increase the product), so backtracking through the recorded maximisers recovers it.

:::

```{=latex}
\begin{algorithm}
\caption{Viterbi algorithm}
\begin{algorithmic}
\INPUT HMM, evidence $e_1,\dots,e_T$
\OUTPUT A most likely state sequence $\hat x_1,\dots,\hat x_T$
\STATE $m_1(x)\gets P(x)P(e_1\mid x)$ for all $x$
\FOR{$t=2$ \textbf{to} $T$}
    \FORALL{states $x$}
        \STATE $b_t(x)\gets\arg\max_{x'}P(x\mid x')m_{t-1}(x')$ \COMMENT{best predecessor}
        \STATE $m_t(x)\gets P(e_t\mid x)\,P(x\mid b_t(x))\,m_{t-1}(b_t(x))$
    \ENDFOR
\ENDFOR
\STATE $\hat x_T\gets\arg\max_xm_T(x)$
\FOR{$t=T-1$ \textbf{down to} $1$}
    \STATE $\hat x_t\gets b_{t+1}(\hat x_{t+1})$
\ENDFOR
\end{algorithmic}
\end{algorithm}
```

The cost is $O(T|X|^2)$ time and $O(T|X|)$ memory for the back pointers. It is the forward algorithm with the sum replaced by a maximum; in practice one works with logarithms, which turns products into sums and the problem into a shortest-path computation.

::: {#exm-viterbi-weather .example name="Rain from umbrellas, again"}

In the model of @exm-forward-weather with evidence umbrella, umbrella, no umbrella:

| $t$ | $m_t(\text{rain})$ | $m_t(\text{sun})$ | best predecessor of rain / sun |
|---|---|---|---|
| 1 | $0.5\cdot0.8=0.4$ | $0.5\cdot0.3=0.15$ | — |
| 2 | $0.8\cdot0.7\cdot0.4=0.224$ | $0.3\cdot\max(0.3\cdot0.4,\,0.7\cdot0.15)=0.036$ | rain / rain |
| 3 | $0.2\cdot0.7\cdot0.224\approx0.0314$ | $0.7\cdot0.3\cdot0.224\approx0.0470$ | rain / rain |

The best final state is sun, and backtracking gives rain, rain, sun.

:::

::: {#fig-viterbi-algorithm-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (v0r) at (0.00,0.00) {$0.4$};
\node[small vertex] (v0s) at (0.00,-1.30) {$0.15$};
\node[lab,tick] at (0.00,0.95) {$t=1$: umbrella};
\node[small vertex, fill=accentLight, draw=accent] (v1r) at (2.40,0.00) {$0.224$};
\node[small vertex] (v1s) at (2.40,-1.30) {$0.036$};
\node[lab,tick] at (2.40,0.95) {$t=2$: umbrella};
\node[small vertex] (v2r) at (4.80,0.00) {$0.03136$};
\node[small vertex, fill=accentLight, draw=accent] (v2s) at (4.80,-1.30) {$0.04704$};
\node[lab,tick] at (4.80,0.95) {$t=3$: no umbrella};
\node[lab, anchor=east] at (-0.8,0.00) {rain};
\node[lab, anchor=east] at (-0.8,-1.30) {sun};
\draw[->,hl] (v0r)--(v1r);
\draw[->,faint] (v0s)--(v1r);
\draw[->] (v0r)--(v1s);
\draw[->,faint] (v0s)--(v1s);
\draw[->] (v1r)--(v2r);
\draw[->,faint] (v1s)--(v2r);
\draw[->,hl] (v1r)--(v2s);
\draw[->,faint] (v1s)--(v2s);
\end{tikzpicture}
\end{center}
```

The Viterbi trellis for the umbrella example: each node holds $m_t(x)$. Solid arrows mark the best predecessor of each node, faint arrows the others; the highlighted path rain, rain, sun is the most likely explanation.

:::
