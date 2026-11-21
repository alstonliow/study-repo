<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-3-q4" status="draft"}
1. At each node write (current out) $-$ (current in) $=0$:
   $$\begin{aligned}
   \text{node }1:&\ \ y_1-y_3+y_4=0\\
   \text{node }2:&\ -y_1+y_2+y_5=0\\
   \text{node }3:&\ -y_2+y_3+y_6=0\\
   \text{node }4:&\ -y_4-y_5-y_6=0
   \end{aligned}
   \qquad A=\begin{bmatrix}1&0&-1&1&0&0\\-1&1&0&0&1&0\\0&-1&1&0&0&1\\0&0&0&-1&-1&-1\end{bmatrix}.$$
   This $A$ is the transpose of the incidence matrix (@thm-incidence-matrix-subspaces).

2. The four rows add to zero, so the rank is $3$ and there are $6-3=3$ free variables. Take $y_3,y_5,y_6$ free (the pivots fall in columns $1,2,4$).

3. Each special solution is a current around a loop:
   $$(1,1,1,0,0,0)\ \ (\text{loop }1\to2\to3\to1),\quad (1,0,0,-1,1,0)\ \ (1\to2\to4\to1),\quad (1,1,0,-1,0,1)\ \ (1\to2\to3\to4\to1),$$
   for $(y_3,y_5,y_6)=(1,0,0),(0,1,0),(0,0,1)$. Each satisfies all four node equations.
:::

::: {.solution for="prob-mit1806s10-5-q12" status="draft"}
1. $A=\begin{bmatrix}-1&1&0&0\\-1&0&1&0\\0&-1&1&0\\0&-1&0&1\\0&0&-1&1\end{bmatrix}$, $C=\operatorname{diag}(2,2,3,3,3)$, and
   $$A^{\mathsf T}CA=\begin{bmatrix}4&-2&-2&0\\-2&8&-3&-3\\-2&-3&8&-3\\0&-3&-3&6\end{bmatrix}:$$
   each diagonal entry is the total conductance at the node, each off-diagonal entry is minus the conductance of the edge joining the nodes.

2. $A^{\mathsf T}CA$ is singular (constant potentials), so ground node 4: $x_4=0$. Solving the first three equations gives
   $$\mathbf{x}=\big(\tfrac5{12},\ \tfrac16,\ \tfrac16,\ 0\big).$$
   Check row 4: $-3\cdot\frac16-3\cdot\frac16=-1$.

3. The currents are $\mathbf{y}=-CA\mathbf{x}=\big(\tfrac12,\ \tfrac12,\ 0,\ \tfrac12,\ \tfrac12\big)$: one unit enters at node 1, splits equally along the two paths $1\to2\to4$ and $1\to3\to4$, and nothing flows on edge 3 between the two nodes of equal potential.
:::

::: {.solution for="prob-mit1806s10-5-q13" status="draft"}
a. The graph has $9$ nodes and $12$ edges and is connected, so $\operatorname{rank}A=9-1=8$ (@thm-incidence-matrix-subspaces): $8$ independent columns.

b. $\mathbf{f}$ must be in $C(A^{\mathsf T})=N(A)^{\perp}$, and $N(A)$ is the line through $(1,\dots,1)$. So $f_1+\dots+f_9=0$: the external currents must balance.

c. The sum of the degrees counts every edge twice (once at each end): $2\cdot12=24$.
:::

::: {.solution for="prob-mit18065ps-30-q3" status="draft"}
1. "Tree": connected with no loops, so a tree on $k$ nodes has exactly $k-1$ edges (@cor-euler-formula-from-rank with no loops).

2. "Spanning": the tree reaches all $N$ nodes, so it has $N-1$ edges.

3. These $N-1$ edges are chosen among the $M$ edges of the graph, so $M\ge N-1$ (with equality exactly when the connected graph is itself a tree).
:::
