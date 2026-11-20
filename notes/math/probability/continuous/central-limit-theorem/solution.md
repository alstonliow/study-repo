<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-14-q2" status="draft"}
(a) One toss of Bob $i$'s coin has mean $0$ and variance $i^2$. Group the tosses into $n$ rounds, one toss of each Bob per round: each round contributes an independent sum with mean $0$ and variance $\sum_{i=1}^ki^2=\frac{k(k+1)(2k+1)}6$. By the central limit theorem (@thm-central-limit-theorem), $(X_1+\dots+X_k)/\sqrt n$ is approximately $N\bigl(0,\frac{k(k+1)(2k+1)}6\bigr)$.

(b) Let $Z_n=\frac1{\sqrt n}\sum_{k=1}^n\frac{X_k-\mu}\sigma$, which tends to $N(0,1)$ in distribution. The event is $|Z_n|\le n^{\alpha-1/2}$.

- $\alpha=\frac12$: the limit is $\Phi(1)-\Phi(-1)=2\Phi(1)-1\approx0.683$.
- $\alpha>\frac12$: the interval $[-n^{\alpha-1/2},n^{\alpha-1/2}]$ grows. By Chebyshev, $\Pr(|Z_n|>t)\le\frac1{t^2}$, so the probability tends to $1$.
- $\alpha<\frac12$: the interval shrinks to $0$. For any fixed $\varepsilon>0$ it is eventually inside $[-\varepsilon,\varepsilon]$, whose probability tends to $2\Phi(\varepsilon)-1$, which is as small as we like. So the limit is $0$.
:::

::: {.solution for="prob-mit6041f10-10-q1" status="draft"}
Insolvency means a gain below $-5$.

(a) $\Pr(R<-5)=\Phi\bigl(\frac{-5-7}{10}\bigr)=\Phi(-1.2)\approx0.115$: more than one year in ten, an unacceptable risk.

(b) The average $\bar R$ is normal with mean $7$ and standard deviation $10/\sqrt{20}\approx2.24$, so $\Pr(\bar R<-5)=\Phi(-5.37)\approx4\times10^{-8}$.

(c) Now $\mathrm{Cov}(R_i,R_j)=\frac12\cdot100=50$ for $i\ne j$, so
$$\mathrm{Var}(\bar R)=\frac1{400}\bigl(20\cdot100+380\cdot50\bigr)=52.5,$$
standard deviation about $7.25$, and $\Pr(\bar R<-5)=\Phi(-12/7.25)\approx\Phi(-1.66)\approx0.049$. Correlation destroys most of the benefit of diversification.
:::

::: {.solution for="prob-mit6041f10-10-q2" status="draft"}
1. The male votes $X\sim\mathrm{Bin}(300,0.4)$ have mean $120$ and variance $72$; the female votes $Y\sim\mathrm{Bin}(196,0.5)$ have mean $98$ and variance $49$.

2. $D=X-Y$ is a sum of many independent terms, with mean $22$ and variance $121$, so it is approximately normal with standard deviation $11$.

3. $D$ is integer valued, so $\Pr(D>0)=\Pr(D\ge1)$; with the half-integer correction this is about $\Pr(D>0.5)\approx\Phi\bigl(\frac{21.5}{11}\bigr)=\Phi(1.95)\approx0.975$. (Without the correction, $\Phi(2)\approx0.977$.)
:::

::: {.solution for="prob-mit6041f10-10-q3" status="draft"}
$S_n$ has mean $\frac n2$ and standard deviation $\frac{\sqrt n}2$; let $Z_n=(S_n-\frac n2)/\frac{\sqrt n}2$, which converges in distribution to a standard normal (@thm-central-limit-theorem).

(a) The event contains at most $21$ values of $S_n$, and each has probability at most $\binom n{\lfloor n/2\rfloor}2^{-n}\le\frac1{\sqrt{n/2}}$ (a standard bound on the central binomial coefficient), so the probability is at most $21\sqrt{2/n}\to0$. In terms of $Z_n$ the window $|Z_n|\le20/\sqrt n$ shrinks to a point. The limit is $0$.

(b) The event is $|S_n/n-\frac12|\le\frac1{10}$, whose probability tends to $1$ by the weak law of large numbers.

(c) The event is $|Z_n|\le1$, so the limit is $\Phi(1)-\Phi(-1)\approx0.683$.
:::
