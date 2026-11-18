---
title: "Probabilistic Programs and Rejection Sampling"
sources: [cs221-16]
requires: [ai/bayesian-networks/bayesian-networks, ai/reinforcement-learning/markov-decision-processes]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 16 (probabilistic programs, rejection sampling, hidden Markov model example), in our own wording. -->

Exact inference builds tables whose size is exponential in the number of variables. Sampling methods instead estimate probabilities from random full assignments, which are cheap to draw from a Bayesian network.

::: {#def-probabilistic-program .definition name="Probabilistic program, ancestral sampling"}

A *probabilistic program* is a program that makes random choices and returns an assignment to some random variables; it defines the joint distribution of its output. A Bayesian network is such a program: visit the variables in a topological order and draw each $x_i$ from $p(\cdot\mid x_{\text{Parents}(i)})$, using the values already drawn for its parents (*ancestral sampling*). The output has exactly the joint distribution of @def-bayesian-network.

:::

For the alarm network the program is: $b\gets\text{Bernoulli}(0.05)$, $e\gets\text{Bernoulli}(0.05)$, $a\gets\max(b,e)$, return $(b,e,a)$. A *hidden Markov model* for tracking is another: an object starts at $0$ and moves right with probability $\tfrac12$ each step ($H_t$ is its position) and a noisy sensor reports $E_t$, the position plus noise.

::: {#def-rejection-sampling .definition name="Rejection sampling"}

To estimate $P(Q=q\mid E=e)$, *rejection sampling* draws many samples from the probabilistic program, keeps (*accepts*) those with $E=e$, and returns the fraction of accepted samples with $Q=q$. Evidence and query may be any functions of the sample.

:::

```{=latex}
\begin{algorithm}
\caption{Rejection sampling}
\begin{algorithmic}
\INPUT Probabilistic program, evidence $E=e$, query $Q$, number of samples $m$
\OUTPUT Estimate of $P(Q\mid E=e)$
\STATE $N(q)\gets0$ for all values $q$
\FOR{$j=1$ \TO $m$}
    \STATE $x\gets$ a sample from the program
    \IF{$x$ agrees with $E=e$}
        \STATE $N(x_Q)\gets N(x_Q)+1$
    \ENDIF
\ENDFOR
\RETURN $N/\sum_qN(q)$
\end{algorithmic}
\end{algorithm}
```

The accepted samples are independent draws from $P(\cdot\mid E=e)$, so the estimate converges to the true conditional probability as $m\to\infty$ (@def-monte-carlo-estimate). Its weakness is rare evidence: only a fraction $P(E=e)$ of the samples is accepted. In the alarm network $P(A=1)=0.0975$, so about $90\%$ of the work is thrown away, and with many evidence variables $P(E=e)$ is typically tiny.

::: {#fig-rejection-sampling-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.55cm]
\foreach \i/\b/\e/\a in {0/0/0/0,1/0/0/0,2/0/1/1,3/0/0/0,4/0/0/0,5/1/0/1,6/0/0/0,7/0/0/0,8/0/0/0,9/0/1/1} {
  \node[lab] at (\i,0) {$\b$}; \node[lab] at (\i,-1) {$\e$}; \node[lab] at (\i,-2) {$\a$};
}
\node[lab,anchor=east] at (-0.6,0) {$b$}; \node[lab,anchor=east] at (-0.6,-1) {$e$}; \node[lab,anchor=east] at (-0.6,-2) {$a$};
\begin{scope}[on background layer]\foreach \i in {2,5,9} { \draw[hl box] (\i-0.4,-2.45) rectangle (\i+0.4,0.45); }\end{scope}
\foreach \i in {0,1,3,4,6,7,8} { \draw[faint] (\i-0.35,-2.35) -- (\i+0.35,0.35); }
\end{tikzpicture}
\end{center}
```

Ten possible samples from the alarm network as columns $(b,e,a)$. Rejection sampling for $P(B\mid A=1)$ keeps only the boxed samples with $a=1$ and estimates $P(B=1\mid A=1)\approx\frac13$ from them; most samples are struck out.

:::
