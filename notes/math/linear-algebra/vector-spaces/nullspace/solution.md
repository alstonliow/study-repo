<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-3-q3" status="draft"}
$C\mathbf{x}=\begin{bmatrix}A\mathbf{x}\\B\mathbf{x}\end{bmatrix}$ by block multiplication, which is zero exactly when both $A\mathbf{x}=\mathbf{0}$ and $B\mathbf{x}=\mathbf{0}$. Hence
$$N(C)=N(A)\cap N(B).$$
:::

::: {.solution for="prob-mit1806s10-3-q7" status="draft"}
(a) $I$ is $r\times r$, $F$ is $r\times(n-r)$, the zero blocks are $(m-r)\times r$ and $(m-r)\times(n-r)$.

(b) If $r=m$ there are no zero rows: $R=[I\ F]$. Take $B=\begin{bmatrix}I\\0\end{bmatrix}$ ($n\times r$); then $RB=I$.

(c) If $r=n$ there is no $F$: $R=\begin{bmatrix}I\\0\end{bmatrix}$. Take $C=[I\ 0]$ ($r\times m$); then $CR=I$.

(d) $R^{\mathsf T}=\begin{bmatrix}I&0\\F^{\mathsf T}&0\end{bmatrix}$ ($n\times m$). Subtracting multiples of the first $r$ rows clears $F^{\mathsf T}$:
$$\operatorname{rref}(R^{\mathsf T})=\begin{bmatrix}I_r&0_{r\times(m-r)}\\0_{(n-r)\times r}&0_{(n-r)\times(m-r)}\end{bmatrix}.$$

(e) By block multiplication $R^{\mathsf T}R=\begin{bmatrix}I&F\\F^{\mathsf T}&F^{\mathsf T}F\end{bmatrix}$ ($n\times n$). Subtracting $F^{\mathsf T}$ times the first block row from the second leaves zeros there, so
$$\operatorname{rref}(R^{\mathsf T}R)=\begin{bmatrix}I_r&F\\0_{(n-r)\times r}&0_{(n-r)\times(n-r)}\end{bmatrix},$$
which is $R$ without its zero rows (padded with $n-r$ zero rows).

**Same nullspace.** Row operations do not change the nullspace, and the nonzero rows of $\operatorname{rref}(R^{\mathsf T}R)$ are the nonzero rows of $R$. So $N(R^{\mathsf T}R)=N(R)$.
:::

::: {.solution for="prob-mit1806s10-3-q8" status="draft"}
1. Row operations give $R$; column exchanges move the pivot columns first, giving $\begin{bmatrix}I&F\\0&0\end{bmatrix}$.

2. Subtracting combinations of the first $r$ columns from the others clears $F$. The result is
   $$\begin{bmatrix}I_r&0_{r\times(n-r)}\\0_{(m-r)\times r}&0_{(m-r)\times(n-r)}\end{bmatrix}:$$
   only the rank survives.
:::
