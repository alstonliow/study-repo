<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-32-q1" status="draft"}
**(a)** First equation: $s^2+4s+3=(s+1)(s+3)$, so $x_1=e^{-t}$, $x_2=e^{-3t}$, $x=c_1e^{-t}+c_2e^{-3t}$; overdamped. $\dot x_1=-e^{-t}$, $\dot x_2=-3e^{-3t}$.

Second equation: $s^2+s+\tfrac52=0$ gives $s=-\tfrac12\pm\tfrac32i$, so $x_1=e^{-t/2}\cos\tfrac32t$, $x_2=e^{-t/2}\sin\tfrac32t$; underdamped. $\dot x_1=-e^{-t/2}\left(\tfrac12\cos\tfrac32t+\tfrac32\sin\tfrac32t\right)$, $\dot x_2=e^{-t/2}\left(\tfrac32\cos\tfrac32t-\tfrac12\sin\tfrac32t\right)$.

**(b)** $\begin{pmatrix}0&1\\-3&-4\end{pmatrix}$ and $\begin{pmatrix}0&1\\-\frac52&-1\end{pmatrix}$ (@prp-companion-matrix).

**(c)** The solution $x_1=e^{-t}$ gives $(e^{-t},-e^{-t})$, which moves into the origin along the line $y=-x$; $x_2=e^{-3t}$ gives $(e^{-3t},-3e^{-3t})$, along $y=-3x$. Their negatives run along the other halves of these lines. All other trajectories also approach the origin, eventually tangent to the slow line $y=-x$ (a stable node).

**(d)** $x(0)=1$, $\dot x(0)=0$: $c_1+c_2=1$, $-c_1-3c_2=0$, so $x=\tfrac32e^{-t}-\tfrac12e^{-3t}$, with $y=\dot x=-\tfrac32e^{-t}+\tfrac32e^{-3t}$. The graph of $x$ decreases from $1$ towards $0$, with zero slope at $t=0$ and never crossing $0$.

**(e)** Every time-shift traces the same curve (@prp-autonomous-trajectories): $x=\tfrac32e^{-(t-a)}-\tfrac12e^{-3(t-a)}$.

**(f)** The portrait is a stable spiral, turning clockwise (the lower-left entry is negative). With $x(0)=0$, $\dot x(0)=1$: $x=\tfrac23e^{-t/2}\sin\tfrac32t$ and $y=\dot x=e^{-t/2}\left(\cos\tfrac32t-\tfrac13\sin\tfrac32t\right)$. It crosses the $y$-axis when $x=0$, i.e. at $t=\tfrac{2\pi k}3$ for integers $k$. Both graphs are decaying oscillations with pseudo-period $\tfrac{4\pi}3$.

**(g)** On the $x$-axis $y=0$; the velocity of a companion system is $(\dot x,\dot y)=(y,\,cx+dy)=(0,\,cx)$, which is vertical.
:::
