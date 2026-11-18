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
