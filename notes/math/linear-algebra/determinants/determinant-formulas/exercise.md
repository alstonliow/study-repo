::: {.problem #prob-mit1806s10-7-q1 origin="external" source="mit1806s10-7-q1"}
$F_n$ is the determinant of the $1,1,-1$ tridiagonal matrix of order $n$:
$$F_2=\begin{vmatrix}1&-1\\1&1\end{vmatrix}=2\qquad F_3=\begin{vmatrix}1&-1&0\\1&1&-1\\0&1&1\end{vmatrix}=3\qquad F_4=\begin{vmatrix}1&-1&&\\1&1&-1&\\&1&1&-1\\&&1&1\end{vmatrix}\neq4.$$
Expand in cofactors to show that $F_n=F_{n-1}+F_{n-2}$. These determinants are *Fibonacci numbers* $1,2,3,5,8,13,\ldots$. The sequence usually starts $1,1,2,3$ (with two 1's) so our $F_n$ is the usual $F_{n+1}$.
:::

::: {.problem #prob-mit1806s10-7-q2 origin="external" source="mit1806s10-7-q2"}
Cofactors of the $1,3,1$ matrices in Problem 21 give a recursion $S_n=3S_{n-1}-S_{n-2}$. Amazingly that recursion produces every second Fibonacci number. Here is the challenge.

*Show that $S_n$ is the Fibonacci number $F_{2n+2}$ by proving $F_{2n+2}=3F_{2n}-F_{2n-2}$. Keep using Fibonacci's rule $F_k=F_{k-1}+F_{k-2}$ starting with $k=2n+2$.*

*Note (these notes):* The $1,3,1$ matrices have $3$ on the diagonal and $1$ just above and below it; here $F_k$ is the usual Fibonacci sequence $1,1,2,3,5,\dots$
:::

::: {.problem #prob-mit1806s10-7-q3 origin="external" source="mit1806s10-7-q3"}
The symmetric Pascal matrices have determinant 1. If I subtract 1 from the $n,n$ entry, why does the determinant become zero? (Use rule 3 or cofactors.)
$$\det\begin{bmatrix}1&1&1&1\\1&2&3&4\\1&3&6&10\\1&4&10&20\end{bmatrix}=1\ \text{(known)}\qquad\det\begin{bmatrix}1&1&1&1\\1&2&3&4\\1&3&6&10\\1&4&10&\mathbf{19}\end{bmatrix}=\mathbf{0}\ \text{(to explain)}.$$
:::

::: {.problem #prob-mit1806s10-7-q6 origin="external" source="mit1806s10-7-q6"}
Suppose $A$ is a 5 by 5 matrix. Its entries in row 1 multiply determinants (cofactors) in rows 2–5 to give the determinant. Can you guess a "Jacobi formula" for $\det A$ using 2 by 2 determinants from rows 1–2 *times* 3 by 3 determinants from rows 3–5? Test your formula on the $-1,2,-1$ tridiagonal matrix that has determinant 6.
:::

::: {.problem #prob-mit1806s10-7-q7 origin="external" source="mit1806s10-7-q7"}
The 2 by 2 matrix $AB=$ (2 by 3)(3 by 2) has a "Cauchy–Binet formula" for $\det AB$:
$$\det AB=\text{sum of (2 by 2 determinants in }A)\text{ (2 by 2 determinants in }B).$$

(a) Guess which 2 by 2 determinants to use from $A$ and $B$.

(b) Test your formula when the rows of $A$ are $1,2,3$ and $1,4,7$ with $B=A^{\mathsf T}$.
:::

::: {.problem #prob-mit1806s10-7-q13 origin="external" source="mit1806s10-7-q13"}
Challenge problem: in MATLAB (and in GNU Octave), the command A=toepliz(v) produces a symmetric matrix in which each descending diagonal (from left to right) is constant and the first row is $v$. For instance, if v = [0 1 0 0 0 1], then toepliz(v) is the matrix with 1s on both sides of the main diagonal and on the far corners, and 0s elsewhere. More generally, let $v(n)$ be the vector in $\mathbb{R}^n$ with a 1 in the second and last places and 0s elsewhere, and let A(n)=toepliz(v(n)).

(a) Experiment with $n=5,\dots,12$ in MATLAB to see the repeating pattern of $\det A(n)$.

(b) Expand $\det A(n)$ in terms of cofactors of the first row and in terms of cofactors of the first column. Use the known determinant $C_n$ of problem 5.2.13 to recover the pattern found in part (a).

*Note (these notes):* $C_n$ is the determinant of the $n\times n$ matrix with $0$ on the diagonal and $1$ just above and below it: $C_n=0$ for odd $n$ and $C_n=(-1)^{n/2}$ for even $n$, since $C_n=-C_{n-2}$.
:::
