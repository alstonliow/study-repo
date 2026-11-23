---
title: "IEEE Floating-Point Representation"
sources: [cmu15213-4, cmu15213r-3]
requires: [cs/data-representation/integer-encodings]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 4 "Floating Point" and Recitation 3, in our own wording; proofs written out in steps. The abstract model of floating-point numbers is def-floating-point-system in math/numerical; this note gives the bit-level encoding. -->

::: {#def-binary-fraction .definition name="Binary fractions"}

A *binary fraction* $b_m\cdots b_1b_0.b_{-1}b_{-2}\cdots b_{-n}$ denotes
$$\sum_{i=-n}^{m}b_i\,2^i .$$
Bits right of the binary point have weights $\tfrac12,\tfrac14,\tfrac18,\dots$

:::

So $101.11_2=4+1+\tfrac12+\tfrac14=5\tfrac34$. Only numbers of the form $x/2^k$ have finite binary fractions: $\tfrac15=0.\overline{0011}_2$ repeats forever, so `0.1` and `0.2` are never stored exactly.

::: {#def-ieee-floating-point .definition name="IEEE 754 floating-point format" related="def-floating-point-system"}

A floating-point format with $k$ exponent bits and $n$ fraction bits stores a bit pattern $s\,|\,e_{k-1}\cdots e_0\,|\,f_{n-1}\cdots f_0$. Let $e$ be the unsigned value of the exponent field, $\mathit{Bias}=2^{k-1}-1$ and $f=0.f_{n-1}\cdots f_0$ (a binary fraction in $[0,1)$). The value is $(-1)^s\,M\,2^E$ with

| case | exponent field | $E$ | $M$ |
|---|---|---|---|
| normalized | $0<e<2^k-1$ | $e-\mathit{Bias}$ | $1+f$ |
| denormalized | $e=0$ | $1-\mathit{Bias}$ | $f$ |
| infinity | $e=2^k-1$, $f=0$ | | $\pm\infty$ |
| NaN (not a number) | $e=2^k-1$, $f\ne0$ | | NaN |

*Single precision* (`float`) has $k=8$, $n=23$, $\mathit{Bias}=127$; *double precision* (`double`) has $k=11$, $n=52$, $\mathit{Bias}=1023$.

:::

::: {#fig-ieee-floating-point-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0,0) rectangle (0.5,0.6); \node[lab] at (0.25,0.3) {$s$};
\draw[cell frame] (0.5,0) rectangle (3.3,0.6); \node[lab] at (1.9,0.3) {\texttt{exp}};
\draw[cell frame] (3.3,0) rectangle (10.5,0.6); \node[lab] at (6.9,0.3) {\texttt{frac}};
\node[tick] at (0.25,0.85) {1}; \node[tick] at (1.9,0.85) {8 bits}; \node[tick] at (6.9,0.85) {23 bits};
\node[lab, anchor=east] at (-0.2,0.3) {\texttt{float}};
\draw[hl cell] (0,-1.1) rectangle (0.5,-0.5); \node[lab] at (0.25,-0.8) {$s$};
\draw[cell frame] (0.5,-1.1) rectangle (4.1,-0.5); \node[lab] at (2.3,-0.8) {\texttt{exp}};
\draw[cell frame] (4.1,-1.1) rectangle (10.5,-0.5); \node[lab] at (7.3,-0.8) {\texttt{frac}};
\node[tick] at (2.3,-1.35) {11 bits}; \node[tick] at (7.3,-1.35) {52 bits (drawn shortened)};
\node[lab, anchor=east] at (-0.2,-0.8) {\texttt{double}};
\end{tikzpicture}
\end{center}
```

The three fields of single and double precision: sign, exponent and fraction

:::

::: {#exm-encode-15213 .example name="Encoding $15213.0$ as a `float`"}

1. $15213=11101101101101_2=1.1101101101101_2\times2^{13}$, so it is normalized with $E=13$ and $M=1.1101101101101_2$.

2. The exponent field is $e=E+127=140=10001100_2$.

3. The fraction field is the bits of $M$ after the point, padded with zeros to 23 bits: $11011011011010000000000$.

4. With $s=0$ the pattern is $0\,10001100\,11011011011010000000000$ = `0x466DB400`. The integer $15213$ (`0x00003B6D`) shares the bit string $1101101101101$ with it, shifted.

:::

::: {#prp-denormal-continuity .proposition name="Why denormalized values use $E=1-\mathit{Bias}$"}

With $E=1-\mathit{Bias}$ for denormalized values, the largest denormalized value and the smallest positive normalized value differ by exactly one step $2^{1-\mathit{Bias}-n}$, so the positive representable values near zero are evenly spaced with that step from $0$ up to $2^{1-\mathit{Bias}}$.

:::

::: {.proof}
1. Denormalized values are $f\cdot2^{1-\mathit{Bias}}$ with $f\in\{0,2^{-n},\dots,1-2^{-n}\}$: evenly spaced by $2^{-n}\cdot2^{1-\mathit{Bias}}$, the largest being $(1-2^{-n})2^{1-\mathit{Bias}}$.

2. The smallest normalized value has $e=1$, $f=0$: $1\cdot2^{1-\mathit{Bias}}$.

3. Their difference is $2^{-n}\cdot2^{1-\mathit{Bias}}$, the same step. With $E=-\mathit{Bias}$ instead, the denormalized values would stop at half that height and leave a gap.
:::

::: {#exm-tiny-float .example name="An 8-bit format"}

Take $s=1$ bit, $k=4$, $n=3$, so $\mathit{Bias}=7$. Some nonnegative values:

| bits ($s\,e\,f$) | $e$ | $E$ | value |
|---|---|---|---|
| 0 0000 000 | 0 | $-6$ | $0$ |
| 0 0000 001 | 0 | $-6$ | $\tfrac18\cdot2^{-6}=\tfrac1{512}$ (smallest positive) |
| 0 0000 111 | 0 | $-6$ | $\tfrac78\cdot2^{-6}=\tfrac7{512}$ (largest denormalized) |
| 0 0001 000 | 1 | $-6$ | $2^{-6}=\tfrac8{512}$ (smallest normalized) |
| 0 0111 000 | 7 | $0$ | $1$ |
| 0 0111 001 | 7 | $0$ | $\tfrac98$ |
| 0 1110 111 | 14 | $7$ | $\tfrac{15}8\cdot2^7=240$ (largest finite) |
| 0 1111 000 | 15 | | $+\infty$ |

Read as unsigned integers, the patterns are in the same order as their values; this is why floating-point numbers can be compared with an integer comparison (after handling the sign).

:::

::: {#fig-ieee-floating-point-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.75cm]
\draw[->] (-0.3,0) -- (15.2,0);
\foreach \v in {0,0.0625,0.125,0.1875} { \node[dot, fill=accent] at (\v,0) {}; }
\foreach \v in {0.25,0.3125,0.375,0.4375,0.5,0.625,0.75,0.875,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,10,12,14} { \node[dot] at (\v,0) {}; }
\foreach \v in {0,1,2,4,8,14} { \draw (\v,-0.12) -- (\v,-0.22); \node[tick] at (\v,-0.45) {$\v$}; }
\node[tick, anchor=south] at (0.1,0.2) {denormalized};
\node[lab, anchor=west] at (15.3,0) {$+\infty$};
\end{tikzpicture}
\end{center}
```

All nonnegative finite values of a 6-bit format ($k=3$, $n=2$, $\mathit{Bias}=3$). Denormalized values (terracotta) are evenly spaced near $0$; normalized values double their spacing at every power of two

:::

::: {#prp-ieee-special-properties .proposition name="Properties of the encoding"}

1. The pattern of all zeros is $+0$; the pattern with only the sign bit set is $-0$, and $+0=-0$ compares as equal.
2. For nonnegative values that are not NaN, $x<y$ if and only if the bit patterns satisfy $B2U(x)<B2U(y)$.
3. NaN compares unequal to everything, including itself.

:::

::: {.proof}
1. Both have $E$ denormalized and $f=0$, so $M=0$.

2. Patterns with larger exponent fields are larger values: every value with field $e$ is below $2^{e-\mathit{Bias}+1}$ and every value with field $e+1$ is at least that (for $e=0$ use @prp-denormal-continuity). Within one exponent field, the value grows with $f$. Larger $e$ also means a larger unsigned pattern, and for equal $e$ the pattern grows with $f$.

3. This is a rule of the standard, chosen so that `x != x` tests for NaN.
:::

::: {#rmk-ieee-floating-point-1 name="Where infinities and NaNs come from"}

Overflow produces $\pm\infty$ ($1/0=+\infty$, $-1/0=-\infty$); operations without a sensible value produce NaN ($\sqrt{-1}$, $\infty-\infty$, $0\cdot\infty$). Both propagate through later operations instead of stopping the program, so a NaN at the end of a long computation can be traced back by testing intermediate results.

:::
