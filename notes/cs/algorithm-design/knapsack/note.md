---
title: "0-1 Knapsack"
sources: [mit6006-18, mit6006r-18]
requires: [cs/algorithm-design/subset-sum]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 18 and Recitation 18, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/pseudopolynomial-time on 2026-11-25 (one problem per note, SPEC §8.6). -->

Subset sum with values: the same subproblems, maximising instead of deciding.

::: {#exm-knapsack .example name="0-1 knapsack"}

Items $i=0,\dots,n-1$ have integer sizes $s_i$ and values $v_i$, and a knapsack has capacity $S$. Choose items of total size at most $S$ and largest total value. With subproblems $x(i,c)$, the best value from items $i,\dots,n-1$ with capacity $c$:
$$x(i,c)=\max\bigl\{x(i+1,c),\ v_i+x(i+1,c-s_i)\ \text{(if }s_i\le c)\bigr\},\qquad x(n,c)=0,$$
and the answer $x(0,S)$, in $O(nS)$ time. Rod cutting is the *unbounded* version, where each piece length may be used any number of times (relation $x(c)=\max_i\{v_i+x(c-s_i)\}$), and subset sum is the case $v_i=s_i$ with the question whether the value $S$ is reached.

:::

```{=latex}
\begin{algorithm}
\caption{0-1 knapsack}
\begin{algorithmic}
\INPUT Sizes $s_i$ and values $v_i$, $i=0,\dots,n-1$; capacity $S$
\OUTPUT The largest total value $x(0,S)$
\STATE $x(n,c)\gets0$ for $0\le c\le S$
\FOR{$i=n-1$ down to $0$}
    \FOR{$c=0$ to $S$}
        \STATE $x(i,c)\gets x(i+1,c)$
        \IF{$s_i\le c$}
            \STATE $x(i,c)\gets\max\{x(i,c),\ v_i+x(i+1,c-s_i)\}$
        \ENDIF
    \ENDFOR
\ENDFOR
\RETURN $x(0,S)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-pseudopolynomial-time-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$0$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$1$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$4$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$5$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$7$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$8$};
\draw[hl cell] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$9$};
\node[lab,tick,anchor=east] at (-0.050,0.275) {$(1,1)$};
\draw[cell frame] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$0$};
\draw[cell frame] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$0$};
\draw[cell frame] (1.100,-0.550) rectangle (1.650,0.000);
\node[lab] at (1.375,-0.275) {$0$};
\draw[cell frame] (1.650,-0.550) rectangle (2.200,0.000);
\node[lab] at (1.925,-0.275) {$4$};
\draw[cell frame] (2.200,-0.550) rectangle (2.750,0.000);
\node[lab] at (2.475,-0.275) {$5$};
\draw[cell frame] (2.750,-0.550) rectangle (3.300,0.000);
\node[lab] at (3.025,-0.275) {$7$};
\draw[cell frame] (3.300,-0.550) rectangle (3.850,0.000);
\node[lab] at (3.575,-0.275) {$7$};
\draw[hl cell] (3.850,-0.550) rectangle (4.400,0.000);
\node[lab] at (4.125,-0.275) {$9$};
\node[lab,tick,anchor=east] at (-0.050,-0.275) {$(3,4)$};
\draw[cell frame] (0.000,-1.100) rectangle (0.550,-0.550);
\node[lab] at (0.275,-0.825) {$0$};
\draw[cell frame] (0.550,-1.100) rectangle (1.100,-0.550);
\node[lab] at (0.825,-0.825) {$0$};
\draw[cell frame] (1.100,-1.100) rectangle (1.650,-0.550);
\node[lab] at (1.375,-0.825) {$0$};
\draw[cell frame] (1.650,-1.100) rectangle (2.200,-0.550);
\node[lab] at (1.925,-0.825) {$0$};
\draw[hl cell] (2.200,-1.100) rectangle (2.750,-0.550);
\node[lab] at (2.475,-0.825) {$5$};
\draw[cell frame] (2.750,-1.100) rectangle (3.300,-0.550);
\node[lab] at (3.025,-0.825) {$7$};
\draw[cell frame] (3.300,-1.100) rectangle (3.850,-0.550);
\node[lab] at (3.575,-0.825) {$7$};
\draw[cell frame] (3.850,-1.100) rectangle (4.400,-0.550);
\node[lab] at (4.125,-0.825) {$7$};
\node[lab,tick,anchor=east] at (-0.050,-0.825) {$(4,5)$};
\draw[hl cell] (0.000,-1.650) rectangle (0.550,-1.100);
\node[lab] at (0.275,-1.375) {$0$};
\draw[cell frame] (0.550,-1.650) rectangle (1.100,-1.100);
\node[lab] at (0.825,-1.375) {$0$};
\draw[cell frame] (1.100,-1.650) rectangle (1.650,-1.100);
\node[lab] at (1.375,-1.375) {$0$};
\draw[cell frame] (1.650,-1.650) rectangle (2.200,-1.100);
\node[lab] at (1.925,-1.375) {$0$};
\draw[cell frame] (2.200,-1.650) rectangle (2.750,-1.100);
\node[lab] at (2.475,-1.375) {$0$};
\draw[cell frame] (2.750,-1.650) rectangle (3.300,-1.100);
\node[lab] at (3.025,-1.375) {$7$};
\draw[cell frame] (3.300,-1.650) rectangle (3.850,-1.100);
\node[lab] at (3.575,-1.375) {$7$};
\draw[cell frame] (3.850,-1.650) rectangle (4.400,-1.100);
\node[lab] at (4.125,-1.375) {$7$};
\node[lab,tick,anchor=east] at (-0.050,-1.375) {$(5,7)$};
\draw[hl cell] (0.000,-2.200) rectangle (0.550,-1.650);
\node[lab] at (0.275,-1.925) {$0$};
\draw[cell frame] (0.550,-2.200) rectangle (1.100,-1.650);
\node[lab] at (0.825,-1.925) {$0$};
\draw[cell frame] (1.100,-2.200) rectangle (1.650,-1.650);
\node[lab] at (1.375,-1.925) {$0$};
\draw[cell frame] (1.650,-2.200) rectangle (2.200,-1.650);
\node[lab] at (1.925,-1.925) {$0$};
\draw[cell frame] (2.200,-2.200) rectangle (2.750,-1.650);
\node[lab] at (2.475,-1.925) {$0$};
\draw[cell frame] (2.750,-2.200) rectangle (3.300,-1.650);
\node[lab] at (3.025,-1.925) {$0$};
\draw[cell frame] (3.300,-2.200) rectangle (3.850,-1.650);
\node[lab] at (3.575,-1.925) {$0$};
\draw[cell frame] (3.850,-2.200) rectangle (4.400,-1.650);
\node[lab] at (4.125,-1.925) {$0$};
\node[lab,tick,anchor=east] at (-0.050,-1.925) {$i=n$};
\node[lab,tick] at (0.275,0.730) {$0$};
\node[lab,tick] at (0.825,0.730) {$1$};
\node[lab,tick] at (1.375,0.730) {$2$};
\node[lab,tick] at (1.925,0.730) {$3$};
\node[lab,tick] at (2.475,0.730) {$4$};
\node[lab,tick] at (3.025,0.730) {$5$};
\node[lab,tick] at (3.575,0.730) {$6$};
\node[lab,tick] at (4.125,0.730) {$7$};
\end{tikzpicture}
\end{center}
```

The table $x(i,c)$ for items (size, value) $(1,1),(3,4),(4,5),(5,7)$ and capacity $S=7$ (row $i$, column $c$), filled from the bottom row $x(n,c)=0$. The answer is $x(0,7)=9$. The highlighted cells follow the choices: the first item is skipped, the items of sizes $3$ and $4$ are taken, and the last does not fit.

:::
