---
title: "Secret Sharing"
sources: [cs70-8]
requires: [math/discrete/polynomials/finite-fields]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 8 (cs70-8), in our own wording; proofs written out in steps. -->

::: {#def-shamir-secret-sharing .definition name="Secret sharing with polynomials"}

A secret $s$ is to be shared among $n$ people so that any $k$ of them can recover it. Choose a prime $q$ larger than $s$ and $n$, and work in $\mathrm{GF}(q)$. Choose a polynomial $P$ of degree at most $k-1$ with $P(0)=s$, its other coefficients uniformly at random, and give person $i$ the *share* $P(i)$, for $i=1,\dots,n$.

:::

::: {#thm-secret-sharing .theorem name="Secret sharing works"}

1. Any $k$ people can compute $s$.

2. Any $k-1$ people learn nothing about $s$: for each possible value $b$ of the secret, exactly one polynomial of degree at most $k-1$ is consistent with their shares and with $P(0)=b$.

:::

::: {.proof}

1. $k$ shares are the values of $P$ at $k$ distinct points, so by interpolation (@thm-interpolation, valid in $\mathrm{GF}(q)$ by @prp-polynomials-mod-p) they determine $P$, and then $s=P(0)$.

2. $k-1$ shares give $k-1$ points. Adding the point $(0,b)$ gives $k$ points with distinct $x$-coordinates (the shares are at $1,\dots,n$, never $0$), and by @thm-interpolation exactly one polynomial of degree at most $k-1$ passes through them.

3. So every one of the $q$ possible secrets is consistent with what the $k-1$ people hold, each with exactly one polynomial, and each of those polynomials was equally likely to be chosen. Their shares give them no reason to prefer any value of $s$.

:::

::: {#fig-secret-sharing-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm,y=0.45cm]
\draw[->, muted] (-0.6,0) -- (3.4,0) node[lab, right] {$x$};
\draw[->, muted] (0,-1.5) -- (0,7.5);
\draw[emph, primary, domain=-0.15:3.1, samples=60] plot (\x,{-0.5*\x*\x+(2.5)*\x+0});
\fill[primary] (0,0) circle[pt]; \node[tick, anchor=east, primary] at (-0.12,0) {$s=0$};
\draw[emph, secondary, domain=-0.15:3.1, samples=60] plot (\x,{0.5*\x*\x+(-0.5)*\x+2});
\fill[secondary] (0,2) circle[pt]; \node[tick, anchor=east, secondary] at (-0.12,2) {$s=2$};
\draw[emph, accent, domain=-0.15:3.1, samples=60] plot (\x,{1.5*\x*\x+(-3.5)*\x+4});
\fill[accent] (0,4) circle[pt]; \node[tick, anchor=east, accent] at (-0.12,4) {$s=4$};
\foreach \x/\y in {1/2,2/3} \fill[ink] (\x,\y) circle[pt];
\node[lab, anchor=west] at (1.05,1.2) {shares};
\end{tikzpicture}
\end{center}
```

The idea over the reals, with $k=3$: two shares are matched by a parabola with *every* value at $0$, so two people learn nothing about the secret. A third share fixes the parabola.

:::

::: {#rmk-secret-sharing-why-finite .remark name="Why a finite field"}

The scheme would also reconstruct over the real numbers, but there "no information" cannot be made precise and calculations would be inexact. Over $\mathrm{GF}(q)$ every value is exact, and the $q$ possible secrets can be counted.

:::
