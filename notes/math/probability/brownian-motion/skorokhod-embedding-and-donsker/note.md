---
title: "Skorokhod Embedding and Donsker's Invariance Principle"
sources: [camiii-ap-5]
requires: [math/probability/brownian-motion/strong-markov-and-reflection, math/probability/measure-theoretic/strong-law-of-large-numbers]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 5.4, in our own wording; proofs written out in steps. -->

Every random walk with finite variance can be read off a Brownian path at suitable stopping times. This *embedding* turns the law of large numbers for the stopping times into uniform closeness of the rescaled random walk to Brownian motion: Donsker's invariance principle, the functional central limit theorem.

::: {#lem-two-sided-exit .lemma name="Two-sided exit"}

For standard one-dimensional Brownian motion and $x,y>0$, with $T_a$ the hitting time of $a$,

$$
\Pr_0(T_{-x}<T_y)=\frac y{x+y},\qquad E_0[T_{-x}\wedge T_y]=xy.
$$

:::

::: {.proof}

1. $B$ stopped at $T=T_{-x}\wedge T_y$ is a bounded martingale (values in $[-x,y]$), and $T<\infty$ a.s. Optional stopping: $0=E[B_T]=-x\Pr(T_{-x}<T_y)+y(1-\Pr(T_{-x}<T_y))$, which gives the first formula.

2. $B_t^2-t$ is a martingale. Optional stopping at $T\wedge n$ gives $E[B_{T\wedge n}^2]=E[T\wedge n]$; letting $n\to\infty$ (bounded convergence on the left, monotone on the right) $E[T]=E[B_T^2]=x^2\frac y{x+y}+y^2\frac x{x+y}=xy$.

:::

::: {#thm-skorokhod-embedding .theorem name="Skorokhod embedding"}

Let $\mu$ be a probability measure on $\mathbb R$ with mean $0$ and variance $\sigma^2$. There exist a filtered probability space carrying a standard Brownian motion $B$ and stopping times $0=T_0\le T_1\le\dots$ such that $S_n=B_{T_n}$ satisfy:

1. $(T_n)$ is a random walk whose steps $T_{n+1}-T_n$ have mean $\sigma^2$;
2. $(S_n)$ is a random walk with step law $\mu$.

:::

::: {.proof}

1. *Splitting $\mu$.* Assume first $\mu(\{0\})=0$. Let $\mu^\pm(A)=\mu(\pm A)$ for $A\subseteq(0,\infty)$ and define a probability measure on $(0,\infty)^2$ by $d\nu(x,y)=C(x+y)\,d\mu^-(x)\,d\mu^+(y)$. Since $\mu$ has mean zero, $\int x\,d\mu^-=\int y\,d\mu^+=:m$, and $\int(x+y)\,d\mu^-d\mu^+=m\,\mu^+(0,\infty)+m\,\mu^-(0,\infty)=m$. So $C=1/m$ and $C\int x\,d\mu^-=C\int y\,d\mu^+=1$. (An atom at $0$ is handled by taking $T=0$ with probability $\mu(\{0\})$ and otherwise embedding $\mu$ conditioned on $\mathbb R\setminus\{0\}$; the mean of $T$ is still $\sigma^2$.)

2. *Construction.* Take $B$ and independent i.i.d. pairs $(X_n,Y_n)\sim\nu$; let $\mathcal F_t=\sigma(\text{all }(X_n,Y_n),\mathcal F^B_t)$ and $T_0=0$, $T_{n+1}=\inf\{t\ge T_n:B_t-B_{T_n}\in\{-X_{n+1},Y_{n+1}\}\}$. By the strong Markov property it is enough to treat $n=1$; write $T=T_1$, $(X,Y)=(X_1,Y_1)$.

3. *Law of $B_T$.* Conditionally on $(X,Y)=(x,y)$, @lem-two-sided-exit gives $\Pr(B_T=y)=\frac x{x+y}$, so for $A\subseteq(0,\infty)$,
$$
\Pr(B_T\in A)=\int\frac x{x+y}\mathbf 1_{y\in A}\,C(x+y)\,d\mu^-(x)\,d\mu^+(y)=\mu^+(A)\cdot C\int x\,d\mu^-(x)=\mu^+(A).
$$
The same for $A\subseteq(-\infty,0)$ gives $\mu^-$. So $B_T\sim\mu$.

4. *Mean of $T$.* $E[T]=E[XY]=\int xy\,d\nu=C\int(x^2y+xy^2)\,d\mu^-d\mu^+=\int x^2d\mu^-+\int y^2d\mu^+=\sigma^2$, using $C\int y\,d\mu^+=1=C\int x\,d\mu^-$.

:::

::: {#thm-donsker .theorem name="Donsker's invariance principle"}

Let $X_1,X_2,\dots$ be i.i.d. with mean $0$ and variance $1$, $S_n=X_1+\dots+X_n$, and let $S_t$ be the linear interpolation $S_t=(1-\{t\})S_{\lfloor t\rfloor}+\{t\}S_{\lfloor t\rfloor+1}$. Define $S^{[N]}_t=N^{-1/2}S_{tN}$, $t\in[0,1]$. Then $S^{[N]}$ converges in distribution (as a random element of $C[0,1]$ with the uniform metric) to standard Brownian motion on $[0,1]$.

:::

::: {.proof}

1. Let $B$ be a Brownian motion; by scaling, $B^{(N)}_t=N^{1/2}B_{t/N}$ is also one. Apply @thm-skorokhod-embedding (with $\mu=$ law of $X_1$, $\sigma=1$) to $B^{(N)}$ to get stopping times $T^{(N)}_n$, and let $S^{(N)}_n=B^{(N)}_{T^{(N)}_n}$, interpolated linearly. Then $S^{(N)}$ has the law of $S$, and $(T^{(N)}_n)\sim(T^{(1)}_n)$.

2. Rescale: $\tilde S^{(N)}_t=N^{-1/2}S^{(N)}_{tN}$ (same law as $S^{[N]}$) and $\tilde T^{(N)}_n=T^{(N)}_n/N$. At $t=n/N$, $\tilde S^{(N)}_{n/N}=N^{-1/2}B^{(N)}_{T^{(N)}_n}=B_{\tilde T^{(N)}_n}$. So $\tilde S^{(N)}$ is the Brownian path $B$ read at the random times $\tilde T^{(N)}_n$ instead of the deterministic times $n/N$.

3. *Times are nearly regular.* By the strong law of large numbers, $T^{(1)}_n/n\to1$ a.s., hence $\frac1N\sup_{n\le N}|T^{(1)}_n-n|\to0$ a.s., so for each $\delta>0$, $\Pr\big(\sup_{n\le N}|\tilde T^{(N)}_n-\tfrac nN|\ge\delta\big)\to0$.

4. For $t\in[\frac nN,\frac{n+1}N]$, $\tilde S^{(N)}_t=B_u$ for some $u$ between $\tilde T^{(N)}_n$ and $\tilde T^{(N)}_{n+1}$ (linear interpolation of values of a continuous path). On the event of step 3, $|t-u|\le\delta+\frac1N$. Hence
$$
\{\|\tilde S^{(N)}-B\|_\infty>\varepsilon\}\subseteq\Big\{\exists n\le N:\ \big|\tilde T^{(N)}_n-\tfrac nN\big|>\delta\Big\}\cup\Big\{\exists\,t,u\in[0,\tfrac{N+1}{N}]:\ |t-u|<\delta+\tfrac1N,\ |B_t-B_u|>\varepsilon\Big\}.
$$
The first event has probability $\to0$ by step 3. The second has probability $<\varepsilon'$ for $N$ large and $\delta$ small, because $B$ has uniformly continuous paths on compact intervals.

5. So $\tilde S^{(N)}\to B$ uniformly in probability, hence in distribution; as $\tilde S^{(N)}\sim S^{[N]}$, $S^{[N]}\Rightarrow B$.

:::

::: {#fig-skorokhod-embedding-and-donsker-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (8.4,0) node[lab, right] {$t$};
\draw[faint] (0,-1.4) -- (0,1.8);
\draw[emph] (0,0) -- (0.6,0.5) -- (1.2,0.2) -- (1.9,0.9) -- (2.8,0.3) -- (3.5,1.2) -- (4.4,0.8) -- (5.3,1.5) -- (6.2,1.0) -- (7.2,1.6) -- (8,1.3);
\foreach \x/\y in {1.2/0.2, 2.8/0.3, 4.4/0.8, 6.2/1.0} {\node[small vertex, fill=accentLight, draw=accent] at (\x,\y) {};}
\draw[hl] (0,0) -- (1.2,0.2) -- (2.8,0.3) -- (4.4,0.8) -- (6.2,1.0);
\node[tick] at (1.2,-0.3) {$T_1$};
\node[tick] at (2.8,-0.3) {$T_2$};
\node[tick] at (4.4,-0.3) {$T_3$};
\node[tick] at (6.2,-0.3) {$T_4$};
\node[lab, text=accent] at (3.6,2.2) {$S_n=B_{T_n}$: the walk lives on the Brownian path};
\end{tikzpicture}
\end{center}
```

The random walk $S_n$ is the Brownian path sampled at stopping times $T_n$ with mean spacing $\sigma^2$ (here $1$); by the law of large numbers $T_n\approx n$, so after rescaling the walk is uniformly close to the Brownian path.

:::

::: {#rmk-donsker-consequences .remark name="Why Donsker matters"}

Donsker gives the central limit theorem for functionals of the whole path: if $F:C[0,1]\to\mathbb R$ is continuous, then $F(S^{[N]})\Rightarrow F(B)$. With $F=\sup$, the maximum of a random walk, scaled by $\sqrt N$, converges to $S_1=\sup_{t\le1}B_t$, with the law of $|B_1|$ (@cor-reflection-maximum). The embedding argument also explains why one cannot *construct* Brownian motion this way: the proof of the embedding already uses a Brownian motion.

:::
