---
title: "Interactive Proof Systems"
sources: [mit18404j-25]
requires: [cs/theory/probabilistic-computation, math/discrete/graph/isomorphism]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 25, in our own wording; proofs written out in steps. -->

$\mathrm{NP}$ is the class of languages with short certificates that a deterministic verifier checks. Letting the verifier flip coins and talk with the prover gives a much larger class.

::: {#def-ip .definition name="Interactive proof system, IP"}

An *interactive proof system* for $A$ consists of a *verifier* $V$, a probabilistic polynomial-time machine, and a *prover* $P$ of unlimited power, which exchange polynomially many messages, each of polynomial length, about a common input $w$; at the end $V$ accepts or rejects. Write $\Pr[(V\leftrightarrow P)\text{ accepts } w]$ for the probability over $V$'s coins. $A\in\mathrm{IP}$ if some $V$ satisfies

1. *completeness:* if $w\in A$, some prover $P$ makes $V$ accept with probability at least $\tfrac23$;
2. *soundness:* if $w\notin A$, every prover $\tilde P$ makes $V$ accept with probability at most $\tfrac13$.

:::

The prover is trying to convince the verifier that $w\in A$; the verifier must not be fooled by a dishonest prover. As for $\mathrm{BPP}$, repetition reduces the error (@lem-amplification).

::: {#prp-np-in-ip .proposition name="$\mathrm{NP}\subseteq\mathrm{IP}$ and $\mathrm{BPP}\subseteq\mathrm{IP}$"}

:::

::: {.proof}

1. For $A\in\mathrm{NP}$, the prover sends a certificate and the verifier checks it deterministically (@thm-np-verifier); no false certificate is accepted.

2. For $A\in\mathrm{BPP}$, the verifier ignores the prover and decides $A$ by itself.

:::

## Graph non-isomorphism

$\mathit{ISO}=\{\langle G,H\rangle: G\cong H\}$ (@def-graph-isomorphism) is in $\mathrm{NP}$: the certificate is the isomorphism. Its complement $\mathit{NONISO}$ is not known to be in $\mathrm{NP}$: how would one certify briefly that *no* bijection works?

::: {#thm-noniso-in-ip .theorem name="$\mathit{NONISO}\in\mathrm{IP}$"}

:::

::: {.proof}

1. *Protocol.* On input $\langle G_1,G_2\rangle$ with $n$ nodes each, repeat twice:
    a. $V$ picks $i\in\{1,2\}$ at random and a random permutation $\pi$ of the nodes, and sends $H=\pi(G_i)$, a randomly relabelled copy of $G_i$;
    b. $P$ replies with some $j\in\{1,2\}$.

   $V$ accepts iff $j=i$ in both rounds.

2. *Completeness.* If $G_1\not\cong G_2$, then $H$ is isomorphic to exactly one of them; the unlimited prover finds which one and always answers $j=i$, so $V$ accepts with probability $1$.

3. *Soundness.* If $G_1\cong G_2$, then a random relabelling of $G_1$ and a random relabelling of $G_2$ have the same distribution. So $H$ carries no information about $i$, and any prover answers correctly with probability exactly $\tfrac12$ in each round. $V$ accepts with probability $\tfrac14\le\tfrac13$.

:::

::: {#fig-interactive-proofs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (v) at (0,0) {verifier $V$\\ (coins, poly time)};
\node[hl box] (p) at (7,0) {prover $P$\\ (unlimited)};
\draw[map] (1.4,0.35) -- node[lab, note, above] {$H=\pi(G_i)$, $i$ and $\pi$ secret} (5.7,0.35);
\draw[map] (5.7,-0.35) -- node[lab, note, below] {$j$: "$H$ came from $G_j$"} (1.4,-0.35);
\node[lab, note] at (0,-1.1) {accept iff $j=i$};
\end{tikzpicture}
\end{center}
```

One round of the protocol of @thm-noniso-in-ip. Only a prover facing non-isomorphic graphs can tell where $H$ came from.

:::

::: {#fig-interactive-proofs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
\begin{scope}
\node[small vertex] (a) at (0,1) {}; \node[small vertex] (b) at (1,1) {};
\node[small vertex] (c) at (1,0) {}; \node[small vertex] (d) at (0,0) {};
\draw (a)--(b)--(c)--(d)--(a);
\node[lab, note] at (0.5,-0.6) {$G_1$: 4-cycle};
\end{scope}
\begin{scope}[xshift=3cm]
\node[small vertex] (a) at (0,1) {}; \node[small vertex] (b) at (1,1) {};
\node[small vertex] (c) at (1,0) {}; \node[small vertex] (d) at (0,0) {};
\draw (a)--(b)--(c)--(a); \draw (c)--(d);
\node[lab, note] at (0.5,-0.6) {$G_2$: triangle and tail};
\end{scope}
\begin{scope}[xshift=7cm]
\draw[regionB] (-0.45,-0.35) rectangle (1.45,1.35);
\node[small vertex] (a) at (0,1) {}; \node[small vertex] (b) at (1,1) {};
\node[small vertex] (c) at (1,0) {}; \node[small vertex] (d) at (0,0) {};
\draw (a)--(c)--(b)--(d)--(a);
\node[lab, note] at (0.5,-0.75) {$H$ from $V$};
\end{scope}
\end{tikzpicture}
\end{center}
```

$G_1\not\cong G_2$ (one has a triangle), so the prover can answer: the challenge $H$ has degrees $2,2,2,2$ and no triangle, hence $H\cong G_1$ and $j=1$.

:::

::: {#rmk-interactive-proofs-1}

$\mathrm{IP}\subseteq\mathrm{PSPACE}$: a polynomial-space machine can compute the best possible acceptance probability by exploring all message sequences and coin flips. Shamir's theorem gives equality, $\mathrm{IP}=\mathrm{PSPACE}$; the next note proves the first step, $\mathrm{coNP}\subseteq\mathrm{IP}$ (@cor-conp-in-ip), whose method extends to $\mathit{TQBF}$.

:::
