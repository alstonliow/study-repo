::: {.problem #prob-mit6046s15-1-q1 origin="external" source="mit6046s15-1-q1"}
**Restaurant Location**

*Drunken Donuts*, a new wine-and-donuts restaurant chain, wants to build restaurants on many street corners with the goal of maximizing their total profit.

The street network is described as an undirected graph $G=(V,E)$, where the potential restaurant sites are the vertices of the graph. Each vertex $u$ has a nonnegative integer value $p_u$, which describes the potential ***profit*** of site $u$. Two restaurants cannot be built on adjacent vertices (to avoid self-competition). You are supposed to design an algorithm that outputs the chosen set $U\subseteq V$ of sites that maximizes the total profit $\sum_{u\in U}p_u$.

First, for parts (a)–(c), suppose that the street network $G$ is acyclic, i.e., a tree.

(a) Consider the following "greedy" restaurant-placement algorithm: Choose the highest-profit vertex $u_0$ in the tree (breaking ties according to some order on vertex names) and put it into $U$. Remove $u_0$ from further consideration, along with all of its neighbors in $G$. Repeat until no further vertices remain. Give a counterexample to show that this algorithm does not always give a restaurant placement with the maximum profit.

(b) Give an efficient algorithm to determine a placement with maximum profit.

(c) Suppose that, in the absence of good market research, DD decides that all sites are equally good, so the goal is simply to design a restaurant placement with the largest number of locations. Give a simple greedy algorithm for this case, and prove its correctness.

(d) Now suppose that the graph is arbitrary, not necessarily acyclic. Give the fastest correct algorithm you can for solving the problem.
:::

::: {.problem #prob-mit6046s15-5-q2 origin="external" source="mit6046s15-5-q2"}
**Choosing Prizes**

In this problem, you are presented with a collection of $n$ prizes from which you are allowed to select at most $m$ prizes, where $m<n$. Each prize $p$ has a nonnegative integer value, denoted $p.value$. Your objective is to maximize the total value of your chosen prizes.

The problem has several variations, described in parts (a)–(d) below. In each case, you should give an efficient algorithm to solve the problem, and analyze your algorithm's time and space requirements.

In parts (a)–(c), the prizes are presented to you as a sequence $P=(p_1,p_2,\dots,p_n)$, and your algorithm must output a subsequence $S$ of $P$. In other words, the selected prizes $S$ ($|S|=m$) must be listed in the same order as they are in $P$.

(a) Give an algorithm that returns a subsequence $S=(s_1,s_2,\dots)$ of $P$ of length at most $m$, for which $\sum_js_j.value$ is maximum. Analyze your algorithm in terms of $n$ and $m$.

(b) Now suppose there are two types of prizes, type A and type B. Each prize's type is given as an attribute $p.type$. Give an algorithm that returns a subsequence $S=(s_1,s_2,\dots)$ of $P$ of length at most $m$, for which $\sum_js_j.value$ is maximum, subject to the new constraint that, in $S$, all the prizes of type A must precede all the prizes of type B. Analyze your algorithm in terms of $n$ and $m$.

(c) As in part (a), there is only one type of prize. Give an algorithm that returns a subsequence $S=(s_1,s_2,\dots)$ of $P$ of length at most $m$, for which $\sum_js_j.value$ is maximum, subject to the new constraint that, in $S$, the values of the prizes must form a non-decreasing sequence. Analyze your algorithm in terms of $n$ and $m$.

In part (d), the prizes are represented by a rooted binary tree $T$, with root vertex $r$, where each vertex $u$ has an associated prize, $u.prize$. Let $P$ be the set of prizes in the tree. As before, each prize $p$ has a nonnegative integer attribute $p.value$.

(d) Give an algorithm that returns a set $S$ of at most $m$ prizes for which $\sum_{s\in S}s.value$ is maximum, subject to the new constraint that, for any $s\in S$ that is associated with a non-root node $u$ of $T$, the prize at node $u.parent$ is also in $S$. (This implies that the selected prizes must be associated with nodes that form a connected subtree of $T$ rooted at $r$.)
:::
