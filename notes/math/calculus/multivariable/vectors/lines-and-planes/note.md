---
title: "Lines, Planes and Square Systems"
sources: [mit1802-3, mit1802-4, mit1802-5, mit1802n-M]
requires: [math/calculus/multivariable/vectors/cross-product]
status: draft
---

<!-- Added 2026-11-18 from MIT 18.02 (Fall 2007), Lectures 3-5 and Supplementary Notes M.4, in our own wording. Numbers checked in Python. -->

::: {#prp-plane-equation .proposition name="Equation of a plane"}

The plane through $P_0=(x_0,y_0,z_0)$ with normal vector $\mathbf{N}=\langle a,b,c\rangle\ne\mathbf{0}$ is
$$a(x-x_0)+b(y-y_0)+c(z-z_0)=0,\qquad\text{i.e.}\qquad ax+by+cz=d .$$
Conversely every equation $ax+by+cz=d$ with $(a,b,c)\ne(0,0,0)$ is a plane with normal $\langle a,b,c\rangle$.

:::

::: {.proof}

1. $P=(x,y,z)$ lies in the plane exactly when $\overrightarrow{P_0P}$ is perpendicular to $\mathbf{N}$, i.e. $\mathbf{N}\cdot\overrightarrow{P_0P}=0$; written in components this is the first equation.

2. Conversely, if say $a\ne0$, the point $P_0=(d/a,0,0)$ satisfies the equation, and $ax+by+cz=d$ can be rewritten as $\mathbf{N}\cdot\overrightarrow{P_0P}=0$.

:::

So the coefficients of the equation are the components of a normal vector, and finding a plane means finding a normal, e.g. as a cross product of two vectors lying in the plane. Multiplying the equation by a non-zero constant gives the same plane; planes with proportional normals are parallel.

::: {#exm-vector-and-plane .example name="A vector parallel to a plane"}

Is $\mathbf{v}=\langle1,2,-1\rangle$ parallel or perpendicular to the plane $x+y+3z=5$? A perpendicular vector would be a multiple of $\mathbf{N}=\langle1,1,3\rangle$, which $\mathbf{v}$ is not. And $\mathbf{v}\cdot\mathbf{N}=1+2-3=0$, so $\mathbf{v}$ is perpendicular to the normal: it is parallel to the plane.

:::

::: {#def-parametric-line .definition name="Parametric equations of a line"}

The line through $Q_0$ in the direction $\mathbf{v}\ne\mathbf{0}$ is the path of the moving point
$$Q(t)=Q_0+t\,\mathbf{v},\qquad t\in\mathbb{R},$$
i.e. $x=x_0+v_1t$, $y=y_0+v_2t$, $z=z_0+v_3t$. Through two points $Q_0,Q_1$ take $\mathbf{v}=\overrightarrow{Q_0Q_1}$; then $Q(0)=Q_0$ and $Q(1)=Q_1$.

:::

A line is also the intersection of two non-parallel planes; a direction vector of that line is $\mathbf{N}_1\times\mathbf{N}_2$, since it is perpendicular to both normals.

::: {#exm-line-meets-plane .example name="Where a line meets a plane"}

The line through $Q_0=(-1,2,2)$ and $Q_1=(1,3,-1)$ is $Q(t)=(-1+2t,\ 2+t,\ 2-3t)$. Substituting into $x+2y+4z$ gives $11-8t$.

- At $Q_0$ the value is $11>7$, at $Q_1$ it is $3<7$: the two points are on opposite sides of the plane $x+2y+4z=7$.
- The line meets the plane when $11-8t=7$, i.e. $t=\tfrac12$, at $Q(\tfrac12)=(0,\tfrac52,\tfrac12)$.

If the substitution had given a constant, the line would be parallel to the plane: contained in it when the constant equals the right side, disjoint from it otherwise.

:::

::: {#thm-square-system-geometry .theorem name="Three equations in three unknowns"}

Let $A$ be a $3\times3$ matrix whose rows $\mathbf{N}_1,\mathbf{N}_2,\mathbf{N}_3$ are the normals of the three planes of the system $A\mathbf{x}=\mathbf{b}$.

1. If $\det A\ne0$, the planes meet in exactly one point, $\mathbf{x}=A^{-1}\mathbf{b}$.
2. If $\det A=0$, the normals are coplanar and the system has either no solution or infinitely many.
3. The homogeneous system $A\mathbf{x}=\mathbf{0}$ has only the solution $\mathbf{x}=\mathbf{0}$ if $\det A\ne0$, and infinitely many solutions (a line or a plane through $\mathbf{0}$) if $\det A=0$.

:::

::: {.proof}

1. If $\det A\ne0$ then $A$ is invertible (@thm-inverse-by-cofactors); multiplying $A\mathbf{x}=\mathbf{b}$ by $A^{-1}$ shows that $A^{-1}\mathbf{b}$ is the only possible solution, and it is one.

2. If $\det A=0$ the parallelepiped with edges $\mathbf{N}_1,\mathbf{N}_2,\mathbf{N}_3$ has volume $0$ (@thm-triple-product), so the normals lie in one plane through the origin. A non-zero vector $\mathbf{w}$ perpendicular to that plane (for instance $\mathbf{N}_1\times\mathbf{N}_2$ if it is not $\mathbf{0}$) is parallel to all three planes of the system.

3. Then for any solution $\mathbf{x}$, every point $\mathbf{x}+t\mathbf{w}$ is also a solution, because $A\mathbf{w}=\mathbf{0}$. So there are no solutions or infinitely many.

4. For $\mathbf{b}=\mathbf{0}$ the point $\mathbf{x}=\mathbf{0}$ is always a solution, so case 2 gives infinitely many solutions and case 1 only $\mathbf{0}$.

:::

::: {#rmk-lines-and-planes-1 .remark name="Seeing the cases"}

Two of the planes usually meet in a line, and the third plane cuts that line in one point. The exceptions are when the third plane is parallel to the line: it then either contains the line (a line of solutions) or misses it (no solution). Which of the two happens is decided by elimination, not by the determinant.

:::
