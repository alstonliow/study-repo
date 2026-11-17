---
title: "Theorems, Proofs and Logical Deduction"
sources: [fit1058-cn-3.1, fit1058-cn-3.2, cs70-2.4]
requires: [math/discrete/sets/power-set]
status: draft
---

<!-- Migrated from 1058note notes/chapters/03-proofs.tex: Theorems and proofs; Logical deduction. -->

## Theorems and proofs

::: {#def-theorem .definition name="Theorem"}

A *theorem* is a mathematical statement that has been proved true.

:::

::: {#def-lemma-proposition-corollary .definition name="Lemma, proposition, corollary"}

A *lemma* is a theorem whose main purpose is as a stepping stone in the proof of a more significant theorem. A *proposition* is a theorem of independent interest, typically less significant or easier to prove than the main theorems around it. A *corollary* is a theorem that follows almost immediately from one just proved.

:::

::: {#def-proof .definition name="Proof"}

A *proof* of a claim is a finite sequence of statements (*steps*), ending in the claim, where each step is one of:

- something already known: a *definition*, an *axiom* (a fundamental assumed property, e.g. $x(y+z)=xy+xz$), or a previously proved theorem;

- an *assumption*, made as a starting point;

- a *logical consequence* of earlier steps.

The final step establishes the claim from what precedes it.

:::

::: {#rmk-theorems-and-proofs-1 .remark name="Verifiability"}

A proof must be readable sequentially – each step justified only by what comes *before* it, never by reading ahead. The end of a proof is marked by $\blacksquare$ (or historically “Q.E.D.”, *quod erat demonstrandum*).

:::

::: {#exm-theorems-and-proofs-1 .example}

For any sets $A, B$: if $A \subseteq B$ then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.

:::

::: {.proof}

Assume $A \subseteq B$. Let $X \in \mathcal{P}(A)$; then $X \subseteq A$ by definition of $\mathcal{P}(A)$. Since $A \subseteq B$, also $X \subseteq B$. Hence $X \in \mathcal{P}(B)$ by definition of $\mathcal{P}(B)$. So $X \in \mathcal{P}(A) \implies X \in \mathcal{P}(B)$, i.e. $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.

:::

::: {#rmk-theorems-and-proofs-2 .remark name="Annotating each step"}

- “Assume $A\subseteq B$” – an *assumption* (the theorem is conditional on it).

- “Let $X \in \mathcal{P}(A)$” – a *definition*, naming an arbitrary element so we can reason about it generically.

- “$X \subseteq A$” – a *logical consequence* of the previous line and the definition of $\mathcal{P}(A)$.

- “$X \subseteq B$” – a consequence of $X\subseteq A$ and the assumption $A \subseteq B$.

- “$X \in \mathcal{P}(B)$” – a consequence of $X \subseteq B$ and the definition of $\mathcal{P}(B)$.

- Final line – restates the whole chain as the subset relation $\mathcal{P}(A)\subseteq\mathcal{P}(B)$.

Every line either restates a definition/axiom, states an assumption, or follows logically from what came strictly before – exactly the requirement above.

:::

## Logical deduction

::: {#rmk-theorems-and-proofs-3 .remark name="Modus ponens"}

The core deduction rule: if $P$ has been established, and $P \implies Q$ has been established, then $Q$ may be deduced. This is used constantly and rarely named explicitly, but it is the essence of every logical deduction step in a proof.

:::

::: {#rmk-theorems-and-proofs-4 .remark name="Implication as a subset relation"}

In general, for statements $P,Q$, let $\hat P, \hat Q$ be the sets of situations in which $P$, resp. $Q$, holds. Then
$$P \implies Q \quad \text{corresponds to} \quad \hat P \subseteq \hat Q.$$
This generalizes the set-membership fact from @sec-math-discrete-sets-subsets: $A \subseteq B \iff \forall x\,(x\in A \implies x \in B)$ – the correspondence holds even when $P,Q$ are not phrased as membership statements at all (as the domino example shows).

:::

::: {#rmk-theorems-and-proofs-5 .remark name="Vacuous truth"}

If $X$ is false, $X \implies Y$ is true regardless of $Y$ – corresponding to $\emptyset \subseteq Y$ for any set $Y$ (@sec-math-discrete-sets-subsets, Theorem 1: the empty set is a subset of every set).

:::

::: {#def-converse .definition name="Converse"}

The *converse* of $P \implies Q$ is $Q \implies P$ (equivalently written $P \impliedby Q$). An implication holding does *not* entail its converse holds: implication is not symmetric, as both examples above show ($P\Rightarrow Q$ but not $Q \Rightarrow P$; $X \Rightarrow Y$ but not $Y \Rightarrow X$).

:::

::: {#def-biconditional .definition name="Biconditional"}

When both $P \implies Q$ and its converse $Q \implies P$ hold, we write $P \iff Q$ (“$P$ if and only if $Q$”; $P,Q$ are *logically equivalent*: $\hat P = \hat Q$ as sets of situations).

:::

::: {#def-contrapositive-and-inverse .definition name="Contrapositive and inverse"}

For $P \implies Q$: the *contrapositive* is $\neg Q \implies \neg P$; the *inverse* is $\neg P \implies \neg Q$.

:::

::: {#thm-theorems-and-proofs-1 .theorem}

$P \implies Q$ is logically equivalent to its contrapositive $\neg Q \implies \neg P$. It is *not*, in general, equivalent to its converse or its inverse (which are themselves contrapositives of each other).

:::

::: {.proof}

Both $P\Rightarrow Q$ and $\neg Q \Rightarrow \neg P$ are false in exactly one case ($P$ true, $Q$ false) and true otherwise – identical truth tables, hence logically equivalent. The converse $Q\Rightarrow P$ and inverse $\neg P \Rightarrow \neg Q$ each fail in the case $P$ false, $Q$ true (for the converse) or $P$ false, $Q$ true (checking directly) – a different failure case from the original, so neither need agree with $P \Rightarrow Q$ in general; the domino example ($P\Rightarrow Q$ true, $Q \Rightarrow P$ false) is a concrete witness.

:::

::: {#rmk-theorems-and-proofs-6 .remark name="Common logical fallacies"}

*Affirming the consequent*: from $P\implies Q$ and $Q$, wrongly concluding $P$ (this is the *converse* error from earlier in this section). *Denying the antecedent*: from $P\implies Q$ and $\neg P$, wrongly concluding $\neg Q$ (this is the *inverse* error). *Begging the question / circular reasoning*: using the claim being proved (or something equivalent to it) as a premise in its own proof.

:::

::: {#exm-affirming-the-consequent-in-the .example name="Affirming the consequent, in the wild"}

“If it rains, the ground is wet. The ground is wet. Therefore it rained.” Invalid: the ground could be wet from a sprinkler.

:::

## Proof by contraposition

::: {#rmk-theorems-and-proofs-contraposition .remark name="The pattern"}

To prove $P\implies Q$, assume $\neg Q$ and deduce $\neg P$. This proves the contrapositive $\neg Q\implies\neg P$, which is logically equivalent to $P\implies Q$ (@thm-theorems-and-proofs-1). It helps when $\neg Q$ gives something concrete to work with and $P$ does not. Say at the start that the proof is by contraposition.

:::

::: {#exm-divisor-of-odd-number .example name="Divisors of an odd number are odd"}

Claim: if $d\mid n$ and $n$ is odd, then $d$ is odd. Assuming "$n$ is odd" gives little to work with, so we prove the contrapositive: if $d$ is even, then $n$ is even. Write $d=2k$ and $n=d\,l$ for integers $k,l$. Then $n=2(kl)$ is even.

:::

::: {#thm-pigeonhole .theorem name="Pigeonhole principle"}

If $n$ objects are placed in $k$ boxes and $n>k$, then some box contains at least two objects.

:::

::: {.proof}

By contraposition. Suppose every box contains at most one object. Then the number of objects is at most the number of boxes, so $n\le k$.

:::

::: {#fig-theorems-and-proofs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \h in {0,...,3} {\draw[emph] (\h*1.3,1.6) -- (\h*1.3,0) -- (\h*1.3+1,0) -- (\h*1.3+1,1.6); \node[tick] at (\h*1.3+0.5,-0.35) {hole \the\numexpr\h+1\relax};}
\node[ball] at (0.5,0.4) {};
\node[hl ball] at (1.8,0.4) {}; \node[hl ball] at (1.8,1.1) {};
\node[ball] at (3.1,0.4) {};
\node[ball] at (4.4,0.4) {};
\end{tikzpicture}
\end{center}
```

Five objects in four boxes: some box holds at least two.

:::

::: {#exm-hairs-on-heads .example name="Two people with the same number of hairs"}

Nobody has more than $500\,000$ hairs on their head, but a city of more than $800\,000$ people has more people than possible hair counts $0,1,\dots,500\,000$. By @thm-pigeonhole, two residents have exactly the same number of hairs. The principle gives the conclusion without telling us who they are.

:::
