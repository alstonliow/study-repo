<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-1-q1" status="draft"}
1. In the same way as for $\mathbf{v}$: $\cos\beta=w_1/\lVert\mathbf{w}\rVert$ and $\sin\beta=w_2/\lVert\mathbf{w}\rVert$.

2. Substituting,
   $$\cos\theta=\cos(\beta-\alpha)=\frac{v_1}{\lVert\mathbf{v}\rVert}\frac{w_1}{\lVert\mathbf{w}\rVert}+\frac{w_2}{\lVert\mathbf{w}\rVert}\frac{v_2}{\lVert\mathbf{v}\rVert}=\frac{v_1w_1+v_2w_2}{\lVert\mathbf{v}\rVert\lVert\mathbf{w}\rVert}=\frac{\mathbf{v}\cdot\mathbf{w}}{\lVert\mathbf{v}\rVert\lVert\mathbf{w}\rVert}.$$
:::

::: {.solution for="prob-mit1806s10-1-q2" status="draft"}
Yes. Take three unit vectors $120^\circ$ apart:
$$\mathbf{u}=(1,0),\qquad \mathbf{v}=\big(-\tfrac12,\tfrac{\sqrt3}2\big),\qquad \mathbf{w}=\big(-\tfrac12,-\tfrac{\sqrt3}2\big).$$
Each pair makes an angle of $120^\circ$, so each dot product is $\cos120^\circ=-\frac12<0$. (Four such vectors in the plane are impossible, but three are fine.)
:::
