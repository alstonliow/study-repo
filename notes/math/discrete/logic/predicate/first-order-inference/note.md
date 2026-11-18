---
title: "Models and Inference in First-Order Logic"
sources: [cs221-20]
requires: [math/discrete/logic/predicate/logic-with-quantifiers, math/discrete/logic/propositional/inference-rules]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 20 (first-order models, propositionalization, definite clauses, substitution, unification, modus ponens), in our own wording. Terms, predicates and quantifiers are in the earlier notes of this branch (@def-term-recursive, @def-predicate, @def-universal-quantifier) and are not repeated; proofs written out in steps. -->

Propositional logic is clumsy for "all students know arithmetic" (one symbol per student) and cannot state "every even integer greater than $2$ is a sum of two primes" at all. First-order logic adds *terms* denoting objects (constants such as $\text{alice}$, variables, and functions such as $\text{father}(x)$), *predicates* applied to terms (atomic formulas such as $\text{Knows}(x,\text{arithmetic})$), and quantifiers over objects. Its semantics and inference extend those of @sec-math-discrete-logic-propositional-models-and-entailment and @sec-math-discrete-logic-propositional-inference-rules.

::: {#def-first-order-model .definition name="First-order model"}

A *model* $w$ of first-order logic consists of a non-empty *domain* $D$ of objects and an *interpretation* that maps each constant symbol to an object of $D$, each $k$-ary function symbol to a function $D^k\to D$, and each $k$-ary predicate symbol to a $k$-ary relation on $D$ (the tuples for which it is true). A term then denotes an object, computed recursively, and the truth value $\mathcal I(f,w)$ of a formula is defined recursively, with $\forall x.\,f$ true when $f$ is true for every object assigned to $x$, and $\exists x.\,f$ when it is true for some object.

:::

Assigning truth values directly to atomic formulas would not work: with functions there are infinitely many of them, and two different terms (such as $\text{bob}$ and $\text{father}(\text{alice})$) may denote the same object. The domain is the extra layer of indirection that handles both. Models of formulas and knowledge bases, entailment and satisfiability are then defined exactly as in propositional logic.

::: {#rmk-first-order-inference-1 .remark name="Propositionalization"}

Suppose every object is denoted by exactly one constant: at most one (*unique names*) and at least one (*domain closure*). Then a first-order knowledge base can be *propositionalized*: replace $\forall x.\,f$ by the conjunction of $f$ with $x$ replaced by each constant, $\exists x.\,f$ by the disjunction, and treat each ground atomic formula such as $\text{Student}(\text{alice})$ as a propositional symbol. In this regime first-order logic is only a compact notation for propositional logic, and model checking applies. Without these assumptions, inference must work with variables directly.

:::

::: {#def-first-order-definite-clause .definition name="First-order definite clause"}

A *definite clause* is a formula $\forall x_1\dots\forall x_n.\,(a_1\wedge\dots\wedge a_k)\implies b$, where $a_1,\dots,a_k,b$ are atomic formulas whose variables are among $x_1,\dots,x_n$. For example, $\forall x\,\forall y\,\forall z.\,(\text{Takes}(x,y)\wedge\text{Covers}(y,z))\implies\text{Knows}(x,z)$. A formula with a disjunction in the conclusion, or an existential quantifier, is not a definite clause.

:::

::: {#def-substitution-unification .definition name="Substitution, unifier"}

A *substitution* $\theta$ maps variables to terms; $\text{Subst}(\theta,f)$ replaces every occurrence of each variable $x$ in $f$ by $\theta(x)$. A *unifier* of two atomic formulas (or conjunctions) $f,g$ is a substitution with $\text{Subst}(\theta,f)=\text{Subst}(\theta,g)$. A *most general unifier* $\text{Unify}(f,g)$ is a unifier that commits to as little as possible: every other unifier is obtained from it by a further substitution.

:::

```{=latex}
\begin{algorithm}
\caption{Unification}
\begin{algorithmic}
\INPUT Terms or atomic formulas $s,t$, substitution $\theta$ (initially empty)
\OUTPUT A most general unifier extending $\theta$, or failure
\FUNCTION{Unify}{$s,t,\theta$}
    \STATE $s\gets\text{Subst}(\theta,s)$; $t\gets\text{Subst}(\theta,t)$
    \IF{$s=t$} \RETURN $\theta$ \ENDIF
    \IF{$s$ is a variable}
        \IF{$s$ occurs in $t$} \RETURN failure \ENDIF
        \RETURN $\theta$ with $s\mapsto t$ (and $s$ replaced by $t$ in the terms of $\theta$)
    \ENDIF
    \IF{$t$ is a variable} \RETURN $\textsc{Unify}(t,s,\theta)$ \ENDIF
    \IF{$s=F(s_1,\dots,s_k)$ and $t=F(t_1,\dots,t_k)$ with the same symbol $F$}
        \FOR{$i=1$ \TO $k$}
            \STATE $\theta\gets\textsc{Unify}(s_i,t_i,\theta)$; \textbf{if} failure \textbf{return} failure
        \ENDFOR
        \RETURN $\theta$
    \ENDIF
    \RETURN failure \COMMENT{different symbols, or a constant against a compound term}
\ENDFUNCTION
\end{algorithmic}
\end{algorithm}
```

::: {#exm-unification .example name="Unifiers"}

$\text{Unify}(\text{Knows}(\text{alice},\text{arithmetic}),\ \text{Knows}(x,\text{arithmetic}))=\{x\mapsto\text{alice}\}$. $\text{Unify}(\text{Knows}(\text{alice},y),\ \text{Knows}(x,z))=\{x\mapsto\text{alice},\ y\mapsto z\}$. $\text{Unify}(\text{Knows}(\text{alice},y),\ \text{Knows}(\text{bob},z))$ fails, since $\text{alice}\ne\text{bob}$. $\text{Unify}(\text{Knows}(\text{alice},y),\ \text{Knows}(x,\text{f}(x)))=\{x\mapsto\text{alice},\ y\mapsto\text{f}(\text{alice})\}$.

:::

::: {#def-first-order-modus-ponens .definition name="Modus ponens with unification"}

For atomic formulas $a_1',\dots,a_k'$ and a definite clause $\forall x_1\dots x_n.\,(a_1\wedge\dots\wedge a_k)\implies b$, if $\theta=\text{Unify}(a_1'\wedge\dots\wedge a_k',\ a_1\wedge\dots\wedge a_k)$ exists, then

$$
a_1',\ \dots,\ a_k',\ \ \forall x_1\dots x_n.\,(a_1\wedge\dots\wedge a_k)\implies b\ \ \vdash\ \ \text{Subst}(\theta,b).
$$

:::

::: {#exm-first-order-modus-ponens .example name="Who knows logic"}

From $\text{Takes}(\text{alice},\text{cs221})$, $\text{Covers}(\text{cs221},\text{logic})$ and the clause $\forall x,y,z.\,(\text{Takes}(x,y)\wedge\text{Covers}(y,z))\implies\text{Knows}(x,z)$, unification gives $\theta=\{x\mapsto\text{alice},\ y\mapsto\text{cs221},\ z\mapsto\text{logic}\}$ and modus ponens derives $\text{Knows}(\text{alice},\text{logic})$. Exact matching would fail, since $\text{Takes}(\text{alice},\text{cs221})$ is not literally $\text{Takes}(x,y)$.

:::

::: {#fig-first-order-inference-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.5cm,y=1.1cm]
\node[box] (a) at (0,0) {$\text{Takes}(\text{alice},\text{cs221})$};
\node[box] (b) at (1.5,0) {$\text{Covers}(\text{cs221},\text{logic})$};
\node[box] (c) at (0.75,-1) {$\forall x,y,z.\ \text{Takes}(x,y)\wedge\text{Covers}(y,z)\implies\text{Knows}(x,z)$};
\node[lab] at (0.75,-1.75) {$\theta=\{x\mapsto\text{alice},\ y\mapsto\text{cs221},\ z\mapsto\text{logic}\}$};
\node[hl box] (d) at (0.75,-2.5) {$\text{Knows}(\text{alice},\text{logic})$};
\draw[->] (a) -- (c); \draw[->] (b) -- (c); \draw[->] (c) -- (d);
\end{tikzpicture}
\end{center}
```

Modus ponens with unification in @exm-first-order-modus-ponens: the facts are unified with the premises of the clause, and the substitution is applied to its conclusion.

:::

Modus ponens with unification is sound, by the argument of @thm-modus-ponens-sound: $\text{Subst}(\theta,\cdot)$ only specializes a universally quantified clause. Like its propositional version it is not complete for arbitrary formulas (resolution with unification is). Each application produces an atomic formula. Without function symbols there are at most $c^a$ ground atomic formulas per predicate, for $c$ constants and maximum arity $a$, so forward inference terminates; with functions, terms such as $\text{succ}(\text{succ}(\cdots))$ can grow forever and forward inference may not terminate.

::: {#rmk-first-order-inference-2 .remark name="Writing sentences in first-order logic"}

A universal quantifier usually goes with an implication and an existential one with a conjunction. "All students know arithmetic" is $\forall x.\,\text{Student}(x)\implies\text{Knows}(x,\text{arithmetic})$; writing $\forall x.\,\text{Student}(x)\wedge\text{Knows}(x,\text{arithmetic})$ would say that every object is a student. "Some student knows arithmetic" is $\exists x.\,\text{Student}(x)\wedge\text{Knows}(x,\text{arithmetic})$; with $\implies$ it would be true as soon as some object is not a student. Some statements, such as "$70\%$ of students know machine learning", need more than first-order logic.

:::
