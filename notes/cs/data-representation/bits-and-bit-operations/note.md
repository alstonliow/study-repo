---
title: "Bits, Bytes and Bit-Level Operations"
sources: [cmu15213-2, cmu15213r-3]
requires: [math/discrete/logic/propositional/laws-of-boolean-algebra, math/discrete/sets/set-operations]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 2 "Bits, Bytes and Integers, part 1" and Recitation 3, in our own wording. -->

A computer stores everything (instructions, integers, characters, pictures) as sequences of two-valued signals. This note fixes the vocabulary for such sequences and the operations C offers on them.

::: {#def-bit-vector .definition name="Bit, byte, bit vector, word"}

A *bit* is a value in $\{0,1\}$. A *bit vector* of width $w$ is a sequence
$$x=[x_{w-1},x_{w-2},\dots,x_1,x_0],\qquad x_i\in\{0,1\},$$
written with the *most significant* bit $x_{w-1}$ on the left and the *least significant* bit $x_0$ on the right. A *byte* is a bit vector of width $8$. A *word* is the natural width of a machine's integers and addresses; on x86-64 it is $64$ bits.

:::

Long bit vectors are written in *hexadecimal*: each group of four bits, from the right, becomes one digit $0$–$9$, $\mathtt a$–$\mathtt f$, and C marks the number with the prefix `0x`. A byte is exactly two hex digits.

::: {#exm-hex-conversion .example name="Binary, hex and decimal"}

The 16-bit vector $0011\,1011\,0110\,1101$ has hex digits $3,\mathtt b,6,\mathtt d$, so it is `0x3B6D`, and its value as an unsigned number is $3\cdot16^3+11\cdot16^2+6\cdot16+13=15213$.

:::

::: {#fig-bits-and-bit-operations-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \b [count=\i from 0] in {0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1} {
  \draw[cell frame] (\i*0.5,0) rectangle (\i*0.5+0.5,0.5);
  \node[lab] at (\i*0.5+0.25,0.25) {$\b$};
}
\foreach \i in {0,...,15} { \pgfmathtruncatemacro{\k}{15-\i} \node[tick] at (\i*0.5+0.25,-0.22) {\k}; }
\foreach \h/\j in {3/0,B/1,6/2,D/3} {
  \draw[faint] (\j*2+0.05,0.62) -- (\j*2+0.05,0.75) -- (\j*2+1.95,0.75) -- (\j*2+1.95,0.62);
  \node[lab] at (\j*2+1,1.05) {\texttt{\h}};
}
\node[lab, anchor=west] at (8.2,1.05) {hex: \texttt{0x3B6D}};
\node[lab, anchor=west] at (8.2,0.25) {bits};
\node[lab, anchor=west] at (8.2,-0.22) {\scriptsize bit index};
\end{tikzpicture}
\end{center}
```

Each group of four bits, counted from the least significant end, is one hexadecimal digit

:::

::: {#def-bitwise-operations .definition name="Bitwise operations"}

For bit vectors $x,y$ of equal width, C's operators `&`, `|`, `^` and `~` act bit by bit:
$$(x\,\&\,y)_i=x_i\wedge y_i,\quad (x\mid y)_i=x_i\vee y_i,\quad (x\,\hat{}\,y)_i=x_i\oplus y_i,\quad (\mathord{\sim}x)_i=\neg x_i .$$

:::

Because each bit position is an independent Boolean value, every law of Boolean algebra (@thm-distributive-laws, De Morgan's laws) holds for bit vectors position by position.

::: {#prp-bit-vector-sets .proposition name="Bit vectors as sets"}

Identify $x$ of width $w$ with the set $A_x=\{i: x_i=1\}\subseteq\{0,\dots,w-1\}$. Then
$$A_{x\&y}=A_x\cap A_y,\quad A_{x\mid y}=A_x\cup A_y,\quad A_{x\,\hat{}\,y}=A_x\mathbin{\triangle}A_y,\quad A_{\sim x}=\{0,\dots,w-1\}\setminus A_x .$$

:::

::: {.proof}
1. Fix a position $i$. By definition, $i\in A_{x\&y}$ if and only if $x_i\wedge y_i=1$, that is, $x_i=1$ and $y_i=1$, that is, $i\in A_x$ and $i\in A_y$.

2. The same argument with $\vee$, $\oplus$ and $\neg$ in place of $\wedge$ gives union, symmetric difference and complement.
:::

::: {#exm-bit-masks .example name="Masks"}

A *mask* selects bits. With $x=$ `0x3B6D`: `x & 0xFF` keeps the low byte, `0x6D`; `x | 0xF` sets the low four bits, giving `0x3B6F`; `x ^ 0xFF00` flips the high byte, giving `0xC46D`. In the set view, `0xFF` is $\{0,\dots,7\}$ and `&` intersects with it.

:::

::: {#def-logical-operations .definition name="Logical operations"}

C's *logical* operators `&&`, `||` and `!` treat a whole value as a truth value: $0$ is false, every nonzero value is true, and the result is always $0$ or $1$. `&&` and `||` evaluate their right operand only when the left one does not already decide the result (*short-circuit evaluation*).

:::

::: {#exm-logical-vs-bitwise .example name="Logical versus bitwise"}

For $x=$ `0x41` and $y=$ `0x3E`: `x & y` is `0x00` but `x && y` is `1`; `~x` is `0xBE` (in a byte) but `!x` is `0`; `!!x` is `1`, the standard idiom for "is $x$ nonzero". The expression `p && *p` reads `*p` only when the pointer `p` is not null.

:::

::: {#def-shift-operations .definition name="Shift operations"}

For $x$ of width $w$ and $0\le k<w$:

- the *left shift* `x << k` moves every bit $k$ places to the left, drops the $k$ high bits and fills the right with $0$s;
- the *logical right shift* moves every bit $k$ places to the right and fills the left with $0$s;
- the *arithmetic right shift* moves every bit $k$ places to the right and fills the left with $k$ copies of the old most significant bit.

In C, `>>` on an unsigned value is logical; on a signed value almost every compiler uses the arithmetic shift. A shift by $k<0$ or $k\ge w$ is undefined behaviour.

:::

::: {#fig-bits-and-bit-operations-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.2,2.3499999999999996) {\texttt{x}};
\draw[cell frame] (0.0,2.0999999999999996) rectangle (0.5,2.5999999999999996); \node[lab] at (0.25,2.3499999999999996) {$1$};
\draw[cell frame] (0.5,2.0999999999999996) rectangle (1.0,2.5999999999999996); \node[lab] at (0.75,2.3499999999999996) {$0$};
\draw[cell frame] (1.0,2.0999999999999996) rectangle (1.5,2.5999999999999996); \node[lab] at (1.25,2.3499999999999996) {$1$};
\draw[cell frame] (1.5,2.0999999999999996) rectangle (2.0,2.5999999999999996); \node[lab] at (1.75,2.3499999999999996) {$0$};
\draw[cell frame] (2.0,2.0999999999999996) rectangle (2.5,2.5999999999999996); \node[lab] at (2.25,2.3499999999999996) {$0$};
\draw[cell frame] (2.5,2.0999999999999996) rectangle (3.0,2.5999999999999996); \node[lab] at (2.75,2.3499999999999996) {$0$};
\draw[cell frame] (3.0,2.0999999999999996) rectangle (3.5,2.5999999999999996); \node[lab] at (3.25,2.3499999999999996) {$1$};
\draw[cell frame] (3.5,2.0999999999999996) rectangle (4.0,2.5999999999999996); \node[lab] at (3.75,2.3499999999999996) {$0$};
\node[lab, anchor=east] at (-0.2,1.65) {\texttt{x << 3}};
\draw[cell frame] (0.0,1.4) rectangle (0.5,1.9); \node[lab] at (0.25,1.65) {$0$};
\draw[cell frame] (0.5,1.4) rectangle (1.0,1.9); \node[lab] at (0.75,1.65) {$0$};
\draw[cell frame] (1.0,1.4) rectangle (1.5,1.9); \node[lab] at (1.25,1.65) {$0$};
\draw[cell frame] (1.5,1.4) rectangle (2.0,1.9); \node[lab] at (1.75,1.65) {$1$};
\draw[cell frame] (2.0,1.4) rectangle (2.5,1.9); \node[lab] at (2.25,1.65) {$0$};
\draw[hl cell] (2.5,1.4) rectangle (3.0,1.9); \node[lab] at (2.75,1.65) {$0$};
\draw[hl cell] (3.0,1.4) rectangle (3.5,1.9); \node[lab] at (3.25,1.65) {$0$};
\draw[hl cell] (3.5,1.4) rectangle (4.0,1.9); \node[lab] at (3.75,1.65) {$0$};
\node[lab, anchor=east] at (-0.2,0.95) {logical \texttt{x >> 2}};
\draw[hl cell] (0.0,0.7) rectangle (0.5,1.2); \node[lab] at (0.25,0.95) {$0$};
\draw[hl cell] (0.5,0.7) rectangle (1.0,1.2); \node[lab] at (0.75,0.95) {$0$};
\draw[cell frame] (1.0,0.7) rectangle (1.5,1.2); \node[lab] at (1.25,0.95) {$1$};
\draw[cell frame] (1.5,0.7) rectangle (2.0,1.2); \node[lab] at (1.75,0.95) {$0$};
\draw[cell frame] (2.0,0.7) rectangle (2.5,1.2); \node[lab] at (2.25,0.95) {$1$};
\draw[cell frame] (2.5,0.7) rectangle (3.0,1.2); \node[lab] at (2.75,0.95) {$0$};
\draw[cell frame] (3.0,0.7) rectangle (3.5,1.2); \node[lab] at (3.25,0.95) {$0$};
\draw[cell frame] (3.5,0.7) rectangle (4.0,1.2); \node[lab] at (3.75,0.95) {$0$};
\node[lab, anchor=east] at (-0.2,0.25) {arithmetic \texttt{x >> 2}};
\draw[hl cell] (0.0,0.0) rectangle (0.5,0.5); \node[lab] at (0.25,0.25) {$1$};
\draw[hl cell] (0.5,0.0) rectangle (1.0,0.5); \node[lab] at (0.75,0.25) {$1$};
\draw[cell frame] (1.0,0.0) rectangle (1.5,0.5); \node[lab] at (1.25,0.25) {$1$};
\draw[cell frame] (1.5,0.0) rectangle (2.0,0.5); \node[lab] at (1.75,0.25) {$0$};
\draw[cell frame] (2.0,0.0) rectangle (2.5,0.5); \node[lab] at (2.25,0.25) {$1$};
\draw[cell frame] (2.5,0.0) rectangle (3.0,0.5); \node[lab] at (2.75,0.25) {$0$};
\draw[cell frame] (3.0,0.0) rectangle (3.5,0.5); \node[lab] at (3.25,0.25) {$0$};
\draw[cell frame] (3.5,0.0) rectangle (4.0,0.5); \node[lab] at (3.75,0.25) {$0$};
\end{tikzpicture}
\end{center}
```

Shifting the byte $10100010$: the shaded cells are the bits filled in. A logical right shift fills with $0$, an arithmetic right shift copies the sign bit (here $1$)

:::

::: {#rmk-bits-and-bit-operations-1 name="Why large shift amounts are undefined"}

On x86-64 the shift instructions use only the low $5$ bits of the count for 32-bit operands (low $6$ bits for 64-bit operands), so `x << 32` on a 32-bit `int` may compile to a shift by $0$. Other machines behave differently, so the C standard leaves the result undefined; portable code keeps $0\le k<w$.

:::
