<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-4-q1" status="draft"}
1. Every $\mathbf{v}_i$ has components adding to $0$, so all six lie in the subspace $x_1+x_2+x_3+x_4=0$ of dimension $3$ (see @sec-math-linear-algebra-vector-spaces-matrix-spaces-and-rank-one). At most $3$ of them can be independent (@cor-basis-from-independent-set).

2. Explicitly: $\mathbf{v}_4=\mathbf{v}_2-\mathbf{v}_1$, $\mathbf{v}_5=\mathbf{v}_3-\mathbf{v}_1$, $\mathbf{v}_6=\mathbf{v}_3-\mathbf{v}_2$.

3. $\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$ are independent: in $c_1\mathbf{v}_1+c_2\mathbf{v}_2+c_3\mathbf{v}_3=\mathbf{0}$, components $2,3,4$ give $-c_1=-c_2=-c_3=0$. So the answer is $3$.
:::

::: {.solution for="prob-mit1806s10-4-q2" status="draft"}
1. The plane is $N([1\ \ {-2}\ \ 3])$, with free variables $y,z$. The special solutions $(2,1,0)$ and $(-3,0,1)$ are a basis.

2. Intersecting with the $xy$ plane adds $z=0$, leaving the line $x=2y$, $z=0$. Basis: $(2,1,0)$.

3. Vectors perpendicular to the plane form its orthogonal complement, the row space of $[1\ \ {-2}\ \ 3]$ (@thm-fundamental-theorem-orthogonality), of dimension $3-2=1$. Basis: $(1,-2,3)$.
:::

::: {.solution for="prob-mit1806s10-6-q5" status="draft"}
1. A hyperplane through $\mathbf{0}$ is an $(n-1)$-dimensional subspace, $\{\mathbf{x}:\mathbf{w}^{\mathsf T}\mathbf{x}=0\}$ for some $\mathbf{w}\neq\mathbf{0}$. It contains the points exactly when $\mathbf{w}$ is in the nullspace of the $(n-1)\times n$ matrix $A$ with rows $\mathbf{a}_i^{\mathsf T}$.

2. There is exactly one such hyperplane when $N(A)$ is a line, i.e. $\operatorname{rank}A=n-1$: the vectors $\mathbf{a}_1,\dots,\mathbf{a}_{n-1}$ are linearly independent. If they are dependent, $\dim N(A)\ge2$ and there are infinitely many.

3. For $n=3$: exactly one plane unless $\mathbf{a}_1$ and $\mathbf{a}_2$ are dependent, i.e. $\mathbf{0},\mathbf{a}_1,\mathbf{a}_2$ lie on one line.
:::
