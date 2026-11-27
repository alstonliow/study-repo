<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.2, restated in our own words with our own checks. -->

::: {#exm-minimal-polynomial-identity-shear .example name="Same characteristic polynomial, different minimal polynomials"}

Let $A=I_2$ and $B=\begin{bmatrix}1&1\\0&1\end{bmatrix}$ over any field.

1. $(A-I)^2=0$ and $(B-I)^2=0$, so both minimal polynomials divide $(t-1)^2$: each is $t-1$ or $(t-1)^2$.

2. $A-I=0$, so $m_A=t-1$; $B-I\ne0$, so $m_B=(t-1)^2$.

So $A$ is diagonalisable and $B$ is not, although $\chi_A=\chi_B=(t-1)^2$.

:::

::: {#exm-minimal-polynomial-three-by-three .example name="A minimal polynomial with distinct roots"}

Let $A=\begin{bmatrix}1&0&-2\\0&1&1\\0&0&2\end{bmatrix}$.

1. $A$ is upper triangular, so $\chi_A=(t-1)^2(t-2)$, and $m_A$ is $(t-1)(t-2)$ or $(t-1)^2(t-2)$.

2. $A-I=\begin{bmatrix}0&0&-2\\0&0&1\\0&0&1\end{bmatrix}$ and $A-2I=\begin{bmatrix}-1&0&-2\\0&-1&1\\0&0&0\end{bmatrix}$; multiplying out gives $(A-I)(A-2I)=0$.

3. Hence $m_A=(t-1)(t-2)$, a product of distinct linear factors, and $A$ is diagonalisable.

:::
