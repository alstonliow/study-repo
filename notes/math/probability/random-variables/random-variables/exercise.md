<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-2-01 origin="external" source="fit1058-cn-10.12-q1"}
Two independent fair dice are thrown, represented by random variables $X$
and $Y$. Calculate the probability distribution of $|X-Y|$.
:::

::: {.problem #prob-probability-2-02 origin="external" source="fit1058-cn-10.12-q2"}
Suppose $X$ and $Y$ are independent $\{0,1\}$-valued random variables where
$X$ is unbiased, $\Pr(X=0)=\Pr(X=1)=\frac12$, but the distribution of $Y$ is
unknown. What can you say about the probability distribution of
$X\oplus Y$ (i.e. $X+Y\bmod2$)?
:::

::: {.problem #prob-probability-2-03 origin="external" source="fit1058-cn-10.12-q3"}
One of the bitstrings $000,011,101,110$ is chosen uniformly at random. Let
$X,Y,Z$ be its first, second and third bits.

(a) Prove that (i) $X$ and $Y$ are independent; (ii) $X$ and $Z$ are
    independent; (iii) $Y$ and $Z$ are independent.

(b) Determine whether $Z$ is independent of the pair $(X,Y)$.

(c) Similarly, determine whether $Y$ is independent of the other two,
    and whether $X$ is independent of the other two.
:::

::: {.problem #prob-cs70hw-11-q1 origin="external" source="cs70hw-11-q1"}
**Random Variables Warm-Up.** Let $X$ and $Y$ be random variables, each taking values in the set $\{0, 1, 2\}$, with joint distribution
$$\begin{aligned}
&P[X=0,Y=0]=1/3 && P[X=0,Y=1]=0 && P[X=0,Y=2]=1/3\\
&P[X=1,Y=0]=0 && P[X=1,Y=1]=1/9 && P[X=1,Y=2]=0\\
&P[X=2,Y=0]=1/9 && P[X=2,Y=1]=1/9 && P[X=2,Y=2]=0.
\end{aligned}$$

(a) What are the marginal distributions of $X$ and $Y$?

(b) What are $E[X]$ and $E[Y]$?

(c) (optional) What are $\mathrm{Var}(X)$ and $\mathrm{Var}(Y)$?

(d) Let $I$ be the indicator that $X = 1$, and $J$ be the indicator that $Y = 1$. What are $E[I]$, $E[J]$ and $E[IJ]$?

(e) In general, let $I_A$ and $I_B$ be the indicators for events $A$ and $B$ in a probability space $(\Omega, P)$. What is $E[I_A I_B]$, in terms of the probability of some event?
:::

::: {.problem #prob-cs70hw-11-q2 origin="external" source="cs70hw-11-q2"}
**Marginals.**

(a) Can there exist three random variables $X_1, X_2, X_3$, each taking values in the set $\{+1, -1\}$, with the property that for every $i \ne j$, the joint distribution of $X_i$ and $X_j$ is given by
$$P[X_i = 1, X_j = -1] = \frac{1}{2} \qquad P[X_i = -1, X_j = 1] = \frac{1}{2} \qquad P[X_i = X_j] = 0? \tag{1}$$
If so, specify the joint distribution of $X_1, X_2, X_3$; if not, prove it.

(b) For which natural numbers $n \ge 3$ can there exist random variables $X_1, X_2, \ldots, X_n$, each taking values in the set $\{+1, -1\}$, with the property that for every $i$ and $j$ satisfying $i - j = 1 \pmod n$, the joint distribution of $X_i$ and $X_j$ is given by (1)? For any $n$ that work, specify the joint distribution; for those that do not, prove it.
:::
