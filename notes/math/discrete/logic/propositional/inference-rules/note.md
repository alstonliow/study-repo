---
title: "Inference Rules: Modus Ponens and Resolution"
sources: [cs221-19, cs221-20]
requires: [math/discrete/logic/propositional/models-and-entailment, math/discrete/logic/propositional/normal-forms]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 19 (inference rules, modus ponens, forward inference, derivation, soundness and completeness) and Lecture 20 (recap; "resolution is needed for completeness"), in our own wording. The completeness theorem for definite clauses, the resolution rule and its soundness proof are our own additions (the lecture names resolution without defining it); the completeness of resolution refutation is stated without proof. Proofs written out in steps. -->

Model checking works with truth assignments, the semantics. People reason instead by manipulating formulas: from "it is raining" and "if it is raining, it is wet" we conclude "it is wet" without listing possible worlds. Inference rules make this precise; they act on the syntax only.

::: {#def-inference-rule .definition name="Inference rule, modus ponens"}

An *inference rule* $f_1,\dots,f_n\vdash g$ says that from the *premises* $f_1,\dots,f_n$ one may derive the *conclusion* $g$, for formulas of the given shapes. *Modus ponens* is the rule

$$
p,\quad p\implies q\ \ \vdash\ \ q
$$

for all formulas $p,q$.

:::

::: {#def-derivation .definition name="Forward inference, derivation"}

Given a set of rules and a knowledge base KB, *forward inference* repeatedly picks formulas $f_1,\dots,f_n$ in KB that match the premises of a rule $f_1,\dots,f_n\vdash g$ and adds $g$ to KB, until nothing changes. KB *derives* (proves) $f$, written $\text{KB}\vdash f$, if $f$ is eventually added.

:::

```{=latex}
\begin{algorithm}
\caption{Forward inference}
\begin{algorithmic}
\INPUT Knowledge base KB, set of inference rules
\OUTPUT KB closed under the rules
\REPEAT
    \STATE changed $\gets$ false
    \FOR{each rule $f_1,\dots,f_n\vdash g$ with $f_1,\dots,f_n\in\text{KB}$ and $g\notin\text{KB}$}
        \STATE add $g$ to KB; changed $\gets$ true
    \ENDFOR
\UNTIL{not changed}
\RETURN KB
\end{algorithmic}
\end{algorithm}
```

::: {#exm-inference-rules-forward .example name="Forward inference with modus ponens"}

From $\text{KB}=\{\text{Rain},\ \text{Rain}\implies\text{Wet},\ \text{Wet}\implies\text{Slippery}\}$, modus ponens adds Wet and then Slippery, after which nothing changes. So $\text{KB}\vdash\text{Slippery}$. It cannot derive $\neg\text{Wet}$ (which is false in every model of KB) nor $\text{Rain}\implies\text{Slippery}$ (which is entailed, but is not of a shape modus ponens produces).

:::

::: {#fig-inference-rules-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.9cm,y=1cm]
\node[box] (r) at (0,0) {Rain};
\node[box] (rw) at (1,0) {$\text{Rain}\implies\text{Wet}$};
\node[hl box] (w) at (0.5,-1) {Wet};
\node[box] (ws) at (2.0,-1) {$\text{Wet}\implies\text{Slippery}$};
\node[hl box] (s) at (1.25,-2) {Slippery};
\draw[->] (r) -- (w); \draw[->] (rw) -- (w);
\draw[->] (w) -- (s); \draw[->] (ws) -- (s);
\end{tikzpicture}
\end{center}
```

The derivation of @exm-inference-rules-forward: each highlighted formula is added by modus ponens from the two formulas above it.

:::

Derivation ($\vdash$, syntax) and entailment ($\models$, semantics) are different notions. A good set of rules connects them.

::: {#def-soundness-completeness .definition name="Soundness, completeness"}

A set of inference rules is *sound* if $\text{KB}\vdash f$ implies $\text{KB}\models f$ for every KB and $f$: it derives nothing but the truth. It is *complete* if $\text{KB}\models f$ implies $\text{KB}\vdash f$: it derives the whole truth.

:::

::: {#thm-modus-ponens-sound .theorem name="Modus ponens is sound"}

If every rule $f_1,\dots,f_n\vdash g$ in a set satisfies $\{f_1,\dots,f_n\}\models g$, the set is sound. In particular modus ponens is sound.

:::

::: {.proof}

1. Let $f$ be added to KB at step $m$ of forward inference. We show $\mathcal M(\text{KB}_0)\subseteq\mathcal M(f)$ for the original $\text{KB}_0$, by induction on $m$; formulas of $\text{KB}_0$ satisfy this trivially.

2. If $f$ is added by a rule from premises $f_1,\dots,f_n$ already in KB, then by induction every model $w$ of $\text{KB}_0$ makes all $f_i$ true, and since $\{f_1,\dots,f_n\}\models f$, it makes $f$ true.

3. For modus ponens: in a model where $p$ and $p\implies q$ are true, $q$ is true by the truth table of $\implies$.

:::

Modus ponens is not complete. From $\text{KB}=\{\text{Rain},\ (\text{Rain}\vee\text{Snow})\implies\text{Wet}\}$ it derives nothing, since $\text{Rain}\vee\text{Snow}$ is not in KB, yet $\text{KB}\models\text{Wet}$. It is complete for a restricted kind of knowledge base.

::: {#def-definite-clause .definition name="Definite clause"}

A *definite clause* is a formula $(a_1\wedge\dots\wedge a_k)\implies b$ with propositional symbols $a_1,\dots,a_k,b$ ($k\ge0$; for $k=0$ it is the fact $b$). In conjunctive normal form (@def-cnf) it is a clause with exactly one positive literal, $\neg a_1\vee\dots\vee\neg a_k\vee b$. For definite clauses, modus ponens takes the general form $a_1,\dots,a_k,\ (a_1\wedge\dots\wedge a_k)\implies b\ \vdash\ b$.

:::

::: {#thm-modus-ponens-complete-definite .theorem name="Modus ponens is complete for definite clauses"}

If KB consists of definite clauses and $b$ is a propositional symbol with $\text{KB}\models b$, then forward inference with (general) modus ponens derives $b$.

:::

::: {.proof}

1. Run forward inference to the end and let $S$ be the set of symbols derived. Let $w$ be the model that makes the symbols in $S$ true and all others false.

2. $w$ is a model of KB. Take a clause $(a_1\wedge\dots\wedge a_k)\implies b'$. If some $a_i\notin S$, the premise is false in $w$ and the clause is true. If all $a_i\in S$, modus ponens applies, so $b'\in S$ (forward inference stopped only because nothing new could be added), and the clause is true.

3. Since $\text{KB}\models b$, $b$ is true in every model of KB, in particular in $w$, so $b\in S$: it was derived.

:::

Each step adds one symbol, so forward inference on definite clauses finishes after at most as many rounds as there are symbols. Full propositional logic needs a stronger rule.

::: {#def-resolution .definition name="Resolution"}

For clauses (disjunctions of literals) the *resolution* rule is

$$
\ell_1\vee\dots\vee\ell_m\vee p,\qquad \neg p\vee r_1\vee\dots\vee r_n\ \ \vdash\ \ \ell_1\vee\dots\vee\ell_m\vee r_1\vee\dots\vee r_n ,
$$

where $p$ is a symbol; the conclusion with no literals is the empty clause $\bot$ (false). *Resolution refutation* decides $\text{KB}\models f$ by converting $\text{KB}\cup\{\neg f\}$ to CNF and applying resolution until it derives $\bot$ (then $\text{KB}\models f$) or nothing new can be derived (then not).

:::

```{=latex}
\begin{algorithm}
\caption{Resolution refutation}
\begin{algorithmic}
\INPUT Knowledge base KB, formula $f$
\OUTPUT Whether $\text{KB}\models f$
\STATE $S\gets$ the clauses of the CNF of $\text{KB}\cup\{\neg f\}$
\REPEAT
    \FOR{each pair of clauses in $S$ containing a complementary pair $p$, $\neg p$}
        \STATE $c\gets$ their resolvent
        \IF{$c$ is the empty clause} \RETURN true \ENDIF
        \STATE add $c$ to $S$
    \ENDFOR
\UNTIL{no new clause was added}
\RETURN false
\end{algorithmic}
\end{algorithm}
```

::: {#prp-resolution-sound .proposition name="Resolution is sound"}

$\{\ell_1\vee\dots\vee\ell_m\vee p,\ \neg p\vee r_1\vee\dots\vee r_n\}\models\ell_1\vee\dots\vee\ell_m\vee r_1\vee\dots\vee r_n$.

:::

::: {.proof}

1. Let $w$ be a model of both premises. If $p$ is true in $w$, the second premise forces some $r_j$ to be true; if $p$ is false, the first forces some $\ell_i$ to be true.

2. Either way the conclusion is true in $w$.

:::

Resolution refutation is also complete: if $\text{KB}\models f$, then $\text{KB}\cup\{\neg f\}$ is unsatisfiable and resolution derives $\bot$ from its clauses. So it decides entailment in propositional logic, although it can take exponential time.

::: {#exm-inference-rules-resolution .example name="Where modus ponens failed"}

For $\text{KB}=\{\text{Rain},\ (\text{Rain}\vee\text{Snow})\implies\text{Wet}\}$ and $f=\text{Wet}$, the CNF of $\text{KB}\cup\{\neg\text{Wet}\}$ has the clauses $\text{Rain}$, $\neg\text{Rain}\vee\text{Wet}$, $\neg\text{Snow}\vee\text{Wet}$ and $\neg\text{Wet}$. Resolving $\text{Rain}$ with $\neg\text{Rain}\vee\text{Wet}$ gives $\text{Wet}$, and resolving that with $\neg\text{Wet}$ gives $\bot$. So $\text{KB}\models\text{Wet}$.

:::

::: {#fig-inference-rules-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.6cm,y=1cm]
\node[box] (a) at (0,0) {Rain};
\node[box] (b) at (1,0) {$\neg\text{Rain}\vee\text{Wet}$};
\node[box] (c) at (2,0) {$\neg\text{Snow}\vee\text{Wet}$};
\node[box] (d) at (2.9,0) {$\neg\text{Wet}$};
\node[hl box] (e) at (0.5,-1) {Wet};
\node[hl box] (f) at (1.7,-2) {$\bot$};
\draw[->] (a) -- (e); \draw[->] (b) -- (e);
\draw[->] (e) -- (f); \draw[->] (d) -- (f);
\end{tikzpicture}
\end{center}
```

Resolution refutation for @exm-inference-rules-resolution: the clause $\neg\text{Snow}\vee\text{Wet}$ is not needed.

:::
