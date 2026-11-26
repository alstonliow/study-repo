---
title: "Dynamic Programming over Subsets"
sources: [cs97si-4]
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 4 (subset DP), in our own wording; proofs written out in steps. The example and figure are our own; values checked by computation. -->

When the state must remember *which* items have been used, the subproblems are indexed by subsets. A subset of $\{0,\dots,n-1\}$ is stored as an $n$-bit integer $S$ (a *bitmask*) with bit $i$ set when $i\in S$: then $i\in S$ is `S >> i & 1`, $S\cup\{i\}$ is `S | 1 << i`, and looping $S$ from $0$ to $2^n-1$ visits every subset after all of its proper subsets. This is practical up to $n\approx20$.

::: {#exm-bitmask-dp-tsp .example name="Travelling salesman by subset DP (Held–Karp)"}

Given $n$ cities and distances $d(u,v)\ge0$, find the length of a shortest tour that starts at city $0$, visits every city exactly once and returns to $0$ (@def-travelling-salesman-problem).

1. *Subproblems:* $x(S,v)$ for $0\in S\subseteq\{0,\dots,n-1\}$ and $v\in S$: the length of a shortest path that starts at $0$, visits exactly the cities of $S$, and ends at $v$.
2. *Relation:* the path's last step enters $v$ from some $u\in S\setminus\{v\}$:
   $$x(S,v)=\min_{u\in S\setminus\{v\},\ u\ne v}\bigl(x(S\setminus\{v\},u)+d(u,v)\bigr)\qquad(v\ne0).$$
3. *Order:* increasing $S$ as an integer (removing $v$ makes the mask smaller).
4. *Base:* $x(\{0\},0)=0$; $x(S,0)=\infty$ for $S\ne\{0\}$.
5. *Original:* $\min_{v\ne0}\bigl(x(\{0,\dots,n-1\},v)+d(v,0)\bigr)$.
6. *Time:* $2^n\cdot n$ subproblems with $O(n)$ work each: $O(n^22^n)$, against $(n-1)!$ tours for brute force. Space $O(n2^n)$.

:::

```{=latex}
\begin{algorithm}
\caption{Held--Karp, forward (push) form}
\begin{algorithmic}
\INPUT Distances $d(u,v)$ for $0\le u,v<n$
\OUTPUT The length of a shortest tour
\STATE $x(S,v)\gets\infty$ for all $S,v$; $x(1,0)\gets0$ \COMMENT{mask $1$ is $\{0\}$}
\FOR{$S=1$ \TO $2^n-1$}
    \FOR{$v$ with bit $v$ of $S$ set and $x(S,v)<\infty$}
        \FOR{$u$ with bit $u$ of $S$ clear}
            \STATE $x(S\cup\{u\},u)\gets\min\{x(S\cup\{u\},u),\ x(S,v)+d(v,u)\}$
        \ENDFOR
    \ENDFOR
\ENDFOR
\RETURN $\min_{v\ne0}\bigl(x(2^n-1,v)+d(v,0)\bigr)$
\end{algorithmic}
\end{algorithm}
```

::: {#lem-bitmask-dp-tsp .lemma name="Why the relation is right"}

$x(S,v)$ is the length of a shortest path from $0$ through exactly the cities of $S$ ending at $v$, and the original expression is the shortest tour length.

:::

::: {.proof}

1. Induct on $|S|$. For $S=\{0\}$ the only such path is the empty path at $0$.

2. For $v\ne0$, a path from $0$ through $S$ ending at $v$ consists of a path from $0$ through $S\setminus\{v\}$ ending at its last city $u\ne v$, followed by the edge $uv$. Its length is at least $x(S\setminus\{v\},u)+d(u,v)$ by induction, and a shortest path for $(S\setminus\{v\},u)$ extended by $uv$ achieves it. Minimising over $u$ gives $x(S,v)$.

3. A tour is a path from $0$ through all cities ending at some $v\ne0$, followed by the edge back to $0$; minimising over $v$ gives the original.

:::

::: {#exm-bitmask-dp-tsp-small .example name="Four cities"}

With cities $0,1,2,3$ and (asymmetric) distances, row $u$ giving $d(u,\cdot)$,

$$
d=\begin{pmatrix}0&2&9&10\\1&0&6&4\\15&7&0&8\\6&3&12&0\end{pmatrix},
$$

the table gives $x(\{0,1,2\},2)=8$ (via $0\to1\to2$), $x(\{0,1,2,3\},v)=20,18,16$ for $v=1,2,3$, and the answer $\min(20+1,18+15,16+6)=21$: the tour $0\to2\to3\to1\to0$ of length $9+8+3+1$.

:::

::: {#fig-bitmask-dp-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.1cm,y=1.2cm]
\node[box] (a) at (0,0) {$\{0\}$\\[-1pt]end $0$: $0$};
\node[box] (b1) at (1,1) {$\{0,1\}$\\[-1pt]end $1$: $2$};
\node[box] (b2) at (1,0) {$\{0,2\}$\\[-1pt]end $2$: $9$};
\node[box] (b3) at (1,-1) {$\{0,3\}$\\[-1pt]end $3$: $10$};
\node[box] (c) at (2,0) {$\{0,2,3\}$\\[-1pt]end $3$: $17$};
\node[box] (d) at (3,0) {$\{0,1,2,3\}$\\[-1pt]end $1$: $20$};
\node[hl box] (e) at (4,0) {tour\\[-1pt]$21$};
\draw[map,faint] (a) -- (b1); \draw[map,faint] (a) -- (b3);
\draw[map,hl] (a) -- (b2); \draw[map,hl] (b2) -- node[edge label] {$+8$} (c);
\draw[map,hl] (c) -- node[edge label] {$+3$} (d); \draw[map,hl] (d) -- node[edge label] {$+1$} (e);
\end{tikzpicture}
\end{center}
```

The optimal tour of @exm-bitmask-dp-tsp-small as a path through the subset table: each box is a subset with its end city and value $x(S,v)$.

:::

::: {#rmk-bitmask-dp-1 .remark name="Other subset DPs"}

Assignment problems ("give each of $n$ workers one of $n$ jobs") use $x(S)$ with $|S|$ telling whose turn it is, in $O(n2^n)$. Iterating over all submasks $T\subseteq S$ of every $S$ (with `T = (T - 1) & S`) costs $3^n$ in total and handles partitions into groups. Profile DP for tilings keeps a bitmask of the cells of the current column that are already covered.

:::
