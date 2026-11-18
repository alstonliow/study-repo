<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-1-q3" status="draft"}
1. The differences are equal: $\mathbf{w}_2-\mathbf{w}_1=\mathbf{w}_3-\mathbf{w}_2=(3,3,3)$. Hence $\mathbf{w}_1-2\mathbf{w}_2+\mathbf{w}_3=\mathbf{0}$, i.e. $(x_1,x_2,x_3)=(1,-2,1)$.

2. A nontrivial combination gives zero, so the vectors are *dependent*. They lie in a *plane* through the origin (the plane spanned by $\mathbf{w}_1$ and $\mathbf{w}_2$).
:::

::: {.solution for="prob-mit1806s10-1-q4" status="draft"}
1. With $C$ having $1$ above and $-1$ below the diagonal, the equations are
   $$x_2=b_1,\quad -x_1+x_3=b_2,\quad -x_2+x_4=b_3,\quad -x_3+x_5=b_4,\quad -x_4=b_5.$$

2. Equations 1, 3 and 5 involve only $x_2$ and $x_4$: their left sides add to $x_2+(-x_2+x_4)+(-x_4)=0$.

3. So a solution can exist only if $b_1+b_3+b_5=0$. Since some right sides are impossible, $C$ is not invertible.
:::

::: {.solution for="prob-mit1806s10-1-q5" status="draft"}
1. $\mathbf{u}_2=A\mathbf{u}_1=(.8\cdot.8+.3\cdot.2,\ .2\cdot.8+.7\cdot.2)=(.70,.30)$.

2. $\mathbf{u}_3=A\mathbf{u}_2=(.8\cdot.7+.3\cdot.3,\ .2\cdot.7+.7\cdot.3)=(.65,.35)$.

3. In every vector the two components add to $1$. This persists because each column of $A$ adds to $1$: the components of $A\mathbf{u}$ add to $u_1(.8+.2)+u_2(.3+.7)=u_1+u_2$.
:::
