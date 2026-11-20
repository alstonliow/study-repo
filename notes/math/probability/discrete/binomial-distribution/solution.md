<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-probability-2-04" status="draft"}
The suggestion does not give a fair die. The number of Heads is
$\mathrm{Bin}(5,\frac12)$, so the probabilities of $1,\dots,6$ are
$$\tfrac1{32},\ \tfrac5{32},\ \tfrac{10}{32},\ \tfrac{10}{32},\ \tfrac5{32},\ \tfrac1{32}.$$
Rolling a $3$ or $4$ is ten times as likely as rolling a $1$ or $6$.

A fair alternative:

1. Toss three coins and read them as a binary number $b\in\{0,\dots,7\}$.
   All eight values are equally likely.

2. If $b\le5$, output $b+1$. If $b\in\{6,7\}$, discard the result and toss
   again.

3. Each accepted round gives each of $1,\dots,6$ with probability $\frac16$.
   A round is accepted with probability $\frac68$, so on average this takes
   $\frac43$ rounds, i.e. $4$ tosses.

With a fixed number of coins this cannot be done exactly: every outcome of
$n$ tosses has probability $2^{-n}$, so every event has probability
$k/2^n$, which is never $\frac16$.
:::

::: {.solution for="prob-probability-2-07" status="draft"}
$E(X) = np = 8$, $\mathrm{Var}(X) = np(1-p) = 4$, and $\sigma = 2$. All
probabilities below are $\binom{16}k/2^{16}$ summed over the relevant $k$.

(a) $\Pr(X = 8) = \binom{16}8/2^{16} = 12{,}870/65{,}536\approx 0.196$. So
    "exactly half" happens less than one time in five.

(b) $|X-8|\ge4$ means $X\le4$ or $X\ge12$:
    $$\Pr = \frac{2(1+16+120+560+1820)}{65{,}536} = \frac{5{,}034}{65{,}536}\approx 0.077.$$

(c) $|X-8|\ge6$ means $X\le2$ or $X\ge14$:
    $$\Pr = \frac{2(1+16+120)}{65{,}536} = \frac{274}{65{,}536}\approx 0.0042.$$

(d) Chebyshev gives at most $\frac14$ for (b) and $\frac19\approx 0.11$ for
    (c). Both bounds hold but are much larger than the exact values: about
    $3$ times too big for (b) and about $27$ times for (c).
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-11-q3" status="draft"}
(a) Each of the $n$ planes survives day $1$ independently with probability $p$: $X_1\sim\mathrm{Bin}(n,p)$, $\Pr(X_1=k)=\binom nkp^k(1-p)^{n-k}$.

(b) A plane is left after two days if it flies successfully on both days, with probability $p^2$, independently of the other planes. So $X_2\sim\mathrm{Bin}(n,p^2)$.

(c) In the same way $X_t\sim\mathrm{Bin}(n,p^t)$.

(d) $\Pr(X_t\ge1)=1-\Pr(X_t=0)=1-(1-p^t)^n$.

(e) Not independent. $\Pr(A_1)=\Pr(B_1)=(1-p)^2$, while $A_1\cap B_1$ means planes $1,2,3$ all crash: $\Pr(A_1\cap B_1)=(1-p)^3\ne(1-p)^4$, since $0<1-p<1$.

(f) $\Pr(B_2)=1-p$. $A_2$: plane $1$ crashes, exactly one of the other $n-1$ crashes: $\Pr(A_2)=(1-p)\cdot(n-1)(1-p)p^{n-2}$. $A_2\cap B_2$: planes $1,2$ crash and the rest fly: $(1-p)^2p^{n-2}$. Independence means $(1-p)^2p^{n-2}=(n-1)(1-p)^3p^{n-2}$, i.e. $(n-1)(1-p)=1$, so $n=1+\frac1{1-p}$ (which must be an integer).

(g) Not independent. $\Pr(X_i=0)=(1-p^i)^n>0$ and $\Pr(X_j=n)=p^{jn}>0$, but $\Pr(X_i=0,X_j=n)=0$, since planes never come back.
:::

::: {.solution for="prob-eecs126hw-2-q3" status="draft"}
1. The $i$th entry moves to position $X=1+Y$, where $Y$ is the number of non-zero entries among the first $i-1$.
2. The entries are independent, so conditioning on entry $i$ does not affect the others, and $Y\sim\operatorname{Bin}(i-1,\tfrac9{10})$.
3. Hence $E[X]=1+\tfrac9{10}(i-1)$ and $\operatorname{var}(X)=\operatorname{var}(Y)=\tfrac{9}{100}(i-1)$.
:::

::: {.solution for="prob-mit6041f10-4-q2" status="draft"}
(a) The number of 3's is $\mathrm{Bin}(6,\frac14)$: $\binom63(\frac14)^3(\frac34)^3=\frac{135}{1024}\approx0.132$.

(b) Given exactly two 1's, every choice of the two positions is equally likely (each sequence with two 1's in given places has the same probability). The first roll is one of them in $\binom51$ of the $\binom62$ choices: $\frac5{15}=\frac13$.

(c) Every sequence of three 1's and three 2's has the same probability $(\frac12)^3(\frac14)^3$, so given the counts they are equally likely: $1/\binom63=\frac1{20}$.

(d) Let $K\sim\mathrm{Bin}(6,\frac14)$. $\Pr(K\ge1)=1-(\frac34)^6=\frac{3367}{4096}$, so for $k=1,\dots,6$
$$\Pr(K=k\mid K\ge1)=\frac{\binom6k(1/4)^k(3/4)^{6-k}}{1-(3/4)^6},$$
which is $\frac{1458}{3367},\frac{1215}{3367},\frac{540}{3367},\frac{135}{3367},\frac{18}{3367},\frac1{3367}$.
:::

::: {.solution for="prob-mit6041f10-4-q4" status="draft"}
(a) $A$ is determined by tosses $1$–$8$ and $B$ by toss $9$. The tosses are independent, so $\Pr(A\cap B)=\binom86p^6(1-p)^2\cdot p=\Pr(A)\Pr(B)$.

(b) Tosses $1$–$4$ and $8$–$10$ do not overlap, so the probability is $\binom43p^3(1-p)\cdot\binom32p^2(1-p)=12p^5(1-p)^2$.

(c) Given 4 heads in 7 tosses, all $\binom74=35$ placements are equally likely. The second head is at toss 4 when tosses $1$–$3$ hold exactly one head ($3$ ways), toss 4 is a head, and tosses $5$–$7$ hold two heads ($3$ ways). The probability is $\frac9{35}$.

(d) The windows $1$–$8$ and $6$–$10$ overlap in tosses $6,7,8$. Let $k$ be the number of heads there; then tosses $1$–$5$ have $5-k$ heads and tosses $9,10$ have $3-k$, so $1\le k\le3$. Summing,
$$\sum_{k=1}^3\binom5{5-k}\binom3k\binom2{3-k}p^{8-k}(1-p)^{2+k}=15p^7(1-p)^3+60p^6(1-p)^4+10p^5(1-p)^5.$$
:::
