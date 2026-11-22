---
title: "Turing Machines"
sources: [mit18404j-5]
requires: [cs/automata/non-context-free-languages]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 5, in our own wording; proofs written out in steps. -->

## The model

::: {#def-turing-machine .definition name="Turing machine"}

A *Turing machine* (TM) is a 7-tuple $M=(Q,\Sigma,\Gamma,\delta,q_0,q_{\text{acc}},q_{\text{rej}})$ where $Q$ is a finite set of states, $\Sigma$ the input alphabet, $\Gamma\supseteq\Sigma\cup\{\sqcup\}$ the tape alphabet with *blank* $\sqcup\notin\Sigma$, $q_0$ the start state, $q_{\text{acc}}\ne q_{\text{rej}}$ the accept and reject states, and

$$
\delta:Q\times\Gamma\to Q\times\Gamma\times\{\mathrm L,\mathrm R\}
$$

the transition function. The tape is infinite to the right; it starts with the input $w$ in its leftmost cells, followed by blanks, and the head on the first cell. In state $q$ reading $a$, if $\delta(q,a)=(r,b,\mathrm D)$ the machine writes $b$, moves the head one cell in direction $\mathrm D$ (it stays put if asked to move left from the first cell) and enters $r$. It stops when it enters $q_{\text{acc}}$ or $q_{\text{rej}}$.

:::

Unlike a finite automaton, a TM can write on its tape, move both ways, and run for as long as it likes. On an input it can *accept* (halt in $q_{\text{acc}}$), *reject by halting* (in $q_{\text{rej}}$), or *reject by looping*, never halting.

::: {#def-configuration .definition name="Configuration"}

A *configuration* of $M$ is a string $uqv$ with $u,v\in\Gamma^*$ and $q\in Q$: the tape holds $uv$ followed by blanks, the state is $q$, and the head is on the first symbol of $v$. A configuration $C_1$ *yields* $C_2$ if one step of $M$ takes $C_1$ to $C_2$. The start configuration on $w$ is $q_0w$.

:::

::: {#fig-turing-machines-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm, y=0.55cm]
\foreach \i/\s in {0/a,1/a,2/b,3/b,4/c,5/c,6/\sqcup,7/\sqcup,8/\sqcup}
  {\draw[cell frame] (\i,0) rectangle (\i+1,1); \node[lab] at (\i+0.5,0.5) {$\s$};}
\draw[hl cell] (2,0) rectangle (3,1); \node[lab] at (2.5,0.5) {$b$};
\node[lab] at (10,0.5) {$\cdots$};
\node[box] (c) at (2.5,-2.4) {finite control\\ state $q$};
\draw[->, emph] (c.north) -- (2.5,-0.1);
\node[lab, note, anchor=west] at (4.8,-1.2) {read, write, move L or R};
\end{tikzpicture}
\end{center}
```

A Turing machine: a finite control and a head on an infinite tape. The configuration shown is $aa\,q\,bbcc$.

:::

## Recognizable and decidable languages

::: {#def-recognizable-decidable .definition name="Turing-recognizable and decidable languages"}

The language of $M$ is $L(M)=\{w: M \text{ accepts } w\}$. A language is *Turing-recognizable* if it is $L(M)$ for some TM $M$. A *decider* is a TM that halts on every input, and a language is *Turing-decidable* (or *decidable*) if some decider recognizes it.

:::

So a recognizer must accept the strings in the language but may loop on the others; a decider must always answer.

::: {#exm-tm-abc .example name="A decider for $a^kb^kc^k$"}

The language $B=\{a^kb^kc^k: k\ge0\}$ is not context-free (@exm-anbncn-not-cf) but is decidable. On input $w$:

1. scan the input; reject unless $w\in a^*b^*c^*$;
2. return to the start; cross off one $a$, one $b$ and one $c$ (replacing each by a new symbol $\times$), and return to the start; repeat while any of the three symbols remain;
3. accept if all symbols are crossed off; reject if some round finds one kind of symbol used up before the others.

Each round removes one symbol of each kind, so the machine halts after at most $k+1$ rounds, and accepts exactly when the three counts are equal.

:::

::: {#fig-turing-machines-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm, y=0.5cm]
\foreach \r/\row in {0/{a,a,b,b,c,c},1/{\times,a,\times,b,\times,c},2/{\times,\times,\times,\times,\times,\times}} {
  \foreach \s [count=\i from 0] in \row {
    \draw[cell frame] (\i,-1.5*\r) rectangle (\i+1,-1.5*\r+1);
    \node[lab] at (\i+0.5,-1.5*\r+0.5) {$\s$};
  }
}
\node[lab, note, anchor=west] at (6.6,0.5) {input};
\node[lab, note, anchor=west] at (6.6,-1) {after round 1};
\node[lab, note, anchor=west] at (6.6,-2.5) {after round 2: accept};
\end{tikzpicture}
\end{center}
```

The decider of @exm-tm-abc on $aabbcc$.

:::

::: {#rmk-turing-machines-1}

The classes are nested: regular $\subsetneq$ context-free $\subsetneq$ decidable $\subsetneq$ Turing-recognizable. The second inclusion is @thm-cfl-decidable, its strictness is @exm-tm-abc, and the last is strict by @thm-atm-undecidable.

:::
