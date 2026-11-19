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
