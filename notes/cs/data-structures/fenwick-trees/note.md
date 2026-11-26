---
title: "Fenwick Trees"
sources: [cs97si-3]
requires: [cs/data-structures/interfaces]
status: draft
---

<!-- Added 2026-11-26 from Stanford CS 97SI (Winter 2011-12), Lecture 3, in our own wording; proofs written out in steps. The example and figures are our own. -->

A prefix-sum array (@sec-cs-algorithm-patterns-prefix-sums) answers range sums in $O(1)$ but needs $O(n)$ work after every change of an entry. A *Fenwick tree* (binary indexed tree) supports both operations in $O(\log n)$ with one array of $n$ numbers.

::: {#def-fenwick-tree .definition name="Fenwick tree"}

For $i\ge1$ let $\operatorname{low}(i)=i\mathbin{\&}(-i)$ be the largest power of $2$ dividing $i$ (the lowest set bit). The Fenwick tree of $a_1,\dots,a_n$ is the array

$$
T[i]=\sum_{j=i-\operatorname{low}(i)+1}^{i}a_j\qquad(1\le i\le n),
$$

so $T[i]$ is the sum of the block of length $\operatorname{low}(i)$ that ends at $i$. Its operations:

- $\operatorname{prefix}(i)=a_1+\dots+a_i$: add $T[i]$ and replace $i$ by $i-\operatorname{low}(i)$, until $i=0$;
- $\operatorname{add}(i,\delta)$ ($a_i\gets a_i+\delta$): add $\delta$ to $T[i]$ and replace $i$ by $i+\operatorname{low}(i)$, while $i\le n$.

A range sum is $a_l+\dots+a_r=\operatorname{prefix}(r)-\operatorname{prefix}(l-1)$.

:::

```{=latex}
\begin{algorithm}
\caption{Fenwick tree operations}
\begin{algorithmic}
\INPUT Array $T[1..n]$, indices $1\le i\le n$
\STATE \textbf{function} $\operatorname{prefix}(i)$
\STATE \quad $s\gets0$
\WHILE{$i>0$}
    \STATE $s\gets s+T[i]$; $i\gets i-(i\mathbin{\&}-i)$
\ENDWHILE
\STATE \quad \textbf{return} $s$
\STATE \textbf{function} $\operatorname{add}(i,\delta)$
\WHILE{$i\le n$}
    \STATE $T[i]\gets T[i]+\delta$; $i\gets i+(i\mathbin{\&}-i)$
\ENDWHILE
\end{algorithmic}
\end{algorithm}
```

::: {#thm-fenwick-tree .theorem name="Fenwick tree"}

$\operatorname{prefix}(i)$ returns $a_1+\dots+a_i$, and $\operatorname{add}(i,\delta)$ updates exactly the entries $T[k]$ whose block contains $i$. Both take $O(\log n)$ time. Starting from $T=0$ and calling $\operatorname{add}(i,a_i)$ for every $i$ builds the tree in $O(n\log n)$.

:::

::: {.proof}

1. *Prefix.* The loop visits $i_0=i$, $i_1=i_0-\operatorname{low}(i_0)$, and so on. The block of $T[i_t]$ is $(i_{t+1},i_t]$, so the blocks visited are consecutive, disjoint, and together cover $(0,i]$. Hence the sum is $a_1+\dots+a_i$.

2. *Number of steps.* Subtracting $\operatorname{low}(i)$ clears the lowest set bit of $i$, so the loop runs at most once per bit, $O(\log n)$ times.

3. *Blocks are dyadic.* If $\operatorname{low}(k)=2^j$, the block of $k$ is $(k-2^j,k]=(m2^j,(m+1)2^j]$ with $m+1=k/2^j$ odd. Two dyadic intervals are nested or disjoint. The dyadic interval of length $2^s$ ending at $r$ is a block exactly when $\operatorname{low}(r)=2^s$.

4. *Add visits every block containing $i$.* The first block containing $i$ is that of $k=i$ itself, since every block containing $i$ ends at some $k\ge i$ and has length at least $\operatorname{low}(i)$. Let $k$ be a block containing $i$ with $\operatorname{low}(k)=2^j$, and $k'=k+2^j$. Then $k'$ is a multiple of $2^{j+1}$, so $\operatorname{low}(k')\ge2^{j+1}$ and the block of $k'$ starts at $k'-\operatorname{low}(k')\le k-2^j$; it contains the block of $k$, hence $i$. For any $s$ with $2^j<2^s<\operatorname{low}(k')$, the dyadic interval of length $2^s$ containing the block of $k$ ends at the multiple of $2^s$ in $[k,k+2^s)$, which is $k'$; as $\operatorname{low}(k')\ne2^s$ it is not a block. So $k'$ is the next block containing $i$, and the loop visits all of them in increasing order.

5. *Steps of add.* Each step at least doubles $\operatorname{low}(i)$, so at most $\lfloor\log_2 n\rfloor+1$ steps happen before $i>n$.

6. *Build.* $n$ calls of $\operatorname{add}$ at $O(\log n)$ each.

:::

::: {#exm-fenwick-tree-1 .example name="Eight entries"}

For $a=(5,2,9,-3,5,20,10,-8)$ the tree is $T=(5,7,9,13,5,25,10,40)$: for instance $T[6]=a_5+a_6=25$ and $T[8]$ is the total $40$. Then $\operatorname{prefix}(7)=T[7]+T[6]+T[4]=10+25+13=48$, and $\operatorname{add}(3,\delta)$ changes $T[3]$, $T[4]$ and $T[8]$.

:::

::: {#fig-fenwick-tree-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.35cm,y=0.6cm]
\foreach \i/\v in {1/5,2/2,3/9,4/-3,5/5,6/20,7/10,8/-8} {
  \draw[cell frame] (\i-0.47,-0.4) rectangle (\i+0.47,0.4); \node[lab,tick] at (\i,0) {$\v$};
  \node[lab,tick] at (\i,-0.9) {$\i$};
}
\node[lab,tick,anchor=east] at (0.4,0) {$a$};
\foreach \i/\l/\v in {1/1/5,3/1/9,5/1/5,7/1/10,2/2/7,6/2/25,4/4/13,8/8/40} {
  \pgfmathsetmacro{\y}{1.2+1.1*log2(\l)}
  \draw[cell frame] (\i-\l+0.55,\y-0.4) rectangle (\i+0.45,\y+0.4);
  \node[lab,tick] at (\i-\l/2+0.5,\y) {$T[\i]=\v$};
}
\foreach \i/\l in {7/1,6/2,4/4} {
  \pgfmathsetmacro{\y}{1.2+1.1*log2(\l)}
  \draw[hl] (\i-\l+0.55,\y-0.4) rectangle (\i+0.45,\y+0.4);
}
\end{tikzpicture}
\end{center}
```

@exm-fenwick-tree-1: each $T[i]$ covers the block of length $\operatorname{low}(i)$ ending at $i$. The highlighted blocks $T[7]$, $T[6]$, $T[4]$ tile $[1,7]$, so $\operatorname{prefix}(7)=48$.

:::

::: {#rmk-fenwick-tree-1 .remark name="Extensions"}

The same index walks work in two dimensions: $T[i][j]$ stores the sum over a rectangle of blocks, and both operations become two nested loops, $O(\log^2 n)$. Storing differences $a_i-a_{i-1}$ instead turns range additions into two point updates. Unlike a segment tree, a Fenwick tree needs an invertible operation (sums, XOR) to answer arbitrary ranges; it cannot answer range minima this way.

:::
