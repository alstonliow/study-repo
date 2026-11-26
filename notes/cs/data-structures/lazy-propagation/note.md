---
title: "Lazy Propagation"
sources: []
requires: [cs/data-structures/segment-trees]
status: draft
---

<!-- Added 2026-11-26 for the CSES range-update problems, in our own wording. TODO: add a source. -->

With a segment tree (@sec-cs-data-structures-segment-trees) a *point* update is cheap. To change a whole range $[i,j]$ at once (add $x$ to every entry, or assign $x$ to every entry), touching every leaf costs $O(n)$. *Lazy propagation* postpones the work: a node fully inside the range records the pending change in a tag and its children are updated only when a later operation needs them.

::: {#def-lazy-tag .definition name="Lazy tag"}

Every node $v$ stores its value $s(v)$ for its whole interval, already including all changes applied to $v$ or to an ancestor that were stopped at $v$, and a tag $t(v)$ describing a change that has been applied to $v$ but not yet to its children. For range addition, $t(v)=\delta$ means "add $\delta$ to every entry below $v$", and applying it to a node covering $\ell$ positions changes a sum by $\delta\ell$ (a minimum or maximum by $\delta$). *Pushing down* $v$ applies $t(v)$ to both children (changing their values and combining it into their tags) and resets $t(v)$.

:::

::: {#thm-lazy-propagation .theorem name="Lazy propagation"}

Assume that tags can be composed (applying $f$ then $g$ is again a tag) and that applying a tag to the stored value of a node takes $O(1)$ time given its length. If every operation pushes down the tags of the nodes it visits before descending to their children, then range update and range query both take $O(\log n)$ time and return correct answers.

:::

::: {.proof}

1. *Invariant.* For every node $v$, the true value of $\star$ over its interval equals $s(v)$ after applying all tags stored at the strict ancestors of $v$ (from the root down). Initially all tags are empty.

2. *Update.* A node whose interval lies inside the range is changed in $O(1)$: its value and tag are updated, and its children are left alone, which keeps the invariant for the subtree. A node that is only partly covered is first pushed down, so its children satisfy the invariant without the node's tag, then the two children are updated recursively, and $s(v)$ is recomputed from them.

3. *Query.* A visited node is pushed down before descending, so the values of its children are true; a node inside the range returns $s(v)$.

4. *Time.* The visited nodes are the same as for a segment-tree query (at most four per depth, Theorem @thm-segment-tree) and each does $O(1)$ extra work for the push-down.

:::

::: {#exm-lazy-propagation-1 .example name="Range addition, range sum"}

For $a=(1,2,3,4)$ the root stores $10$. After "add $5$ to positions $0..3$" the root stores $10+5\cdot4=30$ with tag $5$, and no other node changes. The query for the sum of positions $0..1$ pushes the tag down first: the left child (value $3$) becomes $3+5\cdot 2=13$ with tag $5$, the right child becomes $7+10=17$ with tag $5$, and the answer is $13$.

:::

::: {#fig-lazy-propagation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node[box] (r) at (3,2) {$30$ \ \tiny tag $5$};
\node[box] (a) at (1,0.7) {$3$};
\node[box] (b) at (5,0.7) {$7$};
\draw[->] (r) -- (a); \draw[->] (r) -- (b);
\node[box] (r2) at (9,2) {$30$};
\node[hl box] (a2) at (7.5,0.7) {$13$ \ \tiny tag $5$};
\node[hl box] (b2) at (10.5,0.7) {$17$ \ \tiny tag $5$};
\draw[->] (r2) -- (a2); \draw[->] (r2) -- (b2);
\node[lab, anchor=north] at (3,-0.1) {before the query: children stale};
\node[lab, anchor=north] at (9,-0.1) {after the push-down};
\end{tikzpicture}
\end{center}
```

@exm-lazy-propagation-1: the tag of the root moves to its children when the query needs them. The stored values of the children now include the addition.

:::

::: {#rmk-lazy-propagation-1 .remark name="Combining several kinds of update"}

For range *assignment* together with range *addition* a tag is a pair (assign $a$, then add $d$) and composition must follow the order of the operations: a later assignment erases the earlier tag, a later addition is added to the tag's $d$. Arithmetic progressions can be added lazily too: a tag $(c,d)$ meaning "add $c+kd$ to the $k$-th entry of the interval" composes by adding the two pairs, with the offset of a right child shifted by the length of its left sibling.

:::
