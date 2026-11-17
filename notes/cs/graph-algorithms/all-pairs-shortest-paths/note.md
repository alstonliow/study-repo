---
title: "All-Pairs Shortest Paths: Johnson's Algorithm"
sources: [mit6006-14, mit6006r-14, mit6046-11]
requires: [cs/graph-algorithms/bellman-ford, cs/graph-algorithms/dijkstra]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 14 and Recitation 14, in our own wording; proofs written out in steps. -->

::: {#def-apsp .definition name="All-pairs shortest paths"}

*All-pairs shortest paths* (APSP): given a weighted directed graph $G=(V,E)$, return $\delta(u,v)$ for all $u,v\in V$, or report that $G$ has a negative-weight cycle.

:::

The output has $|V|^2$ entries, so running a single-source algorithm from every vertex is a reasonable plan: $|V|$ runs of BFS or DAG relaxation take $O(|V|(|V|+|E|))$, $|V|$ runs of Dijkstra take $O(|V|^2\log|V|+|V|\cdot|E|)$ for non-negative weights, and $|V|$ runs of Bellman–Ford take $O(|V|^2|E|)$. Johnson's algorithm gets the Dijkstra bound for arbitrary weights, by first making all weights non-negative without changing which paths are shortest.

Adding the same constant to every weight does not work: it penalises paths with many edges. What works is a *potential*.

::: {#lem-reweighting .lemma name="Reweighting by a potential"}

Let $h:V\to\mathbb Z$ be any function and set $w'(u,v)=w(u,v)+h(u)-h(v)$. Then for every walk $\pi$ from $v_0$ to $v_k$,
$$w'(\pi)=w(\pi)+h(v_0)-h(v_k).$$
So every walk from $v_0$ to $v_k$ changes weight by the same amount, the shortest paths for $w$ and $w'$ are the same, $\delta'(u,v)=\delta(u,v)+h(u)-h(v)$, and the closed walks have the same weight under both.

:::

::: {.proof}

$w'(\pi)=\sum_{i=1}^k\bigl(w(v_{i-1},v_i)+h(v_{i-1})-h(v_i)\bigr)=w(\pi)+h(v_0)-h(v_k)$, because the terms $h(v_1),\dots,h(v_{k-1})$ cancel in pairs (a telescoping sum). The rest follows by taking infima over the walks from $v_0$ to $v_k$, and by $v_0=v_k$ for closed walks.

:::

::: {#fig-all-pairs-shortest-paths-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0,0.8) {$a$};
\node[lab,tick] at (-0.85,0.8) {$h=-1$};
\node[small vertex] (b) at (1.8,0.8) {$b$};
\node[lab,tick] at (2.65,0.8) {$h=0$};
\node[small vertex] (c) at (1.8,-0.8) {$c$};
\node[lab,tick] at (2.65,-0.8) {$h=-3$};
\node[small vertex] (d) at (0,-0.8) {$d$};
\node[lab,tick] at (-0.85,-0.8) {$h=0$};
\draw[->] (a) -- node[edge label, pos=0.5] {$2$} (b);
\draw[->] (b) -- node[edge label, pos=0.5] {$-3$} (c);
\draw[->] (a) -- node[edge label, pos=0.5] {$4$} (d);
\draw[->] (d) -- node[edge label, pos=0.5] {$1$} (c);
\draw[->] (c) -- node[edge label, pos=0.5] {$2$} (a);
\node[small vertex] (a2) at (5.0,0.8) {$a$};
\node[small vertex] (b2) at (6.8,0.8) {$b$};
\node[small vertex] (c2) at (6.8,-0.8) {$c$};
\node[small vertex] (d2) at (5.0,-0.8) {$d$};
\draw[->] (a2) -- node[edge label, pos=0.5] {$1$} (b2);
\draw[->] (b2) -- node[edge label, pos=0.5] {$0$} (c2);
\draw[->] (a2) -- node[edge label, pos=0.5] {$3$} (d2);
\draw[->] (d2) -- node[edge label, pos=0.5] {$4$} (c2);
\draw[->] (c2) -- node[edge label, pos=0.5] {$0$} (a2);
\draw[emph,->] (3.0,0) -- (4.3,0);
\node[lab,tick] at (3.6,-0.35) {$w'=w+h(u)-h(v)$};
\end{tikzpicture}
\end{center}
```

Johnson's reweighting. Left: a graph with a negative edge and the potentials $h(v)=\delta(x,v)$ from an added source $x$. Right: the new weights $w'(u,v)=w(u,v)+h(u)-h(v)$ are all non-negative, and every path between two given vertices changes weight by the same amount.

:::

We want $h$ with $w'(u,v)\ge0$, that is $h(v)\le h(u)+w(u,v)$ for every edge. This is the triangle inequality of @lem-shortest-path-properties, satisfied by $h(v)=\delta(x,v)$ for any vertex $x$ from which all distances are finite.

::: {#def-johnson .definition name="Johnson's algorithm"}

1. Add a new vertex $x$ with an edge $(x,v)$ of weight $0$ to every $v\in V$.
2. Run Bellman–Ford from $x$. If some $\delta(x,v)=-\infty$, report a negative-weight cycle and stop.
3. Otherwise let $h(v)=\delta(x,v)$ and reweight: $w'(u,v)=w(u,v)+h(u)-h(v)$.
4. For each $u\in V$, run Dijkstra from $u$ with weights $w'$, and return $\delta(u,v)=\delta'(u,v)-h(u)+h(v)$.

:::

::: {#thm-johnson .theorem name="Johnson's algorithm"}

Johnson's algorithm solves APSP in $O(|V|^2\log|V|+|V|\cdot|E|)$ time.

:::

::: {.proof}

1. The new vertex $x$ has no incoming edges, so it lies on no cycle, and the cycles of the new graph are those of $G$. Every $v$ is reachable from $x$, with $\delta(x,v)\le0$. So some $\delta(x,v)=-\infty$ exactly when $G$ has a negative-weight cycle (reachable from $x$, which means anywhere), and Bellman–Ford detects this (@thm-bellman-ford).

2. Otherwise all $h(v)$ are finite, and $w'(u,v)=w(u,v)+\delta(x,u)-\delta(x,v)\ge0$ by the triangle inequality. So Dijkstra is correct for $w'$ (@thm-dijkstra), and @lem-reweighting converts $\delta'$ back to $\delta$.

3. *Time.* Bellman–Ford on the graph with $|V|+1$ vertices and $|E|+|V|$ edges takes $O(|V|(|V|+|E|))$. Reweighting takes $O(|E|)$. The $|V|$ runs of Dijkstra take $O(|V|(|V|\log|V|+|E|))$, and the conversion $O(|V|^2)$. The Dijkstra runs dominate.

:::

::: {#rmk-all-pairs-reductions .remark name="Reductions"}

The proof uses no new induction: it *reduces* APSP with arbitrary weights to APSP with non-negative weights, and relies on the correctness of Bellman–Ford and Dijkstra. For dense graphs the bound is $O(|V|^3)$, which the simpler Floyd–Warshall algorithm also achieves (@thm-floyd-warshall).

:::

## All pairs by matrix multiplication

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 11, in our own wording; proof written out in steps. -->

Let $V=\{1,\dots,n\}$ and let $W$ be the $n\times n$ matrix with $W_{uu}=0$, $W_{uv}=w(u,v)$ for edges and $\infty$ otherwise. Let $D^{(m)}_{uv}$ be the least weight of a walk from $u$ to $v$ with at most $m$ edges, so $D^{(1)}=W$.

::: {#def-min-plus-product .definition name="Min-plus product"}

The *min-plus product* of $n\times n$ matrices $A$ and $B$ is $(A\otimes B)_{uv}=\min_k(A_{uk}+B_{kv})$: ordinary matrix multiplication with $+$ replaced by $\min$ and $\times$ by $+$.

:::

::: {#prp-shortest-paths-by-squaring .proposition name="Shortest paths by repeated squaring"}

$D^{(a+b)}=D^{(a)}\otimes D^{(b)}$. Hence, if $G$ has no negative-weight cycle, $\delta=D^{(n-1)}$ is computed by $\lceil\log_2(n-1)\rceil$ squarings $W,W^{\otimes2},W^{\otimes4},\dots$, in $O(n^3\log n)$ time.

:::

::: {.proof}

1. A walk from $u$ to $v$ with at most $a+b$ edges splits at some vertex $k$ into a walk with at most $a$ edges and one with at most $b$ (pad with the $0$-weight steps $W_{kk}=0$ if needed); conversely such pairs join into such a walk. Taking minima gives the product formula.

2. Without negative cycles, shortest walks can be taken with at most $n-1$ edges (@lem-simple-shortest-paths), so $D^{(m)}=\delta$ for every $m\ge n-1$; squaring overshoots harmlessly.

3. Each product takes $O(n^3)$ time, and there are $O(\log n)$ of them.

:::

The min-plus product has no subtraction, so Strassen's trick (@thm-strassen) does not apply directly. Floyd–Warshall (@thm-floyd-warshall) gets $O(n^3)$, and Johnson's algorithm $O(n^2\log n+n|E|)$; but the matrix view gives *transitive closure* (is there a path?) by Boolean matrix multiplication, which can use fast matrix multiplication, in $O(n^{\omega}\log n)$ time with $\omega<2.38$.
