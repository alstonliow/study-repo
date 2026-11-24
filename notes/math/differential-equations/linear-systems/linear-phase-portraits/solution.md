<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1803ps-34-q2" status="draft"}
**(a)** $T=a-1$ and $\Delta=-a+3$. Eliminating $a=T+1$: the mark moves along the line $\Delta=2-T$.

**(b)**

- $\Delta=0$: $a=3$.
- $\Delta=T^2/4$: $3-a=\tfrac{(a-1)^2}4$, i.e. $a^2+2a-11=0$, so $a=-1\pm2\sqrt3\approx-4.46$ and $2.46$.
- $T=0$: $a=1$.

**(c)** By @thm-trace-determinant-classification; rotation is counterclockwise because the lower-left entry $1$ is positive.

| $a$ | type |
|---|---|
| $a<-1-2\sqrt3$ | stable node |
| $a=-1-2\sqrt3$ | stable defective node (counterclockwise) |
| $-1-2\sqrt3<a<1$ | stable spiral, counterclockwise |
| $a=1$ | center, counterclockwise |
| $1<a<-1+2\sqrt3$ | unstable spiral, counterclockwise |
| $a=-1+2\sqrt3$ | unstable defective node (counterclockwise) |
| $-1+2\sqrt3<a<3$ | unstable node |
| $a=3$ | degenerate: unstable comb (eigenvalues $0$ and $2$; a line of critical points, trajectories leaving it along parallel lines) |
| $a>3$ | saddle |

**(d)** For the nodes, saddle and comb, draw the eigenlines of the eigenvectors $(\lambda+1,1)$ (from the second row: $x=(\lambda+1)y$) and orient them by the sign of $\lambda$; for spirals and the center, draw curves turning counterclockwise, inwards for $a<1$ and outwards for $a>1$.
:::

::: {.solution for="prob-mit1803ps-34-q3" status="draft"}
**(a)** $A=\begin{pmatrix}0&1\\c&-2\end{pmatrix}$ has characteristic polynomial $\lambda^2+2\lambda-c$.

**(b)** $\lambda=-1\pm\sqrt{1+c}$. From the first row, an eigenvector for $\lambda$ is $(1,\lambda)$.

- $c>-1$: two real eigenvalues $\lambda_\pm=-1\pm\sqrt{1+c}$ with eigenvectors $(1,\lambda_\pm)$.
- $c=-1$: $\lambda=-1$ double, eigenvectors the multiples of $(1,-1)$ only.
- $c<-1$: $\lambda=-1\pm i\omega$ with $\omega=\sqrt{-1-c}$, eigenvectors $(1,-1\pm i\omega)$.

**(c)**

- $c>-1$: $\mathbf x=c_1e^{\lambda_+t}(1,\lambda_+)+c_2e^{\lambda_-t}(1,\lambda_-)$.
- $c=-1$: $(A+I)\mathbf w=(1,-1)$ gives $\mathbf w=(1,0)$, so $\mathbf x=c_1e^{-t}(1,-1)+c_2e^{-t}\bigl(t(1,-1)+(1,0)\bigr)$.
- $c<-1$: the real and imaginary parts of $e^{(-1+i\omega)t}(1,-1+i\omega)$ give
$$\mathbf x=e^{-t}\left[c_1\begin{pmatrix}\cos\omega t\\-\cos\omega t-\omega\sin\omega t\end{pmatrix}+c_2\begin{pmatrix}\sin\omega t\\-\sin\omega t+\omega\cos\omega t\end{pmatrix}\right].$$

**(d)** $T=-2$, $\Delta=-c$. So: $c>0$ saddle; $c=0$ degenerate (eigenvalues $0,-2$: a line of critical points along $y=0$, a stable comb); $-1<c<0$ stable node; $c=-1$ stable defective node; $c<-1$ stable spiral, clockwise (the lower-left entry $c$ is negative). For $c=-3$: $\omega=\sqrt2$, so solutions are $e^{-t}$ times combinations of $\cos\sqrt2t$, $\sin\sqrt2t$: they wind clockwise around the origin with angular speed about $\sqrt2$ while shrinking by $e^{-1}$ per unit time, a stable spiral.
:::
