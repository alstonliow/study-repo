---
title: "Object Files and Symbols"
sources: [cmu15213-13]
requires: [cs/machine-level/buffer-overflow]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 13 "Linking", first part, in our own wording. -->

Programs are written as many source files and use library code written by others. *Linking* combines separately compiled pieces into one program. It lets each file be compiled on its own (modularity) and only changed files be recompiled (efficiency).

::: {#def-object-file-kinds .definition name="Kinds of object files"}

- A *relocatable object file* (`.o`) holds code and data compiled from one source file, in a form that can be combined with other relocatable files; addresses in it start at $0$ and references to other files are left open.
- An *executable object file* (`a.out`) holds code and data in a form that can be copied into memory and run.
- A *shared object file* (`.so`) is a relocatable file that can be loaded and linked into a running program, at load time or later (@def-shared-library).

On Linux all three use the *Executable and Linkable Format* (ELF).

:::

::: {#def-elf-sections .definition name="ELF sections"}

A relocatable ELF file is a header followed by *sections*:

| section | contents |
|---|---|
| `.text` | machine code |
| `.rodata` | read-only data: string constants, jump tables (@def-jump-table) |
| `.data` | initialized global and `static` variables |
| `.bss` | uninitialized (or zero) global and `static` variables: only their sizes, they take no space in the file |
| `.symtab` | the symbol table: names and locations of functions and global variables |
| `.rel.text`, `.rel.data` | relocation entries for references that must be fixed (@def-relocation) |
| `.debug` | information for a debugger (with `gcc -g`) |

:::

::: {#fig-object-files-and-symbols-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.55cm]
\foreach \s/\d [count=\i from 0] in {ELF header/{word size, byte order, file type, machine},.text/code,.rodata/read-only data,.data/initialized globals,.bss/{uninitialized globals (size only)},.symtab/symbol table,.rel.text/{relocations for .text},.rel.data/{relocations for .data},.debug/debugging information,section header table/{offset and size of each section}} {
  \draw[cell frame] (0,-\i) rectangle (3.2,-\i-0.9); \node[tick] at (1.6,-\i-0.45) {\texttt{\s}};
  \node[tick, anchor=west] at (3.4,-\i-0.45) {\d};
}
\draw[hl cell] (0,-1) rectangle (3.2,-1.9); \node[tick] at (1.6,-1.45) {\texttt{.text}};
\draw[hl cell] (0,-3) rectangle (3.2,-3.9); \node[tick] at (1.6,-3.45) {\texttt{.data}};
\end{tikzpicture}
\end{center}
```

Layout of a relocatable ELF object file. The code and the initialized data (shaded) are copied into memory when the program runs

:::

::: {#def-linker-symbols .definition name="Global, external and local symbols"}

Each relocatable module $m$ has a symbol table listing:

- *global symbols* defined by $m$ that other modules can reference: non-`static` functions and global variables;
- *external symbols*: global symbols that $m$ references but other modules define;
- *local symbols* defined and used only by $m$: functions and global variables declared `static`.

Local variables of a function (non-`static`) are not symbols at all: they live in registers or on the stack and the linker never sees them.

:::

::: {#exm-symbol-classification .example name="Classifying the names in two files"}

```c
/* main.c */                         /* sum.c */
int sum(int *a, int n);              int sum(int *a, int n) {
int array[2] = {1, 2};                   int s = 0;
                                         for (int i = 0; i < n; i++)
int main(void) {                             s += a[i];
    int val = sum(array, 2);             return s;
    return val;                      }
}
```

In `main.o`: `main` and `array` are global symbols defined here (`array` in `.data`), `sum` is an external symbol, and `val` is not a symbol. In `sum.o`: `sum` is a global symbol defined in `.text`; `s` and `i` are not symbols.

:::

::: {#exm-static-locals .example name="`static` variables become local symbols"}

```c
int f(void) { static int x = 0; return x++; }
int g(void) { static int x = 1; return x; }
```

Each `static int x` is allocated once, in `.data`, and keeps its value between calls. The compiler gives the two variables distinct local symbols, such as `x.1` and `x.2`, so they do not clash with each other or with an `x` in another module.

:::

::: {#fig-object-files-and-symbols-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0) rectangle (3.4,2.2); \node[lab] at (1.7,2.45) {\texttt{main.o}};
\node[box] (m) at (1.7,1.6) {\texttt{main} (global)};
\node[box] (a) at (1.7,0.6) {\texttt{array} (global)};
\draw[regionC] (5.4,0) rectangle (8.8,2.2); \node[lab] at (7.1,2.45) {\texttt{sum.o}};
\node[box] (s) at (7.1,1.1) {\texttt{sum} (global)};
\draw[->, draw=accent, emph] (m.east) to[out=0,in=180] node[edge label, pos=0.45] {external reference} (s.west);
\end{tikzpicture}
\end{center}
```

The symbols of the two modules. The reference from `main` to `sum` is external in `main.o`; the linker connects it to the definition in `sum.o`

:::

::: {#rmk-object-files-and-symbols-1 name="Tools"}

`readelf -a file.o` prints the header, sections and symbol table of an ELF file; `nm file.o` lists its symbols with their section (`T` for `.text`, `D` for `.data`, `B` for `.bss`, `U` for undefined, that is, external); `objdump -dr file.o` disassembles code and shows its relocation entries.

:::
