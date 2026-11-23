---
title: "Loops and Switch Statements in Machine Code"
sources: [cmu15213-6]
requires: [cs/machine-level/condition-codes-and-jumps]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 6 "Machine-Level Programming II: Control", in our own wording. -->

Machine code has no loop or `switch` instructions. Compilers build them from conditional jumps, following a few fixed patterns. Recognising the patterns is how one reads compiled code.

::: {#def-do-while-translation .definition name="Translation of `do`–`while`"}

```text
do Body while (Test);          loop:
                                   Body
                                   if (Test) goto loop;
```

The body runs once before the first test; one conditional jump backwards closes the loop.

:::

::: {#def-while-translation .definition name="Two translations of `while`"}

*Jump to middle* (used with `-Og`): jump straight to the test at the bottom.

```text
    goto test;
loop:
    Body
test:
    if (Test) goto loop;
```

*Guarded do* (used with `-O1`): test once in front, then run a `do`–`while`.

```text
    if (!Test) goto done;
loop:
    Body
    if (Test) goto loop;
done:
```

The guarded form lets the compiler optimise the first test when it can tell that it holds.

:::

::: {#def-for-translation .definition name="Translation of `for`"}

`for (Init; Test; Update) Body` means `Init; while (Test) { Body; Update; }`, and is then translated as a `while` loop.

:::

::: {#exm-popcount-loop .example name="Counting the 1 bits"}

```c
long pcount(unsigned long x) {
    long result = 0;
    while (x) {
        result += x & 0x1;
        x >>= 1;
    }
    return result;
}
```

With `-Og` the guarded form is used here because the loop is simple:

```text
pcount:
    movl    $0, %eax          result = 0 (movl clears the upper half)
    testq   %rdi, %rdi
    je      .L4               if (x == 0) goto done
.L3:
    movq    %rdi, %rdx
    andl    $1, %edx          t = x & 1
    addq    %rdx, %rax        result += t
    shrq    %rdi              x >>= 1 (logical: x is unsigned)
    jne     .L3               the shift sets ZF: loop while x != 0
.L4:
    ret
```

The test `x != 0` is not a separate instruction: `shrq` already sets `ZF`.

:::

::: {#fig-loops-and-switch-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (i) at (0,0) {\texttt{result = 0}};
\node[hl box] (g) at (0,-1.2) {\texttt{x == 0} ?};
\node[box] (b) at (0,-2.6) {\texttt{result += x \& 1}\\\texttt{x >>= 1}};
\node[hl box] (t) at (0,-4.0) {\texttt{x != 0} ?};
\node[box] (d) at (3.6,-4.0) {\texttt{ret}};
\draw[->] (i) -- (g); \draw[->] (g) -- (b) node[midway, left, tick] {no};
\draw[->] (b) -- (t);
\draw[->, draw=accent] (t.west) -- ++(-1.2,0) |- (b.west) node[pos=0.25, left, tick] {yes};
\draw[->] (t) -- (d) node[midway, below, tick] {no};
\draw[->] (g.east) -| (d.north) node[pos=0.25, above, tick] {yes};
\end{tikzpicture}
\end{center}
```

`pcount` as a guarded `do`–`while`: one test in front, the loop test at the bottom jumps back

:::

::: {#def-jump-table .definition name="Jump table"}

A `switch` whose case labels are dense integers is compiled to a *jump table*: an array of code addresses indexed by the switch value. The code checks the value against the range once (an unsigned comparison catches negative values too, @def-signed-unsigned-casts) and then jumps indirectly with `jmp *.L4(,%rdi,8)`, which loads the 8-byte address at `.L4` $+8x$ and jumps to it.

:::

::: {#exm-switch-table .example name="A switch with fall-through and missing cases"}

```c
long switch_eg(long x, long y, long z) {
    long w = 1;
    switch (x) {
    case 1:  w = y * z; break;
    case 2:  w = y / z;          /* fall through */
    case 3:  w += z; break;
    case 5:
    case 6:  w -= z; break;
    default: w = 2;
    }
    return w;
}
```

```text
switch_eg:
    movq    %rdx, %rcx
    cmpq    $6, %rdi           x > 6 or x < 0 (unsigned compare)?
    ja      .L8                use default
    jmp     *.L4(,%rdi,8)      goto *JTab[x]
```

The table `.L4` has seven entries for $x=0,\dots,6$. Entries $0$ and $4$ point to the default code, entries $5$ and $6$ to the same code, and the code for case $2$ ends without a jump so that it runs into case $3$.

:::

::: {#fig-loops-and-switch-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, lbl bold] at (0.9,0.6) {jump table \texttt{.L4}};
\foreach \x/\t [count=\i from 0] in {0/.L8,1/.L3,2/.L5,3/.L9,4/.L8,5/.L7,6/.L7} {
  \draw[cell frame] (0,-\i*0.5) rectangle (1.8,-\i*0.5+0.45); \node[lab] at (0.9,-\i*0.5+0.225) {\texttt{\t}};
  \node[tick, anchor=east] at (-0.1,-\i*0.5+0.225) {$x=\x$};
}
\node[box] (c1) at (5,0.2) {\texttt{.L3}: \texttt{w = y*z}; break};
\node[box] (c2) at (5,-0.8) {\texttt{.L5}: \texttt{w = y/z}};
\node[box] (c3) at (5,-1.8) {\texttt{.L9}: \texttt{w += z}; break};
\node[box] (c5) at (5,-2.8) {\texttt{.L7}: \texttt{w -= z}; break};
\node[hl box] (cd) at (5,-3.8) {\texttt{.L8}: \texttt{w = 2} (default)};
\draw[->] (1.8,-0.275) to[out=0,in=180] (c1.west);
\draw[->] (1.8,-0.775) -- (c2.west);
\draw[->] (1.8,-1.275) -- (c3.west);
\draw[->] (1.8,-2.275) -- (c5.west);
\draw[->] (1.8,-2.775) -- (c5.west);
\draw[->, draw=accent] (1.8,0.225) to[out=0,in=180] (cd.west);
\draw[->, draw=accent] (1.8,-1.775) to[out=0,in=180] (cd.west);
\draw[->, dashed] (c2) -- (c3) node[midway, right, tick] {fall through};
\end{tikzpicture}
\end{center}
```

The jump table of `switch_eg`: missing cases $0$ and $4$ point to the default code, cases $5$ and $6$ share code, and case $2$ falls through into case $3$

:::

::: {#rmk-loops-and-switch-1 name="Sparse switches"}

When the case values are few and far apart (say $1$, $1000$, $10^6$), a table would be huge and mostly empty. The compiler then emits a sequence of comparisons, often arranged as a binary search over the case values, so the cost is logarithmic in the number of cases instead of constant.

:::
