<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-33-q1" status="draft"}
**(a)** $A=\begin{pmatrix}0&1\\-3&-4\end{pmatrix}$ has eigenvalues $-1$, $-3$ (the characteristic roots) with eigenvectors $(1,-1)$ and $(1,-3)$: the eigenlines are $y=-x$ and $y=-3x$. Solutions along them are $e^{-t}(1,-1)$ and $e^{-3t}(1,-3)$, exactly the trajectories of $x_1=e^{-t}$ and $x_2=e^{-3t}$ found in the previous problem.

**(b)** $\det(A-\lambda I)=\lambda^2+\lambda-2=(\lambda-1)(\lambda+2)$.

- $\lambda=1$: $(A-I)\mathbf v=\mathbf0$ with $A-I=\begin{pmatrix}1&-4\\1&-4\end{pmatrix}$ gives $\mathbf v=(4,1)$.
- $\lambda=-2$: $A+2I=\begin{pmatrix}4&-4\\1&-1\end{pmatrix}$ gives $\mathbf v=(1,1)$.

The solutions on the line through $(4,1)$ are $ce^{t}(4,1)$ (moving out along the two rays, or $c=0$), and those on the line $y=x$ are $ce^{-2t}(1,1)$ (moving in).

**(c)** A saddle ($\det A=-2<0$): trajectories come in along $y=x$, leave along the line through $(4,1)$, and in each of the four wedges between these lines follow hyperbola-like curves, turning from the incoming direction to the outgoing one.
:::

::: {.solution for="prob-mit1803ps-34-q1" status="draft"}
**(a)** $A=\begin{pmatrix}0.5&1\\-2.25&0.5\end{pmatrix}$ has $\det(A-\lambda I)=(\lambda-0.5)^2+2.25$, so $\lambda=0.5\pm1.5i$.

1. For $\lambda=0.5+1.5i$: $A-\lambda I=\begin{pmatrix}-1.5i&1\\-2.25&-1.5i\end{pmatrix}$, and $\mathbf v=(1,1.5i)$.
2. $e^{\lambda t}\mathbf v=e^{t/2}(\cos1.5t+i\sin1.5t)(1,1.5i)$ has real part $e^{t/2}(\cos1.5t,\,-1.5\sin1.5t)$ and imaginary part $e^{t/2}(\sin1.5t,\,1.5\cos1.5t)$ (@thm-complex-eigenvalue-solutions).
3. With $x(0)=1$, $y(0)=0$ only the real part is needed:
$$x=e^{t/2}\cos\tfrac32t,\qquad y=-\tfrac32e^{t/2}\sin\tfrac32t .$$
4. $\dot x(0)=0.5>0$: weasels increasing. $\dot y(0)=-2.25<0$: voles decreasing. The voles are next at baseline when $\sin\frac32t=0$, at $t=2\pi/3\approx2.09$.

The origin is an unstable spiral turning clockwise (the lower-left entry is negative). At $t=k\pi/3$ for $k=-2,\dots,2$ the point $(x,y)$ is approximately $(-0.35,0)$, $(0,0.89)$, $(1,0)$, $(0,-2.53)$, $(-2.85,0)$: a quarter turn clockwise each time, growing by $e^{\pi/6}\approx1.69$.

**(b)** The eigenvalue is $1$ (double) for every $b$, since $A$ is triangular.

- $b=0$: $A=I$, every nonzero vector is an eigenvector, and the normal modes are $e^t\mathbf v$ for every $\mathbf v$. The system is complete; the portrait is an unstable star (rays out of the origin).
- $b\neq0$: $A-I=\begin{pmatrix}0&b\\0&0\end{pmatrix}$, so the eigenvectors are the nonzero multiples of $(1,0)$ and the normal modes are $ce^t(1,0)$. The system is defective. Solving $(A-I)\mathbf w=(1,0)$ gives $\mathbf w=(0,1/b)$, and a complementary solution is $e^t\left(t(1,0)+(0,\tfrac1b)\right)=e^t(t,\tfrac1b)$ (@thm-repeated-eigenvalue-solutions). The portrait is an unstable defective node: trajectories leave the origin tangent to the $x$-axis and bend round, clockwise for $b>0$ and counterclockwise for $b<0$.
:::
