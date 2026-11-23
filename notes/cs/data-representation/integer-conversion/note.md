---
title: "Conversion, Casting, Extension and Truncation"
sources: [cmu15213-2, cmu15213r-6]
requires: [cs/data-representation/integer-encodings]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 2 "Bits, Bytes and Integers, part 1" and Recitation 6 (C review), in our own wording; proofs written out in steps. -->

C converts between signed and unsigned values, and between widths, silently. All these conversions keep or cut the *bit pattern*; the numeric value follows from the encodings of @def-unsigned-encoding and @def-twos-complement-encoding.

::: {#def-signed-unsigned-casts .definition name="Casting between signed and unsigned"}

A cast between a signed and an unsigned type of the same width $w$ keeps the bit pattern and reinterprets it:
$$T2U_w(x)=B2U_w(T2B_w(x)),\qquad U2T_w(u)=B2T_w(U2B_w(u)),$$
where $T2B_w$ and $U2B_w$ are the inverses of the encodings (@thm-encodings-bijective).

:::

::: {#thm-t2u-formula .theorem name="Signed–unsigned conversion formulas"}

For $TMin_w\le x\le TMax_w$ and $0\le u\le UMax_w$,
$$T2U_w(x)=\begin{cases}x, & x\ge 0,\\ x+2^w, & x<0,\end{cases}\qquad U2T_w(u)=\begin{cases}u, & u\le TMax_w,\\ u-2^w, & u>TMax_w.\end{cases}$$

:::

::: {.proof}
1. For any pattern $b$, $B2U_w(b)-B2T_w(b)=b_{w-1}2^w$ (step 3 of the proof of @thm-encodings-bijective).

2. Take $b=T2B_w(x)$. Its sign bit is $1$ exactly when $x<0$, so $T2U_w(x)=B2U_w(b)=x+b_{w-1}2^w$ is $x$ for $x\ge0$ and $x+2^w$ for $x<0$.

3. Take $b=U2B_w(u)$. Its top bit is $1$ exactly when $u\ge 2^{w-1}$, that is $u>TMax_w$, and $U2T_w(u)=u-b_{w-1}2^w$.
:::

::: {#fig-integer-conversion-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.42cm]
\draw[->] (-9,1.6) -- (17,1.6) node[lab, right] {two's complement};
\draw[->] (-9,0) -- (17,0) node[lab, right] {unsigned};
\path[tintA] (0,1.4) rectangle (7.9,1.8); \path[tintA] (0,-0.2) rectangle (7.9,0.2);
\path[tintB] (-8,1.4) rectangle (-0.1,1.8); \path[tintB] (8,-0.2) rectangle (15.9,0.2);
\foreach \v in {-8,0,7} { \node[tick] at (\v,2.0) {$\v$}; }
\foreach \v in {0,7,8,15} { \node[tick] at (\v,-0.45) {$\v$}; }
\draw[map] (3.5,1.4) -- (3.5,0.2); \node[tick, anchor=west] at (3.6,0.8) {same value};
\draw[map, draw=accent] (-4,1.4) to[out=-60,in=120] (12,0.2);
\node[edge label] at (2.5,0.55) {$+2^w$};
\end{tikzpicture}
\end{center}
```

$T2U_4$: nonnegative values keep their value; negative values $-8,\dots,-1$ become $8,\dots,15$, that is, they gain $2^4=16$

:::

::: {#def-c-implicit-conversion .definition name="Implicit conversion in C"}

When an operation (arithmetic or comparison) has one signed and one unsigned operand of the same width, C converts the signed operand to unsigned and performs the operation on unsigned values. Integer constants are signed unless they carry the suffix `U`.

:::

::: {#exm-unsigned-comparisons .example name="Surprising comparisons ($w=32$)"}

| expression | evaluated as | result |
|---|---|---|
| `-1 < 0` | signed | true |
| `-1 < 0U` | unsigned: $4\,294\,967\,295<0$ | false |
| `2147483647 > -2147483647 - 1` | signed | true |
| `2147483647U > -2147483647 - 1` | unsigned: $2^{31}-1>2^{31}$ | false |
| `(int) 2147483648U` | $U2T_{32}(2^{31})$ | $-2\,147\,483\,648$ |

The function `int f(unsigned u) { return u > -1; }` always returns $0$: the constant $-1$ is converted to $UMax_{32}$, and no unsigned value exceeds it.

:::

::: {#exm-unsigned-loop-bug .example name="An unsigned loop counter"}

The loop `for (unsigned i = n - 1; i >= 0; i--)` never ends: `i >= 0` is always true for an unsigned `i`, and after `i` reaches $0$ the decrement wraps to $UMax_{32}$. The same happens with `size_t`, the unsigned type returned by `sizeof` and `strlen`.

:::

::: {#thm-sign-extension .theorem name="Sign extension"}

Let $x$ be a pattern of width $w$ and let $x'$ of width $w+k$ be $x$ with $k$ copies of its sign bit $x_{w-1}$ added on the left. Then
$$B2T_{w+k}(x')=B2T_w(x).$$
Adding zeros on the left (*zero extension*) likewise preserves $B2U$.

:::

::: {.proof}
1. By induction it is enough to treat $k=1$.

2. If $x_{w-1}=0$ the new top bit is $0$, and both values equal $\sum_{i=0}^{w-2}x_i2^i$.

3. If $x_{w-1}=1$, the new pattern has bit $w$ with weight $-2^w$ and bit $w-1$ with weight $+2^{w-1}$. Together they contribute $-2^w+2^{w-1}=-2^{w-1}$, the weight of the old sign bit.

4. The lower bits are unchanged, so the values agree.

5. Zero extension adds terms $0\cdot2^i$ to $B2U$.
:::

::: {#fig-integer-conversion-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \b [count=\i from 0] in {1,0,1,1} { \draw[cell frame] (2+\i*0.55,1) rectangle (2.55+\i*0.55,1.55); \node[lab] at (2.275+\i*0.55,1.275) {$\b$}; }
\draw[hl cell] (2,1) rectangle (2.55,1.55); \node[lab] at (2.275,1.275) {$1$};
\node[lab, anchor=east] at (1.9,1.275) {$w=4$: $-5$};
\foreach \b [count=\i from 0] in {1,1,1,1,1,0,1,1} { \draw[cell frame] (\i*0.55-0.2,0) rectangle (\i*0.55+0.35,0.55); \node[lab] at (\i*0.55+0.075,0.275) {$\b$}; }
\foreach \i in {0,1,2,3,4} { \draw[hl cell] (\i*0.55-0.2,0) rectangle (\i*0.55+0.35,0.55); \node[lab] at (\i*0.55+0.075,0.275) {$1$}; }
\node[lab, anchor=west] at (4.3,0.275) {$w=8$: $-128+64+32+16+8+2+1=-5$};
\draw[map] (2.275,1) -- (0.075,0.55);
\draw[map] (2.275,1) -- (2.275,0.55);
\end{tikzpicture}
\end{center}
```

Sign extension of $1011$ ($-5$) to 8 bits copies the sign bit into the four new positions; the value stays $-5$

:::

::: {#thm-truncation .theorem name="Truncation"}

Let $x'$ be the pattern $x$ of width $w$ cut to its low $k$ bits. Then
$$B2U_k(x')=B2U_w(x)\bmod 2^k,\qquad B2T_k(x')=U2T_k\bigl(B2U_w(x)\bmod 2^k\bigr).$$

:::

::: {.proof}
1. $B2U_w(x)=\sum_{i<k}x_i2^i+2^k\sum_{i\ge k}x_i2^{i-k}$; the second sum is a multiple of $2^k$ and the first is in $\{0,\dots,2^k-1\}$, so the first is the remainder mod $2^k$ (@thm-division).

2. The first sum is $B2U_k(x')$.

3. The two's-complement value of the same $k$ bits is $U2T_k$ of their unsigned value (@thm-t2u-formula).
:::

::: {#exm-truncation .example name="Casting `int` to `short`"}

The `int` $53191$ is `0x0000CFC7`. Cast to `short` it keeps `0xCFC7`; its unsigned value $53191$ exceeds $TMax_{16}=32767$, so the `short` is $53191-65536=-12345$. Casting back to `int` sign-extends `0xCFC7` to `0xFFFFCFC7`, which is still $-12345$: truncation lost information, extension did not.

:::

::: {#rmk-integer-conversion-1 name="When to use unsigned"}

Unsigned arithmetic is the right tool for modular arithmetic, for bit sets and masks (@prp-bit-vector-sets), and for sizes and indices that can never be negative. Mixing it with signed values invites the bugs of @exm-unsigned-comparisons; when a counter must go down to $0$, write the loop test as `i < n` with an unsigned `i` running upward, or use a signed type.

:::
