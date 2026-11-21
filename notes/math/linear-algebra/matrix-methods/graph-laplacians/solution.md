<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-35-q1" status="draft"}
1. Triangle (each node has degree $2$, every pair joined):
$$L=\begin{bmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{bmatrix},\quad\text{eigenvalues }0,3,3 .$$

2. Square (cycle $1-2-3-4-1$):
$$L=\begin{bmatrix}2&-1&0&-1\\-1&2&-1&0\\0&-1&2&-1\\-1&0&-1&2\end{bmatrix},\quad\text{eigenvalues }0,2,2,4 .$$

3. Both have one zero eigenvalue with eigenvector $\mathbf{1}$, since both graphs are connected (@thm-laplacian-components). The square's Laplacian is a circulant, so its eigenvalues are $2-w^k-w^{-k}=2-2\cos(k\pi/2)$.
:::
