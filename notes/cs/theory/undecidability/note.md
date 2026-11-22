---
title: "Undecidability and Diagonalization"
sources: [mit18404j-8]
requires: [cs/theory/decidable-languages, math/discrete/functions/cantor-diagonalization]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 8, in our own wording; proofs written out in steps. The program-based version of the same diagonal argument is @thm-halting-undecidable. -->

## The acceptance problem

::: {#def-atm .definition name="Acceptance problem for Turing machines"}

$$
A_{\mathsf{TM}}=\{\langle M,w\rangle: M \text{ is a TM that accepts } w\}.
$$

:::

::: {#thm-atm-recognizable .theorem name="Universal Turing machine"}

$A_{\mathsf{TM}}$ is Turing-recognizable.

:::

::: {.proof}

1. The *universal Turing machine* $U$, on input $\langle M,w\rangle$, simulates $M$ on $w$ step by step, keeping $M$'s tape and state on its own tape and looking up each move in the description of $M$.

2. If $M$ accepts, $U$ accepts; if $M$ rejects, $U$ rejects. If $M$ loops, so does $U$. So $L(U)=A_{\mathsf{TM}}$.

:::

$U$ is a recognizer, not a decider: it cannot tell a long computation from one that never ends.

::: {#thm-atm-undecidable .theorem name="$A_{\mathsf{TM}}$ is undecidable" related="thm-halting-undecidable"}

No Turing machine decides $A_{\mathsf{TM}}$.

:::

::: {.proof}

1. Suppose a decider $H$ decides $A_{\mathsf{TM}}$: $H$ accepts $\langle M,w\rangle$ if $M$ accepts $w$, and rejects otherwise.

2. Build a TM $D$ that, on input $\langle M\rangle$, runs $H$ on $\langle M,\langle M\rangle\rangle$ and does the opposite: it accepts if $H$ rejects and rejects if $H$ accepts. $D$ always halts, because $H$ does.

3. Run $D$ on its own description $\langle D\rangle$. By step 2, $D$ accepts $\langle D\rangle$ iff $H$ rejects $\langle D,\langle D\rangle\rangle$, iff $D$ does not accept $\langle D\rangle$.

4. This is a contradiction, so $H$ does not exist.

:::

::: {#fig-undecidability-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.15cm, y=0.62cm]
\foreach \j/\t in {1/{\langle M_1\rangle},2/{\langle M_2\rangle},3/{\langle M_3\rangle},4/{\langle M_4\rangle},5/{\cdots}} \node[lab, note] at (\j,0.9) {$\t$};
\foreach \i/\t in {1/M_1,2/M_2,3/M_3,4/M_4,5/\vdots} \node[lab] at (-0.1,-\i+1) {$\t$};
\foreach \i/\row in {1/{acc,rej,acc,rej},2/{acc,acc,acc,acc},3/{rej,rej,rej,rej},4/{acc,acc,rej,rej}} {
  \foreach \s [count=\j] in \row {
    \ifnum\i=\j \draw[hl cell] (\j-0.45,-\i+0.6) rectangle (\j+0.45,-\i+1.4);
    \else \draw[cell frame] (\j-0.45,-\i+0.6) rectangle (\j+0.45,-\i+1.4); \fi
    \node[lab, note] at (\j,-\i+1) {\s};
  }
}
\node[lab] at (-0.1,-4.3) {$D$};
\foreach \s [count=\j] in {rej,rej,acc,acc} {\draw[hl cell] (\j-0.45,-4.7) rectangle (\j+0.45,-3.9); \node[lab, note] at (\j,-4.3) {\s};}
\node[lab] at (5,-4.3) {$?$};
\end{tikzpicture}
\end{center}
```

The diagonal argument of @thm-atm-undecidable: entry $(i,j)$ is $H$'s answer on $\langle M_i,\langle M_j\rangle\rangle$. $D$ flips the diagonal, so it differs from every $M_i$ at $\langle M_i\rangle$ and cannot appear in the list; its entry at $\langle D\rangle$ would have to differ from itself.

:::

::: {#rmk-undecidability-1}

Counting gives a softer result: there are countably many TMs but uncountably many languages over $\Sigma$, so some languages are not even recognizable (@prp-most-problems-undecidable). The diagonal argument above gives an explicit undecidable language.

:::

## Recognizable and co-recognizable

::: {#thm-decidable-iff-co-recognizable .theorem name="Decidable iff recognizable and co-recognizable"}

A language $A$ is decidable if and only if both $A$ and its complement $\overline A$ are Turing-recognizable ($A$ is *co-recognizable*).

:::

::: {.proof}

1. If $A$ is decidable, so is $\overline A$ (swap accept and reject), and deciders are recognizers.

2. Conversely, let $M_1$ recognize $A$ and $M_2$ recognize $\overline A$. On input $w$, run $M_1$ and $M_2$ in parallel, one step of each in turn.

3. Every $w$ lies in $A$ or in $\overline A$, so one of the two machines eventually accepts. Accept if $M_1$ accepts and reject if $M_2$ accepts. This machine always halts and decides $A$.

:::

::: {#cor-complement-atm-unrecognizable .corollary name="$\overline{A_{\mathsf{TM}}}$ is not recognizable"}

:::

::: {.proof}

1. $A_{\mathsf{TM}}$ is recognizable (@thm-atm-recognizable).

2. If $\overline{A_{\mathsf{TM}}}$ were recognizable too, $A_{\mathsf{TM}}$ would be decidable by @thm-decidable-iff-co-recognizable, contradicting @thm-atm-undecidable.

:::

::: {#fig-undecidability-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (-1.2,0) ellipse (2.6 and 1.4);
\draw[regionB] (1.2,0) ellipse (2.6 and 1.4);
\node[lab] at (-2.4,0.3) {recognizable};
\node[lab] at (2.5,0.3) {co-recognizable};
\node[lab] at (0,0.3) {decidable};
\node[lab, note] at (-2.4,-0.4) {$A_{\mathsf{TM}}$};
\node[lab, note] at (2.5,-0.4) {$\overline{A_{\mathsf{TM}}}$};
\node[lab, note] at (0,-0.4) {$A_{\mathsf{CFG}}$};
\end{tikzpicture}
\end{center}
```

@thm-decidable-iff-co-recognizable: the decidable languages are exactly the intersection of the recognizable and the co-recognizable ones.

:::
