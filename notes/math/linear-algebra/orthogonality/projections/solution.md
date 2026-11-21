<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-5-q6" status="draft"}
1. $C(A)$ is spanned by $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$: the vectors with last component $0$. The columns are orthonormal, so $P=AA^{\mathsf T}$ (@prp-projection-with-orthonormal-columns).

2. $P$ is $4\times4$:
   $$P=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&0\end{bmatrix},\qquad P\mathbf{b}=(1,2,3,0).$$
:::

::: {.solution for="prob-mit1806s10-5-q7" status="draft"}
1. Normal equations with $A=\begin{bmatrix}1&1\\2&0\\-1&1\end{bmatrix}$: $A^{\mathsf T}A=\begin{bmatrix}6&0\\0&2\end{bmatrix}$ and $A^{\mathsf T}\mathbf{b}=(3,3)$, so $\hat{\mathbf{x}}=(\frac12,\frac32)$.

2. $\frac12(1,2,-1)+\frac32(1,0,1)=(2,1,1)=\mathbf{b}$. The closest combination is $\mathbf{b}$ itself: $\mathbf{b}$ already lies in the plane of the two vectors, and the error is $\mathbf{0}$.
:::

::: {.solution for="prob-mit1806s10-5-q8" status="draft"}
1. $(I-P)^2=I-2P+P^2=I-2P+P=I-P$.

2. $I-P$ projects onto the *left nullspace* $N(A^{\mathsf T})$, the orthogonal complement of $C(A)$ (@prp-projection-matrix-properties).
:::

::: {.solution for="prob-mit1806s10-5-q9" status="draft"}
a. $A$ has rank $1$: $A=\mathbf{a}\mathbf{r}^{\mathsf T}$ with $\mathbf{a}=(3,4)$ and $\mathbf{r}=(1,2,2)$. So $C(A)$ is the line through $\mathbf{a}$ and
$$P_C=\frac{\mathbf{a}\mathbf{a}^{\mathsf T}}{\mathbf{a}^{\mathsf T}\mathbf{a}}=\frac1{25}\begin{bmatrix}9&12\\12&16\end{bmatrix}.$$

b.

1. The row space is the line through $\mathbf{r}$:
   $$P_R=\frac{\mathbf{r}\mathbf{r}^{\mathsf T}}{\mathbf{r}^{\mathsf T}\mathbf{r}}=\frac19\begin{bmatrix}1&2&2\\2&4&4\\2&4&4\end{bmatrix}.$$

2. $B=P_CAP_R=A$. Reason: every column of $A$ is already in $C(A)$, so $P_CA=A$. And for any $\mathbf{x}=\mathbf{x}_r+\mathbf{x}_n$ (@cor-orthogonal-decomposition), $AP_R\mathbf{x}=A\mathbf{x}_r=A\mathbf{x}$, so $AP_R=A$.
:::

::: {.solution for="prob-mit1806s10-5-q10" status="draft"}
Check two things:

1. $\mathbf{p}$ lies in the span of the $\mathbf{a}$'s (for example, $[A\ \mathbf{p}]$ has the same rank $n$ as $A=[\mathbf{a}_1\cdots\mathbf{a}_n]$);

2. the error $\mathbf{b}-\mathbf{p}$ is orthogonal to every $\mathbf{a}_i$: $A^{\mathsf T}(\mathbf{b}-\mathbf{p})=\mathbf{0}$.

Both are needed: $\mathbf{p}=\mathbf{b}$ always passes test 2 (its error $\mathbf{0}$ is orthogonal to everything), yet $\mathbf{b}$ need not lie in the subspace. Together the two conditions characterise the projection (@thm-projection-onto-subspace).
:::

::: {.solution for="prob-mit18065ps-10-q17" status="draft"}
1. $\widehat{x}=36/4=9$ (the mean of the data) and $\mathbf{p}=(9,9,9,9)$.

2. $\mathbf{e}=(-9,-1,-1,11)$ and $\mathbf{a}^{\mathsf T}\mathbf{e}=-9-1-1+11=0$.

3. $\lVert\mathbf{e}\rVert=\sqrt{81+1+1+121}=\sqrt{204}\approx14.3$.
:::
