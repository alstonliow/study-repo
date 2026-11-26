<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-2-q2" status="draft"}
1. If $M$ is not maximum, by Berge's theorem (@thm-berge-augmenting-path) it has an augmenting path $P$, and $M\triangle P$ is a larger matching.

2. Augmenting never uncovers a vertex: the inner vertices of $P$ stay matched (each swaps its matching edge), and the two ends, previously exposed, become matched. So $M\triangle P$ covers every vertex that $M$ covers, in particular $S$.

3. Repeating, after at most $|V|/2$ augmentations we reach a maximum matching $M^*$, which still covers $S$.
:::

::: {.solution for="prob-mit18433-2-q3" status="draft"}
1. Every edge of $M$ either has an end in $U$ or lies inside one component $K_i$ (there are no edges between components). At most $|U|$ edges of $M$ have an end in $U$, with equality only if every $u\in U$ is matched and no edge of $M$ joins two vertices of $U$; and $G[K_i]$ contains at most $\lfloor|K_i|/2\rfloor$ edges of $M$. So $|M|\le|U|+\sum_i\lfloor|K_i|/2\rfloor$, which equals $\frac12(|V|+|U|-o(G-U))$ (@lem-tutte-berge-bound).

2. $M$ is maximum and $U$ a minimiser, so by @thm-tutte-berge equality holds, hence equality in every step: each $G[K_i]$ contains exactly $\lfloor|K_i|/2\rfloor$ edges of $M$ (part 1), every $u\in U$ is matched, and not to another vertex of $U$.

3. So $u\in U$ is matched to some $v\in K_i$. If $K_i$ were even, $G[K_i]$ would be perfectly matched by edges inside $K_i$ and $v$ would already be matched inside $K_i$. Hence $K_i$ is odd (part 2).

4. All vertices of $U$ and of even components are matched, so unmatched vertices lie in odd components (part 3).
:::

::: {.solution for="prob-mit18433-2-q4" status="draft"}
There can be several. Let $G$ be a single edge $vw$. The maximum matching has size $1$. For $U=\varnothing$, $G-U$ has one even component and $\frac12(2+0-0)=1$; for $U=\{v\}$, $G-U$ is the single vertex $w$, an odd component, and $\frac12(2+1-1)=1$. Both attain the minimum. (A path on three vertices $a$–$b$–$c$ gives another example: $U=\varnothing$ and $U=\{b\}$ both give $1$.)
:::

::: {.solution for="prob-mit18433-2-q5" status="draft"}
Run Edmonds' algorithm to the end (@thm-blossom-algorithm). Let $X$ be the set of vertices of $G$ that are Even in the final shrunk graph $G'$ or lie inside a shrunk vertex (all shrunk vertices are Even), $U_0$ the Odd vertices, and $Y$ the unlabelled ones. $U_0$ is a minimiser (proof of @thm-tutte-berge). We show $B=X$ and $C=U_0$.

1. *A blossom can be matched leaving any vertex out.* If a (possibly nested) blossom expands to the vertex set $K$ and $z\in K$, then $K-z$ has a perfect matching using edges inside $K$. By induction on the nesting: the blossom is an odd cycle of parts $K_1,\dots,K_{2l+1}$ with $z\in K_j$; match the other parts in consecutive pairs along the cycle edges, and inside each part leave out the vertex used by the cycle edge (or $z$ for $K_j$), matching the rest by induction.

2. *$X\subseteq B$.* An Even vertex $w$ of $G'$ is joined to an exposed root by an even alternating path in the tree; flipping it gives a maximum matching of $G'$ leaving $w$ exposed. Expanding the blossoms as in @thm-blossom-shrinking, with step 1 used to leave out any chosen vertex $z$ of the blossom $w$ (or $z=w$), gives a maximum matching of $G$ missing $z$. So every vertex of $X$ is inessential.

3. *$B\subseteq X$.* In $G-U_0$, each Even vertex of $G'$ expands to an odd component of $G$ (a single vertex or an odd blossom), and the unlabelled vertices, matched among themselves and joined only to unlabelled or Odd vertices, form even components. By exercise 2-3 every maximum matching covers $U_0$ and all vertices of the even components. So vertices of $U_0\cup Y$ are not inessential.

4. *$C=U_0$.* In $G'$, Even vertices are adjacent only to Odd vertices; in $G$ a vertex of $X$ is adjacent only to vertices of its own blossom (in $X$) or of $U_0$. So $C=N(B)\setminus B\subseteq U_0$. Conversely every Odd vertex was labelled from an Even neighbour, so $U_0\subseteq C$.

5. Hence $U=C=U_0$ attains the minimum, and the odd components of $G-C$ are exactly the blossoms and Even vertices, whose union is $B$.
:::

::: {.solution for="prob-mit18433-2-q6" status="draft"}
We check Tutte's condition (@cor-tutte-perfect-matching).

1. $3|V|=2|E|$, so $|V|$ is even; $G$ is connected, so $o(G-\varnothing)=0$.

2. Let $U\ne\varnothing$ and let $K$ be an odd component of $G-U$. The degrees in $K$ add up to $3|K|$, which is odd; edges inside $K$ contribute $2$ each, so the number of edges leaving $K$, all of which go to $U$, is odd. As $G$ is $2$-edge-connected and $K\ne V$, it is at least $2$, hence at least $3$.

3. Counting the edges between $U$ and the odd components, $3\,o(G-U)\le\sum_{u\in U}\deg u=3|U|$. So $o(G-U)\le|U|$ for every $U$, and $G$ has a perfect matching.
:::

::: {.solution for="prob-mit18433-2-q7" status="draft"}
Let $n=|V|$; it is odd, as $G-v$ has a perfect matching, so $\nu(G)=\frac{n-1}2$.

1. *$U=\varnothing$.* If a minimiser $U$ contained a vertex $u$, then by exercise 2-3 every maximum matching would cover $u$. But a perfect matching of $G-u$ has $\frac{n-1}2=\nu(G)$ edges, so it is a maximum matching of $G$ missing $u$: a contradiction.

2. *The final graph is one vertex.* At termination the set of Odd vertices is a minimiser (proof of @thm-tutte-berge), so there are no Odd vertices. Then no tree has grown: the Even vertices of the final graph $G'$ have no edges to Even, unlabelled or (non-existent) Odd vertices, so they are isolated. $G$ is connected: if it had components $G_1\ne G_2$, deleting a vertex of $G_1$ would need $G_1$ minus that vertex to be perfectly matchable, so $|G_1|$ is odd, while deleting a vertex of $G_2$ would need $G_1$ itself to be perfectly matchable, so $|G_1|$ is even. Hence $G'$ is connected too. It contains an exposed vertex, which is Even and isolated, so $G'$ is that single vertex.

3a. *Odd ears preserve factor-criticality.* An odd cycle is factor-critical. Let $H$ be factor-critical and add an odd ear $v_0,\dots,v_k$ with new vertices $v_1,\dots,v_{k-1}$ (an even number). To delete a vertex $z$ of $H$: take a perfect matching of $H-z$ and the edges $v_1v_2,v_3v_4,\dots,v_{k-2}v_{k-1}$. To delete $v_i$ with $i$ odd: match $v_1,\dots,v_{i-1}$ in consecutive pairs, match $v_{i+1}v_{i+2},\dots,v_{k-1}v_k$ (an odd number of vertices $v_{i+1},\dots,v_{k-1}$ plus $v_k$), and use a perfect matching of $H-v_k$. For $i$ even, symmetrically pair $v_0v_1,\dots,v_{i-2}v_{i-1}$, pair $v_{i+1},\dots,v_{k-1}$ among themselves, and use a perfect matching of $H-v_0$. (If $v_0=v_k$ the same works.)

3b. *Converse.* By part 2, Edmonds' algorithm (in its last round) shrinks blossoms $B_1,\dots,B_k$ and ends with a single vertex; let $G_0=G,\dots,G_k$ be the shrunk graphs, kept as multigraphs so that each edge is an edge of $G$. We show by backward induction that each $G_i$ has an odd ear decomposition. $G_k$ is a single vertex; $G_{k-1}$ has vertex set $B_k$, an odd cycle plus chords, so: the cycle, then the chords as trivial ears. For the step from $G_i$ to $G_{i-1}$, the vertex $b_i$ of $G_i$ is expanded into the odd cycle $C_i$ of $B_i$. In the decomposition of $G_i$, $b_i$ is an inner vertex of exactly one ear (or of the starting cycle) and an end of some later ears. Where that ear passes through $b_i$, its two edges now end at vertices $p,q$ of $C_i$; the two paths of $C_i$ from $p$ to $q$ have lengths of different parity (their sum $|C_i|$ is odd). Route the ear through the even one (length $0$ if $p=q$), which keeps it odd, and add the odd one as the next ear (if $p=q$, the whole cycle $C_i$ as a closed odd ear). Then add the chords of $B_i$ as trivial ears; later ears ending at $b_i$ now end at a vertex of $C_i$. This is an odd ear decomposition of $G_{i-1}$, and for $i=1$ of $G$.
:::
