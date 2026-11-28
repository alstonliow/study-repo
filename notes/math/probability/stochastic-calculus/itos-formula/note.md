---
title: "Integration by Parts and Itô's Formula"
sources: [camiii-sc-3]
requires: [math/probability/stochastic-calculus/ito-integral]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Stochastic Calculus and Applications (lecture notes), Section 3.5, in our own wording; proofs written out in steps. -->

::: {#thm-stochastic-integration-by-parts .theorem name="Integration by parts"}

For continuous semi-martingales $X,Y$,
$$X_tY_t-X_0Y_0=\int_0^tX_s\,dY_s+\int_0^tY_s\,dX_s+\langle X,Y\rangle_t .$$

:::

::: {.proof}

1. For a subdivision with points $s_i=i2^{-n}\wedge t$ the algebraic identity $X_{s_i}Y_{s_i}-X_{s_{i-1}}Y_{s_{i-1}}=X_{s_{i-1}}(Y_{s_i}-Y_{s_{i-1}})+Y_{s_{i-1}}(X_{s_i}-X_{s_{i-1}})+(X_{s_i}-X_{s_{i-1}})(Y_{s_i}-Y_{s_{i-1}})$ holds.

2. Sum over $i$. The first two sums converge u.c.p. to the stochastic integrals by @prp-integral-riemann-sums, and the last sum to $\langle X,Y\rangle_t$ by @prp-covariation-properties.

:::

The term $\langle X,Y\rangle$ is the *Itô correction*; it is absent for finite variation processes.

::: {#thm-ito-formula .theorem name="Itô's formula"}

Let $X=(X^1,\dots,X^p)$ be continuous semi-martingales and $f\in C^2(\mathbb R^p)$. Then, almost surely,
$$f(X_t)=f(X_0)+\sum_{i=1}^p\int_0^t\frac{\partial f}{\partial x^i}(X_s)\,dX^i_s+\frac12\sum_{i,j=1}^p\int_0^t\frac{\partial^2f}{\partial x^i\partial x^j}(X_s)\,d\langle X^i,X^j\rangle_s .$$
In particular $f(X)$ is a semi-martingale.

:::

::: {.proof}

1. *Polynomials.* The formula holds for constants. Suppose it holds for $f$; apply @thm-stochastic-integration-by-parts to $g(x)=x_kf(x)$, i.e. to the product of the semi-martingales $X^k$ and $f(X)$. Substituting the formula for $f(X)$ and using $\langle X^k,\int g\,dX^i\rangle=\int g\,d\langle X^k,X^i\rangle$ shows it holds for $g$. By induction it holds for all polynomials.

2. *Approximation.* By stopping, assume $X$ and $\langle X^i,X^j\rangle$ stay in a compact set $K$. By Weierstrass' theorem (applied to $f$ and its first two derivatives) choose polynomials $f_m\to f$ in $C^2(K)$.

3. Each term of Itô's formula for $f_m$ converges u.c.p. to the corresponding term for $f$, by uniform convergence of the derivatives and stochastic dominated convergence (@prp-stochastic-dominated-convergence). Hence the formula holds for $f$.

:::

::: {#exm-ito-brownian-square .example name="B² − t as a stochastic integral"}

For a standard Brownian motion, $f(x)=x^2$ gives $B_t^2=2\int_0^tB_s\,dB_s+t$, i.e.
$$B_t^2-t=2\int_0^tB_s\,dB_s,$$
a continuous local martingale (in fact a martingale), recovering @prp-brownian-martingales with no computation.

:::

::: {#exm-ito-martingales .example name="Martingales from space-time functions"}

For a $d$-dimensional Brownian motion $B$ and $f\in C^{1,2}$, apply Itô's formula to $(t,B^1,\dots,B^d)$ with $d\langle B^i,B^j\rangle=\delta_{ij}\,dt$:
$$f(t,B_t)-f(0,B_0)-\int_0^t\Big(\frac\partial{\partial s}+\frac12\Delta\Big)f(s,B_s)\,ds=\sum_{i=1}^d\int_0^t\frac{\partial f}{\partial x^i}(s,B_s)\,dB^i_s$$
is a continuous local martingale. This proves in general the statement that @sec-math-probability-brownian-motion-harmonic-functions-and-dirichlet-problem explains in discrete time.

:::

::: {#rmk-differential-notation .remark name="Differential notation"}

Itô's formula is often written $df(X)=\sum_if_i(X)\,dX^i+\frac12\sum_{ij}f_{ij}(X)\,d\langle X^i,X^j\rangle$. Writing $dX\,dY=d\langle X,Y\rangle$ with $(dB)^2=dt$, $dB\,dt=0$, $(dt)^2=0$ turns the computation into a second-order Taylor expansion in which only the products of martingale increments survive.

:::

::: {#fig-itos-formula-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-0.2,0) -- (4.2,0);
\draw[emph] plot[domain=0.3:3.7,samples=20] (\x,{0.3*(\x-2)*(\x-2)+0.2});
\node[small vertex] at (1.0,0.5) {};
\draw[hl, dashed] (0.2,1.22) -- (2.2,-0.02);
\node[tick] at (1.0,-0.3) {$X_s$};
\node[lab, text=accent] at (3.2,1.9) {$\tfrac12f''(X_s)(\Delta X)^2$};
\node[lab] at (3.2,1.4) {$\to\tfrac12f''\,d\langle X\rangle$};
\end{tikzpicture}
\end{center}
```

Since $(\Delta B)^2\approx\Delta t$ is of first order in time, the second-order Taylor term $\tfrac12f''(X)(\Delta X)^2$ of $f(X)$ does not vanish in the limit; it is the Itô correction.

:::
