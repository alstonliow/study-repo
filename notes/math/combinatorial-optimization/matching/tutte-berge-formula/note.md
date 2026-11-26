---
title: "The Tutte–Berge Formula"
sources: [mit18433-2]
requires: [math/combinatorial-optimization/matching/blossom-algorithm]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on non-bipartite matching (Section 2, Tutte–Berge formula and Tutte's theorem), in our own wording; example our own (checked by computation); proofs written out in steps. -->

König's theorem (@thm-konig) is the min-max relation for matchings in bipartite graphs. For general graphs the dual objects are sets of vertices whose deletion leaves many odd components.

::: {#thm-tutte-berge .theorem name="Tutte–Berge formula"}

For every graph $G=(V,E)$,
$$\max_M|M|=\min_{U\subseteq V}\frac12\big(|V|+|U|-o(G-U)\big),$$
where $o(G-U)$ is the number of odd components of $G-U$.

:::

::: {.proof}

1. The inequality $\le$ is @lem-tutte-berge-bound. For $\ge$, run Edmonds' algorithm (@def-blossom-algorithm). Let $G_0=G,G_1,\dots,G_k$ be the graphs after shrinking the blossoms $B_1,\dots,B_k$, with $G_i=(V_i,E_i)$, and let $M_i$ be the corresponding matchings, where $M_k$ is the final one and $M_0$ the expanded maximum matching of $G$.

2. Let $U$ be the set of Odd vertices at the end. These are vertices of $G_k$ that were never shrunk (blossoms consist of Even and Odd vertices and become Even), so $U\subseteq V$. By @thm-blossom-algorithm, $|M_k|=\frac12(|V_k|+|U|-o(G_k-U))$.

3. *Unshrinking one blossom keeps the equality.* Going from $G_i$ back to $G_{i-1}$ adds $|B_i|-1$ vertices, an even number, all to the component of $G_i-U$ containing the vertex of $B_i$; so the parities of the components, and $o(G_i-U)$, do not change. Meanwhile $|V_{i-1}|=|V_i|+|B_i|-1$ and $|M_{i-1}|=|M_i|+\frac12(|B_i|-1)$.

4. So both sides of $|M_i|=\frac12(|V_i|+|U|-o(G_i-U))$ grow by $\frac12(|B_i|-1)$, and by backward induction the equality holds for $i=0$: $M_0$ and $U$ attain the bound in $G$.

:::

::: {#cor-tutte-perfect-matching .corollary name="Tutte's theorem"}

A graph $G$ has a perfect matching if and only if $o(G-U)\le|U|$ for every $U\subseteq V$.

:::

::: {.proof}

$G$ has a perfect matching iff $\max_M|M|=\frac12|V|$. By @thm-tutte-berge this holds iff $\frac12(|V|+|U|-o(G-U))\ge\frac12|V|$ for all $U$, that is, iff $o(G-U)\le|U|$ for all $U$.

:::

::: {#exm-tutte-berge-star .example name="Three triangles on a centre"}

Take three triangles $\{1,2,3\}$, $\{4,5,6\}$, $\{7,8,9\}$ and a centre $10$ joined to $1$, $4$ and $7$. The graph is connected with $10$ vertices, so $U=\varnothing$ only gives the bound $5$. The matching $\{23,56,89,1\,10\}$ has $4$ edges, and $U=\{10\}$ proves it maximum: $G-U$ is three triangles, $o(G-U)=3$, and $\frac12(10+1-3)=4$. By Tutte's theorem the graph has no perfect matching.

:::

::: {#fig-tutte-berge-formula-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex, fill=accentLight, draw=accent] (c) at (0,0) {$10$};
\node[small vertex] (t1) at (0.0,1.1) {$1$};
\node[small vertex] (t2) at (-0.43,1.89) {$2$};
\node[small vertex] (t3) at (0.43,1.89) {$3$};
\draw[bold] (t2) -- (t3);
\draw[faint] (t1) -- (t2);
\draw[faint] (t1) -- (t3);
\draw[bold] (c) -- (t1);
\node[small vertex] (t4) at (-0.95,-0.55) {$4$};
\node[small vertex] (t5) at (-1.42,-1.32) {$5$};
\node[small vertex] (t6) at (-1.85,-0.57) {$6$};
\draw[bold] (t5) -- (t6);
\draw[faint] (t4) -- (t5);
\draw[faint] (t4) -- (t6);
\draw[faint] (c) -- (t4);
\node[small vertex] (t7) at (0.95,-0.55) {$7$};
\node[small vertex] (t8) at (1.85,-0.57) {$8$};
\node[small vertex] (t9) at (1.42,-1.32) {$9$};
\draw[bold] (t8) -- (t9);
\draw[faint] (t7) -- (t8);
\draw[faint] (t7) -- (t9);
\draw[faint] (c) -- (t7);
\end{tikzpicture}
\end{center}
```

The example: deleting $U=\{10\}$ (highlighted) leaves three odd triangles, so every matching has at most $\frac12(10+1-3)=4$ edges; the thick edges form such a matching.

:::

::: {#rmk-tutte-berge-formula-1 .remark name="Structure of the minimisers"}

For a minimiser $U$, every maximum matching matches each vertex of $U$ into a different odd component of $G-U$, matches the even components perfectly and each odd component up to one vertex (exercise). Choosing $U$ through the inessential vertices gives the canonical minimiser of the Edmonds–Gallai decomposition (exercise).

:::
