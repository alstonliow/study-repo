---
title: "Fixed-Parameter Algorithms"
sources: [mit6046-18]
requires: [cs/theory/approximation-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 18, in our own wording; proofs written out in steps. -->

An NP-hard problem may still be easy when some *parameter* of the input is small. Our example is *$k$-vertex cover*: given a graph $G=(V,E)$ and an integer $k$, is there a vertex cover with at most $k$ vertices? Let $n=|V|$ and $m=|E|$.

Trying all sets of $k$ vertices takes $\binom nk\cdot O(m)=O(n^km)$ time. This is polynomial for each fixed $k$, but the degree grows with $k$, which is useless already for $k=10$ on large graphs.

::: {#def-fpt .definition name="Fixed-parameter tractable"}

A *parameterised problem* has inputs with a size $n$ and a non-negative integer parameter $k$. It is *fixed-parameter tractable* (FPT) if it can be solved in time $f(k)\cdot n^{O(1)}$ for some computable function $f$, with the exponent of $n$ independent of $k$. Equivalently (as one can show), in time $f(k)+n^{O(1)}$.

:::

## Bounded search tree

::: {#thm-vertex-cover-branching .theorem name="Vertex cover in $O(2^km)$"}

Pick any edge $\{u,v\}$. Any vertex cover contains $u$ or $v$, so recursively try both: put $u$ in the cover and solve $(G-u,k-1)$, or put $v$ in and solve $(G-v,k-1)$. Answer NO when $k=0$ and edges remain, YES when no edges remain. This decides $k$-vertex cover in $O(2^km)$ time.

:::

::: {.proof}

1. *Correctness*, by induction on $k$: a cover of size at most $k$ for $G$ exists iff one of the two smaller instances has a cover of size at most $k-1$, because every cover contains $u$ or $v$, and removing a covered vertex removes its edges.

2. *Time:* the recursion tree is binary with depth at most $k$, so it has at most $2^{k+1}$ nodes, each doing $O(m)$ work to delete a vertex and find an edge.

:::

::: {#fig-fixed-parameter-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r) at (0,0) {$(G,k)$};
\node[box] (a) at (-2.2,-1.1) {$(G-u,k-1)$};
\node[box] (b) at (2.2,-1.1) {$(G-v,k-1)$};
\node[box] (aa) at (-3.3,-2.2) {$k-2$}; \node[box] (ab) at (-1.1,-2.2) {$k-2$}; \node[box] (ba) at (1.1,-2.2) {$k-2$}; \node[box] (bb) at (3.3,-2.2) {$k-2$};
\draw (r) -- node[edge label] {$u$} (a); \draw (r) -- node[edge label] {$v$} (b);
\draw (a)--(aa) (a)--(ab) (b)--(ba) (b)--(bb);
\node[lab,tick] at (0,-2.9) {$\vdots$ depth at most $k$: at most $2^k$ leaves};
\end{tikzpicture}
\end{center}
```

The bounded search tree for $k$-vertex cover: for an uncovered edge $\{u,v\}$, branch on putting $u$ or $v$ in the cover. Each branch lowers $k$, so the tree has depth at most $k$ and at most $2^k$ leaves, whatever the size of the graph.

:::

For $k=O(\log n)$ this is polynomial, and in practice it works for $k$ up to around $30$.

## Kernelization

::: {#def-kernel .definition name="Kernel"}

A *kernelization* is a polynomial-time algorithm that turns an instance $(x,k)$ into an equivalent instance $(x',k')$ with $k'\le k$ whose size is bounded by a function $g(k)$ of the parameter alone. The reduced instance is the *kernel*.

:::

::: {#thm-vertex-cover-kernel .theorem name="A quadratic kernel for vertex cover"}

Make the graph simple (a vertex with a loop must be in the cover: take it and decrease $k$; drop repeated edges). Then repeat: if a vertex has degree greater than $k$, put it in the cover and decrease $k$ by $1$. Delete isolated vertices. If $k$ becomes negative, or more than $k^2$ edges remain, answer NO. Otherwise the remaining graph has at most $k^2$ edges and $2k^2$ vertices, and is equivalent to the original. Combined with @thm-vertex-cover-branching this decides $k$-vertex cover in $O(n+m+2^kk^2)$ time.

:::

::: {.proof}

1. A vertex $v$ of degree greater than $k$ must be in every cover of size at most $k$: otherwise all its more than $k$ neighbours would have to be.

2. After the rule no longer applies, every vertex covers at most $k$ edges, so a cover of size at most $k$ covers at most $k^2$ edges. With more edges the answer is NO.

3. Otherwise there are at most $k^2$ edges, hence at most $2k^2$ non-isolated vertices. The reductions take $O(n+m)$ time, and branching on the kernel takes $O(2^kk^2)$.

:::

::: {#thm-fpt-kernel .theorem name="FPT means kernelizable"}

A decidable parameterised problem is FPT if and only if it has a kernelization.

:::

::: {.proof}

1. *Kernel ⇒ FPT:* shrink to size $g(k)$ in polynomial time, then solve the kernel by any algorithm, in time depending on $k$ only.

2. *FPT ⇒ kernel:* suppose an algorithm runs in time $f(k)n^c$. If $n\ge f(k)$, it runs in $n^{c+1}$, polynomial time, so the kernelization can just solve the instance and output a trivial YES or NO instance of constant size. If $n<f(k)$, the instance already has size less than $f(k)$ and is its own kernel.

:::

::: {#rmk-fixed-parameter-algorithms-approx .remark name="Connection to approximation"}

FPT algorithms can give approximation schemes: if an optimisation problem has an FPT algorithm in the size $k$ of the optimum, then for small optima it is solved exactly. Conversely, problems believed not to be FPT (such as $k$-clique, which is $\mathrm W[1]$-hard) are not expected to have efficient exact algorithms even for moderate $k$.

:::
