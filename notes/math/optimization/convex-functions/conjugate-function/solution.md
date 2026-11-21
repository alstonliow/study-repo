<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-2-q5" status="draft"}
We show $f^*(y)=0$ if $y\succeq0$ and $\mathbf 1^Ty=1$, and $f^*(y)=\infty$ otherwise: $f^*$ is the indicator of the probability simplex.

1. If $y$ is in the simplex, then $y^Tx=\sum_iy_ix_i\le\max_ix_i$ for every $x$, so $y^Tx-f(x)\le0$, with equality at $x=0$. Hence $f^*(y)=0$.

2. If some $y_k<0$, take $x=-te_k$ with $t>0$. Then $f(x)=\max\{0,-t\}=0$ when $n\ge2$ (and $f(x)=-t$ when $n=1$), so $y^Tx-f(x)\ge-ty_k=t\lvert y_k\rvert\to\infty$.

3. If $y\succeq0$ but $\mathbf 1^Ty\ne1$, take $x=t\mathbf 1$: $y^Tx-f(x)=t(\mathbf 1^Ty-1)$, which tends to $\infty$ as $t\to\infty$ or $t\to-\infty$, depending on the sign of $\mathbf 1^Ty-1$.
:::
