::: {.problem #prob-mit18335ps-3-q1 origin="external" source="mit18335ps-3-q1"}
**QR and orthogonal bases**

(a) Trefethen, problem 10.4.

(b) Prove that $A=QR$ and $B=RQ$ have the same eigenvalues, assuming $A$ is a square matrix. Then do a little experiment: Construct a random $5\times5$ real-symmetric matrix in Julia via `X=rand(5,5); A = X' + X`. Use `QR = qr(A)` (do `using LinearAlgebra` first) to compute the QR factorization of $A$, and then compute `B = QR.R * QR.Q`. Then find the QR factorization $B=Q'R'$, and compute $R'Q'$ ...repeat this process until the matrix converges (maybe writing a loop and/or a function). From what it converges to, suggest a procedure to compute the eigenvalues and eigenvectors of a real-symmetric matrix (no need to prove that it converges in general—we will discuss this in class).

(c) Trefethen, problem 28.2,
:::
