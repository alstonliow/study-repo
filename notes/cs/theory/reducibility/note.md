---
title: "Reducibility"
sources: [mit18404j-9]
requires: [cs/theory/undecidability]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 9, in our own wording; proofs written out in steps. The informal program version is @def-reduction. -->

To show that $B$ is undecidable, show that a decider for $B$ would give a decider for a problem already known to be undecidable, such as $A_{\mathsf{TM}}$.

## Proving undecidability by reduction

::: {#thm-halt-tm-undecidable .theorem name="The halting problem" related="thm-halting-undecidable"}

$HALT_{\mathsf{TM}}=\{\langle M,w\rangle: M \text{ is a TM that halts on input } w\}$ is undecidable.

:::

::: {.proof}

1. Suppose a TM $R$ decides $HALT_{\mathsf{TM}}$. Build a decider $S$ for $A_{\mathsf{TM}}$: on input $\langle M,w\rangle$,
    a. run $R$ on $\langle M,w\rangle$; if it rejects ($M$ loops on $w$), reject;
    b. otherwise simulate $M$ on $w$, which halts, and accept iff $M$ accepts.

2. $S$ always halts and decides $A_{\mathsf{TM}}$, contradicting @thm-atm-undecidable.

:::

::: {#thm-etm-undecidable .theorem name="Emptiness for Turing machines"}

$E_{\mathsf{TM}}=\{\langle M\rangle: M \text{ is a TM and } L(M)=\emptyset\}$ is undecidable.

:::

::: {.proof}

1. Suppose a TM $R$ decides $E_{\mathsf{TM}}$. Build a decider $S$ for $A_{\mathsf{TM}}$: on input $\langle M,w\rangle$, construct the description of the TM

$$
M_w=\text{"on input } x\text{: if } x\ne w \text{, reject; otherwise run } M \text{ on } w \text{ and accept if it accepts."}
$$

2. Then $L(M_w)=\{w\}$ if $M$ accepts $w$, and $L(M_w)=\emptyset$ otherwise.

3. $S$ runs $R$ on $\langle M_w\rangle$ and accepts iff $R$ rejects. $S$ never runs $M_w$; it only writes down its description, which is a finite computation. So $S$ decides $A_{\mathsf{TM}}$, a contradiction.

:::

## Mapping reducibility

::: {#def-mapping-reducibility .definition name="Mapping reducibility"}

A function $f:\Sigma^*\to\Sigma^*$ is *computable* if some TM, on every input $w$, halts with $f(w)$ on its tape. $A$ is *mapping reducible* to $B$, written $A\le_{\mathrm m}B$, if there is a computable $f$ with

$$
w\in A \iff f(w)\in B \qquad\text{for all } w.
$$

:::

::: {#prp-mapping-reduction-properties .proposition name="Mapping reductions transfer (un)decidability"}

Let $A\le_{\mathrm m}B$. If $B$ is decidable, so is $A$; if $B$ is Turing-recognizable, so is $A$. Hence if $A$ is undecidable (unrecognizable), so is $B$. Also $A\le_{\mathrm m}B$ iff $\overline A\le_{\mathrm m}\overline B$.

:::

::: {.proof}

1. Let $f$ be the reduction and $M$ decide (recognize) $B$. On input $w$, compute $f(w)$ and run $M$ on it, giving the same answer.

2. This machine accepts $w$ iff $f(w)\in B$ iff $w\in A$, and it halts whenever $M$ halts on $f(w)$. So it decides (recognizes) $A$.

3. The same $f$ satisfies $w\notin A\iff f(w)\notin B$, which is $\overline A\le_{\mathrm m}\overline B$.

:::

::: {#fig-reducibility-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0) ellipse (1.6 and 2.0);
\draw[regionB] (5,0) ellipse (1.6 and 2.0);
\draw[tintA, draw=none] (0,0.6) ellipse (1.0 and 0.9);
\draw[tintB, draw=none] (5,0.6) ellipse (1.0 and 0.9);
\draw (0,0.6) ellipse (1.0 and 0.9);
\draw (5,0.6) ellipse (1.0 and 0.9);
\node[lab] at (0,1.15) {$A$};
\node[lab] at (5,1.15) {$B$};
\node[lab, note] at (0,-2.3) {$\Sigma^*$};
\node[lab, note] at (5,-2.3) {$\Sigma^*$};
\fill (0.2,0.5) circle (2pt); \fill (5.3,0.4) circle (2pt);
\fill (-0.3,-1.2) circle (2pt); \fill (4.7,-1.1) circle (2pt);
\draw[map] (0.2,0.5) -- node[lab, note, above] {$f$} (5.3,0.4);
\draw[map] (-0.3,-1.2) -- node[lab, note, below] {$f$} (4.7,-1.1);
\end{tikzpicture}
\end{center}
```

A mapping reduction $f$ from $A$ to $B$ (@def-mapping-reducibility) sends members of $A$ into $B$ and non-members outside $B$. It need not be one-to-one or onto.

:::

::: {#exm-reductions .example name="Mapping reductions"}

1. $A_{\mathsf{TM}}\le_{\mathrm m}HALT_{\mathsf{TM}}$: map $\langle M,w\rangle$ to $\langle M',w\rangle$, where $M'$ runs $M$ and enters an infinite loop if $M$ rejects. Then $M'$ halts on $w$ iff $M$ accepts $w$.
2. $A_{\mathsf{TM}}\le_{\mathrm m}\overline{E_{\mathsf{TM}}}$ by $\langle M,w\rangle\mapsto\langle M_w\rangle$ from the proof of @thm-etm-undecidable. No mapping reduction to $E_{\mathsf{TM}}$ itself exists: it would give $\overline{A_{\mathsf{TM}}}\le_{\mathrm m}\overline{E_{\mathsf{TM}}}$, and $\overline{E_{\mathsf{TM}}}$ is recognizable (search for an accepted string by running $M$ on all strings in parallel), which would make $\overline{A_{\mathsf{TM}}}$ recognizable, against @cor-complement-atm-unrecognizable.

:::

::: {#thm-eqtm-neither .theorem name="Equivalence of Turing machines"}

$EQ_{\mathsf{TM}}=\{\langle M_1,M_2\rangle: L(M_1)=L(M_2)\}$ is neither Turing-recognizable nor co-recognizable.

:::

::: {.proof}

1. By @prp-mapping-reduction-properties and @cor-complement-atm-unrecognizable it is enough to show $\overline{A_{\mathsf{TM}}}\le_{\mathrm m}EQ_{\mathsf{TM}}$ (so $EQ_{\mathsf{TM}}$ is not recognizable) and $\overline{A_{\mathsf{TM}}}\le_{\mathrm m}\overline{EQ_{\mathsf{TM}}}$ (so it is not co-recognizable).

2. Let $T_\emptyset$ reject everything and $T_{\mathrm{all}}$ accept everything. Given $\langle M,w\rangle$, let $M_w'$ ignore its input and simulate $M$ on $w$, accepting if $M$ accepts. Then $L(M_w')=\Sigma^*$ if $M$ accepts $w$, and $\emptyset$ otherwise.

3. The map $\langle M,w\rangle\mapsto\langle M_w',T_\emptyset\rangle$ is a computable reduction $\overline{A_{\mathsf{TM}}}\le_{\mathrm m}EQ_{\mathsf{TM}}$: the languages are equal iff $M$ does not accept $w$.

4. The map $\langle M,w\rangle\mapsto\langle M_w',T_{\mathrm{all}}\rangle$ gives $A_{\mathsf{TM}}\le_{\mathrm m}EQ_{\mathsf{TM}}$, that is, $\overline{A_{\mathsf{TM}}}\le_{\mathrm m}\overline{EQ_{\mathsf{TM}}}$.

:::

::: {#fig-reducibility-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-5.0,-1.1) rectangle (1.2,1.1);
\draw[regionB] (-1.2,-1.25) rectangle (5.0,1.25);
\node[lab, note, align=center] at (-3.1,0) {recognizable only\\ $A_{\mathsf{TM}}$, $HALT_{\mathsf{TM}}$, $\overline{E_{\mathsf{TM}}}$};
\node[lab, note, align=center] at (0,0) {decidable\\ $A_{\mathsf{CFG}}$};
\node[lab, note, align=center] at (3.1,0) {co-recognizable only\\ $\overline{A_{\mathsf{TM}}}$, $E_{\mathsf{TM}}$};
\node[lab, note, align=center] at (0,-1.9) {neither: $EQ_{\mathsf{TM}}$};
\end{tikzpicture}
\end{center}
```

Where the languages of this note sit.

:::
