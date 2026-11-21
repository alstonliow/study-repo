<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-2-q9" status="draft"}
1. Entry $(i,j)$ of $Q^{\mathsf T}Q$ is row $i$ of $Q^{\mathsf T}$ (that is, $\mathbf{q}_i^{\mathsf T}$) times column $j$ of $Q$: it is $\mathbf{q}_i^{\mathsf T}\mathbf{q}_j$.

2. (a) The diagonal of $I$ gives $\mathbf{q}_i^{\mathsf T}\mathbf{q}_i=\lVert\mathbf{q}_i\rVert^2=1$.

3. (b) The off-diagonal zeros of $I$ give $\mathbf{q}_i^{\mathsf T}\mathbf{q}_j=0$ for $i\neq j$.

4. (c) The rotation $Q=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$: its columns are unit vectors ($\cos^2\theta+\sin^2\theta=1$) and their dot product is $-\cos\theta\sin\theta+\sin\theta\cos\theta=0$.
:::

::: {.solution for="prob-mit1806s10-6-q6" status="draft"}
(a) Take the dot product with $\mathbf{q}_1$: $c_1\mathbf{q}_1^{\mathsf T}\mathbf{q}_1+c_2\mathbf{q}_1^{\mathsf T}\mathbf{q}_2+c_3\mathbf{q}_1^{\mathsf T}\mathbf{q}_3=c_1\cdot1+0+0=0$. Dotting with $\mathbf{q}_2$ and $\mathbf{q}_3$ gives $c_2=c_3=0$.

(b) Multiply $Q\mathbf{x}=\mathbf{0}$ by $Q^{\mathsf T}$: $\mathbf{x}=Q^{\mathsf T}Q\mathbf{x}=\mathbf{0}$, since $Q^{\mathsf T}Q=I$. So $N(Q)=\{\mathbf{0}\}$ and the columns are independent.
:::

::: {.solution for="prob-mit1806s10-6-q7" status="draft"}
1. $A=\mathbf{a}/\lVert\mathbf{a}\rVert=\frac1{\sqrt2}(1,-1,0,0)$.

2. $\mathbf{b}-(A^{\mathsf T}\mathbf{b})A=(0,1,-1,0)+\frac12(1,-1,0,0)=\frac12(1,1,-2,0)$, so $B=\frac1{\sqrt6}(1,1,-2,0)$.

3. $A^{\mathsf T}\mathbf{c}=0$ and $B^{\mathsf T}\mathbf{c}=-\frac2{\sqrt6}$, so $\mathbf{c}-(B^{\mathsf T}\mathbf{c})B=(0,0,1,-1)+\frac13(1,1,-2,0)=\frac13(1,1,1,-3)$ and $C=\frac1{\sqrt{12}}(1,1,1,-3)$.

4. Each of $\mathbf{a},\mathbf{b},\mathbf{c}$ has components summing to $0$, so they lie in $N([1\ 1\ 1\ 1])=\mathbf{d}^{\perp}$, which has dimension $4-1=3$. They are independent: $x_1\mathbf{a}+x_2\mathbf{b}+x_3\mathbf{c}=(x_1,\ x_2-x_1,\ x_3-x_2,\ -x_3)=\mathbf{0}$ forces $x_1=x_2=x_3=0$. Three independent vectors in a 3-dimensional space are a basis (@cor-basis-from-independent-set).

5. $A,B,C$ are combinations of $\mathbf{a},\mathbf{b},\mathbf{c}$, so they are in the same space, and orthonormal vectors are independent (@prob-mit1806s10-6-q6). So they are a basis too.
:::

::: {.solution for="prob-mit1806s10-6-q8" status="draft"}
1. The first three columns are the vectors of @prob-mit1806s10-6-q7, so the first three columns of $Q$ are $\frac1{\sqrt2}(1,-1,0,0)$, $\frac1{\sqrt6}(1,1,-2,0)$, $\frac1{\sqrt{12}}(1,1,1,-3)$.

2. The fourth column $(0,0,0,1)$ minus its projections onto those three leaves a vector orthogonal to all of them, hence in the direction of $(1,1,1,1)$; normalised, $\frac12(1,1,1,1)$.

3. Scaling the columns by $\sqrt2,\sqrt6,\sqrt{12},2$ gives the integer matrix
   $$\begin{bmatrix}1&1&1&1\\-1&1&1&1\\0&-2&1&1\\0&0&-3&1\end{bmatrix},$$
   whose columns are orthogonal. (MATLAB may return some columns with the opposite sign.)
:::

::: {.solution for="prob-mit1806s10-6-q9" status="draft"}
1. $A=Q_1R$ with $R$ invertible, so $C(A)=C(Q_1)$: the columns of $Q_1$ are an orthonormal basis of the column space (@thm-qr-factorization).

2. The columns of $Q_2$ are orthonormal and orthogonal to those of $Q_1$, hence to $C(A)$. They lie in $C(A)^{\perp}=N(A^{\mathsf T})$, which has dimension $m-n$, so they are an orthonormal basis of the left nullspace.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802f07-1-q4" status="draft"}
a) $\mathbf{u}=\langle\cos\theta,\sin\theta\rangle$ and $\mathbf{v}=\langle-\sin\theta,\cos\theta\rangle$: $\hat\imath$ and $\hat\jmath$ turned counterclockwise by $\theta$. For $\theta=\pi/4$, $\mathbf{u}=\frac1{\sqrt2}\langle1,1\rangle$ and $\mathbf{v}=\frac1{\sqrt2}\langle-1,1\rangle$, unit vectors at $45^\circ$ and $135^\circ$.

b) $A_{\theta_1}A_{\theta_2}=\begin{pmatrix}c_1c_2-s_1s_2&-(c_1s_2+s_1c_2)\\s_1c_2+c_1s_2&c_1c_2-s_1s_2\end{pmatrix}=\begin{pmatrix}\cos(\theta_1+\theta_2)&-\sin(\theta_1+\theta_2)\\\sin(\theta_1+\theta_2)&\cos(\theta_1+\theta_2)\end{pmatrix}$ (with $c_i=\cos\theta_i$, $s_i=\sin\theta_i$). Rotating by $\theta_2$ and then by $\theta_1$ is the same as rotating by $\theta_1+\theta_2$.

c) $\det A_\theta=\cos^2\theta+\sin^2\theta=1$, so by the cofactor formula $A_\theta^{-1}=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix}=A_\theta^T$; hence $A_\theta A_\theta^T=A_\theta A_\theta^{-1}=I$. Since $\cos(-\theta)=\cos\theta$ and $\sin(-\theta)=-\sin\theta$, this matrix is also $A_{-\theta}$: the rotation that undoes a rotation by $\theta$ is the rotation by $-\theta$.

d) The first column is a unit vector with first entry $-\frac1{\sqrt2}$, so it is $\frac1{\sqrt2}\langle-1,\pm1\rangle$; the second column is a unit vector perpendicular to it, one of two opposite choices. The four matrices are
$$\tfrac1{\sqrt2}\begin{pmatrix}-1&-1\\1&-1\end{pmatrix},\quad\tfrac1{\sqrt2}\begin{pmatrix}-1&1\\1&1\end{pmatrix},\quad\tfrac1{\sqrt2}\begin{pmatrix}-1&1\\-1&-1\end{pmatrix},\quad\tfrac1{\sqrt2}\begin{pmatrix}-1&-1\\-1&1\end{pmatrix},$$
with determinants $1,-1,1,-1$. The first is the rotation $A_{3\pi/4}$, the third is $A_{-3\pi/4}$; the second and fourth are reflections (in the lines through the origin at angles $3\pi/8$ and $-3\pi/8$, i.e. $67.5^\circ$ and $-67.5^\circ$).

e) (Drawings omitted.) The two rotations turn the F by $\pm135^\circ$; it still reads as an F. The two reflections produce a mirror-image F. A matrix with positive determinant keeps the orientation (counterclockwise stays counterclockwise), one with negative determinant reverses it, which is what makes the letter appear mirrored.
:::

::: {.solution for="prob-mit1802n-1f-q9" status="draft"}
The $(i,j)$ entry of $AA^T$ is (row $i$ of $A$)$\cdot$(column $j$ of $A^T$) $=$ (row $i$)$\cdot$(row $j$). So $AA^T=I_n$ means: (row $i$)$\cdot$(row $i$)$=1$ for every $i$, i.e. (a), and (row $i$)$\cdot$(row $j$)$=0$ for $i\ne j$, i.e. (b).
:::

::: {.solution for="prob-mit18065ps-3-q4" status="draft"}
$(Q\mathbf{x})^{\mathsf T}(Q\mathbf{y})=\mathbf{x}^{\mathsf T}Q^{\mathsf T}Q\mathbf{y}=\mathbf{x}^{\mathsf T}I\mathbf{y}=\mathbf{x}^{\mathsf T}\mathbf{y}$, using $Q^{\mathsf T}Q=I$. Taking $\mathbf{y}=\mathbf{x}$ gives $\lVert Q\mathbf{x}\rVert^2=\lVert\mathbf{x}\rVert^2$. Since dot products and lengths are preserved, so are the cosines of angles $\mathbf{x}^{\mathsf T}\mathbf{y}/(\lVert\mathbf{x}\rVert\lVert\mathbf{y}\rVert)$.
:::

::: {.solution for="prob-mit18065ps-3-q6" status="draft"}
1. The columns of a permutation matrix are the columns $\mathbf{e}_1,\dots,\mathbf{e}_n$ of $I$ in another order, each used once. These are unit vectors and any two different ones are orthogonal.

2. Entry $(i,j)$ of $P^{\mathsf T}P$ is (column $i$)$^{\mathsf T}$(column $j$), which is $1$ for $i=j$ and $0$ otherwise. So $P^{\mathsf T}P=I$ and $P^{-1}=P^{\mathsf T}$.
:::

::: {.solution for="prob-mit18065ps-9-q8" status="draft"}
1. The multiple is $\mathbf{a}^{\mathsf T}\mathbf{b}/\mathbf{a}^{\mathsf T}\mathbf{a}=4/2=2$, so $\mathbf{A}_2=\mathbf{b}-2\mathbf{a}=(2,-2)$, and $\mathbf{a}^{\mathsf T}\mathbf{A}_2=0$.

2. Sketch: $\mathbf{a}$ points along the diagonal at $45^\circ$; $\mathbf{b}$ along the $x$-axis; $2\mathbf{a}=(2,2)$ is the projection of $\mathbf{b}$ onto the line of $\mathbf{a}$, and $\mathbf{A}_2$ goes from the tip of $2\mathbf{a}$ to the tip of $\mathbf{b}$, at $-45^\circ$, perpendicular to $\mathbf{a}$.
:::

::: {.solution for="prob-mit18065ps-9-q9" status="draft"}
1. $\mathbf{q}_1=(1,1)/\sqrt2$ and $\mathbf{q}_2=(2,-2)/(2\sqrt2)=(1,-1)/\sqrt2$.

2. The missing entry is $\mathbf{q}_1^{\mathsf T}\mathbf{b}=4/\sqrt2=2\sqrt2$; also $\lVert\mathbf{a}\rVert=\sqrt2$ and $\lVert\mathbf{A}_2\rVert=2\sqrt2$:
$$\begin{bmatrix}1&4\\1&0\end{bmatrix}=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}\begin{bmatrix}\sqrt2&2\sqrt2\\0&2\sqrt2\end{bmatrix}.$$

3. Check column 2: $2\sqrt2\,\mathbf{q}_1+2\sqrt2\,\mathbf{q}_2=(2,2)+(2,-2)=(4,0)$.
:::
