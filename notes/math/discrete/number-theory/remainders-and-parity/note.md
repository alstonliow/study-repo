---
title: "Remainders and Parity"
sources: [fit1058-cn-7.3, fit1058-cn-7.4]
requires: []
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: Remainders and the mod operation; Parity. -->

## Remainders and the mod operation

::: {#thm-division .theorem name="Division algorithm"}

For all $n\in\mathbb{Z}$ and $d\in\mathbb{N}$ there exist *unique* $q,r\in\mathbb{Z}$ with
$$n=qd+r, \qquad 0\le r\le d-1.$$

:::

::: {.proof}

**Existence**: The set $S=\{n-kd : k\in\mathbb{Z},\ n-kd\ge0\}$ is nonempty (take $k=-|n|$), so it has a least element $r=n-qd\ge0$. If $r\ge d$, then $r-d=n-(q+1)d$ would be a smaller element of $S$, a contradiction. So $0\le r\le d-1$.

**Uniqueness**: Suppose $n=q_1d+r_1=q_2d+r_2$ with $0\le r_1,r_2\le d-1$. Then $r_1-r_2=(q_2-q_1)d$, so $d\mid(r_1-r_2)$. But $|r_1-r_2|\le d-1<d$, so $r_1-r_2=0$, and then $q_1=q_2$.

:::

::: {#def-the-mod-operation .definition name="The mod operation"}

The unique $r$ of @thm-division is written $n\bmod d$ (read “$n$ mod $d$”), and the quotient is $q=\lfloor n/d\rfloor$. Thus
$$\frac nd = \left\lfloor\frac nd\right\rfloor + \frac{n\bmod d}{d}, \qquad 0\le\frac{n\bmod d}{d}<1.$$

:::

::: {#exm-remainders-and-parity-1 .example}

$6\bmod4=2$,  $7\bmod4=3$,  $6\bmod2=0$,  $7\bmod2=1$,  $6\bmod5=1$,  $144\bmod100=44$,  $174\bmod48=30$.

:::

::: {.remark name="Negative $n$"}

The divisor $d$ is always positive, but $n$ may be negative; $q$ is still the largest integer with $qd\le n$. For example $-6\bmod5=4$: the largest multiple of $5$ that is $\le-6$ is $-10$ (so $q=-2$), and $-10+4=-6$. A programming language’s `%` operator need not agree with $\bmod$ on negative arguments.

:::

## Parity

::: {#def-parity .definition name="Parity"}

The *parity* of $x\in\mathbb{Z}$ is $x\bmod2$; $x$ is *even* if this is $0$ and *odd* if it is $1$.

:::

::: {#exm-remainders-and-parity-1-2 .example}

The sum or difference of two odd numbers is even, while their product is odd.

:::

::: {.remark name="Parity as Boolean algebra"}

Writing parities as $0,1$, the addition and multiplication tables mod $2$ are
$$\begin{array}{c|cc}
+ & 0 & 1\\\hline
0 & 0 & 1\\
1 & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|cc}
\times & 0 & 1\\\hline
0 & 0 & 0\\
1 & 0 & 1
\end{array}$$
These are exactly the truth tables of $\oplus$ and $\wedge$ with $0=$ False and $1=$ True. So $\mathbb{Z}_2$ with $+,\times$ *is* propositional logic with $\oplus,\wedge$, up to renaming. This is why logic gates can do arithmetic.

:::
