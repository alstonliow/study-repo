<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-3-q1" status="draft"}
1. Solve the equation for the pivot variable: $x=12+3y+z$, with $y,z$ free.

2. So
   $$\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}12\\0\\0\end{bmatrix}+y\begin{bmatrix}3\\1\\0\end{bmatrix}+z\begin{bmatrix}1\\0\\1\end{bmatrix}:$$
   a particular solution plus the nullspace of $[1\ \ {-3}\ \ {-1}]$, which is the parallel plane through the origin (@thm-complete-solution).
:::

::: {.solution for="prob-mit1806s10-3-q10" status="draft"}
(a) The coefficient of $\mathbf{x}_p$ must be exactly $1$: $A(c\mathbf{x}_p+\mathbf{x}_n)=c\mathbf{b}$, which is $\mathbf{b}$ only for $c=1$ (when $\mathbf{b}\ne\mathbf{0}$).

(b) Any $\mathbf{x}_p+\mathbf{x}_n$ with $\mathbf{x}_n\in N(A)$ is also a particular solution; if $N(A)\ne\{\mathbf{0}\}$ there are infinitely many.

(c) Take $A=\begin{bmatrix}1&1\\1&1\end{bmatrix}$, $\mathbf{b}=(1,1)$. The solutions form the line $x_1+x_2=1$. Setting the free variable $x_2=0$ gives $\mathbf{x}_p=(1,0)$ of length $1$, but $(\frac12,\frac12)$ is also a solution, of length $\frac1{\sqrt2}<1$. (The shortest solution lies in the row space; see @thm-pseudoinverse-properties.)

(d) $\mathbf{x}_n=\mathbf{0}$ is always in the nullspace. For invertible $A$ it is the only one.
:::

::: {.solution for="prob-mit1806s10-3-q11" status="draft"}
Always $r\le m$ and $r\le n$. By @thm-rank-and-solutions:

(a) Some $\mathbf{b}$ unreachable: $r<m$.

(b) Always solvable ($r=m$) with free variables ($r<n$): $r=m<n$.

(c) Unique when solvable ($r=n$) but not always solvable ($r<m$): $r=n<m$.

(d) Always solvable and unique: $r=m=n$.
:::

::: {.solution for="prob-mit1806s10-3-q12" status="draft"}
1. Divide row 2 by $4$, then subtract $3$ times row 2 from row 1:
   $$\begin{bmatrix}1&2&0&0\\0&0&1&0\end{bmatrix},\qquad\begin{bmatrix}1&2&0&-1\\0&0&1&2\end{bmatrix}.$$
   So $R=\begin{bmatrix}1&2&0\\0&0&1\end{bmatrix}$ and $\mathbf{d}=(-1,2)$.

2. $R\mathbf{x}=\mathbf{0}$ with $x_2=1$: $x_3=0$, $x_1=-2$, so $\mathbf{x}_n=(-2,1,0)$.

3. $R\mathbf{x}=\mathbf{d}$ with $x_2=0$: $x_3=2$, $x_1=-1$, so $\mathbf{x}_p=(-1,0,2)$. Check in the original system: $U\mathbf{x}_p=(-1+6,\ 8)=(5,8)=\mathbf{c}$.
:::

::: {.solution for="prob-mit1806s10-3-q13" status="draft"}
1. Row $i$ of $K\mathbf{x}=\mathbf{b}$ says $-x_{i-1}+2x_i-x_{i+1}=10$, with $x_0=x_{10}=0$: the second difference of $\mathbf{x}$ is the constant $-10$.

2. A quadratic $x_i=c\,i(10-i)$ vanishes at $i=0$ and $i=10$ and has constant second difference: $-x_{i-1}+2x_i-x_{i+1}=c\big(-(i-1)(11-i)+2i(10-i)-(i+1)(9-i)\big)=2c$. So $c=5$.

3. Since $K$ is invertible (its pivots are positive), this is the solution:
   $$\mathbf{x}=(45,80,105,120,125,120,105,80,45),$$
   and the points do lie on the parabola $y=5x(10-x)$. A numerical solve confirms these values.
:::

::: {.solution for="prob-mit1806s10-3-q14" status="draft"}
1. Yes. It is enough to show $A\mathbf{y}=C\mathbf{y}$ for every vector $\mathbf{y}$ (take $\mathbf{y}=\mathbf{e}_j$ to compare column $j$).

2. Given $\mathbf{y}$, set $\mathbf{b}=A\mathbf{y}$. Then $\mathbf{y}$ solves $A\mathbf{x}=\mathbf{b}$, so by hypothesis it also solves $C\mathbf{x}=\mathbf{b}$: $C\mathbf{y}=\mathbf{b}=A\mathbf{y}$.
:::
