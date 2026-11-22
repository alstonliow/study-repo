---
title: "Logarithmic Space: L and NL"
sources: [mit18404j-19, mit18404j-20]
requires: [cs/theory/savitch-theorem]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lectures 19 and 20, in our own wording; proofs written out in steps. -->

## Sublinear space

To use less space than the input, separate the input from the work space.

::: {#def-l-nl .definition name="L and NL"}

A *log-space* TM has a read-only input tape and a read/write *work tape*; only the cells used on the work tape count as space. Then

$$
\mathrm L=\mathrm{SPACE}(\log n),\qquad \mathrm{NL}=\mathrm{NSPACE}(\log n).
$$

:::

Logarithmic space is enough for a constant number of counters and pointers into the input, since a number up to $n$ has $O(\log n)$ bits.

::: {#exm-l-examples .example name="Languages in L"}

1. $\{0^k1^k: k\ge0\}\in\mathrm L$: check the form, then count the $0$'s and the $1$'s in binary on the work tape and compare.
2. $\mathit{PALINDROMES}\in\mathrm L$: with two pointers $i$ and $n+1-i$ into the input, compare the symbols at those positions for each $i$.

:::

::: {#prp-path-nl .proposition name="Reachability is in NL"}

$\mathit{PATH}\in\mathrm{NL}$ (@prp-path-in-p).

:::

::: {.proof}

1. Starting at $s$, repeatedly guess an edge out of the current node and move along it, keeping only the current node and a step counter on the work tape.

2. Accept if $t$ is reached; reject a branch once the counter exceeds the number $m$ of nodes (a shortest path has fewer than $m$ steps).

3. A node and a counter take $O(\log m)\subseteq O(\log n)$ bits.

:::

Whether $\mathit{PATH}\in\mathrm L$ is open; this is the $\mathrm L$ versus $\mathrm{NL}$ question. By @thm-savitch, $\mathrm{NL}\subseteq\mathrm{SPACE}(\log^2n)$ (Savitch's proof works for $s(n)\ge\log n$).

::: {#def-configuration-graph .definition name="Configuration graph"}

The *configuration graph* $G_{M,w}$ of a log-space TM $M$ on $w$ has a node for each configuration (state, input head position, work tape contents and work head position) and an edge $c_1\to c_2$ when $c_1$ can yield $c_2$. With space $O(\log n)$ there are at most $n\cdot 2^{O(\log n)}=n^{O(1)}$ configurations, and $M$ accepts $w$ iff $G_{M,w}$ has a path from the start configuration to an accepting one.

:::

::: {#thm-nl-in-p .theorem name="$\mathrm{NL}\subseteq\mathrm P$"}

:::

::: {.proof}

1. Let $N$ decide $A$ in log space. On input $w$, build the configuration graph $G_{N,w}$: it has polynomially many nodes, and whether one configuration yields another can be read off from the transition function.

2. Decide whether an accepting configuration is reachable from the start, in polynomial time (@prp-path-in-p).

:::

::: {#fig-logarithmic-space-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, note] at (-0.9,0.2) {$\mathrm L$};
\node[lab, note] at (0.7,0.2) {$\mathrm{NL}$};
\node[lab, note] at (2.3,0.2) {$\mathrm P$};
\node[lab, note] at (3.9,0.2) {$\mathrm{NP}$};
\node[lab, note] at (5.5,0.2) {$\mathrm{PSPACE}$};
\foreach \x in {-0.1,1.5,3.1,4.7} \node[lab] at (\x,0.2) {$\subseteq$};
\draw[decorate, decoration={brace, mirror, amplitude=4pt}] (-1.1,-0.15) -- node[lab, tick, below=4pt] {$\mathrm{NL}\ne\mathrm{PSPACE}$ by the space hierarchy} (5.9,-0.15);
\node[lab, tick] at (0.7,0.65) {$\mathit{PATH}$};
\node[lab, tick] at (3.9,0.65) {$\mathit{SAT}$};
\node[lab, tick] at (5.5,0.65) {$\mathit{TQBF}$};
\end{tikzpicture}
\end{center}
```

The chain $\mathrm L\subseteq\mathrm{NL}\subseteq\mathrm P\subseteq\mathrm{NP}\subseteq\mathrm{PSPACE}$, with a complete problem above each class. Only $\mathrm{NL}\ne\mathrm{PSPACE}$ is known (@thm-space-hierarchy), so some inclusion is strict.

:::

## NL-completeness

Polynomial-time reductions are too strong inside $\mathrm P$, so we use log-space ones.

::: {#def-log-space-reduction .definition name="Log-space reducibility, NL-completeness"}

A *log-space transducer* is a TM with a read-only input tape, a write-only output tape whose head only moves right, and a work tape of size $O(\log n)$. It computes $f$ if it halts with $f(w)$ on the output tape. $A\le_{\mathrm L}B$ if $A\le_{\mathrm m}B$ by such an $f$. $B$ is *NL-complete* if $B\in\mathrm{NL}$ and $A\le_{\mathrm L}B$ for every $A\in\mathrm{NL}$.

:::

::: {#prp-log-space-reduction-properties .proposition name="Log-space reductions compose"}

If $A\le_{\mathrm L}B$ and $B\in\mathrm L$, then $A\in\mathrm L$.

:::

::: {.proof}

1. Let $f$ be the reduction and $M_B$ decide $B$ in log space. The output $f(w)$ may be polynomially long, so it cannot be stored.

2. Instead run $M_B$ and, whenever it needs the $i$-th symbol of $f(w)$, recompute $f(w)$ from the start, discarding all output except the $i$-th symbol. This needs a counter for $i$ and the work tapes of both machines: $O(\log n)$ space.

:::

::: {#thm-path-nl-complete .theorem name="PATH is NL-complete"}

:::

::: {.proof}

1. $\mathit{PATH}\in\mathrm{NL}$ by @prp-path-nl.

2. Let $N$ decide $A\in\mathrm{NL}$ in space $c\log n$, with a single accepting configuration. The reduction maps $w$ to $\langle G_{N,w},c_{\text{start}},c_{\text{acc}}\rangle$ (@def-configuration-graph); $w\in A$ iff the output is in $\mathit{PATH}$.

3. A log-space transducer can write this graph: it cycles through all strings of length $c\log n$ (on its work tape) and outputs those that are configurations, then cycles through all pairs and outputs the pairs where the first yields the second, checking that by looking at the input symbol under the input head.

:::

::: {#fig-logarithmic-space-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,1.4) rectangle (5,1.9); \node[lab, note] at (2.5,1.65) {input $w$ (read only)};
\draw[hl cell] (0,0.5) rectangle (1.6,1.0); \node[lab, note] at (0.8,0.75) {work};
\node[lab, tick] at (2.6,0.75) {$O(\log n)$ cells};
\draw[cell frame] (0,-0.4) rectangle (6.5,0.1); \node[lab, note] at (3.25,-0.15) {output $f(w)$ (write only, left to right)};
\node[box] (q) at (-1.8,0.75) {control};
\draw[map] (q) -- (0,1.65); \draw[map] (q) -- (0,0.75); \draw[map] (q) -- (0,-0.15);
\end{tikzpicture}
\end{center}
```

A log-space transducer (@def-log-space-reduction): only the work tape counts against the space bound.

:::
