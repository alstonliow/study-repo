<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-3-q3" status="draft"}
Let $N\sim\text{Poisson}(\lambda)$ be the total and $N_A,N_B$ the counts, so that given $N=n$, $N_A\sim\text{Bin}(n,p)$.

(a)–(b) For $a,b\ge0$,
$$P(N_A=a,N_B=b)=e^{-\lambda}\frac{\lambda^{a+b}}{(a+b)!}\binom{a+b}{a}p^a(1-p)^b=e^{-\lambda p}\frac{(\lambda p)^a}{a!}\cdot e^{-\lambda(1-p)}\frac{(\lambda(1-p))^b}{b!}.$$
The joint PMF factorises, so $N_A\sim\text{Poisson}(\lambda p)$, $N_B\sim\text{Poisson}(\lambda(1-p))$, and they **are independent** (the splitting property, @thm-poisson-merging-splitting).
:::

::: {.solution for="prob-eecs126hw-7-q2" status="draft"}
(a) Survivors of a $\text{Poisson}(\mu)$ population, each kept with probability $p$, form a $\text{Poisson}(\mu p)$ variable (splitting, @thm-poisson-merging-splitting), and adding independent $\text{Poisson}(\lambda)$ immigrants gives $\text{Poisson}(\mu p+\lambda)$ (@exm-transform-poisson-sum). So $X_1\sim\text{Poisson}(\lambda_0p+\lambda)$, and by induction
$$X_n\sim\text{Poisson}\Bigl(\lambda_0p^n+\lambda\frac{1-p^n}{1-p}\Bigr).$$

(b) The parameter tends to $\frac{\lambda}{1-p}$, and Poisson PMFs are continuous in the parameter, so $X_n\to\text{Poisson}\bigl(\frac{\lambda}{1-p}\bigr)$ in distribution.

For an arbitrary $X_0$, write $X_n=A_n+B_n$, where $A_n$ counts the members of generation $0$ still alive ($A_n\sim\text{Bin}(X_0,p^n)$ given $X_0$) and $B_n$, the descendants-free count of immigrants still alive, is independent of $X_0$ and, by (a) with $\lambda_0=0$, $\text{Poisson}(\lambda\frac{1-p^n}{1-p})$.

1. $P(A_n>0)=E[1-(1-p^n)^{X_0}]\to0$ by dominated convergence, since $X_0<\infty$ and each term is at most $1$.
2. For every $k$, $|P(X_n=k)-P(B_n=k)|\le P(A_n>0)\to0$.
3. $P(B_n=k)\to P(\text{Poisson}(\frac{\lambda}{1-p})=k)$. So the limit is the same Poisson distribution for every initial distribution.
:::

::: {.solution for="prob-eecs126hw-7-q4" status="draft"}
(a) The counts are non-negative, so the sum is $0$ iff there are no arrivals in $[0,1]\cup[2,5]$, of total length $4$. By @thm-poisson-process-counts the probability is $e^{-4\lambda}$.

(b) $N(1,3)=N(1,2)+N(2,3)$, and $N(2,3)\sim\text{Poisson}(\lambda)$ is independent of $N(1,2)$. So the answer is $3+\lambda$.

(c) Given $N(2)=1$, the second arrival comes after time $2$; by memorylessness the wait after time $2$ is $\text{Exp}(\lambda)$, independent of the past. So $E(T_2\mid N(2)=1)=2+\frac1\lambda$.
:::

::: {.solution for="prob-eecs126hw-7-q5" status="draft"}
Let $\lambda=\lambda_A=\lambda_B$. By merging (@thm-poisson-merging-splitting), points come at rate $2\lambda$ and each is scored by $A$ with probability $\frac12$, independently. So the lead $D$ of team $A$ is a fair $\pm1$ random walk started at $m$ and stopped at $\pm k$.

(a) By gambler's ruin (@exm-gamblers-ruin) on $\{-k,\dots,k\}$, $A$ wins with probability $\frac{m+k}{2k}$.

(b) The expected number of points until a fair walk from $m$ leaves $(-k,k)$ is $(k-m)(k+m)=k^2-m^2$ (first-step equations $t(x)=1+\frac{t(x-1)+t(x+1)}2$, $t(\pm k)=0$). The times between points are i.i.d. $\text{Exp}(2\lambda)$, independent of who scores, so by Wald's identity
$$E[T]=\frac{k^2-m^2}{2\lambda}.$$
:::

::: {.solution for="prob-eecs126hw-8-q1" status="draft"}
The sum is $\text{Exp}(\lambda p)$.

1. Let the $X_i$ be the interarrival times of a Poisson process of rate $\lambda$, and mark each arrival independently with probability $p$. The index $N$ of the first marked arrival is $\text{Geom}(p)$, independent of the $X_i$, so $\sum_{i=1}^{N}X_i$ is the time of the first marked arrival.
2. By splitting (@thm-poisson-merging-splitting) the marked arrivals form a Poisson process of rate $\lambda p$, whose first arrival time is $\text{Exp}(\lambda p)$.

(Check with transforms: $E[e^{s\sum}]=\sum_np(1-p)^{n-1}\bigl(\frac{\lambda}{\lambda-s}\bigr)^n=\frac{\lambda p}{\lambda p-s}$.)
:::

::: {.solution for="prob-eecs126hw-8-q2" status="draft"}
Write $\beta=\frac{\lambda}{\lambda+\mu}$. In the merged process (@thm-poisson-merging-splitting) each event is a bus with probability $\beta$ and a student with probability $1-\beta$, independently.

(a) The students arriving in an interval of length $x$: $\text{Poisson}(\mu x)$ (@thm-poisson-process-counts), independent of the buses.

(b) After the 9:30 bus everything starts afresh. The number $K$ of students before the next bus is the number of failures before the first success in the merged event sequence:
$$P(K=k)=(1-\beta)^k\beta=\Bigl(\frac{\mu}{\lambda+\mu}\Bigr)^k\frac{\lambda}{\lambda+\mu},\qquad k\ge0.$$

(c) The students on the next bus are those who arrived since the last bus before 9:30. Looking backwards from 9:30 the processes are again Poisson (infinitely long past), so the students since the last bus and those until the next bus are two independent copies of $K$ from (b). Their sum has the negative binomial distribution
$$P(K_1+K_2=k)=(k+1)\beta^2(1-\beta)^k,\qquad k\ge0,$$
with mean $2\mu/\lambda$, twice that in (b) (the inspection paradox).
:::

::: {.solution for="prob-eecs126d-7-q3" status="draft"}
The gaps $G_1,G_2,\dots$ (from time $0$ to the first car, then between cars) are i.i.d. $\text{Exp}(\lambda)$, and you turn at the end of the first gap longer than $\tau$. Let $q=P(G>\tau)=e^{-\lambda\tau}$.

(a) $N$ is the number of gaps $\le\tau$ before the first gap $>\tau$: $P(N=k)=(1-q)^kq$, so $E[N]=\frac{1-q}{q}=e^{\lambda\tau}-1$.

(b) $N\ge n$ says exactly that $G_1,\dots,G_n\le\tau$, and by independence the gap $G_n$ is then distributed as $G$ given $G\le\tau$:
$$E[G\mid G\le\tau]=\frac{1}{1-e^{-\lambda\tau}}\int_0^\tau\lambda te^{-\lambda t}\,dt=\frac1\lambda-\frac{\tau e^{-\lambda\tau}}{1-e^{-\lambda\tau}}.$$

(c) The wait is $G_1+\dots+G_N+\tau$, where given $N$ the first $N$ gaps are i.i.d. given $\le\tau$. So
$$E[\text{wait}]=E[N]\,E[G\mid G\le\tau]+\tau=\frac{e^{\lambda\tau}-1}{\lambda}-\tau+\tau=\frac{e^{\lambda\tau}-1}{\lambda},$$
using $(e^{\lambda\tau}-1)\frac{e^{-\lambda\tau}}{1-e^{-\lambda\tau}}=1$.
:::
