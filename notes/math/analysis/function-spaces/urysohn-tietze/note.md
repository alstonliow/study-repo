---
title: "Normal Spaces, Urysohn's Lemma and the Tietze Extension Theorem"
sources: [camii-lan-3, camii-lans-3]
requires: [math/analysis/topology/compact-spaces]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part II Linear Analysis (lecture notes), Sections 3.1 and 3.2, and Example Sheet 3 (questions 1, 2), in our own wording; proofs written out in steps. -->

To study $C(K)$ for a compact Hausdorff space $K$ we need enough continuous functions. Normality gives them: closed sets can be separated by continuous functions and continuous functions on closed subsets can be extended.

::: {#def-normal-space .definition name="Normal space"}

A topological space $X$ in which points are closed is *normal* if any two disjoint closed sets $C_0,C_1$ have disjoint open neighbourhoods $U_0\supseteq C_0$, $U_1\supseteq C_1$.

:::

::: {#prp-compact-hausdorff-normal .proposition name="Metric and compact Hausdorff spaces are normal"}

Every metric space is normal. Every compact Hausdorff space is normal.

:::

::: {.proof}

1. *Metric.* For disjoint closed $C_0,C_1$ put $U_i=\{x:d(x,C_i)<d(x,C_{1-i})\}$. These are open (distance to a set is continuous), disjoint, and contain $C_0$ and $C_1$ respectively.

2. *Compact Hausdorff.* First, a point $p$ and a compact set $C\not\ni p$ in a Hausdorff space have disjoint neighbourhoods: for each $c\in C$ choose disjoint neighbourhoods $V_c\ni c$, $W_c\ni p$; finitely many $V_c$ cover $C$ and the intersection of the corresponding $W_c$ is a neighbourhood of $p$ disjoint from their union. For compact disjoint $C_0,C_1$: each $c\in C_1$ has disjoint neighbourhoods $V_c\supseteq C_0$ and $W_c\ni c$ (the first sentence applied with the roles of point and compact set exchanged, then once more). Finitely many $W_c$ cover $C_1$, and the intersection of the corresponding $V_c$ is a neighbourhood of $C_0$ disjoint from their union.

:::

::: {#lem-urysohn .lemma name="Urysohn's lemma"}

Let $X$ be normal and $C_0,C_1$ disjoint closed subsets. Then there is a continuous $f:X\to[0,1]$ with $f=0$ on $C_0$ and $f=1$ on $C_1$.

:::

::: {.proof}

1. *Reformulation of normality.* If $C$ is closed and $U\supseteq C$ open, there is an open $V$ with $C\subseteq V\subseteq\overline V\subseteq U$ (apply normality to $C$ and $X\setminus U$).

2. *Construction.* Let $Q$ be the dyadic rationals in $[0,1]$. We construct open sets $U_q$ ($q\in Q$) with $C_0\subseteq U_0$, $U_1=X\setminus C_1$, and $\overline{U_q}\subseteq U_r$ whenever $q<r$. First $U_1=X\setminus C_1$ and, by step 1, an open $U_0$ with $C_0\subseteq U_0\subseteq\overline{U_0}\subseteq U_1$. If $U_q$ is defined for all $q$ with denominator $2^n$, take consecutive such $q<s$ and $r=(q+s)/2$; by step 1 applied to $\overline{U_q}\subseteq U_s$ there is an open $U_r$ with $\overline{U_q}\subseteq U_r\subseteq\overline{U_r}\subseteq U_s$.

3. *Definition.* Put $f(x)=\inf\{q\in Q:x\in U_q\}$, with $f(x)=1$ if $x$ lies in no $U_q$. Then $0\le f\le1$, $f=0$ on $C_0\subseteq U_0$, and $f=1$ on $C_1$, since $U_q\subseteq U_1=X\setminus C_1$ for all $q$.

4. *Continuity.* If $x\in\overline{U_q}$ then $x\in U_r$ for all $r>q$, so $f(x)\le q$. If $x\notin U_q$ then $f(x)\ge q$. So $f(x)<a$ iff $x\in U_q$ for some dyadic $q<a$: $\{f<a\}=\bigcup_{q<a}U_q$ is open. And $\{f>a\}=\bigcup_{q>a}X\setminus\overline{U_q}$ is open. Sub-basic sets $\{f<a\}$, $\{f>a\}$ are open, so $f$ is continuous.

:::

::: {#fig-urysohn-tietze-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) ellipse (3.2 and 1.8);
\draw[faint] (-0.6,0) ellipse (2.2 and 1.3); \node[lab] at (1.9,0.9) {$U_{3/4}$};
\draw[faint] (-0.9,0) ellipse (1.5 and 0.95); \node[lab] at (0.3,0.8) {$U_{1/2}$};
\draw[faint] (-1.2,0) ellipse (0.9 and 0.6); \node[lab] at (-0.5,0.5) {$U_{1/4}$};
\draw[regionA] (-1.4,0) circle (0.3); \node[lab] at (-1.4,0) {$C_0$};
\draw[hl] (2.7,-0.3) circle (0.25); \node[lab, right] at (3.0,-0.3) {$C_1$};
\end{tikzpicture}
\end{center}
```

Urysohn's lemma: nested open sets $U_q$ between $C_0$ and the complement of $C_1$; $f(x)$ is the least $q$ with $x\in U_q$.

:::

::: {#thm-tietze .theorem name="Tietze–Urysohn extension theorem"}

Let $X$ be normal, $L\subseteq X$ closed and $g:L\to\mathbb R$ continuous. Then $g$ extends to a continuous $f:X\to\mathbb R$. If $|g|\le M$ on $L$ then $f$ can be chosen with $|f|\le M$. The same holds for complex-valued $g$ (extend real and imaginary parts, then normalise if bounded).

:::

::: {.proof}

1. *Bounded case, one step.* Let $|g|\le M$ on $L$. The sets $A=\{g\le-M/3\}$ and $B=\{g\ge M/3\}$ are disjoint and closed in $L$, hence in $X$. By @lem-urysohn there is continuous $h:X\to[-M/3,M/3]$ with $h=-M/3$ on $A$ and $h=M/3$ on $B$. Then $|g-h|\le2M/3$ on $L$.

2. *Iteration.* Apply step 1 to $g_1=g-h_1$ (bound $\frac23M$) to get $h_2$ with $|h_2|\le\frac13\cdot\frac23M$ and $|g_1-h_2|\le(\frac23)^2M$ on $L$, and so on. We obtain continuous $h_n$ on $X$ with $|h_n|\le\frac13(\frac23)^{n-1}M$ and $|g-(h_1+\dots+h_n)|\le(\frac23)^nM$ on $L$.

3. The series $f=\sum h_n$ converges uniformly (M-test), so $f$ is continuous, $f=g$ on $L$ and $|f|\le\frac M3\sum(\frac23)^{n-1}=M$.

4. *Unbounded case.* Replace $g$ by $\arctan\circ g$, extend to $\tilde f$ with $|\tilde f|\le\pi/2$ by the bounded case. The closed set $\{|\tilde f|=\pi/2\}$ is disjoint from $L$; Urysohn gives continuous $\phi:X\to[0,1]$ with $\phi=1$ on $L$ and $\phi=0$ on that set. Then $f=\tan(\phi\tilde f)$ is continuous, finite, and equals $g$ on $L$.

:::

::: {#cor-closed-g-delta-zero-set .corollary name="Zero sets in normal spaces"}

In a normal space $X$, a set $S$ is the zero set $f^{-1}(0)$ of a continuous $f:X\to\mathbb R$ if and only if $S$ is closed and a countable intersection of open sets ($G_\delta$).

:::

::: {.proof}

1. $f^{-1}(0)=\bigcap_n\{|f|<1/n\}$ is a closed $G_\delta$.

2. Conversely let $S=\bigcap U_n$ closed with $U_n$ open. Apply Urysohn to $S$ and $X\setminus U_n$ to get continuous $f_n:X\to[0,1]$ with $f_n=0$ on $S$, $f_n=1$ off $U_n$. Then $f=\sum2^{-n}f_n$ is continuous (M-test), vanishes on $S$, and is positive off $S$: if $x\notin S$ then $x\notin U_n$ for some $n$ and $f_n(x)=1$.

:::
