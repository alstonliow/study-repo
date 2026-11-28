---
title: "Brownian Motion: Definition, Wiener's Construction and Invariance"
sources: [camiii-ap-5]
requires: [math/probability/continuous-time/continuous-time-processes, math/probability/measure-theoretic/portmanteau-and-prokhorov]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 5.1, in our own wording; proofs written out in steps. -->

Brownian motion is the continuous-time limit of a random walk: a continuous random path whose increments over disjoint time intervals are independent Gaussians with variance equal to the length of the interval.

::: {#def-brownian-motion .definition name="Brownian motion"}

A continuous process $(B_t)_{t\ge0}$ in $\mathbb R^d$ is a *Brownian motion started at $x$* if

1. $B_0=x$ almost surely;
2. for $s<t$, $B_t-B_s\sim N(0,(t-s)I)$;
3. for $t_1<\dots<t_k$ the variables $B_{t_1},B_{t_2}-B_{t_1},\dots,B_{t_k}-B_{t_{k-1}}$ are independent.

If $x=0$ it is *standard*; we always take standard Brownian motion and write $\mathcal F^B_t=\sigma(B_s:s\le t)$.

:::

::: {#thm-wiener .theorem name="Wiener's theorem"}

Brownian motion exists (on some probability space).

:::

::: {.proof}

*Dimension $1$, time $[0,1]$.* Let $(Z_d)_{d\in D}$ be i.i.d. $N(0,1)$ indexed by the dyadics $D=\bigcup D_n$, $D_n=\{k2^{-n}\}$.

1. *Construction on $D_n$.* Put $B_0=0$, $B_1=Z_1$. Given $B$ on $D_{n-1}$ and $d\in D_n\setminus D_{n-1}$ with neighbours $d^\pm=d\pm2^{-n}$ in $D_{n-1}$, set
$$
B_d=\frac{B_{d^+}+B_{d^-}}2+2^{-(n+1)/2}Z_d .
$$
(The midpoint of the neighbours, plus an independent Gaussian correction.)

2. *Increments are independent Gaussians.* Write $B_{d^+}-B_d=N-N'$ and $B_d-B_{d^-}=N+N'$ with $N=\frac{B_{d^+}-B_{d^-}}2$ and $N'=2^{-(n+1)/2}Z_d$. Both are $N(0,2^{-(n+1)})$, so $\operatorname{cov}(N-N',N+N')=\operatorname{var}N-\operatorname{var}N'=0$, and each increment has variance $2^{-n}$. The vector of increments over $D_n$ is Gaussian (a linear combination of independent Gaussians), so independence follows from vanishing correlations; the remaining pairs involve different $Z$'s and are checked likewise.

3. *Hölder bound.* For $s,t\in D$, $E|B_t-B_s|^p=|t-s|^{p/2}E|N(0,1)|^p<\infty$, i.e. $\|B_t-B_s\|_p=C_p|t-s|^{1/2}$. With $p>2$ and $\beta=\frac12>\frac1p$, Kolmogorov's criterion (@thm-kolmogorov-continuity-criterion) extends $B$ to a continuous process on $[0,1]$, $\alpha$-Hölder for every $\alpha<\frac12$.

4. *Properties persist.* For times $t_i$ and dyadic $t_i^n\to t_i$, the increments $(B_{t^n_2}-B_{t^n_1},\dots)$ are independent $N(0,t^n_{i+1}-t^n_i)$, with characteristic function $\exp(-\frac12\sum(t^n_{i+1}-t^n_i)u_i^2)\to\exp(-\frac12\sum(t_{i+1}-t_i)u_i^2)$. By continuity of paths the increments converge a.s., and by Lévy's theorem the limit has this Gaussian law with independent components. So 2 and 3 hold on $[0,1]$.

5. *Extension.* For $[0,\infty)$ take independent copies $(B^i_t)_{t\in[0,1]}$ and set $B_t=\sum_{i<\lfloor t\rfloor}B^i_1+B^{\lfloor t\rfloor}_{t-\lfloor t\rfloor}$. For $\mathbb R^d$ take $d$ independent coordinates. 

:::

::: {#fig-definition-and-construction-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (8.4,0);
\draw[faint] (0,0) -- (8,1.8);
\foreach \x/\y in {0/0,8/1.8} {\node[small vertex] at (\x,\y) {};}
\draw[emph] (0,0) -- (4,1.5) -- (8,1.8);
\node[small vertex] at (4,1.5) {};
\draw[hl] (0,0) -- (2,0.4) -- (4,1.5) -- (6,1.0) -- (8,1.8);
\node[tick] at (4,-0.3) {$D_1$};
\node[tick] at (2,-0.3) {};
\node[lab, text=accent] at (3.2,2.4) {each level adds midpoints plus a smaller Gaussian correction};
\end{tikzpicture}
\end{center}
```

Level $0$ joins $(0,0)$ to $(1,B_1)$ by a line (faint); level $1$ moves the midpoint by $2^{-1}Z$; level $2$ moves the new midpoints by $2^{-3/2}Z$, and so on. The corrections shrink fast enough for the limit to be continuous.

:::

::: {#lem-brownian-gaussian .lemma name="Brownian motion is a Gaussian process"}

For $0\le t_1<\dots<t_m$ the vector $(B_{t_1},\dots,B_{t_m})$ is Gaussian with $\operatorname{cov}(B_s,B_t)=s\wedge t$.

:::

::: {.proof}

1. The increments are independent Gaussians, so jointly Gaussian; $(B_{t_1},\dots,B_{t_m})$ is their image under an invertible linear map, hence Gaussian.

2. For $s\le t$: $E[B_sB_t]=E[B_s(B_t-B_s)]+E[B_s^2]=0+s$.

:::

::: {#prp-brownian-invariance .proposition name="Invariance properties"}

Let $B$ be a standard Brownian motion in $\mathbb R^d$.

1. *Rotations:* for $U$ orthogonal, $(UB_t)_{t\ge0}$ is a standard Brownian motion.
2. *Scaling:* for $a>0$, $(a^{-1/2}B_{at})_{t\ge0}$ is a standard Brownian motion.
3. *Simple Markov property:* for $s\ge0$, $(B_{t+s}-B_s)_{t\ge0}$ is a standard Brownian motion independent of $\mathcal F^B_s$.
4. *Time inversion:* $X_0=0$, $X_t=tB_{1/t}$ for $t>0$, is a standard Brownian motion.

:::

::: {.proof}

Parts 1–3 are immediate from the definition (the transformed process is continuous, Gaussian and has the right covariance or increments). For 4:

1. For $t>0$ the map $t\mapsto X_t$ is continuous. For $t_1,\dots,t_m>0$, $(X_{t_i})=(t_iB_{1/t_i})$ is a linear image of a Gaussian vector, hence Gaussian, with $\operatorname{cov}(X_s,X_t)=st\,(\tfrac1s\wedge\tfrac1t)=s\wedge t$. So $X$ has the finite-dimensional distributions of Brownian motion on $(0,\infty)$.

2. Continuity at $0$: $(X_q)_{q\in\mathbb Q_{>0}}$ has the law of $(B_q)_{q\in\mathbb Q_{>0}}$, and $\Pr(\lim_{q\downarrow0}B_q=0)=1$ by continuity of $B$. So $\Pr(\lim_{q\downarrow0}X_q=0)=1$, and continuity of $X$ on $(0,\infty)$ extends this to all $t\downarrow0$.

:::

::: {#rmk-brownian-scaling .remark name="A random fractal"}

Scaling shows that zooming in on a Brownian path (time by $a$, space by $a^{1/2}$) gives again a Brownian path: the path is statistically self-similar. Time inversion exchanges the behaviour at $0$ with that at $\infty$, which is why local and long-time properties (next note) are equivalent.

:::
