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

::: {.solution for="prob-mit6042f10-12-q4" status="draft"}
Toss the coin $n$ times and guess "biased" if the fraction $\hat p$ of heads exceeds $\frac58$, the midpoint of $\frac12$ and $\frac34$, and "fair" otherwise. We want both kinds of error to have probability at most $0.05$, whichever coin was picked.

1. *Fair coin:* $\hat p$ has mean $\frac12$ and variance $\frac1{4n}$. By Chebyshev (@thm-chebyshev-s-inequality), $\Pr(\hat p\ge\frac58)\le\Pr(|\hat p-\frac12|\ge\frac18)\le\frac{1/(4n)}{1/64}=\frac{16}n$.

2. *Biased coin:* variance $\frac{3/16}n$, so $\Pr(\hat p\le\frac58)\le\frac{(3/16)/n}{1/64}=\frac{12}n$.

3. Both are at most $0.05$ once $n\ge320$. So $320$ tosses certainly suffice.

Chebyshev is pessimistic. With the normal approximation (central limit theorem), the error for the fair coin is about $\Pr\bigl(Z\ge\frac{1/8}{1/(2\sqrt n)}\bigr)=\Pr(Z\ge\frac{\sqrt n}4)$, which is $0.05$ when $\frac{\sqrt n}4\approx1.645$, i.e. $n\approx44$; the biased coin needs slightly fewer. So in practice about $44$ tosses are enough.
:::

::: {.solution for="prob-run-of-heads-code" status="draft"}
```{.python}
import random


def mean_flips_until_run(k, trials, rng):
    """Monte Carlo estimate of the expected number of fair coin flips until
    k heads in a row first appear. rng is a random.Random; use rng.random()."""
    total = 0
    for _ in range(trials):
        flips = run = 0
        while run < k:
            flips += 1
            run = run + 1 if rng.random() < 0.5 else 0
        total += flips
    return total / trials
```

1. One trial tosses until the current run of heads reaches $k$: a head adds one to the run, a tail resets it to $0$. The number of tosses is one sample of $T$.
2. The trials are independent, so the sample mean has mean $E[T]$ and variance $\operatorname{Var}(T)/\text{trials}$ (@prp-sample-mean). For $k=3$, $\operatorname{Var}(T)=142$, so $20\,000$ trials give a standard error of about $0.08$.
3. For $k=0$ no toss is needed and the estimate is exactly $0$.
:::

::: {.solution for="prob-mit6041f10-9-q2" status="draft"}
Let $a=\sigma^2/c^2\in(0,1]$ and let
$$X=\begin{cases}\mu-c&\text{with probability }a/2,\\\mu&\text{with probability }1-a,\\\mu+c&\text{with probability }a/2.\end{cases}$$

1. By symmetry $E[X]=\mu$.

2. $\mathrm{Var}(X)=c^2\cdot\frac a2+c^2\cdot\frac a2=ac^2=\sigma^2$.

3. $|X-\mu|\ge c$ exactly when $X\ne\mu$, which has probability $a=\sigma^2/c^2$: equality in Chebyshev's inequality.
:::
