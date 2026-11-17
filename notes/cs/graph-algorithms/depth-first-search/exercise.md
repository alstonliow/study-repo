::: {.problem #prob-mit6006s20-5-q1 origin="external" source="mit6006s20-5-q1"}
**Graph Practice**

(a) Draw the undirected graph described on the right by **adjacency matrix** `Adj`: a direct access array Set mapping each vertex $u\in\{0,\dots,5\}$ to an adjacency list `Adj[u]`, where each adjacency list is also implemented using a direct access array Set such that `Adj[u][v] = 1` if and only if vertices `u` and `v` are connected by an edge.

```python
#       0  1  2  3  4  5
Adj = [[0, 0, 1, 0, 0, 0],  # 0
       [0, 0, 0, 1, 1, 1],  # 1
       [1, 0, 0, 1, 1, 0],  # 2
       [0, 1, 1, 0, 0, 0],  # 3
       [0, 1, 1, 0, 0, 1],  # 4
       [0, 1, 0, 0, 1, 0]]  # 5
```

(b) Write down the adjacency list representation of the graph on the right: where a Python Dictionary maps each vertex `v` to its adjacency list `Adj[v]`, and each adjacency list is a Python List containing `v`'s outgoing neighbors **listed in alphabetical order**.

```{=latex}
\begin{center}
\begin{tikzpicture}[graph, x=1.1cm, y=1.1cm]
\node (A) at (0,0) {$A$}; \node (B) at (1.2,0) {$B$};
\node (C) at (2.4,0.6) {$C$}; \node (E) at (3.6,0.6) {$E$};
\node (D) at (2.4,-0.6) {$D$}; \node (F) at (3.6,-0.6) {$F$};
\draw[->] (A)--(B); \draw[->] (B)--(C); \draw[->] (B)--(D);
\draw[->] (C)--(E); \draw[->] (C)--(F); \draw[->] (D)--(E);
\draw[->] (D)--(F); \draw[->] (F)--(E); \draw[->] (F) to[bend left=40] (D);
\end{tikzpicture}
\end{center}
```

(c) Run both BFS and DFS on the graph from part (b), starting from node A. While performing each search, visit the outgoing neighbors of a vertex in alphabetical order. For each search, draw the resulting tree and list vertices in the order in which they were first visited.

(d) It is possible to remove a single edge from the graph in (b) to make it a DAG. State every edge with this property, and for each, state a topological sort order of the resulting DAG.

*Note (these notes):* The directed graph of part (b), drawn in the original, is redrawn here.
:::

::: {.problem #prob-mit6006s20-5-q2 origin="external" source="mit6006s20-5-q2"}
**Power Plants**

The Boston electrical network contains $n$ power plants and $n^2$ buildings, pairs of which may be directly connected to each other via bidirectional wires. Every building is powered by either: having a wire directly to a power plant, or having a wire to another building that is recursively powered. Note that the network has the property that no building could be powered by more than one power plant (or else accounting would be ambiguous). Boston has secured funds to install an emergency generator in one of the power plants, which would provide backup power to all buildings powered by it, were the power plant to fail. Given a list $W$ of all the wires in the network, describe an $O(n^4)$-time algorithm to determine the power plant where Boston should install the generator that would provide backup power to the most buildings upon plant failure.
:::
