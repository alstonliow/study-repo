---
title: "Nonregular Languages and the Pumping Lemma"
sources: [mit18404j-3]
requires: [cs/automata/regular-expressions]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 3, in our own wording; proofs written out in steps. -->

A DFA has finitely many states, so it cannot count without bound. The pumping lemma turns this into a tool for proving that a language is not regular.

::: {#thm-pumping-lemma-regular .theorem name="Pumping lemma for regular languages"}

If $A$ is regular, there is a number $p$ (the *pumping length*) such that every $s\in A$ with $|s|\ge p$ can be written $s=xyz$ with

$$
xy^iz\in A \text{ for all } i\ge0,\qquad |y|>0,\qquad |xy|\le p.
$$

:::

::: {.proof}

1. Let a DFA $M$ with $p$ states recognize $A$, and let $s\in A$ with $n=|s|\ge p$.

2. On $s$, $M$ visits the $n+1$ states $r_0,r_1,\dots,r_n$. Among the first $p+1$ of them, $r_0,\dots,r_p$, two are equal by the pigeonhole principle: $r_j=r_l$ with $j<l\le p$.

3. Let $x=s_1\cdots s_j$, $y=s_{j+1}\cdots s_l$ and $z$ the rest. Then $y$ takes $M$ from $r_j$ back to $r_j$, so $|y|=l-j>0$, and $|xy|=l\le p$.

4. For each $i\ge0$, on $xy^iz$ the machine reaches $r_j$ after $x$, returns to $r_j$ after each copy of $y$, and then reads $z$ exactly as on $s$, ending in the accept state $r_n$. So $xy^iz\in A$.

:::

::: {#fig-nonregular-languages-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[state] (0) at (0,0) {$r_0$};
\node[hl state] (j) at (2.8,0) {$r_j$};
\node[accept state] (n) at (5.6,0) {$r_n$};
\draw[start] (0.west) -- ++(-0.6,0);
\draw[trans, dashed] (0) -- node[lab, note, above=2pt] {$x$} (j);
\draw[trans, dashed] (j) -- node[lab, note, above=2pt] {$z$} (n);
\draw[trans] (j) .. controls (1.8,2.2) and (3.8,2.2) .. node[lab, note, above] {$y$} (j);
\draw[cell frame] (0,-1.4) rectangle (1.6,-0.9); \node[lab] at (0.8,-1.15) {$x$};
\draw[hl cell] (1.6,-1.4) rectangle (3.4,-0.9); \node[lab] at (2.5,-1.15) {$y$};
\draw[cell frame] (3.4,-1.4) rectangle (5.6,-0.9); \node[lab] at (4.5,-1.15) {$z$};
\draw[decorate, decoration={brace, mirror, amplitude=4pt}] (0,-1.5) -- node[lab, note, below=4pt] {$|xy|\le p$} (3.4,-1.5);
\end{tikzpicture}
\end{center}
```

Proof of @thm-pumping-lemma-regular: within the first $p$ symbols the run repeats a state $r_j$, and the input read between the two visits is $y$. Skipping the loop ($i=0$) or going round it more often ($i\ge2$) still ends in $r_n$.

:::

To show $A$ is not regular: assume it is, take its pumping length $p$, choose a string $s\in A$ with $|s|\ge p$ (the choice is ours), and show that *every* split $s=xyz$ with $|y|>0$ and $|xy|\le p$ has some $xy^iz\notin A$.

::: {#exm-0n1n-nonregular .example name="$0^k1^k$ is not regular"}

Let $D=\{0^k1^k: k\ge0\}$ and suppose it is regular with pumping length $p$. Take $s=0^p1^p\in D$. In any split with $|xy|\le p$, the string $y$ lies inside the leading $0$'s and is nonempty, so $xyyz=0^{p+|y|}1^p$ has more $0$'s than $1$'s and is not in $D$. This contradicts the pumping lemma.

:::

::: {#exm-equal-01-nonregular .example name="Equal numbers of 0s and 1s"}

Let $B=\{w: w \text{ has equal numbers of } 0\text{s and } 1\text{s}\}$. If $B$ were regular, so would be $B\cap 0^*1^*=D$ (@prp-regular-complement-intersection and @thm-regex-to-nfa), contradicting @exm-0n1n-nonregular. Closure properties often save a pumping argument.

By contrast, the strings with equal numbers of the substrings $01$ and $10$ form a regular language: in any binary string these counts differ by at most one, and they are equal exactly when the string is empty or starts and ends with the same symbol.

:::

::: {#exm-ww-nonregular .example name="Doubled strings"}

Let $F=\{ww: w\in\{0,1\}^*\}$. With pumping length $p$, take $s=0^p1\,0^p1\in F$. Any admissible $y$ consists of $0$'s from the first block, so $xyyz=0^{p+|y|}1\,0^p1$. A string in $F$ has even length and its two halves are equal; here either the length is odd, or the first half ends in $0$ while the whole string ends in $1$. So $xyyz\notin F$, and $F$ is not regular. (The choice $s=0^p0^p$ would fail: it can be pumped.)

:::

::: {#rmk-nonregular-languages-1}

The pumping lemma gives a necessary condition, not a sufficient one: some nonregular languages satisfy its conclusion, so failing to find a contradiction proves nothing.

:::

::: {#fig-nonregular-languages-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.42cm]
\foreach \i in {0,...,5} \draw[cell frame] (\i,0) rectangle (\i+1,0.42);
\foreach \i in {6,...,11} \draw[cell frame] (\i,0) rectangle (\i+1,0.42);
\foreach \i in {2,3} \draw[hl cell] (\i,0) rectangle (\i+1,0.42);
\foreach \i in {0,...,5} \node[lab, note] at (\i+0.5,0.21) {0};
\foreach \i in {6,...,11} \node[lab, note] at (\i+0.5,0.21) {1};
\node[lab, note, anchor=east] at (-0.3,0.21) {$s=0^p1^p$};
\begin{scope}[yshift=-0.9cm]
\foreach \i in {0,...,7} \draw[cell frame] (\i,0) rectangle (\i+1,0.42);
\foreach \i in {2,3,4,5} \draw[hl cell] (\i,0) rectangle (\i+1,0.42);
\foreach \i in {8,...,13} \draw[cell frame] (\i,0) rectangle (\i+1,0.42);
\foreach \i in {0,...,7} \node[lab, note] at (\i+0.5,0.21) {0};
\foreach \i in {8,...,13} \node[lab, note] at (\i+0.5,0.21) {1};
\node[lab, note, anchor=east] at (-0.3,0.21) {$xy^2z$};
\node[lab, note, anchor=west] at (14.4,0.21) {more 0s than 1s};
\end{scope}
\draw[decorate, decoration={brace, amplitude=3pt}] (2,0.5) -- node[lab, note, above=3pt] {$y$} (4,0.5);
\end{tikzpicture}
\end{center}
```

@exm-0n1n-nonregular with $p=6$: whatever $y$ is, it lies in the first $p$ symbols, all $0$'s, so pumping it up unbalances the string.

:::
