---
title: "Bowling"
sources: [mit6006-15, mit6006r-15]
requires: [cs/algorithm-design/recursive-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 15 and Recitation 15, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/recursive-algorithms on 2026-11-25 (one problem per note, SPEC §8.6). -->

Bowling is a first dynamic program designed from scratch with the SRT BOT framework (@def-srtbot), on suffix subproblems.

::: {#exm-bowling .example name="Bowling"}

Pins $0,\dots,n-1$ stand in a row, pin $i$ with value $v_i$ (possibly negative). One throw knocks down either one pin $i$, scoring $v_i$, or two neighbouring pins $i,i+1$, scoring $v_iv_{i+1}$; a pin can be hit only once, and pins may be left standing. Maximise the total score.

1. *Subproblems:* $B(i)$, the best score using only pins $i,\dots,n-1$ (suffixes), for $0\le i\le n$.
2. *Relation:* pin $i$ is skipped, hit alone, or hit with pin $i+1$:
   $$B(i)=\max\{B(i+1),\;v_i+B(i+1),\;v_iv_{i+1}+B(i+2)\}$$
   (the last option only if $i+1<n$).
3. *Order:* decreasing $i$. 4. *Base:* $B(n)=0$. 5. *Original:* $B(0)$.
6. *Time:* $n+1$ subproblems with $O(1)$ work each, so $O(n)$.

For values $3,-2,4,4,-1,2$ the best score is $21$: hit $3$ alone, skip $-2$, hit $4,4$ together, skip $-1$, hit $2$. The best score is the weight of a heaviest path from $B(0)$ to $B(n)$ in the subproblem DAG. A divide-and-conquer attempt (split in the middle, and either hit the two middle pins together or not) also works but takes $O(n^2)$ time and does not generalise as easily.

:::

```{=latex}
\begin{algorithm}
\caption{Bowling}
\begin{algorithmic}
\INPUT Pin values $v_0,\dots,v_{n-1}$
\OUTPUT The best total score $B(0)$
\STATE $B(n)\gets0$
\FOR{$i=n-1$ down to $0$}
    \STATE $B(i)\gets\max\{B(i+1),\ v_i+B(i+1)\}$
    \IF{$i+1<n$}
        \STATE $B(i)\gets\max\{B(i),\ v_iv_{i+1}+B(i+2)\}$
    \ENDIF
\ENDFOR
\RETURN $B(0)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-recursive-algorithms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (b0) at (0.0,0) {$B_0$};
\node[lab,tick] at (0.0,-0.5) {21};
\node[small vertex] (b1) at (1.5,0) {$B_1$};
\node[lab,tick] at (1.5,-0.5) {18};
\node[small vertex] (b2) at (3.0,0) {$B_2$};
\node[lab,tick] at (3.0,-0.5) {18};
\node[small vertex] (b3) at (4.5,0) {$B_3$};
\node[lab,tick] at (4.5,-0.5) {6};
\node[small vertex] (b4) at (6.0,0) {$B_4$};
\node[lab,tick] at (6.0,-0.5) {2};
\node[small vertex] (b5) at (7.5,0) {$B_5$};
\node[lab,tick] at (7.5,-0.5) {2};
\node[small vertex] (b6) at (9.0,0) {$B_6$};
\node[lab,tick] at (9.0,-0.5) {0};
\draw[->, hl] (b0) -- node[edge label] {$3$} (b1);
\draw[->] (b0) to[bend left=45] node[edge label] {$-6$} (b2);
\draw[->, hl] (b1) -- node[edge label] {$0$} (b2);
\draw[->] (b1) to[bend left=45] node[edge label] {$-8$} (b3);
\draw[->] (b2) -- node[edge label] {$4$} (b3);
\draw[->, hl] (b2) to[bend left=45] node[edge label] {$16$} (b4);
\draw[->] (b3) -- node[edge label] {$4$} (b4);
\draw[->] (b3) to[bend left=45] node[edge label] {$-4$} (b5);
\draw[->, hl] (b4) -- node[edge label] {$0$} (b5);
\draw[->] (b4) to[bend left=45] node[edge label] {$-2$} (b6);
\draw[->, hl] (b5) -- node[edge label] {$2$} (b6);
\node[lab,tick, anchor=east] at (-0.4,-0.5) {$B(i)$:};
\end{tikzpicture}
\end{center}
```

The subproblem DAG of bowling for pin values $3,-2,4,4,-1,2$. A straight edge $B_i\to B_{i+1}$ handles pin $i$ alone (worth $\max\{v_i,0\}$: hit it or skip it); a curved edge $B_i\to B_{i+2}$ hits pins $i,i+1$ together (worth $v_iv_{i+1}$). The numbers under the vertices are $B(i)$, and the highlighted heaviest path from $B_0$ to $B_6$ has weight $21$.

:::
