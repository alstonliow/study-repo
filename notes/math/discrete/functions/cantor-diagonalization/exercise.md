::: {.problem #prob-cs70hw-8-q1 origin="external" source="cs70hw-8-q1"}
**Countability Proof Practice.**

(a) A disk is a 2D region of the form $\{(x, y) \in \mathbb{R}^2 : (x - x_0)^2 + (y - y_0)^2 \le r^2\}$, for some $x_0, y_0, r \in \mathbb{R}$, $r > 0$. Say you have a set of disks in $\mathbb{R}^2$ such that none of the disks overlap. Is this set always countable, or potentially uncountable?

(Hint: Attempt to relate it to a set that we know is countable, such as $\mathbb{Q} \times \mathbb{Q}$)

(b) A circle is a subset of the plane of the form $\{(x, y) \in \mathbb{R}^2 : (x - x_0)^2 + (y - y_0)^2 = r^2\}$ for some $x_0, y_0, r \in \mathbb{R}$, $r > 0$. Now say you have a set of circles in $\mathbb{R}^2$ such that none of the circles overlap. Is this set always countable, or potentially uncountable?

(Hint: The difference between a circle and a disk is that a disk contains all of the points in its interior, whereas a circle does not.)

(c) Is the set containing all increasing functions $f: \mathbb{N} \to \mathbb{N}$ (i.e., if $x \ge y$, then $f(x) \ge f(y)$) countable or uncountable? Prove your answer.

(d) Is the set containing all decreasing functions $f: \mathbb{N} \to \mathbb{N}$ (i.e., if $x \ge y$, then $f(x) \le f(y)$) countable or uncountable? Prove your answer.
:::

::: {.problem #prob-cs70hw-8-q3 origin="external" source="cs70hw-8-q3"}
**Finite and Infinite Graphs.** The graph material that we learned in lecture still applies if the set of vertices of a graph is infinite. We thus make a distinction between finite and infinite graphs: a graph $G = (V, E)$ is finite if $V$ and $E$ are both finite. Otherwise, the graph is infnite. As examples, consider the graphs

- $G_1 = (V = \mathbb{Z}, E = \{(i, j) \in \mathbb{Z} \times \mathbb{Z} \mid |i - j| = 1\})$
- $G_2 = (V = \mathbb{Z}, E = \{(i, j) \in \mathbb{Z} \times \mathbb{Z} \mid i < j\})$
- $G_3 = (V = \mathbb{Z}^2, E = \{((i, j), (k, l)) \in \mathbb{Z}^2 \times \mathbb{Z}^2 \mid (i = k \land |j - l| = 1) \lor (j = l \land |i - k| = 1)\})$

Observe that $G_1$ is a line of integers, $G_2$ is a complete graph over all integers, and $G_3$ is an grid of integers. Prove whether the following sets of graphs are countable or uncountable

(a) The set of all finite graphs $G = (V, E)$, for $V \subseteq \mathbb{N}$

(b) The set of all infinite graphs over a fixed, countably infinite set of vertices (in other words, they all have the same vertex set).

(c) The set of all graphs over a fixed, countably infinite set of vertices, the degree of each vertex is exactly two. For instance, every vertex in $G_1$ (defined above) has degree 2.

(Hint: if $V$ is a countably infinite set, then the set of bijections $f: V \to V$ is uncountable. You may use this fact without proof.)

(d) We say that graphs $G = (V, E)$ and $G' = (V', E')$ are isomorphic if the exists some bijection $f: V \to V'$ such that $(u, v) \in V$ iff $(f(u), f(v)) \in V'$. Such a bijection $f$ is called a graph isomorphism. Suppose we consider two graphs to be the equivalent if they are isomorphic. The idea is that if we relabel the vertices of a graph, it is still the same graph. Using this definition of "being the same graph", can you conclude that the set of trees over countably infinite vertices is countable?

(Hint: Begin by showing that for any graph isomorphism $f$, and any vertex $v$, $f(v)$ and $v$ have the same degree)

*Note (these notes):* In (d), $(u,v)\in V$ should read $(u,v)\in E$, and similarly $V'$ should read $E'$.
:::
