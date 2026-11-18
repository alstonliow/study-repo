::: {.problem #prob-mit6006s20-6-q1 origin="external" source="mit6006s20-6-q1"}
**Dijkstra Practice**

Consider weighted graph $G=(V,E,w)$ below, which is acyclic and has nonnegative edge weights.

```{=latex}
\begin{center}
\begin{tikzpicture}[graph, x=1.3cm, y=1.3cm]
\node (a) at (0,1) {$a$}; \node (b) at (1,1) {$b$}; \node (c) at (2,1) {$c$};
\node (d) at (0,0) {$d$}; \node (e) at (1,0) {$e$}; \node (f) at (2,0) {$f$};
\draw[->] (a) -- node[edge label, above] {$2$} (b);
\draw[->] (b) -- node[edge label, above] {$1$} (c);
\draw[->] (a) -- node[edge label, left] {$6$} (d);
\draw[->] (d) -- node[edge label, pos=0.35, above left] {$1$} (b);
\draw[->] (b) -- node[edge label, left] {$3$} (e);
\draw[->] (b) -- node[edge label, pos=0.35, above right] {$2$} (f);
\draw[->] (f) -- node[edge label, right] {$1$} (c);
\draw[->] (d) -- node[edge label, below] {$0$} (e);
\draw[->] (e) -- node[edge label, below] {$2$} (f);
\end{tikzpicture}
\end{center}
```

(a) Run both DAG Relaxation and Dijkstra on $G$ from vertex $a$. Each algorithm tries to relax every edge $(u,v)\in E$, but does so in a different order. For each algorithm, write down a list of all edges in **relaxation order**: the order the algorithm tries to relax them. If there is ambiguity on which vertex or outgoing adjacency to process next, process them in **alphabetical order**.

(b) List $\delta(a,v)$ for each $v\in V$ (via either algorithm).

*Note (these notes):* The graph, drawn in the original, is redrawn here.
:::

::: {.problem #prob-mit6006s20-6-q5 origin="external" source="mit6006s20-6-q5"}
**SparkPlug Derby**

LightQueen McNing is a race car that wants to drive to California to compete in a road race: the annual SparkPlug Derby. She has a map depicting:

- the $n$ intersections in the country, where each intersection $x_i$ is marked with its positive integer elevation $e_i$ and whether it contains a gas station; and
- the $r$ roads connecting pairs of them, where each road $r_j$ is marked with the positive integer $t_j$ denoting the driving time it will take LightQueen to drive along it in either direction.

Some intersections connect to many roads, but the average number of roads at any intersection is less than 5. LightQueen needs to get from Carburetor Falls at intersection $s$ to the SparkPlug Derby race track at intersection $t$, subject to the following conditions:

- LightQueen's gas tank has a positive integer capacity $g<n$: it can hold up to $g$ units of gas at a time (starting full). Along the way, she can refill her tank (by any integer amount) at any intersection marked with a gas station. It takes exactly $t_G$ time for her to fill up 1 unit of gas.
- LightQueen uses gas only when driving uphill. Specifically, if she drives on a road from intersection $x_i$ to $x_j$ at elevations $e_i$ and $e_j$ respectively, LightQueen will use exactly $e_j-e_i$ units of gas to travel along it if $e_j>e_i$, and will use zero units of gas otherwise.

Given LightQueen's map, describe an $O(n^2\log n)$-time algorithm to return a fastest route to the race that keeps a strictly positive amount of gas in her tank at all times (if such a route exists).
:::

::: {.problem #prob-mit6006r-13-q2 origin="external" source="mit6006r-13-q2"}
CIA officer Mary Cathison needs to drive to meet with an informant across an unwelcome city. Some roads in the city are equipped with government surveillance cameras, and Mary will be detained if cameras from more than one road observe her car on the way to her informant. Mary has a map describing the length of each road and the locations and ranges of surveillance cameras. Help Mary find the shortest drive to reach her informant, being seen by at most one surveillance camera along the way.
:::
