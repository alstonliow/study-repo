---
title: "Erasure Codes"
sources: [cs70-9]
requires: [math/discrete/polynomials/finite-fields]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 9 (cs70-9), in our own wording; proofs written out in steps. -->

::: {#def-erasure-code .definition name="Polynomial erasure code"}

A message of $n$ packets $m_1,\dots,m_n$, each in $\mathrm{GF}(q)$, must survive the loss of up to $k$ packets; the receiver knows which packets were lost. Let $P$ be the polynomial of degree at most $n-1$ with $P(i)=m_i$ for $i=1,\dots,n$ (@thm-interpolation). Send the *codeword* $c_j=P(j)$ for $j=1,\dots,n+k$, which needs $q\ge n+k$.

:::

::: {#thm-erasure-code .theorem name="Recovering from erasures"}

The message can be recovered from any $n$ of the $n+k$ packets. With fewer than $n$ packets it cannot be: there are then several polynomials consistent with what was received.

:::

::: {.proof}

1. Any $n$ received packets are values of $P$ at $n$ distinct points, so by @thm-interpolation they determine $P$, and $m_i=P(i)$.

2. With only $n-1$ packets, @prp-counting-polynomials gives $q$ polynomials of degree at most $n-1$ through them, which give different messages.

:::

::: {#rmk-erasure-codes-optimal .remark name="Optimal"}

So the code is as good as possible: the message is $n$ numbers, and any $n$ of the $n+k$ packets are enough to recover it. A *message* is what the user wants to send; a *codeword* is what is transmitted, with redundancy added.

:::
