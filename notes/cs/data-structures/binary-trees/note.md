---
title: "Binary Trees"
sources: [mit6006-6, mit6006r-6]
requires: [cs/data-structures/linked-lists-and-dynamic-arrays, math/discrete/graph/trees]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 6 and Recitation 6, in our own wording; proofs written out in steps. -->

Arrays make reading fast and linked lists make local changes fast; binary trees aim for $O(\log n)$ time for *every* operation of the sequence and set interfaces. This note gives operations that run in time proportional to the height; @sec-cs-data-structures-avl-trees keeps the height logarithmic.

## Terminology

::: {#def-binary-tree .definition name="Binary tree"}

A *binary tree* is a pointer structure whose nodes each store an `item` and pointers `parent`, `left` and `right` (each possibly empty), forming a rooted tree (@def-rooted-tree) in which each node has at most one *left child* and at most one *right child*. The *root* has no parent and a *leaf* has no children. The *subtree* of a node $X$ consists of $X$ and all its descendants. The *depth* of $X$ is the number of edges from $X$ up to the root, and the *height* of $X$ is the largest number of edges on a downward path from $X$ to a leaf of its subtree. The height $h$ of the tree is the height of its root.

:::

::: {#def-traversal-order .definition name="Traversal order"}

The *traversal order* (in-order) of a subtree rooted at $X$ lists the traversal order of the left subtree of $X$, then $X$, then the traversal order of the right subtree. So every node in $X$'s left subtree comes before $X$, and every node in its right subtree comes after $X$.

:::

Listing all $n$ nodes in traversal order by this recursion takes $O(n)$ time, as each node is visited once with $O(1)$ work. The traversal order is the "meaning" of the tree: below, it will be the sequence order or the sorted order of keys.

## Navigation and changes in $O(h)$ time

::: {#prp-binary-tree-navigation .proposition name="First node and successor"}

1. The first node in the traversal order of $X$'s subtree is found by following left pointers from $X$ until a node with no left child.
2. The *successor* of $X$ (the next node in the traversal order of the whole tree) is: the first node of $X$'s right subtree if $X$ has a right child; otherwise the lowest ancestor $Y$ of $X$ such that $X$ is in $Y$'s left subtree (none if there is no such ancestor).

Both take $O(h)$ time. The last node and the predecessor are symmetric.

:::

::: {.proof}

1. If $X$ has a left child, all of its left subtree precedes $X$ and its right subtree, so the first node is the first node of the left subtree; otherwise $X$ itself is first. Induction on the height of $X$ gives the claim. Each step goes down one level, so it takes $O(h)$ time.

2. If $X$ has a right subtree, the nodes right after $X$ in the order are those of that subtree, starting with its first node.

3. Otherwise $X$ is the last node of the subtree of each ancestor whose right subtree contains it. Walk up from $X$: as long as we arrive from a right child, the current subtree ends with $X$. The first time we arrive at an ancestor $Y$ from its left child, $X$ is the last node of $Y$'s left subtree, and $Y$ comes right after it. If this never happens, $X$ is the last node of the tree. Walking up takes $O(h)$ time.

:::

The tree changes only at leaves, which keeps the operations simple.

::: {#prp-binary-tree-insert-delete .proposition name="Inserting and deleting"}

1. *Insert node $Y$ right after node $X$ in traversal order:* if $X$ has no right child, make $Y$ the right child of $X$; otherwise make $Y$ the left child of the successor of $X$, which has no left child.
2. *Delete the item of node $X$:* if $X$ is a leaf, detach it from its parent. Otherwise, if $X$ has a left child, swap the items of $X$ and its predecessor and delete the predecessor's node recursively; if it has only a right child, do the same with its successor.

Both keep the traversal order of the other items and take $O(h)$ time.

:::

::: {.proof}

1. *Insert.* If $X$ has no right child, a new right child of $X$ comes right after $X$ and before everything that followed $X$. Otherwise the successor $S$ is the first node of $X$'s right subtree, so it has no left child, and a new left child of $S$ comes right before $S$, hence right after $X$. Finding $S$ takes $O(h)$.

2. *Delete.* If $X$ has a left child, its predecessor $P$ lies in that subtree, below $X$. Swapping the items of $X$ and $P$ puts the item to be deleted in $P$; removing it from there leaves the other items in the same order, because $X$ and $P$ were adjacent in the order. Each recursive call moves to a strictly deeper node, so after at most $h$ steps we reach a leaf. The case of a right child is symmetric.

:::

## Two applications

::: {#def-binary-search-tree .definition name="Binary search tree"}

A *binary search tree* (set binary tree) is a binary tree whose traversal order is increasing order of key. Equivalently, for every node $X$, every key in $X$'s left subtree is smaller than $X$'s key and every key in its right subtree is larger.

:::

To `find(k)` in a binary search tree, start at the root: if $k$ is smaller than the current key go left, if larger go right, if equal return the item; falling off the tree means $k$ is absent. This is binary search on the tree and takes $O(h)$ time; `find_next`, `find_prev`, `insert` and `delete` follow the same pattern and also take $O(h)$.

To use a tree as a *sequence*, let the traversal order be the sequence order. To reach the $i$-th node quickly, every node stores the size of its subtree.

::: {#prp-subtree-at .proposition name="The $i$-th node"}

Suppose every node $X$ stores $X.\mathrm{size}$, the number of nodes in its subtree. Then the $i$-th node (counting from $0$) in the traversal order of $X$'s subtree is found in $O(h)$ time: let $n_L$ be the size of the left subtree ($0$ if empty); if $i<n_L$, find the $i$-th node of the left subtree; if $i=n_L$, return $X$; if $i>n_L$, find the $(i-n_L-1)$-th node of the right subtree.

:::

::: {.proof}

The traversal order of $X$'s subtree is the $n_L$ nodes of the left subtree, then $X$ at position $n_L$, then the right subtree. So each case returns the right node, by induction on the height. Each step goes down one level and does $O(1)$ work, so the time is $O(h)$.

:::

Sizes are kept correct by adding $1$ (or $-1$) to the size of every ancestor when a leaf is added (or removed), in $O(h)$ time. With this, `get_at`, `set_at`, `insert_at` and `delete_at` all take $O(h)$ time.

::: {#rmk-binary-trees-build .remark name="Building and the goal"}

A sequence tree can be built from an array in $O(n)$ time: make the middle item the root and build its two subtrees recursively from the two halves, which gives height $\lceil\log_2(n+1)\rceil-1$. A binary search tree can be built by sorting first, in $O(n\log n)$. So far all dynamic operations cost $O(h)$, and repeated insertions can make $h=n-1$ (a path). The next note keeps $h=O(\log n)$.

:::
