::: {.problem #prob-mit1806s10-3-q1 origin="external" source="mit1806s10-3-q1"}
The plane $x-3y-z=12$ is parallel to the plane $x-3y-z=0$ in Problem 17. One particular point on this plane is $(12,0,0)$. All points on the plane have the form (fill in the first components)
$$\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}\ \\0\\0\end{bmatrix}+y\begin{bmatrix}\ \\1\\0\end{bmatrix}+z\begin{bmatrix}\ \\0\\1\end{bmatrix}.$$
:::

::: {.problem #prob-mit1806s10-3-q10 origin="external" source="mit1806s10-3-q10"}
Explain why these are all false:

(a) The complete solution is any linear combination of $\mathbf{x}_p$ and $\mathbf{x}_n$.

(b) A system $A\mathbf{x}=\mathbf{b}$ has at most one particular solution.

(c) The solution $\mathbf{x}_p$ with all free variables zero is the shortest solution (minimum length $\lVert\mathbf{x}\rVert$). Find a 2 by 2 counterexample.

(d) If $A$ is invertible there is no solution $\mathbf{x}_n$ in the nullspace.
:::

::: {.problem #prob-mit1806s10-3-q11 origin="external" source="mit1806s10-3-q11"}
Write down all known relations between $r$ and $m$ and $n$ if $A\mathbf{x}=\mathbf{b}$ has

(a) no solution for some $\mathbf{b}$

(b) infinitely many solutions for every $\mathbf{b}$

(c) exactly one solution for some $\mathbf{b}$, no solution for other $\mathbf{b}$

(d) exactly one solution for every $\mathbf{b}$.
:::

::: {.problem #prob-mit1806s10-3-q12 origin="external" source="mit1806s10-3-q12"}
Apply Gauss-Jordan elimination to $U\mathbf{x}=\mathbf{0}$ and $U\mathbf{x}=\mathbf{c}$. Reach $R\mathbf{x}=\mathbf{0}$ and $R\mathbf{x}=\mathbf{d}$:
$$\begin{bmatrix}U&\mathbf{0}\end{bmatrix}=\begin{bmatrix}1&2&3&0\\0&0&4&0\end{bmatrix}\qquad\text{and}\qquad\begin{bmatrix}U&\mathbf{c}\end{bmatrix}=\begin{bmatrix}1&2&3&5\\0&0&4&8\end{bmatrix}.$$
Solve $R\mathbf{x}=\mathbf{0}$ to find $\mathbf{x}_n$ (its free variable is $x_2=1$). Solve $R\mathbf{x}=\mathbf{d}$ to find $\mathbf{x}_p$ (its free variable is $x_2=0$).
:::

::: {.problem #prob-mit1806s10-3-q13 origin="external" source="mit1806s10-3-q13"}
Suppose $K$ is the 9 by 9 second difference matrix (2's on the diagonal, -1's on the diagonal above and also below). Solve the equation $K\mathbf{x}=\mathbf{b}=(10,\dots,10)$. If you graph $x_1,\dots,x_9$ above the points $1,\dots,9$ on the $x$ axis, I think the nine points fall on a parabola.
:::

::: {.problem #prob-mit1806s10-3-q14 origin="external" source="mit1806s10-3-q14"}
Suppose $A\mathbf{x}=\mathbf{b}$ and $C\mathbf{x}=\mathbf{b}$ have the same (complete) solutions for every $\mathbf{b}$. Is it true that $A=C$?
:::
