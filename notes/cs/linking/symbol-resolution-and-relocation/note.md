---
title: "Symbol Resolution, Relocation and Loading"
sources: [cmu15213-13]
requires: [cs/linking/object-files-and-symbols]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 13 "Linking", static linking part, in our own wording; the relocation example is worked out in steps. -->

A static linker such as `ld` takes relocatable object files and produces an executable in two steps: *symbol resolution* matches each symbol reference with exactly one definition, and *relocation* merges the sections and fixes every reference to point at the final address.

::: {#def-strong-weak-symbols .definition name="Strong and weak symbols"}

A global symbol is *strong* if it is a function or an initialized global variable, and *weak* if it is an uninitialized global variable. The linker resolves multiply defined names by three rules:

1. Two strong symbols with the same name are an error.
2. If there is one strong symbol and any number of weak ones with that name, references resolve to the strong one.
3. If all the symbols with that name are weak, the linker picks one of them arbitrarily.

(Recent versions of gcc treat uninitialized globals as strong by default, `-fno-common`, which makes rule 3 an error too.)

:::

::: {#exm-weak-symbol-bugs .example name="Silent errors from weak symbols"}

| `p1.c` | `p2.c` | outcome |
|---|---|---|
| `int x; int p1() {}` | `int p1() {}` | link error: two strong `p1` |
| `int x; p1() {}` | `int x; p2() {}` | both refer to the same `x` |
| `int x; int y; p1() {}` | `double x; p2() {}` | writes to `x` in `p2` overwrite `y` (8 bytes into a 4-byte slot) |
| `int x = 7; int y = 5; p1() {}` | `double x; p2() {}` | same, with the strong `x` from `p1.c` |

The last two link without complaint and corrupt memory at run time. The rules of thumb: avoid global variables; use `static` for those private to a file; initialize globals so that they are strong; and declare an external global with `extern`, in a header shared by the defining file.

:::

::: {#def-relocation .definition name="Relocation"}

Relocation has two steps. First, the linker merges all sections of the same kind (all `.text` sections into one, and so on) and assigns run-time addresses to the merged sections and to every symbol defined in them. Second, for each *relocation entry* left by the assembler (offset of the reference in its section, the symbol, and the type), it patches the bytes at that offset. The two main types are an *absolute* reference, replaced by the symbol's address, and a *PC-relative* reference, replaced by the symbol's address minus the address of the next instruction.

:::

::: {#exm-pc-relative-call .example name="Relocating a call"}

In `main.o`, `call sum` is assembled as `e8 00 00 00 00` with a relocation entry "PC-relative to `sum`, $-4$" at offset `0xf` of `.text`. Suppose the linker places `main` at `0x4004d0` and `sum` at `0x4004e8`. The reference sits at address `0x4004d0 + 0xf = 0x4004df`, and the next instruction starts 4 bytes later, at `0x4004e3`. The patched value is
$$\texttt{0x4004e8}-\texttt{0x4004e3}=5,$$
so the call becomes `e8 05 00 00 00`: at run time the processor adds $5$ to the address of the next instruction and lands on `sum`.

:::

::: {#fig-symbol-resolution-and-relocation-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,1.4) rectangle (2.6,2.4); \node[tick] at (1.3,2.15) {\texttt{main.o}};
\draw[cell frame] (0.15,1.5) rectangle (1.25,1.95); \node[tick] at (0.7,1.72) {\texttt{.text}};
\draw[cell frame] (1.35,1.5) rectangle (2.45,1.95); \node[tick] at (1.9,1.72) {\texttt{.data}};
\draw[regionC] (0,0) rectangle (2.6,1.0); \node[tick] at (1.3,0.75) {\texttt{sum.o}};
\draw[cell frame] (0.15,0.1) rectangle (1.25,0.55); \node[tick] at (0.7,0.32) {\texttt{.text}};
\draw[regionB] (5,-0.2) rectangle (8,2.6); \node[tick] at (6.5,2.35) {executable};
\draw[cell frame] (5.2,1.0) rectangle (7.8,2.0); \node[tick] at (6.5,1.75) {\texttt{.text}};
\draw[hl cell] (5.3,1.05) rectangle (7.7,1.45); \node[tick] at (6.5,1.25) {\texttt{main} \quad \texttt{sum}};
\draw[cell frame] (5.2,0.0) rectangle (7.8,0.7); \node[tick] at (6.5,0.35) {\texttt{.data}: \texttt{array}};
\draw[map] (1.25,1.72) to[out=0,in=180] (5.3,1.25);
\draw[map] (1.25,0.32) to[out=0,in=180] (5.3,1.25);
\draw[map] (2.45,1.72) to[out=0,in=180] (5.2,0.35);
\end{tikzpicture}
\end{center}
```

Relocation merges sections of the same kind from all modules and gives every symbol its run-time address; then every reference is patched

:::

::: {#def-loading .definition name="Loading an executable"}

An executable ELF file has a *segment header table* that says which parts of the file to copy where. The *loader* (`execve`, @def-execve) creates the memory image of @def-x86-64-linux-layout: it maps the read-only code segment (`.init`, `.text`, `.rodata`) and the read/write data segment (`.data`, `.bss`, the latter filled with zeros), sets up the stack and heap, and jumps to the program's entry point `_start`, which calls `main`.

:::

::: {#fig-symbol-resolution-and-relocation-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.55cm]
\foreach \s [count=\i from 0] in {ELF header,segment header table,.init,.text,.rodata,.data,.bss,.symtab and others} { \draw[cell frame] (0,-\i) rectangle (3,-\i-0.9); \node[tick] at (1.5,-\i-0.45) {\texttt{\s}}; }
\draw[regionB] (6,-6.4) rectangle (9,-4.6); \node[tick] at (7.5,-5.5) {read/write segment};
\draw[regionA] (6,-4.4) rectangle (9,-2.6); \node[tick] at (7.5,-3.5) {read-only code segment};
\draw[map] (3,-2.5) to[out=0,in=180] (6,-3.0); \draw[map] (3,-4.4) to[out=0,in=180] (6,-4.0);
\draw[map] (3,-5.5) to[out=0,in=180] (6,-5.0); \draw[map] (3,-6.5) to[out=0,in=180] (6,-6.0);
\node[tick] at (7.5,-2.2) {memory (from \texttt{0x400000})};
\node[tick] at (1.5,0.5) {executable file};
\end{tikzpicture}
\end{center}
```

Loading: two contiguous parts of the file become the code and data segments of the process

:::
