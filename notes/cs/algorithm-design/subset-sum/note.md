---
title: "Subset Sum"
sources: [mit6006-18, mit6006r-18]
requires: [cs/algorithm-design/pseudopolynomial-time]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 18 and Recitation 18, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/pseudopolynomial-time on 2026-11-25 (one problem per note, SPEC §8.6). -->

Suffixes of the items paired with integer targets: a pseudopolynomial dynamic program (@def-pseudopolynomial).

::: {#exm-subset-sum .example name="Subset sum"}

Given positive integers $a_0,\dots,a_{n-1}$ and a target $T$, is there a subset with sum exactly $T$? This is a *decision problem*: the answer is yes or no. For $2,5,9,14$ the target $16=2+14$ is reachable, while $10$ is not.

1. *Subproblems:* $x(i,t)$: does some subset of $a_i,\dots,a_{n-1}$ sum to $t$? For $0\le i\le n$, $0\le t\le T$.
2. *Relation:* $a_i$ is used or not: $x(i,t)=x(i+1,t)\ \text{or}\ \bigl(t\ge a_i\ \text{and}\ x(i+1,t-a_i)\bigr)$.
3. *Order:* decreasing $i$. 4. *Base:* $x(i,0)=$ yes; $x(n,t)=$ no for $t\ge1$.
5. *Original:* $x(0,T)$. 6. *Time:* $O(nT)$ subproblems with $O(1)$ work: $O(nT)$.

Bottom up computes all $(n+1)(T+1)$ entries; top down computes only those reachable from $x(0,T)$, which can be far fewer.

:::

```{=latex}
\begin{algorithm}
\caption{Subset sum}
\begin{algorithmic}
\INPUT Positive integers $a_0,\dots,a_{n-1}$ and a target $T$
\OUTPUT Whether some subset sums to $T$
\STATE $x(n,0)\gets$ yes; $x(n,t)\gets$ no for $1\le t\le T$
\FOR{$i=n-1$ down to $0$}
    \FOR{$t=0$ to $T$}
        \STATE $x(i,t)\gets x(i+1,t)$
        \IF{$t\ge a_i$ and $x(i+1,t-a_i)$}
            \STATE $x(i,t)\gets$ yes
        \ENDIF
    \ENDFOR
\ENDFOR
\RETURN $x(0,T)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-pseudopolynomial-time-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,tick] at (0.21,0.2) {0};
\node[lab,tick] at (0.63,0.2) {1};
\node[lab,tick] at (1.05,0.2) {2};
\node[lab,tick] at (1.47,0.2) {3};
\node[lab,tick] at (1.89,0.2) {4};
\node[lab,tick] at (2.31,0.2) {5};
\node[lab,tick] at (2.73,0.2) {6};
\node[lab,tick] at (3.15,0.2) {7};
\node[lab,tick] at (3.57,0.2) {8};
\node[lab,tick] at (3.99,0.2) {9};
\node[lab,tick] at (4.41,0.2) {10};
\node[lab,tick] at (4.83,0.2) {11};
\node[lab,tick] at (5.25,0.2) {12};
\node[lab,tick] at (5.67,0.2) {13};
\node[lab,tick] at (6.09,0.2) {14};
\node[lab,tick] at (6.51,0.2) {15};
\node[lab,tick] at (6.93,0.2) {16};
\node[lab,tick, anchor=east] at (-0.05,-0.21) {$i=0$ ($a_i=2$)};
\draw[hl cell] (0.00,0.00) rectangle (0.42,-0.42);
\draw[cell frame] (0.42,0.00) rectangle (0.84,-0.42);
\draw[hl cell] (0.84,0.00) rectangle (1.26,-0.42);
\draw[cell frame] (1.26,0.00) rectangle (1.68,-0.42);
\draw[cell frame] (1.68,0.00) rectangle (2.10,-0.42);
\draw[hl cell] (2.10,0.00) rectangle (2.52,-0.42);
\draw[cell frame] (2.52,0.00) rectangle (2.94,-0.42);
\draw[hl cell] (2.94,0.00) rectangle (3.36,-0.42);
\draw[cell frame] (3.36,0.00) rectangle (3.78,-0.42);
\draw[hl cell] (3.78,0.00) rectangle (4.20,-0.42);
\draw[cell frame] (4.20,0.00) rectangle (4.62,-0.42);
\draw[hl cell] (4.62,0.00) rectangle (5.04,-0.42);
\draw[cell frame] (5.04,0.00) rectangle (5.46,-0.42);
\draw[cell frame] (5.46,0.00) rectangle (5.88,-0.42);
\draw[hl cell] (5.88,0.00) rectangle (6.30,-0.42);
\draw[cell frame] (6.30,0.00) rectangle (6.72,-0.42);
\draw[hl cell] (6.72,0.00) rectangle (7.14,-0.42);
\node[lab,tick, anchor=east] at (-0.05,-0.63) {$i=1$ ($a_i=5$)};
\draw[hl cell] (0.00,-0.42) rectangle (0.42,-0.84);
\draw[cell frame] (0.42,-0.42) rectangle (0.84,-0.84);
\draw[cell frame] (0.84,-0.42) rectangle (1.26,-0.84);
\draw[cell frame] (1.26,-0.42) rectangle (1.68,-0.84);
\draw[cell frame] (1.68,-0.42) rectangle (2.10,-0.84);
\draw[hl cell] (2.10,-0.42) rectangle (2.52,-0.84);
\draw[cell frame] (2.52,-0.42) rectangle (2.94,-0.84);
\draw[cell frame] (2.94,-0.42) rectangle (3.36,-0.84);
\draw[cell frame] (3.36,-0.42) rectangle (3.78,-0.84);
\draw[hl cell] (3.78,-0.42) rectangle (4.20,-0.84);
\draw[cell frame] (4.20,-0.42) rectangle (4.62,-0.84);
\draw[cell frame] (4.62,-0.42) rectangle (5.04,-0.84);
\draw[cell frame] (5.04,-0.42) rectangle (5.46,-0.84);
\draw[cell frame] (5.46,-0.42) rectangle (5.88,-0.84);
\draw[hl cell] (5.88,-0.42) rectangle (6.30,-0.84);
\draw[cell frame] (6.30,-0.42) rectangle (6.72,-0.84);
\draw[cell frame] (6.72,-0.42) rectangle (7.14,-0.84);
\node[lab,tick, anchor=east] at (-0.05,-1.05) {$i=2$ ($a_i=9$)};
\draw[hl cell] (0.00,-0.84) rectangle (0.42,-1.26);
\draw[cell frame] (0.42,-0.84) rectangle (0.84,-1.26);
\draw[cell frame] (0.84,-0.84) rectangle (1.26,-1.26);
\draw[cell frame] (1.26,-0.84) rectangle (1.68,-1.26);
\draw[cell frame] (1.68,-0.84) rectangle (2.10,-1.26);
\draw[cell frame] (2.10,-0.84) rectangle (2.52,-1.26);
\draw[cell frame] (2.52,-0.84) rectangle (2.94,-1.26);
\draw[cell frame] (2.94,-0.84) rectangle (3.36,-1.26);
\draw[cell frame] (3.36,-0.84) rectangle (3.78,-1.26);
\draw[hl cell] (3.78,-0.84) rectangle (4.20,-1.26);
\draw[cell frame] (4.20,-0.84) rectangle (4.62,-1.26);
\draw[cell frame] (4.62,-0.84) rectangle (5.04,-1.26);
\draw[cell frame] (5.04,-0.84) rectangle (5.46,-1.26);
\draw[cell frame] (5.46,-0.84) rectangle (5.88,-1.26);
\draw[hl cell] (5.88,-0.84) rectangle (6.30,-1.26);
\draw[cell frame] (6.30,-0.84) rectangle (6.72,-1.26);
\draw[cell frame] (6.72,-0.84) rectangle (7.14,-1.26);
\node[lab,tick, anchor=east] at (-0.05,-1.47) {$i=3$ ($a_i=14$)};
\draw[hl cell] (0.00,-1.26) rectangle (0.42,-1.68);
\draw[cell frame] (0.42,-1.26) rectangle (0.84,-1.68);
\draw[cell frame] (0.84,-1.26) rectangle (1.26,-1.68);
\draw[cell frame] (1.26,-1.26) rectangle (1.68,-1.68);
\draw[cell frame] (1.68,-1.26) rectangle (2.10,-1.68);
\draw[cell frame] (2.10,-1.26) rectangle (2.52,-1.68);
\draw[cell frame] (2.52,-1.26) rectangle (2.94,-1.68);
\draw[cell frame] (2.94,-1.26) rectangle (3.36,-1.68);
\draw[cell frame] (3.36,-1.26) rectangle (3.78,-1.68);
\draw[cell frame] (3.78,-1.26) rectangle (4.20,-1.68);
\draw[cell frame] (4.20,-1.26) rectangle (4.62,-1.68);
\draw[cell frame] (4.62,-1.26) rectangle (5.04,-1.68);
\draw[cell frame] (5.04,-1.26) rectangle (5.46,-1.68);
\draw[cell frame] (5.46,-1.26) rectangle (5.88,-1.68);
\draw[hl cell] (5.88,-1.26) rectangle (6.30,-1.68);
\draw[cell frame] (6.30,-1.26) rectangle (6.72,-1.68);
\draw[cell frame] (6.72,-1.26) rectangle (7.14,-1.68);
\node[lab,tick, anchor=east] at (-0.05,-1.89) {$i=4$};
\draw[hl cell] (0.00,-1.68) rectangle (0.42,-2.10);
\draw[cell frame] (0.42,-1.68) rectangle (0.84,-2.10);
\draw[cell frame] (0.84,-1.68) rectangle (1.26,-2.10);
\draw[cell frame] (1.26,-1.68) rectangle (1.68,-2.10);
\draw[cell frame] (1.68,-1.68) rectangle (2.10,-2.10);
\draw[cell frame] (2.10,-1.68) rectangle (2.52,-2.10);
\draw[cell frame] (2.52,-1.68) rectangle (2.94,-2.10);
\draw[cell frame] (2.94,-1.68) rectangle (3.36,-2.10);
\draw[cell frame] (3.36,-1.68) rectangle (3.78,-2.10);
\draw[cell frame] (3.78,-1.68) rectangle (4.20,-2.10);
\draw[cell frame] (4.20,-1.68) rectangle (4.62,-2.10);
\draw[cell frame] (4.62,-1.68) rectangle (5.04,-2.10);
\draw[cell frame] (5.04,-1.68) rectangle (5.46,-2.10);
\draw[cell frame] (5.46,-1.68) rectangle (5.88,-2.10);
\draw[cell frame] (5.88,-1.68) rectangle (6.30,-2.10);
\draw[cell frame] (6.30,-1.68) rectangle (6.72,-2.10);
\draw[cell frame] (6.72,-1.68) rectangle (7.14,-2.10);
\draw[emph] (6.72,0) rectangle (7.14,-0.42);
\end{tikzpicture}
\end{center}
```

The subset sum table for $2,5,9,14$: row $i$, column $t$ is shaded when some subset of $a_i,\dots,a_{n-1}$ sums to $t$. Rows are filled from the bottom ($i=n$: only $t=0$). The framed cell $x(0,16)$ is shaded ($16=2+14$), while $x(0,10)$ is not. The table has $(n+1)(T+1)$ cells, which grows with the value $T$, not just with $n$.

:::
