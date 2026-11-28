---
title: "Suffix Trees and Their Applications"
sources: [mit6851-16]
requires: [cs/strings/suffix-arrays, cs/range-queries/range-minimum-query]
aliases: [cs/algorithm-topics/suffix-trees]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 16, in our own wording; proofs written out in steps. The example banana$ is the lecture's; the figure is our own and the suffix and LCP arrays were checked by computation. Overlap: the suffix trie (cs/algorithm-topics/suffix-tries) and suffix array notes; merges proposed to the owner, none done. -->

A suffix tree is the compressed trie of all suffixes of a text. It has linear size, answers pattern queries in time proportional to the pattern, and together with the constant-time LCA and level-ancestor structures solves many string problems directly.

::: {#def-compressed-trie .definition name="Compressed trie and suffix tree"}

A *compressed trie* of a set of strings is the trie in which every maximal path of non-branching nodes is contracted to one edge labelled by the concatenated letters. The *suffix tree* of a text $T$ is the compressed trie of all suffixes of $T\$$, where $\$$ is a letter not in the alphabet that ends every suffix. Its leaves correspond one-to-one to the suffixes. The *letter depth* of a node is the length of the string spelled from the root to it.

Storing the edge labels as pairs (first index, last index) into $T$ makes the tree take $O(|T|)$ space (a tree with $|T|$ leaves and no unary nodes has fewer than $2|T|$ nodes).

:::

::: {#fig-suffix-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[small vertex] (r) at (0,0) {};
\node[small vertex] (l6) at (-4.4,-2.0) {$6$};
\node[small vertex] (a) at (-2.2,-1.0) {};
\node[small vertex] (l5) at (-3.2,-2.2) {$5$};
\node[small vertex] (n1) at (-1.2,-2.0) {};
\node[small vertex] (l3) at (-1.9,-3.4) {$3$};
\node[small vertex] (l1) at (-0.5,-3.4) {$1$};
\node[small vertex] (l0) at (0.9,-2.0) {$0$};
\node[small vertex] (n2) at (3.0,-1.0) {};
\node[small vertex] (l4) at (2.2,-2.2) {$4$};
\node[small vertex] (l2) at (3.9,-2.2) {$2$};
\draw (r)--node[edge label,midway,above left] {$\$$} (l6);
\draw (r)--node[edge label,midway,above left] {$a$} (a);
\draw (r)--node[edge label,midway,right] {$banana\$$} (l0);
\draw (r)--node[edge label,midway,above right] {$na$} (n2);
\draw (a)--node[edge label,midway,above left] {$\$$} (l5);
\draw (a)--node[edge label,midway,above right] {$na$} (n1);
\draw (n1)--node[edge label,midway,above left] {$\$$} (l3);
\draw (n1)--node[edge label,midway,above right] {$na\$$} (l1);
\draw (n2)--node[edge label,midway,above left] {$\$$} (l4);
\draw (n2)--node[edge label,midway,above right] {$na\$$} (l2);
\end{tikzpicture}
\end{center}
```

The suffix tree of $T=\text{banana}\$$; a leaf carries the starting index of its suffix.

:::

::: {#prp-suffix-tree-queries .proposition name="Pattern queries on a suffix tree"}

Let $T$ have length $n$ and let a pattern $P$ of length $m$ be given. A substring of $T$ is a prefix of a suffix, so $P$ occurs in $T$ exactly when it can be followed from the root; the leaves below the point where $P$ ends are the occurrences. With subtree sizes and leaf pointers stored, one can

* *decide* whether $P$ occurs, and *count* its occurrences (the size of the subtree below), without enumerating them;
* *list the first $k$* occurrences in the order of the leaves in $O(k)$ extra time, by threading the leaves in a linked list and storing at each node its leftmost leaf;
* find the *longest repeated substring* as the branching node of maximum letter depth, in $O(n)$ time;
* find the *longest common prefix* of $T[i..]$ and $T[j..]$ as the letter depth of $\operatorname{lca}$ of the two leaves, in $O(1)$ time after linear preprocessing (@thm-rmq-linear).

The time to follow $P$ depends on how the children of a node are stored (below).

:::

::: {#prp-trie-node-storage .proposition name="Storing the children of a node"}

Let $\Sigma$ be the alphabet and $|P|=m$. Storing the children of every node

* in an array of size $|\Sigma|$ gives query time $O(m)$ and space $O(n|\Sigma|)$;
* in a balanced search tree gives $O(m\log|\Sigma|)$ and $O(n)$;
* in a hash table gives $O(m)$ expected time and $O(n)$ space, but then only exact matching (no predecessor among siblings);
* in a van Emde Boas tree (@def-veb) gives $O(m\log\log|\Sigma|)$ and $O(n)$ with predecessor support.

A weight-balanced search tree (the weight of a child is the number of leaves below it) gives $O(m+\log k)$ for a trie of $k$ strings, because every step either consumes a letter of $P$ or discards a constant fraction of the candidate leaves; leaf trimming and arrays on the top part improve this to $O(m+\log|\Sigma|)$ with $O(n)$ space (suffix trays).

:::

::: {#prp-suffix-tree-array .proposition name="Suffix tree $\leftrightarrow$ suffix array and LCP array"}

The suffix array $\mathrm{SA}$ is the left-to-right order of the leaves of the suffix tree (children sorted by first letter), and the LCP array $\mathrm{LCP}[i]=\operatorname{lcp}(T[\mathrm{SA}[i]..],T[\mathrm{SA}[i+1]..])$ lists the letter depths of the internal nodes met between consecutive leaves. Conversely the suffix tree is recovered in linear time from $\mathrm{SA}$ and $\mathrm{LCP}$ by building the Cartesian tree of the LCP array in which *all* minima of a range become children of one node (@thm-cartesian-linear), with the suffixes $\mathrm{SA}[0],\mathrm{SA}[1],\dots$ inserted as leaves in order.

:::

::: {.proof}

1. A traversal of the suffix tree visits the leaves in sorted order of the suffixes, since children are ordered and the suffixes below an edge share its letters.

2. For two consecutive leaves, the lowest common ancestor is the node where their paths separate, and its letter depth is their longest common prefix. So the LCP array holds these depths.

3. The range minimum of $\mathrm{LCP}[i..j-1]$ is the lcp of the suffixes $\mathrm{SA}[i]$ and $\mathrm{SA}[j]$ (the lcp of a range of sorted strings is the minimum of the adjacent lcps), which is the letter depth of the lowest common ancestor of the two leaves; this is the Cartesian-tree statement of @thm-cartesian-range-minimum, so the Cartesian tree of $\mathrm{LCP}$ with ties merged is the tree of internal nodes, labelled by their letter depths.

4. The edge labels are then read from $T$ and $\mathrm{SA}$.

:::

::: {#exm-suffix-trees-1 .example name="banana"}

For $T=\text{banana}\$$ the sorted suffixes are $\$,a\$,ana\$,anana\$,banana\$,na\$,nana\$$, so $\mathrm{SA}=[6,5,3,1,0,4,2]$ and $\mathrm{LCP}=[0,1,3,0,0,2]$. The three zeros are the root, the letter depths $1,3$ are the internal nodes under $a$ ($a$ and $ana$), and $2$ is the node $na$, as in @fig-suffix-trees-1.

:::

::: {#prp-multiple-documents .proposition name="Several texts"}

For documents $T_1,\dots,T_k$ concatenate them with distinct terminators $\$_1,\dots,\$_k$ and cut each path below its terminator. The *longest common substring* of all documents is the node of maximum letter depth with all $k$ terminators below it; the *number of distinct documents* below a node is stored at it. All $d$ distinct documents containing $P$ are reported in $O(m+d)$ time (Muthukrishnan): store at every terminator leaf the number of the previous leaf with the same terminator; with $[l,r]$ the leaf range below the end of $P$, a document is reported by each leaf of $[l,r]$ whose stored value is $<l$, and these are found one by one by range-minimum queries on the stored values, splitting the range at each minimum found.

:::

::: {#rmk-suffix-trees-1 .remark name="Level ancestors and substrings"}

All occurrences of a known substring $T[i..j]$ are the leaves below the ancestor of the leaf $i$ at letter depth $j-i+1$. This is a level-ancestor query with weighted edges; the lecture gives an $O(\log\log n)$-time, $O(n)$-space structure by keeping the long paths and ladders of @def-long-path-decomposition in van Emde Boas predecessor structures instead of lookup tables.

:::
