---
title: "One-Way Functions and Diffie–Hellman"
sources: [fit1058-cn-7.16, fit1058-cn-7.17, fit1058-cn-7.18]
requires: [math/discrete/number-theory/modular-exponentiation, math/discrete/number-theory/primitive-roots, math/discrete/sequences/big-o]
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: One-way functions; Modular exponentiation with fixed base; Diffie–Hellman key agreement. -->

## One-way functions

::: {#def-one-way-function-informal .definition name="One-way function, informal"}

A function $f$ is *one-way* if it is easy to compute but hard to invert, for almost all inputs.

:::

::: {.remark name="None are proved"}

No function has been *proved* to be one-way; doing so would resolve $P\ne NP$ (@sec-math-discrete-sequences-big-o). Several functions are believed to be one-way and are used as such.

:::

::: {.remark name="Application: password storage"}

Instead of storing each password $P_i$, a system stores $(U_i,f(P_i))$ for a one-way $f$. A login with password $P$ is accepted iff $f(P)=f(P_i)$, which is fast to check. An attacker who steals $f(P_i)$ still faces the inversion problem. This is not encryption: no key is involved, and nobody is meant to recover $P_i$.

:::

## Modular exponentiation with fixed base

::: {#def-modular-exponentiation-with-fixed-base .definition name="Modular exponentiation with fixed base"}

Fix $n\in\mathbb{N}$ and a base $a<n$. The function is $x\longmapsto a^x\bmod n$, for $x<\varphi(n)$.

:::

::: {#def-discrete-logarithm-problem .definition name="Discrete Logarithm problem"}

Fix $n\in\mathbb{N}$ and a primitive root $a$ of $n$. Given $y\in\mathbb{Z}_n^*$, find $x\le\varphi(n)$ with $a^x\equiv y\pmod n$. We write $x=\log_a y$.

:::

::: {#exm-diffie-hellman-1 .example}

With $n=7$ and $a=3$, the table in @sec-math-discrete-number-theory-primitive-roots gives $\log_3 6=3$ and $\log_3 4=4$.

:::

::: {.remark name="Choosing the parameters"}

The base is chosen to be a primitive root because then $a^x$ takes the widest range of values, which maximises the search space for an attacker. Discrete Logarithm is believed to have no fast algorithm, and in practice is about as hard as integer factorisation. Since $\varphi(n)$ is largest when $n$ is prime, the best candidate one-way function uses a large prime $p$ and a primitive root $a$ of $p$.

:::

## Diffie–Hellman key agreement

::: {#def-diffie-hellman-scheme .definition name="Diffie–Hellman scheme"}

The public global parameters are a large prime $p$ and a primitive root $a$ of $p$. Each user picks a private random number $x\in\{1,\dots,p-1\}$ and publishes $y=a^x\bmod p$. Users $A$ and $B$, with private numbers $x_A,x_B$ and public numbers $y_A,y_B$, compute
$$k_{AB} := y_B^{\,x_A}\bmod p, \qquad k_{BA} := y_A^{\,x_B}\bmod p.$$

:::

::: {#prp-dhagree .proposition name="Agreement"}

$k_{AB}=k_{BA}$.

:::

::: {.proof}

In $\mathbb{Z}_p^*$,  $k_{AB}=y_B^{\,x_A}=(a^{x_B})^{x_A}=a^{x_Ax_B}=(a^{x_A})^{x_B}=y_A^{\,x_B}=k_{BA}$.

:::

::: {#exm-diffie-hellman-with-small-numbers .example name="Diffie–Hellman with small numbers"}

Take $p=11$ and $a=2$, a primitive root of $11$ (Exercise 7.17). Alice picks $x_A=3$ and Bob picks $x_B=6$, so $y_A=2^3\bmod11=8$ and $y_B=2^6\bmod11=64\bmod11=9$. They exchange $y_A$ and $y_B$, and compute
$$k_{AB}=9^3\bmod11=729\bmod11=3, \qquad k_{BA}=8^6\bmod11=262144\bmod11=3.$$
Both equal $a^{x_Ax_B}=2^{18}\equiv3\pmod{11}$, which an eavesdropper who sees only $8$ and $9$ cannot easily compute.

:::

::: {.remark name="Agreement, not encryption"}

Diffie–Hellman is a key *agreement* scheme, not a cryptosystem: neither party can use it to send a message of their choosing. The shared $k_{AB}$ is then used as the key of a conventional secret-key cryptosystem. Its value is that no secure channel is needed to set up the shared key, and neither party alone decides it.

:::

::: {#def-diffie-hellman-problem .definition name="Diffie–Hellman problem"}

Given $p$, $a$, $a^{x_A}\bmod p$ and $a^{x_B}\bmod p$, find $a^{x_Ax_B}\bmod p$.

:::

::: {#prp-dhreduce .proposition}

Any algorithm for Discrete Logarithm yields an algorithm for the Diffie–Hellman problem, with only polynomial extra work.

:::

::: {.proof}

Give $p,a,a^{x_A}$ to the Discrete Logarithm algorithm to recover $x_A$. Then compute $(a^{x_B})^{x_A}=a^{x_Ax_B}\bmod p$ by fast modular exponentiation (@sec-math-discrete-number-theory-modular-exponentiation).

:::

::: {.remark name="Open problem"}

Whether the reduction also goes the other way (an efficient algorithm for the Diffie–Hellman problem giving one for Discrete Logarithm) is widely believed but unproven.

:::
