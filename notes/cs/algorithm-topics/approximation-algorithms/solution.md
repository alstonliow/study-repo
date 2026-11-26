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

::: {.solution for="prob-mit6854ps-5-q1" status="draft"}
Let the FF bins be $1,\dots,L$ in order of opening, with final contents $c_1,\dots,c_L$, and $S=\sum_ia_i\le L^*$.

*(a)* For $i<j$, the first item put into bin $j$ did not fit into bin $i$ at that time, and bin $i$ only fills up later, so $c_i+c_j>1$. If $L=1$ the claim is $1\le2L^*-1$. If $L\ge2$, add this over the $L$ pairs $(1,2),(2,3),\dots,(L-1,L),(1,L)$: every bin occurs twice, so $2S>L$. Hence $L<2S\le2L^*$, and as both are integers, $L\le2L^*-1$.

*(b)*

1. *$|B_3|\le2$.* A bin of $B_3$ has content at most $\tfrac23$ and only items of size at most $\tfrac12$. Let $i<j<k$ be three bins of $B_3$. Each item $x$ of bin $j$ did not fit into bin $i$: $x>1-c_i\ge\tfrac13$. Two such items would exceed $\tfrac23$, so bin $j$ holds a single item, and $c_j\le\tfrac12$. Then the item of bin $k$ did not fit into bin $j$: it exceeds $1-c_j\ge\tfrac12$, contradicting $k\in B_3$.

2. *Counting.* Let $p=|B_2|$. Bins of $B_1$ hold more than $\tfrac23$, bins of $B_2$ more than $\tfrac12$, so $S>\tfrac23|B_1|+\tfrac12p$, i.e. $|B_1|<\tfrac32S-\tfrac34p$. The $p$ items larger than $\tfrac12$ need $p$ different bins, so $p\le L^*$.

3. Hence $L_{FF}=|B_1|+p+|B_3|<\tfrac32S+\tfrac14p+2\le\tfrac32L^*+\tfrac14L^*+2=\tfrac74L^*+2$.
:::

::: {.solution for="prob-mit6854ps-5-q2" status="draft"}
Let $U_j$ be the size of the union of the first $j$ greedy sets ($U_0=0$), and let $O_1,\dots,O_k$ be an optimal choice.

1. The optimal sets cover $\mathrm{OPT}$ elements, of which at least $\mathrm{OPT}-U_{j-1}$ are not yet covered after $j-1$ greedy steps. These lie in $k$ sets, so one $O_l$ contains at least $(\mathrm{OPT}-U_{j-1})/k$ of them. The greedy set gains at least as much: $U_j-U_{j-1}\ge(\mathrm{OPT}-U_{j-1})/k$.

2. Rearranged: $\mathrm{OPT}-U_j\le(1-\tfrac1k)(\mathrm{OPT}-U_{j-1})$, and by induction $\mathrm{OPT}-U_j\le(1-\tfrac1k)^j\mathrm{OPT}$, which is the hint.

3. With $j=k$: $U_k\ge\big(1-(1-\tfrac1k)^k\big)\mathrm{OPT}\ge(1-\tfrac1e)\mathrm{OPT}$.
:::
