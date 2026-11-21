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

::: {#fig-indicator-variables-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0) rectangle (0.75,1.6);
\node[tick, below] at (0.375,0) {$I_1=0$};
\node[dot] at (0.375,0.3) {};
\node[dot] at (0.375,0.75) {};
\draw[hl cell] (0.9,0) rectangle (1.65,1.6);
\node[tick, below] at (1.275,0) {$I_2=1$};
\draw[cell frame] (1.8,0) rectangle (2.55,1.6);
\node[tick, below] at (2.175,0) {$I_3=0$};
\node[dot] at (2.175,0.3) {};
\draw[cell frame] (2.7,0) rectangle (3.45,1.6);
\node[tick, below] at (3.075,0) {$I_4=0$};
\node[dot] at (3.075,0.3) {};
\node[dot] at (3.075,0.75) {};
\draw[hl cell] (3.6,0) rectangle (4.35,1.6);
\node[tick, below] at (3.975,0) {$I_5=1$};
\draw[cell frame] (4.5,0) rectangle (5.25,1.6);
\node[tick, below] at (4.875,0) {$I_6=0$};
\node[dot] at (4.875,0.3) {};
\end{tikzpicture}
\end{center}
```

Six balls in six bins: the empty bins (highlighted) have indicator $1$, and the number of empty bins is $I_1+\dots+I_6=3$ here; its mean is $6(5/6)^6\approx2.0$

:::

::: {#exm-roulette .example name="Roulette" level="easy"}
A roulette wheel has $38$ slots: $18$ red, $18$ black and $2$ green. Betting \$1 on black wins \$1 with probability $\frac{18}{38}$ and loses \$1 otherwise, so one game has expected winnings
$$1\cdot\frac{18}{38}+(-1)\cdot\frac{20}{38}=-\frac1{19}.$$
By linearity, $n$ games have expected winnings $-\frac n{19}$: about $-\$53$ over $1000$ games. The two green slots give the casino its edge.
:::

::: {#exm-two-dice-by-linearity .example name="Two dice again" level="easy"}
The total of two dice is $Y_1+Y_2$, where $Y_i$ is the score on die $i$ and $E[Y_i]=\frac72$. By linearity its expectation is $7$, with no need for its distribution.
:::
