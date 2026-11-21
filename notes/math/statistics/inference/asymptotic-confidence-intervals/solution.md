<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18650f16-1-q3" status="draft"}
1. The $X_i$ are i.i.d. with mean $p$ and variance $p(1-p)>0$; this is the central limit theorem (@thm-central-limit-theorem).

2. By symmetry of $Z$, $\Pr(Z<-t)=\Pr(Z>t)=1-\Pr(Z\le t)$, so $\Pr(|Z|\le t)=\Pr(Z\le t)-\Pr(Z<-t)=2\Pr(Z\le t)-1$.

3. $p\in I_t$ if and only if $\bigl|\sqrt n(\bar X_n-p)/\sqrt{p(1-p)}\bigr|\le t$. By part 1 (the limit CDF is continuous) the probability of this tends to $\Pr(|Z|\le t)=2\Phi(t)-1$ by part 2.

4. We need $2\Phi(t)-1=0.95$, that is $\Phi(t)=0.975$: $t_0=1.96$.

5. a) $p(1-p)=\frac14-(p-\frac12)^2\le\frac14$.

   b) $J_1=\bigl[\bar X_n-\frac{1.96}{2\sqrt n},\ \bar X_n+\frac{1.96}{2\sqrt n}\bigr]$ contains $I_{t_0}$, so $\liminf\Pr(p\in J_1)\ge0.95$.

   c) Yes. On $[0,0.3]$ the function $p(1-p)$ is increasing, so $p(1-p)\le0.21$, and $\bar X_n\pm1.96\sqrt{0.21/n}$ works; its half-width $1.96\cdot0.458/\sqrt n$ is smaller than $1.96\cdot0.5/\sqrt n$.

6. a) $p\in I_{t_0}$ means $(\bar X_n-p)^2\le\frac{t_0^2}np(1-p)$, that is, with $c=t_0^2/n$,
   $$(1+c)p^2-(2\bar X_n+c)p+\bar X_n^2\le0 .$$

   b) The quadratic has positive leading coefficient, so the inequality holds between its roots
   $$p_\pm=\frac{2\bar X_n+c\pm\sqrt{(2\bar X_n+c)^2-4(1+c)\bar X_n^2}}{2(1+c)}=\frac{2\bar X_n+c\pm\sqrt{c^2+4c\bar X_n(1-\bar X_n)}}{2(1+c)} .$$

   c) $J_2=[p_-,p_+]$. The event $p\in J_2$ is the event $p\in I_{t_0}$, whose probability tends to $0.95$ by parts 3 and 4.

7. $J_3=\bar X_n\pm1.96\sqrt{\bar X_n(1-\bar X_n)/n}$. By the law of large numbers and continuous mapping, $\sqrt{\bar X_n(1-\bar X_n)}/\sqrt{p(1-p)}\to1$ in probability, so by Slutsky's theorem (@thm-slutsky) $\sqrt n(\bar X_n-p)/\sqrt{\bar X_n(1-\bar X_n)}\to N(0,1)$ in distribution, and $\Pr(p\in J_3)\to0.95$ (@prp-three-asymptotic-intervals, part 3).

8. a) With $\hat p=0.7341$ and $n=10^4$:
   $J_1=[0.7243,\,0.7439]$ (length $0.0196$); $J_2=[0.7254,\,0.7427]$ (length $0.01732$); $J_3=[0.7254,\,0.7428]$ (length $0.01732$). $J_2$ and $J_3$ agree to four decimals and are about $12\%$ shorter than the conservative $J_1$, because $\hat p(1-\hat p)\approx0.195$ is well below $1/4$.

   b) The interval must not depend on $p$ before the data are seen, so use $J_1$, of length $1.96/\sqrt n$. We need $1.96/\sqrt n\le0.05$, i.e. $n\ge(1.96/0.05)^2=1536.6$: at least $n=1537$ voters.
:::

::: {.solution for="prob-mit18650f16-2-q3" status="draft"}
1. The mean and variance of a Poisson variable are both $\lambda$, so by the central limit theorem $a_n=\sqrt{n/\lambda}$, $b_n=\lambda$ work: $\sqrt{n/\lambda}\,(\bar X_n-\lambda)\to N(0,1)$.

2. As in Problem Set 1: by symmetry $\Pr(Z<-t)=1-\Pr(Z\le t)$, so $\Pr(|Z|\le t)=2\Pr(Z\le t)-1$.

3. $I=\bigl[\bar X_n-1.96\sqrt{\lambda/n},\ \bar X_n+1.96\sqrt{\lambda/n}\bigr]$: the event $\lambda\in I$ is $|a_n(\bar X_n-b_n)|\le1.96$, whose probability tends to $2\Phi(1.96)-1=0.95$.

4. Either solve for $\lambda$ or plug in (@prp-three-asymptotic-intervals).

   *Solving:* $|\bar X_n-\lambda|\le1.96\sqrt{\lambda/n}$ means $(\bar X_n-\lambda)^2\le c\lambda$ with $c=1.96^2/n$, i.e. $\lambda^2-(2\bar X_n+c)\lambda+\bar X_n^2\le0$, which holds between the roots:
   $$J=\Bigl[\bar X_n+\tfrac c2-\sqrt{c\bar X_n+\tfrac{c^2}4},\ \ \bar X_n+\tfrac c2+\sqrt{c\bar X_n+\tfrac{c^2}4}\Bigr].$$
   The event $\lambda\in J$ equals the event $\lambda\in I$, so its probability tends to $0.95$.

   *Plug-in:* $J'=\bar X_n\pm1.96\sqrt{\bar X_n/n}$; since $\bar X_n/\lambda\to1$ in probability, Slutsky's theorem gives $\Pr(\lambda\in J')\to0.95$ as well.
:::

::: {.solution for="prob-mit18650f16-2-q4" status="draft"}
1. $M_n\le\theta$, and for $0<\varepsilon<\theta$, $\Pr(|M_n-\theta|>\varepsilon)=\Pr(M_n<\theta-\varepsilon)=\bigl(1-\varepsilon/\theta\bigr)^n\to0$.

2. Let $W_n=n(1-M_n/\theta)\in[0,n]$. For $0\le t\le n$,
$$\Pr(W_n\le t)=\Pr\bigl(M_n\ge\theta(1-t/n)\bigr)=1-\Bigl(1-\frac tn\Bigr)^n,$$
with $\Pr(W_n\le t)=0$ for $t<0$ and $1$ for $t>n$. For fixed $t\ge0$ this tends to $1-e^{-t}$, the CDF of $\operatorname{Exp}(1)$, at every $t$.

3. Let $q=-\ln0.05\approx3.00$, so $\Pr(E\le q)=0.95$ for $E\sim\operatorname{Exp}(1)$. Since $\theta\ge M_n$ always, $\theta\in[M_n,M_n+c]$ if and only if $\theta-M_n\le c$. Take $c$ to depend on the data only: $W_n\le q$ is equivalent to $\theta\le M_n/(1-q/n)$ (for $n>q$), so
$$I=\Bigl[M_n,\ M_n+\frac{q}{n-q}M_n\Bigr],\qquad c=\frac{qM_n}{n-q},$$
has $\Pr(\theta\in I)=\Pr(W_n\le q)\to1-e^{-q}=0.95$. Its length is of order $1/n$, much shorter than the $1/\sqrt n$ of central-limit intervals.

4. No. $\Pr(M_n\le x)=(x/\theta)^n$ on $[0,\theta]$, so $M_n$ has density $nx^{n-1}/\theta^n$ and $E[M_n]=\frac n{n+1}\theta<\theta$: the bias is $-\theta/(n+1)$. The estimator $\frac{n+1}nM_n$ is unbiased.
:::
