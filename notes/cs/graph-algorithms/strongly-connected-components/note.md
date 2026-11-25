---
title: "Strongly Connected Components"
sources: [res-clrs-strongly-connected-components]
requires: [cs/graph-algorithms/topological-sort]
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Section 22.5, in our own wording; proofs written out in steps. The example graphs are our own. -->

In an undirected graph, "connected to" is symmetric, and the connected components come out of one Full-DFS (@prp-connected-components-algorithm). In a directed graph, $v$ may be reachable from $u$ but not $u$ from $v$. The right notion of component asks for reachability in both directions, and two depth-first searches are enough to find all the components.

## Components and the component graph

::: {#def-strongly-connected .definition name="Strongly connected component"}

Let $G=(V,E)$ be a directed graph. Two vertices $u,v$ are *strongly connected*, written $u\leftrightarrow v$, if there is a walk from $u$ to $v$ and a walk from $v$ to $u$. The equivalence classes of $\leftrightarrow$ are the *strongly connected components* (SCCs) of $G$. The graph $G$ is *strongly connected* if it has one SCC.

:::

::: {#prp-strongly-connected-equivalence .proposition name="Strong connectivity is an equivalence relation"}

The relation $\leftrightarrow$ is reflexive, symmetric and transitive. So the SCCs partition $V$.

:::

::: {.proof}

1. *Reflexive.* The walk of length $0$ goes from $u$ to $u$.

2. *Symmetric.* The definition is symmetric in $u$ and $v$.

3. *Transitive.* If $u\leftrightarrow v$ and $v\leftrightarrow w$, join a walk $u\to v$ to a walk $v\to w$, and a walk $w\to v$ to a walk $v\to u$.

:::

::: {#def-component-graph .definition name="Component graph, transpose"}

The *component graph* $G^{\mathrm{SCC}}$ has one vertex for each SCC of $G$, and an edge from $C$ to $C'\ne C$ when $G$ has an edge from some vertex of $C$ to some vertex of $C'$. The *transpose* $G^{\mathsf T}$ has the same vertices as $G$ and the edge $(v,u)$ for every edge $(u,v)$ of $G$.

:::

::: {#lem-component-graph-dag .lemma name="The component graph is a DAG"}

1. $G^{\mathrm{SCC}}$ has no directed cycle.
2. $G$ and $G^{\mathsf T}$ have the same SCCs, and $(G^{\mathsf T})^{\mathrm{SCC}}$ is the transpose of $G^{\mathrm{SCC}}$.

:::

::: {.proof}

1. Suppose $G^{\mathrm{SCC}}$ had a cycle $C_0,C_1,\dots,C_k=C_0$ with $k\ge2$ and $C_0\ne C_1$. Each edge $C_i\to C_{i+1}$ comes from an edge of $G$, and inside each $C_i$ any two vertices are joined by walks. Joining these gives, for $u\in C_0$ and $v\in C_1$, a walk $u\to v$ (along the cycle to $C_1$) and a walk $v\to u$ (on round the cycle back to $C_0$).

2. So $u\leftrightarrow v$, and $C_0=C_1$, a contradiction.

3. A walk in $G$ reversed is a walk in $G^{\mathsf T}$, so $u$ reaches $v$ in $G$ exactly when $v$ reaches $u$ in $G^{\mathsf T}$. Hence $u\leftrightarrow v$ means the same in both graphs. An edge from $C$ to $C'$ in $G$ is an edge from $C'$ to $C$ in $G^{\mathsf T}$.

:::

::: {#fig-strongly-connected-components-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\fill[primaryLight, rounded corners] (-0.45,1.35) -- (1.95,1.35) -- (1.25,-0.85) -- (0.25,-0.85) -- cycle;
\fill[primaryLight, rounded corners] (2.55,0.45) rectangle (4.95,1.35);
\fill[primaryLight, rounded corners] (1.8,-1.35) rectangle (4.2,-0.45);
\fill[primaryLight, rounded corners] (5.1,-1.35) rectangle (6.0,-0.45);
\node[small vertex] (a) at (0.00,0.90) {$a$};
\node[small vertex] (b) at (1.50,0.90) {$b$};
\node[small vertex] (c) at (0.75,-0.40) {$c$};
\node[small vertex] (d) at (3.00,0.90) {$d$};
\node[small vertex] (e) at (4.50,0.90) {$e$};
\node[small vertex] (f) at (2.25,-0.90) {$f$};
\node[small vertex] (g) at (3.75,-0.90) {$g$};
\node[small vertex] (h) at (5.55,-0.90) {$h$};
\draw[trans] (a) -- (b);
\draw[trans] (b) -- (c);
\draw[trans] (c) -- (a);
\draw[trans] (b) -- (d);
\draw[trans] (d) to[bend left=20] (e);
\draw[trans] (e) to[bend left=20] (d);
\draw[trans] (c) -- (f);
\draw[trans] (f) to[bend left=20] (g);
\draw[trans] (g) to[bend left=20] (f);
\draw[trans] (e) -- (g);
\draw[trans] (e) -- (h);
\draw[trans] (g) -- (h);
\node[state] (C1) at (8.0,0.90) {$abc$};
\node[state] (C2) at (9.8,0.90) {$de$};
\node[state] (C3) at (8.0,-0.90) {$fg$};
\node[state] (C4) at (9.8,-0.90) {$h$};
\draw[trans] (C1) -- (C2);
\draw[trans] (C1) -- (C3);
\draw[trans] (C2) -- (C3);
\draw[trans] (C2) -- (C4);
\draw[trans] (C3) -- (C4);
\node[lab] at (2.75,-1.85) {$G$ with its SCCs shaded};
\node[lab] at (8.9,-1.85) {$G^{\mathrm{SCC}}$};
\end{tikzpicture}
\end{center}
```

A directed graph with four SCCs, $\{a,b,c\}$, $\{d,e\}$, $\{f,g\}$ and $\{h\}$, and its component graph. Contracting each SCC to one vertex leaves a DAG (@lem-component-graph-dag).

:::

## Finishing times of components

Run Full-DFS on $G$ and number the vertices $1,2,\dots,|V|$ in the order in which their visits finish; call this number the *finishing position* $f(u)$. For a set $C$ of vertices let $f(C)=\max_{u\in C}f(u)$, the position of the last vertex of $C$ to finish.

::: {#lem-scc-finishing .lemma name="Edges between components go to earlier finishes"}

Let $C\ne C'$ be SCCs of $G$, and suppose $G$ has an edge from a vertex of $C$ to a vertex of $C'$. Then $f(C)>f(C')$ for every Full-DFS of $G$.

:::

::: {.proof}

Let $x$ be the first vertex of $C\cup C'$ that the search visits. When the visit of $x$ starts, every other vertex of $C\cup C'$ is unvisited.

1. *Case $x\in C$.* Every vertex of $C$ is reachable from $x$, and through the edge from $C$ to $C'$ so is every vertex of $C'$. As in the proof of @thm-dfs, all of them are visited during the visit of $x$, so they finish before $x$ does. Hence $f(C)=f(x)>f(C')$.

2. *Case $x\in C'$.* Every vertex of $C'$ is reachable from $x$, so all of $C'$ is visited and finishes during the visit of $x$, and $f(C')=f(x)$.

3. No vertex of $C$ is reachable from $x$. Otherwise a walk from $x$ into $C$, the edge from $C$ to $C'$ and a walk inside $C'$ back to $x$ would make $C$ and $C'$ strongly connected, so $C=C'$.

4. So no vertex of $C$ is visited during the visit of $x$. They are all still unvisited when $x$ finishes, and each finishes later. Hence $f(C)>f(x)=f(C')$.

:::

So if we list the SCCs by decreasing $f(C)$, every edge of $G^{\mathrm{SCC}}$ points forward: this is a topological order of the component graph, which extends @thm-dfs-topological-sort from DAGs to all directed graphs.

## The two-pass algorithm

::: {#thm-kosaraju .theorem name="SCCs by two depth-first searches"}

The following algorithm finds the SCCs of $G$ in $O(|V|+|E|)$ time.

1. Run Full-DFS on $G$ and record the finishing order.
2. Build $G^{\mathsf T}$.
3. Run Full-DFS on $G^{\mathsf T}$, taking the start vertices of the outer loop in decreasing order of $f$.

Each DFS tree of the second search consists of exactly the vertices of one SCC.

:::

::: {.proof}

1. *Time.* Two depth-first searches take $O(|V|+|E|)$ each, and $G^{\mathsf T}$ is built from the adjacency lists of $G$ in $O(|V|+|E|)$ time. Sorting by $f$ costs nothing extra: push each vertex onto a list when it finishes in step 1.

2. *Correctness.* We show by induction on $k$ that the first $k$ trees of the second search are SCCs. Before the first tree this holds trivially.

3. Suppose the first $k$ trees are SCCs, and the $(k+1)$-st tree starts at $u$, in the SCC $C$. The vertices visited so far form whole SCCs, and $u$ is unvisited, so all of $C$ is unvisited. Since $u$ comes first in decreasing order of $f$ among unvisited vertices, $f(C)=f(u)$, and $f(C)\ge f(C'')$ for every SCC $C''$ that is still unvisited.

4. In $G^{\mathsf T}$ every vertex of $C$ is reachable from $u$ (@lem-component-graph-dag), so the tree from $u$ contains all of $C$.

5. Let $(v,w)$ be an edge of $G^{\mathsf T}$ with $v\in C$ and $w$ in another SCC $C'$. Then $(w,v)$ is an edge of $G$ from $C'$ to $C$, so $f(C')>f(C)$ by @lem-scc-finishing. By step 3, $C'$ is not unvisited, so it is one of the earlier trees.

6. So the search from $u$ can leave $C$ only towards vertices that are already visited, and its tree is exactly $C$.

:::

```{=latex}
\begin{algorithm}
\caption{Strongly connected components (two passes)}
\begin{algorithmic}
\INPUT directed graph $G=(V,E)$ as adjacency lists
\OUTPUT the SCCs of $G$
\STATE run Full-DFS on $G$; push each vertex onto a stack $S$ when its visit finishes
\STATE build $G^{\mathsf T}$; mark every vertex unvisited
\WHILE{$S$ is not empty}
    \STATE $u\gets$ pop$(S)$
    \IF{$u$ is unvisited}
        \STATE run DFS from $u$ in $G^{\mathsf T}$; output the vertices it visits as one SCC
    \ENDIF
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#fig-strongly-connected-components-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0.00,0.90) {$a$};
\node[small vertex] (b) at (1.50,0.90) {$b$};
\node[small vertex] (c) at (0.75,-0.40) {$c$};
\node[small vertex] (d) at (3.00,0.90) {$d$};
\node[small vertex] (e) at (4.50,0.90) {$e$};
\node[small vertex] (f) at (2.25,-0.90) {$f$};
\node[small vertex] (g) at (3.75,-0.90) {$g$};
\node[small vertex] (h) at (5.55,-0.90) {$h$};
\draw[trans] (a) -- (b);
\draw[trans] (b) -- (c);
\draw[trans] (c) -- (a);
\draw[trans] (b) -- (d);
\draw[trans] (d) to[bend left=20] (e);
\draw[trans] (e) to[bend left=20] (d);
\draw[trans] (c) -- (f);
\draw[trans] (f) to[bend left=20] (g);
\draw[trans] (g) to[bend left=20] (f);
\draw[trans] (e) -- (g);
\draw[trans] (e) -- (h);
\draw[trans] (g) -- (h);
\node[lab,tick] at (-0.35,1.28) {$8$};
\node[lab,tick] at (1.50,1.38) {$7$};
\node[lab,tick] at (0.30,-0.62) {$4$};
\node[lab,tick] at (3.00,1.38) {$6$};
\node[lab,tick] at (4.50,1.38) {$5$};
\node[lab,tick] at (2.25,-1.38) {$3$};
\node[lab,tick] at (3.75,-1.38) {$2$};
\node[lab,tick] at (5.55,-1.38) {$1$};
\node[lab] at (2.75,-1.95) {pass 1 on $G$: finishing positions};
\begin{scope}[xshift=7.4cm]
\node[small vertex, fill=accentLight, draw=accent] (A) at (0.00,0.90) {$a$};
\node[small vertex] (B) at (1.50,0.90) {$b$};
\node[small vertex] (C) at (0.75,-0.40) {$c$};
\node[small vertex, fill=accentLight, draw=accent] (D) at (3.00,0.90) {$d$};
\node[small vertex] (E) at (4.50,0.90) {$e$};
\node[small vertex, fill=accentLight, draw=accent] (F) at (2.25,-0.90) {$f$};
\node[small vertex] (G) at (3.75,-0.90) {$g$};
\node[small vertex, fill=accentLight, draw=accent] (H) at (5.55,-0.90) {$h$};
\draw[trans, hl] (A) -- (C);
\draw[trans, hl] (C) -- (B);
\draw[trans] (B) -- (A);
\draw[trans] (D) -- (B);
\draw[trans, hl] (D) to[bend left=20] (E);
\draw[trans] (E) to[bend left=20] (D);
\draw[trans] (F) -- (C);
\draw[trans, hl] (F) to[bend left=20] (G);
\draw[trans] (G) to[bend left=20] (F);
\draw[trans] (G) -- (E);
\draw[trans] (H) -- (E);
\draw[trans] (H) -- (G);
\node[lab] at (2.75,-1.95) {pass 2 on $G^{\mathsf T}$: four trees};
\end{scope}
\end{tikzpicture}
\end{center}
```

The two passes on the graph of @fig-strongly-connected-components-1. Pass 1 (Full-DFS on $G$ from $a$, neighbours in alphabetical order) finishes the vertices in the order $h,g,f,c,e,d,b,a$. Pass 2 runs on the reversed graph and starts in the order $a,d,f,h$ (highlighted roots). Its tree edges (thick) give the trees $\{a,c,b\}$, $\{d,e\}$, $\{f,g\}$, $\{h\}$; every other edge leaving a tree goes into an earlier tree.

:::

::: {#rmk-strongly-connected-components-1 .remark name="One pass is enough"}

Tarjan's algorithm finds the SCCs with a single depth-first search. It records for each vertex the earliest vertex on the current DFS path that it can reach, and outputs an SCC when a vertex can reach nothing earlier than itself. The running time is also $O(|V|+|E|)$. The two-pass algorithm above is easier to prove correct.

:::

Once the SCCs are known, the component graph is built in $O(|V|+|E|)$ time, and many problems on general directed graphs reduce to a problem on the DAG $G^{\mathrm{SCC}}$, solved in topological order. Within one SCC every vertex reaches every other.
