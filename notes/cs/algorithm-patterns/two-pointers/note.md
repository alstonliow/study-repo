---
title: "Two Pointers"
sources: []
requires: [cs/sorting/comparison-sorting]
status: draft
---

<!-- Added 2026-11-26 in our own words (owner decision 2026-11-26: new notes for the LeetCode Hot 100 problems without a fitting note). No single source; TODO: add a source if one is integrated later. The examples and figures are our own. -->

A *two-pointer* scan keeps two indices into an array and moves one of them at every step, so it finishes in $O(n)$ steps. Its correctness rests on an argument that each move discards only candidates that cannot be the answer.

## Pointers from both ends

::: {#prp-two-pointers-pair-sum .proposition name="Pair with a given sum"}

Let $A[1..n]$ be sorted in nondecreasing order and $t$ a target. Start with $\ell=1$, $r=n$; while $\ell<r$, stop if $A[\ell]+A[r]=t$, set $\ell\gets\ell+1$ if the sum is less than $t$, and $r\gets r-1$ if it is greater. This finds indices $i<j$ with $A[i]+A[j]=t$ whenever they exist, in $O(n)$ time.

:::

::: {.proof}

1. *Invariant.* Every solution pair $(i,j)$ has $\ell\le i<j\le r$. It holds at the start.

2. *A move up keeps it.* If $A[\ell]+A[r]<t$, then for every $j\le r$, $A[\ell]+A[j]\le A[\ell]+A[r]<t$ because $A$ is sorted. So no solution uses $\ell$, and discarding it keeps the invariant. The move $r\gets r-1$ is symmetric.

3. *Termination.* Each step shrinks $r-\ell$ by one, so after at most $n-1$ steps either a solution is reported or $\ell=r$, and then by the invariant there is none.

:::

::: {#fig-two-pointers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.7cm,y=0.7cm]
\foreach \v [count=\i] in {1,3,4,6,8,11} { \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\v$}; }
\draw[hl cell] (0,0) rectangle (1,1); \node[lab] at (0.5,0.5) {$1$};
\draw[hl cell] (5,0) rectangle (6,1); \node[lab] at (5.5,0.5) {$11$};
\node[lab,tick] at (0.5,-0.4) {$\ell$}; \node[lab,tick] at (5.5,-0.4) {$r$};
\node[lab,note,anchor=west] at (6.4,0.5) {$1+11=12>10$: move $r$};
\end{tikzpicture}
\end{center}
```

Looking for sum $10$. The sum $12$ is too big, and $11$ is too big with every remaining partner (all are $\ge1$), so $r$ moves left. The scan continues with $1+8<10$, $3+8>10$, $3+6<10$ and stops at $4+6=10$.

:::

The same discarding argument solves other problems on lines and bars.

::: {#exm-two-pointers-container .example name="Container with most water"}

Given heights $h[1..n]$, maximise $(j-i)\min(h[i],h[j])$. Start from both ends and always move the pointer at the shorter line. If $h[\ell]\le h[r]$, every container $(\ell,j)$ with $j<r$ is narrower and no taller than $\min(h[\ell],h[j])\le h[\ell]$, so it holds less than $(\ell,r)$; hence $\ell$ can be discarded. So one $O(n)$ scan finds the maximum.

:::

::: {#exm-two-pointers-three-sum .example name="Three numbers summing to zero"}

To list all triples of values summing to $0$, sort $A$ in $O(n\log n)$ time, then for each $i$ run the pair scan on $A[i+1..n]$ with target $-A[i]$, continuing past each solution instead of stopping. Skip an $i$ with $A[i]=A[i-1]$, and after a solution move $\ell$ and $r$ past equal values, so each triple of values is reported once. The total time is $O(n^2)$.

:::

::: {#fig-two-pointers-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.35cm]
\foreach \v [count=\i] in {1,8,6,2,5,4,8,3,7} { \draw[bar] (\i-0.6,0) rectangle (\i-0.4,\v); \node[lab,tick] at (\i-0.5,-0.7) {\i}; }
\fill[tintA] (1.5,0) rectangle (8.5,7);
\draw[hl] (1.5,7) -- (8.5,7);
\node[lab,note,anchor=west] at (9.3,4) {$(9-2)\cdot7=49$};
\end{tikzpicture}
\end{center}
```

Heights $1,8,6,2,5,4,8,3,7$. The best container uses lines $2$ and $9$ and holds $49$. The scan reaches it by first discarding line $1$, the shorter of lines $1$ and $9$.

:::

::: {#exm-two-pointers-rain .example name="Trapped rain water"}

Water above bar $i$ rises to $\min(L_i,R_i)$, where $L_i=\max h[1..i]$ and $R_i=\max h[i..n]$, so the total is $\sum_i(\min(L_i,R_i)-h[i])$. Two pointers find it with $O(1)$ extra space: keep the running maxima $L$ from the left and $R$ from the right. If $L\le R$, the true $R_\ell$ is at least $R\ge L=L_\ell$, so bar $\ell$ holds exactly $L-h[\ell]$; add it and move $\ell$. Otherwise handle $r$ symmetrically.

:::

::: {#fig-two-pointers-3}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.5cm,y=0.5cm]
\foreach \v/\w [count=\i] in {0/0,1/1,0/1,2/2,1/2,0/2,1/2,3/3,2/2,1/2,2/2,1/1} {
  \fill[tintA] (\i-1,\v) rectangle (\i,\w);
  \draw[bar] (\i-1,0) rectangle (\i,\v);
}
\draw[faint] (0,0) -- (12,0);
\end{tikzpicture}
\end{center}
```

Bars $0,1,0,2,1,0,1,3,2,1,2,1$ trap $6$ units of water (shaded): each bar is filled up to the lower of the highest bars on its two sides.

:::

## Pointers in the same direction

::: {#rmk-two-pointers-1 .remark name="Read and write pointers"}

To compact an array in place, a *read* pointer $i$ scans every position and a *write* pointer $w$ marks the end of the kept prefix. For moving all zeros to the end while keeping the order of the other values: for $i=1,\dots,n$, if $A[i]\ne0$, swap $A[i]$ with $A[w+1]$ and set $w\gets w+1$. The invariant is that $A[1..w]$ holds the nonzero values among $A[1..i]$ in their original order, and $A[w+1..i]$ holds only zeros. It takes $O(n)$ time and $O(1)$ extra space.

:::
