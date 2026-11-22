---
title: "NL = coNL"
sources: [mit18404j-20, mit18404j-21]
requires: [cs/theory/logarithmic-space]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lectures 20 and 21, in our own wording; proofs written out in steps. -->

For time, it is open whether $\mathrm{NP}=\mathrm{coNP}$. For logarithmic space the analogous question has a positive answer: a nondeterministic machine can *certify* that a node is unreachable.

::: {#thm-immerman-szelepcsenyi .theorem name="Immerman–Szelepcsényi"}

$\mathrm{NL}=\mathrm{coNL}$. Equivalently, $\overline{\mathit{PATH}}\in\mathrm{NL}$.

:::

```{=latex}
\begin{algorithm}
\caption{Inductive counting: one branch of the NL machine for $\overline{\mathit{PATH}}$}
\begin{algorithmic}
\INPUT graph $G$ with $m$ nodes, nodes $s,t$
\STATE $c\gets1$ \COMMENT{$c=c_0=|R_0|$}
\FOR{$i=0$ \TO $m-1$}
    \STATE $c'\gets0$
    \FOR{each node $v$}
        \STATE $d\gets0$; $\mathit{in}\gets$ false
        \FOR{each node $u$}
            \STATE guess whether $u\in R_i$; if yes, guess a path from $s$ to $u$ of length $\le i$ (reject if it fails), $d\gets d+1$, and set $\mathit{in}\gets$ true if $u=v$ or $u\to v$
        \ENDFOR
        \STATE \textbf{if} $d\ne c$ \textbf{then} reject
        \STATE \textbf{if} $\mathit{in}$ \textbf{then} $c'\gets c'+1$
    \ENDFOR
    \STATE $c\gets c'$ \COMMENT{now $c=c_{i+1}$}
\ENDFOR
\STATE confirm $c$ members of $R_m$ as in the loop above, rejecting if $t$ is one of them or if fewer are found
\STATE accept
\end{algorithmic}
\end{algorithm}
```

The two statements are equivalent because $\mathit{PATH}$ is NL-complete (@thm-path-nl-complete): if $\overline{\mathit{PATH}}\in\mathrm{NL}$, then every $A\in\mathrm{NL}$ has $\overline A\le_{\mathrm L}\overline{\mathit{PATH}}$ and so $\overline A\in\mathrm{NL}$ (as in @prp-log-space-reduction-properties, nondeterministically).

A nondeterministic machine *computes* a value if every branch either outputs the correct value or rejects, and at least one branch outputs it.

::: {.proof}

1. Let $G$ have $m$ nodes and let $R_i$ be the set of nodes reachable from $s$ by paths of length at most $i$, and $c_i=|R_i|$. So $R_0=\{s\}$, $c_0=1$, and $R_{m}$ is the set of all nodes reachable from $s$.

2. *Using a count to certify non-reachability.* Suppose $c_i$ is known. To check that a node $v$ is not in $R_i$: go through all nodes $u$ in order; for each, guess whether $u\in R_i$, and if so, guess a path of length at most $i$ from $s$ to $u$ and reject if the guess fails; count the nodes confirmed to be in $R_i$, and reject if $u=v$ is one of them. At the end, if the count equals $c_i$, every node of $R_i$ was found and $v$ was not among them; otherwise reject.

3. *Computing $c_{i+1}$ from $c_i$.* Go through all nodes $v$ and decide whether $v\in R_{i+1}$: as in step 2, run through all $u$, confirming the members of $R_i$ by guessed paths; $v\in R_{i+1}$ iff $v$ equals or is adjacent from some confirmed $u$. If the confirmed count is not $c_i$, reject. This decides membership of $v$ in both directions, so counting the $v$ that are in $R_{i+1}$ gives $c_{i+1}$.

4. Starting from $c_0=1$, compute $c_1,c_2,\dots,c_m$, keeping only the current and next count. Finally apply step 2 with $c_m$ to $v=t$, and accept iff $t\notin R_m$.

5. Every branch that does not reject has verified each claim it used, so it gives the right answer; the branch that guesses correctly everywhere does not reject. The work tape holds a constant number of nodes, counters and counts, all of $O(\log m)$ bits.

:::

::: {#fig-nl-equals-conl-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionC] (0.8,0) ellipse (2.3 and 1.45);
\draw[regionB] (0.4,0) ellipse (1.35 and 1.0);
\draw[regionA] (0,0) circle (0.55);
\node[dot] (s) at (0,0) {};
\node[lab, note] at (0,-0.28) {$s$};
\node[lab, tick] at (0,0.32) {$R_0$};
\node[lab, tick] at (1.2,0.55) {$R_1$};
\node[lab, tick] at (2.4,0.9) {$R_2$};
\node[hl dot] at (4.0,-0.4) {};
\node[lab, note] at (4.0,-0.75) {$t$};
\node[lab, note, anchor=west] at (4.4,0.5) {count $c_0=1,\ c_1,\ c_2,\dots$};
\node[lab, note, anchor=west] at (4.4,0) {$t$ outside: find all $c_m$ members};
\node[lab, note, anchor=west] at (4.4,-0.4) {of $R_m$, none of them $t$};
\end{tikzpicture}
\end{center}
```

Inductive counting (@thm-immerman-szelepcsenyi): from the size $c_i$ of the set $R_i$ reachable in at most $i$ steps, the machine computes $c_{i+1}$; knowing $c_m$, it certifies that $t$ is unreachable by exhibiting all reachable nodes.

:::

::: {#exm-nl-equals-conl .example name="Counting on a small graph"}

Let $G$ have nodes $s,a,b,t$ and edges $s\to a$, $a\to b$, $t\to b$. Then $R_0=\{s\}$, $R_1=\{s,a\}$, $R_2=R_3=\{s,a,b\}$, so $c_0,c_1,c_2,c_3=1,2,3,3$. To certify that $t$ is unreachable, a branch guesses paths to $s$, $a$ and $b$ (of lengths $0,1,2$), reaches the count $3=c_3$, and has not met $t$.

:::

::: {#cor-nl-complete-complements .corollary name="The complement of PATH is NL-complete"}

:::

::: {.proof}

1. $\overline{\mathit{PATH}}\in\mathrm{NL}$ by @thm-immerman-szelepcsenyi.

2. For every $A\in\mathrm{NL}$, also $\overline A\in\mathrm{NL}$, so $\overline A\le_{\mathrm L}\mathit{PATH}$ by @thm-path-nl-complete. The same reduction gives $A\le_{\mathrm L}\overline{\mathit{PATH}}$.

:::
