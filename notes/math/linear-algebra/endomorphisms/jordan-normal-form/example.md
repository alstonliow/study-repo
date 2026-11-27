<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.4, restated in our own words with our own checks. -->

::: {#exm-multiplicities-jordan-block .example name="Multiplicities of a Jordan block and of a scalar matrix"}

1. For the $n\times n$ Jordan block $J_n(\lambda)$: $\chi=(t-\lambda)^n$, so the algebraic multiplicity is $n$; $J_n(\lambda)-\lambda I$ has rank $n-1$, so the geometric multiplicity is $1$; and $(J_n(\lambda)-\lambda I)^{n-1}\ne0=(J_n(\lambda)-\lambda I)^n$, so $\lambda$ has multiplicity $n$ in the minimal polynomial.

2. For $\lambda I_n$: algebraic and geometric multiplicity are both $n$, and the minimal polynomial is $t-\lambda$, multiplicity $1$.

:::

::: {#exm-small-jordan-forms .example name="All Jordan normal forms of size 2 and 3"}

Here $\lambda,\mu$ and $\lambda_1,\lambda_2,\lambda_3$ are distinct complex numbers.

| size | Jordan normal form | $\chi_A$ | $m_A$ |
|---|---|---|---|
| 2 | $\operatorname{diag}(\lambda,\lambda)$ | $(t-\lambda)^2$ | $t-\lambda$ |
| 2 | $\operatorname{diag}(\lambda,\mu)$ | $(t-\lambda)(t-\mu)$ | $(t-\lambda)(t-\mu)$ |
| 2 | $J_2(\lambda)$ | $(t-\lambda)^2$ | $(t-\lambda)^2$ |
| 3 | $\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$ | $(t-\lambda_1)(t-\lambda_2)(t-\lambda_3)$ | $(t-\lambda_1)(t-\lambda_2)(t-\lambda_3)$ |
| 3 | $\operatorname{diag}(\lambda_1,\lambda_1,\lambda_2)$ | $(t-\lambda_1)^2(t-\lambda_2)$ | $(t-\lambda_1)(t-\lambda_2)$ |
| 3 | $J_2(\lambda_1)\oplus(\lambda_2)$ | $(t-\lambda_1)^2(t-\lambda_2)$ | $(t-\lambda_1)^2(t-\lambda_2)$ |
| 3 | $\lambda_1I_3$ | $(t-\lambda_1)^3$ | $t-\lambda_1$ |
| 3 | $J_2(\lambda_1)\oplus(\lambda_1)$ | $(t-\lambda_1)^3$ | $(t-\lambda_1)^2$ |
| 3 | $J_3(\lambda_1)$ | $(t-\lambda_1)^3$ | $(t-\lambda_1)^3$ |

For size $2$ and $3$ the pair $(\chi_A,m_A)$ determines the Jordan normal form; for size $2$ the minimal polynomial alone does. From size $4$ on it does not: $J_2(\lambda)\oplus J_2(\lambda)$ and $J_2(\lambda)\oplus J_1(\lambda)\oplus J_1(\lambda)$ share both.

:::

::: {#exm-jordan-basis-two-eigenvalues .example name="A Jordan basis with two eigenvalues"}

Let $A=\begin{bmatrix}3&-2&0\\1&0&0\\1&0&1\end{bmatrix}$.

1. Expanding along the last column, $\chi_A=(t-1)\bigl(t(t-3)+2\bigr)=(t-1)^2(t-2)$.

2. $A-I=\begin{bmatrix}2&-2&0\\1&-1&0\\1&0&0\end{bmatrix}$ has rank $2$, so $E(1)=\langle e_3\rangle$ has dimension $1<2$. Hence $A$ is not diagonalisable, $m_A=\chi_A$, and the Jordan normal form is $J_2(1)\oplus(2)$.

3. $A-2I=\begin{bmatrix}1&-2&0\\1&-2&0\\1&0&-1\end{bmatrix}$ has kernel $E(2)=\langle(2,1,2)^{\mathsf T}\rangle$; take $v_3=(2,1,2)^{\mathsf T}$.

4. We need $v_1,v_2$ with $(A-I)v_1=0$ and $(A-I)v_2=v_1$, so $v_2\in\ker(A-I)^2\setminus\ker(A-I)$. Here $(A-I)^2=\begin{bmatrix}2&-2&0\\1&-1&0\\2&-2&0\end{bmatrix}$, with kernel $\langle e_3,(1,1,0)^{\mathsf T}\rangle$. Take $v_2=(1,1,0)^{\mathsf T}$; then $v_1=(A-I)v_2=e_3$.

5. With $P=[v_1\ v_2\ v_3]=\begin{bmatrix}0&1&2\\0&1&1\\1&0&2\end{bmatrix}$, one checks $Av_1=v_1$, $Av_2=(1,1,1)^{\mathsf T}=v_1+v_2$, $Av_3=2v_3$, so
$$P^{-1}AP=\begin{bmatrix}1&1&0\\0&1&0\\0&0&2\end{bmatrix}.$$

:::
