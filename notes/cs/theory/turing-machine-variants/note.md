---
title: "Variants of Turing Machines and the Church–Turing Thesis"
sources: [mit18404j-6]
requires: [cs/theory/turing-machines]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 6, in our own wording; proofs written out in steps. -->

Reasonable changes to the Turing machine model do not change which languages can be recognized or decided. This robustness is the evidence for the Church–Turing thesis.

## Multitape machines

::: {#def-multitape-tm .definition name="Multitape Turing machine"}

A *$k$-tape Turing machine* has $k$ tapes, each with its own head; the input starts on tape 1 and the others are blank. Its transition function is

$$
\delta:Q\times\Gamma^k\to Q\times\Gamma^k\times\{\mathrm L,\mathrm R\}^k,
$$

so each step reads all $k$ heads, writes on all tapes and moves each head.

:::

::: {#thm-multitape-equivalent .theorem name="Multitape machines are no stronger"}

Every multitape TM has an equivalent single-tape TM.

:::

::: {.proof}

1. Let $M$ have $k$ tapes. The single-tape machine $S$ stores the contents of the $k$ tapes one after another, separated by a new symbol $\#$; for each symbol $a$ it has a *dotted* copy $\dot a$ marking the cell under that tape's head.

2. To simulate one step of $M$, $S$ scans its tape from left to right to read the $k$ dotted symbols (remembering them in its finite state), then scans again to write the new symbols and move each dot one cell left or right.

3. If a head moves onto the $\#$ at the right end of its segment, $S$ shifts the rest of the tape one cell to the right to make room for a blank.

4. $S$ enters the accept or reject state exactly when $M$ does, so it accepts the same strings and halts on the same inputs.

:::

::: {#fig-turing-machine-variants-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=0.5cm]
\foreach \t/\row/\h in {0/{a,a,b,a}/1,1/{0,1,1}/2,2/{x,y}/0} {
  \foreach \s [count=\i from 0] in \row {
    \ifnum\i=\h \draw[hl cell] (\i,-1.4*\t) rectangle (\i+1,-1.4*\t+1);
    \else \draw[cell frame] (\i,-1.4*\t) rectangle (\i+1,-1.4*\t+1); \fi
    \node[lab] at (\i+0.5,-1.4*\t+0.5) {$\s$};
  }
  \node[lab, note, anchor=east] at (-0.3,-1.4*\t+0.5) {tape \pgfmathparse{int(\t+1)}\pgfmathresult};
}
\draw[map, emph] (6,-1.3) -- (8,-1.3);
\foreach \s [count=\i from 0] in {\#,a,\dot a,b,a,\#,0,1,\dot 1,\#,\dot x,y,\#} {
  \draw[cell frame] (\i+8.6,-1.8) rectangle (\i+9.6,-0.8);
  \node[lab] at (\i+9.1,-1.3) {$\s$};
}
\node[lab, note] at (15,-2.5) {one tape; dots mark the heads};
\end{tikzpicture}
\end{center}
```

The simulation of @thm-multitape-equivalent: three tapes (heads shaded) are stored on one tape between separators.

:::

## Nondeterministic machines

::: {#def-ntm .definition name="Nondeterministic Turing machine"}

A *nondeterministic* TM has a transition function $\delta:Q\times\Gamma\to\mathcal P(Q\times\Gamma\times\{\mathrm L,\mathrm R\})$. Its computations form a tree of configurations, and it accepts $w$ if some branch reaches $q_{\text{acc}}$. It is a *decider* if every branch halts on every input.

:::

::: {#thm-ntm-equivalent .theorem name="Nondeterminism adds no power"}

Every nondeterministic TM $N$ has an equivalent deterministic TM $D$; if $N$ is a decider, $D$ can be made a decider too.

:::

::: {.proof}

1. $D$ explores the computation tree of $N$ on $w$ *breadth-first*. Depth-first search would fail: it could follow an infinite branch forever and miss an accepting branch.

2. Let $b$ be the largest number of choices in any step of $N$. A node of the tree at depth $d$ is named by an *address* in $\{1,\dots,b\}^d$, the choices made on the way down.

3. $D$ uses three tapes (enough, by @thm-multitape-equivalent): tape 1 keeps $w$, tape 2 is a scratch copy for simulating $N$, and tape 3 holds an address. For each address in order of length and then lexicographically, $D$ copies $w$ to tape 2 and runs $N$ along the choices the address gives, abandoning it if a choice is invalid.

4. If some branch accepts, $D$ reaches its address after finitely many others and accepts. Otherwise $D$ never accepts.

5. If $N$ is a decider, its tree is finite by König's lemma (finitely many choices at each node, no infinite branch), so it has some depth $d$. $D$ rejects once every address of some length leads to a halted (rejecting) branch.

:::

::: {#fig-turing-machine-variants-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=0.9cm, every node/.style={small vertex}, level 1/.style={sibling distance=2.6cm}, level 2/.style={sibling distance=1.2cm}]
\node {1}
  child {node {2} child {node {5}} child {node {6}}}
  child {node {3} child {node {7}}}
  child {node {4} child {node {8}} child {node[hl state] {9}}};
\node[lab, note, anchor=west] at (3.9,-0.9) {visit in order};
\node[lab, note, anchor=west] at (3.9,-1.35) {of depth: 1, 2, 3, \dots};
\end{tikzpicture}
\end{center}
```

The deterministic simulation of @thm-ntm-equivalent visits the configurations of $N$'s computation tree level by level (numbered in visiting order), so an accepting configuration (shaded) at finite depth is found even if other branches are infinite.

:::

## Enumerators

::: {#def-enumerator .definition name="Enumerator"}

An *enumerator* is a TM with an extra output device on which it prints strings; it starts with a blank tape and may run forever. The language it *enumerates* is the set of strings it ever prints, in any order and possibly with repetitions.

:::

::: {#thm-enumerator-recognizable .theorem name="Recognizable means enumerable"}

A language is Turing-recognizable if and only if some enumerator enumerates it.

:::

::: {.proof}

1. If an enumerator $E$ enumerates $A$, a TM recognizing $A$ runs $E$ on the side and accepts its input $w$ as soon as $E$ prints $w$.

2. Conversely, let $M$ recognize $A$ and list $\Sigma^*$ as $s_1,s_2,\dots$. For $i=1,2,3,\dots$ the enumerator runs $M$ for $i$ steps on each of $s_1,\dots,s_i$ and prints those that accept.

3. Every $s_j\in A$ is accepted by $M$ in some number $t$ of steps, so it is printed in round $\max(j,t)$; strings outside $A$ are never printed. Running each input for a bounded number of steps avoids getting stuck on an input where $M$ loops.

:::

## The Church–Turing thesis

::: {#rmk-church-turing-thesis}

Many other models (the $\lambda$-calculus, register machines, Post systems, ordinary programming languages with unbounded memory) were shown to be equivalent to Turing machines. The *Church–Turing thesis* states that the intuitive notion of an algorithm is captured exactly by Turing machines: a problem is algorithmically solvable iff the corresponding language is decidable. It is a claim about the informal notion, not a theorem. From now on we describe TMs by high-level algorithms, assuming implementation details can be filled in.

:::

::: {#def-encoding .definition name="Encodings"}

For objects $O_1,\dots,O_k$ (numbers, graphs, automata, grammars, Turing machines) we write $\langle O_1,\dots,O_k\rangle$ for a fixed encoding of them as a string over some alphabet. A TM given an input that is not a valid encoding rejects it, so we may assume inputs are well formed.

:::
