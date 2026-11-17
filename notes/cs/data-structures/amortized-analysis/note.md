---
title: "Amortized Analysis"
sources: [mit6046-5]
requires: [cs/data-structures/linked-lists-and-dynamic-arrays]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 5, in our own wording; proofs written out in steps. Extends @def-amortized-cost. -->

An operation has amortized cost $\hat c$ if every sequence of operations, starting from an empty structure, costs at most the sum of the amortized costs (@def-amortized-cost). Four methods prove such bounds. We use two running examples: a dynamic table that doubles when full (@def-dynamic-array), and a binary counter.

::: {#exm-binary-counter .example name="Binary counter"}

A $k$-bit counter is incremented by flipping the trailing $1$s to $0$ and the next $0$ to $1$. One increment can flip all $k$ bits, but $n$ increments from $0$ flip $O(n)$ bits in total: bit $i$ flips once every $2^i$ increments, so the total is at most $\sum_in/2^i<2n$.

:::

::: {#fig-amortized-analysis-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.500,0.500);
\node[lab] at (0.250,0.250) {$0$};
\draw[cell frame] (0.500,0.000) rectangle (1.000,0.500);
\node[lab] at (0.750,0.250) {$0$};
\draw[cell frame] (1.000,0.000) rectangle (1.500,0.500);
\node[lab] at (1.250,0.250) {$0$};
\draw[cell frame] (1.500,0.000) rectangle (2.000,0.500);
\node[lab] at (1.750,0.250) {$0$};
\node[lab, anchor=east] at (-0.100,0.250) {0};
\draw[cell frame] (0.000,-0.620) rectangle (0.500,-0.120);
\node[lab] at (0.250,-0.370) {$0$};
\draw[cell frame] (0.500,-0.620) rectangle (1.000,-0.120);
\node[lab] at (0.750,-0.370) {$0$};
\draw[cell frame] (1.000,-0.620) rectangle (1.500,-0.120);
\node[lab] at (1.250,-0.370) {$0$};
\draw[hl cell] (1.500,-0.620) rectangle (2.000,-0.120);
\node[lab] at (1.750,-0.370) {$1$};
\node[lab, anchor=east] at (-0.100,-0.370) {1};
\node[lab,tick, anchor=west] at (2.15,-0.37) {1 flips};
\draw[cell frame] (0.000,-1.240) rectangle (0.500,-0.740);
\node[lab] at (0.250,-0.990) {$0$};
\draw[cell frame] (0.500,-1.240) rectangle (1.000,-0.740);
\node[lab] at (0.750,-0.990) {$0$};
\draw[hl cell] (1.000,-1.240) rectangle (1.500,-0.740);
\node[lab] at (1.250,-0.990) {$1$};
\draw[hl cell] (1.500,-1.240) rectangle (2.000,-0.740);
\node[lab] at (1.750,-0.990) {$0$};
\node[lab, anchor=east] at (-0.100,-0.990) {2};
\node[lab,tick, anchor=west] at (2.15,-0.99) {2 flips};
\draw[cell frame] (0.000,-1.860) rectangle (0.500,-1.360);
\node[lab] at (0.250,-1.610) {$0$};
\draw[cell frame] (0.500,-1.860) rectangle (1.000,-1.360);
\node[lab] at (0.750,-1.610) {$0$};
\draw[cell frame] (1.000,-1.860) rectangle (1.500,-1.360);
\node[lab] at (1.250,-1.610) {$1$};
\draw[hl cell] (1.500,-1.860) rectangle (2.000,-1.360);
\node[lab] at (1.750,-1.610) {$1$};
\node[lab, anchor=east] at (-0.100,-1.610) {3};
\node[lab,tick, anchor=west] at (2.15,-1.61) {1 flips};
\draw[cell frame] (0.000,-2.480) rectangle (0.500,-1.980);
\node[lab] at (0.250,-2.230) {$0$};
\draw[hl cell] (0.500,-2.480) rectangle (1.000,-1.980);
\node[lab] at (0.750,-2.230) {$1$};
\draw[hl cell] (1.000,-2.480) rectangle (1.500,-1.980);
\node[lab] at (1.250,-2.230) {$0$};
\draw[hl cell] (1.500,-2.480) rectangle (2.000,-1.980);
\node[lab] at (1.750,-2.230) {$0$};
\node[lab, anchor=east] at (-0.100,-2.230) {4};
\node[lab,tick, anchor=west] at (2.15,-2.23) {3 flips};
\draw[cell frame] (0.000,-3.100) rectangle (0.500,-2.600);
\node[lab] at (0.250,-2.850) {$0$};
\draw[cell frame] (0.500,-3.100) rectangle (1.000,-2.600);
\node[lab] at (0.750,-2.850) {$1$};
\draw[cell frame] (1.000,-3.100) rectangle (1.500,-2.600);
\node[lab] at (1.250,-2.850) {$0$};
\draw[hl cell] (1.500,-3.100) rectangle (2.000,-2.600);
\node[lab] at (1.750,-2.850) {$1$};
\node[lab, anchor=east] at (-0.100,-2.850) {5};
\node[lab,tick, anchor=west] at (2.15,-2.85) {1 flips};
\draw[cell frame] (0.000,-3.720) rectangle (0.500,-3.220);
\node[lab] at (0.250,-3.470) {$0$};
\draw[cell frame] (0.500,-3.720) rectangle (1.000,-3.220);
\node[lab] at (0.750,-3.470) {$1$};
\draw[hl cell] (1.000,-3.720) rectangle (1.500,-3.220);
\node[lab] at (1.250,-3.470) {$1$};
\draw[hl cell] (1.500,-3.720) rectangle (2.000,-3.220);
\node[lab] at (1.750,-3.470) {$0$};
\node[lab, anchor=east] at (-0.100,-3.470) {6};
\node[lab,tick, anchor=west] at (2.15,-3.47) {2 flips};
\draw[cell frame] (0.000,-4.340) rectangle (0.500,-3.840);
\node[lab] at (0.250,-4.090) {$0$};
\draw[cell frame] (0.500,-4.340) rectangle (1.000,-3.840);
\node[lab] at (0.750,-4.090) {$1$};
\draw[cell frame] (1.000,-4.340) rectangle (1.500,-3.840);
\node[lab] at (1.250,-4.090) {$1$};
\draw[hl cell] (1.500,-4.340) rectangle (2.000,-3.840);
\node[lab] at (1.750,-4.090) {$1$};
\node[lab, anchor=east] at (-0.100,-4.090) {7};
\node[lab,tick, anchor=west] at (2.15,-4.09) {1 flips};
\draw[hl cell] (0.000,-4.960) rectangle (0.500,-4.460);
\node[lab] at (0.250,-4.710) {$1$};
\draw[hl cell] (0.500,-4.960) rectangle (1.000,-4.460);
\node[lab] at (0.750,-4.710) {$0$};
\draw[hl cell] (1.000,-4.960) rectangle (1.500,-4.460);
\node[lab] at (1.250,-4.710) {$0$};
\draw[hl cell] (1.500,-4.960) rectangle (2.000,-4.460);
\node[lab] at (1.750,-4.710) {$0$};
\node[lab, anchor=east] at (-0.100,-4.710) {8};
\node[lab,tick, anchor=west] at (2.15,-4.71) {4 flips};
\end{tikzpicture}
\end{center}
```

A $4$-bit counter counting from $0$ to $8$; highlighted bits flip at each increment. The step to $8$ flips four bits, but the eight increments flip $15<2\cdot8$ bits in total.

:::

The last sentence is the *aggregate method*: bound the total cost of any $n$ operations and divide by $n$.

## The accounting method

::: {#def-accounting-method .definition name="Accounting method"}

Charge each operation an amortized cost $\hat c_i$. When $\hat c_i$ exceeds the actual cost $c_i$, store the difference as *credit* on parts of the structure; an operation may pay part of its actual cost from stored credit. If the stored credit never becomes negative, then $\sum_ic_i\le\sum_i\hat c_i$ for every sequence.

:::

For the counter, charge $2$ per increment: $1$ pays for setting a bit to $1$, and $1$ is stored on that bit. When a $1$ is later reset to $0$, its stored credit pays. Every $1$-bit carries one credit, so the credit is never negative, and increments cost $O(1)$ amortized.

For the table, charge $3$ per insertion: $1$ for writing the item and $2$ stored on it. When a full table of size $m$ doubles, the $m/2$ items inserted since the last doubling have stored $m$ credits, enough to copy all $m$ items.

## The potential method

::: {#def-potential-method .definition name="Potential method"}

Choose a *potential function* $\Phi$ from states of the structure to real numbers with $\Phi\ge\Phi_0$, the potential of the empty structure. The amortized cost of an operation that takes the state from $D_{i-1}$ to $D_i$ at actual cost $c_i$ is
$$\hat c_i=c_i+\Phi(D_i)-\Phi(D_{i-1}).$$

:::

::: {#thm-potential-method .theorem name="Potential method"}

For every sequence of $n$ operations, $\sum_{i=1}^nc_i\le\sum_{i=1}^n\hat c_i$.

:::

::: {.proof}

1. Summing the definition, the potential terms telescope: $\sum_i\hat c_i=\sum_ic_i+\Phi(D_n)-\Phi(D_0)$.

2. Since $\Phi(D_n)\ge\Phi(D_0)$, the sum of the amortized costs is at least the sum of the actual costs.

:::

The potential is the credit of the accounting method, stored in the whole structure instead of on its parts. For the counter take $\Phi$ = number of $1$-bits: an increment that resets $t$ bits costs $t+1$ and changes $\Phi$ by $1-t$, so $\hat c=2$.

::: {#prp-table-doubling-halving .proposition name="Doubling and halving tables"}

Let a table of size $m$ holding $n$ items double when an insertion finds it full and halve when a deletion leaves it a quarter full. With $\Phi=|2n-m|$ (and copying $n$ items costing $n$), insertions and deletions cost $O(1)$ amortized.

:::

::: {.proof}

1. Right after a resize, $n=m/2$, so $\Phi=0$.

2. An insertion or deletion without resizing has actual cost $1$ and changes $\Phi$ by at most $2$: amortized cost at most $3$.

3. A doubling happens when $n=m$, so $\Phi=m$ before it; it costs $m$ to copy, after which $\Phi$ is about $0$. The release of potential pays for the copy, so the amortized cost is $O(1)$.

4. A halving happens when $n=m/4$, so $\Phi=|m/2-m|=m/2$; copying $m/4$ items is paid by the drop of $\Phi$ to about $0$.

:::

## The charging method

Another view is to *charge* the cost of an expensive operation to earlier cheap operations, and to show that no operation is charged more than a constant number of times. For the table, a doubling to size $2m$ is charged to the $m/2$ insertions since the previous resize, each paying $O(1)$, and these insertions are never charged again. Amortization is how the bounds for 2-3 trees, union-find (@sec-cs-data-structures-union-find) and dynamic arrays are proved.
