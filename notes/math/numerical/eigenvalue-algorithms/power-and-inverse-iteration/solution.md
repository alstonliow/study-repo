<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-4-q2" status="draft"}
**(a)** Write the start as $x=\sum_kc_kv_k$ with $c_1,c_2\ne0$ (true for a random $x$). After $k$ steps $x$ is proportional to
$$\lambda_1^k\Bigl(c_1v_1+c_2\Bigl(\frac{\lambda_2}{\lambda_1}\Bigr)^kv_2\Bigr)+O(\lvert\lambda_3\rvert^k).$$
The $v_3,v_4,\dots$ components die out, but $\lambda_2/\lambda_1=e^{i\phi}$ has modulus $1$ and $\phi\ne0$ (e.g. $\lambda_2=-\lambda_1$, or a complex pair). So the relative weight of $v_2$ keeps rotating: the iterate wanders around in $\operatorname{span}\{v_1,v_2\}$ (for $\lambda_2=-\lambda_1$ it alternates between two directions) and does not converge, even up to a scalar factor.

**(b)** After many steps the current and previous iterates, $x_k\approx a\,v_1+b\,v_2$ and $x_{k-1}$, are (up to the decaying $O(\lvert\lambda_3/\lambda_1\rvert^k)$ terms) two linearly independent vectors spanning $\operatorname{span}\{v_1,v_2\}$, an invariant subspace of $A$. Apply the Rayleigh–Ritz procedure to it:

1. orthonormalise: $q_1=x_{k-1}/\lVert x_{k-1}\rVert$, $q_2\propto x_k-(q_1^*x_k)q_1$, and $Q=[q_1\ q_2]$;

2. form the $2\times2$ matrix $A_2=Q^*AQ$, which needs $Aq_1$ (a multiple of $x_k$, already known) and $Aq_2$ (one extra product, or the next iterate);

3. compute the eigenvalues $\theta_1,\theta_2$ and eigenvectors $\mathbf{w}_1,\mathbf{w}_2$ of $A_2$; then $\theta_j\to\lambda_j$ and $Q\mathbf{w}_j\to v_j$.

This works because if $AQ=QA_2$ exactly (an invariant subspace), every eigenpair of $A_2$ gives one of $A$: $A(Q\mathbf{w})=QA_2\mathbf{w}=\theta Q\mathbf{w}$. Monitoring the Ritz values between iterations gives a stopping test; the error decreases like $\lvert\lambda_3/\lambda_1\rvert^k$. It is two-dimensional simultaneous iteration (@def-simultaneous-iteration) without re-orthogonalising at every step.
:::
