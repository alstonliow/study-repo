---
title: "The Chinese Remainder Theorem"
sources: [cs70-6.6]
requires: [math/discrete/number-theory/modular-arithmetic]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 6 §6 (cs70-6.6), in our own wording; proofs written out in steps. -->

::: {#thm-crt-two .theorem name="Chinese Remainder Theorem, two moduli"}

Let $m,n\ge1$ with $\gcd(m,n)=1$. For all integers $a,b$ there is exactly one $x\in\{0,1,\dots,mn-1\}$ with
$$x\equiv a\pmod n\qquad\text{and}\qquad x\equiv b\pmod m.$$

:::

::: {.proof}

1. Since $\gcd(m,n)=1$, $m$ has an inverse $m^{-1}$ modulo $n$, and $n$ has an inverse $n^{-1}$ modulo $m$ (@thm-inverse).

2. Let $u=m\cdot(m^{-1}\bmod n)$ and $v=n\cdot(n^{-1}\bmod m)$. Then $u\equiv1\pmod n$ and $u\equiv0\pmod m$, while $v\equiv0\pmod n$ and $v\equiv1\pmod m$.

3. **Existence.** Let $x=(au+bv)\bmod mn$. Modulo $n$, $x\equiv a\cdot1+b\cdot0=a$; modulo $m$, $x\equiv a\cdot0+b\cdot1=b$.

4. **Uniqueness.** If $x$ and $y$ in $\{0,\dots,mn-1\}$ are both solutions, then $n\mid x-y$ and $m\mid x-y$, so $mn\mid x-y$ (@prp-coprimedivides). But $|x-y|<mn$, so $x-y=0$.

:::

::: {#fig-chinese-remainder-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=0.65cm]
\draw[cell frame] (0,0) rectangle ++(1,1); \node[lab] at (0+0.5,0+0.5) {0};
\draw[cell frame] (1,0) rectangle ++(1,1); \node[lab] at (1+0.5,0+0.5) {6};
\draw[cell frame] (2,0) rectangle ++(1,1); \node[lab] at (2+0.5,0+0.5) {12};
\draw[cell frame] (3,0) rectangle ++(1,1); \node[lab] at (3+0.5,0+0.5) {3};
\draw[cell frame] (4,0) rectangle ++(1,1); \node[lab] at (4+0.5,0+0.5) {9};
\draw[cell frame] (0,-1) rectangle ++(1,1); \node[lab] at (0+0.5,-1+0.5) {10};
\draw[cell frame] (1,-1) rectangle ++(1,1); \node[lab] at (1+0.5,-1+0.5) {1};
\draw[cell frame] (2,-1) rectangle ++(1,1); \node[lab] at (2+0.5,-1+0.5) {7};
\draw[cell frame] (3,-1) rectangle ++(1,1); \node[lab] at (3+0.5,-1+0.5) {13};
\draw[cell frame] (4,-1) rectangle ++(1,1); \node[lab] at (4+0.5,-1+0.5) {4};
\draw[cell frame] (0,-2) rectangle ++(1,1); \node[lab] at (0+0.5,-2+0.5) {5};
\draw[cell frame] (1,-2) rectangle ++(1,1); \node[lab] at (1+0.5,-2+0.5) {11};
\draw[cell frame] (2,-2) rectangle ++(1,1); \node[lab] at (2+0.5,-2+0.5) {2};
\draw[cell frame] (3,-2) rectangle ++(1,1); \node[lab] at (3+0.5,-2+0.5) {8};
\draw[cell frame] (4,-2) rectangle ++(1,1); \node[lab] at (4+0.5,-2+0.5) {14};
\foreach \b in {0,...,4} \node[lab] at (\b+0.5,1.4) {$\b$};
\foreach \a in {0,1,2} \node[lab] at (-0.5,-\a+0.5) {$\a$};
\node[lab] at (2.5,2.1) {$b=x\bmod5$};
\node[lab, anchor=east] at (-0.9,-0.5) {$a=x\bmod3$};
\end{tikzpicture}
\end{center}
```

With $n=3$ and $m=5$: each $x\in\{0,\dots,14\}$ sits in row $x\bmod3$ and column $x\bmod5$, and every cell holds exactly one $x$.

:::

::: {#thm-crt .theorem name="Chinese Remainder Theorem"}

Let $n_1,\dots,n_k\ge1$ be pairwise coprime and $N=n_1n_2\cdots n_k$. For all integers $a_1,\dots,a_k$ there is exactly one $x\in\{0,\dots,N-1\}$ with $x\equiv a_i\pmod{n_i}$ for every $i$. It is
$$x=\Bigl(\sum_{i=1}^{k}a_ib_i\Bigr)\bmod N,\qquad b_i=\frac N{n_i}\Bigl(\Bigl(\frac N{n_i}\Bigr)^{-1}\bmod n_i\Bigr).$$

:::

::: {.proof}

1. $\frac N{n_i}$ is a product of moduli coprime to $n_i$, so it is coprime to $n_i$ and has an inverse modulo $n_i$; hence $b_i$ is defined.

2. $b_i\equiv1\pmod{n_i}$, and $b_i\equiv0\pmod{n_j}$ for $j\ne i$, because $n_j$ divides $\frac N{n_i}$.

3. So modulo $n_j$, every term of $\sum_ia_ib_i$ vanishes except $a_jb_j\equiv a_j$: $x$ is a solution.

4. If $x$ and $y$ are solutions in $\{0,\dots,N-1\}$, every $n_i$ divides $x-y$. Applying @prp-coprimedivides repeatedly, $N\mid x-y$, and as before $x=y$.

:::

::: {#rmk-crt-vector-view .remark name="Arithmetic in pieces"}

The theorem gives a bijection between $\{0,\dots,mn-1\}$ and pairs $(x\bmod n,\ x\bmod m)$, and it respects arithmetic: the pair of $x+y$ is the sum of the pairs, and likewise for products (@thm-congarith). So working modulo $mn$ is the same as working modulo $n$ and modulo $m$ side by side. The numbers $b_i$ behave like basis vectors: $b_i$ is the number whose pair has $1$ in place $i$ and $0$ elsewhere.

:::
