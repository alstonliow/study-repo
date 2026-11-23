---
title: "Procedures and the Run-Time Stack"
sources: [cmu15213-7, cmu15213r-4]
requires: [cs/machine-level/condition-codes-and-jumps]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 7 "Machine-Level Programming III: Procedures" and Recitation 4 (argument registers), in our own wording; proofs written out in steps. -->

A procedure call has to do three things: pass *control* to the callee and back, pass *data* (arguments and the return value), and give the callee *memory* for its local variables that disappears when it returns. x86-64 does all three with one region of memory, the stack, and a convention for registers.

::: {#def-run-time-stack .definition name="Run-time stack, `push`, `pop`"}

The *stack* is a region of memory that grows toward lower addresses; `%rsp` holds the address of its top element. `pushq S` decrements `%rsp` by $8$ and then stores $S$ at address `%rsp`. `popq D` loads the 8 bytes at `%rsp` into $D$ and then increments `%rsp` by $8$. The bytes below `%rsp` are free; popping does not erase them.

:::

::: {#fig-procedures-and-the-stack-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \c/\x/\v/\top in {0/0/{},1/4.2/{0x123},2/8.4/{}} {
  \foreach \i in {0,...,3} { \draw[cell frame] (\x,-\i*0.55) rectangle (\x+2.2,-\i*0.55+0.5); }
}
\node[lab] at (1.1,-0.3) {\dots}; \node[lab] at (5.3,-0.3) {\dots}; \node[lab] at (9.5,-0.3) {\dots};
\node[lab] at (1.1,-0.85) {\texttt{0x15213}};
\node[lab] at (5.3,-0.85) {\texttt{0x15213}}; \draw[hl cell] (4.2,-1.65) rectangle (6.4,-1.15); \node[lab] at (5.3,-1.4) {\texttt{0x123}};
\node[lab] at (9.5,-0.85) {\texttt{0x15213}}; \node[lab, text=muted] at (9.5,-1.4) {\texttt{0x123}};
\draw[->] (-0.9,-0.85) -- (0,-0.85); \node[tick, anchor=east] at (-0.9,-0.85) {\texttt{\%rsp}=\texttt{0x108}};
\draw[->] (3.3,-1.4) -- (4.2,-1.4); \node[tick, anchor=east] at (3.3,-1.75) {\texttt{0x100}};
\draw[->] (7.5,-0.85) -- (8.4,-0.85); \node[tick, anchor=east] at (7.5,-0.55) {\texttt{0x108}};
\node[lab] at (1.1,0.85) {initially}; \node[lab] at (5.3,0.85) {\texttt{pushq \%rax}}; \node[lab] at (9.5,0.85) {\texttt{popq \%rdx}};
\draw[->] (11.2,0.3) -- (11.2,-1.9) node[tick, right, midway] {lower addresses};
\end{tikzpicture}
\end{center}
```

With `%rax` $=$ `0x123`: `push` moves `%rsp` down 8 bytes and stores; `pop` loads into `%rdx` and moves `%rsp` back up, leaving the old value behind as garbage

:::

::: {#def-call-ret .definition name="`call` and `ret`"}

`call f` pushes the *return address* (the address of the instruction right after the `call`) and jumps to `f`. `ret` pops an address and jumps to it. As long as every procedure leaves `%rsp` where it found it, the address that `ret` pops is the one its `call` pushed.

:::

::: {#def-x86-64-calling-convention .definition name="x86-64 Linux calling convention (integer data)"}

- The first six integer or pointer arguments are passed in `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8`, `%r9`, in that order; further arguments are pushed on the stack by the caller, the seventh nearest the top.
- The return value is left in `%rax`.
- *Callee-saved* registers `%rbx`, `%rbp`, `%r12`–`%r15`: a procedure that changes one must restore its old value before returning (typically by pushing it on entry and popping it before `ret`).
- *Caller-saved* registers, all others except `%rsp`: a callee may overwrite them, so a caller that needs a value in one across a call must save it first.
- `%rsp` must be restored, and must be a multiple of 16 just before every `call`.

:::

::: {#def-stack-frame .definition name="Stack frame"}

The part of the stack that one invocation of a procedure uses is its *frame*. From higher to lower addresses it holds the return address (pushed by the caller's `call`), saved callee-saved registers, local variables that cannot stay in registers (arrays, structures, variables whose address is taken), and the *argument build area* for arguments 7 and up of the procedures it calls. Frames are allocated when a procedure is entered and freed when it returns, in last-in first-out order.

:::

::: {#fig-procedures-and-the-stack-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0) rectangle (4,2.0); \node[lab] at (2,1.7) {caller's frame};
\draw[cell frame] (0.2,0.65) rectangle (3.8,1.25); \node[lab] at (2,0.95) {arguments 7, 8, \dots};
\draw[hl cell] (0,0) rectangle (4,0.55); \node[lab] at (2,0.275) {return address};
\draw[regionB] (0,-3.2) rectangle (4,-0.05); \node[lab] at (2,-0.35) {current frame};
\draw[cell frame] (0.2,-1.1) rectangle (3.8,-0.6); \node[lab] at (2,-0.85) {saved registers};
\draw[cell frame] (0.2,-1.9) rectangle (3.8,-1.2); \node[lab] at (2,-1.55) {local variables};
\draw[cell frame] (0.2,-2.95) rectangle (3.8,-2.0); \node[lab] at (2,-2.48) {argument build area};
\draw[->] (5.2,-3.2) -- (4.05,-3.2); \node[lab, anchor=west] at (5.25,-3.2) {\texttt{\%rsp} (stack top)};
\draw[->] (-0.4,2) -- (-0.4,-3.2) node[tick, midway, left] {stack grows down};
\end{tikzpicture}
\end{center}
```

The general layout of a stack frame. Every part is optional: a leaf procedure that keeps everything in registers has no frame beyond its return address

:::

::: {#exm-incr-call .example name="Passing the address of a local variable"}

```c
long incr(long *p, long val) {
    long x = *p;
    long y = x + val;
    *p = y;
    return x;
}

long call_incr(void) {
    long v1 = 15213;
    long v2 = incr(&v1, 3000);
    return v1 + v2;
}
```

```text
call_incr:
    subq    $16, %rsp         allocate 16 bytes of frame
    movq    $15213, 8(%rsp)   v1 lives on the stack: its address is taken
    movl    $3000, %esi       argument 2
    leaq    8(%rsp), %rdi     argument 1 = &v1
    call    incr
    addq    8(%rsp), %rax     v1 + v2 (v2 returned in %rax)
    addq    $16, %rsp         free the frame
    ret
```

`v1` must live in memory because `incr` receives its address; after the call it holds $18213$ and the result is $18213+15213=33426$.

:::

::: {#fig-procedures-and-the-stack-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (3,0.55); \node[lab] at (1.5,0.275) {return address};
\draw[cell frame] (0,-0.55) rectangle (3,0); \node[lab] at (1.5,-0.275) {unused};
\draw[hl cell] (0,-1.1) rectangle (3,-0.55); \node[lab] at (1.5,-0.825) {\texttt{v1}: 15213 $\to$ 18213};
\draw[cell frame] (0,-1.65) rectangle (3,-1.1); \node[lab] at (1.5,-1.375) {unused};
\node[tick, anchor=east] at (-0.1,-0.825) {\texttt{\%rsp+8}};
\draw[->] (4.2,-1.65) -- (3.05,-1.65); \node[lab, anchor=west] at (4.25,-1.65) {\texttt{\%rsp} after \texttt{subq \$16}};
\draw[->] (4.2,-1.25) to[out=180,in=0] (3.05,-0.825); \node[lab, anchor=west] at (4.25,-1.15) {\texttt{\%rdi} = \texttt{\&v1}};
\end{tikzpicture}
\end{center}
```

The frame of `call_incr` while `incr` runs (`incr`'s return address would sit just below): `incr` updates `v1` through the pointer in `%rdi`

:::

::: {#exm-recursive-pcount .example name="A recursive procedure"}

```c
long pcount_r(unsigned long x) {
    if (x == 0) return 0;
    return (x & 1) + pcount_r(x >> 1);
}
```

```text
pcount_r:
    movl    $0, %eax
    testq   %rdi, %rdi
    je      .L6
    pushq   %rbx              save callee-saved %rbx
    movq    %rdi, %rbx
    andl    $1, %ebx          keep x & 1 across the call
    shrq    %rdi              argument x >> 1
    call    pcount_r
    addq    %rbx, %rax
    popq    %rbx              restore %rbx
.L6:
    rep; ret
```

The value `x & 1` must survive the recursive call, so it is kept in a callee-saved register; the procedure saves the caller's `%rbx` first. Each level of recursion has its own saved copy on the stack.

:::

::: {#prp-stack-discipline-recursion .proposition name="Recursion needs no special mechanism"}

If every procedure follows the calling convention, then each invocation, recursive or not, sees its own local state intact after any call it makes.

:::

::: {.proof}
1. An invocation's state lives in its frame, in callee-saved registers, or in caller-saved registers it saved in its frame before calling.

2. A call creates new frames only below the current `%rsp`, and the callee restores `%rsp` before returning, so the caller's frame is never overwritten.

3. Callee-saved registers are restored by the callee by convention, and saved caller-saved registers are reloaded from the frame by the caller.

4. These arguments do not depend on which procedure is called, so they apply equally when the callee is the procedure itself, and by induction on call depth to any nesting.
:::

::: {#fig-procedures-and-the-stack-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \k/\b [count=\i from 0] in {{pcount\_r(5)}/{caller's \%rbx},{pcount\_r(2)}/{1 (from 5\&1)},{pcount\_r(1)}/{0 (from 2\&1)}} {
  \draw[regionA] (0,-\i*1.3) rectangle (4,-\i*1.3+1.2);
  \node[lab] at (2,-\i*1.3+0.95) {\texttt{\k}};
  \draw[cell frame] (0.2,-\i*1.3+0.05) rectangle (3.8,-\i*1.3+0.6); \node[tick] at (2,-\i*1.3+0.33) {saved \%rbx = \b};
}
\draw[hl box] (0,-3.3) rectangle (4,-2.75); \node[lab] at (2,-3.03) {\texttt{pcount\_r(0)}: returns 0};
\draw[->] (4.8,-3.0) -- (4.8,0.9) node[midway, right, tick] {returns $0,1,1,2$};
\end{tikzpicture}
\end{center}
```

Frames of `pcount_r(5)` at the deepest point. Each level saved the previous `%rbx`, which holds the caller's bit; on the way back up the bits $1,0,1$ of $5=101_2$ are added

:::

::: {#rmk-procedures-and-the-stack-1 name="Frame pointer"}

Most frames have a size known at compile time, so `%rsp` alone locates everything. A procedure that allocates a variable-size array on the stack keeps a *frame pointer* in `%rbp` (`pushq %rbp; movq %rsp, %rbp` on entry, `leave` before `ret`) so that its locals have fixed offsets from `%rbp`.

:::
