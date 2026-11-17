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

::: {.problem #prob-cs70hw-3-q2 origin="external" source="cs70hw-3-q2"}
**Binary Trees.** You have seen the recursive definition of binary trees from lecture and from previous classes. Here, we define binary trees in graph theoretic terms as follows (Note: here we will modify the definition of leaves slightly for consistency).

- A binary tree of height $> 0$ is a tree where exactly one vertex, called the root, has degree 2, and all other vertices have degrees 1 or 3. Each vertex of degree 1 is called a leaf. The height $h$ is defined as the maximum length of the path between the root and any leaf.
- A binary tree of height 0 is the graph with a single vertex. The vertex is both a leaf and a root.

(a) Let $T$ be a binary tree of height $> 0$, and let $h(T)$ denote it's height. Let $r$ be the root in $T$ and $u$ and $v$ be it's neighbors. Show that removing $r$ from $T$ will result in two binary trees, $L, R$ with roots $u$ and $v$ respectively. Also, show that $h(T) = \max(h(L), h(R)) + 1$

(b) Using the graph theoretic definition of binary trees, prove that the number of vertices in a binary tree of height $h$ is at most $2^{h+1} - 1$

(c) Prove that all binary trees with $n$ leaves have $2n - 1$ vertices
:::

::: {.problem #prob-mit6042f10-5-q1 origin="external" source="mit6042f10-5-q1"}
Recall that a tree is a connected acyclic graph. In particular, a single vertex is a tree. We define a *Splitting Binary Tree*, or *SBTree* for short, as either the lone vertex, or a tree with the following properties:

1. exactly one node of degree 2 (called the *root*).
2. every other node is of degree 3 or 1 (called *internal nodes* and *leaves*, respectively).

For the case of one single vertex (see above), that vertex is considered to be a leaf. It is easier to understand the definition visually, so an example is shown in Figure 1. An example of a tree which is not an SBTree is shown in Figure 2.

*Figure 1: Splitting Binary Tree: Node A is the root, B and E are internal nodes, and C, D, F, and G are leaves. Notice how all internal nodes have degree 3.*

*Figure 2: This is an example of a tree which is NOT a Splitting Binary Tree. Notice how both A and C have degree 2, when a BSTree can only have one such node.*

(a) Show if an SBTree has more than one vertex, then the induced subgraph obtained by removing the unique root consists of two disconnected SBTrees. You may assume that by removing the root you obtain two separate connected componenents, so all you need to prove is that those two components are SBTrees.

(b) Prove that two SBTrees with the same number of leaves must also have the same total number of nodes. Hint: As a conjecture, guess an expression for the total number of nodes in terms of the number of leaves $N(l)$. Then use induction to prove that it holds for all trees with the same $l$

*Note (these notes):* Figure 1: the edges are A–B, A–C, B–D, B–E, E–F, E–G. Figure 2: the edges are A–B, A–C, B–D, B–E, C–F. The figures are described rather than redrawn.
:::
