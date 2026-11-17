<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-11-q4" status="draft"}
(a) Vertex $i$ is isolated when its $n-1$ possible edges are all absent: $E[X_i]=(1-p)^{n-1}$, so $E[X]=n(1-p)^{n-1}$ by linearity (@thm-linearity-of-expectation). $X$ is not binomial because the $X_i$ are not independent: for $n=2$, $X_1=X_2$ always, so $X\in\{0,2\}$, which no binomial distribution with $2$ trials and $0<p<1$ does.

(b) For $i\ne j$, both are isolated when the $2(n-2)+1=2n-3$ edges at $i$ or $j$ are absent: $E[X_iX_j]=(1-p)^{2n-3}$. Since $X_i^2=X_i$,
$$E[X^2]=n(1-p)^{n-1}+n(n-1)(1-p)^{2n-3},$$
and $\mathrm{Var}(X)=n(1-p)^{n-1}+n(n-1)(1-p)^{2n-3}-n^2(1-p)^{2n-2}$.
:::

::: {.solution for="prob-cs70hw-11-q5" status="draft"}
Let $N=\binom n2$. The final edge set is a uniformly random $m$-subset of the $N$ possible edges. For each of the $\binom n3$ triples $T$ let $I_T$ indicate that its $3$ edges are present. The number of $m$-subsets containing $3$ given edges is $\binom{N-3}{m-3}$, so
$$E[I_T]=\frac{\binom{N-3}{m-3}}{\binom Nm}=\frac{m(m-1)(m-2)}{N(N-1)(N-2)},$$
and by linearity the expected number of triangles is $\binom n3\frac{m(m-1)(m-2)}{N(N-1)(N-2)}$ (which is $0$ when $m<3$).
:::
