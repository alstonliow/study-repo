::: {.problem #prob-mit1806s10-6-q1 origin="external" source="mit1806s10-6-q1"}
Write down $E=\lVert A\mathbf{x}-\mathbf{b}\rVert^2$ as a sum of four squares–the last one is $(C+4D-20)^2$. Find the derivative equations $\partial E/\partial C=0$ and $\partial E/\partial D=0$. Divide by 2 to obtain the normal equations $A^{\mathsf T}A\hat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}$.

*Note (these notes):* The four points of the book's example are $(t,b)=(0,0),(1,8),(3,8),(4,20)$. The line is $b=C+Dt$.
:::

::: {.problem #prob-mit1806s10-6-q2 origin="external" source="mit1806s10-6-q2"}
Find the closest line $b=Dt$, through the origin, to the same four points. An exact fit would solve $D\cdot0=0$, $D\cdot1=8$, $D\cdot3=8$, $D\cdot4=20$. Find the 4 by 1 matrix $A$ and solve $A^{\mathsf T}A\hat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}$. Redraw figure 4.9a showing the best line $b=Dt$ and the $e$'s.

*Note (these notes):* The four points of the book's example are $(t,b)=(0,0),(1,8),(3,8),(4,20)$.
:::

::: {.problem #prob-mit1806s10-6-q3 origin="external" source="mit1806s10-6-q3"}
Form the closest parabola $b=C+Dt+Et^2$ to the same four points, and write down the unsolvable equations $A\mathbf{x}=\mathbf{b}$ in three unknowns $\mathbf{x}=(C,D,E)$. Set up the three normal equations $A^{\mathsf T}A\hat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}$ (solution not required). In figure 4.9a you are now fitting a parabola to 4 points–what is happening in Figure 4.9b?

*Note (these notes):* The four points of the book's example are $(t,b)=(0,0),(1,8),(3,8),(4,20)$. Figure 4.9b shows $\mathbf{b}$, its projection $\mathbf{p}$ onto the column space and the error $\mathbf{e}$.
:::

::: {.problem #prob-mit1806s10-6-q4 origin="external" source="mit1806s10-6-q4"}
Find the plane that gives the best fit to the 4 values $\mathbf{b}=(0,1,3,4)$ at the corners $(1,0)$ and $(0,1)$ and $(-1,0)$ and $(0,-1)$ of a square. The equations $C+Dx+Ey=b$ at those 4 points are $A\mathbf{x}=\mathbf{b}$ with 3 unknowns $\mathbf{x}=(C,D,E)$. What is $A$? At the center $(0,0)$ of the square, show that $C+Dx+Ey$ is the average of the $b$'s.
:::

::: {.problem #prob-mit18065ps-10-q12 origin="external" source="mit18065ps-10-q12"}
Problems 12 and 17 use four data points $\mathbf{b}=(0,8,8,20)$ to bring out the key ideas.


With $\mathbf{b}=0,8,8,20$ at $t=0,1,3,4$, set up and solve the normal equations $A^{\mathsf T}A\widehat{\mathbf{x}}=A^{\mathsf T}\mathbf{b}$. For the best straight line in Figure II.3a, find its four heights $p_i$ and four errors $e_i$. What is the minimum squared error $E=e_1^2+e_2^2+e_3^2+e_4^2$?

*Note (these notes):* The textbook figure is not reproduced here.
:::
