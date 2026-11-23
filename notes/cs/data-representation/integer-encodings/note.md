---
title: "Unsigned and Two's-Complement Encodings"
sources: [cmu15213-2]
requires: [cs/data-representation/bits-and-bit-operations]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 2 "Bits, Bytes and Integers, part 1", in our own wording; proofs written out in steps. -->

A bit vector by itself has no numeric value; an *encoding* assigns one. C uses two encodings for integers of a fixed width $w$: unsigned and two's complement.

::: {#def-unsigned-encoding .definition name="Unsigned encoding"}

The *unsigned* value of $x=[x_{w-1},\dots,x_0]$ is
$$B2U_w(x)=\sum_{i=0}^{w-1}x_i\,2^i .$$
Its range is $0,\dots,UMax_w$ with $UMax_w=2^w-1$ (all bits $1$).

:::

::: {#def-twos-complement-encoding .definition name="Two's-complement encoding"}

The *two's-complement* value of $x=[x_{w-1},\dots,x_0]$ is
$$B2T_w(x)=-x_{w-1}\,2^{w-1}+\sum_{i=0}^{w-2}x_i\,2^i .$$
The most significant bit has *negative* weight $-2^{w-1}$ and is called the *sign bit*. The range is $TMin_w,\dots,TMax_w$ with
$$TMin_w=-2^{w-1}\ (\text{pattern }10\cdots0),\qquad TMax_w=2^{w-1}-1\ (\text{pattern }01\cdots1).$$

:::

::: {#fig-integer-encodings-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \b/\w [count=\i from 0] in {1/-8,0/4,1/2,1/1} {
  \draw[cell frame] (\i*1.1,0) rectangle (\i*1.1+1.0,0.6);
  \node[lab] at (\i*1.1+0.5,0.3) {$\b$};
  \node[tick] at (\i*1.1+0.5,-0.25) {$\w$};
}
\draw[hl cell] (0,0) rectangle (1.0,0.6); \node[lab] at (0.5,0.3) {$1$};
\node[lab, anchor=east] at (-0.15,0.3) {bits};
\node[lab, anchor=east] at (-0.15,-0.25) {\scriptsize weights $B2T_4$};
\node[lab, anchor=west] at (4.6,0.3) {$B2T_4(1011)=-8+2+1=-5$};
\node[lab, anchor=west] at (4.6,-0.35) {$B2U_4(1011)=8+2+1=11$};
\end{tikzpicture}
\end{center}
```

The same pattern $1011$ under the two encodings: only the weight of the sign bit differs ($-8$ instead of $+8$)

:::

::: {#thm-encodings-bijective .theorem name="Both encodings are bijections"}

$B2U_w$ is a bijection from $\{0,1\}^w$ onto $\{0,\dots,2^w-1\}$, and $B2T_w$ is a bijection from $\{0,1\}^w$ onto $\{-2^{w-1},\dots,2^{w-1}-1\}$.

:::

::: {.proof}
1. Every $u\in\{0,\dots,2^w-1\}$ has a base-$2$ expansion with $w$ digits, so $B2U_w$ is onto.

2. Both sets have $2^w$ elements, so a map between them that is onto is also one-to-one.

3. For two's complement, $B2T_w(x)=B2U_w(x)-x_{w-1}2^w$: the sign bit's unsigned weight $2^{w-1}$ is replaced by $-2^{w-1}$, a change of $-2^w$.

4. Patterns with $x_{w-1}=0$ have $B2U_w(x)\in\{0,\dots,2^{w-1}-1\}$ and keep that value. Patterns with $x_{w-1}=1$ have $B2U_w(x)\in\{2^{w-1},\dots,2^w-1\}$ and are sent to $\{-2^{w-1},\dots,-1\}$.

5. Each half is mapped one-to-one onto its target by step 1, and the two targets partition $\{-2^{w-1},\dots,2^{w-1}-1\}$, so $B2T_w$ is a bijection.
:::

::: {#fig-integer-encodings-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.62cm]
\draw[->] (-0.6,2.2) -- (15.8,2.2); \node[lab, anchor=west] at (16,2.2) {unsigned};
\draw[->] (-0.6,-2.2) -- (15.8,-2.2); \node[lab, anchor=west] at (16,-2.2) {two's complement};
\node[tick, rotate=90] (p0) at (0,0) {\texttt{0000}};
\draw (0,2.12) -- (0,2.28); \node[tick] at (0,2.5) {$0$};
\draw[map] (p0.east) -- (0,2.12);
\draw (8,-2.28) -- (8,-2.12); \node[tick] at (8,-2.5) {$0$};
\draw[map] (p0.west) -- (8,-2.12);
\node[tick, rotate=90] (p1) at (1,0) {\texttt{0001}};
\draw (1,2.12) -- (1,2.28); \node[tick] at (1,2.5) {$1$};
\draw[map] (p1.east) -- (1,2.12);
\draw (9,-2.28) -- (9,-2.12); \node[tick] at (9,-2.5) {$1$};
\draw[map] (p1.west) -- (9,-2.12);
\node[tick, rotate=90] (p2) at (2,0) {\texttt{0010}};
\draw (2,2.12) -- (2,2.28); \node[tick] at (2,2.5) {$2$};
\draw[map] (p2.east) -- (2,2.12);
\draw (10,-2.28) -- (10,-2.12); \node[tick] at (10,-2.5) {$2$};
\draw[map] (p2.west) -- (10,-2.12);
\node[tick, rotate=90] (p3) at (3,0) {\texttt{0011}};
\draw (3,2.12) -- (3,2.28); \node[tick] at (3,2.5) {$3$};
\draw[map] (p3.east) -- (3,2.12);
\draw (11,-2.28) -- (11,-2.12); \node[tick] at (11,-2.5) {$3$};
\draw[map] (p3.west) -- (11,-2.12);
\node[tick, rotate=90] (p4) at (4,0) {\texttt{0100}};
\draw (4,2.12) -- (4,2.28); \node[tick] at (4,2.5) {$4$};
\draw[map] (p4.east) -- (4,2.12);
\draw (12,-2.28) -- (12,-2.12); \node[tick] at (12,-2.5) {$4$};
\draw[map] (p4.west) -- (12,-2.12);
\node[tick, rotate=90] (p5) at (5,0) {\texttt{0101}};
\draw (5,2.12) -- (5,2.28); \node[tick] at (5,2.5) {$5$};
\draw[map] (p5.east) -- (5,2.12);
\draw (13,-2.28) -- (13,-2.12); \node[tick] at (13,-2.5) {$5$};
\draw[map] (p5.west) -- (13,-2.12);
\node[tick, rotate=90] (p6) at (6,0) {\texttt{0110}};
\draw (6,2.12) -- (6,2.28); \node[tick] at (6,2.5) {$6$};
\draw[map] (p6.east) -- (6,2.12);
\draw (14,-2.28) -- (14,-2.12); \node[tick] at (14,-2.5) {$6$};
\draw[map] (p6.west) -- (14,-2.12);
\node[tick, rotate=90] (p7) at (7,0) {\texttt{0111}};
\draw (7,2.12) -- (7,2.28); \node[tick] at (7,2.5) {$7$};
\draw[map] (p7.east) -- (7,2.12);
\draw (15,-2.28) -- (15,-2.12); \node[tick] at (15,-2.5) {$7$};
\draw[map] (p7.west) -- (15,-2.12);
\node[tick, rotate=90] (p8) at (8,0) {\texttt{1000}};
\draw (8,2.12) -- (8,2.28); \node[tick] at (8,2.5) {$8$};
\draw[map] (p8.east) -- (8,2.12);
\draw (0,-2.28) -- (0,-2.12); \node[tick] at (0,-2.5) {$-8$};
\draw[map, draw=accent] (p8.west) -- (0,-2.12);
\node[tick, rotate=90] (p9) at (9,0) {\texttt{1001}};
\draw (9,2.12) -- (9,2.28); \node[tick] at (9,2.5) {$9$};
\draw[map] (p9.east) -- (9,2.12);
\draw (1,-2.28) -- (1,-2.12); \node[tick] at (1,-2.5) {$-7$};
\draw[map, draw=accent] (p9.west) -- (1,-2.12);
\node[tick, rotate=90] (p10) at (10,0) {\texttt{1010}};
\draw (10,2.12) -- (10,2.28); \node[tick] at (10,2.5) {$10$};
\draw[map] (p10.east) -- (10,2.12);
\draw (2,-2.28) -- (2,-2.12); \node[tick] at (2,-2.5) {$-6$};
\draw[map, draw=accent] (p10.west) -- (2,-2.12);
\node[tick, rotate=90] (p11) at (11,0) {\texttt{1011}};
\draw (11,2.12) -- (11,2.28); \node[tick] at (11,2.5) {$11$};
\draw[map] (p11.east) -- (11,2.12);
\draw (3,-2.28) -- (3,-2.12); \node[tick] at (3,-2.5) {$-5$};
\draw[map, draw=accent] (p11.west) -- (3,-2.12);
\node[tick, rotate=90] (p12) at (12,0) {\texttt{1100}};
\draw (12,2.12) -- (12,2.28); \node[tick] at (12,2.5) {$12$};
\draw[map] (p12.east) -- (12,2.12);
\draw (4,-2.28) -- (4,-2.12); \node[tick] at (4,-2.5) {$-4$};
\draw[map, draw=accent] (p12.west) -- (4,-2.12);
\node[tick, rotate=90] (p13) at (13,0) {\texttt{1101}};
\draw (13,2.12) -- (13,2.28); \node[tick] at (13,2.5) {$13$};
\draw[map] (p13.east) -- (13,2.12);
\draw (5,-2.28) -- (5,-2.12); \node[tick] at (5,-2.5) {$-3$};
\draw[map, draw=accent] (p13.west) -- (5,-2.12);
\node[tick, rotate=90] (p14) at (14,0) {\texttt{1110}};
\draw (14,2.12) -- (14,2.28); \node[tick] at (14,2.5) {$14$};
\draw[map] (p14.east) -- (14,2.12);
\draw (6,-2.28) -- (6,-2.12); \node[tick] at (6,-2.5) {$-2$};
\draw[map, draw=accent] (p14.west) -- (6,-2.12);
\node[tick, rotate=90] (p15) at (15,0) {\texttt{1111}};
\draw (15,2.12) -- (15,2.28); \node[tick] at (15,2.5) {$15$};
\draw[map] (p15.east) -- (15,2.12);
\draw (7,-2.28) -- (7,-2.12); \node[tick] at (7,-2.5) {$-1$};
\draw[map, draw=accent] (p15.west) -- (7,-2.12);
\end{tikzpicture}
\end{center}
```

The sixteen 4-bit patterns. Unsigned (top) maps them in order onto $0,\dots,15$. Two's complement (bottom) gives $0000$–$0111$ the same values $0,\dots,7$ and moves $1000$–$1111$ (terracotta arrows) down by $16$, onto $-8,\dots,-1$

:::

::: {#prp-twos-complement-facts .proposition name="Useful facts about two's complement"}

For every width $w$:

1. $|TMin_w|=TMax_w+1$, so the range is asymmetric: $-TMin_w$ is not representable.
2. $UMax_w=2\,TMax_w+1$.
3. The all-ones pattern has $B2T_w=-1$ and $B2U_w=UMax_w$.
4. The pattern of $0$ is all zeros in both encodings.

:::

::: {.proof}
1. $TMax_w+1=2^{w-1}=-TMin_w$.

2. $2(2^{w-1}-1)+1=2^w-1$.

3. $B2T_w(1\cdots1)=-2^{w-1}+\sum_{i=0}^{w-2}2^i=-2^{w-1}+(2^{w-1}-1)=-1$, and $B2U_w(1\cdots1)=2^w-1$.

4. Every term of both sums is zero.
:::

::: {#exm-integer-ranges .example name="Ranges of C integer types on x86-64"}

| C type | $w$ | minimum | maximum |
|---|---|---|---|
| `unsigned char` | 8 | 0 | 255 |
| `signed char` | 8 | −128 | 127 |
| `short` | 16 | −32 768 | 32 767 |
| `int` | 32 | −2 147 483 648 | 2 147 483 647 |
| `unsigned` | 32 | 0 | 4 294 967 295 |
| `long` | 64 | $-2^{63}$ | $2^{63}-1\approx9.22\times10^{18}$ |

The header `limits.h` names these as `INT_MIN`, `INT_MAX`, `UINT_MAX` and so on. The C standard fixes only minimum sizes; the widths above are those of x86-64 Linux.

:::

::: {#rmk-integer-encodings-1 name="Why two's complement"}

Other signed encodings exist (sign-magnitude, ones' complement), but both have two zeros and need separate adder circuits. Under two's complement, signed and unsigned addition are the same bit-level operation (@thm-twos-complement-addition), so one adder serves both. Every modern processor uses it, and C23 requires it.

:::
