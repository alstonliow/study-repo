---
title: "Integer Arithmetic: Addition, Negation, Multiplication and Shifts"
sources: [cmu15213-3, cmu15213r-3]
requires: [cs/data-representation/integer-conversion, math/discrete/number-theory/modular-arithmetic]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 3 "Bits, Bytes and Integers, part 2" and Recitation 3 (biasing), in our own wording; proofs written out in steps. -->

Machine integers have a fixed width $w$, so the true result of an operation may not fit. The hardware keeps the low $w$ bits of the true result; this note works out what that means for each encoding.

::: {#thm-unsigned-addition .theorem name="Unsigned addition"}

For $0\le x,y<2^w$, the unsigned sum $x+^{\mathrm u}_wy$ computed by the machine is
$$x+^{\mathrm u}_wy=(x+y)\bmod 2^w=\begin{cases}x+y, & x+y<2^w,\\ x+y-2^w, & x+y\ge2^w\ (\text{overflow}).\end{cases}$$
Overflow happened if and only if the computed sum $s$ satisfies $s<x$ (equivalently $s<y$).

:::

::: {.proof}
1. The true sum satisfies $0\le x+y<2^{w+1}$, so it fits in $w+1$ bits; dropping bit $w$ is truncation to $w$ bits, which gives $(x+y)\bmod2^w$ (@thm-truncation).

2. Without overflow, $s=x+y\ge x$.

3. With overflow, $s=x+y-2^w=x-(2^w-y)<x$ because $y<2^w$.
:::

::: {#thm-twos-complement-addition .theorem name="Two's-complement addition"}

For $TMin_w\le x,y\le TMax_w$, the machine's signed sum is
$$x+^{\mathrm t}_wy=U2T_w\bigl((x+y)\bmod 2^w\bigr)=\begin{cases}x+y-2^w, & x+y>TMax_w\ (\text{positive overflow}),\\ x+y, & TMin_w\le x+y\le TMax_w,\\ x+y+2^w, & x+y<TMin_w\ (\text{negative overflow}).\end{cases}$$
It has the same bit pattern as the unsigned sum of the two patterns. Overflow happened if and only if $x$ and $y$ have the same sign and the computed sum has the other sign.

:::

::: {.proof}
1. By @thm-t2u-formula, $T2U_w(x)\equiv x$ and $T2U_w(y)\equiv y\pmod{2^w}$, so the unsigned sum of the patterns is $\equiv x+y\pmod{2^w}$; reading it as two's complement gives $U2T_w((x+y)\bmod2^w)$.

2. The true sum lies in $[-2^w,2^w-2]$. Reducing it into $[TMin_w,TMax_w]$ by a multiple of $2^w$ gives the three cases.

3. If $x\ge0$ and $y<0$ (or the other way), $x+y$ lies between $y$ and $x$, so it is representable: no overflow.

4. If $x,y\ge0$ and overflow occurs, the result is $x+y-2^w\le 2(2^{w-1}-1)-2^w<0$. If $x,y<0$ and overflow occurs, the result is $x+y+2^w\ge 2(-2^{w-1})+2^w=0$. Without overflow the sum has the sign of $x$ and $y$.
:::

::: {#fig-integer-arithmetic-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.3cm, y=0.3cm]
\draw[->] (-17,0) -- (16,0) node[lab, right] {true sum $x+y$};
\draw[->] (0,-9.5) -- (0,9.5) node[lab, above] {computed $x+^{\mathrm t}_4y$};
\foreach \v in {-16,-8,8,14} { \draw (\v,-0.3) -- (\v,0.3); \node[tick] at (\v,-1.1) {$\v$}; }
\foreach \v in {-8,7} { \draw (-0.3,\v) -- (0.3,\v); \node[tick, anchor=east] at (-0.4,\v) {$\v$}; }
\draw[gridline, dashed] (-17,7) -- (16,7); \draw[gridline, dashed] (-17,-8) -- (16,-8);
\draw[emph, draw=accent] (-16,0) -- (-9,7);
\draw[emph, draw=primary] (-8,-8) -- (7,7);
\draw[emph, draw=accent] (8,-8) -- (14,-2);
\node[tick, anchor=south] at (-12.5,7.3) {negative overflow: $+16$};
\node[tick, anchor=north] at (11,-8.3) {positive overflow: $-16$};
\end{tikzpicture}
\end{center}
```

Four-bit two's-complement addition. True sums in $[-8,7]$ come out unchanged (blue); sums above $7$ lose $16$ and sums below $-8$ gain $16$ (terracotta)

:::

::: {#prp-twos-complement-negation .proposition name="Negation"}

In two's complement, $-^{\mathrm t}_wx=\mathord{\sim}x+1$ for every $x$; in particular $-^{\mathrm t}_w\,TMin_w=TMin_w$.

:::

::: {.proof}
1. For any pattern $x$, $x+\mathord{\sim}x$ is the all-ones pattern, whose value is $-1$ (@prp-twos-complement-facts).

2. Hence $x+(\mathord{\sim}x+1)\equiv0\pmod{2^w}$, so $\mathord{\sim}x+1$ is the additive inverse of $x$ in arithmetic mod $2^w$, which is the machine's negation.

3. For $x=TMin_w=10\cdots0$, $\mathord{\sim}x+1=01\cdots1+1=10\cdots0$ again: the true negation $2^{w-1}$ is not representable and wraps to itself.
:::

::: {#thm-machine-multiplication .theorem name="Multiplication"}

The machine's product of two $w$-bit values keeps the low $w$ bits of the true product:
$$x*^{\mathrm u}_wy=(x\cdot y)\bmod 2^w,\qquad x*^{\mathrm t}_wy=U2T_w\bigl((x\cdot y)\bmod 2^w\bigr).$$
Signed and unsigned products of the same two patterns have the same low $w$ bits.

:::

::: {.proof}
1. The unsigned case is truncation of the true product (@thm-truncation).

2. For the signed case, the patterns have unsigned values $x'\equiv x$ and $y'\equiv y\pmod{2^w}$, so $x'y'\equiv xy\pmod{2^w}$ and both products reduce to the same residue.
:::

::: {#thm-shift-multiply-divide .theorem name="Shifts multiply and divide by powers of two"}

For $0\le k<w$:

1. `x << k` equals $x*_w2^k$, for unsigned and for two's-complement $x$.
2. For unsigned $u$, the logical shift `u >> k` equals $\lfloor u/2^k\rfloor$.
3. For two's-complement $x$, the arithmetic shift `x >> k` equals $\lfloor x/2^k\rfloor$ (rounding toward $-\infty$).
4. For $x<0$, $(x+2^k-1)$ `>> k` equals $\lceil x/2^k\rceil$, which is C's division `x / (1<<k)` (rounding toward $0$).

:::

::: {.proof}
1. Shifting left by $k$ multiplies every weight by $2^k$ and drops the bits that pass position $w-1$, which is the product reduced mod $2^w$.

2. Writing $u=2^kq+r$ with $0\le r<2^k$, the low $k$ bits of $u$ hold $r$ and the rest hold $q$; the shift keeps exactly $q=\lfloor u/2^k\rfloor$.

3. For $x\ge0$ this is item 2. For $x<0$ the pattern's unsigned value is $x+2^w$; the arithmetic shift gives the pattern whose value is $\lfloor(x+2^w)/2^k\rfloor-2^{w-k}$ (the $k$ copied sign bits add $2^w-2^{w-k}$ to the unsigned value, which is $-2^{w-k}$ in two's complement), and this equals $\lfloor x/2^k\rfloor$ because $2^w/2^k$ is an integer.

4. For integers $x$ and $m=2^k$, $\lceil x/m\rceil=\lfloor(x+m-1)/m\rfloor$; apply item 3 to $x+m-1$.
:::

::: {#exm-biasing .example name="Dividing $-15213$ by $16$"}

`-15213 >> 4` is $\lfloor-15213/16\rfloor=\lfloor-950.8\rfloor=-951$, but C's `-15213 / 16` is $-950$. Adding the bias $2^4-1=15$ first gives $(-15213+15)$ `>> 4` $=\lfloor-15198/16\rfloor=-950$. Compilers emit exactly this: add the bias only when $x<0$, then shift.

:::

::: {#rmk-integer-arithmetic-1 name="Compilers multiply with shifts"}

Multiplying by a constant becomes shifts and adds when that is cheaper: `x * 12` is `(x << 3) + (x << 2)`, and on x86-64 often a single `lea` (@def-x86-64-lea). Item 1 of @thm-shift-multiply-divide guarantees the result is the same even when the product overflows.

:::

::: {#fig-integer-arithmetic-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.4cm]
\draw[->] (-3.5,0) -- (1.5,0);
\foreach \v in {-3,-2,-1,0,1} { \draw (\v,-0.08) -- (\v,0.08); \node[tick] at (\v,-0.35) {$\v$}; }
\node[hl dot] at (-2.25,0) {}; \node[tick] at (-2.25,0.35) {$-9/4=-2.25$};
\draw[map, draw=accent, bend right=40] (-2.3,-0.1) to (-3,-0.12);
\node[lab, anchor=north] at (-3,-0.6) {\texttt{x >> 2} $=-3$};
\draw[map, draw=primary, bend left=40] (-2.2,-0.1) to (-2,-0.12);
\node[lab, anchor=north west] at (-1.9,-0.6) {\texttt{(x + 3) >> 2} $=-2$};
\end{tikzpicture}
\end{center}
```

For $x=-9$ and $k=2$: the plain arithmetic shift rounds $-2.25$ down to $-3$; adding the bias $2^k-1=3$ first rounds toward zero, to $-2$

:::
