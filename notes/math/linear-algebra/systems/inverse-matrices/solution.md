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
