<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-6-q1" status="draft"}
1. With $A=\begin{bmatrix}1&0\\1&1\\1&3\\1&4\end{bmatrix}$, $\mathbf{x}=(C,D)$ and $\mathbf{b}=(0,8,8,20)$:
   $$E=C^2+(C+D-8)^2+(C+3D-8)^2+(C+4D-20)^2.$$

2. Differentiating,
   $$\frac{\partial E}{\partial C}=2\big[C+(C+D-8)+(C+3D-8)+(C+4D-20)\big]=8C+16D-72,$$
   $$\frac{\partial E}{\partial D}=2\big[(C+D-8)+3(C+3D-8)+4(C+4D-20)\big]=16C+52D-224.$$

3. Setting both to zero and dividing by $2$: $4C+8D=36$ and $8C+26D=112$. These are $A^{\mathsf T}A\hat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}$ with $A^{\mathsf T}A=\begin{bmatrix}4&8\\8&26\end{bmatrix}$ and $A^{\mathsf T}\mathbf{b}=(36,112)$. The solution is $C=1$, $D=4$.
:::

::: {.solution for="prob-mit1806s10-6-q2" status="draft"}
1. $A=(0,1,3,4)^{\mathsf T}$ (one column), $\mathbf{b}=(0,8,8,20)$. Then $A^{\mathsf T}A=26$ and $A^{\mathsf T}\mathbf{b}=0+8+24+80=112$, so
   $$\hat D=\frac{112}{26}=\frac{56}{13}\approx4.31.$$

2. The picture: the line $b=\frac{56}{13}t$ through the origin, and at each $t_i$ a vertical segment from the line to the data point, of signed length $e_i=b_i-\hat Dt_i$:
   $$\mathbf{e}=\big(0,\ \tfrac{48}{13},\ -\tfrac{64}{13},\ \tfrac{36}{13}\big).$$
   Check: $\mathbf{e}$ is orthogonal to the column $(0,1,3,4)$: $\frac{48-192+144}{13}=0$.
:::

::: {.solution for="prob-mit1806s10-6-q3" status="draft"}
1. The equations $C+Dt_i+Et_i^2=b_i$ are
   $$C=0,\quad C+D+E=8,\quad C+3D+9E=8,\quad C+4D+16E=20,\qquad A=\begin{bmatrix}1&0&0\\1&1&1\\1&3&9\\1&4&16\end{bmatrix}.$$
   They are unsolvable: the first three give $C=0$, $D=8$, $E=0$, and then the fourth would say $32=20$.

2. The normal equations:
   $$\begin{bmatrix}4&8&26\\8&26&92\\26&92&338\end{bmatrix}\begin{bmatrix}C\\D\\E\end{bmatrix}=\begin{bmatrix}36\\112\\400\end{bmatrix}$$
   (their solution is $C=2$, $D=\frac43$, $E=\frac23$).

3. In the picture of $\mathbb{R}^4$: $\mathbf{b}=(0,8,8,20)$ is projected onto the three-dimensional column space spanned by $(1,1,1,1)$, $(0,1,3,4)$, $(0,1,9,16)$; $\mathbf{p}=A\hat{\mathbf{x}}$ and the error $\mathbf{e}=\mathbf{b}-\mathbf{p}$ is perpendicular to all three columns.
:::

::: {.solution for="prob-mit1806s10-6-q4" status="draft"}
1. One row $(1,x_i,y_i)$ per corner:
   $$A=\begin{bmatrix}1&1&0\\1&0&1\\1&-1&0\\1&0&-1\end{bmatrix}.$$

2. The columns are orthogonal, so $A^{\mathsf T}A=\operatorname{diag}(4,2,2)$, and $A^{\mathsf T}\mathbf{b}=(8,\ 0-3,\ 1-4)=(8,-3,-3)$. Hence $C=2$, $D=-\frac32$, $E=-\frac32$: the plane $b=2-\frac32x-\frac32y$.

3. At $(0,0)$ the plane gives $C$. The first normal equation reads $4C=b_1+b_2+b_3+b_4$, because the column of $1$s is orthogonal to the other two columns. So $C=\frac{0+1+3+4}4=2$ is the average of the $b$'s.
:::

::: {.solution for="prob-mit18065ps-10-q12" status="draft"}
1. The line $C+Dt$ gives $A=\begin{bmatrix}1&0\\1&1\\1&3\\1&4\end{bmatrix}$, $A^{\mathsf T}A=\begin{bmatrix}4&8\\8&26\end{bmatrix}$, $A^{\mathsf T}\mathbf{b}=\begin{bmatrix}36\\112\end{bmatrix}$.

2. $4C+8D=36$ and $8C+26D=112$: the first gives $C=9-2D$, then $72+10D=112$, so $D=4$, $C=1$. Best line $1+4t$.

3. Heights $\mathbf{p}=(1,5,13,17)$, errors $\mathbf{e}=\mathbf{b}-\mathbf{p}=(-1,3,-5,3)$, and $E=1+9+25+9=44$. Check: $\mathbf{e}$ is orthogonal to both columns of $A$ ($-1+3-5+3=0$ and $0+3-15+12=0$).
:::
