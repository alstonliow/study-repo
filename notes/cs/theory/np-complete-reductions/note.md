---
title: "NP-Completeness Proofs by Reduction"
sources: [mit6046-16, mit6046r-8]
requires: [cs/theory/complexity-classes]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 16 and Recitation 8, in our own wording; proofs written out in steps. Definitions of NP, reductions and NP-completeness are in @sec-cs-theory-complexity-classes. -->

To show that a decision problem $X$ is NP-complete:

1. show $X\in\mathrm{NP}$ by giving a polynomial-time verifier for short certificates (@def-np);
2. choose a known NP-complete problem $Y$ and give a polynomial-time map $R$ from inputs of $Y$ to inputs of $X$;
3. prove that $y$ is a YES input of $Y$ if and only if $R(y)$ is a YES input of $X$ (both directions).

Then every problem in NP reduces to $Y$, hence to $X$ (@prp-np-complete-consequences). A reduction is usually built from *gadgets*: small pieces of the new input that imitate variables, clauses or other parts of the old one.

::: {#def-3sat .definition name="3SAT"}

*3SAT*: given a Boolean formula in conjunctive normal form in which every clause is the OR of exactly three literals (variables or negated variables), such as $(x_1\lor x_3\lor\bar x_6)\land(\bar x_2\lor x_3\lor\bar x_7)$, is there an assignment of true/false to the variables that makes the formula true?

:::

3SAT is NP-complete (Cook–Levin): a verifier is a circuit of polynomial size, and "does some certificate make this circuit output YES" can be written as a 3CNF formula. It is the usual starting point.

## Graph problems

::: {#thm-independent-set-np-complete .theorem name="Independent set"}

*Independent set*: given a graph $G$ and an integer $k$, does $G$ have $k$ pairwise non-adjacent vertices? This problem is NP-complete.

:::

::: {.proof}

1. *In NP:* the certificate is the $k$ vertices; check that no two are adjacent.

2. *Reduction from 3SAT.* For a formula with $m$ clauses, make a triangle for each clause, with one vertex per literal, and join every vertex labelled $x_i$ to every vertex labelled $\bar x_i$. Set $k=m$.

3. *If satisfiable:* pick one true literal in each clause; its vertices are in different triangles and never a variable and its negation, so they are independent: $m$ vertices.

4. *If an independent set of size $m$ exists:* it has exactly one vertex per triangle, and never both $x_i$ and $\bar x_i$. Set those literals true (other variables arbitrarily); every clause contains a true literal.

:::

::: {#fig-np-complete-reductions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (c00) at (0.0,0) {$x_1$};
\node[small vertex, fill=accentLight, draw=accent] (c01) at (1.6,0) {$x_2$};
\node[small vertex] (c02) at (0.8,1.3) {$\bar x_3$};
\draw (c00) -- (c01) -- (c02) -- (c00);
\node[small vertex] (c10) at (4.5,0) {$\bar x_1$};
\node[small vertex] (c11) at (6.1,0) {$x_2$};
\node[small vertex, fill=accentLight, draw=accent] (c12) at (5.3,1.3) {$x_3$};
\draw (c10) -- (c11) -- (c12) -- (c10);
\draw[faint, dashed] (c00) to[bend right=15] (c10);
\draw[faint, dashed] (c02) to[bend right=15] (c12);
\end{tikzpicture}
\end{center}
```

The reduction from 3SAT to independent set for $(x_1\lor x_2\lor\bar x_3)\land(\bar x_1\lor x_2\lor x_3)$: a triangle per clause, and a dashed edge between each literal and its negation. Choosing one true literal per clause ($x_2$, $x_3$) gives an independent set of size $2$, one vertex per triangle.

:::

::: {#cor-vertex-cover-clique .corollary name="Vertex cover and clique"}

*Vertex cover* (are there $k$ vertices touching every edge?) and *clique* (are there $k$ pairwise adjacent vertices?) are NP-complete.

:::

::: {.proof}

$S$ is independent iff $V\setminus S$ is a vertex cover, so $(G,k)\mapsto(G,|V|-k)$ reduces independent set to vertex cover. $S$ is independent in $G$ iff it is a clique in the complement graph, so $(G,k)\mapsto(\bar G,k)$ reduces it to clique. Both are clearly in NP.

:::

Hamiltonian cycle is NP-complete too, and reduces to Hamiltonian path: split one vertex $v$ into two copies $v'$ (keeping $v$'s outgoing edges) and $v''$ (keeping its incoming edges); a Hamiltonian path must run from $v'$ to $v''$, which closes into a cycle through $v$.

## Number problems

::: {#def-3dm .definition name="3-dimensional matching"}

*3DM*: given disjoint sets $X,Y,Z$ of $n$ elements each and a set $T\subseteq X\times Y\times Z$ of triples, is there a set of $n$ triples covering every element exactly once? 3DM is NP-complete (by a reduction from 3SAT with "wheel" gadgets for the variables).

:::

::: {#thm-subset-sum-np-complete .theorem name="Subset sum"}

Subset sum (@exm-subset-sum) is NP-complete.

:::

::: {.proof}

1. *In NP:* the certificate is the subset.

2. *Reduction from 3DM.* Number the $3n$ elements $0,\dots,3n-1$ and let $b=|T|+1$. For a triple using elements $p,q,r$ create the number $b^p+b^q+b^r$, and set the target $t=\sum_{e=0}^{3n-1}b^e$ (the number written $11\cdots1$ in base $b$).

3. *Matching ⇒ subset:* the triples of a perfect matching use every element once, so their numbers add to $t$.

4. *Subset ⇒ matching:* at most $|T|<b$ numbers are added, so no base-$b$ digit carries; digit $e$ of the sum counts the chosen triples containing element $e$. The sum is $t$ only if every digit is $1$: each element is covered exactly once.

5. The numbers have $O(n)$ digits in base $b$, polynomial size.

:::

::: {#cor-partition-np-complete .corollary name="Partition"}

*Partition*: can a set $A$ of positive integers be split into two parts with equal sums? It is NP-complete.

:::

::: {.proof}

Given subset sum instance $(A,t)$ with $\sigma=\sum A$, add the two numbers $\sigma+t$ and $2\sigma-t$. The total is $4\sigma$, so each part must sum to $2\sigma$; the two new numbers cannot be on the same side (their sum $3\sigma$ is too large). The side with $2\sigma-t$ needs $t$ more from $A$, so a partition exists iff some subset of $A$ sums to $t$.

:::

The numbers in these reductions are exponentially large, which is necessary: subset sum and partition have pseudopolynomial algorithms (@exm-subset-sum), so they are only *weakly* NP-complete. A problem is *strongly* NP-complete if it stays NP-complete when all numbers are bounded by a polynomial in the input size; then no pseudopolynomial algorithm exists unless P = NP. *3-partition* and *4-partition* (split $3n$ or $4n$ numbers into groups of $3$ or $4$ with equal sums) are strongly NP-complete, and reductions from them show that packing rectangles into a rectangle and solving jigsaw puzzles are strongly NP-complete as well.
