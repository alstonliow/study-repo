---
title: "Persistent Data Structures"
sources: [mit6851-1]
requires: [cs/data-structures/binary-trees, cs/algorithm-design/amortized-analysis]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 1, in our own wording; proofs written out in steps. Full and confluent persistence are only stated (owner scope: competition-relevant parts first). The figure is our own. -->

A *persistent* data structure keeps all its past versions. In contests the usual instance is the persistent segment tree, which is path copying applied to a segment tree; the general theory says when one can do better than copying.

::: {#def-persistence .definition name="Kinds of persistence"}

Data structures are modelled on a *pointer machine*: nodes of bounded size hold data and pointers, and an operation reads or changes $O(1)$ fields or creates a node. A structure is

* *partially persistent* if any version can be queried but only the newest can be updated (versions form a line);
* *fully persistent* if every version can be queried and updated (versions form a tree);
* *confluently persistent* if in addition two versions can be combined into a new one (versions form a DAG);
* *functionally persistent* if it is implemented by never changing a node, only creating new ones.

Functional implies confluent implies full implies partial.

:::

::: {#prp-path-copying .proposition name="Path copying"}

Any pointer structure in which every update changes the nodes on one root-to-node path (a balanced binary search tree, a segment tree, a trie) can be made functionally persistent: an update copies the changed node and, bottom-up, every ancestor of it, and the new root is the new version. If an update touches $s$ nodes, it creates $s$ nodes; for a balanced search tree that is $O(\log n)$ time and $O(\log n)$ new nodes per update, and a query on version $v$ starts from the root of $v$ at no extra cost.

:::

::: {#fig-persistent-data-structures-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0,0) {$5$};
\node[small vertex] (b) at (-1,-0.9) {$3$};
\node[small vertex] (c) at (1,-0.9) {$8$};
\node[small vertex] (d) at (-1.6,-1.8) {$1$};
\node[small vertex] (e) at (-0.4,-1.8) {$4$};
\draw (a)--(b); \draw (a)--(c); \draw (b)--(d); \draw (b)--(e);
\node[small vertex, fill=accentLight] (a2) at (-4.4,0) {$5'$};
\node[small vertex, fill=accentLight] (b2) at (-3.4,-0.9) {$3'$};
\node[small vertex, fill=accentLight] (e2) at (-3.0,-1.8) {$4'$};
\draw (a2)--(b2); \draw (b2)--(e2); \draw[hl] (b2) to[bend right=15] (d); \draw[hl] (a2) to[bend left=30] (c);
\node[lab] at (0,-2.6) {version $1$};
\node[lab] at (-3.6,-2.6) {version $2$};
\end{tikzpicture}
\end{center}
```

Path copying: changing node $4$ copies $4$, its parent $3$ and the root $5$ (shaded); the new nodes point to the unchanged subtrees $1$ and $8$ (curved edges), which both versions share.

:::

::: {#thm-partial-persistence .theorem name="Partial persistence with bounded in-degree (Driscoll–Sarnak–Sleator–Tarjan)"}

Every pointer-machine structure in which each node has $O(1)$ pointers into it can be made partially persistent with $O(1)$ amortized extra time and $O(1)$ extra space per update, and $O(1)$ extra time per read of a field in any version.

:::

::: {.proof}

Let at most $p$ pointers point into any node and let $d$ be the fields per node.

1. *Layout.* Each node keeps its fields as originally, a list of its at most $p$ back pointers (nodes that point to it) and a *mod log* of $2p$ entries $(\text{field},\text{version},\text{value})$. A node has constant size.

2. *Read of field $f$ in version $v$.* Take the log entry for $f$ with the largest version $\le v$, or the original value if there is none: $O(1)$ since the log has constant size.

3. *Write.* If the node has room in its log, append the entry. Otherwise create a new node holding the latest value of every field (and the back pointers), with an empty log; set the pointers *from* the old node's targets back to the new node's back-pointer lists; and, for each of the at most $p$ nodes pointing to the old node, perform a write that makes them point to the new node (recursively, in the new version). The old node stays for reading old versions.

4. *Amortised cost.* Let the potential be $c$ times the number of entries in the logs of the *current* (non-archived) nodes. A write that finds room costs $O(1)$ and raises the potential by $c$. A write that finds the log full copies the node, which turns $2p$ entries into $0$ in the current layout: the potential drops by $2cp$, which pays for the copying and for the at most $p$ recursive writes, each of amortised cost at most $2c$ (induction on the recursion; it terminates because the potential is non-negative and falls at every copy). Hence a write costs $O(1)$ amortised.

:::

::: {#rmk-persistent-data-structures-1 .remark name="Full, confluent and functional"}

Full persistence has the same bounds, again for bounded in-degree (Driscoll et al.). Versions now form a tree, so the log entry to use is the nearest ancestor version that wrote the field; the version tree is stored as a list of nested begin/end markers in an order-maintenance structure, which supports "insert after" and "is $x$ before $y$" in $O(1)$, and a full node is split into two by cutting its log along a subtree of versions. For confluent persistence the number of paths in the version DAG can be $2^u$ after $u$ updates, and the general overhead known (Fiat–Kaplan) depends on the logarithm of the number of root-to-version paths. For purely functional structures there are general lower bounds on what can be done (Pippenger), and efficient special cases such as persistent deques with concatenation and tries. The lecture lists as open whether the amortised bounds for full persistence can be made worst-case.

:::

::: {#rmk-persistent-data-structures-2 .remark name="Persistent segment trees in contests"}

Path copying on a segment tree gives $O(\log n)$ time and space per update and one root per version. The classic uses are the $k$-th smallest in a range (version $i$ = counts of the first $i$ elements, answer by walking versions $r$ and $l-1$ together) and rolling back or branching an array.

:::
