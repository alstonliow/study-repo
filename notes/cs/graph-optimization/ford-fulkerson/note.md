---
title: "The Ford–Fulkerson Method"
sources: [mit6046-13, mit6046-14, mit6046r-7]
requires: [cs/graph-optimization/maximum-flow, cs/graph-algorithms/breadth-first-search]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lectures 13-14 and Recitation 7, in our own wording; example our own (checked by computation); proofs written out in steps. Split from cs/graph-optimization/maximum-flow on 2026-11-25 (one algorithm per note, SPEC §8.6); Edmonds–Karp, which changes one choice, stays here. -->

The Ford–Fulkerson method finds a maximum flow (@def-flow-network) by pushing flow along augmenting paths (@def-residual-network) until none is left; by max-flow min-cut (@thm-max-flow-min-cut) the flow is then maximum.

::: {#def-ford-fulkerson .definition name="Ford–Fulkerson method"}

Start with $f=0$. While $G_f$ has an augmenting path $p$, push $c_f(p)$ along it. The *Edmonds–Karp* algorithm chooses a shortest augmenting path (fewest edges), found by BFS.

:::

```{=latex}
\begin{algorithm}
\caption{Ford–Fulkerson method (Edmonds–Karp)}
\begin{algorithmic}
\INPUT Flow network $G=(V,E,c)$, source $s$, sink $t$
\OUTPUT A maximum flow $f$
\STATE $f(u,v)\gets0$ for all $u,v$
\COMMENT{Edmonds–Karp: always take a shortest augmenting path, found by BFS}
\WHILE{$G_f$ has a path $p$ from $s$ to $t$}
    \STATE $c_f(p)\gets\min\{c(u,v)-f(u,v):(u,v)\in p\}$
    \FOR{$(u,v)\in p$}
        \STATE $f(u,v)\gets f(u,v)+c_f(p)$; $f(v,u)\gets f(v,u)-c_f(p)$
    \ENDFOR
\ENDWHILE
\RETURN $f$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-maximum-flow-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s0) at (0.00,0.00) {$s$};
\node[small vertex] (a0) at (1.40,0.80) {$a$};
\node[small vertex] (b0) at (1.40,-0.80) {$b$};
\node[small vertex] (t0) at (2.80,0.00) {$t$};
\draw[->, hl] (s0) -- node[edge label, pos=0.5] {$3$} (a0);
\draw[->] (s0) -- node[edge label, pos=0.5] {$2$} (b0);
\draw[->] (a0) -- node[edge label, pos=0.5] {$1$} (b0);
\draw[->, hl] (a0) -- node[edge label, pos=0.5] {$2$} (t0);
\draw[->] (b0) -- node[edge label, pos=0.5] {$3$} (t0);
\node[lab,tick] at (1.40,1.55) {push $2$ along $s,a,t$};
\node[small vertex] (s1) at (3.60,0.00) {$s$};
\node[small vertex] (a1) at (5.00,0.80) {$a$};
\node[small vertex] (b1) at (5.00,-0.80) {$b$};
\node[small vertex] (t1) at (6.40,0.00) {$t$};
\draw[->] (s1) to[bend left=25] node[edge label, pos=0.5] {$1$} (a1);
\draw[->, hl] (s1) -- node[edge label, pos=0.5] {$2$} (b1);
\draw[->] (a1) to[bend left=25] node[edge label, pos=0.5] {$2$} (s1);
\draw[->] (a1) -- node[edge label, pos=0.5] {$1$} (b1);
\draw[->, hl] (b1) -- node[edge label, pos=0.5] {$3$} (t1);
\draw[->] (t1) -- node[edge label, pos=0.5] {$2$} (a1);
\node[lab,tick] at (5.00,1.55) {push $2$ along $s,b,t$};
\node[small vertex] (s2) at (7.20,0.00) {$s$};
\node[small vertex] (a2) at (8.60,0.80) {$a$};
\node[small vertex] (b2) at (8.60,-0.80) {$b$};
\node[small vertex] (t2) at (10.00,0.00) {$t$};
\draw[->, hl] (s2) to[bend left=25] node[edge label, pos=0.5] {$1$} (a2);
\draw[->] (a2) to[bend left=25] node[edge label, pos=0.5] {$2$} (s2);
\draw[->, hl] (a2) -- node[edge label, pos=0.5] {$1$} (b2);
\draw[->] (b2) -- node[edge label, pos=0.5] {$2$} (s2);
\draw[->, hl] (b2) to[bend left=25] node[edge label, pos=0.5] {$1$} (t2);
\draw[->] (t2) -- node[edge label, pos=0.5] {$2$} (a2);
\draw[->] (t2) to[bend left=25] node[edge label, pos=0.5] {$2$} (b2);
\node[lab,tick] at (8.60,1.55) {push $1$ along $s,a,b,t$};
\node[small vertex] (s3) at (10.80,0.00) {$s$};
\node[small vertex] (a3) at (12.20,0.80) {$a$};
\node[small vertex] (b3) at (12.20,-0.80) {$b$};
\node[small vertex] (t3) at (13.60,0.00) {$t$};
\draw[->] (a3) -- node[edge label, pos=0.5] {$3$} (s3);
\draw[->] (b3) -- node[edge label, pos=0.5] {$2$} (s3);
\draw[->] (b3) -- node[edge label, pos=0.5] {$1$} (a3);
\draw[->] (t3) -- node[edge label, pos=0.5] {$2$} (a3);
\draw[->] (t3) -- node[edge label, pos=0.5] {$3$} (b3);
\node[lab,tick] at (12.20,1.55) {no augmenting path};
\end{tikzpicture}
\end{center}
```

Ford–Fulkerson on @exm-max-flow-small, choosing shortest augmenting paths as Edmonds–Karp does. Each panel is the residual network $G_f$ (labels are residual capacities) with the augmenting path highlighted. After pushing $2$, $2$ and $1$ units, $t$ is unreachable from $s$, and the flow of value $5$ is maximum; the vertices reachable from $s$, here only $s$, give the minimum cut of @fig-maximum-flow-1.

:::

::: {#cor-integral-flow .corollary name="Integrality"}

If all capacities are integers, Ford–Fulkerson ends with an integer maximum flow, after at most $|f^*|$ augmentations, each found in $O(|E|)$ time.

:::

::: {.proof}

By induction every flow and residual capacity stays an integer, so each augmentation adds at least $1$ to the value, and the value is bounded by the maximum $|f^*|$. When the loop stops there is no augmenting path, so the flow is maximum by @thm-max-flow-min-cut.

:::

With irrational capacities the plain method may not even terminate, and with bad path choices it can take $|f^*|$ steps on a graph with only four vertices. Shortest augmenting paths avoid both problems.

::: {#thm-edmonds-karp .theorem name="Edmonds–Karp"}

Edmonds–Karp performs $O(|V||E|)$ augmentations, so it runs in $O(|V||E|^2)$ time.

:::

::: {.proof}

1. *Monotonicity.* Let $\delta(v)$ be the BFS distance from $s$ in $G_f$. After an augmentation along a shortest path, no distance decreases: new residual edges $(v,u)$ appear only where flow was pushed along $(u,v)$ on a shortest path, so $\delta(v)=\delta(u)+1$ and the new edge goes *backwards* in distance; an induction on the new distances shows $\delta'(v)\ge\delta(v)$ for all $v$.

2. *Critical edges.* In each augmentation some edge $(u,v)$ of the path has $c_f(u,v)=c_f(p)$ and disappears. At that moment $\delta(v)=\delta(u)+1$. It can reappear only after $(v,u)$ lies on a later shortest augmenting path, when $\delta'(u)=\delta'(v)+1\ge\delta(v)+1=\delta(u)+2$.

3. So between two times that $(u,v)$ is critical, $\delta(u)$ grows by at least $2$; as $\delta(u)\le|V|$, each of the $O(|E|)$ residual edges is critical $O(|V|)$ times, and each augmentation has a critical edge: $O(|V||E|)$ augmentations, each costing $O(|E|)$ for BFS.

:::
