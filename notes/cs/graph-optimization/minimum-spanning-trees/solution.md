<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-6-q2" status="draft"}
(a) Suppose $T\ne T'$ are both MSTs, and let $e$ be the lightest edge in exactly one of them, say $e\in T\setminus T'$. Adding $e$ to $T'$ closes a cycle, which contains an edge $e'\notin T$ (else $T$ would contain a cycle). Then $e'\in T'\setminus T$, so $w(e')>w(e)$ by the choice of $e$ and distinct weights, and $T'+e-e'$ is a spanning tree lighter than $T'$: a contradiction.

(b) *Correct* (this is Borůvka's algorithm). Each $e_C$ is the lightest edge crossing the cut $(C,V\setminus C)$, which respects $A$, so by @thm-cut-property it lies in an MST, which by (a) is *the* MST. All edges added in a phase belong to the one MST, so together they form no cycle. Each component merges with at least one other in every phase, so the number of components at least halves: $O(\lg V)$ phases, each $O(V+E)$ (label components by DFS, then one scan of the edges): $O(E\lg V)$.

(c) *Incorrect.* Take $V_1=\{a,b\}$, $V_2=\{c,d\}$ with edges $ab$ ($10$), $cd$ ($11$), $ac$ ($1$), $bd$ ($2$), $bc$ ($3$). The algorithm returns $\{ab,cd,ac\}$ of weight $22$, while $\{ac,bd,bc\}$ weighs $6$.

(d) *Correct.* The heaviest edge of a cycle is in no MST: if it were in the MST $T$, removing it splits $T$ in two, the cycle crosses that cut at another, lighter edge, and swapping gives a lighter tree. So every removed edge is outside the unique MST, the MST survives every phase (in particular the graph stays connected), and when only a spanning tree is left, it is the MST. Efficiently: each phase finds one cycle by DFS in $O(V+E)$ and removes its heaviest edge; there are $E-V+1$ phases, $O(E(V+E))$ in total (the reverse-delete algorithm is a faster implementation of the same idea).
:::
