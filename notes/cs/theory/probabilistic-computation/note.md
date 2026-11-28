---
title: "Probabilistic Computation and BPP"
sources: [mit18404j-23, mit18404j-24]
requires: [cs/theory/nondeterministic-time, math/probability/limit-theorems/chernoff-bounds]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lectures 23 and 24, in our own wording; proofs written out in steps. -->

::: {#def-ptm .definition name="Probabilistic Turing machine"}

A *probabilistic Turing machine* (PTM) is a nondeterministic TM in which every nondeterministic step has exactly two choices, each taken with probability $\tfrac12$ (a *coin flip*), independently. A branch with $k$ coin flips has probability $2^{-k}$, and

$$
\Pr[M \text{ accepts } w]=\sum_{\text{accepting branches } b}\Pr[b].
$$

:::

::: {#def-bpp .definition name="Error probability, BPP"}

A PTM $M$ *decides $A$ with error probability $\varepsilon$* if $\Pr[M\text{ accepts }w]\ge1-\varepsilon$ for $w\in A$ and $\Pr[M\text{ rejects }w]\ge1-\varepsilon$ for $w\notin A$. $\mathrm{BPP}$ is the class of languages decided by polynomial-time PTMs with error probability $\tfrac13$.

:::

The constant $\tfrac13$ is arbitrary: any constant below $\tfrac12$ gives the same class, by repetition.

::: {#lem-amplification .lemma name="Amplification"}

Let $0\le\varepsilon<\tfrac12$ and let $M_1$ decide $A$ in polynomial time with error $\varepsilon$. For every polynomial $r(n)$ there is a polynomial-time PTM $M_2$ that decides $A$ with error $2^{-r(n)}$.

:::

::: {.proof}

1. $M_2$ runs $M_1$ independently $k$ times on $w$ and outputs the majority answer.

2. Each run is wrong with probability at most $\varepsilon$. The majority is wrong only if at least $k/2$ runs are wrong, while the expected number of wrong runs is at most $\varepsilon k$, a constant fraction below $k/2$.

3. By the Chernoff bound (@thm-chernoff-bound) this probability is at most $e^{-ck}$ for a constant $c>0$ depending on $\varepsilon$. Taking $k=\lceil r(n)/(c\log_2 e)\rceil$, a polynomial number of runs, makes it at most $2^{-r(n)}$.

:::

::: {#fig-probabilistic-computation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=8cm]
\draw[->] (0,0) -- (13.5,0) node[lab, note, right] {runs $k$};
\draw[->] (0,0) -- (0,0.42) node[lab, note, above] {error};
\foreach \i/\k/\e in {1/1/0.3333,2/3/0.2593,3/5/0.2099,4/11/0.1221,5/21/0.0557,6/41/0.0135} {
  \draw[bar] (2*\i-1.4,0) rectangle (2*\i-0.2,\e);
  \node[lab, tick] at (2*\i-0.8,-0.035) {\k};
}
\draw[gridline] (0,0.3333) -- (13,0.3333); \node[lab, tick, anchor=east] at (0,0.3333) {$\tfrac13$};
\end{tikzpicture}
\end{center}
```

@lem-amplification for $\varepsilon=\tfrac13$: the probability that a majority of $k$ independent runs is wrong, for $k=1,3,5,11,21,41$. It decays exponentially in $k$.

:::

::: {#rmk-probabilistic-computation-1}

$\mathrm P\subseteq\mathrm{BPP}$, and $\mathrm{BPP}\subseteq\mathrm{PSPACE}$ (compute the acceptance probability by trying all coin sequences, reusing space). Many believe $\mathrm{BPP}=\mathrm P$; it is not known whether $\mathrm{BPP}\subseteq\mathrm{NP}$. With *one-sided* error ($w\notin A$ always rejected, $w\in A$ accepted with probability at least $\tfrac12$) one gets the class $\mathrm{RP}\subseteq\mathrm{NP}$.

:::

::: {#exm-polynomial-identity .example name="Testing a product"}

Given $n\times n$ matrices $A,B,C$ over $\mathbb Z_p$, is $AB=C$? Computing $AB$ costs about $n^3$ operations. Instead pick a random vector $r\in\{0,1\}^n$ and check $A(Br)=Cr$ with $O(n^2)$ operations. If $AB\ne C$, then $D=AB-C$ has a nonzero row $d$ with some $d_j\ne0$; for each choice of the other entries of $r$, at most one of the two values of $r_j$ makes $d\cdot r=0$. So a wrong $C$ passes with probability at most $\tfrac12$, and $k$ repetitions push this below $2^{-k}$. This one-sided test is a first instance of the polynomial-identity idea developed in @sec-cs-theory-branching-programs.

:::

::: {#fig-probabilistic-computation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=0.95cm, every node/.style={small vertex}, level 1/.style={sibling distance=3.2cm}, level 2/.style={sibling distance=1.6cm}]
\node {}
  child {node {} child {node[hl state] {a}} child {node[hl state] {a}}}
  child {node {} child {node[hl state] {a}} child {node {r}}};
\node[lab, note, anchor=west] at (3.4,-1.9) {each leaf: probability $\tfrac14$};
\node[lab, note, anchor=west] at (3.4,-2.35) {$\Pr[\text{accept}]=\tfrac34$};
\end{tikzpicture}
\end{center}
```

A PTM's computation tree (@def-ptm): every step is a fair coin flip, and the acceptance probability is the total probability of accepting leaves (shaded).

:::
