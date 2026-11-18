::: {.problem #prob-mit1802f07-2-q1 origin="external" source="mit1802f07-2-q1"}
Consider the four points $A:(2,4,0)$, $B:(3,1,1)$, $C:(1,1,3)$, $D:(0,5,1)$. Find the distance between the lines $(AB)$ and $(CD)$, i.e. the distance between the closest points on these two lines, by using two different methods:

a) Find a pair of planes which are parallel to both lines, with the first plane containing the line $(AB)$ and the second plane containing the line $(CD)$. Then find the distance between these two planes.

b) Find parametric equations of the lines $(AB)$ and $(CD)$, and find the times at which the line segment connecting a point $P_1$ on $(AB)$ to a point $P_2$ on $(CD)$ is perpendicular to both lines. The length of this segment is then the distance between the lines.

Important: since the positions of the points $P_1$ and $P_2$ can be chosen independently of each other, the parameters on the two lines should be allowed to vary independently of each other (call them $t_1$ and $t_2$ for example).
:::

::: {.problem #prob-mit1802f07-3-q1 origin="external" source="mit1802f07-3-q1"}
In 3D computer graphics, one needs to represent 3-dimensional objects on a plane screen, by drawing a given point $P$ at the place where the line from $P$ to the eye meets the screen. Suppose that the screen is the $yz$-plane, and the eye is at $E:(2,0,0)$.

a) At what point $Q:(y,z)$ in the $yz$-plane should one represent the point $P:(x_0,y_0,z_0)$? (Express $y$ and $z$ in terms of the coordinates of $P$. Assume that $x_0<2$. Why is this assumption legitimate?)

b) What does the image on the screen of a line segment in space look like? (Justify your answer.)

c) A line segment connects $P_0:(-1,-3,1)$ to $P_1:(-2,4,6)$. What is drawn on the screen?

d) A bird leaves from $P_0$ at time $t=0$, and flies in a straight line at constant speed in such a way that it passes through $P_1$ at time $t=1$. What does the trajectory of the bird (for $t\ge0$) look like on the screen? Show that, as $t$ tends to infinity, the trajectory on the screen tends to a limit point (the "vanishing point"), and give its coordinates.

e) In fact, part of the trajectory of the bird is hidden by a vertical fence erected in front of the observer. The fence lies in the plane $x=1$, and its top is at the altitude $z=1$. What portion of the trajectory is hidden?

Hint: observe that the points hidden by the fence are exactly those which lie below a certain plane passing through $E$.
:::

::: {.problem #prob-mit1802n-1e-q1 origin="external" source="mit1802n-1e-q1"}
Find the equations of the following planes:

a) through $(2,0,-1)$ and perpendicular to $\mathbf{i}+2\mathbf{j}-2\mathbf{k}$

b) through the origin, $(1,1,0)$, and $(2,-1,3)$

c) through $(1,0,1)$, $(2,-1,2)$, $(-1,3,2)$

d) through the points on the $x$, $y$ and $z$-axes where $x=a$, $y=b$, $z=c$ respectively (give the equation in the form $Ax+By+Cz=1$ and remember it)

e) through $(1,0,1)$ and $(0,1,1)$ and parallel to $\mathbf{i}-\mathbf{j}+2\mathbf{k}$
:::

::: {.problem #prob-mit1802n-1e-q2 origin="external" source="mit1802n-1e-q2"}
Find the dihedral angle between the planes $2x-y+z=3$ and $x+y+2z=1$.
:::

::: {.problem #prob-mit1802n-1e-q3 origin="external" source="mit1802n-1e-q3"}
Find in parametric form the equations for

a) the line through $(1,0,-1)$ and parallel to $2\mathbf{i}-\mathbf{j}+3\mathbf{k}$

b) the line through $(2,-1,-1)$ and perpendicular to the plane $x-y+2z=3$

c) all lines passing through $(1,1,1)$ and lying in the plane $x+2y-z=2$
:::

::: {.problem #prob-mit1802n-1e-q4 origin="external" source="mit1802n-1e-q4"}
Where does the line through $(0,1,2)$ and $(2,0,3)$ intersect the plane $x+4y+z=4$?
:::

::: {.problem #prob-mit1802n-1e-q5 origin="external" source="mit1802n-1e-q5"}
The line passing through $(1,1,-1)$ and perpendicular to the plane $x+2y-z=3$ intersects the plane $2x-y+z=1$ at what point?
:::

::: {.problem #prob-mit1802n-1e-q6 origin="external" source="mit1802n-1e-q6"}
Show that the distance $D$ from the origin to the plane $ax+by+cz=d$ is given by the formula $D=\dfrac{|d|}{\sqrt{a^2+b^2+c^2}}$.

(Hint: Let $\mathbf{n}$ be the unit normal to the plane. and $P$ be a point on the plane; consider the component of $OP$ in the direction $\mathbf{n}$.)
:::

::: {.problem #prob-mit1802n-1h-q3 origin="external" source="mit1802n-1h-q3"}
a) For what $c$-value(s) will
$$x_1-x_2+x_3=0,\qquad 2x_1+x_2+x_3=0,\qquad -x_1+cx_2+2x_3=0$$
have a non-trivial solution?

b) For what $c$-value(s) will $\begin{pmatrix}2&1\\0&-1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=c\begin{pmatrix}x\\y\end{pmatrix}$ have a non-trivial solution? (Write it as a system of homogeneous equations.)

c) For each value of $c$ in part (a), find a non-trivial solution to the corresponding system. (Interpret the equations as asking for a vector orthogonal to three given vectors; find it by using the cross product.)

*Note (these notes):* Parts (a), (b) and (c) were assigned.
:::

::: {.problem #prob-mit1802n-1h-q7 origin="external" source="mit1802n-1h-q7"}
Suppose we want to find a pure oscillation (sine wave) of frequency 1 passing through two given points. In other words, we want to choose constants $a$ and $b$ so that the function
$$f(x)=a\cos x+b\sin x$$
has prescribed values at two given $x$-values: $f(x_1)=y_1$, $f(x_2)=y_2$.

a) Show this is possible in one and only one way, if we assume that $x_2\ne x_1+n\pi$, for every integer $n$.

b) If $x_2=x_1+n\pi$ for some integer $n$, when can $a$ and $b$ be found?
:::
