---
title: "Complexity: P, NP and Reductions"
sources: [mit6006-19, mit6006r-19]
requires: [cs/theory/computability, cs/algorithms/problems-and-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 19 and Recitation 19, in our own wording; proofs written out in steps. The informal versions in @sec-math-discrete-sequences-big-o (FIT1058 extra) cover the same ideas; a merge is proposed to the owner. -->

## Decision problems and decidability

::: {#def-decision-problem .definition name="Decision problem"}

A *decision problem* assigns to every input the answer YES or NO; the inputs are split into *YES inputs* and *NO inputs*. Examples: does a weighted graph have a path from $s$ to $t$ of weight at most $d$? does it have a negative-weight cycle? a simple path of weight at least $d$? does a set of integers have a subset with sum $T$? can a player force a win from a given chess position? does a program halt on a given input?

:::

A problem is *decidable* if some program (of constant size, independent of the input) solves it in finite time on every input (@def-halting-problem).

::: {#prp-most-problems-undecidable .proposition name="Most decision problems are undecidable"}

There are only countably many programs but uncountably many decision problems. So most decision problems are not solved by any program.

:::

::: {.proof}

1. A program is a finite string of bits, so the set of programs is countable (@prp-finite-strings-countable).

2. Inputs are also finite bit strings, which can be listed as $x_0,x_1,x_2,\dots$; a decision problem is then an infinite sequence of bits (the answer for each $x_i$), that is, a subset of $\mathbb N$. The set of these is uncountable (@thm-power-set-uncountable).

3. Each program solves at most one problem, so the solvable problems form a countable subset of an uncountable set, and all the others are undecidable.

:::

Concrete undecidable problems exist too, such as the halting problem (@thm-halting-undecidable). Fortunately, most problems that arise in practice have an algorithmic structure and are decidable; the question is how fast.

## Complexity classes

::: {#def-p-exp-r .definition name="The classes R, EXP and P" related="def-classes-p-and-np-extra"}

$\mathrm R$ is the class of decision problems decidable in finite time, $\mathrm{EXP}$ those decidable in time $2^{n^{O(1)}}$, and $\mathrm P$ those decidable in time $n^{O(1)}$, where $n$ is the input size. Then $\mathrm P\subseteq\mathrm{EXP}\subseteq\mathrm R$, and both inclusions are strict (by the time hierarchy theorems, which we do not prove). For example, deciding who wins a generalised chess position on an $n\times n$ board is in $\mathrm{EXP}$ but not in $\mathrm P$.

:::

::: {#def-np .definition name="NP" related="def-classes-p-and-np-extra"}

$\mathrm{NP}$ (*nondeterministic polynomial time*) is the class of decision problems that have a polynomial-time *verifier*: an algorithm $V$ that takes an input $I$ and a *certificate* $c$, a bit string of length polynomial in $|I|$, runs in time polynomial in $|I|$, and satisfies

1. if $I$ is a YES input, then $V(I,c)$ outputs YES for some certificate $c$;
2. if $I$ is a NO input, then $V(I,c)$ outputs NO for every certificate $c$.

:::

A certificate is a short proof that the answer is YES, and no proof can convince the verifier of a NO input. For subset sum the certificate is the subset (add it up and compare with $T$); for a negative-weight cycle, the cycle; for a long simple path, the path (check it is simple and add its weights).

::: {#prp-p-np-exp .proposition name="$\mathrm P\subseteq\mathrm{NP}\subseteq\mathrm{EXP}$"}

Every problem in $\mathrm P$ is in $\mathrm{NP}$, and every problem in $\mathrm{NP}$ is in $\mathrm{EXP}$.

:::

::: {.proof}

1. If $A$ solves a problem in polynomial time, the verifier $V(I,c)=A(I)$, which ignores $c$, satisfies both conditions.

2. If $V$ is a verifier whose certificates have length at most $p(n)$ and whose running time is at most $q(n)$, try all at most $2^{p(n)+1}$ certificates and answer YES if $V$ accepts one. This is correct by the two conditions and takes $O\bigl(2^{p(n)+1}q(n)\bigr)=2^{n^{O(1)}}$ time.

:::

::: {#fig-complexity-classes-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionC] (0,0) ellipse (4.2 and 2.2);
\draw[regionB] (-0.6,-0.2) ellipse (3.2 and 1.7);
\draw[regionA] (-1.2,-0.4) ellipse (2.2 and 1.2);
\draw[regionA] (-2.0,-0.6) ellipse (1.0 and 0.65);
\node[lab] at (3.4,0.2) {$\mathrm R$};
\node[lab] at (2.0,0.4) {$\mathrm{EXP}$};
\node[lab] at (0.1,0.45) {$\mathrm{NP}$};
\node[lab] at (-2.0,-0.6) {$\mathrm P$};
\draw[hl] (0.02,-1.17) arc[start angle=-50, end angle=40, x radius=1.9, y radius=1.0];
\node[lab,tick, anchor=east] at (0.45,-0.75) {NP-complete};
\node[lab,tick] at (1.8,-0.35) {chess};
\node[lab,tick] at (-2.0,-0.95) {shortest paths};
\node[lab,tick] at (0,-2.55) {outside $\mathrm R$: the halting problem};
\end{tikzpicture}
\end{center}
```

The classes $\mathrm P\subseteq\mathrm{NP}\subseteq\mathrm{EXP}\subseteq\mathrm R$, drawn as most researchers believe them to be ($\mathrm P\ne\mathrm{NP}$; only $\mathrm P\ne\mathrm{EXP}$ and $\mathrm{EXP}\ne\mathrm R$ are proved). The NP-complete problems are the hardest problems in $\mathrm{NP}$, at its outer edge (for example SAT and subset sum).

:::

Whether $\mathrm P=\mathrm{NP}$ is open; most researchers believe $\mathrm P\ne\mathrm{NP}$, that is, finding solutions is harder than checking them. A proof either way earns one of the Millennium Prizes.

## Reductions and NP-completeness

::: {#def-polynomial-reduction .definition name="Polynomial reduction, NP-hard, NP-complete" related="def-np-hard-np-complete-extra"}

A *reduction* from problem $A$ to problem $B$ converts any instance of $A$ into an instance of $B$, in polynomial time, so that the answer for $B$ gives the answer for $A$ (compare @def-reduction). Then $B$ is at least as hard as $A$, written $A\le B$. A problem $B$ is *NP-hard* if $A\le B$ for every $A\in\mathrm{NP}$, and *NP-complete* if moreover $B\in\mathrm{NP}$.

:::

Reductions are also how we usually *solve* problems: unweighted shortest paths reduce to weighted ones (weight $1$ everywhere), shortest paths with small positive integer weights reduce to unweighted ones (subdivide each edge), and longest paths in a DAG reduce to shortest paths (negate the weights).

::: {#prp-np-complete-consequences .proposition name="Why NP-completeness matters"}

1. If $A\le B$ and $B\in\mathrm P$, then $A\in\mathrm P$.
2. If some NP-complete problem is in $\mathrm P$, then $\mathrm P=\mathrm{NP}$.
3. If $A$ is NP-hard and $A\le B$, then $B$ is NP-hard.

:::

::: {.proof}

1. Convert an instance of $A$ in polynomial time; the new instance has polynomial size, so the algorithm for $B$ runs in polynomial time on it. A polynomial of a polynomial is a polynomial.

2. Every problem in $\mathrm{NP}$ reduces to the NP-complete problem, so it is in $\mathrm P$ by part 1.

3. For $X\in\mathrm{NP}$, $X\le A\le B$, and composing two polynomial reductions gives one.

:::

So all NP-complete problems are equally hard, and showing a problem NP-complete is strong evidence that it has no polynomial algorithm. The first NP-complete problem was *circuit satisfiability* (Cook–Levin); others follow by part 3.

::: {#rmk-complexity-classes-examples .remark name="NP-complete problems"}

NP-complete problems include subset sum (@exm-subset-sum), longest simple path, the decision version of the travelling salesman problem, $3$-colouring a graph (while $2$-colouring is in $\mathrm P$), finding a largest clique, satisfiability of Boolean formulas, the longest common subsequence of $n$ strings, and many puzzles (Sudoku, Minesweeper, Tetris). Subset sum is only *weakly* NP-complete: its pseudopolynomial algorithm (@def-pseudopolynomial) is polynomial when the numbers are small. *3-partition* (split $n$ integers into triples with equal sums) is *strongly* NP-complete: it has no pseudopolynomial algorithm unless $\mathrm P=\mathrm{NP}$. Reductions from it show that packing rectangles into a rectangle, and even jigsaw puzzles, are NP-complete.

:::
