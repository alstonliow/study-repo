::: {.problem #prob-mit6046s15-6-q2 origin="external" source="mit6046s15-6-q2"}
**Minimum Spanning Trees with Unique Edge Weights**

Consider an undirected graph $G=(V,E)$ with a weight function $w$ providing nonnegative real-valued weights, such that the weights of all the edges are different.

(a) Prove that, under the given uniqueness assumption, $G$ has a unique Minimum Spanning Tree.

Each of the next three parts outlines an MST algorithm for graphs with unique edge weights. In each case, say whether this is a correct MST algorithm or not. If so, give a proof, a more detailed description of an efficient algorithm, and an analysis. If not, give a specific counterexample. (We are omitting the point values for these parts because we will assign more points to algorithms and fewer to counterexamples.)

(b) [Batched Edge-Addition MST] The algorithm maintains a set $A$ of edges that are known to be in the MST. Initially, $A$ is empty. The algorithm operates in phases; in each, it adds a batch of one or more edges to $A$. Phases continue until we have a spanning tree.

Specifically, in each phase, the algorithm does the following: For each component tree $C$ in the forest formed by $A$, identify the lightest weight edge $e_C$ crossing the cut between $C$ and the rest of the components. After determining these edges for all component trees, add all of the edges $e_C$ to $A$, in one batch.

(c) [Divide-and-Conquer MST] The algorithm uses a simple Divide-and-Conquer strategy: Divide the set $V$ of vertices arbitrarily into disjoint sets $V_1$ and $V_2$, each of size roughly $V/2$. Define graph $G_1=(V_1,E_1)$, where $E_1$ is the subset of $E$ for which both endpoints are in $V_1$. Define $G_2=(V_2,E_2)$ analogously.

Recursively find (unique) MSTs for both $G_1$ and $G_2$; call them $T_1$ and $T_2$. Then find the (unique) lightest edge that crosses the cut between the two sets of vertices $V_1$ and $V_2$, and add that to form the final spanning tree $T$.

(d) [Cycle-Breaking MST] The algorithm operates in phases. In each phase, the algorithm first finds some nonempty subset of the simple cycles in the graph. Then it identifies the heaviest edge on each cycle, and removes all these heavy edges. Phases continue until we have a spanning tree.
:::
