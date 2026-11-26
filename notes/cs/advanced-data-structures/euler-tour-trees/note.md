---
title: "Euler-Tour Trees"
sources: [mit6851-20]
requires: [cs/data-structures/augmented-search-trees]
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 20, in our own wording; proofs written out in steps. The example is the lecture's tree, the figure is our own. -->

An Euler-tour tree represents a dynamic forest by storing the depth-first tour of each tree in a balanced search tree. It is simpler than a link-cut tree (@thm-link-cut-trees) and handles aggregates over *subtrees* instead of paths.

::: {#def-euler-tour-tree .definition name="Euler-tour tree"}

For a rooted tree with $n$ vertices, the *Euler tour* is the sequence of vertices visited by a depth-first traversal that writes the vertex on entering it and again after returning from each child; it has $2n-1$ entries and starts and ends at the root. An *Euler-tour tree* stores this sequence, in order, in a balanced binary search tree keyed by position. Each vertex keeps pointers to its first and its last entry.

:::

::: {#exm-euler-tour-trees-1 .example name="A seven-vertex tree"}

Let $R$ have children $A$ and $B$, let $B$ have children $C,F,G$, and let $C$ have children $D,E$. The tour is $R\,A\,R\,B\,C\,D\,C\,E\,C\,B\,F\,B\,G\,B\,R$. The subtree of $C$ is the contiguous piece $C\,D\,C\,E\,C$ between its first and last entry.

:::

::: {#fig-euler-tour-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \v [count=\i from 0] in {R,A,R,B,C,D,C,E,C,B,F,B,G,B,R} {\draw[cell frame] (0.55*\i,0) rectangle +(0.55,0.55); \node[lab] at (0.55*\i+0.275,0.275) {$\v$};}
\foreach \i in {4,5,6,7,8} \draw[hl cell] (0.55*\i,0) rectangle +(0.55,0.55);
\draw[hl] (2.2,-0.25) -- (4.95,-0.25);
\node[lab] at (3.575,-0.6) {subtree of $C$};
\end{tikzpicture}
\end{center}
```

The tour of @exm-euler-tour-trees-1; the shaded piece is the subtree of $C$, found as the range between the first and last occurrence of $C$.

:::

::: {#thm-euler-tour-tree .theorem name="Operations on Euler-tour trees"}

With a balanced search tree supporting search, split and concatenate in $O(\log n)$, an Euler-tour tree supports in $O(\log n)$ time:

* $\operatorname{findroot}(v)$: the first (or last) entry of the sequence containing $v$;
* $\operatorname{connected}(u,v)$: $\operatorname{findroot}(u)=\operatorname{findroot}(v)$;
* $\operatorname{cut}(v)$: remove the subtree of $v$ from its tree;
* $\operatorname{link}(u,v)$: make the root $u$ of one tree a child of $v$ in another;
* subtree aggregate (sum, minimum, size, ...) of $v$, by a range query between its first and last entry.

:::

::: {.proof}

1. *findroot.* The root is the first and the last entry of the tour, found by walking to the leftmost entry of the search tree.

2. *cut.* The subtree of $v$ is the piece from the first to the last entry of $v$. Split the sequence before the first entry and after the last entry of $v$ into three parts: before, the subtree, after. Concatenate before and after, deleting one of the two copies of the parent that are now adjacent (the parent appears right before and right after the removed piece). The subtree becomes its own sequence.

3. *link.* Split the tour of $v$'s tree just before the last entry of $v$, and concatenate: the first part, a new entry of $v$, the whole tour of $u$'s tree, and the rest (which starts with the old last entry of $v$). The tour of $u$'s tree is now enclosed by two entries of $v$, as the tour of a child.

4. *aggregate.* Each search-tree node stores the aggregate of its subtree, so the range between the two entries of $v$ is combined from $O(\log n)$ nodes.

5. Each operation uses $O(1)$ searches, splits and concatenations.

:::

::: {#rmk-euler-tour-trees-1 .remark name="Variants"}

Storing the sequence in a B-tree with fan-out $\Theta(\log n)$ makes searches $O(\log n/\log\log n)$ and updates $O(\log^2n/\log\log n)$. A tree whose roots may change (rerooting) is handled by rotating the cyclic tour. For *path* aggregates use link-cut trees instead; for forests under edge insertions and deletions in a general graph see @sec-cs-advanced-data-structures-dynamic-connectivity.

:::
