<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-9-q1" status="draft"}
(a) Take capacity $B=2k$ and two items: $a_1$ with size $1$ and value $2$ (density $2$), and $a_2$ with size $2k$ and value $2k$ (density $1$). $Alg_1$ takes $a_1$, after which $a_2$ no longer fits: value $2$. The optimum takes $a_2$: value $2k$, so $Alg_1$ gets $\frac{v_{Opt}}k$.

(b) If everything fits, $Alg_2$ is optimal. Otherwise, filling the knapsack greedily by density and taking a *fraction* of item $a_i$ gives the optimum of the fractional problem (any other filling can be improved by exchanging less dense material for denser), so $v_{Opt}\le\sum_{j<i}v_j+v_i$. $Alg_2$ returns $\max\{v_i,\sum_{j<i}v_j\}$, which is at least half of that sum. Both returned sets fit: the first $i-1$ items by the choice of $i$, and $a_i$ since $s_i\le B$.

(c) $S_{0,0}=0$ and $S_{0,v}=\infty$ for $v>0$; then $S_{i,v}=\min\{S_{i-1,v},\ s_i+S_{i-1,v-v_i}\}$ (the second term only when $v_i\le v$). The optimum value is the largest $v$ with $S_{n,v}\le B$, and parent pointers recover the items. There are $n\cdot nV$ subproblems with $O(1)$ work: $O(n^2V)$ time, pseudopolynomial.

(d) The scaled values are at most $\frac n\varepsilon$, so $Alg_3$ on them runs in $O(n^2\cdot\frac n\varepsilon)=O(n^3/\varepsilon)$, polynomial in $n$ and $\frac1\varepsilon$. Let $\mu=\frac{\varepsilon V}n$, so $v'_i=\lfloor v_i/\mu\rfloor$ and $\mu v'_i\le v_i<\mu(v'_i+1)$. For the returned set $C$ (optimal for the scaled values) and an optimal set $O$:
$$v_C\ge\mu\,v'_C\ge\mu\,v'_O\ge v_O-\mu|O|\ge v_O-\varepsilon V\ge(1-\varepsilon)v_O,$$
using $|O|\le n$ and $v_O\ge V$ (the most valuable item fits alone). So the ratio is at most $\frac1{1-\varepsilon}$, which is $1+O(\varepsilon)$: $Alg_4$ is an FPTAS (@def-approximation-ratio).
:::
