<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-12-q1" status="draft"}
Write $X=\sum_iX_i$ with $X_i$ the indicator that $i$ is isolated, and $q=1-p$. Then $\mathrm{Var}(X_i)=q^{n-1}(1-q^{n-1})$, and for $i\ne j$, $\mathrm{Cov}(X_i,X_j)=E[X_iX_j]-E[X_i]E[X_j]=q^{2n-3}-q^{2n-2}$ (both are isolated when the $2n-3$ edges at $i$ or $j$ are absent). By @prp-covariance-properties,
$$\mathrm{Var}(X)=nq^{n-1}(1-q^{n-1})+n(n-1)\bigl(q^{2n-3}-q^{2n-2}\bigr).$$
This agrees with HW 11 Q4(b).
:::

::: {.solution for="prob-cs70hw-12-q2" status="draft"}
Take $c=0$, $d=1$ (so $\tilde Y=Y$), $a=1$ and $b=-\frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}(Y)}$. Then $ad-bc=1\ne0$, and by bilinearity (@prp-covariance-properties)
$$\mathrm{Cov}(\tilde X,Y)=\mathrm{Cov}(X,Y)+b\,\mathrm{Var}(Y)=0.$$
:::
