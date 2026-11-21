<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18065ps-18-q10" status="draft"}
1. Block elimination: with $L=\begin{bmatrix}I&0\\C^{\mathsf T}S^{-1}&I\end{bmatrix}$,
$$H=L\begin{bmatrix}S&0\\0&-C^{\mathsf T}S^{-1}C\end{bmatrix}L^{\mathsf T},$$
checked by multiplying out (the lower right block is $C^{\mathsf T}S^{-1}C-C^{\mathsf T}S^{-1}C=0$).

2. $S$ is positive definite. $C^{\mathsf T}S^{-1}C$ is positive definite: $S^{-1}$ is, and $C$ is invertible (as in Problem 12 of Lecture 16). So $-C^{\mathsf T}S^{-1}C$ is negative definite.

3. $H$ is congruent to the block diagonal matrix, which has $n$ positive and $n$ negative eigenvalues. By @thm-sylvester-law-of-inertia congruence keeps these counts, so $H$ has $n$ positive and $n$ negative eigenvalues.
:::
