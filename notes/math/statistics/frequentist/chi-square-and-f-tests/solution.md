<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit1805s22-9-q3" status="draft"}
Use @def-chi-square-variance-test with $H_0:\sigma^2=1$, $H_A:\sigma^2>1$ (right-sided).

1. $n=12$, sample variance $s^2\approx2.340$.

2. Test statistic $X^2=(n-1)s^2/\sigma_0^2\approx11\cdot2.340\approx25.74$, null distribution $\chi^2_{11}$.

3. The critical value at $0.05$ is $19.68$, and the p-value is $P(\chi^2_{11}\ge25.74)\approx0.0071$. Reject $H_0$: the data indicate variance greater than $1$.
:::

::: {.solution for="prob-mit1805s22-9-q4" status="draft"}
Goodness of fit (@def-goodness-of-fit) with $H_0$: the first digits follow Benford's law.

1. There are $100$ entries, so the expected counts are $E_k=100\,p(k)$: $30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6$. (The last few are just under $5$, so the approximation is rough, but the result is far from borderline.)

2. $G=2\sum O_k\ln(O_k/E_k)\approx56.4$ and $X^2=\sum(O_k-E_k)^2/E_k\approx62.7$. No parameters are estimated, so $\mathit{df}=9-1=8$.

3. The critical value of $\chi^2_8$ at $0.001$ is $26.1$; the p-values are about $2\times10^{-9}$ ($G$) and $10^{-10}$ ($X^2$). Reject $H_0$ even at $\alpha=0.001$.

Recommendation: the digits are far too evenly spread for genuine accounting data (only $7$ entries start with $1$, where Benford predicts $30$), so the expense report deserves a closer audit. The test shows that the data do not follow Benford's law, not by itself that they were invented.
:::

::: {.solution for="prob-mit1805s22-9-q5" status="draft"}
(a) `var.test(x, y)` performs the two-sided F test of @def-f-test-variances and reports $F\approx0.970$ on $(19,19)$ degrees of freedom with p-value $\approx0.95$.

(b) The statistic is $F=s_x^2/s_y^2$, which under $H_0$ has the $F(n_x-1,n_y-1)=F(19,19)$ distribution. Here $s_x^2\approx1.130$ and $s_y^2\approx1.165$, so $F\approx0.970<1$, and the p-value is $2P(F(19,19)\le0.970)\approx0.95$. Do not reject $H_0$: the data are entirely consistent with equal variances (as they should be, since both were generated with variance $1$).
:::

::: {.solution for="prob-mit1805s22-9-q6" status="draft"}
(a) Use @def-one-way-anova with $k=4$, $n=351$. The grand mean is $1.375$, so
$$\mathit{MS}_B=\frac{351}3\bigl(0.055^2+0.115^2+0.155^2+0.015^2\bigr)\approx4.739,\qquad\mathit{MS}_W=\frac{0.56+0.80+0.93+0.82}4=0.7775,$$
and $F\approx6.09$ on $(3,1400)$ degrees of freedom. The critical value at $0.01$ is $3.80$ and the p-value is $\approx0.0004$: reject equal means.

(b) Equal group sizes make the pooled variance of @def-two-sample-t-test $s_p^2=\frac{s_1^2+s_2^2}2\cdot\frac2{351}$, with $700$ degrees of freedom; test one-sided (10-day higher).

| 10-day vs | $t$ | one-sided p |
|---|---|---|
| clean | $3.22$ | $0.0007$ |
| 5-day | $3.85$ | $0.00007$ |
| full | $1.98$ | $0.024$ |

At $\alpha=0.01$ the first two reject and the third does not.

No: running several tests each at level $0.01$ gives an overall chance of at least one false rejection larger than $0.01$ (up to about $0.03$ for three tests), so one rejection among three is not a level-$0.01$ test of the null hypothesis of (a). That conclusion has to come from a single test designed for it, such as the ANOVA.
:::
