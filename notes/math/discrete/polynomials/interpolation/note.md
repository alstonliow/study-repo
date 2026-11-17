---
title: "Polynomial Interpolation"
sources: [cs70-8, cs70-9]
requires: [math/discrete/polynomials/polynomials-and-roots]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 8 and Note 9 (cs70-8, cs70-9), in our own wording; proofs written out in steps. -->

::: {#thm-interpolation .theorem name="Interpolation"}

Given $d+1$ pairs $(x_1,y_1),\dots,(x_{d+1},y_{d+1})$ with the $x_i$ distinct, there is exactly one polynomial $p$ of degree at most $d$ with $p(x_i)=y_i$ for all $i$.

:::

::: {.proof}

1. **Basis polynomials.** For each $i$ let
   $$\Delta_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j}.$$
   The denominators are non-zero because the $x_j$ are distinct. $\Delta_i$ has degree $d$, $\Delta_i(x_i)=1$, and $\Delta_i(x_j)=0$ for $j\ne i$.

2. **Existence.** $p(x)=\sum_{i=1}^{d+1}y_i\Delta_i(x)$ has degree at most $d$, and at $x_j$ every term vanishes except $y_j\Delta_j(x_j)=y_j$.

3. **Uniqueness.** If $q$ also has degree at most $d$ and $q(x_i)=y_i$ for all $i$, then $r=p-q$ has degree at most $d$ and $d+1$ roots $x_1,\dots,x_{d+1}$. By @thm-at-most-d-roots, $r$ is the zero polynomial, so $p=q$.

:::

::: {#rmk-interpolation-lagrange .remark name="Lagrange interpolation"}

Building $p$ from the $\Delta_i$ is *Lagrange interpolation*. The $\Delta_i$ depend only on the points $x_j$, not on the values $y_j$: they are a basis, and $p$ is the combination with coefficients $y_i$. The idea is the same as in the Chinese Remainder Theorem (@thm-crt), where numbers that are $1$ in one place and $0$ elsewhere are combined.

:::

::: {#rmk-interpolation-linear-system .remark name="Interpolation as a linear system"}

Another way: treat the coefficients $a_0,\dots,a_d$ as unknowns. Each condition $p(x_i)=y_i$ is the linear equation $a_dx_i^d+\cdots+a_1x_i+a_0=y_i$, so we get $d+1$ linear equations in $d+1$ unknowns. @thm-interpolation says that this system always has exactly one solution.

:::

::: {#rmk-interpolation-two-representations .remark name="Coefficients or values"}

A polynomial of degree at most $d$ can be given by its $d+1$ coefficients (the *coefficient representation*) or by its values at $d+1$ fixed points (the *value representation*). Evaluating converts the first into the second, and interpolation converts back.

:::
