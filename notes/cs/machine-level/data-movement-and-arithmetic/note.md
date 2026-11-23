---
title: "Operands, Data Movement and Arithmetic"
sources: [cmu15213-5, cmu15213r-4]
requires: [cs/machine-level/x86-64-basics, cs/data-representation/integer-arithmetic]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 5 "Machine-Level Programming I: Basics" and Recitation 4, in our own wording. Assembly is in AT&T syntax (source first, destination last), as produced by gcc. -->

::: {#def-operand-forms .definition name="Operands and addressing modes"}

An x86-64 instruction operand is one of

- an *immediate*: a constant, written `$-533` or `$0x1F`;
- a *register*: written `%rax`; its value is the register's contents;
- a *memory reference*: the bytes at a computed *effective address*. The general form
$$D(R_b,R_i,S)\quad\text{denotes the address}\quad D+R[R_b]+S\cdot R[R_i],$$
where the displacement $D$ is a constant, $R_b$ and $R_i$ are registers, and the scale $S$ is $1$, $2$, $4$ or $8$. Any part may be omitted: `(%rax)` is $R[\%rax]$, `8(%rbp)` is $R[\%rbp]+8$, `(%rdx,%rcx,4)` is $R[\%rdx]+4R[\%rcx]$.

:::

::: {#exm-address-computation .example name="Computing effective addresses"}

With `%rdx` $=$ `0xf000` and `%rcx` $=$ `0x0100`:

| operand | address |
|---|---|
| `0x8(%rdx)` | `0xf008` |
| `(%rdx,%rcx)` | `0xf100` |
| `(%rdx,%rcx,4)` | `0xf400` |
| `0x80(,%rdx,2)` | `0x1e080` |

The scale factors $1,2,4,8$ match the sizes of `char`, `short`, `int` and `long`/pointers, so `(%rdx,%rcx,4)` is the address of `a[i]` for an `int` array `a` in `%rdx` and index `i` in `%rcx`.

:::

::: {#fig-data-movement-and-arithmetic-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (d) at (0,0) {$D$\\\texttt{0x80}};
\node[box] (b) at (2,0) {$R[R_b]$\\base};
\node[box] (i) at (4.4,0) {$R[R_i]$\\index};
\node[box] (s) at (6.4,0) {$S$\\$1,2,4,8$};
\node[lab] at (1,0) {$+$}; \node[lab] at (3.1,0) {$+$}; \node[lab] at (5.4,0) {$\times$};
\node[hl box] (a) at (3.2,-1.6) {effective address $D+R[R_b]+S\cdot R[R_i]$};
\draw[->] (d) -- (a); \draw[->] (b) -- (a); \draw[->] (i) -- (a); \draw[->] (s) -- (a);
\node[box] (m) at (3.2,-3.0) {memory: \texttt{movq} reads or writes these 8 bytes};
\draw[->] (a) -- (m) node[midway, right, tick] {\texttt{mov}};
\node[lab, anchor=west] at (6.6,-1.6) {\texttt{leaq}: stop here};
\end{tikzpicture}
\end{center}
```

The general memory operand. `mov` uses the effective address to reach memory; `lea` keeps the address itself

:::

::: {#def-x86-64-mov .definition name="Data movement: `mov`"}

`movq S, D` copies the 8-byte value of operand $S$ to $D$. The suffix gives the size: `b` (1 byte), `w` (2), `l` (4), `q` (8). Source and destination cannot both be memory. `movl` with a register destination also sets the upper 4 bytes of the register to $0$. `movzbl`, `movsbq` and their relatives copy a smaller value into a larger destination with zero extension or sign extension (@thm-sign-extension).

:::

::: {#exm-swap .example name="Swapping through pointers"}

```c
void swap(long *xp, long *yp) {
    long t0 = *xp;
    long t1 = *yp;
    *xp = t1;
    *yp = t0;
}
```

```text
swap:
    movq    (%rdi), %rax      t0 = *xp      (xp in %rdi)
    movq    (%rsi), %rdx      t1 = *yp      (yp in %rsi)
    movq    %rdx, (%rdi)      *xp = t1
    movq    %rax, (%rsi)      *yp = t0
    ret
```

The arguments arrive in `%rdi` and `%rsi` (@def-x86-64-calling-convention). Dereferencing a pointer is a memory operand with the pointer register as base; the local variables live only in registers.

:::

::: {#def-x86-64-lea .definition name="Load effective address: `lea`"}

`leaq S, D` computes the effective address of the memory operand $S$ and stores the address itself (not the memory contents) in register $D$. Compilers use it for pointer arithmetic such as `p = &x[i]` and for arithmetic of the form $a+k\cdot b+c$ with $k\in\{1,2,4,8\}$.

:::

::: {#exm-lea-multiply .example name="Multiplying by 12 with `lea`"}

```c
long m12(long x) { return x * 12; }
```

```text
m12:
    leaq    (%rdi,%rdi,2), %rax    t = x + 2*x
    salq    $2, %rax               return t << 2
    ret
```

$x+2x=3x$, and shifting left by two multiplies by $4$ (@thm-shift-multiply-divide), so the result is $12x$ in two cheap instructions instead of a multiplication.

:::

::: {#def-x86-64-arithmetic .definition name="Arithmetic and logical instructions"}

| instruction | effect | | instruction | effect |
|---|---|---|---|---|
| `addq S, D` | $D\gets D+S$ | | `salq k, D` | $D\gets D\ll k$ |
| `subq S, D` | $D\gets D-S$ | | `sarq k, D` | $D\gets D\gg_{\mathrm a} k$ (arithmetic) |
| `imulq S, D` | $D\gets D\cdot S$ | | `shrq k, D` | $D\gets D\gg_{\mathrm l} k$ (logical) |
| `xorq S, D` | $D\gets D\oplus S$ | | `incq D`, `decq D` | $D\gets D\pm1$ |
| `andq S, D` | $D\gets D\,\&\,S$ | | `negq D` | $D\gets -D$ |
| `orq S, D` | $D\gets D\mid S$ | | `notq D` | $D\gets\mathord{\sim}D$ |

There is one `add` for signed and unsigned values, because the bit-level results agree (@thm-twos-complement-addition); only the right shifts come in two kinds. All of these also set the condition codes (@def-condition-codes).

:::

::: {#exm-arith .example name="A longer arithmetic expression"}

```c
long arith(long x, long y, long z) {
    long t1 = x + y;
    long t2 = z + t1;
    long t3 = x + 4;
    long t4 = y * 48;
    long t5 = t3 + t4;
    long rval = t2 * t5;
    return rval;
}
```

```text
arith:
    leaq    (%rdi,%rsi), %rax      t1 = x + y
    addq    %rdx, %rax             t2 = z + t1
    leaq    (%rsi,%rsi,2), %rdx    3*y
    salq    $4, %rdx               t4 = 48*y
    leaq    4(%rdi,%rdx), %rcx     t5 = x + 4 + t4
    imulq   %rcx, %rax             rval = t2 * t5
    ret
```

The compiler reorders and combines the C statements: `t3` never exists on its own, it is folded into the displacement `4` of a `lea`.

:::

::: {#fig-data-movement-and-arithmetic-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r/\v/\c [count=\i from 0] in {rdi/x/,rsi/y/,rdx/{z, then t4}/,rax/{t1, t2, rval}/hl,rcx/t5/} {
  \node[lab, anchor=east] at (0,-\i*0.6) {\texttt{\%\r}};
  \draw[cell frame] (0.1,-\i*0.6-0.25) rectangle (2.9,-\i*0.6+0.25);
  \node[lab] at (1.5,-\i*0.6) {\v};
}
\draw[hl cell] (0.1,-2.05) rectangle (2.9,-1.55); \node[lab] at (1.5,-1.8) {t1, t2, rval};
\node[lab, anchor=west] at (3.2,0) {argument 1};
\node[lab, anchor=west] at (3.2,-0.6) {argument 2};
\node[lab, anchor=west] at (3.2,-1.2) {argument 3, reused for a temporary};
\node[lab, anchor=west] at (3.2,-1.8) {return value};
\node[lab, anchor=west] at (3.2,-2.4) {temporary};
\end{tikzpicture}
\end{center}
```

Register use in `arith`: the compiler keeps every C variable in a register and reuses `%rdx` once `z` is no longer needed

:::
