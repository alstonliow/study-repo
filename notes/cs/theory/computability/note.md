---
title: "Self-Reference and Computability"
sources: [cs70-12]
requires: [math/discrete/functions/cantor-diagonalization]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 12 (cs70-12), in our own wording; proofs written out in steps. -->

## Self-reference

::: {#rmk-computability-liar}

The sentence "This statement is false" is not a proposition (@sec-math-discrete-logic-propositional-propositions): if it is true, then what it says holds, so it is false; if it is false, then what it says fails, so it is true. The trouble comes from a statement that refers to itself. Russell's barber, who shaves exactly those men of the village who do not shave themselves, has the same shape: he shaves himself if and only if he does not. The same self-reference, applied to programs, limits what computers can do.

:::

Throughout, a *program* is a finite string over a fixed alphabet, run on an input string; on a given input it either *halts* (stops after finitely many steps) or *loops* (runs forever). Programs are data, so a program can take another program, or itself, as input. The precise model of computation (for example Turing machines) does not matter for the arguments below.

::: {#def-quine .definition name="Quine"}

A *quine* is a program that, run on empty input, prints its own text.

:::

::: {#thm-recursion-theorem .theorem name="Recursion theorem"}

For every program $P(x,y)$ there is a program $Q(x)$ such that, for every input $x$, $Q(x)$ behaves as $P(x,Q)$, where $Q$ stands for the text of $Q$.

:::

::: {#rmk-computability-recursion-theorem}

So a program may use its own text as if it had been given it as an input. Taking $P(x,y)$ = "print $y$" gives a quine, so quines exist in every general-purpose programming language. We state the theorem without proof; @exm-quine-construction shows the idea.

:::

## The halting problem

::: {#def-halting-problem .definition name="Halting problem, computable"}

A yes/no question about inputs is *computable* (decidable) if some program, on every input, halts with the correct answer. The *halting problem* asks, given a program $P$ and an input $x$, whether $P$ halts on $x$. A program solving it would be a program $\mathrm{TestHalt}$ that always halts, with
$$\mathrm{TestHalt}(P,x)=\begin{cases}\text{yes}&\text{if $P$ halts on $x$},\\ \text{no}&\text{if $P$ loops on $x$}.\end{cases}$$

:::

::: {#thm-halting-undecidable .theorem name="Turing, 1936"}

The halting problem is not computable: no program $\mathrm{TestHalt}$ as in @def-halting-problem exists.

:::

::: {.proof}

1. Suppose, for contradiction, that $\mathrm{TestHalt}$ exists. Use it to write the program $\mathrm{Turing}(P)$: if $\mathrm{TestHalt}(P,P)=\text{yes}$, loop forever; otherwise halt. So $\mathrm{Turing}$ halts on $P$ exactly when $P$ loops on $P$.

2. Run $\mathrm{Turing}$ on its own text. Suppose $\mathrm{Turing}(\mathrm{Turing})$ halts. Then $\mathrm{TestHalt}(\mathrm{Turing},\mathrm{Turing})$ answered no, which means $\mathrm{Turing}$ loops on $\mathrm{Turing}$. Contradiction.

3. Suppose $\mathrm{Turing}(\mathrm{Turing})$ loops. Then $\mathrm{TestHalt}(\mathrm{Turing},\mathrm{Turing})$ answered yes, which means $\mathrm{Turing}$ halts on $\mathrm{Turing}$. Contradiction.

4. Both cases are impossible, so $\mathrm{TestHalt}$ does not exist.

:::

::: {#rmk-computability-diagonal}

This is a diagonal argument, as in @thm-reals-uncountable. Programs are finite strings, so they can be listed $P_0,P_1,P_2,\dots$ (@prp-finite-strings-countable). Make a table whose entry $(i,j)$ records whether $P_i$ halts on $P_j$. $\mathrm{Turing}$ differs from each $P_n$ on the input $P_n$ (the diagonal entry), so it is not in the list; since the list contains every program, $\mathrm{Turing}$, and hence $\mathrm{TestHalt}$, cannot exist. Many other questions about programs are not computable either: whether a program ever prints anything (@exm-prints-something-undecidable), whether it ever reaches a given line, whether two programs give the same output.

:::

::: {#def-reduction .definition name="Reduction"}

A question $A$ *reduces* to a question $B$ if a program could answer $A$ using a program for $B$ as a subroutine. Then if $A$ is not computable, neither is $B$: a program for $B$ would give one for $A$.

:::

::: {#thm-easy-halting-undecidable .theorem name="The easy halting problem"}

No program decides, for every program $P$, whether $P$ halts on input $0$.

:::

::: {.proof}

1. Suppose, for contradiction, that a program $\mathrm{TestEasyHalt}$ does this.

2. Given $P$ and $x$, let $P'$ be the program that ignores its input $y$ and runs $P$ on $x$ (the texts of $P$ and $x$ are written into $P'$). Writing down $P'$ from $P$ and $x$ is a simple mechanical step.

3. $P'$ halts on $0$ if and only if $P$ halts on $x$.

4. So the program "build $P'$, then return $\mathrm{TestEasyHalt}(P')$" decides the halting problem, contradicting @thm-halting-undecidable. This reduces the halting problem to the easy halting problem (@def-reduction).

:::

## Gödel's incompleteness theorem

::: {#def-consistent-complete .definition name="Consistent, sound, complete"}

A *formal system* is a list of axioms with rules of inference; a *proof* is a finite string that follows the rules. A formal system is *consistent* if there is no proposition $S$ such that both $S$ and $\neg S$ have proofs; *sound* if every proposition that has a proof is true; and *complete* if for every proposition $S$ of its language, $S$ or $\neg S$ has a proof. A sound system is consistent, since $S$ and $\neg S$ are not both true.

:::

An inconsistent system is useless: if it proves both $S$ and $\neg S$, then for any $R$ it proves $S\lor R$ and hence, with $\neg S$, also $R$, so it proves every statement. Hilbert asked in 1900, and again in 1928, whether arithmetic is consistent and complete. Gödel showed in 1931 that it cannot be both. The halting problem gives a short proof of a slightly weaker form.

::: {#thm-goedel-incompleteness .theorem name="Incompleteness"}

No formal system that can express arithmetic, and whose proofs can be checked by a program, is both sound and complete.

:::

::: {.proof}

1. For a program $P$ and an input $x$, let $S_{P,x}$ be the statement "there is a number $z$ that encodes a halting run of $P$ on $x$". Checking that $z$ lists, step by step, the states of a computer running $P$ on $x$ until it stops is ordinary arithmetic, so $S_{P,x}$ can be written in the language of arithmetic. It is true exactly when $P$ halts on $x$.

2. Suppose, for contradiction, that the system is sound and complete. By completeness, for each $(P,x)$ there is a proof of $S_{P,x}$ or of $\neg S_{P,x}$.

3. Proofs are finite strings, so they can be listed one by one (@prp-finite-strings-countable). The program $\mathrm{Search}(P,x)$ runs through this list and checks each string: if it is a proof of $S_{P,x}$, output yes; if it is a proof of $\neg S_{P,x}$, output no. Checking a proof is possible by assumption.

4. By step 2, $\mathrm{Search}$ halts on every input. By soundness, the statement it found a proof of is true, so its answer is correct.

5. So $\mathrm{Search}$ decides the halting problem, contradicting @thm-halting-undecidable.

:::

::: {#rmk-computability-goedel}

Gödel's theorem is stronger: consistency is enough in place of soundness (in Rosser's form), and its proof is a topic for a logic course. Gödel's own argument builds, by encoding formulas as numbers, a statement $G$ that says "$G$ has no proof". If $G$ has a proof, the system proves a false statement; if not, $G$ is true but unprovable, so the system is incomplete. It is the liar's paradox with "false" replaced by "not provable".

:::
