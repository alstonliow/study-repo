---
title: "Memory Layout, Buffer Overflow and Its Defences"
sources: [cmu15213-9, cmu15213r-6, cmu15213lab-3]
requires: [cs/machine-level/procedures-and-the-stack, cs/machine-level/arrays-and-structs]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 9 "Machine-Level Programming V: Advanced Topics", Recitation 6 and the Attack Lab handout (only its ideas: code injection and return-oriented programming), in our own wording. -->

::: {#def-x86-64-linux-layout .definition name="Memory layout of an x86-64 Linux process"}

From high to low addresses a running program's address space contains:

- the *stack*, starting just below $2^{47}$ and growing down, limited to $8$ MiB by default;
- *shared libraries* (code and data of `libc` and others), mapped in at load time;
- the *heap*, memory from `malloc`, growing up from just above the data;
- *data*: global and `static` variables, including string constants;
- *text*: the executable machine code, read-only.

:::

::: {#fig-buffer-overflow-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionB] (0,4.2) rectangle (3.4,5.2); \node[lab] at (1.7,4.7) {stack};
\draw[->] (1.7,4.15) -- (1.7,3.75);
\draw[regionC] (0,2.4) rectangle (3.4,3.0); \node[lab] at (1.7,2.7) {shared libraries};
\draw[->] (1.7,1.75) -- (1.7,2.15);
\draw[regionA] (0,1.1) rectangle (3.4,1.7); \node[lab] at (1.7,1.4) {heap};
\draw[cell frame] (0,0.55) rectangle (3.4,1.05); \node[lab] at (1.7,0.8) {data (globals)};
\draw[cell frame] (0,0) rectangle (3.4,0.5); \node[lab] at (1.7,0.25) {text (code)};
\node[tick, anchor=west] at (3.5,5.2) {\texttt{0x00007FFFFFFFFFFF}};
\node[tick, anchor=west] at (3.5,0.0) {\texttt{0x400000}};
\node[tick, anchor=west] at (3.5,4.2) {limit 8 MiB};
\node[tick, anchor=west] at (3.5,1.4) {\texttt{malloc}};
\node[tick, anchor=west] at (3.5,0.8) {\texttt{int global[100];}};
\node[tick, anchor=west] at (3.5,0.25) {\texttt{main}, \texttt{f}, \dots};
\end{tikzpicture}
\end{center}
```

The address space of an x86-64 Linux process (not to scale): the stack at the top grows down, the heap above the data grows up

:::

::: {#def-buffer-overflow .definition name="Buffer overflow"}

A *buffer overflow* writes past the end of an array. When the array is a local variable, the write overwrites whatever lies above it in the stack frame: other locals, saved registers and, eventually, the return address (@def-stack-frame). C library functions that copy without a length limit (`gets`, `strcpy`, `strcat`, `scanf("%s", …)`) cause most overflows, because the callee cannot know the size of the caller's buffer.

:::

::: {#exm-echo-overflow .example name="Overflowing an echo buffer"}

```c
void echo(void) {
    char buf[4];     /* far too small */
    gets(buf);
    puts(buf);
}
```

One compilation reserves 24 bytes below the return address for the frame: `subq $24, %rsp` with `buf` at `%rsp`. Input up to 23 characters (plus the terminating zero) only writes unused frame bytes and nothing visible goes wrong. Input of 24 or more characters reaches the saved return address of `echo`; `ret` then jumps to a corrupted address, and the program usually crashes with a segmentation fault, or continues somewhere unexpected.

:::

::: {#fig-buffer-overflow-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,1.6) rectangle (4.2,2.2); \node[lab] at (2.1,1.9) {caller's frame};
\draw[hl cell] (0,1.0) rectangle (4.2,1.55); \node[lab] at (2.1,1.275) {return address};
\draw[cell frame] (0,0.6) rectangle (4.2,0.95); \node[tick] at (2.1,0.775) {unused (20 bytes)};
\draw[cell frame] (0,0) rectangle (4.2,0.55); \node[lab] at (2.1,0.275) {\texttt{buf[0..3]}};
\draw[->] (5,0) -- (4.25,0); \node[lab, anchor=west] at (5.05,0) {\texttt{\%rsp}, \texttt{buf}};
\draw[->, emph, draw=accent] (-0.4,0.05) -- (-0.4,1.5) node[midway, left, tick, align=right] {\texttt{gets} writes\\upward};
\node[lab, anchor=west] at (5.05,1.275) {overwritten by byte 24 on};
\end{tikzpicture}
\end{center}
```

The frame of `echo`: `gets` fills `buf` toward higher addresses and, given a long line, overwrites the return address

:::

::: {#def-code-injection .definition name="Code-injection attack"}

An attacker supplies input that contains (1) machine code, the *exploit code*, and (2) padding followed by an address that points into the buffer itself. When the vulnerable procedure returns, `ret` jumps into the injected bytes and the processor runs the attacker's code with the program's privileges.

:::

::: {#fig-buffer-overflow-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,1.6) rectangle (4.2,2.2); \node[lab] at (2.1,1.9) {caller's frame};
\draw[hl cell] (0,1.0) rectangle (4.2,1.55); \node[lab] at (2.1,1.275) {address $B$};
\draw[cell frame] (0,0.6) rectangle (4.2,0.95); \node[tick] at (2.1,0.775) {padding};
\draw[regionB] (0,0) rectangle (4.2,0.55); \node[lab] at (2.1,0.275) {exploit code};
\node[lab, anchor=east] at (-0.1,0.0) {$B$};
\draw[->, emph, draw=accent] (4.25,1.275) to[out=0,in=0, looseness=1.4] (4.25,0.275);
\node[tick, anchor=west] at (5.0,0.8) {\texttt{ret} jumps here};
\end{tikzpicture}
\end{center}
```

A code-injection string overwrites the return address with the address $B$ of the buffer, so `ret` transfers control into the injected code

:::

::: {#def-overflow-defences .definition name="System-level defences"}

- *Stack randomization* (part of address-space layout randomization, ASLR): the operating system starts the stack, and the other regions, at a random offset on every run, so the attacker cannot know the address $B$ of the buffer in advance.
- *Non-executable memory*: page permissions (@def-page-permission-bits) mark the stack and heap as not executable, so jumping into injected bytes faults.
- *Stack canary* (stack protector): on entry, the compiler stores a random value just above the local buffers; before returning it checks the value and aborts the program if it changed. An overflow must pass the canary to reach the return address.

:::

::: {#exm-canary-code .example name="A canary in compiled code"}

```text
echo:
    subq    $24, %rsp
    movq    %fs:40, %rax       load the secret canary
    movq    %rax, 8(%rsp)      place it above buf
    xorl    %eax, %eax
    ...                         gets(buf); puts(buf)
    movq    8(%rsp), %rax
    xorq    %fs:40, %rax       unchanged?
    je      .L6
    call    __stack_chk_fail   no: abort
.L6:
    addq    $24, %rsp
    ret
```

:::

::: {#def-return-oriented-programming .definition name="Return-oriented programming"}

When the stack is not executable, an attacker can still reuse code that is already in the program. A *gadget* is a short instruction sequence ending in `ret` (byte `c3`), often the tail of an existing function or even bytes in the middle of another instruction. An overflow writes a chain of gadget addresses onto the stack; each gadget's `ret` pops the next address, so the gadgets run one after another and together perform the attack.

:::

::: {#fig-buffer-overflow-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \g [count=\i from 0] in {1,2,3} { \draw[cell frame] (0,\i*0.55) rectangle (2.4,\i*0.55+0.5); \node[lab] at (1.2,\i*0.55+0.25) {gadget \g\ address}; }
\node[lab, anchor=east] at (-0.1,0.25) {\texttt{\%rsp} after \texttt{echo} returns};
\foreach \g/\c [count=\i from 0] in {1/{popq \%rax; ret},2/{movq \%rax,\%rdi; ret},3/{call system \dots}} {
  \node[box] (g\i) at (6.2,2.2-\i*1.0) {\texttt{\c}};
}
\draw[map] (2.4,0.25) to[out=0,in=180] (g0.west);
\draw[map] (2.4,0.8) to[out=0,in=180] (g1.west);
\draw[map] (2.4,1.35) to[out=0,in=180] (g2.west);
\draw[map, draw=accent, dashed] (g0.east) to[out=0,in=0] (g1.east);
\draw[map, draw=accent, dashed] (g1.east) to[out=0,in=0] (g2.east);
\node[tick, anchor=west] at (9.0,1.7) {each \texttt{ret} pops the next address};
\end{tikzpicture}
\end{center}
```

A return-oriented chain: overwritten return addresses lead from one gadget in existing code to the next

:::

::: {#rmk-buffer-overflow-1 name="The real fix"}

The defences raise the cost of an attack; the cause is the unchecked copy. Use length-limited functions (`fgets(buf, sizeof buf, stdin)` instead of `gets`, `strncpy`/`snprintf` instead of `strcpy`/`sprintf`, `%20s` instead of `%s` in `scanf`), and compute buffer sizes including the terminating zero (@exm-c-memory-bugs).

:::
