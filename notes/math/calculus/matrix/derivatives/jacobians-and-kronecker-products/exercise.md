::: {.problem #prob-mit18s096ps-1-q3 origin="external" source="mit18s096ps-1-q3"}
(a) Argue briefly that linear functions that map $n \times n$ matrices to $n \times n$ matrices themselves form a vector space $V$. What is the dimension of this vector space?

(b) Argue briefly that linear functions of $n \times n$ matrices of the form $X \rightarrow AX$, where $A$ is $n \times n$, form a vector space. What is the dimension of this vector space?

(c) Argue briefly why it follows that there must be infinitely many linear functions $\in V$ that are not of the form $X \rightarrow AX$.
:::

::: {.problem #prob-mit18s096ps-2-q4 origin="external" source="mit18s096ps-2-q4"}
The Jacobian determinant (sometimes called simply "the Jacobian," clashing with the concept of the Jacobian matrix) is the determinant of the Jacobian matrix. Specifically if $f(x)$ is a function from $\mathbb{R}^n$ to $\mathbb{R}^n$ and $(\frac{\partial f_i}{\partial x_j})_{1 \le i,j \le n}$ is the Jacobian matrix $f'(x)$, then its determinant $\det f'(x)$ is the Jacobian determinant. Sometimes we take the absoute value and not worry too much about the sign.

(a) The Jacobian determinant represents the local scaling of volume. Compute the Jacobian determinant of the hyperbolic rotation defined in Pset 1, problem 1b, in simplest form. Use this to describe how a little square around a point generally transforms with a hyperbolic rotation.

(b) There are many ways to equivalently take a scalar function $f(\alpha)$ and extend it to a matrix function $F(M)$, which takes in a square matrix and returns a square matrix of the same size.

The simplest is to define $f(M)=X f(\Lambda) X^{-1},$ where $M=X\Lambda X^{-1}$ is an eigen-decomposition of $M$ (and use continuity to include non-diagonalizable matrices). Here, $f(\Lambda)$ denotes the application of a scalar function $f(\lambda)$ to the eigenvalues $\lambda$ (on the diagonal of $\Lambda$). (e.g., you've probably seen $e^M$ defined in terms of $e^\lambda$.)

One could then write $f'(M)$ as an explicit $n^2\times n^2$ Jacobian matrix (e.g. via $\operatorname{vec}(dM)$ and Kronecker products), and could then compute its determinant.

  (i) Write a computer program (in any language) to find the $9\times 9$ Jacobian matrix of $f(M)$ and then the Jacobian determinant by either finite differences or by using automatic differentiation, for $f(\lambda)$ being $e^\lambda$, $\lambda^2$, and $\sin(\lambda)$ on the $3\times 3$ matrix $M = [0\: 1\: 4;1\: 0\: 1;4\: 1\: 0]$ with entries $M_{i,j} = (i-j)^2$.

  (ii) Compare with the following known theoretical formula for the Jacobian determinant for a scalar function $f(\lambda)$ applied to a diagonalizable matrix $M$, in terms of $M$'s eigenvalues $\lambda$:
$$
\frac{\prod_{i < j} |f(\lambda_i)-
f(\lambda_j)|^2}{\prod_{i < j} |\lambda_i-\lambda_j|^2}
\prod_i f'(\lambda_i)
$$

*Note (these notes):* The hyperbolic rotation is Problem 0(b) of Pset 1 (@prob-mit18s096ps-1-q0).
:::
