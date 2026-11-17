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

::: {#rmk-secret-sharing-why-finite .remark name="Why a finite field"}

The scheme would also reconstruct over the real numbers, but there "no information" cannot be made precise and calculations would be inexact. Over $\mathrm{GF}(q)$ every value is exact, and the $q$ possible secrets can be counted.

:::
