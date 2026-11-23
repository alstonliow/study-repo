---
title: "Condition Codes, Jumps and Conditional Moves"
sources: [cmu15213-6, cmu15213r-4]
requires: [cs/machine-level/data-movement-and-arithmetic]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 6 "Machine-Level Programming II: Control" and Recitation 4 (comparisons and jumps), in our own wording; proofs written out in steps. -->

Straight-line code runs instructions in order. Branches in C (`if`, `?:`, loops) need instructions that test a result and change `%rip`. x86-64 does this in two steps: an instruction sets *condition codes*, and a later instruction reads them.

::: {#def-condition-codes .definition name="Condition codes"}

Four single-bit registers describe the most recent arithmetic or logical result $t$ of width $w$:

- `CF` (carry flag): the unsigned operation overflowed (a carry out of, or borrow into, the top bit);
- `ZF` (zero flag): $t=0$;
- `SF` (sign flag): the top bit of $t$ is $1$ ($t<0$ as a signed value);
- `OF` (overflow flag): the two's-complement operation overflowed (@thm-twos-complement-addition).

Arithmetic instructions set them as a side effect; `lea` does not. `cmpq b, a` sets them as for $a-b$ and `testq b, a` as for $a\,\&\,b$, without storing the result.

:::

::: {#fig-condition-codes-and-jumps-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (cmp) at (0,0) {\texttt{cmpq \%rsi, \%rdi}\\computes $x-y$};
\foreach \f/\m [count=\i from 0] in {CF/{borrow (unsigned $x<y$)},ZF/{$x-y=0$},SF/{$x-y<0$},OF/{signed overflow}} {
  \draw[cell frame] (3,0.9-\i*0.6) rectangle (3.6,1.4-\i*0.6); \node[lab] at (3.3,1.15-\i*0.6) {\texttt{\f}};
  \node[tick, anchor=west] at (3.7,1.15-\i*0.6) {\m};
  \draw[->] (cmp.east) -- (3,1.15-\i*0.6);
}
\node[hl box] (j) at (8.6,0) {\texttt{jl .L2}\\jump if \texttt{SF \^{} OF}};
\draw[->] (6.1,0) -- (j.west);
\end{tikzpicture}
\end{center}
```

A comparison only sets the four flags; a later conditional instruction combines them

:::

::: {#thm-signed-less-than-flags .theorem name="Signed less-than from the flags"}

After `cmpq b, a` (computing $t=a-^{\mathrm t}_wb$), the signed comparison $a<b$ holds if and only if $\mathtt{SF}\oplus\mathtt{OF}=1$. The unsigned comparison $a<b$ holds if and only if $\mathtt{CF}=1$.

:::

::: {.proof}
1. Without overflow ($\mathtt{OF}=0$), $t=a-b$ exactly, so $a<b$ iff $t<0$ iff $\mathtt{SF}=1$.

2. With positive overflow, the true difference $a-b$ exceeded $TMax_w$, so $a>b$; the stored $t$ wrapped to a negative value, so $\mathtt{SF}=1$, $\mathtt{OF}=1$ and $\mathtt{SF}\oplus\mathtt{OF}=0$, correctly "not less".

3. With negative overflow, $a-b<TMin_w$, so $a<b$; the stored $t$ wrapped to a nonnegative value, so $\mathtt{SF}=0$, $\mathtt{OF}=1$ and $\mathtt{SF}\oplus\mathtt{OF}=1$.

4. For unsigned values, $a-b$ borrows exactly when $a<b$, which is what $\mathtt{CF}$ records.
:::

::: {#def-set-and-jump .definition name="Reading the flags: `set`, `j` and `cmov`"}

| suffix | condition | meaning after `cmp b, a` |
|---|---|---|
| `e` / `ne` | `ZF` / `~ZF` | $a=b$ / $a\ne b$ |
| `s` / `ns` | `SF` / `~SF` | result negative / nonnegative |
| `l` / `ge` | `SF^OF` / `~(SF^OF)` | signed $a<b$ / $a\ge b$ |
| `le` / `g` | `(SF^OF)\|ZF` / its negation | signed $a\le b$ / $a>b$ |
| `b` / `ae` | `CF` / `~CF` | unsigned $a<b$ / $a\ge b$ ("below", "above or equal") |
| `be` / `a` | `CF\|ZF` / its negation | unsigned $a\le b$ / $a>b$ |

`setX D` writes $1$ or $0$ into a one-byte register $D$; `jX L` jumps to label $L$ if the condition holds and otherwise falls through; `cmovX S, D` copies $S$ to $D$ only if the condition holds. `jmp L` always jumps; `jmp *%rax` jumps to the address in a register.

:::

::: {#exm-reading-jumps .example name="Reading comparisons"}

- `cmpq $0x15213, %r12` then `jge L`: jump if `%r12` $\ge$ `0x15213` as signed values. The operand order is reversed from the natural reading: `cmp b, a` compares $a$ with $b$.
- `cmpq %rax, %rdi` then `jae L`: jump if `%rdi` $\ge$ `%rax` as unsigned values.
- `testq %r8, %r8` then `jnz L`: jump if `%r8` $\ne0$; testing a register against itself is the idiom for comparing with zero.

:::

::: {#exm-absdiff-branch .example name="`if`–`else` as a conditional jump"}

```c
long absdiff(long x, long y) {
    long result;
    if (x > y) result = x - y;
    else       result = y - x;
    return result;
}
```

```text
absdiff:
    cmpq    %rsi, %rdi        compare x with y
    jle     .L4               if x <= y goto else part
    movq    %rdi, %rax
    subq    %rsi, %rax        result = x - y
    ret
.L4:
    movq    %rsi, %rax
    subq    %rdi, %rax        result = y - x
    ret
```

The compiler inverts the test and jumps over the `then` part: C `if (t) A else B` becomes "if not $t$ goto else; A; goto done; else: B; done:".

:::

::: {#fig-condition-codes-and-jumps-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (t) at (0,0) {\texttt{cmpq \%rsi,\%rdi}};
\node[hl box] (j) at (0,-1.2) {\texttt{jle .L4}};
\node[box] (a) at (-2,-2.6) {\texttt{result = x - y}};
\node[box] (b) at (2,-2.6) {\texttt{.L4: result = y - x}};
\node[box] (r) at (0,-4) {\texttt{ret}};
\draw[->] (t) -- (j);
\draw[->] (j) -- (a) node[midway, left, tick] {fall through ($x>y$)};
\draw[->, draw=accent] (j) -- (b) node[midway, right, tick] {jump ($x\le y$)};
\draw[->] (a) -- (r); \draw[->] (b) -- (r);
\end{tikzpicture}
\end{center}
```

Control flow of `absdiff` with a conditional jump

:::

::: {#def-conditional-move .definition name="Conditional move translation"}

For `result = t ? A : B` with cheap, side-effect-free `A` and `B`, a compiler may compute *both* values and select one with `cmov`:
`v = A; ve = B; if (!t) v = ve;` where the last line is a single `cmovX`. This avoids a jump.

:::

::: {#rmk-condition-codes-and-jumps-1 name="When conditional moves are used"}

A modern processor guesses the outcome of each branch long before it is known and runs ahead (@def-branch-prediction); a wrong guess costs about 15–20 cycles. A conditional move has no guess to get wrong, so it wins when the branch is unpredictable and both values are cheap. It is wrong when computing both is expensive, when one is unsafe (`p ? *p : 0` would dereference a null pointer), or when one has side effects (`x > 0 ? x *= 7 : x += 3`).

:::
