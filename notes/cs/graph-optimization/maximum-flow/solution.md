<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-1-q5" status="draft"}
1. By max-flow min-cut (@thm-max-flow-min-cut), $\lambda_{st}$ is the capacity of some $s$–$t$ cut $(S,V\setminus S)$, $s\in S$, $t\notin S$ (capacity of the arcs from $S$ to $V\setminus S$).

2. If $u\in S$, the same cut separates $u$ from $t$, so its capacity is at least $\lambda_{ut}$.

3. If $u\notin S$, it separates $s$ from $u$, so its capacity is at least $\lambda_{su}$.

4. In either case $\lambda_{st}\ge\min(\lambda_{su},\lambda_{ut})$. (If $u=s$ or $u=t$ the claim is trivial.)
:::

::: {.solution for="prob-mit6854ps-3-q5" status="draft"}
*1.* Give the conservation row of vertex $i$ (written with $w$ moved to the left) a free multiplier $z_i$ and the capacity row of $(i,j)$ a multiplier $y_{ij}\ge0$. The column of $x_{ij}\ge0$ has $+1$ in row $i$, $-1$ in row $j$ and $+1$ in its capacity row, and objective $0$: $z_i-z_j+y_{ij}\ge0$. The column of $w$ (free) has $-1$ in row $s$, $+1$ in row $t$ and objective $1$: $z_t-z_s=1$. The dual objective is $\sum u_{ij}y_{ij}$ (the conservation rows have right side $0$). Adding a constant to all $z_i$ changes nothing, so we may fix $z_s=0$, $z_t=1$.

*2.* Put $z_i=0$ for $i\in S$, $z_i=1$ otherwise, and $y_{ij}=1$ if $i\in S$, $j\notin S$, else $0$. The constraint $z_i-z_j+y_{ij}\ge0$ reads $0-1+1$, $1-0+0$ or $0+0$, all $\ge0$. The objective is $\sum_{i\in S,j\notin S}u_{ij}=U(S:\bar S)$.

*3.* For $0<\theta\le1$ let $S_\theta=\{i:z^*_i<\theta\}$; it contains $s$ and not $t$. An edge $(i,j)$ leaves $S_\theta$ exactly when $z^*_i<\theta\le z^*_j$. Choose $\theta$ uniformly in $(0,1]$:
$$\mathbb E\,U(S_\theta:\bar S_\theta)=\sum_{(i,j)}u_{ij}\Pr[z^*_i<\theta\le z^*_j]\le\sum_{(i,j)}u_{ij}\max(0,z^*_j-z^*_i)\le\sum u_{ij}y^*_{ij}.$$
By strong duality the right side is the maximum flow value $w^*$, so some $S_\theta$ has capacity at most $w^*$; by 2 and weak duality every cut has capacity at least $w^*$, so this cut has capacity exactly $w^*$. Only the at most $n$ distinct sets $S_\theta$ (thresholds at the values $z^*_i$) need to be tried.
:::
