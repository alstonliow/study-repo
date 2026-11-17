---
title: "Correcting General Errors"
sources: [cs70-9]
requires: [math/discrete/polynomials/erasure-codes]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 9 (cs70-9), in our own wording; proofs written out in steps. -->

## The Berlekamp–Welch decoder

::: {#def-reed-solomon-general .definition name="Code for general errors"}

Now up to $k$ of the transmitted characters may be *changed*, and the receiver does not know which. With $P$ as in @def-erasure-code, send $c_j=P(j)$ for $j=1,\dots,n+2k$ (so $q>n+2k$). The receiver gets $r_1,\dots,r_{n+2k}$, with $r_i=P(i)$ except at the at most $k$ *error positions* $e_1,\dots,e_k$.

:::

::: {#prp-general-errors-unique .proposition name="The message is determined"}

$P$ is the only polynomial of degree at most $n-1$ that agrees with the received values in at least $n+k$ positions.

:::

::: {.proof}

$P$ agrees with $r$ in at least $n+k$ positions. If $P'$ also does, the two sets of positions have at least $(n+k)+(n+k)-(n+2k)=n$ positions in common, where $P'(i)=r_i=P(i)$. Two polynomials of degree at most $n-1$ that agree at $n$ points are equal (@thm-interpolation).

:::

::: {#def-error-locator .definition name="Error-locator polynomial"}

$E(x)=(x-e_1)(x-e_2)\cdots(x-e_k)$, of degree $k$ with leading coefficient $1$. (If there are fewer than $k$ errors, use any further positions.) The receiver does not know $E$, but $P(i)E(i)=r_iE(i)$ for every $i$: where there is no error $P(i)=r_i$, and at an error $E(i)=0$.

:::

::: {#thm-berlekamp-welch .theorem name="Berlekamp–Welch decoding"}

Let $Q(x)=P(x)E(x)$, of degree at most $n+k-1$. Write $Q$ with $n+k$ unknown coefficients and $E(x)=x^k+b_{k-1}x^{k-1}+\cdots+b_0$ with $k$ unknown coefficients. The $n+2k$ conditions
$$Q(i)=r_iE(i),\qquad i=1,\dots,n+2k,$$
are linear equations in these $n+2k$ unknowns. They have a solution, and for every solution $(Q',E')$, $E'$ divides $Q'$ and $Q'/E'=P$.

:::

::: {.proof}

1. **A solution exists:** the true $Q=PE$ and $E$ satisfy every condition, as noted in @def-error-locator.

2. **Every solution gives $P$.** Let $(Q',E')$ be any solution. For each $i$, multiply $Q'(i)=r_iE'(i)$ by $E(i)$ and $Q(i)=r_iE(i)$ by $E'(i)$: both $Q'(i)E(i)$ and $Q(i)E'(i)$ equal $r_iE(i)E'(i)$.

3. So the polynomials $Q'E$ and $QE'$, each of degree at most $n+2k-1$, agree at $n+2k$ points, and by @thm-interpolation they are equal: $Q'E=QE'=PEE'$.

4. $E$ and $E'$ have leading coefficient $1$, so they are not zero, and we can cancel $E$: $Q'=PE'$. (Cancelling is allowed because in $\mathrm{GF}(q)$ a product of non-zero polynomials is non-zero: compare leading coefficients.) Hence $Q'/E'=P$.

:::

::: {#rmk-reed-solomon-not-unique .remark name="The solution need not be unique"}

If fewer than $k$ errors occur, the equations can have several solutions $(Q',E')$, for example one for each choice of a spare "error" position. By the theorem every one of them gives the same quotient $P$, so this does no harm.

:::

## Distance

::: {#def-hamming-distance .definition name="Hamming distance, minimum distance"}

The *Hamming distance* $d(s,r)$ between two strings of the same length is the number of positions where they differ. The *minimum distance* of a code is the smallest Hamming distance between the codewords of two different messages.

:::

::: {#rmk-reed-solomon-distance-meaning .remark name="What distance buys"}

A code of minimum distance $k+1$ can, in principle, recover from $k$ erasures: filling in the erased positions can produce only one codeword. A code of minimum distance $2k+1$ can recover from $k$ general errors: a received string within distance $k$ of a codeword is at distance at least $k+1$ from every other codeword, so the nearest codeword is unique.

:::

::: {#thm-reed-solomon-distance .theorem name="Minimum distance of the code"}

The code that sends $n$ message characters as $n+2k$ values of $P$ has minimum distance exactly $2k+1$.

:::

::: {.proof}

1. **At most $2k+1$.** Take two messages that differ only in the last character. Their polynomials agree at $1,\dots,n-1$, so their codewords agree in the first $n-1$ positions and differ in at most $n+2k-(n-1)=2k+1$.

2. **At least $2k+1$.** Suppose two different messages had codewords at distance at most $2k$. The codewords would agree in at least $n$ positions, so the two polynomials of degree at most $n-1$ would agree at $n$ points and be equal (@thm-interpolation). Then the messages, which are their values at $1,\dots,n$, would be equal, a contradiction.

:::
