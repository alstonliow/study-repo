<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-6-q1" status="draft"}
Write $R,S,W$ for Rain, Sprinkler, WetGrass.

**(a)** $\text{Rain}\rightarrow\text{WetGrass}$ and $\text{Sprinkler}\rightarrow\text{WetGrass}$. There is no edge between Rain and Sprinkler, since they are independent.

**(b)** Each variable is conditioned on its parents:
$$\mathbb P(R=r,S=s,W=w)=p(r)\,p(s)\,p(w\mid r,s).$$

**(c)** Marginalise out $R$ and $S$:
$$\mathbb P(W=1)=\sum_{r\in\{0,1\}}\sum_{s\in\{0,1\}}p(r)\,p(s)\,p(W=1\mid r,s).$$

**(d)** $\mathbb P(R=1,S=1,W=0)=p(R=1)\,p(S=1)\,\big(1-p(W=1\mid 1,1)\big)=0.2\cdot0.5\cdot0.1=0.01.$

**(e)**

1. a. True. $R$ and $S$ have no common ancestor and no path between them except through $W$, which is not observed.
2. b. False. Observing the common child $W$ makes them dependent (explaining away). For example, given $W=1$, $\mathbb P(R=1\mid W=1,S=0)=1$ but $\mathbb P(R=1\mid W=1,S=1)\approx0.243$.
3. c. True. $\mathbb P(W=1)=0.45$, so $\mathbb P(R=1\mid W=1)=\frac{0.2\,(0.5\cdot0.9+0.5\cdot0.8)}{0.45}\approx0.378$, while $\mathbb P(R=1\mid W=1,S=1)=\frac{0.2\cdot0.9}{0.2\cdot0.9+0.8\cdot0.7}\approx0.243$. Learning that the sprinkler was on explains the wet grass, so rain becomes less likely.
:::
