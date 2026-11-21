---
title: "Laws, Distribution Functions and Skorokhod Representation"
sources: [camii-pm-2, camii-pm-3]
requires: [math/probability/measure-theoretic/probability-spaces-and-independence, math/analysis/measure-theory/product-measures, math/probability/continuous/modes-of-convergence]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Sections 2.3, 2.4 (second half) and the end of 3.5, in our own wording; proofs written out in steps. Convergence in distribution is defined in math/probability/continuous/modes-of-convergence (def-convergence-in-distribution). -->

::: {#def-law-random-variable .definition name="Random variable, law" generalizes="def-random-variable"}

A *random variable* with values in a measurable space $(G,\mathcal G)$ is a measurable map $X:\Omega\to G$ on a probability space $(\Omega,\mathcal F,\Pr)$. Its *law* (distribution) is the image measure $\mu_X=\Pr\circ X^{-1}$ on $\mathcal G$ (@def-image-measure). For real $X$, the *distribution function* is $F_X(x)=\Pr(X\le x)=\mu_X((-\infty,x])$.

:::

By @thm-uniqueness-of-extension, applied to the π-system of half-lines, $F_X$ determines $\mu_X$. It is non-decreasing, right-continuous (continuity from above), and tends to $0$ at $-\infty$ and $1$ at $+\infty$ (continuity from below and above). Any function with these four properties is called a *distribution function*.

::: {#thm-distribution-function-realised .theorem name="Every distribution function is the law of a random variable"}

Let $F$ be a distribution function. On $\Omega=(0,1)$ with Lebesgue measure, the random variable

$$
X(\omega)=\inf\{x\in\mathbb R:\ \omega\le F(x)\}
$$

has $F_X=F$. Hence there is a unique Borel probability measure with distribution function $F$.

:::

::: {.proof}

1. By @lem-generalised-inverse (with $g=F$, $I=(0,1)$), $X$ is a non-decreasing, left-continuous, hence Borel, function on $(0,1)$ with $X(\omega)\le x\iff\omega\le F(x)$.

2. So $\Pr(X\le x)=\lambda\big((0,F(x)]\cap(0,1)\big)=F(x)$.

3. The law of $X$ is a probability measure with distribution function $F$; uniqueness is the remark before the theorem.

:::

::: {#fig-distribution-functions-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (5.4,0) node[lab, right] {$x$};
\draw[->] (0,-0.2) -- (0,3.3) node[lab, above] {};
\draw[emph] (0.000,0.150) -- (1.500,0.900);
\draw[emph] (1.500,1.600) -- (2.600,1.600) -- (4.000,2.600) -- (5.000,2.800);
\fill (1.5,1.6) circle (1.8pt);
\draw[fill=white] (1.5,0.9) circle (1.8pt);
\draw[faint, dashed] (0,2.8) -- (5.0,2.8);
\node[lab, left] at (0,2.8) {$1$};
\draw[hl] (-0.15,1.25) -- (0.15,1.25);
\node[lab, left] at (-0.15,1.25) {$\omega$};
\draw[faint, dashed] (0,1.25) -- (1.5,1.25) -- (1.5,0) node[lab, below] {$X(\omega)$};
\draw[hl] (-0.15,2.2) -- (0.15,2.2);
\node[lab, left] at (-0.15,2.2) {$\omega'$};
\draw[faint, dashed] (0,2.2) -- (3.44,2.2) -- (3.44,0) node[lab, below] {$X(\omega')$};
\node[lab] at (4.6,2.45) {$F$};
\end{tikzpicture}
\end{center}
```

The inverse transform: a uniform $\omega\in(0,1)$ is sent to the first $x$ with $F(x)\ge\omega$. All $\omega$ in the gap of a jump go to the jump point, which therefore gets probability equal to the jump.

:::

This is the *inverse transform method* used to simulate any distribution from a uniform random number.

::: {#thm-iid-sequence-exists .theorem name="Independent sequences exist"}

On $((0,1),\mathcal B,\lambda)$ there are independent random variables $Y_1,Y_2,\dots$ with any prescribed distribution functions $F_1,F_2,\dots$.

:::

::: {.proof}

1. Write $\omega=\sum_{n\ge1}\omega_n2^{-n}$, forbidding expansions ending in all zeros. Each $R_n(\omega)=\omega_n$ is a finite sum of indicators of dyadic intervals, hence measurable, and $\Pr(R_1=a_1,\dots,R_n=a_n)=2^{-n}$, since this event is a dyadic interval of length $2^{-n}$. So $R_1,R_2,\dots$ are independent fair bits.

2. Split $\mathbb N$ into infinitely many disjoint infinite sets $I_1,I_2,\dots$ (for example by the power of $2$ dividing $n$) and put $U_j=\sum_{k\ge1}R_{i_{j,k}}2^{-k}$, where $i_{j,1}<i_{j,2}<\cdots$ lists $I_j$.

3. The $U_j$ are independent by @cor-independence-grouping. Each $U_j$ is uniform on $(0,1)$: its first $m$ binary digits are independent fair bits, so $\Pr(U_j\le k2^{-m})=k2^{-m}$ for dyadic points, and right-continuity extends this to all $u$.

4. Let $G_j$ be the generalised inverse of $F_j$ from @thm-distribution-function-realised and $Y_j=G_j(U_j)$. Functions of independent variables are independent, and $Y_j$ has distribution function $F_j$.

:::

::: {#prp-independence-product-law .proposition name="Independence means product law"}

Random variables $X_1,\dots,X_n$ with values in $(E_k,\mathcal E_k)$ are independent if and only if the law of $X=(X_1,\dots,X_n)$ is the product $\mu_{X_1}\otimes\dots\otimes\mu_{X_n}$, and if and only if

$$
E\Big[\prod_{k=1}^nf_k(X_k)\Big]=\prod_{k=1}^nE\big[f_k(X_k)\big]\qquad\text{for all bounded measurable }f_k .
$$

:::

::: {.proof}

1. If the $X_k$ are independent, $\mu_X$ and the product measure agree on the π-system of rectangles $A_1\times\dots\times A_n$, both giving $\prod_k\Pr(X_k\in A_k)$. They are probability measures, so they are equal (@thm-uniqueness-of-extension).

2. If $\mu_X$ is the product measure, Fubini (@thm-fubini) factorises $\int\prod_kf_k(x_k)\,\mu_X(dx)$.

3. Taking $f_k=\mathbf 1_{A_k}$ in the product formula gives independence.

:::

## Convergence in distribution

A non-decreasing $F$ has at most countably many jumps (each contains a different rational), so the continuity points of $F_X$ are dense; convergence in distribution (@def-convergence-in-distribution) asks for $F_{X_n}(x)\to F_X(x)$ at each of them. The variables need not live on one probability space. The next theorem says that, after a change of space, they can be taken to converge almost surely.

::: {#thm-skorokhod-representation .theorem name="Skorokhod representation theorem"}

If $X_n\to X$ in distribution (real random variables), there are random variables $\tilde X_n,\tilde X$ on a common probability space with $F_{\tilde X_n}=F_{X_n}$, $F_{\tilde X}=F_X$ and $\tilde X_n\to\tilde X$ almost surely.

:::

::: {.proof}

1. Take $\Omega=(0,1)$ with Lebesgue measure and let $\tilde X_n(\omega)=\inf\{x:\ \omega\le F_n(x)\}$, $\tilde X(\omega)=\inf\{x:\ \omega\le F(x)\}$, where $F_n=F_{X_n}$ and $F=F_X$. By @thm-distribution-function-realised they have the right laws.

2. Fix $\omega\in(0,1)$ and let $x<\tilde X(\omega)$ be a continuity point of $F$. Then $F(x)<\omega$, so $F_n(x)<\omega$ for large $n$, i.e. $\tilde X_n(\omega)>x$. Continuity points are dense, so $\liminf_n\tilde X_n(\omega)\ge\tilde X(\omega)$.

3. Now let $\omega<\omega'<1$ and $y>\tilde X(\omega')$ be a continuity point of $F$. Then $F(y)\ge\omega'>\omega$, so $F_n(y)>\omega$ for large $n$, i.e. $\tilde X_n(\omega)\le y$. Hence $\limsup_n\tilde X_n(\omega)\le\tilde X(\omega')$ for every $\omega'>\omega$.

4. If $\tilde X$ is continuous at $\omega$, steps 2 and 3 give $\tilde X_n(\omega)\to\tilde X(\omega)$. $\tilde X$ is monotone, so its discontinuities are countable, a Lebesgue-null set.

:::

So results about convergence in distribution can often be proved by a pointwise argument. For example, if $X_n\to X$ in distribution and $g$ is bounded and continuous, then $E[g(X_n)]=E[g(\tilde X_n)]\to E[g(\tilde X)]=E[g(X)]$ by bounded convergence (@cor-bounded-convergence-finite-measure).
