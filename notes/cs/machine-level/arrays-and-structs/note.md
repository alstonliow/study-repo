---
title: "Arrays, Structures, Alignment and Unions"
sources: [cmu15213-8, cmu15213-9]
requires: [cs/machine-level/data-movement-and-arithmetic, cs/data-representation/c-pointers-and-memory]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 8 "Machine-Level Programming IV: Data" and the union part of Lecture 9, in our own wording; proofs written out in steps. -->

::: {#def-array-layout .definition name="Array layout"}

`T A[N]` occupies $N\cdot L$ contiguous bytes, $L=$ `sizeof(T)`, starting at address $x_A$; element $i$ is at
$$x_A+L\cdot i .$$
A *nested* array `T A[R][C]` is an array of $R$ rows, each an array of $C$ elements, stored *row-major*: element $A[i][j]$ is at
$$x_A+L\,(C\cdot i+j).$$

:::

::: {#fig-arrays-and-structs-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,3} { \foreach \j in {0,...,4} {
  \pgfmathtruncatemacro{\k}{5*\i+\j}
  \draw[cell frame] (\k*0.62,0) rectangle (\k*0.62+0.62,0.55);
  \node[tick] at (\k*0.62+0.31,0.275) {$\i,\j$};
}}
\foreach \i in {0,...,3} { \draw[draw=primary] (\i*3.1+0.02,-0.05) rectangle (\i*3.1+3.08,0.6); \node[tick] at (\i*3.1+1.55,0.85) {row \texttt{A[\i]}}; }
\draw[hl cell] (2*3.1+3*0.62,0) rectangle (2*3.1+4*0.62,0.55); \node[tick] at (2*3.1+3.5*0.62,0.275) {$2,3$};
\node[tick] at (0,-0.3) {$x_A$};
\node[tick] at (2*3.1+3.5*0.62,-0.3) {$x_A+4(5\cdot2+3)$};
\end{tikzpicture}
\end{center}
```

`int A[4][5]` in row-major order: the rows follow each other, and `A[2][3]` is element $5\cdot2+3=13$, at byte offset $52$

:::

::: {#exm-array-access-code .example name="Indexing in machine code"}

For `int get_digit(int *z, long i) { return z[i]; }` the compiler emits `movl (%rdi,%rsi,4), %eax`: base `z`, index `i`, scale $4$ (@def-operand-forms). For `int A[16][5]`, the address of `A[i][j]` is computed as `leaq (%rdi,%rdi,4), %rax` ($5i$), then `addq %rsi, %rax` ($5i+j$), then a load with scale $4$.

:::

::: {#def-multi-level-array .definition name="Multi-level array"}

An array of pointers, each pointing to its own row (`int *rows[R]`), is a *multi-level array*. Accessing element $(i,j)$ takes two memory reads: first the pointer `rows[i]`, then the element at that pointer plus $L\cdot j$. The rows need not be contiguous or of equal length.

:::

::: {#fig-arrays-and-structs-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab, anchor=east] at (-0.1,0.6) {\texttt{rows}};
\foreach \i in {0,1,2} { \draw[cell frame] (0,1.1-\i*0.55) rectangle (1,1.65-\i*0.55); \node[tick] at (0.5,1.375-\i*0.55) {\texttt{\&r\i[0]}}; }
\foreach \i/\x in {0/3.0,1/2.2,2/3.6} {
  \foreach \j in {0,...,4} { \draw[cell frame] (\x+\j*0.5,1.1-\i*0.9+0.6) rectangle (\x+\j*0.5+0.5,1.1-\i*0.9+1.1); }
  \draw[map] (1,1.375-\i*0.55) to[out=0,in=180] (\x,1.1-\i*0.9+0.85);
}
\draw[hl cell] (2.2+2*0.5,0.8) rectangle (2.2+3*0.5,1.3);
\node[lab, anchor=west] at (6.4,0.4) {rows anywhere in memory};
\end{tikzpicture}
\end{center}
```

A multi-level array: an array of row pointers. `rows[1][2]` (shaded) needs one read for the pointer and one for the element

:::

::: {#def-struct-layout .definition name="Structure layout and alignment"}

A structure's fields are stored in declaration order. A primitive object of $K$ bytes is *aligned* if its address is a multiple of $K$; x86-64 compilers align every field, inserting *padding* bytes before a field when needed, and pad the end so that the structure's size is a multiple of its largest field's alignment $K_{\max}$ (then every element of an array of structures is aligned too). The structure's own address is a multiple of $K_{\max}$.

:::

::: {#exm-struct-padding .example name="Padding in a structure"}

```c
struct S1 { char c; int i[2]; double v; };
```

`c` is at offset $0$; `i` needs a multiple of $4$, so $3$ padding bytes follow `c` and `i` occupies offsets $4$–$11$; `v` needs a multiple of $8$, so $4$ more padding bytes and `v` at $16$–$23$. Total size $24$, of which $7$ bytes are padding.

Reordering the fields from largest to smallest, `struct S2 { double v; int i[2]; char c; };`, places them at $0$, $8$ and $16$, and the size is again rounded up to $24$. For `struct S3 { char c; int i; char d; }` (size $12$) versus `struct S4 { int i; char c; char d; }` (size $8$), the order saves a third.

:::

::: {#fig-arrays-and-structs-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \k in {0,...,23} { \draw[cell frame] (\k*0.42,0) rectangle (\k*0.42+0.42,0.5); }
\draw[regionA] (0,0) rectangle (0.42,0.5); \node[tick] at (0.21,0.25) {\texttt{c}};
\path[tintD] (0.42,0) rectangle (4*0.42,0.5);
\draw[regionA] (4*0.42,0) rectangle (8*0.42,0.5); \node[tick] at (6*0.42,0.25) {\texttt{i[0]}};
\draw[regionA] (8*0.42,0) rectangle (12*0.42,0.5); \node[tick] at (10*0.42,0.25) {\texttt{i[1]}};
\path[tintD] (12*0.42,0) rectangle (16*0.42,0.5);
\draw[regionB] (16*0.42,0) rectangle (24*0.42,0.5); \node[tick] at (20*0.42,0.25) {\texttt{v}};
\foreach \o in {0,4,8,16,24} { \node[tick] at (\o*0.42,-0.25) {\o}; }
\node[tick] at (2.5*0.42,0.75) {padding}; \node[tick] at (14*0.42,0.75) {padding};
\end{tikzpicture}
\end{center}
```

`struct S1`: three padding bytes align `i` to a multiple of 4, four more align `v` to a multiple of 8

:::

::: {#prp-struct-sorted-fields .proposition name="Sorting fields by alignment removes inner padding"}

If the fields of a structure are declared in order of non-increasing alignment requirement, and each field's size is a multiple of its alignment, no padding is inserted between fields.

:::

::: {.proof}
1. Alignments of primitive types are powers of two, so in a non-increasing sequence each alignment divides all earlier ones.

2. By induction on the fields: the first field is at offset $0$. Suppose field $k$ starts at an offset divisible by its alignment $K_k$. Its size is a multiple of $K_k$, so the next offset is a multiple of $K_k$, hence of $K_{k+1}$, which divides $K_k$. So field $k+1$ is aligned with no padding.

3. Padding may still be needed at the end, to round the total size up to a multiple of $K_{\max}$.
:::

::: {#def-union .definition name="Union"}

A `union` lets its fields share the same storage: all fields start at offset $0$, and the size is that of the largest field (rounded up for alignment). Writing one field and reading another reinterprets the bytes, which is how C code inspects the bit pattern of a `float` or the bytes of an integer (@def-endianness).

:::

::: {#exm-union-bits .example name="Reading a float's bits through a union"}

```c
unsigned float2bits(float f) {
    union { float f; unsigned u; } t;
    t.f = f;
    return t.u;
}
```

`float2bits(15213.0f)` is `0x466DB400` (@exm-encode-15213), while the cast `(unsigned) 15213.0f` converts the value and gives $15213$. A union of `char c[8]` and `long l` shows the byte order directly: on x86-64, `c[0]` is the least significant byte of `l`.

:::

::: {#rmk-arrays-and-structs-1 name="Floating-point registers"}

Floating-point arguments and return values use separate registers, `%xmm0`–`%xmm15` (arguments in `%xmm0`–`%xmm7`, result in `%xmm0`), with instructions such as `addsd` (add scalar double) and `vcvtsi2sd` (convert integer to double). All of them are caller saved. The same registers hold several values at once for vector (SIMD) operations (@sec-cs-machine-level-instruction-level-parallelism).

:::
