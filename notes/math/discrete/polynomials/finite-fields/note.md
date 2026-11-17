---
title: "Polynomials over Finite Fields"
sources: [cs70-8]
requires: [math/discrete/polynomials/interpolation, math/discrete/number-theory/modular-arithmetic]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 8 (cs70-8), in our own wording; proofs written out in steps. -->

::: {#def-finite-field .definition name="The finite field GF(p)"}

For a prime $p$, $\mathrm{GF}(p)$ (also written $\mathbb F_p$) is $\{0,1,\dots,p-1\}$ with addition and multiplication modulo $p$. Every non-zero element has an inverse (@thm-inverse, since $\gcd(x,p)=1$ for $0<x<p$), so we can add, subtract, multiply, and divide by any non-zero element.

:::

::: {#fig-finite-fields-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.6cm]
\foreach \i in {0,...,6} {\draw[gridline] (\i,0) -- (\i,6); \draw[gridline] (0,\i) -- (6,\i);
  \node[tick] at (\i,-0.6) {$\i$}; \node[tick] at (-0.6,\i) {$\i$};}
\foreach \x/\y in {0/1,1/2,2/5,3/3,4/3,5/5,6/2} \fill[primary] (\x,\y) circle[pt];
\node[lab] at (3,-1.4) {$x$};
\node[lab] at (-1.6,3) {$P(x)$};
\end{tikzpicture}
\end{center}
```

The polynomial $P(x)=x^2+1$ over $\mathrm{GF}(7)$ is not a curve but a set of $7$ points, one in each column; still, it is determined by any $3$ of them.

:::

::: {#prp-polynomials-mod-p .proposition name="The polynomial facts hold modulo a prime"}

For polynomials with coefficients and values in $\mathrm{GF}(p)$, division with remainder (@thm-polynomial-division), the factor theorem (@thm-factor-theorem), the bound on roots (@thm-at-most-d-roots) and interpolation (@thm-interpolation, with distinct $x_i$ in $\mathrm{GF}(p)$) all hold.

:::

::: {.proof}

Their proofs use only addition, subtraction, multiplication, and division by non-zero numbers, together with the fact that a product of non-zero numbers is non-zero. All of these hold in $\mathrm{GF}(p)$: if $ab\equiv0$ with $a\not\equiv0$, multiplying by $a^{-1}$ gives $b\equiv0$.

:::

::: {#rmk-finite-fields-not-prime .remark name="Why the modulus must be prime"}

Modulo $8$, the polynomial $x^3$ of degree $3$ has the four roots $0,2,4,6$, so @thm-at-most-d-roots fails: $2$ has no inverse modulo $8$, and $2\cdot4\equiv0$. Over the integers, interpolation fails too: no line with integer coefficients passes through $(0,0)$ and $(2,1)$. (The bound on roots does hold for integers, since integers are real numbers.)

:::

::: {#prp-counting-polynomials .proposition name="Counting polynomials through given points"}

Over $\mathrm{GF}(p)$, let $0\le j\le d+1$. Through $j$ points with distinct $x$-coordinates there pass exactly $p^{\,d+1-j}$ polynomials of degree at most $d$.

:::

::: {.proof}

1. Choose $d+1-j$ further distinct $x$-coordinates (possible when $d+1\le p$). Each choice of values at them, $p^{\,d+1-j}$ choices, gives $d+1$ points and so, by @thm-interpolation, exactly one polynomial.

2. Different choices give different polynomials, since the values differ somewhere; and every polynomial through the $j$ points arises, from its own values at the new coordinates.

:::

::: {#rmk-finite-fields-infinite .remark name="Only finite fields can be counted"}

With $j=0$ there are $p^{d+1}$ polynomials, one for each list of coefficients. Over the real numbers, infinitely many polynomials of degree $d$ pass through $d$ points; counting is possible only because $\mathrm{GF}(p)$ is finite.

:::
