<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit1801f06-2a-q6" status="draft"}
Let $y=u_1u_2\cdots u_n$ and suppose first all $u_i>0$. Then $\ln y=\ln u_1+\dots+\ln u_n$, and differentiating (@prp-logarithmic-differentiation)
$$\frac{y'}{y}=\frac{u_1'}{u_1}+\dots+\frac{u_n'}{u_n}.$$
Multiplying by $y$, the $i$-th term becomes $u_1\cdots u_{i-1}u_i'u_{i+1}\cdots u_n$, which is the formula of @prob-mit1801f06-1-q7. If some $u_i$ are negative, apply the argument to $\lvert y\rvert=\lvert u_1\rvert\cdots\lvert u_n\rvert$, using $(\ln\lvert u\rvert)'=u'/u$; at points where some $u_i=0$ the formula still holds by continuity of both sides, or by the inductive proof.
:::
