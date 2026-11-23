---
title: "Floating-Point Rounding, Operations and Casts"
sources: [cmu15213-4, cmu15213r-3]
requires: [cs/data-representation/ieee-floating-point]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 4 "Floating Point" and Recitation 3 (round to even, guard/round/sticky bits), in our own wording; proofs written out in steps. -->

Every floating-point operation is specified as: compute the exact result, then *round* it to a representable value. This note describes that rounding at the bit level and what it does to the familiar laws of arithmetic.

::: {#def-rounding-modes .definition name="Rounding modes"}

For a real $x$ between two neighbouring representable values $a<x<b$, IEEE 754 offers four modes:

- *round toward zero*: the one of $a,b$ nearer to $0$;
- *round down* (toward $-\infty$): $a$;
- *round up* (toward $+\infty$): $b$;
- *round to nearest, ties to even* (the default): the nearer of $a,b$; if $x$ is exactly halfway, the one whose last fraction bit is $0$.

:::

::: {#exm-round-to-even-decimal .example name="Rounding to even in decimal"}

Rounding to whole numbers: $7.49\mapsto7$, $7.51\mapsto8$, and the ties $7.5\mapsto8$, $6.5\mapsto6$, $-6.5\mapsto-6$. Ties go up half the time and down half the time, so a sum of many rounded values has no systematic bias, unlike "round half up".

:::

::: {#def-guard-round-sticky .definition name="Guard, round and sticky bits"}

To round a binary fraction $1.b_1\cdots b_n\,r\,t_1t_2\cdots$ to $n$ fraction bits, call $b_n$ the *guard* bit $G$ (the last bit kept), $r$ the *round* bit $R$ (the first bit dropped) and $S=t_1\vee t_2\vee\cdots$ the *sticky* bit (the OR of all later bits).

:::

::: {#prp-round-to-even-rule .proposition name="The round-to-nearest-even rule"}

Round to nearest even adds $1$ at the position of $G$ exactly when
$$R\wedge(S\vee G)=1 .$$

:::

::: {.proof}
1. The dropped part is worth $R\cdot\tfrac12+(\text{rest})$ units of the last place, with $0\le\text{rest}<\tfrac12$ and $\text{rest}>0$ exactly when $S=1$.

2. If $R=0$ the dropped part is below half a unit: truncate.

3. If $R=1$ and $S=1$ it is above half: round up.

4. If $R=1$ and $S=0$ it is exactly half: round up only if that makes the last kept bit even, that is, if $G=1$.
:::

::: {#exm-guard-round-sticky .example name="Rounding to three fraction bits"}

| exact | $G\,R\,S$ | round up? | result |
|---|---|---|---|
| $1.000\,0000$ | $0\,0\,0$ | no | $1.000$ |
| $1.101\,0000$ | $1\,0\,0$ | no | $1.101$ |
| $1.000\,1000$ | $0\,1\,0$ | no (tie, $G=0$) | $1.000$ |
| $1.001\,1000$ | $1\,1\,0$ | yes (tie, $G=1$) | $1.010$ |
| $1.000\,1010$ | $0\,1\,1$ | yes | $1.001$ |
| $1.111\,1100$ | $1\,1\,1$ | yes | $10.000=1.000\times2^1$ |

The last row carries out of the leading bit, so the exponent goes up by one.

:::

::: {#fig-floating-point-rounding-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=2.6cm]
\draw (0,0) -- (3,0);
\foreach \v/\l in {0/1.000,1/1.001,2/1.010,3/1.011} { \draw (\v,-0.12) -- (\v,0.12); \node[tick] at (\v,-0.4) {$\l$}; }
\foreach \v in {0.5,1.5,2.5} { \draw[faint] (\v,-0.08) -- (\v,0.08); }
\node[hl dot] at (0.5,0) {}; \draw[map, draw=accent] (0.5,0.15) to[bend right=40] (0,0.15);
\node[hl dot] at (1.5,0) {}; \draw[map, draw=accent] (1.5,0.15) to[bend left=40] (2,0.15);
\node[dot] at (2.3,0) {}; \draw[map] (2.3,0.15) to[bend right=40] (2,0.15);
\node[dot] at (0.75,0) {}; \draw[map] (0.75,-0.15) to[bend right=40] (1,-0.15);
\node[tick, anchor=south] at (1,0.55) {ties (terracotta) go to the neighbour ending in $0$};
\end{tikzpicture}
\end{center}
```

Round to nearest even with three fraction bits: a value goes to the nearer neighbour; an exact tie goes to the neighbour whose last bit is $0$

:::

::: {#def-fp-operations .definition name="Floating-point addition and multiplication"}

For representable $x,y$ the machine computes $x\oplus y=\operatorname{Round}(x+y)$ and $x\otimes y=\operatorname{Round}(x\cdot y)$. For $x=(-1)^{s_1}M_12^{E_1}$ and $y=(-1)^{s_2}M_22^{E_2}$:

- *multiplication*: sign $s_1\oplus s_2$, significand $M_1M_2$, exponent $E_1+E_2$; if $M_1M_2\ge2$, shift right and add $1$ to the exponent; then round the significand and check the exponent for overflow;
- *addition* (say $E_1\ge E_2$): shift $M_2$ right by $E_1-E_2$ to align the binary points, add the signed significands, renormalize (shift left or right and adjust the exponent), round, check for overflow.

:::

::: {#prp-fp-algebra .proposition name="Which laws survive"}

Floating-point addition and multiplication (on non-NaN values) are commutative and monotone ($a\ge b\Rightarrow a\oplus c\ge b\oplus c$), and every finite $x$ has an additive inverse. They are *not* associative, and multiplication does not distribute over addition.

:::

::: {.proof}
1. Commutativity: $x+y=y+x$ exactly, and rounding is a function of the exact value.

2. Monotonicity: $a+c\ge b+c$ exactly, and rounding to nearest is a non-decreasing function of its argument.

3. Inverse: $x\oplus(-x)=\operatorname{Round}(0)=0$.

4. Associativity fails: in double precision, $(10^{20}\oplus(-10^{20}))\oplus3.14=3.14$ but $10^{20}\oplus((-10^{20})\oplus3.14)=10^{20}\oplus(-10^{20})=0$, because $-10^{20}+3.14$ rounds to $-10^{20}$ (the spacing of doubles near $10^{20}$ is $16384$).

5. Distributivity fails: $10^{20}\otimes(10^{20}\ominus10^{20})=0$, while $(10^{20}\otimes10^{20})\ominus(10^{20}\otimes10^{20})=\infty-\infty=$ NaN, because $10^{40}$ overflows single precision; in double precision use $10^{200}$ instead.
:::

::: {#exm-fp-casts .example name="Casts between `int`, `float` and `double` in C"}

| cast | effect |
|---|---|
| `int` → `double` | exact (53-bit significand holds every 32-bit integer) |
| `int` → `float` | may round (only 24 significand bits): `(float) 16777217` is $16777216$ |
| `double` → `float` | may round, may overflow to $\pm\infty$ |
| `float`/`double` → `int` | truncates toward zero: `(int) -2.7` is $-2$; out-of-range values and NaN are undefined in C, and x86-64 returns $TMin_{32}$ |

So `x == (int)(float) x` can be false, while `x == (int)(double) x` always holds for an `int` $x$.

:::

::: {#rmk-floating-point-rounding-1 name="Consequences for programs"}

Compilers may not reorder floating-point sums, because the result would change (@prp-fp-algebra); summing the same numbers in another order, for example in parallel threads, can give a different answer. Comparisons such as `x + y == z` are fragile; numerical code compares with a tolerance. The size of the error that rounding can cause is the subject of @thm-rounding-relative-error.

:::
