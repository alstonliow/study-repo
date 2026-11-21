::: {.problem #prob-mit1802f07-5-q3 origin="external" source="mit1802f07-5-q3"}
a) Now we seek an exact answer to Problem 2b. Use the method of Lagrange multipliers to write down the system of equations satisfied by the point closest to $(2,-1,1)$ at which $x^2+yz=2$. (Hint: it is easier to minimize the square of the distance).

b) Solve the equations to get a numerical approximation to four decimal places for the location of the point. Compare your answers with the approximation in 2(b). Was each coordinate of the approximate answer in 2(b) within 1/100 of the exact answer?

Suggestion: by considering the sum of the second and third equations, show that either $z=-y$ or $\lambda=2$. Assuming $z=-y$, use the multiplier equations to express $x$, $y$, $z$ in terms of $\lambda$, then substitute these formulas into the constraint equation. After clearing the denominator, you should obtain a degree 4 equation for $\lambda$. Use a calculator to solve it. Alternatively, in Matlab, `roots([a4, a3, a2, a1, a0])` finds the roots of the polynomial $a_4\lambda^4+a_3\lambda^3+a_2\lambda^2+a_1\lambda+a_0=0$. (There should be two real roots). Finally, check that the other case $\lambda=2$ yields solutions $(x,y,z)$ that are further away from $(2,-1,1)$.
:::

::: {.problem #prob-mit1802n-2i-q1 origin="external" source="mit1802n-2i-q1"}
A rectangular box is placed in the first octant so that one corner $Q$ is at the origin and the three sides adjacent to $Q$ lie in the coordinate planes. The corner $P$ diagonally opposite $Q$ lies on the surface $f(x,y,z)=c$. Using Lagrange multipliers, tell for which point $P$ the box will have the largest volume, and tell how you know it gives a maximum point, if the surface is

a) the plane $x+2y+3z=18$  b) the ellipsoid $x^2+2y^2+4z^2=12$.
:::

::: {.problem #prob-mit1802n-2i-q3 origin="external" source="mit1802n-2i-q3"}
(Repeat of 2F-2, but this time use Lagrange multipliers.) A rectangular produce box is to be made of cardboard; the sides of single thickness, the ends of double thickness, and the bottom of triple thickness, with the top left open. Its volume is to be 1 cubic foot; what should be its proportions in order to use the least cardboard?
:::

::: {.problem #prob-mit18065ps-24-q1 origin="external" source="mit18065ps-24-q1"}
Minimize $F(\mathbf{x})=\frac12\mathbf{x}^{\mathsf T}S\mathbf{x}=\frac12x_1^2+2x_2^2$ subject to $A^{\mathsf T}\mathbf{x}=x_1+3x_2=b$.

(a) What is the Lagrangian $L(\mathbf{x},\lambda)$ for this problem ?

(b) What are the three equations "derivative of $L$ = zero" ?

(c) Solve those equations to find $\mathbf{x}^*=(x_1^*,x_2^*)$ and the multiplier $\lambda^*$.

(d) Draw Figure VI.4 for this problem with constraint line tangent to cost circle.

(e) Verify that the derivative of the minimum cost is $\partial F^*/\partial b=-\lambda^*$.

*Note (these notes):* The textbook figure is not reproduced here.
:::
