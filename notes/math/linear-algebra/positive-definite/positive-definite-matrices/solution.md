<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-9-q1" status="draft"}
1. $A=C^{\mathsf T}C=\begin{bmatrix}3&0\\1&2\end{bmatrix}\begin{bmatrix}3&1\\0&2\end{bmatrix}=\begin{bmatrix}9&3\\3&5\end{bmatrix}$.

2. For $A=\begin{bmatrix}4&8\\8&25\end{bmatrix}$: the multiplier is $2$ and the pivots are $4$ and $25-16=9$, so $L=\begin{bmatrix}1&0\\2&1\end{bmatrix}$, $D=\operatorname{diag}(4,9)$ and
   $$C=\sqrt DL^{\mathsf T}=\begin{bmatrix}2&0\\0&3\end{bmatrix}\begin{bmatrix}1&2\\0&1\end{bmatrix}=\begin{bmatrix}2&4\\0&3\end{bmatrix}.$$
   Check: $C^{\mathsf T}C=\begin{bmatrix}4&8\\8&16+9\end{bmatrix}$.
:::

::: {.solution for="prob-mit1806s10-9-q2" status="draft"}
1. First matrix: pivots $9,1,8-4=4$, with the single multiplier $\ell_{32}=2$. So
   $$C=\sqrt DL^{\mathsf T}=\begin{bmatrix}3&0&0\\0&1&0\\0&0&2\end{bmatrix}\begin{bmatrix}1&0&0\\0&1&2\\0&0&1\end{bmatrix}=\begin{bmatrix}3&0&0\\0&1&2\\0&0&2\end{bmatrix}.$$

2. Second matrix: subtract row 1 from rows 2 and 3, then row 2 from row 3. The pivots are $1,1,5$ and all three multipliers are $1$. So
   $$C=\begin{bmatrix}1&0&0\\0&1&0\\0&0&\sqrt5\end{bmatrix}\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}=\begin{bmatrix}1&1&1\\0&1&1\\0&0&\sqrt5\end{bmatrix}.$$

3. Check the second: $C^{\mathsf T}C$ has $(3,3)$ entry $1+1+5=7$.
:::

::: {.solution for="prob-mit1806s10-9-q3" status="draft"}
1. Multiply out the right side: with $\mathbf{z}=L^{\mathsf T}\mathbf{x}=(x+\frac bay,\ y)$ it is $a\big(x+\frac bay\big)^2+\frac{ac-b^2}a\,y^2$. Expanding, $ax^2+2bxy+\frac{b^2}ay^2+\big(c-\frac{b^2}a\big)y^2=ax^2+2bxy+cy^2$.

2. So the blank is the second pivot $\frac{ac-b^2}a=c-\frac{b^2}a$.

3. Test: $2x^2+8xy+10y^2=2(x+2y)^2+2y^2$, since $2(x+2y)^2=2x^2+8xy+8y^2$. The pivots $2$ and $2$ are positive, so this form is positive definite.
:::

::: {.solution for="prob-mit1806s10-9-q4" status="draft"}
1. $F_1$: $\partial_xF_1=x^3+2x+2xy$, $\partial_yF_1=x^2+2y$. Setting both to $0$: $y=-x^2/2$, and then $x^3+2x-x^3=2x=0$. The only stationary point is $(0,0)$.

2. $H_1=\begin{pmatrix}3x^2+2+2y&2x\\2x&2\end{pmatrix}$, which at $(0,0)$ is $\begin{pmatrix}2&0\\0&2\end{pmatrix}$, positive definite. So $(0,0)$ is the minimum (@thm-second-derivative-test-several), with $F_1=0$.

3. $F_2$: $\partial_xF_2=3x^2+y-1$, $\partial_yF_2=x$. So $x=0$, $y=1$: the stationary point $(0,1)$.

4. $H_2=\begin{pmatrix}6x&1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ at $(0,1)$, with eigenvalues $1$ and $-1$: indefinite, so $(0,1)$ is a saddle point.
:::

::: {.solution for="prob-mit1806s10-9-q5" status="draft"}
(a) Not a group: $\begin{bmatrix}2&1\\1&1\end{bmatrix}$ and $\begin{bmatrix}1&0\\0&2\end{bmatrix}$ are positive definite, but their product $\begin{bmatrix}2&2\\1&2\end{bmatrix}$ is not symmetric. (Inverses do stay positive definite.)

(b) A group (@prob-mit1806s10-2-q8).

(c) A group: $e^{sA}e^{tA}=e^{(s+t)A}$ (powers of one matrix commute) and $(e^{tA})^{-1}=e^{-tA}$.

(d) Not a group: $\begin{bmatrix}1&4\\0&1\end{bmatrix}$ and $\begin{bmatrix}1&0\\-4&1\end{bmatrix}$ both have the eigenvalue $1$ (twice), but their product $\begin{bmatrix}-15&4\\-4&1\end{bmatrix}$ has determinant $1$ and trace $-14$, so both of its eigenvalues are negative.

(e) A group, by the product rule $\det AB=\det A\det B$ and $\det A^{-1}=1/\det A$.

Subgroups: the orthogonal matrices with determinant $1$ (the rotations) lie in both (b) and (e); the diagonal matrices with entries $\pm1$ form a finite subgroup of (b).
:::

::: {.solution for="prob-mit1806s10-9-q6" status="draft"}
1. Take the dot product of $AB\mathbf{x}=\lambda\mathbf{x}$ with $B\mathbf{x}$: $(B\mathbf{x})^{\mathsf T}A(B\mathbf{x})=\lambda\,\mathbf{x}^{\mathsf T}B\mathbf{x}$ (using $B^{\mathsf T}=B$).

2. $\mathbf{x}\neq\mathbf{0}$ and $B$ is invertible, so $B\mathbf{x}\neq\mathbf{0}$. Positive definiteness gives $(B\mathbf{x})^{\mathsf T}A(B\mathbf{x})>0$ and $\mathbf{x}^{\mathsf T}B\mathbf{x}>0$ (for complex $\mathbf{x}$, use $\bar{\mathbf{x}}^{\mathsf T}$; both quantities are still real and positive).

3. Hence $\lambda=\dfrac{(B\mathbf{x})^{\mathsf T}A(B\mathbf{x})}{\mathbf{x}^{\mathsf T}B\mathbf{x}}>0$.
:::

::: {.solution for="prob-mit1806s10-9-q8" status="draft"}
1. $A^{\mathsf T}CA$ is symmetric: $(A^{\mathsf T}CA)^{\mathsf T}=A^{\mathsf T}C^{\mathsf T}A=A^{\mathsf T}CA$.

2. For $\mathbf{z}\neq\mathbf{0}$: $\mathbf{z}^{\mathsf T}A^{\mathsf T}CA\mathbf{z}=(A\mathbf{z})^{\mathsf T}C(A\mathbf{z})$. Full column rank means $N(A)=\{\mathbf{0}\}$, so $A\mathbf{z}\neq\mathbf{0}$, and positive definiteness of $C$ gives a positive number.
:::

::: {.solution for="prob-mit1806s10-9-q9" status="draft"}
1. Each column of $A^{\mathsf T}CA$ adds to zero, so adding the three equations gives $0=f_1+f_2+f_3$.

2. For $\mathbf{f}=(-1,0,1)$ the equations are $c_2(u_1-u_2)=-1$, $-c_2(u_1-u_2)+c_3(u_2-u_3)=0$, $c_3(u_3-u_2)=1$; the middle one follows from the other two. Taking $u_2=0$ gives the particular solution $\mathbf{u}_p=(-\frac1{c_2},\ 0,\ \frac1{c_3})$.

3. The nullspace is the line of constant vectors (rigid motion of the free system), so all solutions are $\mathbf{u}=\big(-\frac1{c_2},0,\frac1{c_3}\big)+t(1,1,1)$.
:::

::: {.solution for="prob-mit1806s10-9-q10" status="draft"}
1. Integrate from $x$ to $1$: $y(1)-y(x)=-\int_x^1f(s)\,ds$, so $y(x)=\int_x^1f(s)\,ds$.

2. For $f=1$: $y(x)=1-x$, a straight line from $(0,1)$ down to $(1,0)$.
:::

::: {.solution for="prob-mit1806s10-9-q11" status="draft"}
1. Spring $i$ stretches by $e_i=u_i-u_{i-1}$ with $u_0=u_5=0$, so $A$ is $5\times4$:
   $$A=\begin{bmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\\0&0&0&-1\end{bmatrix},\qquad C=\operatorname{diag}(c_1,\dots,c_5),$$
   $$K=A^{\mathsf T}CA=\begin{bmatrix}c_1+c_2&-c_2&0&0\\-c_2&c_2+c_3&-c_3&0\\0&-c_3&c_3+c_4&-c_4\\0&0&-c_4&c_4+c_5\end{bmatrix}.$$

2. With $C=I$, $K$ is the $-1,2,-1$ matrix and
   $$K^{-1}=\frac15\begin{bmatrix}4&3&2&1\\3&6&4&2\\2&4&6&3\\1&2&3&4\end{bmatrix},\qquad \mathbf{u}=K^{-1}(1,1,1,1)=(2,3,3,2).$$
   Check: $K\mathbf{u}=(4-3,\ -2+6-3,\ -3+6-2,\ -3+4)=(1,1,1,1)$.
:::

::: {.solution for="prob-mit1806s10-9-q12" status="draft"}
1. Fixed-fixed: $K$ is the $100\times100$ matrix with $2$ on the diagonal and $-1$ beside it. Solving $K\mathbf{u}=0.01\cdot\mathbf{1}$ gives the parabola $u(i)=0.005\,i(101-i)$ (its second difference is $-0.01$ and it vanishes at $i=0,101$). The graph rises from $0.5$ to a maximum $12.75$ at $i=50,51$ and falls back symmetrically.

2. Fixed-free: change the last diagonal entry to $1$. Now $u(i)=0.01\big(100i-\frac{i(i-1)}2\big)$, which increases all the way to $u(100)=50.5$, flattening out near the free end: the top springs carry the weight of all the masses below.

3. The plots are produced exactly as in the given command; for example in Python, `numpy.linalg.solve(K, 0.01*numpy.ones(100))` followed by a scatter plot.
:::

::: {.solution for="prob-mit1806s10-9-q13" status="draft"}
1. There are $7$ unknowns $u_1,\dots,u_7$ at $x=\frac18,\dots,\frac78$. With $E$ the matrix with $1$s just above the diagonal, $-u''$ becomes $K=64(2I-E-E^{\mathsf T})$, and $10u'$ becomes
   $$80(E-I)\ \text{(forward)},\qquad 40(E-E^{\mathsf T})\ \text{(centered)},\qquad 80(I-E^{\mathsf T})\ \text{(backward)}.$$

2. Solving $(K+D)\mathbf{u}=\mathbf{1}$ in each case gives (to four decimals)

   | $x$ | $\frac18$ | $\frac28$ | $\frac38$ | $\frac48$ | $\frac58$ | $\frac68$ | $\frac78$ |
   |---|---|---|---|---|---|---|---|
   | forward | 0.0125 | 0.0250 | 0.0376 | 0.0496 | 0.0641 | 0.0688 | 0.1125 |
   | centered | 0.0125 | 0.0250 | 0.0374 | 0.0497 | 0.0613 | 0.0697 | 0.0644 |
   | backward | 0.0123 | 0.0244 | 0.0359 | 0.0462 | 0.0539 | 0.0554 | 0.0431 |
   | exact | 0.0125 | 0.0249 | 0.0373 | 0.0493 | 0.0602 | 0.0668 | 0.0589 |

   The exact solution is $u=\frac x{10}-\frac{e^{10x}-1}{10(e^{10}-1)}$: nearly the line $x/10$, with a boundary layer at $x=1$.

3. Graphing the three: the centered difference follows the exact solution best; the forward difference overshoots badly at the last point, and the backward (upwind) difference is too damped near $x=1$.
:::
