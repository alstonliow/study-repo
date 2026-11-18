::: {.problem #prob-mit1806s10-5-q1 origin="external" source="mit1806s10-5-q1"}
Every system with no solution is like the one in problem 6. There are numbers $y_1,\dots,y_m$ that multiply the $m$ equations so they add up to $0=1$. This is called Fredholm's Alternative:

Exactly one of these problems has a solution: $A\mathbf{x}=\mathbf{b}$ OR $A^{\mathsf T}\mathbf{y}=\mathbf{0}$ with $\mathbf{y}^{\mathsf T}\mathbf{b}=1$.

If $\mathbf{b}$ is not in the column space of $A$ it is not orthogonal to the nullspace of $A^{\mathsf T}$. Multiply the equations $x_1-x_2=1$ and $x_2-x_3=1$ and $x_1-x_3=1$ by numbers $y_1,y_2,y_3$ chosen so that the equations add up to $0=1$.
:::

::: {.problem #prob-mit1806s10-5-q2 origin="external" source="mit1806s10-5-q2"}
If $A^{\mathsf T}A\mathbf{x}=\mathbf{0}$ then $A\mathbf{x}=\mathbf{0}$. Reason: $A\mathbf{x}$ is inthe nullspace of $A^{\mathsf T}$ and also in the \_\_\_\_\_ of $A$ and those spaces are \_\_\_\_\_. Conclusion: $A^{\mathsf T}A$ has the same nullspace as $A$. This key fact is repeated in the next section.
:::

::: {.problem #prob-mit1806s10-5-q3 origin="external" source="mit1806s10-5-q3"}
The command N=null(A) will produce a basis for the nullspace of $A$. Then the command B=null(N') will produce a basis for the \_\_\_\_\_ of $A$.
:::

::: {.problem #prob-mit1806s10-5-q4 origin="external" source="mit1806s10-5-q4"}
Suppose I give you four nonzero vectors $\mathbf{r},\mathbf{n},\mathbf{c},\mathbf{l}$ in $\mathbb{R}^2$.

a. What are the conditions for those to be bases for the four fundamental subspaces $C(A^{\mathsf T}),N(A),C(A),N(A^{\mathsf T})$ of a $2\times2$ matrix?

b. What is one possible matrix $A$?
:::

::: {.problem #prob-mit1806s10-5-q5 origin="external" source="mit1806s10-5-q5"}
Suppose I give you four nonzero vectors $\mathbf{r}_1,\mathbf{r}_2,\mathbf{n}_1,\mathbf{n}_2,\mathbf{c}_1,\mathbf{c}_2,\mathbf{l}_1,\mathbf{l}_2$ in $\mathbb{R}^2$.

a. What are the conditions for those to be bases for the four fundamental subspaces $C(A^{\mathsf T}),N(A),C(A),N(A^{\mathsf T})$ of a $2\times2$ matrix?

b. What is one possible matrix $A$?

*Note (these notes):* As printed the vectors are in $\mathbb{R}^2$ and the matrix is $2\times2$, which cannot work; the intended setting is presumably $\mathbb{R}^4$ and a $4\times4$ matrix of rank $2$.
:::

::: {.problem #prob-mit1806s10-5-q11 origin="external" source="mit1806s10-5-q11"}
If $A$ has $r$ independent columns and $B$ has $r$ independent rows, $AB$ is invertible.

Proof: When $A$ is $m$ by $r$ with independent columns, we know that $A^{\mathsf T}A$ is invertible. If $B$ is $r$ by $n$ with independent rows, show that $BB^{\mathsf T}$ is invertible. (Take $A=B^{\mathsf T}$.)

Now show that $AB$ has rank $r$.

*Note (these notes):* As printed, $AB$ is $m$ by $n$ and need not be square; what the argument shows is that $AB$ has rank $r$.
:::
