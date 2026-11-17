<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 21 (source keys cs70-21, in note.md); all values checked numerically. -->

::: {#exm-geometric-as-hitting-time .example name="Waiting for a switch" level="easy"}
In the two-state chain (@prp-two-state-chain) with $a>0$, let $\beta(i)$ be the mean time to enter state $1$. The first step equations are $\beta(1)=0$ and $\beta(0)=1+(1-a)\beta(0)+a\beta(1)$, so $a\beta(0)=1$ and $\beta(0)=\frac1a$. This is the mean of $\mathrm{Geom}(a)$ (@prp-standard-distributions-1-4): from $0$, each step is a trial that succeeds with probability $a$.
:::

::: {#exm-web-chain-hitting-time .example name="Reaching a page" level="medium"}
In the five-page web of @exm-web-chain-invariant, let $\beta(i)$ be the mean number of clicks to reach $E$ from page $i$:
$$\beta(A)=1+\tfrac12\beta(B)+\tfrac12\beta(D),\quad\beta(B)=1+\beta(C),\quad\beta(C)=1+\beta(A),\quad\beta(D)=1+\tfrac13\beta(A)+\tfrac13\beta(B),\quad\beta(E)=0.$$
The second and third give $\beta(B)=2+\beta(A)$; then $\beta(D)=\frac53+\frac23\beta(A)$; then the first gives $\beta(A)=\frac{17}6+\frac56\beta(A)$. So $\beta(A)=17$, $\beta(B)=19$, $\beta(C)=18$, $\beta(D)=13$.
:::

::: {#exm-two-heads .example name="Two heads in a row" level="medium"}
Flip a fair coin until two heads appear in a row. Use the states $S$ (start), $T$ (last flip tails), $H$ (last flip heads, not yet two) and $E$ (done). The mean number of flips $\beta$ to reach $E$ satisfies
$$\beta(S)=1+\tfrac12\beta(T)+\tfrac12\beta(H),\quad\beta(T)=1+\tfrac12\beta(T)+\tfrac12\beta(H),\quad\beta(H)=1+\tfrac12\beta(T),\quad\beta(E)=0.$$
Substituting the third into the second: $\beta(T)=\frac32+\frac34\beta(T)$, so $\beta(T)=6$, $\beta(H)=4$, and $\beta(S)=1+3+2=6$. On average $6$ flips are needed.
:::

::: {#fig-hitting-times-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.7cm]
\node[vertex] (S) at (0,0) {$S$};
\node[vertex] (T) at (1.6,1) {$T$};
\node[vertex] (H) at (1.6,-1) {$H$};
\node[vertex] (E) at (3.4,-1) {$E$};
\draw[->] (S) -- node[edge label] {$\frac12$} (T);
\draw[->] (S) -- node[edge label] {$\frac12$} (H);
\draw[->] (T) to[loop right] node[edge label] {$\frac12$} (T);
\draw[->] (T) to[bend left=20] node[edge label] {$\frac12$} (H);
\draw[->] (H) to[bend left=20] node[edge label] {$\frac12$} (T);
\draw[->] (H) -- node[edge label] {$\frac12$} (E);
\end{tikzpicture}
\end{center}
```

The chain of @exm-two-heads: $T$ and $H$ record the last flip, and $E$ means two heads in a row.

:::

::: {#exm-dice-sum-eight .example name="Two rolls summing to 8" level="medium"}
Roll a fair die until two consecutive rolls sum to $8$. The states are $S$, the last roll $1,\dots,6$, and $E$. From state $i$, the roll $8-i$ ends the game if it is a possible roll, i.e. if $i\ge2$; from $1$ (and from $S$) no roll ends it. So $\beta(1)=\beta(S)$, and by symmetry $\beta(2)=\dots=\beta(6)=\gamma$. The first step equations become
$$\beta(S)=1+\tfrac16\bigl(\beta(S)+5\gamma\bigr),\qquad \gamma=1+\tfrac16\bigl(\beta(S)+4\gamma\bigr).$$
The first gives $\beta(S)=\frac65+\gamma$; the second gives $\gamma=3+\frac12\beta(S)=\frac{18}5+\frac12\gamma$. So $\gamma=\frac{36}5$ and $\beta(S)=\frac{42}5=8.4$ rolls.
:::

::: {#exm-ladder .example name="A slippery ladder" level="medium"}
On a ladder with $20$ rungs, each step takes you up one rung with probability $p$ and otherwise back to the ground (rung $0$). The mean time $\beta(i)$ from rung $i$ to the top satisfies $\beta(20)=0$ and
$$\beta(i)=1+(1-p)\beta(0)+p\,\beta(i+1)\qquad(0\le i\le19).$$
The solution is
$$\beta(i)=\frac{p^{-20}-p^{-i}}{1-p}.$$
Check: $\beta(20)=0$, and $1+(1-p)\beta(0)+p\beta(i+1)=p^{-20}+\frac{p^{-19}-p^{-i}}{1-p}$, which equals $\frac{p^{-20}-p^{-i}}{1-p}$ because $\frac{p^{-20}-p^{-19}}{1-p}=p^{-20}$. From the ground, $\beta(0)=\frac{p^{-20}-1}{1-p}$: about $72$ steps for $p=0.9$, and about $429$ for $p=0.8$.
:::

::: {#exm-gamblers-ruin .example name="Gambler's ruin" level="hard"}
A gambler bets $1$ on each flip of a coin with $\Pr(\text{heads})=p\ne\frac12$, winning on heads and losing on tails, and stops on reaching $M$ or $0$. Let $\rho=\frac{1-p}p$ and let $\alpha(n)$ be the probability of reaching $M$ before $0$ from fortune $n$.

1. By @thm-first-step-hitting-probability, $\alpha(0)=0$, $\alpha(M)=1$ and $\alpha(n)=(1-p)\alpha(n-1)+p\,\alpha(n+1)$ for $0<n<M$.

2. Write $\alpha(n)=(1-p)\alpha(n)+p\,\alpha(n)$ and subtract: $p\bigl(\alpha(n+1)-\alpha(n)\bigr)=(1-p)\bigl(\alpha(n)-\alpha(n-1)\bigr)$. So the differences $\Delta_n=\alpha(n)-\alpha(n-1)$ satisfy $\Delta_{n+1}=\rho\Delta_n$, hence $\Delta_n=\rho^{n-1}\Delta_1$.

3. Summing, $\alpha(n)=\Delta_1(1+\rho+\dots+\rho^{n-1})=\Delta_1\frac{1-\rho^n}{1-\rho}$. The condition $\alpha(M)=1$ fixes $\Delta_1$, and
   $$\alpha(n)=\frac{1-\rho^n}{1-\rho^M}.$$

With $p=0.48$, $n=10$ and $M=100$ this is about $4\times10^{-4}$. The casino then gains $10$ with probability about $1-4\times10^{-4}$ and loses $90$ otherwise, an expected gain of about $9.96$ per gambler; had the gambler bet all $10$ on one flip, it would have been $0.52\cdot10-0.48\cdot10=0.40$. By the same method (@thm-first-step-hitting-time), the mean duration of the game is
$$\beta(n)=\frac n{1-2p}-\frac M{1-2p}\cdot\frac{1-\rho^n}{1-\rho^M},$$
about $249$ flips here.
:::

::: {#fig-hitting-times-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.8cm]
\foreach \i/\l in {0/0,1/1,2/2,4/M-1,5/M} \node[vertex] (s\i) at (\i,0) {$\l$};
\node[lab] (s3) at (3,0) {$\cdots$};
\foreach \i/\j in {1/2,2/3,3/4,4/5} \draw[->] (s\i) to[bend left=28] node[tick, above] {$p$} (s\j);
\foreach \i/\j in {1/0,2/1,3/2,4/3} \draw[->] (s\i) to[bend left=28] node[tick, below] {$1-p$} (s\j);
\draw[->] (s0) to[loop left] node[edge label] {$1$} (s0);
\draw[->] (s5) to[loop right] node[edge label] {$1$} (s5);
\end{tikzpicture}
\end{center}
```

Gambler's ruin: the fortune moves up with probability $p$ and down with probability $1-p$ until it reaches $0$ or $M$, where it stays.

:::
