<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit18s096ps-2-q3" status="draft"}
(a) 1. From $Sq=\lambda q$ and $q^{\mathsf T}q=1$, $\lambda=q^{\mathsf T}Sq$.

2. Differentiate: $d\lambda=dq^{\mathsf T}Sq+q^{\mathsf T}dS\,q+q^{\mathsf T}S\,dq$.

3. Since $S$ is symmetric, $q^{\mathsf T}S=\lambda q^{\mathsf T}$ and $dq^{\mathsf T}Sq=\lambda\,dq^{\mathsf T}q=\lambda\,q^{\mathsf T}dq$. So the outer terms sum to $2\lambda\,q^{\mathsf T}dq$.

4. Differentiating $q^{\mathsf T}q=1$ gives $2q^{\mathsf T}dq=0$, so those terms vanish and $d\lambda=q^{\mathsf T}dS\,q$. (Simplicity of $\lambda$ is what makes $\lambda$ and a normalized $q$ differentiable functions of $S$ in the first place.)

(b) $q^{\mathsf T}dS\,q=\operatorname{tr}(q^{\mathsf T}dS\,q)=\operatorname{tr}(qq^{\mathsf T}dS)$, and $qq^{\mathsf T}$ is symmetric, so $\nabla\lambda=qq^{\mathsf T}$. This is the diagonal case of @thm-symmetric-eigendecomposition-differential.
:::
