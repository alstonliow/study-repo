<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-6-q1" status="draft"}
(a) *$r=w_{ij}$:* nothing changes, $O(1)$. *$r<w_{ij}$:* a new shortest $a\to b$ path either avoids $(i,j)$, and then $D_{ab}$ is still right, or uses it once (weights are non-negative), and then it is a shortest $a\to i$ path, the edge, and a shortest $j\to b$ path. So set $D'_{ab}=\min\{D_{ab},\ D_{ai}+r+D_{jb}\}$ for all $a,b$; when the second term wins, set $\Pi'_{ab}=\Pi_{jb}$ (or $i$ if $b=j$). $O(V^2)$. *$r>w_{ij}$:* distances can only grow, and only for pairs whose shortest paths all used $(i,j)$; in the worst case almost all pairs, so recompute: Floyd–Warshall in $O(V^3)$ (or Dijkstra from the affected sources).

(b) Let $V=\{i,j\}\cup A\cup B$ with $|A|=|B|=\frac{n-2}2$, edges $a\to i$ and $j\to b$ of weight $0$ for $a\in A$, $b\in B$, and $(i,j)$ of weight $2$ as the only route from $A$ to $B$. Lowering $w_{ij}$ to $1$ changes $D_{ab}$ for all $|A||B|=\Theta(V^2)$ pairs, and any algorithm must write each of these entries.

(c) Add a hop index: $D^{(k)}_{uv}[\ell]$ = shortest $u\to v$ path with at most $\ell$ edges and intermediate vertices in $\{1,\dots,k\}$, for $0\le\ell\le h$. Then $D^{(k)}_{uv}[\ell]=\min\bigl\{D^{(k-1)}_{uv}[\ell],\ \min_{\ell_1+\ell_2=\ell}D^{(k-1)}_{uk}[\ell_1]+D^{(k-1)}_{kv}[\ell_2]\bigr\}$ (as in @thm-floyd-warshall), with $D^{(0)}_{uv}[\ell]=w_{uv}$ for $\ell\ge1$ (and $0$ on the diagonal). $O(n^3h^2)$ time, $O(n^2h)$ space.

(d) $D^{(a+b)}=D^{(a)}\otimes D^{(b)}$ (@prp-shortest-paths-by-squaring), so compute $W^{\otimes h}$ by repeated squaring and multiplying the powers given by the binary digits of $h$: $O(\lg h)$ min-plus products, $O(n^3\lg h)$ time.

(e) Keep the matrices $D^{(\ell)}$ for all $\ell\le h$ (at most $\ell$ hops). *$r=w_{ij}$:* nothing. *$r<w_{ij}$:* for each $\ell$, $D'^{(\ell)}_{ab}=\min\bigl\{D^{(\ell)}_{ab},\ \min_{\ell_1+\ell_2=\ell-1}D^{(\ell_1)}_{ai}+r+D^{(\ell_2)}_{jb}\bigr\}$, where the old matrices may be used on both sides because a shortest path uses the edge at most once: $O(n^2h^2)$. *$r>w_{ij}$:* recompute all $D^{(\ell)}$ by $D^{(\ell)}=D^{(\ell-1)}\otimes W'$: $O(n^3h)$ (or only $D^{(h)}$ in $O(n^3\lg h)$ if the extra matrices are rebuilt lazily).
:::
