---
title: "x-Fast and y-Fast Tries"
sources: [mit6851-11]
requires: [cs/integer-data-structures/van-emde-boas, cs/hashing/perfect-hashing, cs/data-structures/tries]
aliases: [cs/advanced-data-structures/y-fast-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 11, in our own wording; proofs written out in steps. The example and figure are our own. The lecture's other results on van Emde Boas trees (binary-tree view, hashed clusters) are only summarised in the remark. -->

The *predecessor problem* maintains a set $S$ of $n$ integers from $\{0,\dots,u-1\}$ ($w=\log_2u$ bits) under insert, delete, and $\operatorname{pred}(x)$, $\operatorname{succ}(x)$. Balanced trees take $\Theta(\log n)$; van Emde Boas trees (@def-veb) take $O(\log w)=O(\log\log u)$ but $\Theta(u)$ space. Willard's x-fast and y-fast tries get $O(\log w)$ in linear space.

::: {#def-x-fast .definition name="x-fast trie"}

View $S$ as the leaves of the complete binary trie of depth $w$ over $\{0,1\}^w$. A trie node is *marked* if its subtree contains a key. An *x-fast trie* stores

* a perfect hash table (@def-perfect-hashing) of the bit strings (root-to-node paths) of all marked nodes, mapping each to the minimum and maximum key below it;
* the keys in a sorted doubly linked list.

:::

::: {#thm-x-fast .theorem name="x-fast trie"}

An x-fast trie answers $\operatorname{pred}$ and $\operatorname{succ}$ in $O(\log w)$ time (expected, or worst case for a static set), uses $O(nw)$ space, and an insert or delete costs $O(w)$.

:::

::: {.proof}

1. *Search.* Along the path of $x$ the marked nodes form a prefix of the path, because a node is marked whenever a descendant is. A binary search over the length $0,\dots,w$, testing "is this prefix in the hash table?", finds the deepest marked node $v$ on the path in $O(\log w)$ probes.

2. If $v$ is the leaf of $x$, then $x\in S$. Otherwise the child of $v$ on the path of $x$ is unmarked, so all keys below $v$ lie on the other side of $x$. If $x$ goes to the left child, the other child holds keys $>x$ and $\operatorname{succ}(x)$ is its minimum, read from the table; the predecessor is then the list predecessor. The case of the right child is symmetric.

3. *Space.* Each key marks its $w+1$ ancestors, so the table has at most $n(w+1)$ entries.

4. *Updates.* Inserting or deleting a key changes the marks and the minima and maxima of its $w$ ancestors, $O(w)$ table operations, and one list operation.

:::

::: {#fig-y-fast-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=0.9cm, every node/.style={small vertex},
  level 1/.style={sibling distance=3.6cm}, level 2/.style={sibling distance=1.8cm}, level 3/.style={sibling distance=0.9cm}]
\node (r) {}
  child {node (n0) {}
    child {node (n00) {} child[missing] child {node (n001) {$1$}}}
    child {node (n01) {} child {node (n010) {$2$}} child[missing]}}
  child {node[fill=accentLight] (n1) {}
    child {node[fill=accentLight] (n10) {} child[missing] child {node (n101) {$5$}}}
    child {node (n11) {} child {node (n110) {$6$}} child[missing]}};
\draw[hl] (r)--(n1); \draw[hl] (n1)--(n10);
\node[lab,tick] at (1.0,-3.3) {$q=4=100_2$};
\end{tikzpicture}
\end{center}
```

The trie of $S=\{1,2,5,6\}$ with $w=3$ (only marked nodes are drawn and hashed). The query $q=100_2$ follows the shaded path: the longest marked prefix is $10$; its left child is unmarked, so $\operatorname{succ}(4)$ is the minimum below its right child, $5$, and $\operatorname{pred}(4)$ is the list predecessor of $5$, which is $2$.

:::

::: {#def-y-fast .definition name="y-fast trie"}

Partition the sorted keys into groups of size between $\tfrac12w$ and $2w$ and store each group in a balanced search tree. Put one representative key of each group (any key in it) into an x-fast trie. This is a *y-fast trie*.

:::

::: {#thm-y-fast .theorem name="y-fast trie"}

A y-fast trie answers $\operatorname{pred}$ and $\operatorname{succ}$ in $O(\log w)$ time, performs updates in $O(\log w)$ amortised time, and uses $O(n)$ space (expected, with hashing).

:::

::: {.proof}

1. *Space.* There are $O(n/w)$ representatives, so the x-fast trie has $O\bigl(\tfrac nw\cdot w\bigr)=O(n)$ entries, and the groups hold $n$ keys in total.

2. *Query.* Find in the x-fast trie the representatives around $x$ in $O(\log w)$, then search the one or two adjacent groups in $O(\log w)$ (a group has $O(w)$ keys).

3. *Update.* An insert or delete first does the group operation in $O(\log w)$. When a group grows past $2w$ it is split into two groups of about $w$ keys; when it falls below $\tfrac12w$ it is merged with a neighbour (and split again if the result is too large). Either change costs $O(w)$ in the group and $O(w)$ in the x-fast trie.

4. A split or merge leaves groups of size between $\tfrac23w$ and $\tfrac32w$ — a constant fraction away from both limits — so $\Omega(w)$ updates must happen before the next rebalance of that group, and the $O(w)$ cost is $O(1)$ amortised per update.

:::

::: {#rmk-y-fast-trees-1 .remark name="Related bounds"}

The same indirection (groups of $w$ keys under a structure for $n/w$ keys) shortens the update of the binary-tree view of van Emde Boas trees from $O(w)$ to $O(\log w)$. Replacing the cluster arrays of a van Emde Boas tree by hash tables of non-empty clusters also gives $O(n)$ space, with $O(\log\log u)$ time with high probability. Fusion trees (@sec-cs-integer-data-structures-fusion-trees) give $O(\log_wn)$, which is better when $w$ is large relative to $\log n$; taking the better of the two gives $\min(\log_wn,\log w)=O\bigl(\sqrt{\log n/\log\log n}\bigr)$ (a short calculation; not proved here).

:::
