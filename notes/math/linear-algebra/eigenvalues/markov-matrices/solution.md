<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1806s10-1-q6" status="draft"}
1. Iterating (for example with a short loop $\mathbf{u}\leftarrow A\mathbf{u}$) gives, to four decimals,
   $$\mathbf{u}_7\approx(0.6031,\ 0.3969),\qquad \mathbf{v}_7\approx(0.5953,\ 0.4047).$$
   Both are close to the same vector, from opposite sides.

2. Guess $\mathbf{s}=(.6,.4)$. Check: $A\mathbf{s}=(.8\cdot.6+.3\cdot.4,\ .2\cdot.6+.7\cdot.4)=(.6,.4)=\mathbf{s}$.

3. Why: $\mathbf{s}$ is the eigenvector for $\lambda=1$; the other eigenvalue is $\operatorname{tr}A-1=0.5$ with eigenvector $(1,-1)$. Since $\mathbf{u}_0=\mathbf{s}+0.4(1,-1)$ and $\mathbf{v}_0=\mathbf{s}-0.6(1,-1)$, we get $\mathbf{u}_k=\mathbf{s}+0.4(0.5)^k(1,-1)$ and $\mathbf{v}_k=\mathbf{s}-0.6(0.5)^k(1,-1)$, which approach $\mathbf{s}$ (@cor-markov-steady-state).
:::

::: {.solution for="prob-mit1806s10-7-q11" status="draft"}
1. The columns add to $1$, so $\lambda_1=1$; the trace $0.7$ gives $\lambda_2=-0.3$. Eigenvectors: $(9,4)$ for $1$ (from $-0.4x+0.9y=0$) and $(-1,1)$ for $-0.3$.
   $$\Lambda=\begin{bmatrix}1&0\\0&-0.3\end{bmatrix},\qquad S=\begin{bmatrix}9&-1\\4&1\end{bmatrix}.$$

2. $\Lambda^k\to\begin{bmatrix}1&0\\0&0\end{bmatrix}$ since $(-0.3)^k\to0$.

3. With $S^{-1}=\frac1{13}\begin{bmatrix}1&1\\-4&9\end{bmatrix}$,
   $$S\Lambda^kS^{-1}\to\begin{bmatrix}9\\4\end{bmatrix}\frac1{13}\begin{bmatrix}1&1\end{bmatrix}=\frac1{13}\begin{bmatrix}9&9\\4&4\end{bmatrix}.$$
   Both columns are the *steady state* $(\frac9{13},\frac4{13})$ (@cor-markov-steady-state).
:::

::: {.solution for="prob-mit1806s10-8-q11" status="draft"}
1. $A$ is Markov when its entries are $\ge0$ and $\mathbf{1}^{\mathsf T}A=\mathbf{1}^{\mathsf T}$, where $\mathbf{1}=(1,\dots,1)$ (the columns add to $1$).

2. The entries of $A^2$ are sums of products of nonnegative numbers, so they are $\ge0$.

3. $\mathbf{1}^{\mathsf T}A^2=(\mathbf{1}^{\mathsf T}A)A=\mathbf{1}^{\mathsf T}A=\mathbf{1}^{\mathsf T}$.
:::

::: {.solution for="prob-mit1806s10-8-q12" status="draft"}
1. The columns of $B$ add to $0$, so the rows add to the zero row and $B$ is singular: $\lambda_1=0$. (Equivalently, $A$ is Markov and has $\lambda=1$, and $B=A-I$ shifts it to $0$.) The trace gives $\lambda_2=-0.5$.

2. Eigenvectors: $\mathbf{x}_1=(3,2)$ for $0$ (from $-0.2x+0.3y=0$) and $\mathbf{x}_2=(1,-1)$ for $-0.5$.

3. $\mathbf{u}(t)=c_1\mathbf{x}_1+c_2e^{-t/2}\mathbf{x}_2\to c_1\mathbf{x}_1$: the steady state is a multiple of $(3,2)$, fixed by the total $u_1+u_2$, which never changes (the columns of $B$ add to zero).
:::

::: {.solution for="prob-mit1806s10-8-q13" status="draft"}
1. $A$ is Markov, so $1$ is an eigenvalue; $\det A=0$ gives $0$; the trace $1.2$ gives the third: $0.2$.

2. Eigenvectors: $(3,3,4)$ for $\lambda=1$, $(1,-1,0)$ for $0.2$, $(1,1,-2)$ for $0$.

3. $\mathbf{u}_0=(1,0,0)=\frac1{10}(3,3,4)+\frac12(1,-1,0)+\frac1{20}(1,1,-2)$. The other terms are multiplied by $0.2^k$ and $0^k$, so $A^k\mathbf{u}_0\to(0.3,0.3,0.4)$.

4. By linearity, $(100,0,0)$ leads to $(30,30,40)$: the total $100$ is preserved and distributed as in the steady state.
:::
