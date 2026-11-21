---
title: "Convergence Almost Everywhere and in Measure"
sources: [camii-pm-2]
requires: [math/analysis/measure-theory/measurable-functions]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 2.4 (first half), in our own wording; proofs written out in steps. On a probability space these are almost sure convergence and convergence in probability (math/probability/continuous/modes-of-convergence). -->

Let $(E,\mathcal E,\mu)$ be a measure space and $f_n,f:E\to\mathbb R$ measurable.

::: {#def-convergence-ae-in-measure .definition name="Convergence a.e. and in measure" generalizes="def-almost-sure-convergence def-convergence-in-probability"}

$f_n\to f$ *almost everywhere* if

$$
\mu\big(\{x\in E:\ f_n(x)\not\to f(x)\}\big)=0 .
$$

$f_n\to f$ *in measure* if for every $\varepsilon>0$

$$
\mu\big(\{x\in E:\ |f_n(x)-f(x)|>\varepsilon\}\big)\to0\qquad(n\to\infty).
$$

:::

The non-convergence set is measurable by @prp-measurable-closure. When $\mu$ is a probability measure these are @def-almost-sure-convergence and @def-convergence-in-probability.

::: {#thm-ae-and-in-measure .theorem name="A.e. convergence and convergence in measure"}

1. If $\mu(E)<\infty$ and $f_n\to f$ a.e., then $f_n\to f$ in measure.
2. If $f_n\to f$ in measure, then some subsequence $f_{n_k}\to f$ a.e.

:::

::: {.proof}

1. Fix $\varepsilon>0$ and let $A_n=\{|f_n-f|>\varepsilon\}$. If $x$ lies in infinitely many $A_n$, then $f_n(x)\not\to f(x)$; so $\mu(\limsup_nA_n)=0$.

2. The sets $B_m=\bigcup_{n\ge m}A_n$ decrease to $\limsup_nA_n$, and $\mu(B_1)\le\mu(E)<\infty$. By continuity from above (@prp-measure-continuity), $\mu(B_m)\to0$, and $\mu(A_m)\le\mu(B_m)$.

3. For part 2, choose $n_1<n_2<\cdots$ with $\mu\big(\{|f_{n_k}-f|>\tfrac1k\}\big)\le2^{-k}$, and let $C_k$ be that set.

4. $\sum_k\mu(C_k)<\infty$, so by the first Borel–Cantelli argument (@lem-borel-cantelli, which uses only countable subadditivity) the set $N=\limsup_kC_k$ is null: $\mu(N)\le\mu\big(\bigcup_{k\ge m}C_k\big)\le\sum_{k\ge m}2^{-k}\to0$.

5. For $x\notin N$ there is $K$ with $|f_{n_k}(x)-f(x)|\le\frac1k$ for all $k\ge K$, so $f_{n_k}(x)\to f(x)$.

:::

::: {#exm-convergence-in-measure-counterexamples .example name="The converses fail"}

1. *Part 1 needs $\mu(E)<\infty$.* On $\mathbb R$ with Lebesgue measure, $f_n=\mathbf 1_{[n,\infty)}\to0$ everywhere, but $\lambda(\{f_n>\tfrac12\})=\infty$ for all $n$.

2. *In measure does not give a.e.* On $[0,1]$ list the dyadic intervals $[j2^{-k},(j+1)2^{-k}]$, $0\le j<2^k$, $k=0,1,2,\dots$, in order as $I_1,I_2,\dots$ (the "typewriter" sequence) and put $f_n=\mathbf 1_{I_n}$. Then $\lambda(\{f_n>0\})=\lambda(I_n)\to0$, so $f_n\to0$ in measure, but every $x$ lies in infinitely many $I_n$ and outside infinitely many, so $f_n(x)$ converges for no $x$. The subsequence $\mathbf 1_{[0,2^{-k}]}$ does converge to $0$ a.e., as part 2 promises.

:::

::: {#fig-convergence-in-measure-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,-0.00) -- (4,-0.00);
\draw[hl] (0.00,-0.00) -- (4.00,-0.00);
\node[tick, left] at (-0.05,-0.00) {$f_{1}$};
\draw[faint] (0,-0.32) -- (4,-0.32);
\draw[hl] (0.00,-0.32) -- (2.00,-0.32);
\node[tick, left] at (-0.05,-0.32) {$f_{2}$};
\draw[faint] (0,-0.64) -- (4,-0.64);
\draw[emph] (2.00,-0.64) -- (4.00,-0.64);
\node[tick, left] at (-0.05,-0.64) {$f_{3}$};
\draw[faint] (0,-0.96) -- (4,-0.96);
\draw[hl] (0.00,-0.96) -- (1.00,-0.96);
\node[tick, left] at (-0.05,-0.96) {$f_{4}$};
\draw[faint] (0,-1.28) -- (4,-1.28);
\draw[emph] (1.00,-1.28) -- (2.00,-1.28);
\node[tick, left] at (-0.05,-1.28) {$f_{5}$};
\draw[faint] (0,-1.60) -- (4,-1.60);
\draw[emph] (2.00,-1.60) -- (3.00,-1.60);
\node[tick, left] at (-0.05,-1.60) {$f_{6}$};
\draw[faint] (0,-1.92) -- (4,-1.92);
\draw[emph] (3.00,-1.92) -- (4.00,-1.92);
\node[tick, left] at (-0.05,-1.92) {$f_{7}$};
\draw[faint] (0,-2.24) -- (4,-2.24);
\draw[hl] (0.00,-2.24) -- (0.50,-2.24);
\node[tick, left] at (-0.05,-2.24) {$f_{8}$};
\draw[faint] (0,-2.56) -- (4,-2.56);
\draw[emph] (0.50,-2.56) -- (1.00,-2.56);
\node[tick, left] at (-0.05,-2.56) {$f_{9}$};
\draw[faint] (0,-2.88) -- (4,-2.88);
\draw[emph] (1.00,-2.88) -- (1.50,-2.88);
\node[tick, left] at (-0.05,-2.88) {$f_{10}$};
\draw[faint] (0,-3.20) -- (4,-3.20);
\draw[emph] (1.50,-3.20) -- (2.00,-3.20);
\node[tick, left] at (-0.05,-3.20) {$f_{11}$};
\node[tick] at (0,0.3) {$0$}; \node[tick] at (4,0.3) {$1$};
\end{tikzpicture}
\end{center}
```

The typewriter sequence: indicators of dyadic intervals sweeping across $[0,1]$ at ever finer scales. The supports shrink, so $f_n\to0$ in measure, but every point is hit at every scale. The subsequence of intervals starting at $0$ (red) converges a.e.

:::

::: {#rmk-convergence-in-measure-1 .remark name="Relation to integrals"}

Neither mode controls integrals: $n\mathbf 1_{(0,1/n)}\to0$ everywhere and in measure on $[0,1]$, with all integrals equal to $1$. What is needed in addition is domination (@thm-dominated-convergence) or, on probability spaces, uniform integrability (@sec-math-probability-measure-theoretic-uniform-integrability).

:::
