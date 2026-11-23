---
title: "Instruction-Level Parallelism and Loop Unrolling"
sources: [cmu15213-10]
requires: [cs/machine-level/code-optimization]
status: draft
---

<!-- Added 2026-11-23 from CMU 15-213 (Fall 2015), Lecture 10 "Program Optimization", second half, in our own wording; proofs written out in steps. -->

After the blockers of @sec-cs-machine-level-code-optimization are removed, the remaining limit is the processor itself. A modern core runs many instructions at the same time; code is fast when it gives the core enough independent work.

::: {#def-superscalar-pipelined .definition name="Superscalar, out-of-order, pipelined execution"}

A *superscalar* processor can issue several instructions per clock cycle. It reads instructions ahead, finds those whose operands are ready, and executes them *out of order* in several *functional units* (integer ALUs, a multiplier, floating-point adders, load and store units), while making the results appear in program order. Each functional unit is *pipelined*: an operation passes through several stages, one per cycle, and a new operation can start every cycle even though each one takes several cycles to finish.

:::

::: {#def-latency-issue .definition name="Latency and issue time"}

The *latency* $L$ of an operation is the number of cycles from start to result. Its *issue time* is the minimum number of cycles between two independent operations in one unit ($1$ for a fully pipelined unit). Typical values on a recent Intel core: integer add $L=1$; integer multiply $L=3$; floating-point add $L=3$; floating-point multiply $L=5$; all with issue time $1$.

:::

::: {#fig-instruction-level-parallelism-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.0cm, y=0.6cm]
\foreach \op [count=\i from 0] in {a,b,c} {
  \foreach \s in {1,2,3} {
    \pgfmathtruncatemacro{\t}{\i+\s}
    \draw[cell frame] (\t,-\i) rectangle (\t+1,-\i-0.8); \node[tick] at (\t+0.5,-\i-0.4) {$\op$: stage \s};
  }
  \node[lab, anchor=east] at (0.9,-\i-0.4) {operation $\op$};
}
\foreach \t in {1,...,5} { \node[tick] at (\t+0.5,-3.3) {cycle \t}; }
\end{tikzpicture}
\end{center}
```

A three-stage pipelined unit: each operation takes three cycles (latency $3$), but a new one starts every cycle (issue time $1$), so three independent operations finish in five cycles instead of nine

:::

::: {#thm-latency-bound .theorem name="Latency bound"}

If each iteration of a loop applies an operation of latency $L$ to an accumulator, and the next iteration needs the new accumulator value, then the loop needs at least $L$ cycles per element: $\mathit{CPE}\ge L$.

:::

::: {.proof}
1. Let $x_k$ be the accumulator after $k$ elements. Computing $x_{k+1}=x_k\ \mathrm{OP}\ a_{k+1}$ cannot start before $x_k$ is available.

2. Each such operation takes $L$ cycles from start to result, so $x_k$ is available no earlier than $kL$ cycles after $x_0$, by induction on $k$.

3. Hence $n$ elements take at least $nL$ cycles, whatever else the processor does in parallel.
:::

::: {#thm-throughput-bound .theorem name="Throughput bound"}

If the processor has $C$ functional units able to perform an operation, each with issue time $I$, then any loop performing one such operation per element has $\mathit{CPE}\ge I/C$. Similarly, a loop that loads one value per element has $\mathit{CPE}\ge 1/(\text{loads per cycle})$.

:::

::: {.proof}
1. In $T$ cycles each unit starts at most $T/I$ operations, so all units together start at most $CT/I$.

2. Processing $n$ elements needs $n$ operations, so $CT/I\ge n$, that is, $T/n\ge I/C$.
:::

::: {#def-loop-unrolling .definition name="Loop unrolling and multiple accumulators"}

*$k\times1$ unrolling* processes $k$ elements per iteration with one accumulator, reducing loop overhead (index updates and tests) but not the dependency chain. *$k\times k$ unrolling* (multiple accumulators) keeps $k$ accumulators: accumulator $r$ combines elements $r, r+k, r+2k,\dots$, and the $k$ partial results are combined at the end. *Reassociation* ($k\times1a$) writes the body as `acc = acc OP (a[i] OP a[i+1])`, so the inner operation does not wait for the accumulator.

:::

::: {#fig-instruction-level-parallelism-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.75cm]
\node[lab, anchor=south] at (1,0.4) {one accumulator};
\foreach \i in {0,...,5} { \node[small vertex] (s\i) at (1,-\i) {$\times$}; \node[tick, anchor=east] at (0.6,-\i) {$a_{\i}$}; }
\foreach \i [evaluate=\i as \j using int(\i+1)] in {0,...,4} { \draw[->, draw=accent, emph] (s\i) -- (s\j); }
\node[lab, anchor=south] at (5,0.4) {two accumulators};
\foreach \i in {0,...,2} { \node[small vertex] (e\i) at (4.2,-\i*2) {$\times$}; \node[tick, anchor=east] at (3.8,-\i*2) {$a_{\the\numexpr2*\i\relax}$}; }
\foreach \i in {0,...,2} { \node[small vertex] (o\i) at (5.8,-\i*2-1) {$\times$}; \node[tick, anchor=west] at (6.2,-\i*2-1) {$a_{\the\numexpr2*\i+1\relax}$}; }
\draw[->, draw=primary, emph] (e0) -- (e1); \draw[->, draw=primary, emph] (e1) -- (e2);
\draw[->, draw=primary, emph] (o0) -- (o1); \draw[->, draw=primary, emph] (o1) -- (o2);
\node[small vertex] (f) at (5,-6.2) {$\times$};
\draw[->] (e2) -- (f); \draw[->] (o2) -- (f);
\node[tick] at (1,-6.6) {critical path: $n$ operations};
\node[tick] at (5,-7.0) {critical path: about $n/2$};
\end{tikzpicture}
\end{center}
```

Computing a product of six elements. With one accumulator every multiplication waits for the previous one; with two accumulators two chains of half the length run in parallel

:::

::: {#thm-multiple-accumulators .theorem name="Multiple accumulators"}

With $k$ accumulators and a pipelined unit of latency $L$, the $k$ dependency chains have length $n/k$ each, so the latency bound becomes $\mathit{CPE}\ge L/k$. Increasing $k$ helps until $L/k$ falls to the throughput bound (@thm-throughput-bound), that is, until $k\ge L\cdot C/I$; beyond that the units are saturated.

:::

::: {.proof}
1. Accumulator $r$ depends only on its own previous value and on elements $a_r,a_{r+k},\dots$; the $k$ chains share no data, so their operations may overlap.

2. By @thm-latency-bound applied to each chain, chain $r$ needs at least $(n/k)L$ cycles, and nothing forces more: in a pipelined unit, operations of different chains can start on consecutive cycles.

3. So the total is at least $nL/k$ cycles, and when $L/k\ge I/C$ the units have room to start the $k$ chains' operations without waiting. Once $L/k<I/C$, @thm-throughput-bound is the binding limit.
:::

::: {#exm-unrolling-cpe .example name="Floating-point product, latency 5"}

With two floating-point multiply units, each able to start one multiplication per cycle ($C=2$, $I=1$) and $L=5$: one accumulator gives $\mathit{CPE}\approx5$; $2\times1$ unrolling does not help ($5$, the chain is unchanged); $2\times2$ gives $2.5$; $5\times5$ gives $1$; and about $10$ accumulators reach the throughput bound $0.5$. For integer addition ($L=1$) the first version is already at the latency bound $1$, and gains come only from more accumulators up to the load limit.

:::

::: {#rmk-instruction-level-parallelism-2 name="Reassociation changes floating-point results"}

Multiple accumulators and reassociation change the order of the operations. For integers this does not change the result (addition and multiplication mod $2^w$ are associative), but for floating point it can (@prp-fp-algebra), so compilers do it only when told to (`-ffast-math`) and otherwise it is the programmer's decision.

:::

::: {#def-branch-prediction .definition name="Branch prediction"}

When the processor meets a conditional branch whose outcome is not yet known, it *predicts* the outcome and executes the predicted path *speculatively*, keeping the results provisional. If the prediction was right, nothing is lost; if wrong, the provisional results are discarded and execution restarts at the correct target, at a cost of about $15$–$20$ cycles on current processors.

:::

::: {#rmk-instruction-level-parallelism-1 name="Vector instructions"}

SIMD (single instruction, multiple data) instructions apply one operation to several values packed in a wide register: an AVX2 register of 32 bytes holds eight `float`s or four `double`s, and one instruction adds them all. Compilers use them for simple loops over arrays; combined with multiple accumulators they can lower the CPE well below one element per cycle.

:::
