---
title: "Models, Entailment and Satisfiability"
sources: [cs221-19]
requires: [math/discrete/logic/propositional/tautologies]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 19 (semantics of propositional logic: models, knowledge bases, entailment, contradiction, contingency, satisfiability, model checking), in our own wording. Syntax, connectives and tautologies are in the earlier notes of this branch and are not repeated; proofs written out in steps. -->

A logic has a *syntax* (which formulas are valid), a *semantics* (what they mean) and *inference rules* (how to derive formulas from others). This note gives the semantics of propositional logic in terms of models; @sec-math-discrete-logic-propositional-inference-rules treats inference rules.

::: {#def-propositional-model .definition name="Model, interpretation, models of a formula"}

A *model* $w$ is an assignment of a truth value to each propositional symbol; with $k$ symbols there are $2^k$ models. The *interpretation* $\mathcal I(f,w)\in\{T,F\}$ of a formula $f$ in a model $w$ is defined recursively: a symbol gets its value in $w$, and a compound formula gets the value given by the truth table of its main connective applied to the interpretations of its parts. The set of *models of $f$* is

$$
\mathcal M(f)=\{w:\mathcal I(f,w)=T\}.
$$

:::

A short formula can describe a large set of possible worlds: with symbols Rain and Wet, $\mathcal M(\text{Rain}\vee\text{Wet})$ has three of the four models.

::: {#def-knowledge-base .definition name="Knowledge base"}

A *knowledge base* KB is a set of formulas, the facts known so far. Its models are the models satisfying every formula in it, $\mathcal M(\text{KB})=\bigcap_{f\in\text{KB}}\mathcal M(f)$; semantically, KB is the conjunction of its formulas.

:::

Adding a formula can only shrink the set of models: $\mathcal M(\text{KB}\cup\{f\})\subseteq\mathcal M(\text{KB})$. Gaining knowledge narrows down the possible worlds.

::: {#def-entailment .definition name="Entailment, contradiction, contingency"}

Compare $\mathcal M(\text{KB}\cup\{f\})$ with $\mathcal M(\text{KB})$:

1. KB *entails* $f$, written $\text{KB}\models f$, if $\mathcal M(\text{KB}\cup\{f\})=\mathcal M(\text{KB})$, that is, $\mathcal M(\text{KB})\subseteq\mathcal M(f)$: $f$ adds no information;
2. KB *contradicts* $f$ if $\mathcal M(\text{KB}\cup\{f\})=\emptyset$: $f$ is incompatible with KB;
3. $f$ is *contingent* with respect to KB otherwise, when $\emptyset\ne\mathcal M(\text{KB}\cup\{f\})\subsetneq\mathcal M(\text{KB})$.

:::

::: {#fig-models-and-entailment-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}
\draw[regionA] (0,0) circle (0.6); \draw (0,0) circle (1.0);
\node[lab] at (0,0) {KB}; \node[lab] at (0.75,0.75) {$f$};
\node[lab] at (0,-1.4) {entailment};
\end{scope}
\begin{scope}[xshift=3.2cm]
\draw[regionA] (-0.45,0) circle (0.6); \draw (0.75,0) circle (0.5);
\node[lab] at (-0.45,0) {KB}; \node[lab] at (0.75,0) {$f$};
\node[lab] at (0.1,-1.4) {contradiction};
\end{scope}
\begin{scope}[xshift=6.4cm]
\draw[regionA] (-0.3,0) circle (0.6); \draw (0.35,0) circle (0.6);
\node[lab] at (-0.55,0) {KB}; \node[lab] at (0.6,0) {$f$};
\node[lab] at (0,-1.4) {contingency};
\end{scope}
\end{tikzpicture}
\end{center}
```

The sets $\mathcal M(\text{KB})$ (shaded) and $\mathcal M(f)$ among all models. Entailment: the first lies inside the second. Contradiction: they are disjoint. Contingency: they overlap only partly.

:::

These three cases give the answers of a knowledge-based system. Asked whether $f$ holds ($\text{Ask}[f]$), it answers *yes* (entailment), *no* (contradiction) or *I don't know* (contingency). Told $f$ ($\text{Tell}[f]$), it answers *I already knew that*, *I don't buy that*, or *I learned something new* and adds $f$. With a probability distribution on models, as in a Bayesian network (@sec-ai-bayesian-networks-bayesian-networks), the answer becomes the number $P(f\mid\text{KB})=\sum_{w\in\mathcal M(\text{KB}\cup\{f\})}P(w)\big/\sum_{w\in\mathcal M(\text{KB})}P(w)$; logic allows arbitrary formulas as evidence and query, not only assignments to variables.

::: {#def-satisfiable .definition name="Satisfiability, model checking"}

KB is *satisfiable* if $\mathcal M(\text{KB})\ne\emptyset$. *Model checking* is the task of deciding whether a KB is satisfiable (and, if it is, finding a model).

:::

::: {#prp-entailment-via-satisfiability .proposition name="Reducing entailment to satisfiability"}

1. KB contradicts $f$ if and only if $\text{KB}\cup\{f\}$ is unsatisfiable.
2. $\text{KB}\models f$ if and only if $\text{KB}\cup\{\neg f\}$ is unsatisfiable, that is, KB contradicts $\neg f$.

So two calls to a satisfiability checker decide which of the three cases holds.

:::

::: {.proof}

1. This is the definition of contradiction.

2. $\mathcal M(\neg f)$ is the complement of $\mathcal M(f)$. So $\mathcal M(\text{KB}\cup\{\neg f\})=\mathcal M(\text{KB})\setminus\mathcal M(f)$, which is empty exactly when $\mathcal M(\text{KB})\subseteq\mathcal M(f)$, that is, when $\text{KB}\models f$.

3. One satisfiability call gives one bit, and there are three outcomes: if $\text{KB}\cup\{f\}$ is unsatisfiable it is a contradiction; otherwise, if $\text{KB}\cup\{\neg f\}$ is unsatisfiable it is entailment; otherwise contingency.

:::

```{=latex}
\begin{algorithm}
\caption{Ask by model checking}
\begin{algorithmic}
\INPUT Knowledge base KB, formula $f$, a satisfiability checker $\textsc{Sat}$
\OUTPUT yes, no, or I don't know
\IF{not $\textsc{Sat}(\text{KB}\cup\{f\})$}
    \RETURN no \COMMENT{contradiction}
\ELSIF{not $\textsc{Sat}(\text{KB}\cup\{\neg f\})$}
    \RETURN yes \COMMENT{entailment}
\ELSE
    \RETURN I don't know \COMMENT{contingency}
\ENDIF
\end{algorithmic}
\end{algorithm}
```

The simplest checker enumerates all $2^k$ models. Practical SAT solvers search over partial assignments instead: the DPLL algorithm does exhaustive backtracking search with simplification, and conflict-driven clause learning (CDCL) adds learned clauses that prune the search; they decide large instances quickly in practice, although satisfiability is NP-complete in general.

::: {#exm-models-and-entailment-1 .example name="Rain and wet"}

Let $\text{KB}=\{\text{Rain}\vee\text{Snow},\ \text{Rain}\implies\text{Wet},\ \text{Snow}\implies\text{Wet}\}$. Of the $8$ models of Rain, Snow, Wet, those of KB have $\text{Wet}=T$ and at least one of Rain, Snow true: three models. $\text{KB}\cup\{\neg\text{Wet}\}$ is unsatisfiable, so $\text{KB}\models\text{Wet}$. Both $\text{KB}\cup\{\text{Rain}\}$ and $\text{KB}\cup\{\neg\text{Rain}\}$ are satisfiable, so Rain is contingent.

:::
