::: {.problem #prob-mit1806s10-8-q6 origin="external" source="mit1806s10-8-q6"}
(a) Find a symmetric matrix $\begin{bmatrix}1&b\\b&1\end{bmatrix}$ that has a negative eigenvalue.

(b) How do you know it must have a negative pivot?

(c) How do you know it can't have two negative eigenvalues?
:::

::: {.problem #prob-mit1806s10-8-q7 origin="external" source="mit1806s10-8-q7"}
Here is a quick "proof" that the eigenvalues of all real matrices are real:
$$\textbf{False proof}\qquad A\mathbf{x}=\lambda\mathbf{x}\text{ gives }\mathbf{x}^{\mathsf T}A\mathbf{x}=\lambda\mathbf{x}^{\mathsf T}\mathbf{x}\text{ so }\lambda=\frac{\mathbf{x}^{\mathsf T}A\mathbf{x}}{\mathbf{x}^{\mathsf T}\mathbf{x}}\text{ is real.}$$
Find the flaw in this reasoning—a hidden assumption that is not justified. You could test those steps on the 90-degree rotation matrix $[0,-1;\ 1,0]$ with $\lambda=i$ and $\mathbf{x}=(i,1)$.
:::

::: {.problem #prob-mit1806s10-8-q8 origin="external" source="mit1806s10-8-q8"}
Which of these classes of matrices do $A$ and $B$ belong to: Invertible, orthogonal, projection, permutation, diagonalizable, Markov?
$$A=\begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix}\qquad B=\frac13\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}.$$
Which of these factorizations are possible for $A$ and $B$: $LU$, $QR$, $S\Lambda S^{-1}$, $Q\Lambda Q^{\mathsf T}$?
:::

::: {.problem #prob-mit1806s10-8-q10 origin="external" source="mit1806s10-8-q10"}
If $\lambda_{\max}$ is the largest eigenvalue of a symmetric matrix $A$, no diagonal entry can be larger tha $\lambda_{\max}$. What is the first entry $a_{11}$ of $A=Q\Lambda Q^{\mathsf T}$? Show why $a_{11}\le\lambda_{\max}$.
:::

::: {.problem #prob-mit1806s10-9-q7 origin="external" source="mit1806s10-9-q7"}
Write down the 5 by 5 sine matrix $S$ from Worked Example 6.5 D, containing the eigenvectors of $K$ when $n=5$ and $h=1/6$. Multiply $K$ times $S$ to see the five positive eigenvalues.

Their sum should equal the trace 10. Their product should be $\det K=6$.

*Note (these notes):* $K$ is the $5\times5$ matrix with $2$ on the diagonal and $-1$ just above and below it; the sine matrix has entries $S_{jk}=\sin(jk\pi h)=\sin(jk\pi/6)$.
:::
