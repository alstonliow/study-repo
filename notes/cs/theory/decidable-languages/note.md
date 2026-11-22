---
title: "Decidable Problems about Automata and Grammars"
sources: [mit18404j-7]
requires: [cs/theory/turing-machine-variants]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 7, in our own wording; proofs written out in steps. -->

Questions about automata and grammars become languages of encodings, and a decision procedure is a decider for that language. All machines below are deciders: each step is finite.

## Finite automata

::: {#thm-adfa-decidable .theorem name="Acceptance for finite automata"}

The languages

$$
A_{\mathsf{DFA}}=\{\langle B,w\rangle: B \text{ is a DFA that accepts } w\},\quad A_{\mathsf{NFA}}=\{\langle B,w\rangle: B \text{ is an NFA that accepts } w\},\quad A_{\mathsf{REX}}=\{\langle R,w\rangle: w\in L(R)\}
$$

are decidable.

:::

::: {.proof}

1. For $A_{\mathsf{DFA}}$: simulate $B$ on $w$, keeping the current state on the tape, for $|w|$ steps; accept iff the final state is an accept state.

2. For $A_{\mathsf{NFA}}$: convert $B$ into an equivalent DFA by the subset construction (@thm-nfa-dfa-equivalence) and run the decider for $A_{\mathsf{DFA}}$.

3. For $A_{\mathsf{REX}}$: convert $R$ into an NFA (@thm-regex-to-nfa) and use step 2.

:::

::: {#thm-edfa-decidable .theorem name="Emptiness and equivalence for finite automata"}

$E_{\mathsf{DFA}}=\{\langle B\rangle: L(B)=\emptyset\}$ and $EQ_{\mathsf{DFA}}=\{\langle A,B\rangle: L(A)=L(B)\}$ are decidable.

:::

::: {.proof}

1. For $E_{\mathsf{DFA}}$: mark the start state; repeatedly mark every state that has a transition from a marked state, until no new state is marked. Accept iff no accept state is marked. The marked states are exactly those reachable from the start, and $L(B)\ne\emptyset$ iff an accept state is reachable.

2. For $EQ_{\mathsf{DFA}}$: build a DFA $C$ for the symmetric difference

$$
L(C)=\big(L(A)\cap\overline{L(B)}\big)\cup\big(\overline{L(A)}\cap L(B)\big)
$$

by the closure constructions (@thm-regular-closed-union, @prp-regular-complement-intersection). Then $L(A)=L(B)$ iff $L(C)=\emptyset$; run the decider for $E_{\mathsf{DFA}}$ on $\langle C\rangle$.

:::

::: {#fig-decidable-languages-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hl state] (1) at (0,0) {};
\node[hl state] (2) at (1.8,0.8) {};
\node[hl state] (3) at (1.8,-0.8) {};
\node[hl state] (4) at (3.6,0) {};
\node[accept state] (5) at (5.6,0.8) {};
\node[state] (6) at (5.6,-0.8) {};
\draw[start] (1.west) -- ++(-0.6,0);
\draw[trans] (1) -- (2); \draw[trans] (1) -- (3); \draw[trans] (2) -- (4); \draw[trans] (3) -- (4);
\draw (4) edge[trans, loop above] (4);
\draw (6) edge[trans, bend left=25] (5); \draw (5) edge[trans, bend left=25] (6); \draw[trans] (6) -- (4);
\node[lab, note] at (2.6,-1.7) {marked: reachable from the start};
\end{tikzpicture}
\end{center}
```

The marking algorithm for $E_{\mathsf{DFA}}$ (@thm-edfa-decidable): no marked (shaded) state accepts, so $L(B)=\emptyset$, although the DFA has an accept state.

:::

## Context-free grammars

::: {#thm-acfg-decidable .theorem name="Acceptance and emptiness for grammars"}

$A_{\mathsf{CFG}}=\{\langle G,w\rangle: G \text{ is a CFG that generates } w\}$ and $E_{\mathsf{CFG}}=\{\langle G\rangle: L(G)=\emptyset\}$ are decidable.

:::

::: {.proof}

1. For $A_{\mathsf{CFG}}$: convert $G$ to Chomsky normal form (@thm-chomsky-normal-form). If $w=\varepsilon$, accept iff there is a rule $S\to\varepsilon$. Otherwise, every derivation of $w$ has exactly $2|w|-1$ steps; list all derivations of that many steps (finitely many) and accept iff one of them yields $w$.

2. Trying all derivations of $G$ itself would not do: without a bound on their length the search might never end.

3. For $E_{\mathsf{CFG}}$: mark every terminal; repeatedly mark each variable $A$ that has a rule $A\to u$ whose symbols are all marked. When nothing changes, accept iff the start variable is unmarked. A variable gets marked exactly when it derives some string of terminals.

:::

::: {#thm-cfl-decidable .theorem name="Every context-free language is decidable"}

:::

::: {.proof}

1. Let $A=L(G)$ for a CFG $G$. Build $G$ into a TM $M_G$ that, on input $w$, runs the decider for $A_{\mathsf{CFG}}$ on $\langle G,w\rangle$ and gives the same answer.

2. $M_G$ halts on every input and accepts exactly the strings of $A$.

3. (Simulating a PDA directly would not work: some branches of a PDA may run forever, pushing without reading input.)

:::

::: {#rmk-decidable-languages-1}

Not everything about grammars is decidable: $EQ_{\mathsf{CFG}}$ (equal languages) and $ALL_{\mathsf{CFG}}$ (generates every string) are undecidable (@thm-allcfg-undecidable). The symmetric-difference trick fails because CFLs are not closed under complement or intersection (@prp-cfl-closure).

:::

::: {#fig-decidable-languages-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionC] (0,0) ellipse (4.6 and 2.1);
\draw[regionB] (-0.6,-0.1) ellipse (3.6 and 1.65);
\draw[regionA] (-1.2,-0.2) ellipse (2.5 and 1.2);
\draw[regionA] (-1.9,-0.3) ellipse (1.3 and 0.75);
\node[lab] at (-1.9,-0.3) {regular};
\node[lab] at (0.15,0.5) {context-free};
\node[lab] at (1.75,0.95) {decidable};
\node[lab] at (3.55,0.6) {recognizable};
\node[lab, note] at (1.9,-0.2) {$a^kb^kc^k$};
\node[lab, note] at (0.3,-0.55) {$0^k1^k$};
\node[lab, note] at (3.5,-0.3) {$A_{\mathsf{TM}}$};
\end{tikzpicture}
\end{center}
```

The four classes of languages met so far, each strictly inside the next, with a language that separates each class from the one inside it.

:::
