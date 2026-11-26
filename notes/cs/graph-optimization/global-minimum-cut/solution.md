<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-4-q4" status="draft"}
1. Give every edge capacity $1$ and take a maximum adjacency order $v_1,\dots,v_n$ (@def-stoer-wagner). By @lem-maximum-adjacency-cut, $\delta(\{v_n\})$ is a minimum $v_{n-1}$–$v_n$ cut, of capacity $\deg(v_n)\ge k$. So every cut separating $s=v_{n-1}$ from $t=v_n$ has at least $k$ edges.

2. Replace each edge by two opposite arcs. Every $s$–$t$ cut of the digraph has at least $k$ arcs, so by Menger's theorem (@thm-menger-arc-disjoint) there are $k$ arc-disjoint directed $s$–$t$ paths; equivalently an integral flow of value $k$ with $0$–$1$ values.

3. If some edge $uv$ carries flow in both directions, cancel both units: conservation and the value are kept. Then each edge is used in at most one direction, and decomposing the flow as in the proof of @thm-menger-arc-disjoint gives $k$ edge-disjoint $s$–$t$ paths in $G$.
:::
