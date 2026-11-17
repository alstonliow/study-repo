---
title: "Chernoff Bounds"
sources: [mcs-19.6]
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
