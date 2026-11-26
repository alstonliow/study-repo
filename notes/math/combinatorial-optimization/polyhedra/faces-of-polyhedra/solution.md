<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-3-q4" status="draft"}
By @thm-faces-tight-rows a non-empty face is obtained by deciding, for each coordinate $i$, which of the rows $x_i\ge0$, $x_i\le1$ are tight. Making both tight gives the empty set, so a non-empty face is given by choosing for each $i$ one of: $x_i$ free, $x_i=0$, $x_i=1$. Different choices give different faces, so there are $3^3=27$ non-empty faces, plus the empty face ($0^{\mathsf T}x\le1$):

1. the cube itself (all free): $1$;
2. facets (one coordinate fixed): $x_i=0$ or $x_i=1$ for $i=1,2,3$: $6$;
3. edges (two fixed): $\{x:x_i=a,\ x_j=b,\ 0\le x_l\le1\}$ for $\{i,j,l\}=\{1,2,3\}$, $a,b\in\{0,1\}$: $3\cdot4=12$;
4. vertices (all fixed): the $8$ points of $\{0,1\}^3$;
5. the empty face: $1$.

In total $1+6+12+8+1=28$.
:::

::: {.solution for="prob-mit18433-3-q5" status="draft"}
1. By @thm-faces-tight-rows every non-empty face is $F_I=\{x\ge0:x_i=0\ (i\in I)\}$ for some $I\subseteq\{1,\dots,n\}$, and each $F_I$ is a face (of $-\sum_{i\in I}x_i\le0$). The sets $F_I$ are distinct (the point with $x_i=0$ for $i\in I$ and $x_i=1$ otherwise lies in $F_I$ and in no $F_J$ with $J\not\subseteq I$), so there are $2^n$ non-empty faces. With the empty face (from $0^{\mathsf T}x\le1$) this gives $2^n+1$.

2. $F_I$ is a copy of the orthant in the $n-|I|$ free coordinates, so $\dim F_I=n-|I|$. For $0\le k\le n$ there are $\binom nk$ faces of dimension $k$, and one of dimension $-1$.
:::

::: {.solution for="prob-mit18433-3-q6" status="draft"}
We use @thm-faces-tight-rows and the first part of @thm-facets-describe-polyhedra (a row of $I^<$ whose face is not a facet is redundant).

1. Let $F$ be a maximal non-trivial face of $P=\{x:Ax\le b\}$. By @thm-faces-tight-rows, $F=F_I$ for some $I$, and $I$ contains a row $i\in I^<$ (otherwise $F_I=P$). The face $F_{\{i\}}=\{x\in P:a_i^{\mathsf T}x=b_i\}$ contains $F$, is non-empty, and is not $P$; by maximality $F=F_{\{i\}}$.

2. If $F$ is not a facet, row $i$ is redundant: deleting it leaves $P$ unchanged, and $F$ is still a maximal non-trivial face of the same polyhedron. Apply step 1 to the shorter description to get a row $i'$ with $F=F_{\{i'\}}$, and repeat.

3. Each round deletes a row, so this stops. It can only stop at a row $i''$ with $F=F_{\{i''\}}$ that is not redundant, and then $F$ is a facet.
:::
