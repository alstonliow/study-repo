::: {.problem #prob-mit1802f07-11-q2 origin="external" source="mit1802f07-11-q2"}
Consider a tetrahedron with vertices at $P_0=(0,0,0)$, $P_1=(1,0,1)$, $P_2=(1,0,-1)$, and $P_3=(1,1,0)$.

a) Which two faces are exchanged by the symmetry $z\to-z$?

b) Find normals to each face (use the easiest ones, not unit normals), pointing outwards. (You can avoid one calculation using symmetry.)

c) Calculate the flux of $\vec F=y\,\hat{\imath}$ through each face. (Because $\vec F$ is symmetric with respect to $z\to-z$, you can again avoid one calculation using symmetry.)

d) Verify the divergence theorem for the tetrahedron and the vector field $\vec F$ by computing each side of the formula.
:::

::: {.problem #prob-mit1802f07-11-q3 origin="external" source="mit1802f07-11-q3"}
a) Let $f(x,y,z)=1/\rho=(x^2+y^2+z^2)^{-1/2}$. Calculate $\vec F=\nabla f$, and describe geometrically the vector field $\vec F$.

b) Evaluate the flux of $\vec F$ over the sphere of radius $a$ centered at the origin.

c) Show that $\operatorname{div}\vec F=0$. Does the answer obtained in (b) contradict the divergence theorem? Explain.
:::

::: {.problem #prob-mit1802f07-11-q4 origin="external" source="mit1802f07-11-q4"}
The Laplacian of a function $f$ is the quantity $\nabla^2f=f_{xx}+f_{yy}+f_{zz}$; a function $f$ is harmonic if it satisfies the Laplace equation $\nabla^2f=0$.

a) Show that, if $S$ is a closed surface bounding a region $D$, and if $f$ has continuous second derivatives inside $D$, then $\displaystyle\iint_S\nabla f\cdot\hat n\,dS=\iiint_D\nabla^2f\,dV$. (In particular, the flux of the gradient of a harmonic function through a closed surface is always zero).

b) Show that, if $S$ is a closed surface bounding a region $D$, and if $f$ has continuous second derivatives inside $D$, then $\displaystyle\iint_Sf\,\nabla f\cdot\hat n\,dS=\iiint_D(f\,\nabla^2f+|\nabla f|^2)\,dV$.

c) Use the result of (b) to show that, if a function $f$ is harmonic everywhere in $D$, and $f$ is zero at every point of the boundary $S$, then $f$ is zero everywhere in $D$. (first show that $\nabla f=0$).

d) Deduce that if two functions $f$ and $g$ are harmonic everywhere in $D$, and $f=g$ on the boundary $S$, then $f=g$ everywhere in $D$.
:::

::: {.problem #prob-mit1802n-6c-q1 origin="external" source="mit1802n-6c-q1"}
Calculate $\operatorname{div}\mathbf{F}$ for each of the following fields

a) $x^2y\mathbf{i}+xy\mathbf{j}+xz\mathbf{k}$

*Note (these notes):* Only part (a) was assigned.
:::

::: {.problem #prob-mit1802n-6c-q2 origin="external" source="mit1802n-6c-q2"}
Calculate $\operatorname{div}\mathbf{F}$ if $\mathbf{F}=\rho^n(x\mathbf{i}+y\mathbf{j}+z\mathbf{k})$, and tell for what value(s) of $n$ we have $\operatorname{div}\mathbf{F}=0$. (Use $\rho_x=x/\rho$, etc.)
:::

::: {.problem #prob-mit1802n-6c-q3 origin="external" source="mit1802n-6c-q3"}
Verify the divergence theorem when $\mathbf{F}=x\mathbf{i}+y\mathbf{j}+z\mathbf{k}$ and $S$ is the surface composed of the upper half of the sphere of radius $a$ and center at the origin, together with the circular disc in the $xy$-plane centered at the origin and of radius $a$.
:::

::: {.problem #prob-mit1802n-6c-q5 origin="external" source="mit1802n-6c-q5"}
By using the divergence theorem, evaluate the surface integral giving the flux of $\mathbf{F}=x\mathbf{i}+z^2\mathbf{j}+y^2\mathbf{k}$ over the tetrahedron with vertices at the origin and the three points on the positive coordinate axes at distance 1 from the origin.
:::

::: {.problem #prob-mit1802n-6c-q6 origin="external" source="mit1802n-6c-q6"}
Evaluate $\iint_S\mathbf{F}\cdot d\mathbf{S}$ over the closed surface $S$ formed below by a piece of the cone $z^2=x^2+y^2$ and above by a circular disc in the plane $z=1$; take $\mathbf{F}$ to be the field of Exercise 6B-5; use the divergence theorem.

*Note (these notes):* The field of Exercise 6B-5 is $\mathbf{F}=z\,\mathbf{k}$.
:::

::: {.problem #prob-mit1802n-6c-q7 origin="external" source="mit1802n-6c-q7"}
Verify the divergence theorem when $S$ is the closed surface having for its sides a portion of the cylinder $x^2+y^2=1$ and for its top and bottom circular portions of the planes $z=1$ and $z=0$; take $\mathbf{F}$ to be

a) $x^2\mathbf{i}+xy\mathbf{j}$

*Note (these notes):* Only part (a) was assigned.
:::

::: {.problem #prob-mit1802n-6c-q8 origin="external" source="mit1802n-6c-q8"}
Suppose $\operatorname{div}\mathbf{F}=0$ and $S_1$ and $S_2$ are the upper and lower hemispheres of the unit sphere centered at the origin. Direct both hemispheres so that the unit normal is "up", i.e., has positive $\mathbf{k}$-component.

a) Show that $\displaystyle\iint_{S_1}\mathbf{F}\cdot d\mathbf{S}=\iint_{S_2}\mathbf{F}\cdot d\mathbf{S}$, and interpret this physically in terms of flux.

b) State a generalization to an arbitrary closed surface $S$ and a field $\mathbf{F}$ such that $\operatorname{div}\mathbf{F}=0$.
:::
