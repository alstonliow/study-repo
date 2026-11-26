<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-3-q1" status="draft"}
1. $Ax=b$, $x\ge0$ is the system $Ax\le b$, $-Ax\le-b$, $-x\le0$. By @thm-theorem-of-alternatives it has no solution iff there are $p,q,s\ge0$ with $A^{\mathsf T}p-A^{\mathsf T}q-s=0$ and $b^{\mathsf T}p-b^{\mathsf T}q<0$.

2. Given such $p,q,s$, put $y=p-q$: then $A^{\mathsf T}y=s\ge0$ and $b^{\mathsf T}y<0$.

3. Conversely, given $y$ with $A^{\mathsf T}y\ge0$ and $b^{\mathsf T}y<0$, take $p=\max(y,0)$, $q=\max(-y,0)$ (componentwise) and $s=A^{\mathsf T}y$. So the two alternatives of @lem-farkas are exactly those of the theorem.
:::
