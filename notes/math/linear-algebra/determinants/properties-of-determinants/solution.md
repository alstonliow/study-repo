<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-6-q10" status="draft"}
1. With $\mathbf{x}=(1,1,\dots,1)$, component $i$ of $A\mathbf{x}$ is the sum of row $i$, which is $0$. So $A$ is singular and $\det A=0$ (@thm-determinant-consequences).

2. If every row adds to $1$, every row of $A-I$ adds to $0$, so $\det(A-I)=0$ by step 1.

3. This does not mean $\det A=1$: $A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ has row sums $1$ but $\det A=-1$. (It says $1$ is an eigenvalue of $A$.)
:::

::: {.solution for="prob-mit1806s10-6-q11" status="draft"}
1. Subtract row 1 from rows 2 and 3 (determinant unchanged):
   $$\det\begin{bmatrix}1&a&a^2\\0&b-a&(b-a)(b+a)\\0&c-a&(c-a)(c+a)\end{bmatrix}.$$

2. Factor $b-a$ out of row 2 and $c-a$ out of row 3 (linearity in each row):
   $$(b-a)(c-a)\det\begin{bmatrix}1&a&a^2\\0&1&b+a\\0&1&c+a\end{bmatrix}.$$

3. Subtract row 2 from row 3: the last row becomes $(0,0,c-b)$. The matrix is triangular with diagonal $1,1,c-b$, so the determinant is $(b-a)(c-a)(c-b)$.
:::

::: {.solution for="prob-mit1806s10-6-q12" status="draft"}
1. Computing exactly (with fractions), the determinants are
   $$1,\ \tfrac1{12},\ \tfrac1{2160},\ \tfrac1{6048000},\ \approx3.7\times10^{-12},\ \approx5.4\times10^{-18},\ \dots,\ \det\texttt{hilb(10)}\approx2.2\times10^{-53}.$$
   They shrink extremely fast; in floating point the later ones are dominated by rounding errors.

2. The pivots of hilb(5) are
   $$1,\ \tfrac1{12},\ \tfrac1{180},\ \tfrac1{2800},\ \tfrac1{44100}\ \ (\approx1,\ 0.0833,\ 0.0056,\ 0.00036,\ 0.000023),$$
   all positive (the Hilbert matrix is positive definite) and their product is $\det\texttt{hilb(5)}$. The tiny last pivot is why the matrix is so hard to work with numerically.
:::

::: {.solution for="prob-mit1806s10-6-q13" status="draft"}
1. An experiment (five random matrices of each size, looking at $\log_{10}\lvert\det\rvert$) gives roughly:

   | $n$ | rand(n) | randn(n) |
   |---|---|---|
   | 50 | $10^{5}$–$10^{7}$ | $10^{31}$ |
   | 100 | $10^{25}$ | $10^{78}$ |
   | 200 | $10^{80}$ | $10^{185}$ |
   | 400 | $10^{219}$ | $10^{433}$ |

   The determinant grows faster than exponentially in $n$ (roughly like $\sqrt{n!}$ for randn).

2. "Inf" is the floating-point value for overflow: the largest double is about $1.8\times10^{308}$, so $\det(\texttt{randn(400)})\approx10^{433}$ is reported as Inf.
:::
