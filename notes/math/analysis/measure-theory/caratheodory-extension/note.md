---
title: "Carathéodory's Extension Theorem"
sources: [camii-pm-1]
requires: [math/analysis/measure-theory/measures]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 1.1, in our own wording; the proof is written out in five steps. -->

Measures are rarely written down on a whole σ-algebra. One defines them on a ring of simple sets, where the formula is obvious, and extends. Carathéodory's theorem says the extension always exists, provided the set function is countably additive on the ring.

::: {#def-outer-measure .definition name="Outer measure, Carathéodory measurable set"}

Let $\mu$ be a set function on a ring $\mathcal A$ of subsets of $E$. For $B\subseteq E$ put

$$
\mu^*(B)=\inf\Big\{\sum_{n}\mu(A_n):\ A_n\in\mathcal A,\ B\subseteq\bigcup_nA_n\Big\},
$$

with $\inf\emptyset=\infty$. A set $A\subseteq E$ is *$\mu^*$-measurable* if

$$
\mu^*(B)=\mu^*(B\cap A)+\mu^*(B\cap A^c)\qquad\text{for all }B\subseteq E .
$$

:::

::: {#fig-caratheodory-extension-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[tintA] (0,0) rectangle (2.5,2.2);
\draw (0,0) rectangle (2.5,2.2);
\node[lab] at (0.35,1.95) {$A$};
\node[lab] at (4.4,1.95) {$A^c$};
\draw (-0.3,-0.3) rectangle (4.8,2.5);
\fill[overlapB] (2.5,1.1) ellipse (1.6 and 0.75);
\draw[hl] (2.5,1.1) ellipse (1.6 and 0.75);
\draw[faint] (2.5,0) -- (2.5,2.2);
\node[lab] at (1.75,1.1) {$B\cap A$};
\node[lab] at (3.35,1.1) {$B\cap A^c$};
\end{tikzpicture}
\end{center}
```

Carathéodory's criterion: $A$ is measurable when it cuts every test set $B$ into two pieces whose outer measures add up to $\mu^*(B)$.

:::

Clearly $\mu^*(\emptyset)=0$ and $\mu^*$ is increasing. Because $\mu^*$ will be shown to be subadditive, $A$ is $\mu^*$-measurable as soon as $\mu^*(B)\ge\mu^*(B\cap A)+\mu^*(B\cap A^c)$ for every $B$ with $\mu^*(B)<\infty$.

::: {#thm-caratheodory-extension .theorem name="Carathéodory's extension theorem"}

Let $\mathcal A$ be a ring on $E$ and $\mu$ a countably additive set function on $\mathcal A$. The $\mu^*$-measurable sets form a σ-algebra $\mathcal M\supseteq\sigma(\mathcal A)$, and $\mu^*$ restricted to $\mathcal M$ is a measure that agrees with $\mu$ on $\mathcal A$. In particular $\mu$ extends to a measure on $\sigma(\mathcal A)$.

:::

::: {.proof}

1. *$\mu^*$ is countably subadditive.* Let $B\subseteq\bigcup_nB_n$; we may assume every $\mu^*(B_n)$ is finite. Fix $\varepsilon>0$ and choose $A_{n,m}\in\mathcal A$ with $B_n\subseteq\bigcup_mA_{n,m}$ and $\sum_m\mu(A_{n,m})\le\mu^*(B_n)+\varepsilon2^{-n}$. The countable family $(A_{n,m})_{n,m}$ covers $B$, so
$$\mu^*(B)\le\sum_{n,m}\mu(A_{n,m})\le\sum_n\mu^*(B_n)+\varepsilon .$$
Let $\varepsilon\to0$.

2. *$\mu^*=\mu$ on $\mathcal A$.* For $A\in\mathcal A$, the cover $A,\emptyset,\emptyset,\dots$ gives $\mu^*(A)\le\mu(A)$. Conversely let $A\subseteq\bigcup_nA_n$ with $A_n\in\mathcal A$. The sets $C_n=A\cap A_n\setminus(A_1\cup\dots\cup A_{n-1})$ lie in the ring, are disjoint and have union $A$. Countable additivity and monotonicity of $\mu$ on the ring (additivity gives $\mu(C)\le\mu(D)$ for $C\subseteq D$ in $\mathcal A$) yield $\mu(A)=\sum_n\mu(C_n)\le\sum_n\mu(A_n)$. Take the infimum over covers.

3. *$\mathcal A\subseteq\mathcal M$.* Let $A\in\mathcal A$, $B\subseteq E$ with $\mu^*(B)<\infty$, and $\varepsilon>0$. Choose a cover $B\subseteq\bigcup_nA_n$ by ring sets with $\sum_n\mu(A_n)\le\mu^*(B)+\varepsilon$. The sets $A_n\cap A$ cover $B\cap A$ and $A_n\setminus A$ cover $B\cap A^c$, all in $\mathcal A$, and $\mu(A_n)=\mu(A_n\cap A)+\mu(A_n\setminus A)$. Hence
$$\mu^*(B\cap A)+\mu^*(B\cap A^c)\le\sum_n\mu(A_n\cap A)+\sum_n\mu(A_n\setminus A)=\sum_n\mu(A_n)\le\mu^*(B)+\varepsilon .$$

4. *$\mathcal M$ is an algebra.* It contains $\emptyset$, and the definition is symmetric in $A$ and $A^c$. Let $A_1,A_2\in\mathcal M$ and $B\subseteq E$. Using the definition for $A_1$, then for $A_2$ on the set $B\cap A_1^c$,
$$\mu^*(B)=\mu^*(B\cap A_1)+\mu^*(B\cap A_1^c\cap A_2)+\mu^*(B\cap A_1^c\cap A_2^c).$$
The first two sets have union $B\cap(A_1\cup A_2)$, so by subadditivity their sum is at least $\mu^*(B\cap(A_1\cup A_2))$, and the last set is $B\cap(A_1\cup A_2)^c$. With subadditivity in the other direction this shows $A_1\cup A_2\in\mathcal M$.

5. *$\mathcal M$ is a σ-algebra and $\mu^*$ is countably additive on it.* Let $A_1,A_2,\dots\in\mathcal M$ be disjoint (by step 4 any union can be written as a disjoint union of members of $\mathcal M$), $A=\bigcup_nA_n$ and $B\subseteq E$. Applying the definition for $A_n$ to the set $B\cap(A_1\cup\dots\cup A_n)$ and inducting,
$$\mu^*\big(B\cap(A_1\cup\dots\cup A_n)\big)=\sum_{k=1}^n\mu^*(B\cap A_k).$$
Since $A_1\cup\dots\cup A_n\in\mathcal M$ by step 4 and $\mu^*$ is increasing,
$$\mu^*(B)\ge\sum_{k=1}^n\mu^*(B\cap A_k)+\mu^*(B\cap A^c).$$
Let $n\to\infty$ and use subadditivity:
$$\mu^*(B)\ge\sum_{k}\mu^*(B\cap A_k)+\mu^*(B\cap A^c)\ge\mu^*(B\cap A)+\mu^*(B\cap A^c)\ge\mu^*(B).$$
So equality holds throughout: $A\in\mathcal M$, and taking $B=A$ gives $\mu^*(A)=\sum_k\mu^*(A_k)$.

6. By steps 3 and 5, $\mathcal M$ is a σ-algebra containing $\mathcal A$, hence $\sigma(\mathcal A)$; $\mu^*$ is a measure on it, and by step 2 it extends $\mu$.

:::

::: {#rmk-caratheodory-extension-1 .remark name="How large is the extension"}

1. $\mathcal M$ can be strictly larger than $\sigma(\mathcal A)$. For Lebesgue measure, $\mathcal M$ is the *completion* of the Borel σ-algebra: every set of the form $A\cup N$ with $A$ Borel and $N$ a subset of a Borel null set.

2. Every $\mu^*$-null set is $\mu^*$-measurable: if $\mu^*(N)=0$ then $\mu^*(B\cap N)+\mu^*(B\cap N^c)\le0+\mu^*(B)$. So the extension is automatically complete.

3. The extension to $\sigma(\mathcal A)$ is unique when $\mu$ is σ-finite on $\mathcal A$ (@cor-uniqueness-sigma-finite), since a ring is a π-system.

:::
