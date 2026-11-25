---
title: "Piano Fingering"
sources: [mit6006-17, mit6006r-17]
requires: [cs/algorithm-design/more-dynamic-programs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 17 and Recitation 17, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/more-dynamic-programs on 2026-11-25 (one problem per note, SPEC §8.6). -->

Suffix subproblems, expanded with the finger that plays the first note.

::: {#exm-piano-fingering .example name="Piano fingering"}

A pianist plays single notes $t_0,\dots,t_{n-1}$ with the right hand, using fingers $1,\dots,F$. A given function $d(t,f,t',f')$ measures the difficulty of moving from note $t$ played with finger $f$ to note $t'$ played with finger $f'$ (a sum of penalties for awkward crossings, weak fingers and so on). Assign fingers to minimise the total difficulty.

The suffix subproblem "best difficulty for $t_i,\dots,t_{n-1}$" is not enough: the cost of the next transition depends on which finger the rest starts with. So expand with that finger.

1. *Subproblems:* $x(i,f)$, the least total difficulty for $t_i,\dots,t_{n-1}$ when $t_i$ is played with finger $f$.
2. *Relation:* guess the finger for $t_{i+1}$: $x(i,f)=\min_{1\le f'\le F}\bigl\{d(t_i,f,t_{i+1},f')+x(i+1,f')\bigr\}$.
3. *Order:* decreasing $i$. 4. *Base:* $x(n-1,f)=0$. 5. *Original:* $\min_fx(0,f)$.
6. *Time:* $nF$ subproblems with $O(F)$ work: $O(nF^2)$, independent of how many different notes there are.

For a guitar, a "finger" becomes a pair (finger, string), replacing $F$ by $FS$ for $S$ strings. If several notes sound at once, each step chooses an assignment of fingers to at most $T$ notes, at most $F^T$ choices, so $O(nF^{2T})$ time, which is linear in $n$ for fixed small $F$ and $T$.

:::

```{=latex}
\begin{algorithm}
\caption{Piano fingering}
\begin{algorithmic}
\INPUT Notes $t_0,\dots,t_{n-1}$, fingers $1,\dots,F$, difficulty function $d$
\OUTPUT The least total difficulty
\FOR{$f=1$ to $F$}
    \STATE $x(n-1,f)\gets0$
\ENDFOR
\FOR{$i=n-2$ down to $0$}
    \FOR{$f=1$ to $F$}
        \STATE $x(i,f)\gets\min_{1\le f'\le F}\{d(t_i,f,t_{i+1},f')+x(i+1,f')\}$
    \ENDFOR
\ENDFOR
\RETURN $\min_fx(0,f)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-more-dynamic-programs-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (x01) at (0.00,0.00) {$x(0,1)$};
\node[box] (x02) at (0.00,-0.90) {$x(0,2)$};
\node[box] (x03) at (0.00,-1.80) {$x(0,3)$};
\node[lab,tick] at (0.00,0.70) {$t_0$};
\node[box] (x11) at (2.00,0.00) {$x(1,1)$};
\node[box] (x12) at (2.00,-0.90) {$x(1,2)$};
\node[box] (x13) at (2.00,-1.80) {$x(1,3)$};
\node[lab,tick] at (2.00,0.70) {$t_1$};
\node[box] (x21) at (4.00,0.00) {$x(2,1)$};
\node[box] (x22) at (4.00,-0.90) {$x(2,2)$};
\node[box] (x23) at (4.00,-1.80) {$x(2,3)$};
\node[lab,tick] at (4.00,0.70) {$t_2$};
\node[box] (x31) at (6.00,0.00) {$x(3,1)$};
\node[box] (x32) at (6.00,-0.90) {$x(3,2)$};
\node[box] (x33) at (6.00,-1.80) {$x(3,3)$};
\node[lab,tick] at (6.00,0.70) {$t_3$};
\draw[->, faint] (x01.east) -- (x11.west);
\draw[->, faint] (x01.east) -- (x12.west);
\draw[->, faint] (x01.east) -- (x13.west);
\draw[->, hl] (x02.east) -- (x11.west);
\draw[->, faint] (x02.east) -- (x12.west);
\draw[->, faint] (x02.east) -- (x13.west);
\draw[->, faint] (x03.east) -- (x11.west);
\draw[->, faint] (x03.east) -- (x12.west);
\draw[->, faint] (x03.east) -- (x13.west);
\draw[->, faint] (x11.east) -- (x21.west);
\draw[->, faint] (x11.east) -- (x22.west);
\draw[->, hl] (x11.east) -- (x23.west);
\draw[->, faint] (x12.east) -- (x21.west);
\draw[->, faint] (x12.east) -- (x22.west);
\draw[->, faint] (x12.east) -- (x23.west);
\draw[->, faint] (x13.east) -- (x21.west);
\draw[->, faint] (x13.east) -- (x22.west);
\draw[->, faint] (x13.east) -- (x23.west);
\draw[->, faint] (x21.east) -- (x31.west);
\draw[->, faint] (x21.east) -- (x32.west);
\draw[->, faint] (x21.east) -- (x33.west);
\draw[->, faint] (x22.east) -- (x31.west);
\draw[->, faint] (x22.east) -- (x32.west);
\draw[->, faint] (x22.east) -- (x33.west);
\draw[->, faint] (x23.east) -- (x31.west);
\draw[->, hl] (x23.east) -- (x32.west);
\draw[->, faint] (x23.east) -- (x33.west);
\end{tikzpicture}
\end{center}
```

The subproblem DAG of piano fingering for $n=4$ notes and $F=3$ fingers. The edge from $x(i,f)$ to $x(i+1,f')$ costs $d(t_i,f,t_{i+1},f')$, and $x(i,f)$ is the lightest path from it to the last column, where $x(n-1,f)=0$. A fingering is a path from the first column to the last (one is highlighted); the program finds a lightest one with $F^2$ edges per pair of neighbouring notes, so $O(nF^2)$ time. The note gives no particular $d$, so the edge costs are left out.

:::
