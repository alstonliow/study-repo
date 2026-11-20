---
title: "Chi-Square and F Tests"
sources: [mit1805-19]
requires: [math/statistics/frequentist/t-tests]
status: draft
---

<!-- Added 2026-11-20 from MIT 18.05 (Spring 2022), Class 19, in our own wording; proofs written out in steps. -->

The tests in this note compare variances, or compare observed counts with the counts a hypothesis predicts. Their null distributions are chi-square (@def-chi-square-distribution) or ratios of chi-squares.

::: {#def-chi-square-variance-test .definition name="Chi-square test for a variance"}

For independent $N(\mu,\sigma^2)$ data with $H_0:\sigma^2=\sigma_0^2$, the statistic
$$X^2=\frac{(n-1)s^2}{\sigma_0^2}$$
has null distribution $\chi^2_{n-1}$ by @thm-normal-sample-theory. Since $\chi^2_{n-1}$ is not symmetric, a two-sided test uses both tails separately.

:::

::: {#exm-chi-square-variance-test .example name="Is the spread too large?"}

For the data of @exm-one-sample-t-test ($n=5$, $s^2=0.185$) and $H_0:\sigma^2=0.1$, $X^2=4\cdot0.185/0.1=7.4$. Under $\chi^2_4$ this is not extreme: the two-sided p-value is about $0.23$.

:::

::: {#def-goodness-of-fit .definition name="Chi-square test for goodness of fit"}

Data fall into $k$ categories with observed counts $O_1,\dots,O_k$. A null hypothesis gives the category probabilities, possibly after estimating $r$ parameters from the data, and hence expected counts $E_1,\dots,E_k$. The statistics
$$G=2\sum_{i=1}^kO_i\ln\frac{O_i}{E_i},\qquad X^2=\sum_{i=1}^k\frac{(O_i-E_i)^2}{E_i}$$
both have approximately the null distribution $\chi^2_{\mathit{df}}$ with
$$\mathit{df}=k-1-r$$
degrees of freedom, when the expected counts are not small (a common rule: all $E_i\ge5$). Large values reject $H_0$.

:::

The degrees of freedom count the cell counts that can vary freely: the $k$ counts must add up to the total, and each estimated parameter imposes one further constraint.

::: {#exm-goodness-of-fit-die .example name="Is the die fair?"}

A die rolled $60$ times shows the faces $1,\dots,6$ with counts $5,8,9,8,10,20$. Under $H_0$ (fair die) every $E_i=10$, so
$$X^2=\frac{25+4+1+4+0+100}{10}=13.4,\qquad G\approx11.76 .$$
With $\mathit{df}=5$ the critical value at level $0.05$ is $11.07$; both statistics reject (p-values $0.020$ and $0.038$).

:::

::: {#rmk-homogeneity-test .remark name="Test for homogeneity"}

To test whether several populations share the same category probabilities, put the counts in a table with one row per population and one column per category. Under $H_0$ the expected count in a cell is (row total)(column total)/(grand total), and $X^2$ or $G$ over all cells is approximately $\chi^2$ with $(\text{rows}-1)(\text{columns}-1)$ degrees of freedom.

:::

::: {#def-f-distribution .definition name="F distribution"}

If $U\sim\chi^2_a$ and $V\sim\chi^2_b$ are independent, the distribution of $\dfrac{U/a}{V/b}$ is the *F distribution* $F(a,b)$.

:::

::: {#def-f-test-variances .definition name="F test for equal variances"}

For independent samples $x_1,\dots,x_n\sim N(\mu_x,\sigma_x^2)$ and $y_1,\dots,y_m\sim N(\mu_y,\sigma_y^2)$ with $H_0:\sigma_x=\sigma_y$, the statistic $s_x^2/s_y^2$ has null distribution $F(n-1,m-1)$: by @thm-normal-sample-theory it is the ratio of $\chi^2_{n-1}/(n-1)$ and $\chi^2_{m-1}/(m-1)$, and $\sigma^2$ cancels.

:::

::: {#def-one-way-anova .definition name="One-way ANOVA"}

Let there be $k$ groups of $n$ observations each, group $i$ being $N(\mu_i,\sigma^2)$ with a common $\sigma$, all independent; $H_0$: all $\mu_i$ are equal. With group means $\bar y_i$, grand mean $\bar y$ and group sample variances $s_i^2$, put
$$\mathit{MS}_B=\frac n{k-1}\sum_{i=1}^k(\bar y_i-\bar y)^2,\qquad\mathit{MS}_W=\frac1k\sum_{i=1}^ks_i^2 .$$
The statistic $F=\mathit{MS}_B/\mathit{MS}_W$ has null distribution $F(k-1,\,k(n-1))$. Large values reject $H_0$.

:::

Both mean squares estimate $\sigma^2$ when $H_0$ holds: $\mathit{MS}_W$ from the spread inside the groups, $\mathit{MS}_B$ from the spread of the group means, each of which has variance $\sigma^2/n$. Different true means inflate only $\mathit{MS}_B$.

::: {#exm-one-way-anova .example name="Three groups"}

Groups $5,7,6$; $8,9,10$; $6,8,7$ have means $6,9,7$, grand mean $\frac{22}3$, and every $s_i^2=1$. So $\mathit{MS}_W=1$ and $\mathit{MS}_B=\frac32\bigl((\tfrac43)^2+(\tfrac53)^2+(\tfrac13)^2\bigr)=7$, giving $F=7$. The critical value of $F(2,6)$ at level $0.05$ is $5.14$, so $H_0$ is rejected (p $\approx0.027$).

:::
