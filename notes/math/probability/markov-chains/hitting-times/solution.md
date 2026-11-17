<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-15-q1" status="draft"}
(a) Count money in units of \$100. States $\{0,1,2,3,4\}$, start at $1$. For $i\in\{1,2,3\}$: $P(i,i+1)=p$, $P(i,i-1)=1-p$. States $0$ and $4$ are absorbing: $P(0,0)=P(4,4)=1$.

(b) This is gambler's ruin with $M=4$ (@exm-gamblers-ruin). With $\rho=\frac{1-p}p$ and $p\ne\frac12$, the probability of reaching $4$ before $0$ from $1$ is
$$\alpha(1)=\frac{1-\rho}{1-\rho^4}=\frac1{1+\rho+\rho^2+\rho^3}.$$
For $p=\frac12$ the first step equations $\alpha(i)=\frac12\alpha(i-1)+\frac12\alpha(i+1)$ make $\alpha$ linear, so $\alpha(1)=\frac14$; the formula $\frac1{1+\rho+\rho^2+\rho^3}$ also gives $\frac14$ at $\rho=1$.
:::

::: {.solution for="prob-cs70hw-15-q2" status="draft"}
(a) State $i\in\{0,1,\dots,n\}$ is the number of distinct coupons collected so far; start at $0$. From $i<n$, the next coupon is new with probability $\frac{n-i}n$ (move to $i+1$) and a repeat with probability $\frac in$ (stay at $i$). State $n$ is absorbing.

(b) Let $\beta(i)$ be the expected number of trips from state $i$ until state $n$. By @thm-first-step-hitting-time, $\beta(n)=0$ and
$$\beta(i)=1+\frac in\beta(i)+\frac{n-i}n\beta(i+1),\qquad\text{so}\qquad\beta(i)=\frac n{n-i}+\beta(i+1).$$
Unrolling, $\beta(0)=\sum_{i=0}^{n-1}\frac n{n-i}=n\sum_{j=1}^n\frac1j=nH_n\approx n(\ln n+\gamma)$, as in @thm-coupon-collector.
:::

::: {.solution for="prob-cs70hw-15-q3" status="draft"}
(a) With $R_i$ the expected number of steps from $i$ to $n$:
$$R_n=0,\qquad R_0=1+R_1,\qquad R_i=1+\tfrac12R_{i-1}+\tfrac12R_{i+1}\quad(0<i<n).$$

(b) We show by induction that $R_i=(2i+1)+R_{i+1}$ for $0\le i<n$. For $i=0$ this is $R_0=1+R_1$. If $R_{i-1}=(2i-1)+R_i$, then $R_i=1+\frac12\bigl((2i-1)+R_i\bigr)+\frac12R_{i+1}$, so $\frac12R_i=\frac{2i+1}2+\frac12R_{i+1}$, i.e. $R_i=(2i+1)+R_{i+1}$. Adding up from $i$ to $n-1$,
$$R_i=\sum_{j=i}^{n-1}(2j+1)=n^2-i^2.$$
So Alice needs $R_0=n^2$ steps on average.
:::

::: {.solution for="prob-cs70hw-15-q4" status="draft"}
Write the state as (top, bottom) $\in\{00,01,10,11\}$. One step moves (top, bottom) $=(t,b)$ to $(b,B)$, where $B=1$ with probability $p$, independently of the past.

(a) Let $\beta(s)$ be the expected number of seconds from state $s$ until $11$. Then $\beta(11)=0$ and
$$\begin{aligned}
\beta(00)&=1+p\,\beta(01)+(1-p)\,\beta(00),\\
\beta(01)&=1+p\,\beta(11)+(1-p)\,\beta(10),\\
\beta(10)&=1+p\,\beta(01)+(1-p)\,\beta(00).
\end{aligned}$$
(Solving: $\beta(10)=\beta(00)$, $\beta(01)=1+(1-p)\beta(00)$, and then $\beta(00)=\frac{1+p}{p^2}$.)

(b) Now a step from $(t,b)$ to $(b,B)$ takes $1+b+B$ seconds. So $\beta(11)=0$ and
$$\begin{aligned}
\beta(00)&=p\bigl(2+\beta(01)\bigr)+(1-p)\bigl(1+\beta(00)\bigr),\\
\beta(01)&=p\bigl(3+\beta(11)\bigr)+(1-p)\bigl(2+\beta(10)\bigr),\\
\beta(10)&=p\bigl(2+\beta(01)\bigr)+(1-p)\bigl(1+\beta(00)\bigr).
\end{aligned}$$

(c) After the first second, the bottom component holds a boba with probability $p$, independently each second, and the top holds what the bottom held one second earlier. So from the second second on, each second a boba enters Jonathan's mouth with probability $p$. Equivalently, the chain is irreducible (for $0<p<1$) with invariant distribution $\pi(t,b)=\Pr(t)\Pr(b)$, each component independently full with probability $p$ (check: it satisfies the balance equations). By @thm-markov-fraction-of-time, the long-run fraction of seconds with a boba in the top component is $p$, so Jonathan consumes $10p$ calories per second on average.

(d) Under $\pi$, the number of boba is $\mathrm{Bin}(2,p)$, so the long-run average number in the straw is $2p$.
:::
