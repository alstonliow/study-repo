---
title: "Space Complexity and PSPACE"
sources: [mit18404j-17]
requires: [cs/theory/cook-levin]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 17, in our own wording; proofs written out in steps. -->

Space, unlike time, can be reused. This makes space a more generous resource and gives it a different theory.

::: {#def-space-class .definition name="SPACE, NSPACE, PSPACE"}

A TM *runs in space* $s(n)$ if on every input of length $n$ it halts and every branch scans at most $s(n)$ tape cells. Then

$$
\begin{aligned}
\mathrm{SPACE}(s(n))&=\{A: \text{some deterministic 1-tape TM decides } A \text{ in space } O(s(n))\},\\
\mathrm{NSPACE}(s(n))&=\{A: \text{some 1-tape NTM decides } A \text{ in space } O(s(n))\},
\end{aligned}
$$

and $\mathrm{PSPACE}=\bigcup_k\mathrm{SPACE}(n^k)$, $\mathrm{NPSPACE}=\bigcup_k\mathrm{NSPACE}(n^k)$.

:::

::: {#thm-time-space-relations .theorem name="Time versus space"}

For $t(n)\ge n$ and $s(n)\ge n$,

$$
\mathrm{TIME}(t(n))\subseteq\mathrm{SPACE}(t(n)),\qquad \mathrm{SPACE}(s(n))\subseteq\bigcup_c\mathrm{TIME}\big(c^{s(n)}\big).
$$

Hence $\mathrm P\subseteq\mathrm{PSPACE}$, and also $\mathrm{NP}\subseteq\mathrm{PSPACE}\subseteq\mathrm{EXPTIME}=\bigcup_k\mathrm{TIME}(2^{n^k})$.

:::

::: {.proof}

1. In $t(n)$ steps a machine can visit at most $t(n)$ cells.

2. A decider running in space $s(n)$ with $q$ states and $g$ tape symbols has at most $q\,s(n)\,g^{s(n)}\le c^{s(n)}$ configurations. It never repeats a configuration (it would then loop, yet it halts), so it runs for at most $c^{s(n)}$ steps.

3. For $\mathrm{NP}\subseteq\mathrm{PSPACE}$: a polynomial-time NTM's branches have polynomial length; a deterministic machine can try the branches one after another, reusing the same space for each, plus space for the current sequence of choices.

:::

::: {#fig-space-complexity-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionC] (0,0) ellipse (4.6 and 1.9);
\draw[regionB] (-0.7,-0.1) ellipse (3.6 and 1.5);
\draw[regionA] (-1.5,-0.2) ellipse (2.5 and 1.05);
\draw[regionA] (-2.4,-0.3) ellipse (1.3 and 0.6);
\node[lab] at (-2.4,-0.3) {$\mathrm P$};
\node[lab] at (-0.2,0.2) {$\mathrm{NP}$};
\node[lab] at (1.85,0.6) {$\mathrm{PSPACE}$};
\node[lab] at (3.7,0.4) {$\mathrm{EXPTIME}$};
\node[lab, note] at (2.0,-0.3) {$\mathit{TQBF}$};
\end{tikzpicture}
\end{center}
```

$\mathrm P\subseteq\mathrm{NP}\subseteq\mathrm{PSPACE}\subseteq\mathrm{EXPTIME}$ (@thm-time-space-relations). Only $\mathrm P\ne\mathrm{EXPTIME}$ is known (@thm-time-hierarchy), so at least one inclusion is strict.

:::

## Quantified Boolean formulas

::: {#def-tqbf .definition name="TQBF"}

A *quantified Boolean formula* is a Boolean formula preceded by quantifiers $\exists x$ or $\forall x$ over its variables, which range over $\{0,1\}$; when every variable is quantified it is true or false. $\mathit{TQBF}=\{\langle\phi\rangle: \phi \text{ is a true fully quantified Boolean formula}\}$.

:::

For example $\forall x\,\exists y\,[(x\vee y)\wedge(\bar x\vee\bar y)]$ is true (take $y=\bar x$), and $\exists y\,\forall x\,[(x\vee y)\wedge(\bar x\vee\bar y)]$ is false. $\mathit{SAT}$ is the special case with only $\exists$ quantifiers.

::: {#thm-tqbf-in-pspace .theorem name="TQBF is in PSPACE"}

:::

::: {.proof}

1. Evaluate recursively. If $\phi$ has no quantifiers it has no variables; evaluate it.

2. If $\phi=\exists x\,\psi$, evaluate $\psi$ with $x=0$ and then with $x=1$, reusing the same space, and accept iff either is true. If $\phi=\forall x\,\psi$, accept iff both are true.

3. The recursion depth is the number $m$ of variables, and each level stores only the value of its variable and a constant amount of bookkeeping, besides a copy of the formula. So the space is $O(n)$, although the time is exponential.

:::

::: {#fig-space-complexity-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=1.1cm, every node/.style={small vertex}, level 1/.style={sibling distance=3.4cm}, level 2/.style={sibling distance=1.6cm}]
\node[hl state] {$\forall$}
  child {node[hl state] {$\exists$} child {node {0}} child {node[hl state] {1}} edge from parent node[lab, note, left] {$x=0$}}
  child {node[hl state] {$\exists$} child {node[hl state] {1}} child {node {0}} edge from parent node[lab, note, right] {$x=1$}};
\node[lab, note] at (-2.5,-2.75) {$y=0$};
\node[lab, note] at (-0.9,-2.75) {$y=1$};
\node[lab, note] at (0.9,-2.75) {$y=0$};
\node[lab, note] at (2.5,-2.75) {$y=1$};
\end{tikzpicture}
\end{center}
```

Evaluating $\forall x\,\exists y\,[(x\vee y)\wedge(\bar x\vee\bar y)]$ as in @thm-tqbf-in-pspace: leaves are the values of the formula; $\exists$ takes an OR and $\forall$ an AND. Only one root-to-leaf path is stored at a time.

:::

::: {#exm-ladder-dfa .example name="Word ladders"}

A *ladder* is a sequence of strings of the same length, each differing from the previous one in a single symbol. Let $\mathit{LADDER}_{\mathsf{DFA}}=\{\langle B,u,v\rangle: B \text{ is a DFA, and a ladder from } u \text{ to } v \text{ stays inside } L(B)\}$. An NTM decides it in linear space by guessing the ladder one rung at a time, storing only the current string and a counter up to $|\Sigma|^{|u|}$ (a shortest ladder never repeats a string), and checking each rung with $B$. So $\mathit{LADDER}_{\mathsf{DFA}}\in\mathrm{NSPACE}(n)$; Savitch's theorem (@thm-savitch) puts it in $\mathrm{SPACE}(n^2)$.

:::
