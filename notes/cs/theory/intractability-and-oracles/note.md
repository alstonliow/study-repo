---
title: "Provable Intractability and Oracles"
sources: [mit18404j-22]
requires: [cs/theory/hierarchy-theorems]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 22, in our own wording; proofs written out in steps. -->

## A natural intractable problem

The hierarchy theorems give languages outside $\mathrm P$, but artificial ones. Completeness for a large class transfers the separation to natural problems.

::: {#def-exp-complete .definition name="EXPTIME- and EXPSPACE-complete"}

$B$ is *EXPTIME-complete* (*EXPSPACE-complete*) if $B$ is in $\mathrm{EXPTIME}$ ($\mathrm{EXPSPACE}$) and $A\le_{\mathrm p}B$ for every $A$ in that class.

:::

::: {#prp-complete-intractable .proposition name="Complete problems are intractable"}

An EXPTIME-complete language is not in $\mathrm P$. An EXPSPACE-complete language is not in $\mathrm{PSPACE}$, and hence not in $\mathrm P$.

:::

::: {.proof}

1. If an EXPTIME-complete $B$ were in $\mathrm P$, every language in $\mathrm{EXPTIME}$ would reduce to it and be in $\mathrm P$ (@prp-poly-reduction-properties), contradicting @cor-p-ne-exptime.

2. Likewise for $\mathrm{EXPSPACE}$, using @cor-space-separations; polynomial-time reductions keep $\mathrm{PSPACE}$ closed.

:::

::: {#def-eq-rex .definition name="Equivalence of regular expressions"}

$EQ_{\mathsf{REX}}=\{\langle R_1,R_2\rangle: R_1,R_2 \text{ are equivalent regular expressions}\}$. Allowing the *exponentiation* operator $R^{k}=R\,R\cdots R$ ($k$ copies, with $k$ written in binary) gives the larger problem $EQ_{\mathsf{REX}\uparrow}$.

:::

::: {#prp-eq-rex-pspace .proposition name="$EQ_{\mathsf{REX}}\in\mathrm{PSPACE}$"}

:::

::: {.proof}

1. By @thm-savitch and closure of $\mathrm{PSPACE}$ under complement, it suffices to show $\overline{EQ_{\mathsf{REX}}}\in\mathrm{NPSPACE}$.

2. Convert $R_1,R_2$ into NFAs $N_1,N_2$ with $q_1,q_2$ states (@thm-regex-to-nfa); this is polynomial in size.

3. Guess a string on which they differ, one symbol at a time, keeping only the *sets* of states each NFA can be in. Accept if at some point exactly one of the two sets contains an accept state. A shortest such string has length at most $2^{q_1+q_2}$ (there are that many pairs of sets), so a counter of polynomially many bits bounds the guessing.

:::

::: {#thm-eq-rex-exp-complete .theorem name="$EQ_{\mathsf{REX}\uparrow}$ is EXPSPACE-complete"}

So $EQ_{\mathsf{REX}\uparrow}$ is a natural problem that is provably not in $\mathrm{PSPACE}$, and not in $\mathrm P$.

:::

::: {.proof}

1. *Membership.* Expand the exponents; the expressions grow by at most an exponential factor, and the algorithm of @prp-eq-rex-pspace runs in polynomial space in the expanded size, that is, exponential space.

2. *Hardness.* Let $M$ decide $A$ in space $2^{n^k}$. Given $w$, we output $\langle R_1,R_2\rangle$ with $R_2=\Delta^*$ (all strings, over the alphabet $\Delta$ of configuration symbols and $\#$), and $R_1$ describing all strings that are *not* rejecting computation histories of $M$ on $w$. Then $L(R_1)=L(R_2)$ iff no rejecting history exists iff $M$ accepts $w$ (as $M$ is a decider).

3. $R_1=R_{\text{bad-start}}\cup R_{\text{bad-window}}\cup R_{\text{bad-reject}}$. The start and reject parts are short. For the windows, the symbols that must correspond in consecutive configurations are $2^{n^k}$ positions apart; exponentiation writes "a gap of exactly $2^{n^k}$ symbols" as $\Delta^{2^{n^k}}$ in $O(n^k)$ symbols. So $R_{\text{bad-window}}$ is the union, over the finitely many illegal windows, of expressions such as $\Delta^*\,abc\,\Delta^{2^{n^k}-2}\,def\,\Delta^*$.

4. The expressions have polynomial size and are written in polynomial time.

:::

## Oracles and relativization

::: {#def-oracle-tm .definition name="Oracle Turing machine"}

An *oracle TM* $M^A$ for a language $A$ has an extra *oracle tape*; when it enters a query state with a string $y$ written there, it learns in one step whether $y\in A$. $\mathrm P^A$ and $\mathrm{NP}^A$ are the languages decided by polynomial-time deterministic and nondeterministic oracle TMs with oracle $A$.

:::

For example $\overline{\mathit{SAT}}\in\mathrm P^{\mathit{SAT}}$ (ask, then flip the answer), so $\mathrm{coNP}\subseteq\mathrm P^{\mathit{SAT}}$.

::: {#thm-relativization .theorem name="Baker–Gill–Solovay"}

There is an oracle $A$ with $\mathrm P^A=\mathrm{NP}^A$, and an oracle $B$ with $\mathrm P^B\ne\mathrm{NP}^B$.

:::

::: {.proof}

1. Take $A=\mathit{TQBF}$. Then $\mathrm{NP}^{\mathit{TQBF}}\subseteq\mathrm{NPSPACE}=\mathrm{PSPACE}$, because a polynomial-space machine can answer each oracle question itself (@thm-tqbf-in-pspace, @thm-savitch). And $\mathrm{PSPACE}\subseteq\mathrm P^{\mathit{TQBF}}$: reduce to $\mathit{TQBF}$ (@thm-tqbf-pspace-complete) and ask. Together with $\mathrm P^{A}\subseteq\mathrm{NP}^{A}$, all are equal.

2. For $B$, consider $L_B=\{1^n: B \text{ contains some string of length } n\}$, which is in $\mathrm{NP}^B$ for every $B$: guess a string of length $n$ and ask.

3. Build $B$ in stages so that no polynomial-time oracle machine decides $L_B$. List the oracle machines $M_1,M_2,\dots$, with $M_i$ running in time $n^i$. At stage $i$, choose $n$ larger than all lengths used before and with $n^i<2^n$; run $M_i$ on $1^n$, answering its queries consistently with the strings already placed in $B$ (and "no" for new ones).

4. If $M_i$ accepts, put no string of length $n$ into $B$; if it rejects, put into $B$ a string of length $n$ that $M_i$ did not query (one exists, as $M_i$ asks fewer than $2^n$ questions). Either way $M_i$ answers wrongly on $1^n$ for the final $B$, and later stages do not change the answers to its queries. So $L_B\notin\mathrm P^B$.

:::

::: {#rmk-intractability-and-oracles-1}

The diagonalization proofs of @thm-atm-undecidable and the hierarchy theorems remain valid when every machine is given the same oracle: they *relativize*. A relativizing proof of $\mathrm P\ne\mathrm{NP}$ would also prove $\mathrm P^A\ne\mathrm{NP}^A$, contradicting the first half of @thm-relativization; a relativizing proof of $\mathrm P=\mathrm{NP}$ would contradict the second half. So diagonalization alone cannot settle the question.

:::

::: {#fig-intractability-and-oracles-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (m) at (0,0) {oracle TM\\ $M$};
\node[hl box] (o) at (4.2,0) {oracle for $A$};
\draw[map] (m.north east) to[bend left=20] node[lab, note, above] {is $y\in A$?} (o.north west);
\draw[map] (o.south west) to[bend left=20] node[lab, note, below] {yes / no, in one step} (m.south east);
\end{tikzpicture}
\end{center}
```

An oracle machine (@def-oracle-tm) gets membership in $A$ for free.

:::

::: {#fig-intractability-and-oracles-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionC] (0,0) ellipse (4.8 and 1.9);
\draw[regionB] (-0.8,-0.1) ellipse (3.6 and 1.45);
\draw[regionA] (-1.8,-0.2) ellipse (2.3 and 0.95);
\node[lab] at (-2.6,-0.2) {$\mathrm{PSPACE}$};
\node[lab] at (1.4,0.5) {$\mathrm{EXPTIME}$};
\node[lab] at (3.6,0.5) {$\mathrm{EXPSPACE}$};
\node[lab, note] at (-1.0,-0.4) {$EQ_{\mathsf{REX}}$};
\node[lab, note] at (3.75,-0.3) {$EQ_{\mathsf{REX}\uparrow}$};
\end{tikzpicture}
\end{center}
```

$EQ_{\mathsf{REX}}$ lies in $\mathrm{PSPACE}$, while with exponentiation the problem is complete for $\mathrm{EXPSPACE}$ and so lies outside $\mathrm{PSPACE}$ (@thm-eq-rex-exp-complete).

:::
