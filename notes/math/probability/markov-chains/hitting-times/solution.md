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

::: {.solution for="prob-eecs126hw-1-q4" status="draft"}
The answer is $\frac1{n-1}$ for every $k$.

1. Cut the circle at $k$ and unroll it into a path $0,1,\dots,n$, where both ends $0$ and $n$ are $k$ and $1$, $n-1$ are its two neighbours. Before first reaching $k$, the ant moves on this path.
2. Before reaching $k$ the ant must reach one of $k$'s neighbours, say position $1$ (the other case is symmetric); it has not yet visited $k$. At that moment, all other points have been visited exactly when the ant later reaches position $n-1$ before position $0$.
3. By the fresh start property and gambler's ruin (@exm-gamblers-ruin), from $1$ a fair walk reaches $n-1$ before $0$ with probability $\frac1{n-1}$, regardless of which neighbour was reached first.
:::

::: {.solution for="prob-eecs126d-5-q2" status="draft"}
The answer is $\frac{21}2$.

1. The products equal to $12$ are $2\cdot6$, $6\cdot2$, $3\cdot4$, $4\cdot3$: after any useful roll ($2,3,4,6$) exactly one face of the next roll finishes. Let $a$ be the expected number of further rolls from the start or after a useless roll ($1$ or $5$), and $b$ after a useful roll that did not finish.
2. First-step equations (@thm-first-step-hitting-time):
$$a=1+\tfrac13a+\tfrac23b,\qquad b=1+\tfrac16\cdot0+\tfrac36b+\tfrac26a,$$
since after a useful roll, $1$ face finishes, $3$ faces are useful but do not finish, and $2$ are useless.
3. The first gives $a=\frac32+b$; substituting in the second, $\frac b6=\frac32$, so $b=9$ and $a=\frac{21}2$. (A simulation gives $10.51$.)
:::

::: {.solution for="prob-eecs126hw-4-q1" status="draft"}
(a) $\{0,1\}$ and $\{4,5\}$ are closed communicating classes, hence recurrent; $\{2,3\}$ is transient (it leaks to $1$ and to $4$ and never returns).

(b) Reaching $0$ before $5$ means entering $\{0,1\}$ before $\{4,5\}$ (once in a closed class, the chain stays there and hits every state of it). With $h_i$ the probability from $i$ (@thm-first-step-hitting-probability): $h_2=\frac12+\frac12h_3$, $h_3=\frac12h_2$, so $h_2=\frac23$ (and $h_3=\frac13$).

(c) On $\{0,1\}$ balance $\pi(0)\alpha=\pi(1)\beta$ gives $\mu=\bigl(\frac{\beta}{\alpha+\beta},\frac{\alpha}{\alpha+\beta},0,0,0,0\bigr)$; on $\{4,5\}$, $\nu=\bigl(0,0,0,0,\frac{q}{p+q},\frac{p}{p+q}\bigr)$. A stationary distribution puts no mass on transient states, so the stationary distributions are exactly $\lambda\mu+(1-\lambda)\nu$, $\lambda\in[0,1]$.

(d) Yes. The chain is absorbed in $\{0,1\}$ with probability $w=\frac23\gamma+\frac13(1-\gamma)=\frac{1+\gamma}3$, and each closed class is aperiodic (self-loops), so within it the distribution converges (@thm-markov-convergence). The limit is $w\mu+(1-w)\nu$.
:::

::: {.solution for="prob-eecs126hw-5-q4" status="draft"}
(a) The answer is $18$ moves. The grid is symmetric about the diagonal through the start and the stairs, so squares in mirror positions have the same mean time. Let $t_A$ be for the start corner, $t_B$ for its two neighbours, $t_C$ for the centre, $t_D$ for the two other corners and $t_E$ for the two neighbours of the stairs. First-step analysis (@thm-first-step-hitting-time):
$$t_A=1+t_B,\quad t_B=1+\tfrac13(t_A+t_C+t_D),\quad t_C=1+\tfrac12(t_B+t_E),\quad t_D=1+\tfrac12(t_B+t_E),\quad t_E=1+\tfrac13(t_C+t_D).$$
Then $t_C=t_D$, $t_E=1+\frac23t_C$, $t_C=\frac32+\frac12t_B+\frac13t_C$ gives $t_C=\frac94+\frac34t_B$, and $t_B=1+\frac13(1+t_B)+\frac23t_C$ gives $t_B=17$. So $t_C=t_D=15$, $t_E=11$ and $t_A=18$.

(b) The answer is $\frac25$. Reflecting the grid in its middle column swaps the two stairs, so $h(x)+h(x')=1$ for mirror squares $x,x'$; in particular $h=\frac12$ on the middle column. With $a$ the start corner and $d$ the square below it (next to the bad stairs):
$$a=\tfrac12\bigl(\tfrac12+d\bigr),\qquad d=\tfrac13\bigl(a+\tfrac12+0\bigr).$$
So $a=\frac14+\frac16a+\frac1{12}$, $a=\frac25$ (and $d=\frac3{10}$).
:::
