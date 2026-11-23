<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18335ps-2-q3" status="draft"}
Fix $\mathbf{x}\ne\mathbf{0}$ with $A\mathbf{x}\ne\mathbf{0}$, and measure the input $A$ in the Frobenius norm and the output in the $2$-norm.

1. $g$ is linear in $A$: $g(A+\delta A)-g(A)=\delta A\,\mathbf{x}$, exactly.

2. *Upper bound.* $\lVert\delta A\,\mathbf{x}\rVert_2\le\lVert\delta A\rVert_2\lVert\mathbf{x}\rVert_2\le\lVert\delta A\rVert_F\lVert\mathbf{x}\rVert_2$, since $\lVert\cdot\rVert_2\le\lVert\cdot\rVert_F$ (@thm-matrix-norms-singular-values).

3. *Attained.* For any unit $\mathbf{u}\in\mathbb{C}^m$, the rank-one perturbation $\delta A=\epsilon\,\mathbf{u}\mathbf{x}^{\mathsf H}/\lVert\mathbf{x}\rVert_2$ has $\lVert\delta A\rVert_F=\lVert\delta A\rVert_2=\epsilon$ and $\delta A\,\mathbf{x}=\epsilon\lVert\mathbf{x}\rVert_2\mathbf{u}$, so equality holds in step 2.

4. Hence the absolute condition number is $\lVert\mathbf{x}\rVert_2$, and by @def-relative-condition-number the relative one is
$$\kappa=\frac{\lVert\mathbf{x}\rVert_2\,\lVert A\rVert_F}{\lVert A\mathbf{x}\rVert_2}.$$

With the induced $2$-norm on the inputs instead, the same argument gives $\kappa=\lVert\mathbf{x}\rVert_2\lVert A\rVert_2/\lVert A\mathbf{x}\rVert_2$, the same number as for $\mathbf{x}\mapsto A\mathbf{x}$. In either norm $\kappa\ge1$, and it is large when $A$ nearly annihilates $\mathbf{x}$ (cancellation in the sums forming $A\mathbf{x}$). Unlike the problem $\mathbf{x}\mapsto A\mathbf{x}$, it is not bounded by $\kappa(A)$ for singular or rectangular $A$; for $A=I$ it equals $\sqrt n$ with the Frobenius choice, a harmless factor coming from the norm.
:::
