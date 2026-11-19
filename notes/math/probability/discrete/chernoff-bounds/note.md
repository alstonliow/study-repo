---
title: "Chernoff Bounds"
sources: [mcs-19.6, eecs126-1]
requires: [math/probability/discrete/concentration-inequalities]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Section 19.6, in our own wording; the example is our own; proofs written out in steps. -->

Markov's and Chebyshev's inequalities (@thm-markov-inequality, @thm-chebyshev-s-inequality) give tail bounds that decay polynomially. For a sum of many small independent variables, the tail decays exponentially.

::: {#thm-chernoff-bound .theorem name="Chernoff bound"}

Let $T_1,\dots,T_n$ be mutually independent random variables with $0\le T_i\le1$, and $T=\sum_iT_i$. For every $c\ge1$,
$$\Pr\bigl(T\ge c\,E[T]\bigr)\le e^{-\beta(c)\,E[T]},\qquad\beta(c)=c\ln c-c+1.$$

:::

::: {.proof}

1. If $c=1$, the bound is $e^0=1$. Let $c>1$. The function $t\mapsto c^t$ is increasing, so by Markov's inequality applied to the non-negative variable $c^T$,
   $$\Pr\bigl(T\ge cE[T]\bigr)=\Pr\bigl(c^T\ge c^{cE[T]}\bigr)\le\frac{E[c^T]}{c^{cE[T]}}.$$

2. For $0\le t\le1$, convexity of $t\mapsto c^t$ gives $c^t\le1+(c-1)t$ (the chord from $(0,1)$ to $(1,c)$ lies above the graph). So $E[c^{T_i}]\le1+(c-1)E[T_i]\le e^{(c-1)E[T_i]}$, using $1+y\le e^y$.

3. The $T_i$ are mutually independent, so $E[c^T]=\prod_iE[c^{T_i}]\le e^{(c-1)E[T]}$ (@thm-expectation-of-product, extended to $n$ factors).

4. Combining, $\Pr(T\ge cE[T])\le e^{(c-1)E[T]-cE[T]\ln c}=e^{-\beta(c)E[T]}$.

:::

$\beta(c)>0$ for $c>1$ ($\beta(1)=0$ and $\beta'(c)=\ln c>0$), and for example $\beta(2)\approx0.386$, $\beta(3)\approx1.296$.

::: {#exm-chernoff-coin .example name="Many heads"}

Toss a fair coin $1000$ times, with $T$ the number of heads, $E[T]=500$. With $c=1.2$, $\beta(1.2)\approx0.0188$, so
$$\Pr(T\ge600)\le e^{-0.0188\cdot500}\approx8\times10^{-5}.$$
Chebyshev's inequality gives only $\Pr(|T-500|\ge100)\le\frac{250}{100^2}=0.025$ (@exm-markov-vs-chebyshev compares the weaker bounds). The true value is about $1.4\times10^{-10}$.

:::

::: {#cor-murphys-law .corollary name="Murphy's law"}

Let $A_1,\dots,A_n$ be mutually independent events and $T$ the number of them that occur. Then $\Pr(T=0)\le e^{-E[T]}$.

:::

::: {.proof}

$E[T]=\sum_i\Pr(A_i)$ by linearity, and by independence and $1-y\le e^{-y}$,
$$\Pr(T=0)=\prod_i\bigl(1-\Pr(A_i)\bigr)\le\prod_ie^{-\Pr(A_i)}=e^{-E[T]}.$$

:::

If many independent things can go wrong and on average $10$ of them do, then the chance that none does is at most $e^{-10}<5\times10^{-5}$.

::: {#rmk-chernoff-bounds-uses .remark name="Where it is used"}

Chernoff bounds justify random load balancing (a server's load is a sum of many small independent jobs), randomized algorithms that repeat an experiment and take a majority vote, and the sample sizes in polling. They need *mutual* independence and boundedness: pairwise independence is enough for Chebyshev but not for Chernoff.

:::

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Concentration Inequalities", in our own wording; proof written out in steps. -->

::: {#lem-hoeffding .lemma name="Hoeffding's lemma"}

If $a\le X\le b$ and $E[X]=0$, then for every real $s$
$$E\bigl[e^{sX}\bigr]\le e^{s^2(b-a)^2/8}.$$

:::

::: {.proof}

1. By convexity of $x\mapsto e^{sx}$ on $[a,b]$, $e^{sX}\le\frac{b-X}{b-a}e^{sa}+\frac{X-a}{b-a}e^{sb}$. Taking expectations with $E[X]=0$, $E[e^{sX}]\le\frac{b}{b-a}e^{sa}-\frac{a}{b-a}e^{sb}=e^{\psi(u)}$, where $u=s(b-a)$, $\theta=-a/(b-a)\in[0,1]$ and $\psi(u)=-\theta u+\ln(1-\theta+\theta e^u)$.

2. $\psi(0)=0$ and $\psi'(0)=0$. Writing $r=\theta e^u/(1-\theta+\theta e^u)\in[0,1]$, $\psi''(u)=r(1-r)\le\frac14$.

3. By Taylor's theorem $\psi(u)\le\frac{u^2}{8}=\frac{s^2(b-a)^2}{8}$.

:::

::: {#thm-hoeffding-inequality .theorem name="Hoeffding's inequality"}

Let $X_1,\dots,X_n$ be independent with $a_i\le X_i\le b_i$, and $S=\sum_iX_i$. For every $t>0$,
$$\Pr\bigl(S-E[S]\ge t\bigr)\le\exp\Bigl(-\frac{2t^2}{\sum_i(b_i-a_i)^2}\Bigr).$$

:::

::: {.proof}

1. For $s>0$, Markov's inequality applied to $e^{s(S-E[S])}$ gives $\Pr(S-E[S]\ge t)\le e^{-st}E[e^{s(S-E[S])}]$.

2. By independence and @lem-hoeffding applied to each $X_i-E[X_i]\in[a_i-E[X_i],b_i-E[X_i]]$, the expectation is at most $\exp\bigl(s^2\sum_i(b_i-a_i)^2/8\bigr)$.

3. Minimise $-st+s^2c/8$ with $c=\sum_i(b_i-a_i)^2$: at $s=4t/c$ the exponent is $-2t^2/c$.

:::

For $n$ fair coin tosses ($X_i\in\{0,1\}$), $\Pr(\text{heads}\ge\frac n2+t)\le e^{-2t^2/n}$; with $n=1000$ and $t=100$ this is $e^{-20}\approx2\times10^{-9}$. Unlike @thm-chernoff-bound it needs only boundedness, not non-negativity, and depends on the range rather than the mean.
