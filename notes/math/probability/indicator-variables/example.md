<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 15, §4.1 and §4.3 (source keys cs70-15.4.2, cs70-15.4.3, in note.md). -->

::: {#exm-heads-by-indicators .example name="Number of heads" level="easy"}
Toss a coin with heads probability $p$ $n$ times and let $I_i$ indicate "toss $i$ is H". The number of heads is $X=I_1+\cdots+I_n$, so $E[X]=np$, which is $\frac n2$ for a fair coin. This gives the mean of $\mathrm{Bin}(n,p)$ without touching its distribution.
:::

::: {#exm-balls-in-first-bin .example name="Balls in one bin" level="easy"}
Throw $m$ balls into $n$ bins at random. Each ball lands in bin $1$ with probability $\frac1n$, so by @exm-heads-by-indicators the expected number of balls in bin $1$ is $\frac mn$. When $m=n$ it is $1$.
:::

::: {#exm-empty-bins .example name="Empty bins" level="medium"}
Throw $m$ balls into $n$ bins at random and let $Y$ be the number of empty bins. Its distribution is complicated, but with $I_i$ indicating "bin $i$ is empty",
$$E[Y]=\sum_{i=1}^{n}\Pr(\text{bin } i \text{ is empty})=n\Bigl(1-\frac1n\Bigr)^{m}$$
(@exm-balls-and-bins). For $m=n$ and large $n$, $\bigl(1-\frac1n\bigr)^n\approx e^{-1}$, so about $n/e\approx0.368\,n$ bins stay empty: about $368$ when $1000$ balls are thrown into $1000$ bins.
:::

::: {#exm-roulette .example name="Roulette" level="easy"}
A roulette wheel has $38$ slots: $18$ red, $18$ black and $2$ green. Betting \$1 on black wins \$1 with probability $\frac{18}{38}$ and loses \$1 otherwise, so one game has expected winnings
$$1\cdot\frac{18}{38}+(-1)\cdot\frac{20}{38}=-\frac1{19}.$$
By linearity, $n$ games have expected winnings $-\frac n{19}$: about $-\$53$ over $1000$ games. The two green slots give the casino its edge.
:::

::: {#exm-two-dice-by-linearity .example name="Two dice again" level="easy"}
The total of two dice is $Y_1+Y_2$, where $Y_i$ is the score on die $i$ and $E[Y_i]=\frac72$. By linearity its expectation is $7$, with no need for its distribution.
:::
