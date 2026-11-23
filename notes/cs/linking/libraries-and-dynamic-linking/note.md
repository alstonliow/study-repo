---
title: "Static Libraries, Shared Libraries and Interpositioning"
sources: [cmu15213-13]
requires: [cs/linking/symbol-resolution-and-relocation]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 13 "Linking", libraries and interpositioning, in our own wording; the resolution algorithm is stated as a definition with its consequences. -->

::: {#def-static-library .definition name="Static library"}

A *static library* (an *archive*, `.a`) is a collection of relocatable object files with an index, built with `ar rs libvector.a addvec.o multvec.o`. When a program is linked against it, the linker copies into the executable only the member files that define symbols the program actually references.

:::

::: {#def-archive-resolution .definition name="How the linker scans archives"}

The linker processes the files and archives on the command line from left to right, keeping a set $U$ of unresolved references and a set $D$ of defined symbols.

- A relocatable file is always added: its definitions go into $D$ and its unresolved references into $U$.
- For an archive, it repeatedly adds any member that defines a symbol in $U$ (updating $U$ and $D$), until no member does; the other members are discarded.
- If $U$ is not empty at the end, the link fails with "undefined reference".

:::

::: {#prp-library-order .proposition name="Libraries go at the end of the command line"}

If object file `main.o` references a symbol defined only in archive `libx.a`, then `gcc main.o libx.a` succeeds and `gcc libx.a main.o` fails.

:::

::: {.proof}
1. In the second order, $U$ is empty when the archive is scanned, so no member is added.

2. `main.o` then puts the symbol into $U$, and no file after it can resolve it, so $U$ is nonempty at the end.

3. In the first order the symbol is already in $U$ when the archive is scanned, and the member that defines it is added.
:::

::: {#fig-libraries-and-dynamic-linking-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (m) at (0,1.2) {\texttt{main.o}};
\node[box] (lv) at (0,0) {\texttt{libvector.a}\\\texttt{addvec.o}, \texttt{multvec.o}};
\node[box] (lc) at (0,-1.4) {\texttt{libc.a}\\\texttt{printf.o}, \dots};
\node[hl box] (ld) at (3.6,0) {linker};
\node[box] (p) at (7.0,0) {executable with\\\texttt{main.o}, \texttt{addvec.o},\\\texttt{printf.o} only};
\draw[->] (m) -- (ld); \draw[->] (lv) -- (ld) node[midway, above, tick] {\texttt{addvec.o}}; \draw[->] (lc) -- (ld) node[midway, below right, tick] {\texttt{printf.o}};
\draw[->] (ld) -- (p);
\end{tikzpicture}
\end{center}
```

Linking with static libraries: only the members that resolve a reference are copied into the executable

:::

::: {#def-shared-library .definition name="Shared library and dynamic linking"}

A *shared library* (`.so`, built with `gcc -shared -fpic`) is an object module that is not copied into the executable. The static linker records only that the program needs it. When the program is loaded, the *dynamic linker* (`ld-linux.so`) maps the library into the process's address space and resolves the references to it (*load-time linking*). A program can also load a library while running, with `dlopen` and `dlsym` (*run-time linking*). One copy of the library's code in memory is shared by all processes that use it (@def-shared-object).

:::

::: {#def-position-independent-code .definition name="Position-independent code"}

Shared library code must run at whatever address it is mapped to, so it is compiled as *position-independent code* (PIC): references to its own code and data are PC-relative, and references to symbols in other modules go through a table of addresses in the library's data segment, the *global offset table* (GOT), which the dynamic linker fills in. Calls to functions in other modules go through small stubs in a *procedure linkage table* (PLT), resolved on the first call.

:::

::: {#fig-libraries-and-dynamic-linking-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (m) at (0,1.2) {\texttt{main.o}};
\node[box] (so) at (0,-0.2) {\texttt{libc.so}};
\node[hl box] (ld) at (2.8,1.2) {static linker \texttt{ld}};
\node[box] (p) at (5.8,1.2) {\texttt{prog}\\(partially linked)};
\node[hl box] (dl) at (5.8,-0.6) {dynamic linker\\\texttt{ld-linux.so}};
\node[box] (mem) at (9.2,-0.6) {fully linked\\program in memory};
\draw[->] (m) -- (ld); \draw[->] (so) -- (ld) node[midway, below right, tick] {names only};
\draw[->] (ld) -- (p); \draw[->] (p) -- (dl) node[midway, right, tick] {\texttt{execve}};
\draw[->] (so) to[out=-20,in=200] node[midway, below, tick] {code and data} (dl);
\draw[->] (dl) -- (mem);
\end{tikzpicture}
\end{center}
```

Dynamic linking: the executable only names the shared library; the dynamic linker maps the library and resolves references when the program is loaded

:::

::: {#def-library-interpositioning .definition name="Library interpositioning"}

*Interpositioning* intercepts calls to a library function and runs a wrapper of the programmer's choice instead, which may call the real function. It can be done at

- *compile time*: a macro in a local header renames `malloc(n)` to `mymalloc(n)`;
- *link time*: `ld --wrap,malloc` resolves `malloc` to `__wrap_malloc` and `__real_malloc` to the real `malloc`;
- *load or run time*: setting the environment variable `LD_PRELOAD=./mymalloc.so` makes the dynamic linker search that library first; the wrapper finds the real function with `dlsym(RTLD_NEXT, "malloc")`.

:::

::: {#exm-interposition-uses .example name="Uses of interpositioning"}

Counting and timing calls to `malloc` and `free` to find memory leaks or hot spots; tracing which files a program opens; checking library calls for misuse; and, in security, sandboxing a program by refusing certain calls. The run-time form needs no access to the program's source or object files.

:::

::: {#rmk-libraries-and-dynamic-linking-1 name="Static versus shared"}

Static libraries make self-contained executables but duplicate library code in every program on disk and in memory, and a bug fix in the library requires relinking every program. Shared libraries are stored once, shared in memory, and updated in one place, at the cost of a small run-time indirection and of depending on the right version being installed.

:::
