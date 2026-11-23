---
title: "Memory, Words and Byte Ordering"
sources: [cmu15213-3, cmu15213r-3, cmu15213r-13]
requires: [cs/data-representation/integer-encodings]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 3 "Bits, Bytes and Integers, part 2" and Recitations 3 and 13 (byte ordering), in our own wording. -->

::: {#def-byte-addressable-memory .definition name="Byte-addressable memory, address, word size"}

A program sees memory as one large array of bytes, the *virtual address space*. The index of a byte is its *address*. The *word size* $w$ of a machine is the width of an address (a pointer); addresses range over $0,\dots,2^w-1$. A multi-byte object occupies consecutive bytes and is identified by the address of its first (lowest) byte.

:::

On x86-64 pointers are 64 bits wide, although current processors use only the low 48 bits of an address. The sizes of C types follow from the word size:

::: {#exm-c-type-sizes .example name="Sizes of C types in bytes"}

| type | 32-bit machine | x86-64 |
|---|---|---|
| `char` | 1 | 1 |
| `short` | 2 | 2 |
| `int` | 4 | 4 |
| `long` | 4 | 8 |
| `float` | 4 | 4 |
| `double` | 8 | 8 |
| pointer (`char *`, …) | 4 | 8 |

Only `long` and pointers change; code that stores a pointer in an `int` breaks on x86-64.

:::

::: {#def-endianness .definition name="Byte ordering (endianness)"}

Store a $w$-bit value with bytes $b_{k-1},\dots,b_1,b_0$ ($b_0$ least significant, $k=w/8$) at address $a$.

- *Little endian*: $b_0$ goes to $a$, $b_1$ to $a+1$, …: least significant byte first. x86-64 and most ARM systems.
- *Big endian*: $b_{k-1}$ goes to $a$: most significant byte first. Network protocols ("network byte order") and some older processors.

:::

::: {#fig-byte-ordering-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \a [count=\i from 0] in {0x100,0x101,0x102,0x103} { \node[tick] at (2.2+\i*1.1,1.95) {\texttt{\a}}; }
\node[lab, anchor=east] at (1.5,1.3) {big endian};
\foreach \b [count=\i from 0] in {01,23,45,67} { \draw[cell frame] (1.65+\i*1.1,1.0) rectangle (2.75+\i*1.1,1.6); \node[lab] at (2.2+\i*1.1,1.3) {\texttt{\b}}; }
\node[lab, anchor=east] at (1.5,0.3) {little endian};
\foreach \b [count=\i from 0] in {67,45,23,01} { \draw[cell frame] (1.65+\i*1.1,0) rectangle (2.75+\i*1.1,0.6); \node[lab] at (2.2+\i*1.1,0.3) {\texttt{\b}}; }
\draw[hl cell] (1.65,0) rectangle (2.75,0.6); \node[lab] at (2.2,0.3) {\texttt{67}};
\draw[hl cell] (4.95,1.0) rectangle (6.05,1.6); \node[lab] at (5.5,1.3) {\texttt{67}};
\node[lab, anchor=west] at (6.3,0.8) {value \texttt{0x01234567}};
\end{tikzpicture}
\end{center}
```

The 4-byte value `0x01234567` at address `0x100`. The least significant byte `0x67` (shaded) comes first in little-endian order and last in big-endian order

:::

::: {#exm-reading-bytes .example name="Looking at the bytes of an object"}

Casting a pointer to `unsigned char *` lets a program read an object byte by byte:

```c
void show_bytes(const void *p, size_t n) {
    const unsigned char *b = p;
    for (size_t i = 0; i < n; i++)
        printf(" %.2x", b[i]);
    printf("\n");
}
```

On x86-64, `int x = 15213;` (`0x00003B6D`) prints ` 6d 3b 00 00`, and `int y = -15213;` (`0xFFFFC493`) prints ` 93 c4 ff ff`. A big-endian machine would print the four bytes in the reverse order.

:::

::: {#exm-disassembly-endianness .example name="Endianness in machine code"}

A disassembler listing shows instruction bytes in memory order. An instruction that adds the constant `0x12ab` might appear as the bytes `81 c3 ab 12 00 00`: the 4-byte constant is stored least significant byte first, so it reads backwards. This is why little endian matters most when one reads raw memory or machine code by hand.

:::

::: {#rmk-byte-ordering-1 name="What endianness does not affect"}

Byte order applies within one multi-byte scalar. A C string is an array of 1-byte characters ending in the byte `0x00`; its bytes appear in the same order on every machine. Arrays are laid out element by element in increasing addresses everywhere; only the bytes inside each element are ordered by the machine's convention.

:::

::: {#fig-byte-ordering-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \c [count=\i from 0] in {31,35,32,31,33,00} { \draw[cell frame] (\i*1.0,0) rectangle (\i*1.0+1.0,0.6); \node[lab] at (\i*1.0+0.5,0.3) {\texttt{\c}}; }
\foreach \c [count=\i from 0] in {1,5,2,1,3,\textbackslash 0} { \node[tick] at (\i*1.0+0.5,0.85) {\texttt{'\c'}}; }
\foreach \i in {0,...,5} { \node[tick] at (\i*1.0+0.5,-0.25) {$a+\i$}; }
\node[lab, anchor=west] at (6.2,0.3) {same on every machine};
\end{tikzpicture}
\end{center}
```

The string `"15213"` is six bytes: the ASCII codes of the digits and a terminating zero byte, in increasing addresses regardless of byte order

:::

::: {#rmk-byte-ordering-2 name="Network byte order"}

Integers sent over a network (port numbers, IP addresses) are big endian by convention. A little-endian host converts with `htons`/`htonl` before sending and `ntohs`/`ntohl` after receiving (@def-socket-address).

:::
