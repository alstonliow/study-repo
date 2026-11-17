<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-12-q3" status="draft"}
(a) True: $E[X^2]=\mathrm{Var}(X)+E[X]^2=9+4=13$ (@prp-expectation-and-variance-1).

(b) False. Let $X=-1$ or $5$ with probability $\frac12$ each: $E[X]=2$, $\mathrm{Var}(X)=9$, $X\le10$, and $\Pr(X=2)=0$.

(c) False. Let $X=-7$ with probability $\frac1{10}$ and $X=3$ with probability $\frac9{10}$: $E[X]=-0.7+2.7=2$, $E[X^2]=4.9+8.1=13$, so $\mathrm{Var}(X)=9$, and $X\le10$. But $\Pr(X\ge2)=\frac9{10}\ne\frac1{10}=\Pr(X\le2)$.

(d) True. $Y=10-X\ge0$ and $E[Y]=8$. By Markov's inequality (@thm-markov-inequality), $\Pr(X\le1)=\Pr(Y\ge9)\le\frac89$.

(e) True. By Chebyshev's inequality (@thm-chebyshev-s-inequality), $\Pr(X\ge6)\le\Pr(|X-2|\ge4)\le\frac9{16}$.
:::

::: {.solution for="prob-cs70hw-12-q4" status="draft"}
(a)

1. Let $B_i$ indicate that card $i$ goes to Yiming; the $B_i$ are independent with $E[B_i]=\frac12$, $\mathrm{Var}(B_i)=\frac14$. Yiming's sum is $S=\sum_ic_iB_i$.

2. $E[S]=\frac12\sum_ic_i=0$ and, by independence, $\mathrm{Var}(S)=\sum_ic_i^2\cdot\frac14=\frac14$ (@thm-variance-of-an-independent-sum).

3. Jonathan's sum is $\sum_ic_i-S=-S$. Flipping every coin swaps the hands and has the same probability, so $S$ and $-S$ have the same distribution: $\Pr(S\ge\alpha)=\Pr(S\le-\alpha)$.

4. By Chebyshev's inequality, $\Pr(S\ge\alpha)+\Pr(S\le-\alpha)=\Pr(|S|\ge\alpha)\le\frac{1}{4\alpha^2}$, so $\Pr(\text{Yiming wins})=\Pr(S\ge\alpha)\le\frac1{8\alpha^2}$.

(b) Take $k=3$ cards $\frac1{\sqrt2},-\frac1{\sqrt2},0$ (sum $0$, squares sum $1$) and $\alpha=\frac1{\sqrt2}$. Yiming's sum is at least $\frac1{\sqrt2}$ exactly when he gets the first card and not the second: probability $\frac14=\frac1{8\alpha^2}$.
:::

::: {.solution for="prob-cs70hw-12-q5" status="draft"}
(a) $\varphi(x)=(x+c)^2$ is non-negative and increasing for $x>0$. So $\Pr(X\ge\alpha)\le\frac{E[(X+c)^2]}{(\alpha+c)^2}$, and $E[(X+c)^2]=E[X^2]+2cE[X]+c^2=\sigma^2+c^2$.

(b) Let $h(c)=\frac{\sigma^2+c^2}{(\alpha+c)^2}$. Then
$$h'(c)=\frac{2c(\alpha+c)-2(\sigma^2+c^2)}{(\alpha+c)^3}=\frac{2(c\alpha-\sigma^2)}{(\alpha+c)^3},$$
which is negative for $c<\frac{\sigma^2}\alpha$ and positive after, so the minimum is at $c=\frac{\sigma^2}\alpha$. There
$$h=\frac{\sigma^2+\sigma^4/\alpha^2}{(\alpha+\sigma^2/\alpha)^2}=\frac{\sigma^2(\alpha^2+\sigma^2)/\alpha^2}{(\alpha^2+\sigma^2)^2/\alpha^2}=\frac{\sigma^2}{\alpha^2+\sigma^2}.$$

(c) The two tails need not be equal, and one of them can carry almost the whole Chebyshev bound. Let $X=3$ with probability $\frac14$ and $X=-1$ with probability $\frac34$: $E[X]=0$, $\mathrm{Var}(X)=\frac94+\frac34=3$. With $\alpha=3$, $\Pr(X\ge3)=\frac14>\frac3{18}=\frac{\mathrm{Var}(X)}{2\alpha^2}$.

(d) Markov: $\Pr(X\ge5)\le\frac35$. Chebyshev: $\Pr(X\ge5)\le\Pr(|X-3|\ge2)\le\frac24=\frac12$. Part (b), applied to $X-3$ (mean $0$, variance $2$) with $\alpha=2$: $\Pr(X\ge5)\le\frac2{4+2}=\frac13$, the best of the three.
:::
