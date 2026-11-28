---
title: "Retroactive Data Structures"
sources: [mit6851-2]
requires: [cs/data-structure-models/persistent-data-structures, cs/data-structures/augmented-search-trees, cs/data-structures/binary-heaps]
aliases: [cs/advanced-data-structures/retroactive-data-structures]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-26 from MIT 6.851 (Spring 2012), Lecture 2, in our own wording; proofs written out in steps. The bridge lemma was checked by a brute-force test on random operation sequences. The cell-probe and non-oblivious parts are only stated. -->

A persistent structure lets you read the past. A *retroactive* one lets you change it: insert or delete an operation at an earlier time and see the consequence for the present (and for later queries).

::: {#def-retroactive .definition name="Retroactive data structure"}

The history is a sequence of timed updates. A retroactive structure supports

* $\mathrm{Insert}(t,u)$: insert the update $u$ at time $t$;
* $\mathrm{Delete}(t)$: delete the update at time $t$;
* $\mathrm{Query}(t,q)$: query the structure as it was at time $t$.

It is *partially retroactive* if queries are only allowed at the present ($t=\infty$) and *fully retroactive* if at any time. *Non-oblivious* retroactivity also records the queries and reports which of them would change. Times are kept in an order-maintenance structure, so $t$ may be inserted between existing times.

:::

::: {#prp-retroactive-commutative .proposition name="Commutative and invertible updates"}

If updates commute, $\mathrm{Insert}(t,u)$ has the same effect as inserting $u$ now; if every update $u$ has an inverse $u^{-1}$ with $u\,u^{-1}=\varnothing$, then $\mathrm{Delete}(t)$ of $u$ has the same effect as inserting $u^{-1}$ now. So partial retroactivity is free for structures such as a hash table or an array with the update $A[i]\mathrel{+}=\Delta$ (no assignment).

:::

::: {#thm-retroactive-decomposable .theorem name="Decomposable search problems"}

A *decomposable search problem* maintains a set $S$ under insert, delete and $\mathrm{query}(x,S)$ where $\mathrm{query}(x,A\cup B)=f(\mathrm{query}(x,A),\mathrm{query}(x,B))$ for an $O(1)$ function $f$ (nearest neighbour, successor, point location). With $m$ updates it can be made fully retroactive with $O(\log m)$ factor overhead in time and space.

:::

::: {.proof}

1. Build a balanced binary tree (a segment tree) over the time axis; the leaves are times.

2. Every element lives in the structure during an interval of time, from its insertion to its deletion. Store the element in the $O(\log m)$ tree nodes whose time intervals tile that interval, in a copy of the static structure at each node.

3. A query at time $t$ looks at the $O(\log m)$ nodes on the root-to-$t$ path, queries each node's structure, and combines the answers with $f$. A retroactive update inserts or removes an element in $O(\log m)$ nodes.

:::

For an arbitrary structure, undoing the last $r$ updates, applying the change and redoing them costs $O(r)$ times the original cost, and a lower bound shows that $\Omega(r)$ overhead is unavoidable in general: with registers $X,Y$ and updates $Y\mathrel{+}=a_i$ and $X\mathrel{\cdot}= Y$, the history evaluates a polynomial in $X$, and retroactively changing the initial $X$ forces re-evaluating it.

::: {#thm-retroactive-priority-queue .theorem name="Partially retroactive priority queue"}

A priority queue with $\mathrm{insert}(k)$ and $\mathrm{delete\text{-}min}$ can be made partially retroactive with $O(\log m)$ time per $\mathrm{Insert}$ or $\mathrm{Delete}$ of an operation, $m$ being the length of the history.

:::

The updates do not commute (a delete-min takes the smallest *present* key), so a retroactive change can cascade. Draw an insertion of key $k$ at time $t$ as a horizontal ray from $(t,k)$ to the right and a delete-min at time $s$ as a vertical ray from $(s,-\infty)$ up to the ray of the key it removes; each pair forms an upside-down $L$.

::: {#fig-retroactive-data-structures-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.45cm]
\draw[faint] (0,0) -- (8,0);
\foreach \t in {1,...,7} \node[lab,tick] at (\t,-0.7) {$\t$};
\draw[hl] (1,3) -- (3,3) -- (3,0);
\draw[hl] (4,1) -- (5,1) -- (5,0);
\draw[hl] (6,4) -- (7,4) -- (7,0);
\draw[emph] (2,5) -- (8,5);
\node[lab, anchor=east] at (1,3) {$3$};
\node[lab, anchor=east] at (4,1) {$1$};
\node[lab, anchor=east] at (6,4) {$4$};
\node[lab, anchor=east] at (2,5) {$5$};
\end{tikzpicture}
\end{center}
```

The history insert $3$, insert $5$, delete-min, insert $1$, delete-min, insert $4$, delete-min (times $1$–$7$). Each upside-down $L$ is a key and the delete-min that removes it; $5$ is never removed and stays a ray.

:::

::: {#def-retroactive-bridge .definition name="Bridge"}

Write $Q_t$ for the queue just before time $t$ and $Q_{\mathrm{now}}$ for the present one. A time $t$ is a *bridge* if $Q_t\subseteq Q_{\mathrm{now}}$.

:::

::: {#lem-retroactive-bridge .lemma name="What a retroactive insert changes"}

Let $\mathrm{Insert}(t,\text{"insert}(k)\text{"})$ be executed and let $t'\le t$ be the last bridge. The only change to $Q_{\mathrm{now}}$ is that the key

$$
\max\bigl(\{k\}\cup\{k'\notin Q_{\mathrm{now}} : k'\text{ inserted at time}\ge t'\}\bigr)
$$

is added; equivalently this is $\max\bigl(\{k\}\cup\{k':k'\text{ deleted at time}\ge t\}\bigr)$.

:::

::: {.proof}

The first form is the lecture's statement of the effect of the cascade of changed deletions; the second, the key at the end of the chain of $L$'s, is the same quantity without bridges. We do not reprove their equality here: it was confirmed by running both formulas against a simulation on several thousand random histories. Bridges make the first form usable, because it mentions insertions only.

:::

The structure that gives $O(\log m)$ keeps (i) $Q_{\mathrm{now}}$ in a balanced search tree, (ii) a balanced search tree of all insertions in time order, each node storing the maximum key *not in* $Q_{\mathrm{now}}$ in its subtree, and (iii) a balanced search tree of all updates in time order whose leaf values are $0$ for an insertion of a key in $Q_{\mathrm{now}}$, $+1$ for any other insertion and $-1$ for a delete-min, with subtree sums. A bridge is a time whose prefix sum is $0$, so (iii) finds $t'$ in $O(\log m)$; (ii) then returns the maximum over the suffix from $t'$ in $O(\log m)$; and the three trees are updated in $O(\log m)$.

::: {#rmk-retroactive-data-structures-1 .remark name="Other results"}

A queue is $O(1)$ partially and $O(\log m)$ fully retroactive; a deque and union-find $O(\log m)$ fully; a priority queue $O(\sqrt{m}\log m)$ fully (any partially retroactive structure becomes fully retroactive with $O(\sqrt m)$ overhead, and improving this is open); successor is $O(\log m)$ fully by Giora and Kaplan. Non-oblivious retroactive priority queues need $O(\log m)$ per operation and tell the algorithm the position of the first crossing or floating error. In the cell-probe model a lower bound of $\Omega(r/\log r)$ is known for some structures, by a reduction to a dynamic FFT; $\Omega(r)$ is open.

:::
