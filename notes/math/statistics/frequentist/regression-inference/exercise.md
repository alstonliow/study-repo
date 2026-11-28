::: {.problem #prob-camib-sts-3-q9 origin="external" source="camib-sts-3-q9"}
A medical scientist believes that a certain measurement of patient health (e.g. the blood cholesterol level) is influenced by whether a patient has a certain characteristic (e.g. green eyes). The scientist recruits $n$ patients with various combinations of a list of $p$ characteristics. The data $(Y_i)$ are collected, where $Y_i$ is the health measurement of the $i$th patient. The data are modelled as $Y=X\beta+\varepsilon$ where $\varepsilon\sim N_n(0,\sigma^2I)$ for unknown parameters $\beta\in\mathbb R^p$ and $\sigma^2>0$, and where $X$ is the $n\times p$ matrix such that $x_{ij}=1$ if patient $i$ has characteristic $j$, and $x_{ij}=0$ otherwise. Assume that the columns of $X$ are linearly independent.

(a) For a certain characteristic $j$, interpret the hypotheses $H_0:\beta_j=0$ vs $H_1:\beta_j\ne0$. Find the likelihood ratio test of size $\alpha$.

(b) The scientist repeats the test in part (a) for each characteristic $j=1,\dots,p$, and finds that there is one attribute $j^*$ for which the null hypothesis is rejected. To what extent is there evidence that characteristic $j^*$ is associated to the health measurement? Does this depend on the number of characteristics $p$?
:::
