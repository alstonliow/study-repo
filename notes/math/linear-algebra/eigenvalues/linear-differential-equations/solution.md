<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-8-q1" status="draft"}
(a) $2u_1(cu_2-bu_3)+2u_2(au_3-cu_1)+2u_3(bu_1-au_2)=2(cu_1u_2-cu_1u_2)+2(au_2u_3-au_2u_3)+2(bu_1u_3-bu_1u_3)=0$. So $\lVert\mathbf{u}(t)\rVert^2$ is constant.

(b)

1. Transpose the series term by term, using $(A^n)^{\mathsf T}=(A^{\mathsf T})^n=(-A)^n$:
   $$Q^{\mathsf T}=\sum_{n\ge0}\frac{t^n(A^n)^{\mathsf T}}{n!}=\sum_{n\ge0}\frac{t^n(-A)^n}{n!}=e^{-At}.$$

2. $A$ and $-A$ commute, so $e^{-At}e^{At}=e^{0}=I$ (for commuting matrices the exponential law holds, by multiplying the series). Hence $Q^{\mathsf T}Q=I$.
:::

::: {.solution for="prob-mit1806s10-8-q2" status="draft"}
1. $A$ is triangular with eigenvalues $1$ and $0$. Eigenvectors: $(1,0)$ for $\lambda=1$, and $(3,-1)$ for $\lambda=0$ (since $x_1+3x_2=0$). So
   $$\Lambda=\begin{bmatrix}1&0\\0&0\end{bmatrix},\qquad S=\begin{bmatrix}1&3\\0&-1\end{bmatrix},\qquad S^{-1}=\begin{bmatrix}1&3\\0&-1\end{bmatrix}.$$

2. $e^{At}=S\begin{bmatrix}e^t&0\\0&1\end{bmatrix}S^{-1}=\begin{bmatrix}e^t&3e^t-3\\0&1\end{bmatrix}$.

3. At $t=0$ this is $I$. Its derivative $\begin{bmatrix}e^t&3e^t\\0&0\end{bmatrix}$ equals $A$ at $t=0$, as $\frac{d}{dt}e^{At}=Ae^{At}$ requires.
:::

::: {.solution for="prob-mit1806s10-8-q3" status="draft"}
1. $\begin{bmatrix}1&0\\\Delta t&1\end{bmatrix}^{-1}=\begin{bmatrix}1&0\\-\Delta t&1\end{bmatrix}$, so
   $$A=\begin{bmatrix}1&0\\-\Delta t&1\end{bmatrix}\begin{bmatrix}1&\Delta t\\0&1\end{bmatrix}=\begin{bmatrix}1&\Delta t\\-\Delta t&1-(\Delta t)^2\end{bmatrix}.$$
   Both factors are triangular with $1$s on the diagonal, so $\det A=1\cdot1=1$.

2. For $\Delta t=1$: $\det(A-\lambda I)=\lambda^2-\lambda+1$, so $\lambda=\frac{1\pm i\sqrt3}2=e^{\pm i\pi/3}$, and $\lvert\lambda\rvert=1$.

3. $\lambda^6=e^{\pm2\pi i}=1$ for both eigenvalues. They are distinct, so $A=S\Lambda S^{-1}$ and $A^6=S\Lambda^6S^{-1}=SIS^{-1}=I$. (Directly: $\lambda^2=\lambda-1$ gives $\lambda^3=-1$, and the same identity holds for $A$ by Cayley–Hamilton: $A^3=-I$.)
:::

::: {.solution for="prob-mit1806s10-8-q4" status="draft"}
1. $\Delta t=\sqrt2$: trace $0$, determinant $1$, so $\lambda^2+1=0$ and $\lambda=\pm i$. Then $A^2=-I$ (Cayley–Hamilton, or multiply out), so $A^4=I$. Eigenvectors: for $\lambda=i$, $(1-i)x_1+\sqrt2x_2=0$ gives $(\sqrt2,\,-1+i)$; for $\lambda=-i$, the conjugate $(\sqrt2,\,-1-i)$.

2. $\Delta t=2$: trace $-2$, determinant $1$, so $(\lambda+1)^2=0$ and $\lambda=-1$ twice. $A+I=\begin{bmatrix}2&2\\-2&-2\end{bmatrix}$ has rank $1$, so there is only one independent eigenvector, $(1,-1)$, and $A$ is not diagonalizable. Multiplying out,
   $$A^2=\begin{bmatrix}-3&-4\\4&5\end{bmatrix},\qquad A^4=\begin{bmatrix}-7&-8\\8&9\end{bmatrix}.$$
   The powers grow linearly in $n$ (like $n(-1)^n$), the border case between bounded and exploding.
:::

::: {.solution for="prob-mit1806s10-8-q5" status="draft"}
(a)

1. With $h=\Delta t/2$, the left matrix is $I-B$ and the right one is $I+B$ for $B=\begin{bmatrix}0&h\\-h&0\end{bmatrix}$, which is skew-symmetric. $(I-B)^{-1}=\frac1{1+h^2}\begin{bmatrix}1&h\\-h&1\end{bmatrix}$, and
   $$A=(I-B)^{-1}(I+B)=\frac1{1+h^2}\begin{bmatrix}1-h^2&2h\\-2h&1-h^2\end{bmatrix}.$$
   The columns have length $\frac{\sqrt{(1-h^2)^2+4h^2}}{1+h^2}=1$ and are orthogonal, so $A^{\mathsf T}A=I$.

2. In general, if $B^{\mathsf T}=-B$ then $I-B$ is invertible ($(I-B)\mathbf{x}=\mathbf{0}$ gives $\mathbf{x}^{\mathsf T}\mathbf{x}=\mathbf{x}^{\mathsf T}B\mathbf{x}=0$, since $\mathbf{x}^{\mathsf T}B\mathbf{x}=-\mathbf{x}^{\mathsf T}B\mathbf{x}$). The matrices $I-B$ and $I+B$ commute, and $(I\pm B)^{\mathsf T}=I\mp B$, so
   $$A^{\mathsf T}A=(I-B)(I+B)^{-1}(I-B)^{-1}(I+B)=(I-B)(I-B)^{-1}(I+B)^{-1}(I+B)=I.$$

(b) Running the 32 steps numerically gives $U_{32}\approx(0.9998,\ 0.0201)$, exactly on the unit circle but not equal to $U_0=(1,0)$. Each step is a rotation by $2\arctan(\Delta t/2)$, slightly less than $\Delta t$, and $64\arctan(\pi/32)\approx2\pi-0.020$: after 32 steps the point falls short of a full turn by about $0.02$ radians.
:::
