---
title: "Savitch's Theorem and PSPACE-Completeness"
sources: [mit18404j-18]
requires: [cs/theory/space-complexity]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 18, in our own wording; proofs written out in steps. -->

## Savitch's theorem

::: {#thm-savitch .theorem name="Savitch"}

For $s(n)\ge n$, $\mathrm{NSPACE}(s(n))\subseteq\mathrm{SPACE}(s(n)^2)$. In particular $\mathrm{PSPACE}=\mathrm{NPSPACE}$.

:::

::: {.proof}

1. Let $N$ decide $A$ in space $s(n)$; we may assume it has a single accepting configuration $c_{\text{acc}}$ (it erases its tape before accepting). Its configurations on $w$ have length $O(s(n))$ and there are at most $2^{ds(n)}$ of them, for a constant $d$.

2. Define $\mathrm{CANYIELD}(c_1,c_2,t)$, which decides whether $N$ can go from configuration $c_1$ to $c_2$ in at most $t$ steps ($t$ a power of 2):
    a. if $t=1$, check directly whether $c_1=c_2$ or $c_1$ yields $c_2$ in one step;
    b. if $t>1$, for each configuration $c_m$ of length $s(n)$, test $\mathrm{CANYIELD}(c_1,c_m,t/2)$ and $\mathrm{CANYIELD}(c_m,c_2,t/2)$; accept if both hold for some $c_m$, and reject otherwise.

3. Accept $w$ iff $\mathrm{CANYIELD}(c_{\text{start}},c_{\text{acc}},2^{ds(n)})$.

4. *Correctness.* A computation of at most $t$ steps has a middle configuration $c_m$ splitting it into two halves of at most $t/2$ steps; the procedure tries every candidate.

5. *Space.* The two recursive calls run one after the other and reuse the same space. Each level of recursion stores $c_1,c_2,c_m$ and $t$, which is $O(s(n))$, and the depth is $\log_2 2^{ds(n)}=O(s(n))$. The total is $O(s(n)^2)$.

:::

```{=latex}
\begin{algorithm}
\caption{$\mathrm{CANYIELD}(c_1,c_2,t)$}
\begin{algorithmic}
\INPUT configurations $c_1,c_2$ of $N$ on $w$, a power of two $t$
\IF{$t=1$}
    \RETURN whether $c_1=c_2$ or $c_1$ yields $c_2$ in one step
\ENDIF
\FOR{each configuration $c_m$ of length $s(n)$}
    \IF{$\mathrm{CANYIELD}(c_1,c_m,t/2)$ and $\mathrm{CANYIELD}(c_m,c_2,t/2)$}
        \RETURN true
    \ENDIF
\ENDFOR
\RETURN false
\end{algorithmic}
\end{algorithm}
```

The midpoint search is the space-efficient analogue of repeated squaring. Note that the time is exponential: space is saved by recomputing.

::: {#fig-savitch-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[gridline] (0,0) -- (8,0);
\foreach \x/\l in {0/c_1,4/c_m,8/c_2} {\fill (\x,0) circle (2.4pt); \node[lab] at (\x,-0.4) {$\l$};}
\foreach \x/\l in {2/{c_m'},6/{c_m''}} {\fill[draw=none] (\x,0) circle (1.8pt); \node[lab, note] at (\x,-0.4) {$\l$};}
\draw[hl] (0,0.35) to[bend left=25] node[lab, note, above] {$t/2$} (4,0.35);
\draw[hl] (4,0.35) to[bend left=25] node[lab, note, above] {$t/2$} (8,0.35);
\draw[faint] (0,0.15) to[bend left=30] node[lab, tick, above] {$t/4$} (2,0.15);
\draw[faint] (2,0.15) to[bend left=30] node[lab, tick, above] {$t/4$} (4,0.15);
\draw[faint] (4,0.15) to[bend left=30] node[lab, tick, above] {$t/4$} (6,0.15);
\draw[faint] (6,0.15) to[bend left=30] node[lab, tick, above] {$t/4$} (8,0.15);
\node[lab, note] at (4,-1.1) {depth $\log_2 t$, each level stores $O(s(n))$};
\end{tikzpicture}
\end{center}
```

The recursion of @thm-savitch: to go from $c_1$ to $c_2$ in $t$ steps, guess a midpoint $c_m$ and solve two problems of half the length, one after the other in the same space.

:::

## PSPACE-completeness

::: {#def-pspace-complete .definition name="PSPACE-complete"}

$B$ is *PSPACE-complete* if $B\in\mathrm{PSPACE}$ and $A\le_{\mathrm p}B$ for every $A\in\mathrm{PSPACE}$.

:::

Polynomial-time reductions are used, not polynomial-space ones: a reduction must be weaker than the class, or every problem in the class would be complete.

::: {#thm-tqbf-pspace-complete .theorem name="TQBF is PSPACE-complete"}

:::

::: {.proof}

1. $\mathit{TQBF}\in\mathrm{PSPACE}$ by @thm-tqbf-in-pspace.

2. Let $A$ be decided by a TM $M$ in space $n^k$. As in the proof of @thm-cook-levin, configurations of $M$ on $w$ can be written as $O(n^k)$ Boolean variables. We build quantified formulas $\phi_{c_1,c_2,t}$ meaning "$M$ can go from $c_1$ to $c_2$ in at most $t$ steps".

3. For $t=1$: $\phi_{c_1,c_2,1}$ says $c_1=c_2$ or $c_1$ yields $c_2$, with the window formulas of the Cook–Levin proof; its size is $O(n^k)$.

4. For $t>1$ the obvious recursion $\exists m\,[\phi_{c_1,m,t/2}\wedge\phi_{m,c_2,t/2}]$ doubles the size at each level, which is too big. Instead use a $\forall$ to reuse one copy:

$$
\phi_{c_1,c_2,t}=\exists m\;\forall (c_3,c_4)\in\{(c_1,m),(m,c_2)\}\;\big[\phi_{c_3,c_4,t/2}\big],
$$

where the restricted $\forall$ is written with ordinary quantifiers over the variables of $c_3,c_4$ and an implication.

5. Each level adds $O(n^k)$ symbols and there are $\log_2 2^{dn^k}=O(n^k)$ levels, so $\phi_{c_{\text{start}},c_{\text{acc}},2^{dn^k}}$ has size $O(n^{2k})$ and is built in polynomial time. It is true iff $M$ accepts $w$.

:::

The same proof works for a nondeterministic $M$, which gives another proof that $\mathrm{NPSPACE}\subseteq\mathrm{PSPACE}$.

::: {#fig-savitch-theorem-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {$\phi_{c_1,c_2,t}$};
\node[box] (b) at (-2.4,-1.4) {$\phi_{c_1,m,t/2}$};
\node[box] (c) at (2.4,-1.4) {$\phi_{m,c_2,t/2}$};
\draw[map] (a) -- (b); \draw[map] (a) -- (c);
\node[lab, note] at (0,-2.2) {two copies per level: size $2^{\text{depth}}$};
\begin{scope}[xshift=7.5cm]
\node[box] (a2) at (0,0) {$\phi_{c_1,c_2,t}$};
\node[hl box] (b2) at (0,-1.4) {$\forall(c_3,c_4)\;\phi_{c_3,c_4,t/2}$};
\draw[map] (a2) -- (b2);
\node[lab, note] at (0,-2.2) {one copy per level: size $O(\text{depth})$};
\end{scope}
\end{tikzpicture}
\end{center}
```

Why the proof of @thm-tqbf-pspace-complete uses a universal quantifier: it lets one subformula stand for both halves of the computation.

:::
