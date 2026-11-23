---
title: "Machine-Independent Code Optimization"
sources: [cmu15213-10]
requires: [cs/machine-level/procedures-and-the-stack, cs/machine-level/loops-and-switch]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 10 "Program Optimization", first half, in our own wording. -->

Asymptotic complexity is fixed by the choice of algorithm, but constant factors of $10\times$ between two correct programs are common. Some of the improvement comes from the compiler; much of it needs the programmer, because the compiler must stay correct in cases the programmer knows cannot occur.

::: {#def-optimization-blockers .definition name="Optimization blocker"}

A compiler may transform a program only if the result behaves identically for *every* input and every possible state of memory. An *optimization blocker* is a feature of the code that makes a profitable transformation unsafe in some rare case, so the compiler does not apply it. The two main blockers are procedure calls (the callee might have side effects) and *memory aliasing* (two pointers might refer to the same location).

:::

::: {#def-code-motion .definition name="Code motion, strength reduction, common subexpressions"}

- *Code motion*: move a computation whose value does not change between iterations out of a loop.
- *Strength reduction*: replace an expensive operation by a cheaper one, such as a multiplication by $2^k$ by a shift (@thm-shift-multiply-divide), or a product `n*i` recomputed each iteration by a running sum incremented by `n`.
- *Common subexpression elimination*: compute a value used several times once. For neighbours of `a[i*n + j]`, the terms `(i-1)*n`, `i*n`, `(i+1)*n` share the product `i*n`, so one multiplication can replace three.

:::

::: {#exm-lower-quadratic .example name="A quadratic `strlen` loop"}

```c
void lower(char *s) {
    for (size_t i = 0; i < strlen(s); i++)
        if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] -= 'A' - 'a';
}
```

`strlen` walks the whole string, and it is called once per iteration, so the loop does about $n^2/2$ character reads for a string of length $n$: on a string of $500\,000$ characters this takes minutes instead of milliseconds. The compiler cannot hoist the call out of the loop: it does not know that `strlen` has no side effects, and the loop body changes `s`, which might change its length (it does not, but proving that needs knowledge of `strlen`). Moving `size_t len = strlen(s);` before the loop by hand makes the function linear.

:::

::: {#fig-code-optimization-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm, y=0.55cm]
\draw[->] (0,0) -- (5.4,0) node[lab, right] {length $n$ ($\times10^5$)};
\draw[->] (0,0) -- (0,5.4) node[lab, above] {time};
\foreach \v in {1,...,5} { \draw (\v,-0.1) -- (\v,0.1); \node[tick] at (\v,-0.5) {\v}; }
\draw[emph, draw=accent, domain=0:5, samples=40] plot (\x, {0.2*\x*\x});
\draw[emph, draw=primary] (0,0) -- (5,0.25);
\node[tick, anchor=west, text=accent] at (4.2,4.4) {\texttt{strlen} in the loop test: $\Theta(n^2)$};
\node[tick, anchor=west, text=primary] at (3.3,0.8) {\texttt{strlen} hoisted: $\Theta(n)$};
\end{tikzpicture}
\end{center}
```

Running time of `lower` (shape only): calling `strlen` in every loop test makes the function quadratic

:::

::: {#exm-aliasing .example name="Memory aliasing"}

```c
/* Sum the rows of the n x n matrix a into b */
void sum_rows(double *a, double *b, long n) {
    for (long i = 0; i < n; i++) {
        b[i] = 0;
        for (long j = 0; j < n; j++)
            b[i] += a[i*n + j];
    }
}
```

The inner loop loads `b[i]`, adds, and stores it back on every iteration. The compiler must assume that `b` may overlap `a`: if `b` $=$ `a + 3`, say, then storing to `b[i]` changes an element of `a` that a later iteration reads. Accumulating in a local variable, `double val = 0; ... val += a[i*n + j]; b[i] = val;`, removes the memory traffic, and is correct only because the programmer knows the arrays do not overlap.

:::

::: {#fig-code-optimization-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \i in {0,...,8} { \draw[cell frame] (\i*0.7,0) rectangle (\i*0.7+0.7,0.55); \node[tick] at (\i*0.7+0.35,-0.25) {\i}; }
\draw[draw=primary] (0,-0.05) rectangle (6.3,0.6); \node[lab] at (3.15,0.9) {\texttt{a} ($3\times3$)};
\draw[draw=accent] (2.1,-0.55) rectangle (4.2,0.65); \node[lab] at (3.15,-0.85) {\texttt{b} $=$ \texttt{a + 3}};
\draw[hl cell] (2.1,0) rectangle (2.8,0.55);
\end{tikzpicture}
\end{center}
```

If `b` points into `a`, writing `b[0]` changes `a[3]`, which the next row's sum reads; the compiler must keep every intermediate store

:::

::: {#def-combine-benchmark .definition name="Cycles per element (CPE)"}

For a loop that processes $n$ elements, the running time is close to $T(n)=\mathit{overhead}+\mathit{CPE}\cdot n$ clock cycles. The slope $\mathit{CPE}$, *cycles per element*, measures the loop's speed independently of the clock rate and of fixed setup costs.

:::

::: {#exm-combine-steps .example name="Combining the elements of a vector"}

The benchmark computes the sum or product of the elements of a vector stored behind an abstract interface:

```c
void combine1(vec_ptr v, data_t *dest) {
    *dest = IDENT;
    for (long i = 0; i < vec_length(v); i++) {
        data_t val;
        get_vec_element(v, i, &val);   /* bounds-checked access */
        *dest = *dest OP val;
    }
}
```

The machine-independent improvements, applied in order, are: (1) compute `vec_length(v)` once (code motion); (2) get a pointer to the element array once and index it directly, avoiding a bounds-checked call per element; (3) accumulate in a local variable instead of `*dest` (removing the aliasing blocker of @exm-aliasing). Together they cut the CPE several-fold, down to the limit set by the latency of `OP` itself (@thm-latency-bound).

:::

::: {#rmk-code-optimization-1 name="What to leave to the compiler"}

Compilers are good at register allocation, instruction selection, simple strength reduction and constant folding. The programmer should choose good algorithms and data structures, write code the compiler can optimise (local accumulators, no needless calls in inner loops), and measure: a profiler such as `gprof` shows where the time actually goes, and only the hot loops are worth this effort (@thm-amdahl-law).

:::
