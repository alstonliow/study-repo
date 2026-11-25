---
title: "Optimal Binary Search Trees"
sources: [mit6046-10]
requires: [cs/algorithm-design/interval-subproblems, cs/data-structures/binary-trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 10, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/interval-subproblems on 2026-11-25 (one problem per note, SPEC §8.6). -->

Substring subproblems that guess the root, splitting the keys into two intervals.

::: {#exm-optimal-bst .example name="Optimal binary search tree"}

Keys $k_1<\dots<k_n$ are searched with known weights (frequencies) $w_1,\dots,w_n$. A search for $k_r$ costs the number of nodes on the path to it, that is $\mathrm{depth}(k_r)+1$. Find a binary search tree minimising $\sum_rw_r(\mathrm{depth}(k_r)+1)$.

1. *Subproblems:* $e(i,j)$, the least cost of a search tree on $k_i,\dots,k_j$, for $1\le i\le j+1\le n+1$; let $W(i,j)=w_i+\dots+w_j$.
2. *Relation:* guess the root $k_r$. Every key of the subtree then lies one level deeper than in its own subtree, which adds $W(i,j)$:
   $$e(i,j)=W(i,j)+\min_{i\le r\le j}\bigl\{e(i,r-1)+e(r+1,j)\bigr\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $e(i,i-1)=0$ (an empty tree).
5. *Original:* $e(1,n)$, with the chosen roots recorded to build the tree.
6. *Time:* $O(n^2)$ subproblems, $O(n)$ work each with prefix sums for $W$: $O(n^3)$.

Greedily putting the most frequent key at the root is not optimal: with weights $10,8,9$ for keys $1,2,3$, that tree costs $10+2\cdot9+3\cdot8=52$, while the balanced tree with root $2$ costs $8+2\cdot(10+9)=46$.

:::

```{=latex}
\begin{algorithm}
\caption{Optimal binary search tree}
\begin{algorithmic}
\INPUT Weights $w_1,\dots,w_n$ of keys $k_1<\dots<k_n$
\OUTPUT The least cost $e(1,n)$ and the roots $R$ of an optimal tree
\FOR{$i=1$ to $n+1$}
    \STATE $e(i,i-1)\gets0$
\ENDFOR
\FOR{$\ell=0$ to $n-1$}
    \FOR{$i=1$ to $n-\ell$}
        \STATE $j\gets i+\ell$; $e(i,j)\gets\infty$
        \FOR{$r=i$ to $j$}
            \IF{$e(i,r-1)+e(r+1,j)<e(i,j)$}
                \STATE $e(i,j)\gets e(i,r-1)+e(r+1,j)$; $R(i,j)\gets r$
            \ENDIF
        \ENDFOR
        \STATE $e(i,j)\gets e(i,j)+W(i,j)$ \COMMENT{$W(i,j)=w_i+\dots+w_j$, from prefix sums}
    \ENDFOR
\ENDFOR
\RETURN $e(1,n)$, $R$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-interval-subproblems-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.950,0.950);
\node[lab] at (0.475,0.475) {$0$};
\draw[cell frame] (0.950,0.000) rectangle (1.900,0.950);
\node[lab] at (1.425,0.475) {$10\,/\,1$};
\draw[cell frame] (1.900,0.000) rectangle (2.850,0.950);
\node[lab] at (2.375,0.475) {$26\,/\,1$};
\draw[hl cell] (2.850,0.000) rectangle (3.800,0.950);
\node[lab] at (3.325,0.475) {$46\,/\,2$};
\node[lab,tick,anchor=east] at (-0.050,0.475) {$i=1$};
\draw[cell frame] (0.950,-0.950) rectangle (1.900,0.000);
\node[lab] at (1.425,-0.475) {$0$};
\draw[cell frame] (1.900,-0.950) rectangle (2.850,0.000);
\node[lab] at (2.375,-0.475) {$8\,/\,2$};
\draw[cell frame] (2.850,-0.950) rectangle (3.800,0.000);
\node[lab] at (3.325,-0.475) {$25\,/\,3$};
\node[lab,tick,anchor=east] at (-0.050,-0.475) {$i=2$};
\draw[cell frame] (1.900,-1.900) rectangle (2.850,-0.950);
\node[lab] at (2.375,-1.425) {$0$};
\draw[cell frame] (2.850,-1.900) rectangle (3.800,-0.950);
\node[lab] at (3.325,-1.425) {$9\,/\,3$};
\node[lab,tick,anchor=east] at (-0.050,-1.425) {$i=3$};
\draw[cell frame] (2.850,-2.850) rectangle (3.800,-1.900);
\node[lab] at (3.325,-2.375) {$0$};
\node[lab,tick,anchor=east] at (-0.050,-2.375) {$i=4$};
\node[lab,tick] at (0.475,1.130) {$j=0$};
\node[lab,tick] at (1.425,1.130) {$j=1$};
\node[lab,tick] at (2.375,1.130) {$j=2$};
\node[lab,tick] at (3.325,1.130) {$j=3$};
\end{tikzpicture}
\end{center}
```

The table for keys $1,2,3$ with weights $10,8,9$: each cell shows $e(i,j)$ and the best root $R(i,j)$; the cells $e(i,i-1)=0$ are empty trees. The answer $e(1,3)=46$ has root $2$, which gives the balanced tree of @fig-interval-subproblems-1.

:::

::: {#fig-interval-subproblems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0,0) {$1$}; \node[small vertex] (b) at (0.8,-0.9) {$3$}; \node[small vertex] (c) at (0.3,-1.8) {$2$};
\draw (a)--(b) (b)--(c);
\node[lab,tick] at (0.4,-2.5) {cost $10+2\cdot9+3\cdot8=52$};
\node[small vertex] (d) at (5,0) {$2$}; \node[small vertex] (e) at (4.3,-0.9) {$1$}; \node[small vertex] (f) at (5.7,-0.9) {$3$};
\draw (d)--(e) (d)--(f);
\node[lab,tick] at (5,-2.5) {cost $8+2\cdot(10+9)=46$};
\node[lab,tick] at (0.4,0.6) {greedy: heaviest key at the root};
\node[lab,tick] at (5,0.6) {optimal};
\end{tikzpicture}
\end{center}
```

Search trees for keys $1,2,3$ with weights $10,8,9$. Putting the heaviest key at the root (left) costs $52$; the balanced tree found by the dynamic program (right) costs $46$.

:::
