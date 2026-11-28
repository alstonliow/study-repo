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

::: {.solution for="prob-mit6042f10-12-q2" status="draft"}
(a) A proposition is false only if all three of its terms are false; its three variables are different, so this has probability $\frac18$. With indicators $I_j$ for "proposition $j$ is true", $E[\sum_jI_j]=7\cdot\frac78=\frac{49}8$ by linearity (@thm-linearity-of-expectation).

(b) The number of true propositions is an integer. If every assignment made at most $6$ propositions true, the expectation would be at most $6<\frac{49}8$. So some assignment makes all $7$ true. (This is the probabilistic method: a random variable takes some value at least its mean.)
:::

::: {.solution for="prob-eecs126hw-2-q2" status="draft"}
The answer is $np$.

1. By linearity, the expected number lit is $\sum_{i=1}^n\Pr(X_i\ge i)$, where $X_i\sim\operatorname{Bin}(n,p)$ is the number of switches on in row $i$.
2. All rows have the same distribution, so this equals $\sum_{i=1}^{n}\Pr(X\ge i)$ for one $X\sim\operatorname{Bin}(n,p)$.
3. For a variable with values in $\{0,\dots,n\}$, $X=\sum_{i=1}^n\mathbf 1\{X\ge i\}$, so the sum is $E[X]=np$.
:::

::: {.solution for="prob-mit1805s22-2-q5" status="draft"}
Assume $n\ge3$.

1. Let $X_i$ be the indicator that the person in seat $i$ is shorter than both neighbours; the required number is $X=\sum_iX_i$.

2. The three people in seats $i-1,i,i+1$ are a uniformly random ordered triple of distinct heights, so each of the three is equally likely to be the shortest: $E[X_i]=\frac13$.

3. By linearity of expectation, $E[X]=n/3$.

(For $n=2$ both neighbours of each person are the other person, and exactly one person is shorter, so the answer is $1$.)
:::
