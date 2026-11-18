::: {.problem #prob-cs221hw-1-q2 origin="external" source="cs221hw-1-q2"}
(a) **Gradient Warmup:** Let's practice taking gradients, which is a key operation for being able to optimize continuous functions. Let $\mathbf w, \mathbf c \in \mathbb R^d$. For $f(\mathbf w)=\sum_{i=1}^d (w_i-c_i)^2$, derive $\nabla f(\mathbf w)$. Then evaluate the gradient at $\mathbf w=\mathbf 0$.

*Expected:* A compact vector expression for $\nabla f(\mathbf w)$ and its value at $\mathbf w = \mathbf 0$. Show your work.

(c) **Matrix Multiplication Gradient:** Consider two matrices $A$ (size $m \times n$) and $B$ (size $n \times p$) that are multiplied together to form $C = AB$, and then all entries of $C$ are summed to produce a scalar $s = \sum_{i,j} C_{i,j}$. Let $A = \begin{pmatrix} 2 & 1 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ and $B = \begin{pmatrix} 7 & 8 \\ 9 & 0 \\ 1 & 2 \end{pmatrix}$. Compute $C = AB$ and $s = \sum_{i,j} C_{i,j}$. Then find the gradient $\frac{\partial s}{\partial A_{i,k}}$ for each entry of matrix $A$, and similarly find $\frac{\partial s}{\partial B_{k,j}}$ for each entry of matrix $B$.

*Expected:* The computed matrices $C$ and scalar $s$, plus the gradient matrices $\frac{\partial s}{\partial A}$ and $\frac{\partial s}{\partial B}$ with numerical values for each entry. Show your work, including how you derived the gradients.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
