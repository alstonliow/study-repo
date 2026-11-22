---
title: "The Hierarchy Theorems"
sources: [mit18404j-21]
requires: [cs/theory/nl-equals-conl, cs/theory/undecidability]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 21, in our own wording; proofs written out in steps. -->

More space or time lets a machine decide more languages. The proofs are diagonalization, as for @thm-atm-undecidable, with a resource bound added.

::: {#def-space-constructible .definition name="Space and time constructible"}

$f:\mathbb N\to\mathbb N$ with $f(n)\ge\log n$ is *space constructible* if some TM, on input $1^n$, writes the binary representation of $f(n)$ using space $O(f(n))$. $t(n)\ge n\log n$ is *time constructible* if some TM, on input $1^n$, writes the binary representation of $t(n)$ in time $O(t(n))$. All the usual functions ($\log n$, $n^k$, $n\log n$, $2^n$) qualify.

:::

::: {#thm-space-hierarchy .theorem name="Space hierarchy theorem"}

For every space constructible $f$ there is a language decidable in space $O(f(n))$ but not in space $o(f(n))$.

:::

::: {.proof}

1. We construct a decider $D$ that runs in space $O(f(n))$ and differs from every machine running in space $o(f(n))$ on some input. On input $w$ of length $n$:
    a. compute $f(n)$ and mark off $f(n)$ cells of tape; if any later step tries to use more, reject;
    b. if $w$ is not of the form $\langle M\rangle 10^*$ for a TM $M$, reject;
    c. simulate $M$ on $w$ for at most $2^{f(n)}$ steps; if $M$ accepts, reject; if $M$ rejects, accept; if it has not halted, reject.

2. $D$ runs in space $O(f(n))$ and always halts. Let $A=L(D)$.

3. Suppose some $M$ decides $A$ in space $g(n)=o(f(n))$. $D$ simulates $M$ with a constant-factor overhead $c$ in space (to encode $M$'s tape alphabet). Because $g=o(f)$, for long enough inputs $c\,g(n)\le f(n)$, and $M$, which halts within $2^{O(g(n))}\le 2^{f(n)}$ steps on such inputs, is simulated to completion.

4. The padding $10^*$ provides such long inputs: take $w=\langle M\rangle10^k$ with $k$ large. Then $D$ completes the simulation and answers the opposite of $M$ on $w$, so $M$ does not decide $A$.

:::

::: {#fig-hierarchy-theorems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.38cm, y=0.38cm]
\foreach \i in {0,...,5} \draw[hl cell] (\i,0) rectangle (\i+1,1);
\node[lab, tick] at (3,0.5) {$\langle M\rangle$};
\draw[cell frame] (6,0) rectangle (7,1); \node[lab, tick] at (6.5,0.5) {1};
\foreach \i in {7,...,18} {\draw[cell frame] (\i,0) rectangle (\i+1,1); \node[lab, tick] at (\i+0.5,0.5) {0};}
\draw[decorate, decoration={brace, mirror, amplitude=4pt}] (7,-0.2) -- node[lab, note, below=4pt] {padding: makes $n$ large enough that $c\,g(n)\le f(n)$} (19,-0.2);
\draw[faint] (0,2.2) -- (24,2.2);
\draw[hl] (0,2.2) -- (14,2.2);
\node[lab, note, anchor=south] at (7,2.3) {$D$'s space budget $f(n)$};
\draw[emph] (0,3.4) -- (9,3.4);
\node[lab, note, anchor=south] at (4.5,3.5) {$M$ needs $c\,g(n)$};
\end{tikzpicture}
\end{center}
```

The diagonal input in the proof of @thm-space-hierarchy. Padding the description of $M$ makes the input long enough that $M$'s simulation fits in $D$'s budget, so $D$ can flip $M$'s answer.

:::

::: {#cor-space-separations .corollary name="Space separations"}

$\mathrm{SPACE}(n^a)\subsetneq\mathrm{SPACE}(n^b)$ for $0\le a<b$; $\mathrm{NL}\subsetneq\mathrm{PSPACE}$; and $\mathrm{PSPACE}\subsetneq\mathrm{EXPSPACE}=\bigcup_k\mathrm{SPACE}(2^{n^k})$.

:::

::: {.proof}

1. The first is @thm-space-hierarchy with $f(n)=n^b$.

2. $\mathrm{NL}\subseteq\mathrm{SPACE}(\log^2 n)$ by @thm-savitch, and $\mathrm{SPACE}(\log^2n)\subsetneq\mathrm{SPACE}(n)\subseteq\mathrm{PSPACE}$ by the theorem with $f(n)=n$.

3. With $f(n)=2^n$ the theorem gives a language in $\mathrm{SPACE}(2^n)\subseteq\mathrm{EXPSPACE}$ that is not in $\mathrm{SPACE}(n^k)$ for any $k$, since $n^k=o(2^n)$; so it is not in $\mathrm{PSPACE}$.

:::

::: {#thm-time-hierarchy .theorem name="Time hierarchy theorem"}

For every time constructible $t$ there is a language decidable in time $O(t(n))$ but not in time $o(t(n)/\log t(n))$.

:::

::: {.proof}

1. The decider $D$ is as in @thm-space-hierarchy, with a step counter instead of a space bound: on $w=\langle M\rangle10^*$ of length $n$, compute $t(n)$, and simulate $M$ on $w$ for $t(n)/\log t(n)$ steps, answering the opposite if $M$ halts and rejecting otherwise.

2. The simulation keeps $M$'s description and the counter close to the head, on extra tracks that move along with it, so that each simulated step costs $O(\log t(n))$ steps (the counter has $\log t(n)$ bits). The total time is $O(t(n))$.

3. If $M$ decides $L(D)$ in time $g(n)=o(t(n)/\log t(n))$, then for a long enough padded input $D$ completes the simulation of $M$ and answers differently. So no such $M$ exists.

:::

::: {#cor-p-ne-exptime .corollary name="$\mathrm P\ne\mathrm{EXPTIME}$"}

$\mathrm{TIME}(n^a)\subsetneq\mathrm{TIME}(n^b)$ for $1\le a<b$, and $\mathrm P\subsetneq\mathrm{EXPTIME}$.

:::

::: {.proof}

1. $n^a=o(n^b/\log n^b)$, so @thm-time-hierarchy separates the two classes.

2. $\mathrm P\subseteq\mathrm{TIME}(2^n)$, while the theorem with $t(n)=2^{2n}$ gives a language in $\mathrm{TIME}(2^{2n})\subseteq\mathrm{EXPTIME}$ that is not in $\mathrm{TIME}(2^{2n}/2n)\supseteq\mathrm{TIME}(2^n)$.

:::

::: {#fig-hierarchy-theorems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \x/\l in {0/{\mathrm{NL}},1.8/{\mathrm P},3.6/{\mathrm{NP}},5.7/{\mathrm{PSPACE}},8.2/{\mathrm{EXPTIME}},10.9/{\mathrm{EXPSPACE}}} \node[lab] at (\x,0) {$\l$};
\foreach \x in {0.9,2.7,4.55,6.95,9.5} \node[lab] at (\x,0) {$\subseteq$};
\draw[hl] (0,-0.35) -- (5.7,-0.35); \node[lab, tick] at (2.85,-0.6) {$\ne$};
\draw[hl] (1.8,-0.95) -- (8.2,-0.95); \node[lab, tick] at (5,-1.2) {$\ne$};
\draw[hl] (5.7,-1.55) -- (10.9,-1.55); \node[lab, tick] at (8.3,-1.8) {$\ne$};
\end{tikzpicture}
\end{center}
```

What the hierarchy theorems separate (@cor-space-separations, @cor-p-ne-exptime). Each bar spans two classes known to differ; which inclusion in between is strict is unknown.

:::
