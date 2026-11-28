---
title: "Prior Sampling and Likelihood Weighting"
sources: [cs188-16]
requires: [ai/bayesian-networks/rejection-sampling, ai/bayesian-networks/variable-elimination]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 16 (prior sampling, rejection sampling, likelihood weighting and its consistency, comparison with Gibbs sampling), in our own wording; the consistency proof is written out in steps; the numbers continue our traffic example. -->

Exact inference is NP-hard (@thm-bn-inference-np-hard), so we often estimate probabilities from samples instead. *Prior sampling* is ancestral sampling of the network (@def-probabilistic-program): visiting the variables in topological order, draw each from its table given its parents' sampled values. The fraction of $N$ prior samples with a property converges to its probability as $N\to\infty$ (the law of large numbers, @sec-math-probability-limit-theorems-concentration-inequalities); an estimator with this property is *consistent*. Rejection sampling (@def-rejection-sampling) conditions on evidence by throwing away the samples that contradict it, which wastes almost all of them when the evidence is unlikely.

::: {#def-likelihood-weighting .definition name="Likelihood weighting"}

To estimate $P(Q=q\mid E=e)$, *likelihood weighting* generates each sample in topological order, *fixing* each evidence variable $E_j$ to its observed value $e_j$ instead of sampling it and drawing every other variable from its table given its parents. The sample gets the *weight*
$$
w=\prod_{j}p\bigl(e_j\mid \text{parents of }E_j\text{ in the sample}\bigr).
$$
The estimate is the total weight of the samples with $Q=q$ divided by the total weight of all samples.

:::

```{=latex}
\begin{algorithm}
\caption{Likelihood weighting}
\begin{algorithmic}
\INPUT Bayesian network, evidence $E=e$, query value $Q=q$, number of samples $N$
\OUTPUT Estimate of $P(Q=q\mid E=e)$
\STATE $W_q\gets0$; $W\gets0$
\FOR{$k=1$ \textbf{to} $N$}
    \STATE $w\gets1$
    \FOR{each variable $X_i$ in topological order}
        \IF{$X_i$ is an evidence variable with value $e_i$}
            \STATE $x_i\gets e_i$; $w\gets w\cdot p(e_i\mid x_{\text{Parents}(i)})$
        \ELSE
            \STATE draw $x_i$ from $p(\cdot\mid x_{\text{Parents}(i)})$
        \ENDIF
    \ENDFOR
    \STATE $W\gets W+w$; \textbf{if} the sample has $Q=q$ \textbf{then} $W_q\gets W_q+w$
\ENDFOR
\RETURN $W_q/W$
\end{algorithmic}
\end{algorithm}
```

::: {#thm-likelihood-weighting .theorem name="Likelihood weighting is consistent"}

If $P(E=e)>0$, the likelihood weighting estimate converges to $P(Q=q\mid E=e)$ with probability $1$ as the number of samples grows.

:::

::: {.proof}

1. Let $Z$ be the non-evidence variables. A sample with values $z$ is generated with probability $S(z)=\prod_{i:X_i\in Z}p(z_i\mid \text{parents})$, the parents' values taken from $z$ and $e$.
2. Its weight is $w(z)=\prod_jp(e_j\mid\text{parents})$, so by the definition of the network $S(z)\,w(z)=\prod_ip(x_i\mid x_{\text{Parents}(i)})=P(z,e)$, every factor of the joint appearing exactly once.
3. Hence the expected weight is $\mathbb E[w]=\sum_zS(z)w(z)=\sum_zP(z,e)=P(e)$, and likewise $\mathbb E[w\cdot\mathbf 1\{Q=q\}]=\sum_{z:\,q}P(z,e)=P(q,e)$.
4. The samples are independent, so by the strong law of large numbers $W_q/N\to P(q,e)$ and $W/N\to P(e)>0$ with probability $1$, and their ratio $W_q/W\to P(q,e)/P(e)=P(q\mid e)$.

:::

::: {#exm-likelihood-weighting-traffic .example name="Weighting by the evidence"}

In the chain $R\to T\to L$ of @exm-variable-elimination-traffic with evidence $L=+l$, each sample draws $R$ and $T$ from their tables and gets weight $P(+l\mid t)$: $0.4$ if $T=+t$ and $0.1$ if $T=-t$. From the four samples $(+r,+t)$, $(-r,-t)$, $(-r,+t)$, $(-r,-t)$, with weights $0.4,0.1,0.4,0.1$, the estimate of $P(+r\mid+l)$ is $0.4/1.0=0.4$, against the exact $31/95\approx0.33$; with more samples it converges by @thm-likelihood-weighting, since $\mathbb E[w\,\mathbf 1\{+r\}]=0.2\,(0.7\cdot0.4+0.3\cdot0.1)=0.062=P(+r,+l)$ and $\mathbb E[w]=0.19=P(+l)$. Rejection sampling would keep only about $19\%$ of its samples.

:::

::: {#fig-likelihood-weighting-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[lab] at (0.27,0.85) {$R$};
\node[lab] at (0.82,0.85) {$T$};
\node[lab] at (1.37,0.85) {$L$};
\node[lab] at (2.1,0.85) {$w$};
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$+r$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$+t$};
\draw[hl cell] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$+l$};
\node[lab, anchor=east] at (-0.100,0.275) {\#1};
\node[lab] at (2.1,0.27) {$0.4$};
\draw[cell frame] (0.000,-0.600) rectangle (0.550,-0.050);
\node[lab] at (0.275,-0.325) {$-r$};
\draw[cell frame] (0.550,-0.600) rectangle (1.100,-0.050);
\node[lab] at (0.825,-0.325) {$-t$};
\draw[hl cell] (1.100,-0.600) rectangle (1.650,-0.050);
\node[lab] at (1.375,-0.325) {$+l$};
\node[lab, anchor=east] at (-0.100,-0.325) {\#2};
\node[lab] at (2.1,-0.33) {$0.1$};
\draw[cell frame] (0.000,-1.200) rectangle (0.550,-0.650);
\node[lab] at (0.275,-0.925) {$-r$};
\draw[cell frame] (0.550,-1.200) rectangle (1.100,-0.650);
\node[lab] at (0.825,-0.925) {$+t$};
\draw[hl cell] (1.100,-1.200) rectangle (1.650,-0.650);
\node[lab] at (1.375,-0.925) {$+l$};
\node[lab, anchor=east] at (-0.100,-0.925) {\#3};
\node[lab] at (2.1,-0.93) {$0.4$};
\draw[cell frame] (0.000,-1.800) rectangle (0.550,-1.250);
\node[lab] at (0.275,-1.525) {$-r$};
\draw[cell frame] (0.550,-1.800) rectangle (1.100,-1.250);
\node[lab] at (0.825,-1.525) {$-t$};
\draw[hl cell] (1.100,-1.800) rectangle (1.650,-1.250);
\node[lab] at (1.375,-1.525) {$+l$};
\node[lab, anchor=east] at (-0.100,-1.525) {\#4};
\node[lab] at (2.1,-1.53) {$0.1$};
\end{tikzpicture}
\end{center}
```

The four weighted samples of @exm-likelihood-weighting-traffic. The evidence $L=+l$ (highlighted) is fixed, not sampled; each sample is weighted by $P(+l\mid t)$. The weighted fraction with $+r$ is $0.4/1.0$.

:::

Likelihood weighting uses every sample, but evidence influences only the variables *below* it: the upstream variables are still drawn from their priors and are merely reweighted afterwards. If the evidence lies at the leaves and is unlikely, most samples get tiny weights and a few dominate, so the effective number of samples is small. Gibbs sampling (@def-gibbs-sampling) lets evidence influence every variable, at the price of correlated samples.
