::: {.problem #prob-camib-sts-3-q9 origin="external" source="camib-sts-3-q9"}
A medical scientist believes that a certain measurement of patient health (e.g. the blood cholesterol level) is influenced by whether a patient has a certain characteristic (e.g. green eyes). The scientist recruits $n$ patients with various combinations of a list of $p$ characteristics. The data $(Y_i)$ are collected, where $Y_i$ is the health measurement of the $i$th patient. The data are modelled as $Y=X\beta+\varepsilon$ where $\varepsilon\sim N_n(0,\sigma^2I)$ for unknown parameters $\beta\in\mathbb R^p$ and $\sigma^2>0$, and where $X$ is the $n\times p$ matrix such that $x_{ij}=1$ if patient $i$ has characteristic $j$, and $x_{ij}=0$ otherwise. Assume that the columns of $X$ are linearly independent.

(a) For a certain characteristic $j$, interpret the hypotheses $H_0:\beta_j=0$ vs $H_1:\beta_j\ne0$. Find the likelihood ratio test of size $\alpha$.

(b) The scientist repeats the test in part (a) for each characteristic $j=1,\dots,p$, and finds that there is one attribute $j^*$ for which the null hypothesis is rejected. To what extent is there evidence that characteristic $j^*$ is associated to the health measurement? Does this depend on the number of characteristics $p$?
:::

::: {.problem #prob-camii-sms-1-q3 origin="external" source="camii-sms-1-q3"}
Show that the maximum likelihood estimator of $\sigma^2$ in the normal linear model is $\hat\sigma^2_{\mathrm{MLE}}=\|(I-P)Y\|^2/n$. Find the distribution of $\hat\sigma^2_{\mathrm{MLE}}$ and conclude that $\hat\sigma^2_{\mathrm{MLE}}$ is a biased estimator of $\sigma^2$ but $\hat\sigma^2$ is unbiased. Is $\hat\sigma^2$ still unbiased when $\varepsilon$ is not normally distributed (but has the same mean and variance given $X$)? Finish this question by constructing a confidence interval of $\sigma^2$ with level $1-\alpha$ in the normal model.

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::

::: {.problem #prob-camii-sms-1-q9 origin="external" source="camii-sms-1-q9"}
Suppose we observe data $(X,Y)$ generated from a normal linear model. Let $x^*\in\mathbb R^p$ be a fixed vector and $\epsilon^*\sim N(0,\sigma^2)$ be independent of $(X,Y)$. Denote $Y^*=(x^*)^{\mathsf T}\beta+\epsilon^*$. Construct $(1-\alpha)$-confidence intervals for $(x^*)^{\mathsf T}\beta$ and $Y^*$. Which interval is shorter in length? Can you give an intuitive explanation to your answer?

*Note (these notes):* Sheet notation: $X$ is an $n\times p$ design matrix of full column rank, $P$ the orthogonal projection onto its column space, $X_0$ the first $p_0<p$ columns of $X$ and $P_0$ the orthogonal projection onto the column space of $X_0$; $Y\in\mathbb R^n$, $\hat\beta=(X^{\mathsf T}X)^{-1}X^{\mathsf T}Y$, $\hat\beta_0=(X_0^{\mathsf T}X_0)^{-1}X_0^{\mathsf T}Y$, $\hat\sigma^2=\|(I-P)Y\|^2/(n-p)$. The normal linear model is $Y=X\beta+\varepsilon$, $\varepsilon\mid X\sim N_n(0,\sigma^2I)$.
:::
