<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-graph-2-01 origin="external" source="fit1058-cn-12.7-q1"}
Draw all trees that have six vertices (every tree on six vertices should be
identical to one in your set, up to relabelling and redrawing).
:::

::: {.problem #prob-graph-2-02 origin="external" source="fit1058-cn-12.7-q2"}
The *diameter* of a graph is the length of the longest path in it.
Prove that every tree of diameter $\ge3$ has a vertex $v$ such that
$$2\le\deg(v)\le n-2,$$
where $n$ is the number of vertices.
:::

::: {.problem #prob-graph-2-03 origin="external" source="fit1058-cn-12.7-q3"}
If a tree has $k$ vertices of degree 3 and all other vertices are leaves, how
many leaves does it have?
:::

::: {.problem #prob-graph-2-04 origin="external" source="fit1058-cn-12.7-q4"}
(a) Prove that every tree with at least three vertices has a vertex of
    degree at least 2.

(b) Is there a number $N$ such that every tree with at least $N$
    vertices has a vertex of degree at least 3?
:::

::: {.problem #prob-graph-2-05 origin="external" source="fit1058-cn-12.7-q5"}
Prove that a graph $G$ is a tree if and only if for every pair $u,v$ of
vertices, there is a unique path between them in $G$.
:::

::: {.problem #prob-graph-2-06 origin="external" source="fit1058-cn-12.7-q6"}
Give an upper bound on the average degree of a tree.
:::

::: {.problem #prob-cs70-5-q2 origin="external" source="cs70-5.5-q2"}
In this question, we complete the induction component of the proof of Theorem 5.4.

(a) Suppose in the proof that $G'$ has two distinct connected components $G'_1$ and $G'_2$. Complete the inductive step to show that $G$ is connected and has $n - 1$ edges. (Hint: Argue that you can apply the induction hypothesis to $G'_1$ and $G'_2$ separately. Note that this requires strong induction!)

(b) More generally, $G'$ may have $t \ge 2$ distinct connected components $G'_1$ through $G'_t$ — generalize your argument above to this setting in order to complete the proof of Theorem 5.4.

*Note (these notes):* Theorem 5.4 of CS70 Note 5 says that "connected with no cycles" and "connected with $n-1$ edges" are equivalent (see *Four ways to say tree* in @sec-math-discrete-graph-trees). Its proof of the forward direction removes a vertex $v$ from a connected graph $G$ with no cycles and calls the result $G'$.
:::

::: {.problem #prob-cs70-5-q3 origin="external" source="cs70-5.5-q3"}
Complete the proof of the converse direction in Theorem 5.4 by proving, using induction on the number of vertices $n$, that any connected graph must have at least $n - 1$ edges.

*Note (these notes):* Theorem 5.4 of CS70 Note 5 is described in *Four ways to say tree* in @sec-math-discrete-graph-trees.
:::
