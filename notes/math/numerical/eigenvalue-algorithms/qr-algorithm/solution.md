<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-3-q1" status="draft"}
**(b)** *Same eigenvalues.* $Q$ is unitary (orthogonal), so $R=Q^{\mathsf H}A$ and $B=RQ=Q^{\mathsf H}AQ=Q^{-1}AQ$. Similar matrices have the same characteristic polynomial (@thm-similar-same-eigenvalues), hence the same eigenvalues. (This needs no invertibility of $A$: the QR factorization with unitary $Q$ exists for every square $A$, @thm-full-qr-existence.)

*Experiment* (run in Python with numpy instead of Julia; $X$ with uniform random entries, $A=X^{\mathsf T}+X$). After $300$ repetitions of "factor, multiply in reverse order" the matrix is diagonal to about $10^{-6}$, with diagonal
$$4.8009,\ -1.5445,\ 0.4250,\ -0.4087,\ -0.0889,$$
which are the eigenvalues of $A$, ordered by decreasing absolute value. The slowest entry to vanish sits between $0.4250$ and $-0.4087$, whose ratio $0.96$ is close to $1$.

*Procedure.* Iterate $A_{k}=R_kQ_k$ where $A_{k-1}=Q_kR_k$, starting with $A_0=A$, until the off-diagonal entries are negligible; the diagonal holds the eigenvalues. Since $A_k=(Q_1\cdots Q_k)^{\mathsf T}A\,(Q_1\cdots Q_k)$, the accumulated orthogonal matrix $Q_1Q_2\cdots Q_k$ has the eigenvectors as its columns: in the experiment $\lVert AV-V\Lambda\rVert_{\max}\approx10^{-6}$ for $V=Q_1\cdots Q_{300}$. This is the unshifted QR algorithm (@def-qr-algorithm); in practice one first reduces $A$ to tridiagonal form and uses shifts (@def-shifted-qr-algorithm).

*Note (these notes):* parts (a) and (c) refer to textbook exercises whose statements are not reproduced here and are left unsolved.
:::
