---
title: "Decidability of Logical Theories"
sources: [mit18404j-11]
requires: [cs/theory/recursion-theorem, math/discrete/logic/predicate/multiple-quantifiers]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 11 (the short introduction to logic), in our own wording; proofs written out in steps. Gödel's theorem in program form is @thm-goedel-incompleteness. -->

Can a machine decide which mathematical statements are true? For statements about the natural numbers with addition alone, yes; once multiplication is allowed, no.

::: {#def-theory-of-model .definition name="Theory of a model"}

A *model* $\mathcal M=(U,R_1,\dots,R_k)$ is a universe $U$ with relations $R_i$ on it. Formulas are built from the relation symbols applied to variables, the connectives $\wedge,\vee,\neg$ and the quantifiers $\exists,\forall$ over $U$; a *sentence* is a formula with no free variables, and is true or false in $\mathcal M$. The *theory* of $\mathcal M$ is

$$
\mathrm{Th}(\mathcal M)=\{\langle\phi\rangle: \phi \text{ is a sentence true in } \mathcal M\}.
$$

:::

For example, with $+$ as the ternary relation $\{(a,b,c): a+b=c\}$, the sentence $\forall x\,\exists y\,(y+y=x\vee \exists z\,(z{=}1\wedge y+y+z=x))$ (every number is even or odd, with $1$ expressible) lies in $\mathrm{Th}(\mathbb N,+)$.

::: {#thm-presburger-decidable .theorem name="Presburger arithmetic is decidable"}

$\mathrm{Th}(\mathbb N,+)$ is decidable.

:::

::: {.proof}

1. Put the sentence in prenex form $\phi=Q_1x_1\cdots Q_lx_l\,\psi$ with $\psi$ quantifier-free. For $i=0,\dots,l$ let $\phi_i=Q_{i+1}x_{i+1}\cdots Q_lx_l\,\psi$, a formula with free variables $x_1,\dots,x_i$; so $\phi_0=\phi$ and $\phi_l=\psi$.

2. Encode a tuple $(a_1,\dots,a_i)$ of numbers as a string over the alphabet $\Sigma_i=\{0,1\}^i$: write each $a_j$ in binary, padded to equal length, and read the columns from the least significant bit. We build DFAs $A_i$ that accept exactly the encodings of tuples making $\phi_i$ true.

3. *Base.* $A_l$ checks the atomic formulas $x_p+x_q=x_r$ by carrying a bit of carry in its state, as in @fig-logical-theories-1, and combines them with the closure constructions for $\wedge,\vee,\neg$ (@thm-regular-closed-union, @prp-regular-complement-intersection).

4. *Existential step.* Given $A_{i+1}$, the NFA $A_i$ guesses the extra column entry for $x_{i+1}$ at each step and runs $A_{i+1}$; leading zero columns are handled by letting $A_i$ also accept when $A_{i+1}$ can reach an accept state on further columns $(0,\dots,0,b)$. Convert to a DFA (@thm-nfa-dfa-equivalence).

5. *Universal step.* Use $\forall x\,\theta\equiv\neg\exists x\,\neg\theta$ and complement DFAs.

6. $A_0$ has alphabet $\{0,1\}^0=\{\varepsilon\}$; $\phi$ is true iff $A_0$ accepts the empty string, which is checked directly.

:::

::: {#fig-logical-theories-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[accept state] (0) at (0,0) {$c_0$};
\node[state] (1) at (4,0) {$c_1$};
\draw[start] (0.west) -- ++(-0.6,0);
\draw (0) edge[trans, loop above] node[edge label] {000, 011, 101} (0);
\draw (0) edge[trans, bend left=20] node[edge label] {110} (1);
\draw (1) edge[trans, bend left=20] node[edge label] {001} (0);
\draw (1) edge[trans, loop above] node[edge label] {010, 100, 111} (1);
\end{tikzpicture}
\end{center}
```

The DFA for $x+y=z$ in the proof of @thm-presburger-decidable, reading columns $x_iy_iz_i$ from the least significant bit; the state is the carry. Missing transitions go to a rejecting dead state. For $3+1=4$ the columns are $110,\ 100,\ 001$ and the run is $c_0,c_1,c_1,c_0$.

:::

::: {#thm-arithmetic-undecidable .theorem name="Arithmetic is undecidable"}

$\mathrm{Th}(\mathbb N,+,\times)$ is undecidable.

:::

::: {.proof}

1. Reduce $A_{\mathsf{TM}}$ to it. Given $\langle M,w\rangle$, construct a formula $\phi_{M,w}(x)$ in $+$ and $\times$ which says that the number $x$ encodes an accepting computation history of $M$ on $w$ (@def-computation-history).

2. This is possible because the conditions on a history are local: "the $j$-th digit of $x$ in base $b$ is $d$" can be expressed with $+$, $\times$ and quantifiers, and so can "the start configuration is $q_0w$", "consecutive configurations follow by the rules of $M$" and "the last configuration is accepting".

3. Then $M$ accepts $w$ iff the sentence $\exists x\,\phi_{M,w}(x)$ is true. A decider for $\mathrm{Th}(\mathbb N,+,\times)$ would decide $A_{\mathsf{TM}}$.

:::

::: {#cor-goedel-tm .corollary name="Incompleteness" related="thm-goedel-incompleteness"}

For any sound proof system for arithmetic in which proofs can be checked by a machine, some true sentence of $\mathrm{Th}(\mathbb N,+,\times)$ has no proof.

:::

::: {.proof}

1. The provable sentences are Turing-recognizable: enumerate all candidate proofs and check each.

2. If every true sentence were provable, then for each sentence $\phi$ exactly one of $\phi$ and $\neg\phi$ is true and hence provable. Searching for a proof of either would decide $\mathrm{Th}(\mathbb N,+,\times)$, contradicting @thm-arithmetic-undecidable.

:::

::: {#rmk-logical-theories-1}

With the recursion theorem one can exhibit the unprovable sentence: a TM $S$ that obtains its own description and searches for a proof of the sentence $\psi$ = "$S$ does not accept $0$", accepting if it finds one. If $\psi$ had a proof, $S$ would accept $0$, making $\psi$ false, impossible in a sound system; so $\psi$ has no proof and $S$ never accepts, which makes $\psi$ true.

:::
