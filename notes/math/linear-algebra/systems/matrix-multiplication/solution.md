<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-1-q11" status="draft"}
Column $j$ of $AX$ is $A\mathbf{x}_j$ (@thm-four-ways-to-multiply), so the columns of $AX$ are the three columns of $I$: $AX=I$. Thus $X=A^{-1}$; this is the idea behind Gauss–Jordan.
:::

::: {.solution for="prob-mit1806s10-1-q12" status="draft"}
(a) $(AB)C$ costs $2\cdot4\cdot7+2\cdot7\cdot10=56+140=196$; $A(BC)$ costs $2\cdot4\cdot10+4\cdot7\cdot10=80+280=360$. Prefer $(AB)C$.

(b) $\mathbf{u}^{\mathsf T}\mathbf{v}$ is a number ($N$ multiplications), and multiplying the row $\mathbf{w}^{\mathsf T}$ by it costs $N$ more: $2N$ in all. The other order first forms the $N\times N$ matrix $\mathbf{v}\mathbf{w}^{\mathsf T}$ ($N^2$) and then $\mathbf{u}^{\mathsf T}$ times it ($N^2$): $2N^2$. Choose $(\mathbf{u}^{\mathsf T}\mathbf{v})\mathbf{w}^{\mathsf T}$.

(c) $(AB)C$ is faster when $mnp+mpq<mnq+npq$. Dividing by $mnpq>0$ gives $\frac1q+\frac1n<\frac1p+\frac1m$.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words; owner to review, then remove status.
     MIT 18.02 problem-set problems (prob-mit1802f07-*): no official solutions were available.
     18.02 Notes exercises (prob-mit1802n-*): checked by computation (Python/sympy); official solutions (section S
     of the 18.02 Notes) exist in raw/ but were not copied. -->

::: {.solution for="prob-mit1802n-1f-q5" status="draft"}
a) $A^2=\begin{pmatrix}1&1\\1&2\end{pmatrix}$, $A^3=\begin{pmatrix}1&2\\2&3\end{pmatrix}$, and in general $A^n=\begin{pmatrix}F_{n-1}&F_n\\F_n&F_{n+1}\end{pmatrix}$ with the Fibonacci numbers $F_0=0$, $F_1=1$, $F_{k+1}=F_k+F_{k-1}$. (Induction: multiplying by $A$ on the right sends the columns $(\mathbf{c}_1,\mathbf{c}_2)$ to $(\mathbf{c}_2,\mathbf{c}_1+\mathbf{c}_2)$.)

b) $A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, $A^3=\begin{pmatrix}1&3\\0&1\end{pmatrix}$, $A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$ (each multiplication adds $1$ to the corner).
:::

::: {.solution for="prob-mit1802n-1f-q8" status="draft"}
$A$ times the $j$-th unit vector is the $j$-th column of $A$:
$$A=\begin{pmatrix}2&-1&1\\3&0&1\\1&4&-1\end{pmatrix}.$$
:::

::: {.solution for="prob-mit18065ps-27-q2" status="draft"}
1. A product of $p\times q$ by $q\times r$ costs $pqr$ multiplications.

2. $A^{\mathsf T}A$ costs $n\cdot m\cdot n=mn^2$, then $A(A^{\mathsf T}A)$ costs $m\cdot n\cdot n=mn^2$: total $2mn^2$.

3. $AA^{\mathsf T}$ costs $m^2n$, then $(AA^{\mathsf T})A$ costs $m\cdot m\cdot n=m^2n$: total $2m^2n$.

4. Since $m>n$, $2mn^2<2m^2n$: $A(A^{\mathsf T}A)$ is faster, by the factor $m/n$. The order of multiplication matters, as it does in backpropagation.
:::
