---
title: "Global Minimum Cut: the Stoer–Wagner Algorithm"
sources: [mit18433-4]
requires: [cs/graph-optimization/ford-fulkerson]
status: draft
---

<!-- Added 2026-11-26 from MIT 18.433 (Spring 2015), lecture notes on flows and cuts (Section 4.4), in our own wording; example our own (checked by brute force over all cuts); proofs written out in steps. -->

Let $G=(V,E)$ be an undirected graph with capacities $u_e\ge0$, $n=|V|$, and for $S\subseteq V$ let $u(\delta(S))$ be the total capacity of the edges with one end in $S$. The *global minimum cut* problem asks for $\varnothing\ne S\ne V$ minimising $u(\delta(S))$; its value is the edge connectivity when all capacities are $1$.

::: {#prp-global-cut-by-flows .proposition name="Global minimum cut by $n-1$ flows"}

Fix any vertex $s$. A global minimum cut of an undirected graph is a minimum $s$–$t$ cut for some $t\ne s$, so $n-1$ maximum flow computations (@thm-max-flow-min-cut, each edge replaced by two opposite arcs) find it. In a directed graph, $2(n-1)$ computations ($s$–$t$ and $t$–$s$ for each $t$) find a minimum of $u(\delta^+(S))$.

:::

::: {.proof}

A global minimum cut $S$ has $s$ on one side and some $t$ on the other; it is then a minimum $s$–$t$ cut, and every $s$–$t$ cut is a cut. In the undirected case $\delta(S)=\delta(V\setminus S)$, so it does not matter which side contains $s$.

:::

The algorithm below avoids flows altogether. For vertex sets $A,B$ write $u(A:B)$ for the total capacity of the edges between $A$ and $B$.

::: {#def-stoer-wagner .definition name="Stoer–Wagner algorithm"}

1. *Maximum adjacency order.* Pick any $v_1$, put $S=\{v_1\}$, and for $i=2,\dots,n$ let $v_i$ be a vertex outside $S$ maximising $u(S:\{v\})$, then add it to $S$.
2. The *cut of the phase* is $\delta(\{v_n\})$.
3. If $n=2$, return it. Otherwise merge $v_{n-1}$ and $v_n$ into one vertex (adding the capacities of parallel edges), solve the smaller instance recursively, and return the better of its answer and the cut of the phase.

:::

```{=latex}
\begin{algorithm}
\caption{Stoer--Wagner global minimum cut}
\begin{algorithmic}
\INPUT undirected graph $G$ with capacities $u\ge0$, $|V(G)|\ge2$
\OUTPUT a global minimum cut
\STATE $best\gets$ none
\WHILE{$G$ has at least $2$ vertices}
\STATE $S\gets\{v_1\}$ for any vertex $v_1$
\WHILE{$S\ne V(G)$}
\STATE add to $S$ a vertex $v\notin S$ maximising $u(S:\{v\})$
\ENDWHILE
\STATE let $v_{n-1},v_n$ be the last two vertices added
\STATE $best\gets$ the better of $best$ and $\delta(\{v_n\})$ (in terms of original vertices)
\STATE merge $v_{n-1}$ and $v_n$
\ENDWHILE
\RETURN $best$
\end{algorithmic}
\end{algorithm}
```

The key fact is that each phase finds a minimum cut between its last two vertices, although these are not known in advance.

::: {#lem-maximum-adjacency-cut .lemma name="The cut of the phase"}

In a maximum adjacency order $v_1,\dots,v_n$, the cut $\delta(\{v_n\})$ is a minimum $v_{n-1}$–$v_n$ cut.

:::

::: {.proof}

1. Let $A_i=\{v_1,\dots,v_{i-1}\}$, and let $C$ be any set with $v_{n-1}\in C$, $v_n\notin C$. We show $u(\delta(C))\ge u(A_n:\{v_n\})=u(\delta(\{v_n\}))$.

2. Call $v_i$ ($i\ge2$) *critical* if exactly one of $v_{i-1}$, $v_i$ lies in $C$; then $v_n$ is critical. Put $C_i=(A_i\cup\{v_i\})\cap C$. We prove by induction over the critical vertices that
$$u(A_i:\{v_i\})\le u\big(C_i:(A_i\cup\{v_i\})\setminus C_i\big),$$
the right side being the capacity of the edges of $\delta(C)$ inside $A_i\cup\{v_i\}$.

3. For the first critical vertex $v_i$, all of $v_1,\dots,v_{i-1}$ lie on one side of $C$ and $v_i$ on the other, so both sides equal $u(A_i:\{v_i\})$.

4. Let $v_i$ be critical and $v_j$ the next critical vertex, $j>i$. Then
$$u(A_j:\{v_j\})=u(A_i:\{v_j\})+u(A_j\setminus A_i:\{v_j\})\le u(A_i:\{v_i\})+u(A_j\setminus A_i:\{v_j\}).$$
The inequality holds because $v_i$ was chosen when $S=A_i$, so it was at least as tightly connected to $A_i$ as $v_j$.

5. By induction the first term is at most the capacity of the edges of $\delta(C)$ inside $A_i\cup\{v_i\}$. The vertices $v_i,\dots,v_{j-1}$ are on one side of $C$ (none of $v_{i+1},\dots,v_{j-1}$ is critical) and $v_j$ on the other, so every edge from $A_j\setminus A_i=\{v_i,\dots,v_{j-1}\}$ to $v_j$ is in $\delta(C)$, and these edges are new. Together this is at most the capacity of the edges of $\delta(C)$ inside $A_j\cup\{v_j\}$.

6. Applying this to $v_n$, with $A_n\cup\{v_n\}=V$, gives $u(\delta(\{v_n\}))=u(A_n:\{v_n\})\le u(\delta(C))$.

:::

::: {#thm-stoer-wagner .theorem name="Stoer–Wagner"}

The algorithm returns a global minimum cut. With a Fibonacci heap each phase takes $O(|E|+n\log n)$ time, so the total time is $O(n|E|+n^2\log n)$.

:::

::: {.proof}

1. Induct on $n$. A global minimum cut either separates $v_{n-1}$ from $v_n$, in which case the cut of the phase is at least as good by @lem-maximum-adjacency-cut, or it does not; then it is a cut of the merged graph, which the recursive call finds by induction.

2. A phase is like Prim's algorithm (@def-prim) with keys $u(S:\{v\})$ increased instead of decreased, so $n$ extractions and $|E|$ key changes; there are $n-1$ phases.

:::

::: {#exm-stoer-wagner-small .example name="Four vertices"}

Take capacities $u_{12}=2$, $u_{13}=3$, $u_{23}=1$, $u_{24}=3$, $u_{34}=1$.

1. Phase 1 from $v_1=1$: vertex $3$ (weight $3$ to $\{1\}$), then $2$ (weight $2+1=3$ against $0+1$ for $4$), then $4$. Cut of the phase $\delta(\{4\})$ of capacity $3+1=4$. Merge $2$ and $4$.
2. Phase 2 on $1$, $3$, $\{2,4\}$ (with $u(3,\{2,4\})=1+1=2$, $u(1,\{2,4\})=2$): order $1,3,\{2,4\}$, cut $\delta(\{2,4\})$ of capacity $2+2=4$. Merge.
3. Phase 3: the cut $\delta(\{1\})$ has capacity $5$.

The answer is $4$, and checking all $7$ cuts confirms it ($\{4\}$ and $\{2,4\}$ attain it).

:::

::: {#fig-global-minimum-cut-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (s1) at (0,1.4) {$1$};
\node[small vertex] (s2) at (1.6,1.4) {$2$};
\node[small vertex] (s3) at (0,0) {$3$};
\node[small vertex, fill=accentLight, draw=accent] (s4) at (1.6,0) {$4$};
\draw[emph] (s1) -- node[edge label] {$2$} (s2);
\draw[emph] (s1) -- node[edge label] {$3$} (s3);
\draw[emph] (s2) -- node[edge label] {$1$} (s3);
\draw[hl] (s2) -- node[edge label] {$3$} (s4);
\draw[hl] (s3) -- node[edge label] {$1$} (s4);
\node[lab, right] at (2.3,1.1) {phase 1 order: $1,3,2,4$};
\node[lab, right] at (2.3,0.6) {cut of the phase: $\delta(\{4\})=4$};
\end{tikzpicture}
\end{center}
```

The example: the maximum adjacency order from vertex $1$ ends with $2,4$, and the cut $\delta(\{4\})$ (highlighted edges, capacity $3+1=4$) is a minimum $2$–$4$ cut and a global minimum cut.

:::

::: {#rmk-global-minimum-cut-1 .remark name="Other algorithms"}

Hao and Orlin compute all $n-1$ flows of @prp-global-cut-by-flows in the time of one push–relabel maximum flow, $O(n|E|\log(n^2/|E|))$. Karger's randomised contraction algorithms (Karger–Stein, $O(n^2\log^3n)$, and later near-linear time) are another approach.

:::
