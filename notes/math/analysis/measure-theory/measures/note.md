---
title: "Measures and Uniqueness of Extension"
sources: [camii-pm-1]
requires: [math/analysis/measure-theory/sigma-algebras]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 1.1, in our own wording; proofs written out in steps. The continuity properties are our own addition, used throughout the branch. -->

::: {#def-set-function .definition name="Set functions"}

Let $\mathcal A$ be a collection of subsets of $E$ with $\emptyset\in\mathcal A$. A *set function* is a map $\mu:\mathcal A\to[0,\infty]$ with $\mu(\emptyset)=0$. It is

1. *increasing* if $\mu(A)\le\mu(B)$ whenever $A\subseteq B$ in $\mathcal A$;
2. *additive* if $\mu(A\cup B)=\mu(A)+\mu(B)$ whenever $A,B,A\cup B\in\mathcal A$ and $A\cap B=\emptyset$;
3. *countably additive* if $\mu\big(\bigcup_nA_n\big)=\sum_n\mu(A_n)$ whenever $A_1,A_2,\dots\in\mathcal A$ are pairwise disjoint and $\bigcup_nA_n\in\mathcal A$;
4. *countably subadditive* if $\mu\big(\bigcup_nA_n\big)\le\sum_n\mu(A_n)$ whenever $A_n\in\mathcal A$ and $\bigcup_nA_n\in\mathcal A$.

:::

::: {#def-measure .definition name="Measure, measure space"}

A *measure* on a measurable space $(E,\mathcal E)$ is a countably additive set function $\mu:\mathcal E\to[0,\infty]$. The triple $(E,\mathcal E,\mu)$ is a *measure space*. The measure is *finite* if $\mu(E)<\infty$, a *probability measure* if $\mu(E)=1$, and *σ-finite* if

$$
E=\bigcup_{n}E_n\quad\text{for some }E_n\in\mathcal E\text{ with }\mu(E_n)<\infty .
$$

:::

Counting measure ($\mu(A)=\#A$ on all subsets) and the point mass $\delta_x(A)=\mathbf 1_A(x)$ are measures. Counting measure on $\mathbb Z$ is σ-finite; on $\mathbb R$ it is not.

::: {#prp-measure-continuity .proposition name="Basic properties of measures"}

Let $(E,\mathcal E,\mu)$ be a measure space and $A,B,A_n\in\mathcal E$.

1. $\mu$ is additive and increasing, and $\mu(B\setminus A)=\mu(B)-\mu(A)$ if $A\subseteq B$ and $\mu(A)<\infty$.
2. $\mu$ is countably subadditive.
3. (Continuity from below) If $A_n\uparrow A$, then $\mu(A_n)\uparrow\mu(A)$.
4. (Continuity from above) If $A_n\downarrow A$ and $\mu(A_1)<\infty$, then $\mu(A_n)\downarrow\mu(A)$.

:::

::: {.proof}

1. Take $A_1=A$, $A_2=B$ and $A_n=\emptyset$ for $n\ge3$ in countable additivity to get additivity. If $A\subseteq B$, then $\mu(B)=\mu(A)+\mu(B\setminus A)\ge\mu(A)$, and subtracting the finite $\mu(A)$ gives the difference formula.

2. Put $B_1=A_1$ and $B_n=A_n\setminus(A_1\cup\dots\cup A_{n-1})$. The $B_n$ are disjoint, $B_n\subseteq A_n$ and $\bigcup B_n=\bigcup A_n$. So $\mu(\bigcup A_n)=\sum\mu(B_n)\le\sum\mu(A_n)$.

3. With $A_0=\emptyset$, the sets $A_n\setminus A_{n-1}$ are disjoint with union $A$, so $\mu(A)=\sum_{n\ge1}\mu(A_n\setminus A_{n-1})=\lim_N\sum_{n\le N}\mu(A_n\setminus A_{n-1})=\lim_N\mu(A_N)$.

4. The sets $A_1\setminus A_n$ increase to $A_1\setminus A$. By part 3 and the difference formula, $\mu(A_1)-\mu(A_n)\uparrow\mu(A_1)-\mu(A)$.

:::

::: {#fig-measures-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph] (0,0) ellipse (0.96 and 0.60);
\draw[emph] (0,0) ellipse (1.60 and 1.00);
\draw[emph] (0,0) ellipse (2.24 and 1.40);
\draw[hl] (0,0) ellipse (2.88 and 1.80);
\node[lab] at (0,0.1) {$A_1$};
\node[lab] at (1.2,0.1) {$A_2$};
\node[lab] at (1.85,0.1) {$A_3$};
\node[lab, text=accent] at (2.55,0.1) {$A$};
\node[lab, align=left, right] at (3.2,0) {$A_n\uparrow A$\\$\mu(A_n)\uparrow\mu(A)$};
\end{tikzpicture}
\end{center}
```

Continuity from below: along an increasing sequence of sets the measures increase to the measure of the union. The rings $A_n\setminus A_{n-1}$ are disjoint, so this is countable additivity in disguise.

:::

Continuity from above needs a finite set somewhere: for Lebesgue measure $[n,\infty)\downarrow\emptyset$ while every $[n,\infty)$ has infinite measure.

::: {#def-null-set-almost-everywhere .definition name="Null set, almost everywhere"}

A set $N\in\mathcal E$ with $\mu(N)=0$ is a *null set*. A property of points $x\in E$ holds *almost everywhere* (a.e.), or *almost surely* (a.s.) when $\mu$ is a probability measure, if the set of points where it fails is contained in a null set.

:::

## Uniqueness

::: {#thm-uniqueness-of-extension .theorem name="Uniqueness of extension"}

Let $\mu_1,\mu_2$ be measures on $(E,\mathcal E)$ with $\mu_1(E)=\mu_2(E)<\infty$. If they agree on a π-system $\mathcal A$ with $\sigma(\mathcal A)=\mathcal E$, then $\mu_1=\mu_2$.

:::

::: {.proof}

1. Let $\mathcal D=\{A\in\mathcal E:\ \mu_1(A)=\mu_2(A)\}$. It contains $\mathcal A$. By Dynkin's lemma (@lem-dynkin) it suffices to show that $\mathcal D$ is a d-system.

2. $E\in\mathcal D$ by hypothesis.

3. If $A\subseteq B$ are in $\mathcal D$, then $\mu_i(B\setminus A)=\mu_i(B)-\mu_i(A)$ for $i=1,2$ (all values are finite), and the right-hand sides agree; so $B\setminus A\in\mathcal D$.

4. If $A_n\uparrow A$ with $A_n\in\mathcal D$, then $\mu_1(A)=\lim\mu_1(A_n)=\lim\mu_2(A_n)=\mu_2(A)$ by continuity from below.

:::

::: {#exm-uniqueness-needs-finiteness .example name="Finiteness cannot be dropped"}

On $E=\mathbb Z$ with all subsets measurable, the sets $\{n,n+1,n+2,\dots\}$ ($n\in\mathbb Z$) together with $\emptyset$ form a π-system generating all subsets (each singleton is a difference of two of them). Counting measure $\mu$ and $2\mu$ agree on this π-system, both being $\infty$ on every non-empty member, yet they differ on $\{0\}$.

:::

::: {#cor-uniqueness-sigma-finite .corollary name="Uniqueness for σ-finite measures"}

Let $\mu_1,\mu_2$ agree on a π-system $\mathcal A$ generating $\mathcal E$, and suppose $E=\bigcup_nE_n$ with $E_n\in\mathcal A$ and $\mu_1(E_n)=\mu_2(E_n)<\infty$. Then $\mu_1=\mu_2$.

:::

::: {.proof}

1. Replace $E_n$ by $F_n=E_n\setminus(E_1\cup\dots\cup E_{n-1})$; it is enough that $\mu_1$ and $\mu_2$ agree on $A\cap F_n$ for each $n$ and each $A\in\mathcal E$, because then countable additivity gives $\mu_1(A)=\sum_n\mu_1(A\cap F_n)=\sum_n\mu_2(A\cap F_n)=\mu_2(A)$.

2. Fix $n$. The finite measures $\nu_i(A)=\mu_i(A\cap E_n)$ agree on $\mathcal A$, since $A\cap E_n\in\mathcal A$, and on $E$. By @thm-uniqueness-of-extension, $\nu_1=\nu_2$, so $\mu_1$ and $\mu_2$ agree on all measurable subsets of $E_n$.

3. Each $A\cap F_n$ is such a subset, which proves step 1.

:::
