---
title: "Machine-Level Programs: the x86-64 Machine State"
sources: [cmu15213-5, cmu15213r-4]
requires: [cs/data-representation/byte-ordering]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 5 "Machine-Level Programming I: Basics" and Recitation 4 (registers, gdb), in our own wording. -->

A C compiler translates a program into *machine code*: bytes that a processor executes directly. Reading the human-readable form of that code, *assembly*, shows what the hardware actually does with the data representations of the previous branch.

::: {#def-isa .definition name="Instruction set architecture, microarchitecture"}

The *instruction set architecture* (ISA) is the part of a processor's design a programmer must know to write machine code: the visible state (registers, memory, condition codes) and the instructions with their effect on that state. The *microarchitecture* is how one processor implements the ISA (pipelines, caches, sizes); it changes between models without changing the meaning of programs. x86-64 is the 64-bit ISA of Intel and AMD processors; ARM is the ISA of most phones.

:::

::: {#def-x86-64-state .definition name="The x86-64 programmer-visible state"}

- the *program counter* `%rip`: the address of the next instruction;
- sixteen 64-bit *general-purpose registers* `%rax`, `%rbx`, `%rcx`, `%rdx`, `%rsi`, `%rdi`, `%rbp`, `%rsp`, `%r8`–`%r15`; their low 32, 16 and 8 bits can be named separately (`%eax`, `%ax`, `%al` for `%rax`; `%r8d`, `%r8w`, `%r8b` for `%r8`);
- the *condition codes*: single-bit flags set by recent arithmetic, used for conditional jumps (@def-condition-codes);
- *memory*: a byte-addressed array (@def-byte-addressable-memory) holding code, data and the run-time stack.

`%rsp` always holds the address of the top of the stack. Other registers have conventional uses for passing arguments and results (@def-x86-64-calling-convention).

:::

::: {#fig-x86-64-basics-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \r/\e/\u [count=\i from 0] in {rax/eax/return value,rbx/ebx/callee saved,rcx/ecx/argument 4,rdx/edx/argument 3,rsi/esi/argument 2,rdi/edi/argument 1,rbp/ebp/callee saved,rsp/esp/stack pointer} {
  \draw[cell frame] (0,-\i*0.55) rectangle (3.2,-\i*0.55+0.5);
  \draw[regionA] (1.6,-\i*0.55+0.04) rectangle (3.16,-\i*0.55+0.46);
  \node[lab] at (0.6,-\i*0.55+0.25) {\texttt{\%\r}};
  \node[lab] at (2.38,-\i*0.55+0.25) {\texttt{\%\e}};
  \node[tick, anchor=west] at (3.3,-\i*0.55+0.25) {\u};
}
\foreach \r/\u [count=\i from 0] in {r8/argument 5,r9/argument 6,r10/caller saved,r11/caller saved,r12/callee saved,r13/callee saved,r14/callee saved,r15/callee saved} {
  \draw[cell frame] (6.2,-\i*0.55) rectangle (9.4,-\i*0.55+0.5);
  \draw[regionA] (7.8,-\i*0.55+0.04) rectangle (9.36,-\i*0.55+0.46);
  \node[lab] at (6.8,-\i*0.55+0.25) {\texttt{\%\r}};
  \node[lab] at (8.58,-\i*0.55+0.25) {\texttt{\%\r d}};
  \node[tick, anchor=west] at (9.5,-\i*0.55+0.25) {\u};
}
\node[tick] at (0.6,0.75) {64 bits}; \node[tick] at (2.38,0.75) {low 32 bits};
\draw[hl cell] (0,-4.6) rectangle (3.2,-4.1); \node[lab] at (1.6,-4.35) {\texttt{\%rip}: next instruction};
\end{tikzpicture}
\end{center}
```

The sixteen general-purpose registers with their 32-bit halves (shaded) and conventional roles, and the program counter

:::

::: {#def-compilation-pipeline .definition name="From C source to executable"}

`gcc -Og p1.c p2.c -o p` runs four tools in turn: the *preprocessor* expands `#include` and macros; the *compiler* translates each C file to assembly (`.s`); the *assembler* translates assembly to an *object file* (`.o`) of machine code with some addresses still unknown; the *linker* combines the object files with library code into an executable and fixes those addresses (@def-relocation). `-Og` asks for optimizations that keep the code readable.

:::

::: {#fig-x86-64-basics-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (c) at (0,0) {\texttt{p1.c}\\\texttt{p2.c}};
\node[hl box] (cc) at (2.3,0) {compiler\\\texttt{gcc -Og -S}};
\node[box] (s) at (4.6,0) {\texttt{p1.s}\\\texttt{p2.s}};
\node[hl box] (as) at (6.6,0) {assembler\\\texttt{as}};
\node[box] (o) at (8.6,0) {\texttt{p1.o}\\\texttt{p2.o}};
\node[hl box] (ld) at (8.6,-1.8) {linker\\\texttt{ld}};
\node[box] (lib) at (5.9,-1.8) {static libraries\\\texttt{libc.a}};
\node[box] (p) at (11.0,-1.8) {executable\\\texttt{p}};
\draw[->] (c) -- (cc); \draw[->] (cc) -- (s); \draw[->] (s) -- (as); \draw[->] (as) -- (o);
\draw[->] (o) -- (ld); \draw[->] (lib) -- (ld); \draw[->] (ld) -- (p);
\node[tick] at (4.6,-0.75) {text};
\node[tick] at (9.4,-0.75) {binary};
\end{tikzpicture}
\end{center}
```

Turning C into an executable: compile to assembly text, assemble to binary object files, link them with libraries

:::

::: {#exm-sum-store .example name="A function in C, assembly and machine code"}

```c
long plus(long x, long y);

void sumstore(long x, long y, long *dest) {
    long t = plus(x, y);
    *dest = t;
}
```

compiles with `gcc -Og -S` to

```text
sumstore:
    pushq   %rbx              save %rbx on the stack
    movq    %rdx, %rbx        keep dest in %rbx
    call    plus              t = plus(x, y), returned in %rax
    movq    %rax, (%rbx)      *dest = t
    popq    %rbx              restore %rbx
    ret
```

The assembler encodes these six instructions in 14 bytes, for example `53` for `pushq %rbx` and `48 89 03` for `movq %rax,(%rbx)`. A disassembler such as `objdump -d` recovers the assembly from the bytes.

:::

::: {#rmk-x86-64-basics-1 name="What assembly does not have"}

Machine code knows no types beyond sizes (1, 2, 4 or 8 bytes) and the distinction between integer and floating-point registers. Arrays and structures are just consecutive bytes, a pointer is just an integer, and signed and unsigned values are the same bits until an instruction (a comparison, a shift, a conditional jump) interprets them (@def-condition-codes).

:::

::: {#rmk-x86-64-basics-2 name="Tools for reading machine code"}

`objdump -d` disassembles an executable or object file; `objdump -t` prints its symbol table; `strings` prints its printable strings. In the debugger gdb, `disas f` shows the assembly of `f`, `stepi` and `nexti` step one instruction, `info registers` prints the registers and `x/8xg addr` prints eight 8-byte words at `addr` in hex.

:::
