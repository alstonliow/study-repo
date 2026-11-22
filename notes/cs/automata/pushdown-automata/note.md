---
title: "Pushdown Automata"
sources: [mit18404j-4]
requires: [cs/automata/context-free-grammars]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 4, in our own wording; proofs written out in steps. -->

## Pushdown automata

::: {#def-pda .definition name="Pushdown automaton"}

A *pushdown automaton* (PDA) is an NFA with an unbounded stack. Formally it is a 6-tuple $P=(Q,\Sigma,\Gamma,\delta,q_0,F)$ where $Q,\Sigma,q_0,F$ are as in an NFA, $\Gamma$ is the *stack alphabet*, and

$$
\delta:Q\times\Sigma_\varepsilon\times\Gamma_\varepsilon\to\mathcal P(Q\times\Gamma_\varepsilon).
$$

A transition $(r,c)\in\delta(q,a,b)$, written $a,b\to c$, means: in state $q$, read $a$ (or nothing if $a=\varepsilon$), pop $b$ from the top of the stack (or nothing), push $c$ (or nothing), and go to $r$. $P$ accepts $w$ if some branch reads all of $w$ and ends in a state of $F$.

:::

The stack is a memory of unbounded size, but only its top is visible. PDAs are nondeterministic by definition; deterministic PDAs are strictly weaker.

::: {#exm-pda-0n1n .example name="A PDA for $0^k1^k$"}

To recognize $\{0^k1^k: k\ge0\}$: push a marker $\$$, push a $0$ for each $0$ read, then pop a $0$ for each $1$ read; if the marker is on top when the input ends, accept. A $0$ after a $1$, a $1$ with only $\$$ on the stack, or input left over when the stack empties all kill the branch.

:::

::: {#fig-pushdown-automata-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[accept state] (1) at (0,0) {$q_1$};
\node[state] (2) at (2.8,0) {$q_2$};
\node[state] (3) at (5.6,0) {$q_3$};
\node[accept state] (4) at (8.4,0) {$q_4$};
\draw[start] (1.west) -- ++(-0.6,0);
\draw (1) edge[trans] node[edge label] {$\varepsilon,\varepsilon\to\$$} (2);
\draw (2) edge[trans, loop above] node[edge label] {$0,\varepsilon\to0$} (2);
\draw (2) edge[trans] node[edge label] {$1,0\to\varepsilon$} (3);
\draw (3) edge[trans, loop above] node[edge label] {$1,0\to\varepsilon$} (3);
\draw (3) edge[trans] node[edge label] {$\varepsilon,\$\to\varepsilon$} (4);
\end{tikzpicture}
\end{center}
```

The PDA of @exm-pda-0n1n. A label $a,b\to c$ reads $a$, pops $b$ and pushes $c$.

:::

::: {#exm-pda-palindromes .example name="Even palindromes"}

For $\{ww^{\mathcal R}: w\in\{0,1\}^*\}$, where $w^{\mathcal R}$ is $w$ reversed, a PDA pushes the symbols it reads, *guesses* nondeterministically that it has reached the middle, and from then on pops a symbol for each symbol read, requiring them to match; it accepts if the marker is on top at the end. The guess is essential: no deterministic PDA recognizes this language.

:::

## Grammars and pushdown automata

::: {#thm-cfg-to-pda .theorem name="From grammars to pushdown automata"}

For every CFG $G$ there is a PDA $P$ with $L(P)=L(G)$.

:::

::: {.proof}

1. $P$ guesses a leftmost derivation of its input and checks it on the stack. It starts by pushing $\$$ and then the start variable $S$.

2. It repeats the following, depending on the top of the stack:
    a. a variable $A$: pop $A$ and push the right side $u$ of some rule $A\to u$, chosen nondeterministically, with its leftmost symbol on top;
    b. a terminal $a$: read the next input symbol; if it is $a$, pop it, otherwise this branch dies;
    c. the marker $\$$: pop it and accept if the input is used up.

3. (Pushing a string $u$ takes $|u|$ steps through new states; this is allowed.)

4. At every moment of a branch, the input read so far followed by the stack contents (without $\$$) is a sentential form of a leftmost derivation from $S$. So a branch accepts $w$ only if $S\overset{*}{\Rightarrow}w$.

5. Conversely, if $S\overset{*}{\Rightarrow}w$, the branch that chooses the rules of a leftmost derivation of $w$ matches every terminal and accepts. So $L(P)=L(G)$.

:::

::: {#fig-pushdown-automata-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.00,0.00) rectangle (0.50,0.50); \node[lab] at (0.25,0.25) {$S$};
\draw[cell frame] (0.00,-0.50) rectangle (0.50,0.00); \node[lab] at (0.25,-0.25) {$\$$};
\node[lab, tick] at (0.25,0.80) {start};
\draw[hl cell] (1.30,0.00) rectangle (1.80,0.50); \node[lab] at (1.55,0.25) {$0$};
\draw[cell frame] (1.30,-0.50) rectangle (1.80,0.00); \node[lab] at (1.55,-0.25) {$S$};
\draw[cell frame] (1.30,-1.00) rectangle (1.80,-0.50); \node[lab] at (1.55,-0.75) {$1$};
\draw[cell frame] (1.30,-1.50) rectangle (1.80,-1.00); \node[lab] at (1.55,-1.25) {$\$$};
\node[lab, tick] at (1.55,0.80) {$S\to0S1$};
\draw[hl cell] (2.60,0.00) rectangle (3.10,0.50); \node[lab] at (2.85,0.25) {$S$};
\draw[cell frame] (2.60,-0.50) rectangle (3.10,0.00); \node[lab] at (2.85,-0.25) {$1$};
\draw[cell frame] (2.60,-1.00) rectangle (3.10,-0.50); \node[lab] at (2.85,-0.75) {$\$$};
\node[lab, tick] at (2.85,0.80) {read 0};
\draw[hl cell] (3.90,0.00) rectangle (4.40,0.50); \node[lab] at (4.15,0.25) {$0$};
\draw[cell frame] (3.90,-0.50) rectangle (4.40,0.00); \node[lab] at (4.15,-0.25) {$S$};
\draw[cell frame] (3.90,-1.00) rectangle (4.40,-0.50); \node[lab] at (4.15,-0.75) {$1$};
\draw[cell frame] (3.90,-1.50) rectangle (4.40,-1.00); \node[lab] at (4.15,-1.25) {$1$};
\draw[cell frame] (3.90,-2.00) rectangle (4.40,-1.50); \node[lab] at (4.15,-1.75) {$\$$};
\node[lab, tick] at (4.15,0.80) {$S\to0S1$};
\draw[hl cell] (5.20,0.00) rectangle (5.70,0.50); \node[lab] at (5.45,0.25) {$S$};
\draw[cell frame] (5.20,-0.50) rectangle (5.70,0.00); \node[lab] at (5.45,-0.25) {$1$};
\draw[cell frame] (5.20,-1.00) rectangle (5.70,-0.50); \node[lab] at (5.45,-0.75) {$1$};
\draw[cell frame] (5.20,-1.50) rectangle (5.70,-1.00); \node[lab] at (5.45,-1.25) {$\$$};
\node[lab, tick] at (5.45,0.80) {read 0};
\draw[hl cell] (6.50,0.00) rectangle (7.00,0.50); \node[lab] at (6.75,0.25) {$1$};
\draw[cell frame] (6.50,-0.50) rectangle (7.00,0.00); \node[lab] at (6.75,-0.25) {$1$};
\draw[cell frame] (6.50,-1.00) rectangle (7.00,-0.50); \node[lab] at (6.75,-0.75) {$\$$};
\node[lab, tick] at (6.75,0.80) {$S\to\varepsilon$};
\draw[hl cell] (7.80,0.00) rectangle (8.30,0.50); \node[lab] at (8.05,0.25) {$1$};
\draw[cell frame] (7.80,-0.50) rectangle (8.30,0.00); \node[lab] at (8.05,-0.25) {$\$$};
\node[lab, tick] at (8.05,0.80) {read 1};
\draw[hl cell] (9.10,0.00) rectangle (9.60,0.50); \node[lab] at (9.35,0.25) {$\$$};
\node[lab, tick] at (9.35,0.80) {read 1};
\end{tikzpicture}
\end{center}
```

The PDA of @thm-cfg-to-pda for $S\to0S1\mid\varepsilon$ on input $0011$: the stack (top shaded) after each step. Variables on top are expanded by a guessed rule, terminals on top are matched against the input, and the final $\$$ means accept.

:::

::: {#thm-pda-cfg-equivalence .theorem name="PDAs recognize exactly the CFLs"}

A language is context-free if and only if some PDA recognizes it.

:::

::: {.proof}

1. One direction is @thm-cfg-to-pda.

2. For the other, modify a PDA $P$ so that it has a single accept state, empties its stack before accepting, and each transition either pushes one symbol or pops one symbol, but not both.

3. For each pair of states $p,q$ make a variable $A_{pq}$ meant to generate the strings that take $P$ from $p$ with empty stack to $q$ with empty stack.

4. On such a computation the first move pushes some symbol and the last move pops something. If the symbol pushed first is the one popped last, add the rule $A_{pq}\to aA_{rs}b$, where $a$ is read on the first move (to $r$) and $b$ on the last (from $s$). Otherwise the stack is empty at some middle state $r$; add $A_{pq}\to A_{pr}A_{rq}$. Add $A_{pp}\to\varepsilon$.

5. By induction on the length of computations and of derivations, $A_{pq}\overset{*}{\Rightarrow}w$ exactly when $w$ takes $P$ from $p$ to $q$ with empty stack at both ends. With start variable $A_{q_0q_{\text{accept}}}$ the grammar generates $L(P)$.

:::

::: {#cor-regular-subset-cfl .corollary name="Regular languages are context-free"}

Every regular language is context-free, and the inclusion is strict.

:::

::: {.proof}

1. An NFA is a PDA that never uses its stack, so by @thm-pda-cfg-equivalence every regular language is context-free.

2. $\{0^k1^k\}$ is context-free (@exm-cfg-examples) but not regular (@exm-0n1n-nonregular).

:::
