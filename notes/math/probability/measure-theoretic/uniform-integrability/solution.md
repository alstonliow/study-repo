<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camii-pms-4-q6" status="draft"}
1. On the event $\{|X_1|>\varepsilon\sqrt n\}$ we have $n<X_1^2/\varepsilon^2$. So
$$n\Pr(|X_1|>\varepsilon\sqrt n)\le\varepsilon^{-2}E\big[X_1^2\mathbf 1_{\{|X_1|>\varepsilon\sqrt n\}}\big].$$

2. The integrand tends to $0$ pointwise and is dominated by the integrable $X_1^2$, so the right side tends to $0$ (dominated convergence).

3. By the union bound and identical distribution,
$$\Pr\Big(\max_{k\le n}|X_k|>\varepsilon\sqrt n\Big)\le\sum_{k\le n}\Pr(|X_k|>\varepsilon\sqrt n)=n\Pr(|X_1|>\varepsilon\sqrt n)\to0 .$$
:::

::: {.solution for="prob-camii-pms-6-q1" status="draft"}
1. On $((0,1),\mathcal B,\lambda)$ let $X_1=0$ and $X_n=\frac{n}{\log n}\mathbf 1_{(0,1/n)}$ for $n\ge2$.

2. *Almost sure convergence.* For fixed $\omega$, $X_n(\omega)=0$ as soon as $n\ge1/\omega$.

3. *Uniform integrability.* For $K>0$, $E[X_n\mathbf 1_{\{X_n>K\}}]$ is $0$ if $\frac n{\log n}\le K$ and $\frac1{\log n}$ otherwise. Since $\frac n{\log n}\to\infty$, the $n$ with $\frac n{\log n}>K$ satisfy $n\ge N(K)$ with $N(K)\to\infty$ as $K\to\infty$; so $\sup_nE[X_n\mathbf 1_{\{X_n>K\}}]\le\frac1{\log N(K)}\to0$. By @lem-uniform-integrability-tails the sequence is UI.

4. *Unbounded supremum.* For $\omega\in(\frac1{m+1},\frac1m)$ with $m\ge2$, $X_m(\omega)=\frac m{\log m}$. So
$$E\sup_nX_n\ge\sum_{m\ge2}\frac m{\log m}\Big(\frac1m-\frac1{m+1}\Big)=\sum_{m\ge2}\frac1{(m+1)\log m}=\infty,$$
comparing with $\int\frac{dx}{x\log x}=\log\log x$.
:::

::: {.solution for="prob-camii-pms-6-q2" status="draft"}
1. Let $M_n=n^{-1/2}\max_{k\le n}|X_k|$. By problem 4.6, $M_n\to0$ in probability.

2. $M_n^2\le\frac1n\sum_{k\le n}X_k^2$, so $E[M_n^2]\le E[X_1^2]$: the family $(M_n)$ is bounded in $L^2$, hence uniformly integrable (@prp-uniform-integrability-examples).

3. By @thm-l1-convergence-ui, $E|M_n|\to0$, which is the claim.
:::
