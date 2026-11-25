---
title: "B-Trees"
sources: [mit6046r-2, res-clrs-b-trees]
requires: [cs/data-structures/two-three-trees]
aliases: [cs/data-structures/b-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-23 from CLRS (3rd edition), Chapter 18, in our own wording; proofs written out in steps. Merged 2026-11-24 (owner): the definition def-b-tree comes from MIT 6.046 Recitation 2 and was moved here from cs/data-structures/two-three-trees; its parameter B is CLRS's minimum degree t. The rest of the note, from CLRS, adds the height bound, the disk-access view and the one-pass updates. The example trees are our own. -->

A B-tree is a 2-3 tree (@def-two-three-tree) with wide nodes: every node other than the root has between $B$ and $2B$ children. B-trees are made for data on disk or in any memory that moves whole blocks at a time. One node fills one block, $B$ is in the hundreds, and the tree is so shallow that a search reads only a handful of blocks.

::: {#def-b-tree .definition name="B-tree"}

A *B-tree* with branching parameter $B\ge2$ generalises 2-3 trees: every internal node other than the root has between $B$ and $2B$ children (and one key fewer than children), the root has between $2$ and $2B$ children, and all leaves are at the same depth. Insertion splits overfull nodes and deletion borrows or merges, as in 2-3 trees (@prp-two-three-insert).

:::

## Shape and height

Throughout, a node with $k$ keys $x_1<\dots<x_k$ has, if internal, $k+1$ children, and the keys in the $i$-th child lie between $x_{i-1}$ and $x_i$. We use the same key range for leaves as for internal nodes.

::: {#prp-b-tree-key-counts .proposition name="Keys per node"}

In a B-tree with parameter $B$, every node other than the root holds between $B-1$ and $2B-1$ keys, and the root holds between $1$ and $2B-1$ keys (if the tree is not empty). A node with $2B-1$ keys is called *full*.

:::

::: {.proof}

An internal node has one key fewer than children, so the bounds on children in @def-b-tree become $B-1\le k\le2B-1$ for non-root nodes and $1\le k\le2B-1$ for the root. Leaves follow the same rule by our convention.

:::

::: {#thm-b-tree-height .theorem name="Height of a B-tree"}

A B-tree with parameter $B\ge2$ and $n\ge1$ keys has height
$$
h\le\log_B\frac{n+1}{2}.
$$

:::

::: {.proof}

1. The root has at least $2$ children if $h\ge1$, and every other internal node has at least $B$. So there are at least $2$ nodes at depth $1$, at least $2B$ at depth $2$, and at least $2B^{i-1}$ at depth $i$.

2. The root holds at least $1$ key and every other node at least $B-1$ (@prp-b-tree-key-counts). Hence
$$
n\ge1+(B-1)\sum_{i=1}^{h}2B^{i-1}=1+2(B-1)\frac{B^h-1}{B-1}=2B^h-1.
$$

3. So $B^h\le(n+1)/2$; take $\log_B$.

:::

::: {#fig-b-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[box] (r) at (4.2,0) {$30\;\;60$};
\node[box] (a) at (1.0,-1.3) {$5\;\;10\;\;20$};
\node[box] (b) at (4.2,-1.3) {$35\;\;40\;\;45\;\;50\;\;55$};
\node[box] (c) at (7.4,-1.3) {$70\;\;80$};
\draw (r)--(a) (r)--(b) (r)--(c);
\node[lab,tick] at (2.0,-0.45) {$<30$};
\node[lab,tick] at (4.75,-0.65) {$30..60$};
\node[lab,tick] at (6.4,-0.45) {$>60$};
\node[lab,tick, anchor=west] at (5.75,-1.3) {full};
\end{tikzpicture}
\end{center}
```

A B-tree with $B=3$: non-root nodes hold $2$ to $5$ keys. The root's two keys split the key range into three parts, one per child. The middle leaf holds $2B-1=5$ keys and is full.

:::

## Searching on disk

In the external-memory model (@def-external-memory-model), the cost of an algorithm is the number of blocks it moves between disk and memory. Choose the parameter so that a node fills one block. Then each node costs one transfer, and the work inside a node, in fast memory, is free in this model.

::: {#prp-b-tree-search .proposition name="Search"}

Searching a B-tree reads $O(h)=O(\log_Bn)$ nodes. Inside each node, a linear scan costs $O(B)$ time and a binary search $O(\log B)$, so the total computing time is $O(B\log_Bn)$ or $O(\log n)$.

:::

::: {.proof}

1. At each node, find the least key $x_i\ge k$. If $x_i=k$, stop; otherwise go to the $i$-th child (or the last child if no such key exists), whose range contains $k$. At a leaf, stop.

2. This reads one node per level, $h+1$ nodes in all, and $h=O(\log_Bn)$ by @thm-b-tree-height.

3. A binary search finds $x_i$ in $O(\log B)$ comparisons, and $\log B\cdot\log_Bn=\log n$.

:::

With $B=500$ and $n=10^9$ keys, @thm-b-tree-height gives $h\le3$: four block reads per search, of which the root (and often the next level) can stay in memory.

## Insertion in one pass

The 2-3 tree insertion (@prp-two-three-insert) goes down to a leaf and then splits overfull nodes on the way back up, which reads some nodes twice. A B-tree can instead split *on the way down*: never step into a full node.

::: {#def-b-tree-split .definition name="Splitting a full child"}

Let $y$ be a full child of a non-full node $x$, with keys $y_1<\dots<y_{2B-1}$. To *split* $y$, move the median key $y_B$ up into $x$, between the keys of $x$ that bracket it, and replace $y$ by two nodes: one with $y_1,\dots,y_{B-1}$ and the first $B$ children of $y$, the other with $y_{B+1},\dots,y_{2B-1}$ and the last $B$ children.

:::

::: {#prp-b-tree-insert .proposition name="One-pass insertion"}

To insert $k$: if the root is full, split it under a new empty root (the tree grows by one level). Then walk down from the root towards the leaf where $k$ belongs, and before stepping into a child, split it if it is full. At the leaf, which is now not full, add $k$. This keeps all the rules, reads and writes $O(\log_Bn)$ nodes, and takes $O(B\log_Bn)$ time.

:::

::: {.proof}

1. *A split is valid.* The two new nodes hold $B-1$ keys each, the minimum allowed. Their key ranges are separated by $y_B$, now in $x$, so the search order holds. The parent $x$ was not full, so it can take one more key. The new nodes are at the depth of $y$, so all leaves stay at one depth.

2. *The parent is never full.* We split a child only while standing at its parent, and we enter a node only after making sure it is not full; the root is made non-full first. So every split has a non-full parent, and the leaf reached at the end has room for $k$.

3. *Height.* Only a split of the root adds a level, and it adds it above all leaves at once.

4. *Cost.* One pass from root to leaf with $O(1)$ splits per level, each touching three nodes and moving $O(B)$ keys and pointers: $O(h)$ node accesses and $O(Bh)$ time.

:::

::: {#fig-b-trees-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[box] (r) at (3.0,0) {$30\;\;60$};
\node[box] (a) at (0.6,-1.3) {$5\;\;10\;\;20$};
\node[hl box] (b) at (3.0,-1.3) {$35\;\;40\;\;45\;\;50\;\;55$};
\node[box] (c) at (5.4,-1.3) {$70\;\;80$};
\draw (r)--(a) (r)--(b) (r)--(c);
\draw[emph,->] (6.5,-0.65) -- (7.5,-0.65);
\node[lab,tick] at (7.0,-0.35) {split};
\node[box] (r2) at (10.7,0) {$30\;\;\mathbf{45}\;\;60$};
\node[box] (a2) at (8.2,-1.3) {$5\;\;10\;\;20$};
\node[box] (b2) at (9.75,-1.3) {$35\;\;40$};
\node[hl box] (b3) at (11.5,-1.3) {$50\;\;52\;\;55$};
\node[box] (c2) at (13.2,-1.3) {$70\;\;80$};
\draw (r2)--(a2) (r2)--(b2) (r2)--(b3) (r2)--(c2);
\end{tikzpicture}
\end{center}
```

Inserting $52$ into the tree of @fig-b-trees-1. The search would enter the full leaf, so it is split first: its median $45$ moves up to the root, and the halves $35,40$ and $50,55$ become two leaves. Then $52$ goes into the leaf $50,55$.

:::

## Deletion in one pass

Deletion mirrors insertion: never step into a node with only $B-1$ keys, so that removing a key below never leaves a node too small. Before descending into a child $c$ of $x$ that has exactly $B-1$ keys, add a key to it:

- *Borrow.* If a neighbouring sibling of $c$ has at least $B$ keys, move the key of $x$ that separates them down into $c$, move the sibling's nearest key up into $x$ in its place, and move the sibling's nearest child over to $c$. This is a rotation through the parent.
- *Merge.* If both neighbouring siblings have $B-1$ keys, merge $c$, one sibling and the separating key of $x$ into one node with $2B-1$ keys.

::: {#prp-b-tree-delete .proposition name="One-pass deletion"}

To delete $k$, walk down from the root, making sure as above that every node entered other than the root has at least $B$ keys. At a node $x$:

1. if $x$ is a leaf holding $k$, remove $k$;
2. if $x$ is internal and holds $k$, replace $k$ by its predecessor (from the child before $k$) or its successor (from the child after $k$), choosing a child with at least $B$ keys, and delete that key from the child's subtree; if both children have $B-1$ keys, merge them with $k$ and delete $k$ from the merged node;
3. otherwise continue into the child whose range contains $k$.

If the root is left with no keys, its only child becomes the root (the tree loses a level). Deletion reads and writes $O(\log_Bn)$ nodes and takes $O(B\log_Bn)$ time.

:::

::: {.proof}

1. *Borrowing and merging are valid.* A borrow moves one key into $c$ and one out of a sibling that had at least $B$, so both stay within bounds, and the separating keys still separate. A merge makes a node with $(B-1)+1+(B-1)=2B-1$ keys, and $x$ loses one key, which is allowed because $x$ has at least $B$ keys (or is the root). All leaves keep their depth.

2. *Removals keep the minimum.* A key is removed only from a node that has at least $B$ keys when we reach it, so it keeps at least $B-1$.

3. *Case 2 is correct.* The predecessor of $k$ is the largest key of the child before $k$, and it can replace $k$ without breaking the search order; similarly for the successor. Deleting it from that child's subtree is the same procedure one level down. After a merge, $k$ sits in the merged node, and deleting it there is again a step one level down.

4. *Root.* The root may drop to $0$ keys only after a merge of its last two children; making the merged child the root lowers every leaf by one level at once.

5. *Cost.* The walk visits each level once, with $O(1)$ borrows or merges per level, each costing $O(B)$ time and $O(1)$ node accesses.

:::

::: {#fig-b-trees-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[box] (r) at (2.6,0) {$30\;\;45\;\;60$};
\node[box] (a) at (0.6,-1.3) {$5\;\;10\;\;20$};
\node[hl box] (b) at (2.2,-1.3) {$35\;\;40$};
\node[box] (b3) at (3.5,-1.3) {$50\;\;55$};
\node[box] (c) at (4.8,-1.3) {$70\;\;80$};
\draw (r)--(a) (r)--(b) (r)--(b3) (r)--(c);
\draw[emph,->] (5.8,-0.4) -- (6.8,0.4);
\draw[emph,->] (5.8,-1.0) -- (6.8,-1.8);
\node[lab,tick, anchor=east] at (9.0,1.0) {borrow from left};
\node[box] (rr) at (9.9,1.0) {$\mathbf{20}\;\;45\;\;60$};
\node[box] (ra) at (7.6,-0.2) {$5\;\;10$};
\node[hl box] (rb) at (9.2,-0.2) {$\mathbf{30}\;\;35\;\;40$};
\node[box] (rb3) at (10.8,-0.2) {$50\;\;55$};
\node[box] (rc) at (12.2,-0.2) {$70\;\;80$};
\draw (rr)--(ra) (rr)--(rb) (rr)--(rb3) (rr)--(rc);
\node[lab,tick, anchor=east] at (9.2,-1.6) {merge with right};
\node[box] (mr) at (9.9,-1.6) {$30\;\;60$};
\node[box] (ma) at (7.6,-2.8) {$5\;\;10$};
\node[hl box] (mb) at (9.7,-2.8) {$35\;\;40\;\;\mathbf{45}\;\;50\;\;55$};
\node[box] (mc) at (11.9,-2.8) {$70\;\;80$};
\draw (mr)--(ma) (mr)--(mb) (mr)--(mc);
\end{tikzpicture}
\end{center}
```

Before deleting $35$, the search must enter the leaf $35,40$, which has only $B-1=2$ keys. Top: its left sibling has $3$ keys, so $20$ moves up and $30$ moves down into the leaf. Bottom: if the left sibling had held only $5,10$, no sibling could lend a key, and the leaf would be merged with its right sibling $50,55$ and the separating key $45$ into one full leaf. Either way the leaf now has room to lose $35$.

:::

::: {#rmk-b-trees-1 .remark name="Variants"}

Databases and file systems mostly use *B+ trees*, which keep all items in the leaves, link the leaves in order for fast range scans, and store only routing keys in internal nodes, so that internal nodes branch more widely. With $B=2$ the B-tree is a 2-3-4 tree, which red-black trees encode as binary trees (@sec-cs-data-structures-red-black-trees).

:::
