<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6041f10-6-q5" status="draft"}
$N$ is geometric with success probability $1-p$, so $E[N]=\frac1{1-p}$ and $\mathrm{Var}(N)=\frac p{(1-p)^2}$.

(a) The number attending is $K=B_1+\dots+B_N$ with $B_i$ independent Bernoulli($q$). By @thm-random-sum,
$$E[K]=\frac q{1-p},\qquad\mathrm{Var}(K)=\frac{q(1-q)}{1-p}+\frac{q^2p}{(1-p)^2}.$$

(b) The total is $T=M_1+\dots+M_K$ with $M_i\sim\operatorname{Exp}(\lambda)$, mean $\frac1\lambda$ and variance $\frac1{\lambda^2}$, independent of $K$. Again by @thm-random-sum,
$$E[T]=\frac{q}{\lambda(1-p)},\qquad\mathrm{Var}(T)=\frac{E[K]+\mathrm{Var}(K)}{\lambda^2}=\frac1{\lambda^2}\Bigl(\frac{q(2-q)}{1-p}+\frac{q^2p}{(1-p)^2}\Bigr).$$
:::
