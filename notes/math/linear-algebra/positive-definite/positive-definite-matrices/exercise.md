::: {.problem #prob-mit1806s10-9-q1 origin="external" source="mit1806s10-9-q1"}
With positive pivots in $D$, the factorization $A=LDL^{\mathsf T}$ becomes $L\sqrt D\sqrt DL^{\mathsf T}$. (Square roots of the pivots give $D=\sqrt D\sqrt D$.) Then $C=\sqrt DL^{\mathsf T}$ yields the *Cholesky factorization* $A=C^{\mathsf T}C$ which is "symmetrized $LU$".
$$\text{From}\quad C=\begin{bmatrix}3&1\\0&2\end{bmatrix}\quad\text{find }A.\qquad\text{From}\quad A=\begin{bmatrix}4&8\\8&25\end{bmatrix}\quad\text{find }C=\mathbf{chol}(A).$$
:::

::: {.problem #prob-mit1806s10-9-q2 origin="external" source="mit1806s10-9-q2"}
In the Cholesky factorization $A=C^{\mathsf T}C$, with $C^{\mathsf T}=L\sqrt D$, the square roots of the pivots are on the diagonal of $C$. Find $C$ (upper triangular) for
$$A=\begin{bmatrix}9&0&0\\0&1&2\\0&2&8\end{bmatrix}\qquad\text{and}\qquad A=\begin{bmatrix}1&1&1\\1&2&2\\1&2&7\end{bmatrix}.$$
:::

::: {.problem #prob-mit1806s10-9-q3 origin="external" source="mit1806s10-9-q3"}
The symmetric factorization $A=LDL^{\mathsf T}$ means that $\mathbf{x}^{\mathsf T}A\mathbf{x}=\mathbf{x}^{\mathsf T}LDL^{\mathsf T}\mathbf{x}$:
$$\begin{bmatrix}x&y\end{bmatrix}\begin{bmatrix}a&b\\c&d\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}x&y\end{bmatrix}\begin{bmatrix}1&0\\b/a&1\end{bmatrix}\begin{bmatrix}a&0\\0&(ac-b^2)/a\end{bmatrix}\begin{bmatrix}1&b/a\\0&1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}$$
The left side is $ax^2+2bxy+cy^2$. The right side is $a(x+\frac bay)^2+\underline{\quad}\,y^2$. The second pivot completes the square! Test with $a=2$, $b=4$, $c=10$.

*Note (these notes):* The matrix on the left is meant to be the symmetric $\begin{bmatrix}a&b\\b&c\end{bmatrix}$.
:::

::: {.problem #prob-mit1806s10-9-q4 origin="external" source="mit1806s10-9-q4"}
For $F_1(x,y)=x^4/4+x^2+x^2y+y^2$ and $F_2(x,y)=x^3+xy-x$, find the second-derivative matrices $H_1$ and $H_2$:
$$H=\begin{pmatrix}\frac{\partial^2F}{\partial x^2}&\frac{\partial^2F}{\partial x\partial y}\\\frac{\partial^2F}{\partial y\partial x}&\frac{\partial^2F}{\partial y^2}\end{pmatrix}.$$
$H_1$ is positive-definite so $F_1$ is concave up (= convex). Find the minimum point of $F_1$ and the the saddle point of $F_2$ (look only where the first derivatives are zero).
:::

::: {.problem #prob-mit1806s10-9-q5 origin="external" source="mit1806s10-9-q5"}
A group of nonsingular matrices include $AB$ and $A^{-1}$ if it includes $A$ and $B$. "Products and inverses stay in the group." Which of these are groups (as in 2.7.37)? Invent a "subgroup" of two of these groups (not $I$ by itself = the smallest group).

(a) Positive definite symmetric matrices $A$.

(b) Orthogonal matrices $Q$.

(c) All exponentials $e^{tA}$ of a fixed matrix $A$.

(d) Matrices $P$ with positive eigenvalues.

(e) Matrices $D$ with determinant 1.
:::

::: {.problem #prob-mit1806s10-9-q6 origin="external" source="mit1806s10-9-q6"}
When $A$ and $B$ are symmetric positive definite, $AB$ might not even be symmetric. But its eigenvalues are still positive. Start from $AB\mathbf{x}=\lambda\mathbf{x}$ and take dot products with $B\mathbf{x}$. Then prove $\lambda>0$.
:::

::: {.problem #prob-mit1806s10-9-q8 origin="external" source="mit1806s10-9-q8"}
If $A$ has full column rank, and $C$ is positive-definite, show that $A^{\mathsf T}CA$ is positive definite.
:::

::: {.problem #prob-mit1806s10-9-q9 origin="external" source="mit1806s10-9-q9"}
In the free-free case when $A^{\mathsf T}CA$ in equation (9) is singular, add the three equations $A^{\mathsf T}CA\mathbf{u}=\mathbf{f}$ to show that we need $f_1+f_2+f_3=0$. Find a solution to $A^{\mathsf T}CA\mathbf{u}=\mathbf{f}$ when the forces $\mathbf{f}=(-1,0,1)$ balance themselves. Find *all* solutions!

*Note (these notes):* In the free-free case of the book's equation (9) there are three masses and two springs, and $A^{\mathsf T}CA=\begin{bmatrix}c_2&-c_2&0\\-c_2&c_2+c_3&-c_3\\0&-c_3&c_3\end{bmatrix}$.
:::

::: {.problem #prob-mit1806s10-9-q10 origin="external" source="mit1806s10-9-q10"}
In the fixed-free problem, the matrix $A$ is square and invertible. We can solve $A^{\mathsf T}\mathbf{y}=\mathbf{f}$ separately from $A\mathbf{u}=\mathbf{e}$. Do the same for the differential equation:
$$\text{Solve}\quad-\frac{dy}{dx}=f(x)\quad\text{with }y(1)=0.\qquad\text{Graph }y(x)\text{ if }f(x)=1.$$
:::

::: {.problem #prob-mit1806s10-9-q11 origin="external" source="mit1806s10-9-q11"}
For five springs and four masses with both ends fixed, what are the matrices $A$ and $C$ and $K$? With $C=I$ solve $K\mathbf{u}=\texttt{ones(4)}$.
:::

::: {.problem #prob-mit1806s10-9-q12 origin="external" source="mit1806s10-9-q12"}
(MATLAB) Find the displacements $u(1),\dots,u(100)$ of 100 masses connected by springs all with $c=1$. Each force is $f(i)=0.01$. Print graphs of $u$ with fixed-fixed and fixed-free ends. Note that diag(ones(n, 1), d) is a matrix with $n$ ones along the diagonal $d$. This print command will graph a vector $u$:

plot(u, '+'); xlabel('mass number'); ylabel('movement'); print
:::

::: {.problem #prob-mit1806s10-9-q13 origin="external" source="mit1806s10-9-q13"}
(MATLAB) Chemical engineering has a first derivative of $du/dx$ from fluid velocity as well as $d^2u/dx^2$ from diffusion. Replace $du/dx$ by a forward difference, then a centered difference, then a backward difference, with $\Delta x=\frac18$. Graph your numerical solutions of
$$-\frac{d^2u}{dx^2}+10\frac{du}{dx}=1\quad\text{with }u(0)=u(1)=0.$$
:::

::: {.problem #prob-mit18065ps-5-q3 origin="external" source="mit18065ps-5-q3"}
For which numbers $b$ and $c$ are these matrices positive definite?
$$S=\begin{bmatrix}1&b\\b&9\end{bmatrix}\qquad S=\begin{bmatrix}2&4\\4&c\end{bmatrix}\qquad S=\begin{bmatrix}c&b\\b&c\end{bmatrix}.$$
With the pivots in $D$ and multiplier in $L$, factor each $A$ into $LDL^{\mathsf T}$.
:::

::: {.problem #prob-mit18065ps-5-q14 origin="external" source="mit18065ps-5-q14"}
Find the 3 by 3 matrix $S$ and its pivots, rank, eigenvalues, and determinant:
$$\begin{bmatrix}x_1&x_2&x_3\end{bmatrix}S\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=4(x_1-x_2+2x_3)^2 .$$
:::

::: {.problem #prob-mit18065ps-5-q15 origin="external" source="mit18065ps-5-q15"}
Compute the three upper left determinants of $S$ to establish positive definiteness. Verify that their ratios give the second and third pivots.
$$\text{Pivots = ratios of determinants}\qquad S=\begin{bmatrix}2&2&0\\2&5&3\\0&3&8\end{bmatrix}.$$
:::

::: {.problem #prob-mit18065ps-12-q1 origin="external" source="mit18065ps-12-q1"}
These problems start with a bidiagonal $n$ by $n$ backward difference matrix $D=I-S$. Two tridiagonal second difference matrices are $DD^{\mathsf T}$ and $A=-S+2I-S^{\mathsf T}$. The shift $S$ has one nonzero subdiagonal $S_{i,i-1}=1$ for $i=2,\dots,n$. $A$ has diagonals $-1,2,-1$.

Show that $DD^{\mathsf T}$ equals $A$ except that $1\ne2$ in their $(1,1)$ entries. Similarly $D^{\mathsf T}D=A$ except that $1\ne2$ in their $(n,n)$ entries.
:::

::: {.problem #prob-mit18065ps-13-q4 origin="external" source="mit18065ps-13-q4"}
If $M=\mathbf{1}\mathbf{1}^{\mathsf T}$ is the $n$ by $n$ matrix of 1's, prove that $nI-M$ is positive semidefinite. Problem 3 was the energy test. For Problem 4, find the eigenvalues of $nI-M$.
:::

::: {.problem #prob-mit18065ps-16-q12 origin="external" source="mit18065ps-16-q12"}
If $\mathbf{x}^{\mathsf T}S\mathbf{x}>0$ for all $\mathbf{x}\ne\mathbf{0}$ and $C$ is invertible, why is $(C\mathbf{y})^{\mathsf T}S(C\mathbf{y})$ also positive ? This shows again that if $S$ has all positive eigenvalues, so does $C^{\mathsf T}SC$.
:::
