<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-1-q1" status="draft"}
a) $(1,1,1)$, $(1,-1,-1)$, $(-1,1,-1)$, $(-1,-1,1)$: the vertices with an even number of minus signs. Any two of them differ in exactly two coordinates, each by $2$, so every edge has length $\sqrt{2^2+2^2}=2\sqrt2$. (Each edge is a diagonal of a face of the cube.)

b) $\cos\theta=\dfrac{\langle1,1,1\rangle\cdot\langle1,-1,-1\rangle}{\sqrt3\sqrt3}=-\dfrac13$, so $\theta\approx109.5^\circ$.

c) From $(1,1,1)$ the edges to $(1,-1,-1)$ and $(-1,1,-1)$ are $\langle0,-2,-2\rangle$ and $\langle-2,0,-2\rangle$: $\cos\theta=\frac{4}{8}=\frac12$, $\theta=60^\circ$, as it must be since every face is an equilateral triangle. Opposite edges, e.g. $\langle0,-2,-2\rangle$ (from $(1,1,1)$ to $(1,-1,-1)$) and $\langle0,-2,2\rangle$ (from $(-1,1,-1)$ to $(-1,-1,1)$), have dot product $0+4-4=0$: they are perpendicular. By symmetry: they are diagonals of the two opposite faces $x=1$ and $x=-1$ of the cube, and the two diagonals of a square are perpendicular.

d) An equilateral triangle of side $2\sqrt2$: area $\frac{\sqrt3}4(2\sqrt2)^2=2\sqrt3$. (Check: $\frac12\lvert\langle0,-2,-2\rangle\times\langle-2,0,-2\rangle\rvert=\frac12\lvert\langle4,4,-4\rangle\rvert=2\sqrt3$.)
:::

::: {.solution for="prob-mit1802f07-1-q3" status="draft"}
Let $O$ be the fixed vertex and $\mathbf{A},\mathbf{B},\mathbf{C}$ the edges from $O$; label them so that $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})>0$ (otherwise exchange $\mathbf{B}$ and $\mathbf{C}$). For a face with sides $\mathbf{U},\mathbf{V}$, $\frac12\mathbf{U}\times\mathbf{V}$ is perpendicular to it with length its area (@thm-cross-product-geometry); we only have to choose the outward sign.

1. Face $OAB$: $\frac12\mathbf{A}\times\mathbf{B}$ has positive dot product with $\mathbf{C}$, so it points towards the fourth vertex, inwards. The outward vector is $\frac12\mathbf{B}\times\mathbf{A}$. In the same way the faces $OBC$ and $OCA$ give $\frac12\mathbf{C}\times\mathbf{B}$ and $\frac12\mathbf{A}\times\mathbf{C}$.

2. The fourth face has sides $\mathbf{B}-\mathbf{A}$ and $\mathbf{C}-\mathbf{A}$ from the vertex $A$. Take $\mathbf{N}=\frac12(\mathbf{B}-\mathbf{A})\times(\mathbf{C}-\mathbf{A})=\frac12(\mathbf{B}\times\mathbf{C}+\mathbf{A}\times\mathbf{B}+\mathbf{C}\times\mathbf{A})$. The vector from this face to $O$ is $-\mathbf{A}$, and $\mathbf{N}\cdot(-\mathbf{A})=-\frac12\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})<0$: $\mathbf{N}$ points away from $O$, outwards.

3. Sum: $\frac12\big(\mathbf{B}\times\mathbf{A}+\mathbf{C}\times\mathbf{B}+\mathbf{A}\times\mathbf{C}+\mathbf{B}\times\mathbf{C}+\mathbf{A}\times\mathbf{B}+\mathbf{C}\times\mathbf{A}\big)=\mathbf{0}$, since $\mathbf{U}\times\mathbf{V}=-\mathbf{V}\times\mathbf{U}$.
:::

::: {.solution for="prob-mit1802n-1c-q1" status="draft"}
a) $-1-8=-9$.  b) $-6-4=-10$.
:::

::: {.solution for="prob-mit1802n-1c-q2" status="draft"}
a) $-1\begin{vmatrix}2&2\\-2&-1\end{vmatrix}-0+4\begin{vmatrix}1&2\\3&-2\end{vmatrix}=-1\cdot2+4\cdot(-8)=-34$.

b) $-1\begin{vmatrix}2&2\\-2&-1\end{vmatrix}-1\begin{vmatrix}0&4\\-2&-1\end{vmatrix}+3\begin{vmatrix}0&4\\2&2\end{vmatrix}=-2-8-24=-34$.
:::

::: {.solution for="prob-mit1802n-1c-q3" status="draft"}
By @thm-plane-determinant-area the area is half the absolute value of the determinant of two sides from one vertex.

a) $\frac12\left|\begin{vmatrix}1&2\\1&-1\end{vmatrix}\right|=\frac12|-3|=\frac32$.

b) Sides from $(1,2)$: $\langle0,-3\rangle$ and $\langle1,1\rangle$; $\frac12\left|\begin{vmatrix}0&-3\\1&1\end{vmatrix}\right|=\frac32$.
:::

::: {.solution for="prob-mit1802n-1c-q5" status="draft"}
a) $\begin{vmatrix}a&b\\c+ka&d+kb\end{vmatrix}=a(d+kb)-b(c+ka)=ad-bc$.

b) $\begin{vmatrix}a&b+ka\\c&d+kc\end{vmatrix}=a(d+kc)-c(b+ka)=ad-bc$.
:::

::: {.solution for="prob-mit1802n-1c-q6" status="draft"}
Expand along the first row, which does not change: $\det=a_1M_1-a_2M_2+a_3M_3$, where each minor $M_j$ is a $2\times2$ determinant formed from rows 2 and 3. Adding $k\cdot$(row 3) to row 2 adds to the first row of each minor $k$ times its second row; by Exercise 5a (with the roles of the two rows exchanged, the same computation) this does not change $M_j$. So the determinant is unchanged.
:::

::: {.solution for="prob-mit1802n-1c-q7" status="draft"}
By @thm-plane-determinant-area, $f=\pm$ the area of the parallelogram spanned by the two unit vectors, which is $\sin\theta$ for the angle $\theta$ from the first to the second. So $f\le1$, with $f=1$ when the second vector is the first turned $90^\circ$ counterclockwise (e.g. $(1,0),(0,1)$). The maximum is $1$.
:::

::: {.solution for="prob-mit1802n-1d-q1" status="draft"}
a) $\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&-2&1\\2&-1&-1\end{vmatrix}=3\mathbf{i}+3\mathbf{j}+3\mathbf{k}$.

b) $\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&0&-3\\1&1&-1\end{vmatrix}=3\mathbf{i}-\mathbf{j}+2\mathbf{k}$.
:::

::: {.solution for="prob-mit1802n-1d-q2" status="draft"}
$\overrightarrow{PQ}=\langle1,1,-1\rangle$, $\overrightarrow{PR}=\langle-3,1,-2\rangle$, $\overrightarrow{PQ}\times\overrightarrow{PR}=\langle-1,5,4\rangle$. Area $=\frac12\sqrt{1+25+16}=\frac{\sqrt{42}}2$.
:::

::: {.solution for="prob-mit1802n-1d-q3" status="draft"}
$\mathbf{A}\cdot\mathbf{B}=0$, so the directions are perpendicular. $\mathbf{i}'=\frac1{\sqrt5}(2\mathbf{i}-\mathbf{j})$, $\mathbf{j}'=\frac1{\sqrt6}(\mathbf{i}+2\mathbf{j}+\mathbf{k})$, and $\mathbf{k}'=\mathbf{i}'\times\mathbf{j}'=\frac1{\sqrt{30}}\,\mathbf{A}\times\mathbf{B}=\frac1{\sqrt{30}}(-\mathbf{i}-2\mathbf{j}+5\mathbf{k})$.
:::

::: {.solution for="prob-mit1802n-1d-q4" status="draft"}
$(\mathbf{i}\times\mathbf{i})\times\mathbf{j}=\mathbf{0}\times\mathbf{j}=\mathbf{0}$, while $\mathbf{i}\times(\mathbf{i}\times\mathbf{j})=\mathbf{i}\times\mathbf{k}=-\mathbf{j}$.
:::

::: {.solution for="prob-mit1802n-1d-q5" status="draft"}
Assume $\mathbf{A},\mathbf{B}\ne\mathbf{0}$ (otherwise both equations hold trivially) and let $\theta\in[0,\pi]$ be their angle.

a) $|\mathbf{A}||\mathbf{B}|\sin\theta=|\mathbf{A}||\mathbf{B}|$ means $\sin\theta=1$: $\mathbf{A}\perp\mathbf{B}$.

b) $\sin\theta=\cos\theta$ means $\theta=\pi/4$.
:::

::: {.solution for="prob-mit1802n-1d-q7" status="draft"}
$\overrightarrow{PQ}=\langle-2,1,1\rangle$, $\overrightarrow{PR}=\langle-1,0,1\rangle$, $\overrightarrow{PS}=\langle2,1,-2\rangle$, and $\det(\overrightarrow{PQ},\overrightarrow{PR},\overrightarrow{PS})=1$ (@thm-triple-product). Volume $=\frac16$.
:::
