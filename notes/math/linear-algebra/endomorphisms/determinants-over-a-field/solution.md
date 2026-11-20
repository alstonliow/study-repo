<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-2-q4" status="draft"}
1. Column operations: for each $j=1,\dots,n$ and each $k=1,\dots,n$, add $b_{kj}$ times column $k$ to column $n+j$. Together these add to the right block column the left block column times $B$:
$$\begin{pmatrix}-B\\0\end{pmatrix}+\begin{pmatrix}I\\A\end{pmatrix}B=\begin{pmatrix}0\\AB\end{pmatrix},$$
and the left block column is unchanged. So $C$ becomes $D$.

2. Adding a multiple of one column to another does not change the determinant (multilinearity plus the alternating property, @thm-volume-forms-unique). So $\det C=\det D$.

3. $D$ is block lower triangular, so $\det D=\det I\cdot\det(AB)=\det(AB)$ (@lem-block-triangular-determinant with @lem-determinant-transpose).

4. Moving each of the last $n$ columns of $C$ past the first $n$ columns takes $n\cdot n$ adjacent exchanges and gives $\begin{pmatrix}-B&I\\0&A\end{pmatrix}$. So $\det C=(-1)^{n^2}\det(-B)\det A=(-1)^{n^2+n}\det A\det B=\det A\det B$, since $n^2+n=n(n+1)$ is even.

5. Hence $\det(AB)=\det A\det B$.
:::

::: {.solution for="prob-camib-las-2-q6" status="draft"}
For non-singular $X$, $\operatorname{adj}X=(\det X)X^{-1}$ by @thm-adjugate.

(i) $\operatorname{adj}(AB)=\det(AB)(AB)^{-1}=(\det B\,B^{-1})(\det A\,A^{-1})=\operatorname{adj}B\operatorname{adj}A$.

(ii) $\det(\operatorname{adj}A)=\det\big((\det A)A^{-1}\big)=(\det A)^n(\det A)^{-1}=(\det A)^{n-1}$.

(iii) $\operatorname{adj}(\operatorname{adj}A)=\det(\operatorname{adj}A)(\operatorname{adj}A)^{-1}=(\det A)^{n-1}\cdot\frac{A}{\det A}=(\det A)^{n-2}A$.

Rank of $\operatorname{adj}A$:

1. $\operatorname{rk}A=n$: $\operatorname{adj}A=(\det A)A^{-1}$ is invertible, rank $n$.

2. $\operatorname{rk}A\le n-2$: every $n-1$ rows of $A$ are dependent, so every $(n-1)\times(n-1)$ submatrix has dependent rows and determinant $0$ (@thm-determinant-invertible). All cofactors vanish: $\operatorname{adj}A=0$.

3. $\operatorname{rk}A=n-1$: some $n-1$ rows are independent, and among them some $n-1$ columns are independent (row rank = column rank for that $(n-1)\times n$ block), giving a non-zero $(n-1)$-minor; so $\operatorname{adj}A\ne0$. Also $A\operatorname{adj}A=(\det A)I=0$, so every column of $\operatorname{adj}A$ lies in $\ker A$, of dimension $1$. Hence $\operatorname{rk}\operatorname{adj}A=1$.

Singular $A$: all three still hold.

(i) $\det(A+\lambda I)$ is a monic polynomial of degree $n$ in $\lambda$, so for all but finitely many $\lambda$ both $A+\lambda I$ and $B+\lambda I$ are invertible and $\operatorname{adj}((A+\lambda I)(B+\lambda I))=\operatorname{adj}(B+\lambda I)\operatorname{adj}(A+\lambda I)$. Each entry of each side is a polynomial in $\lambda$; if $\mathbb F$ is infinite, two polynomials agreeing at infinitely many points are equal (@thm-at-most-d-roots), and $\lambda=0$ gives (i). For finite $\mathbb F$: treat the entries of $A$ and $B$ as indeterminates; the identity holds over the infinite field of rational functions $\mathbb Q(a_{ij},b_{ij})$ by the same argument, so it is an identity of polynomials with integer coefficients, valid in every field.

(ii) If $\det A=0$, then $\operatorname{rk}\operatorname{adj}A\le1<n$, so $\det\operatorname{adj}A=0=(\det A)^{n-1}$.

(iii) For $n=2$, $\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ and applying $\operatorname{adj}$ twice gives $A=(\det A)^0A$. For $n\ge3$ and $A$ singular, $\operatorname{rk}\operatorname{adj}A\le1\le n-2$, so $\operatorname{adj}(\operatorname{adj}A)=0=(\det A)^{n-2}A$.
:::
