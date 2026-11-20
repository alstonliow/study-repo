<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-1-q13" status="draft"}
(a) Component $i$ of $A\mathbf{x}$ is (row $i$)$\cdot\mathbf{x}$. Since row 3 = row 1 + row 2, every $A\mathbf{x}$ has third component equal to the sum of the first two. For $(1,0,0)$ that would say $0=1+0$, which is false. A matrix with an unreachable right side is not invertible.

(b) By the same reason, only right sides with $b_1+b_2=b_3$ can have a solution.

(c) Subtracting row 1 and then row 2 (after it has been updated) from row 3 leaves a zero row, so there are at most two pivots.
:::

::: {.solution for="prob-mit1806s10-2-q1" status="draft"}
1. $U$ is already upper triangular with pivots $1$, so only the upward steps are needed. Subtract $c$ times row 3 from row 2 and $b$ times row 3 from row 1:
   $$\left[\begin{array}{ccc|ccc}1&a&0&1&0&-b\\0&1&0&0&1&-c\\0&0&1&0&0&1\end{array}\right].$$

2. Subtract $a$ times row 2 from row 1:
   $$\left[\begin{array}{ccc|ccc}1&0&0&1&-a&ac-b\\0&1&0&0&1&-c\\0&0&1&0&0&1\end{array}\right],\qquad U^{-1}=\begin{bmatrix}1&-a&ac-b\\0&1&-c\\0&0&1\end{bmatrix}.$$

3. Check one entry: row 1 of $U$ times column 3 of $U^{-1}$ is $(ac-b)-ac+b=0$.
:::

::: {.solution for="prob-mit1806s10-2-q2" status="draft"}
1. Write $A=I-N$, where $N$ has $a,b,c$ just above the diagonal and zeros elsewhere. Each power of $N$ moves the nonzero diagonal one step further up: $N^2$ has $ab,bc$ two steps above, $N^3$ has $abc$ in the corner, and $N^4=0$.

2. Then $(I-N)(I+N+N^2+N^3)=I-N^4=I$, so
   $$A^{-1}=I+N+N^2+N^3=\begin{bmatrix}1&a&ab&abc\\0&1&b&bc\\0&0&1&c\\0&0&0&1\end{bmatrix}.$$

3. Gauss–Jordan gives the same result: add $c$ times row 4 to row 3, $b$ times row 3 to row 2, $a$ times row 2 to row 1, working upwards.
:::

::: {.solution for="prob-mit1806s10-2-q6" status="draft"}
1. The pattern says entry $(i,j)$ is $i(7-j)$ for $i\le j$ and $j(7-i)$ for $i\ge j$, i.e. $\min(i,j)\,(7-\max(i,j))$:
   $$7K^{-1}=\begin{bmatrix}6&5&4&3&2&1\\5&10&8&6&4&2\\4&8&12&9&6&3\\3&6&9&12&8&4\\2&4&6&8&10&5\\1&2&3&4&5&6\end{bmatrix}.$$

2. Check $K$ times this matrix. Row $i$ of $K$ forms $-m_{i-1,j}+2m_{ij}-m_{i+1,j}$ (a second difference down column $j$). Along column $j$ the entries $m_{ij}$ are linear in $i$ on each side of the diagonal ($i(7-j)$ above, $j(7-i)$ below, and $0$ beyond the ends at $i=0$ and $i=7$), so the second difference is $0$ except at $i=j$.

3. At $i=j$: $-(j-1)(7-j)+2j(7-j)-j(7-j-1)=(7-j)(-j+1+2j)-j(6-j)=(7-j)(j+1)-j(6-j)=7$. Hence $K\cdot(7K^{-1})=7I$.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-1-q5" status="draft"}
a) The four entries of $M\mathbf{X}$ are the total grams of flour, sugar, egg and butter needed for the assortment: entry $i$ is $\sum_jm_{ij}x_j$.

b) $\mathbf{Y}=N(M\mathbf{X})=(NM)\mathbf{X}$ gives the grams of protein, carbohydrates and fat.

c) $NM=\begin{pmatrix}2.85&5.82&5.65\\34.77&40.54&41.05\\8.92&10.00&19.04\end{pmatrix}$ is invertible, so $\mathbf{X}=A\mathbf{Y}$ with
$$A=(NM)^{-1}\approx\begin{pmatrix}-0.4690&0.0705&-0.0128\\0.3839&-0.0050&-0.1031\\0.0181&-0.0304&0.1127\end{pmatrix}.$$

d) $\mathbf{X}=A\begin{pmatrix}50\\300\\65\end{pmatrix}\approx\begin{pmatrix}-3.14\\10.99\\-0.89\end{pmatrix}$. The answer asks for a negative number of cookies and of croissants, which is impossible: these three pastries cannot provide exactly the recommended amounts. (Their protein content is too low relative to carbohydrates and fat; the exact solution compensates with negative amounts.)
:::

::: {.solution for="prob-mit1802n-1g-q3" status="draft"}
$\det A=5$, and by cofactors (@thm-adjugate)
$$A^{-1}=\frac15\begin{pmatrix}3&1&-2\\-1&3&-1\\1&2&1\end{pmatrix},\qquad\mathbf{x}=A^{-1}\mathbf{b}=\frac15\begin{pmatrix}0\\-5\\5\end{pmatrix}=\begin{pmatrix}0\\-1\\1\end{pmatrix}.$$
:::

::: {.solution for="prob-mit1802n-1g-q4" status="draft"}
The matrix is the $A$ of Exercise 3, so $\mathbf{x}=A^{-1}\mathbf{y}$:
$$x_1=\tfrac15(3y_1+y_2-2y_3),\qquad x_2=\tfrac15(-y_1+3y_2-y_3),\qquad x_3=\tfrac15(y_1+2y_2+y_3).$$
:::

::: {.solution for="prob-mit1802n-1g-q5" status="draft"}
$(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AA^{-1}=I$ and $(B^{-1}A^{-1})(AB)=B^{-1}(A^{-1}A)B=B^{-1}B=I$. So $B^{-1}A^{-1}$ is the inverse of $AB$.
:::
