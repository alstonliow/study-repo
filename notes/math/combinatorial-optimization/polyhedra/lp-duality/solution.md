<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-3-q2" status="draft"}
1. Write (D) $\min\{b^{\mathsf T}y:A^{\mathsf T}y=c,\ y\ge0\}$ in the primal form of @def-lp-primal-dual: maximise $(-b)^{\mathsf T}y$ subject to $A^{\mathsf T}y\le c$, $-A^{\mathsf T}y\le-c$, $-y\le0$.

2. Its dual has one nonnegative variable per row, $p,q,s\ge0$, and reads: minimise $c^{\mathsf T}p-c^{\mathsf T}q$ subject to $Ap-Aq-s=-b$.

3. Put $x=q-p$, a free vector. The constraint becomes $Ax+s=b$ with $s\ge0$, that is $Ax\le b$, and the objective is $-c^{\mathsf T}x$. So the dual of the dual is "minimise $-c^{\mathsf T}x$ subject to $Ax\le b$", i.e. the primal $\max\{c^{\mathsf T}x:Ax\le b\}$ (the sign comes from having negated (D) in step 1).
:::

::: {.solution for="prob-mit18433-3-q3" status="draft"}
1. The dual $A^{\mathsf T}y=c$, $y\ge0$ has no solution. By Farkas' lemma (@lem-farkas, with $A^{\mathsf T}$ in place of $A$) there is $z$ with $Az\ge0$ and $c^{\mathsf T}z<0$. Put $d=-z$: then $Ad\le0$ and $c^{\mathsf T}d>0$.

2. For a primal feasible $x^*$ and $t\ge0$, $A(x^*+td)\le b$, so $x^*+td$ is feasible, and $c^{\mathsf T}(x^*+td)\to+\infty$. So $z^*=+\infty$, and $w^*=+\infty$ by the convention for an infeasible minimisation.

3. Symmetrically (by exercise 2), if the dual is feasible and the primal infeasible, the dual is unbounded and $z^*=w^*=-\infty$.
:::
