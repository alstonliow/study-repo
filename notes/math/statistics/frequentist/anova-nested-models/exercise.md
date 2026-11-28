::: {.problem #prob-camib-sts-3-q7 origin="external" source="camib-sts-3-q7"}
Consider the one-way analysis of variance (ANOVA) model
$$Y_{ij}=\mu_i+\varepsilon_{ij},\qquad i=1,\dots,I,\ j=1,\dots,n_i,$$
where $(\varepsilon_{ij})\overset{\text{iid}}{\sim}N(0,\sigma^2)$. Derive from first principles explicit expressions for the MLEs $\hat\mu_1,\dots,\hat\mu_I$ and $\hat\sigma^2$. Show that we can obtain the same expressions if we regard the ANOVA model as a special case of the general linear regression model $Y=X\beta+\varepsilon$ and specialise the formulae $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$ and $\hat\sigma^2=n^{-1}\|Y-X\hat\beta\|^2$.
:::

::: {.problem #prob-camib-sts-3-q10 origin="external" source="camib-sts-3-q10"}
Consider the one-way ANOVA model of Question 7. Letting $\bar Y_i=n_i^{-1}\sum_{j=1}^{n_i}Y_{ij}$ and $\bar Y=n^{-1}\sum_{i=1}^I\sum_{j=1}^{n_i}Y_{ij}$ with $n=n_1+\dots+n_I$, show from first principles that the size $\alpha$ likelihood ratio test of equality of means rejects $H_0$ if
$$\frac{\frac1{I-1}\sum_{i=1}^In_i(\bar Y_i-\bar Y)^2}{\frac1{n-I}\sum_{i=1}^I\sum_{j=1}^{n_i}(Y_{ij}-\bar Y_i)^2}>k$$
where $F(k)=1-\alpha$ and $F$ is the distribution function of the $F_{I-1,n-I}$ distribution; i.e. if 'the ratio of the between groups sum of squares to the within groups sum of squares is large'.
:::
