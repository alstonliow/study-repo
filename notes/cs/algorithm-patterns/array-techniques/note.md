---
title: "Array and Matrix Techniques"
sources: []
requires: [cs/data-structures/interfaces]
status: draft
---

<!-- Added 2026-11-26 in our own words (owner decision 2026-11-26: new notes for the LeetCode Hot 100 problems without a fitting note). No single source; TODO: add a source if one is integrated later. The examples and figures are our own. -->

Short algorithms that work on a static array (@def-static-array) or a matrix in place, with $O(1)$ extra space. Each rests on one invariant.

## Majority vote

::: {#thm-boyer-moore-majority .theorem name="Boyer–Moore majority vote"}

Scan $A[1..n]$ with a candidate $x$ and a counter $c=0$: at each element $a$, if $c=0$ set $x\gets a$; then increase $c$ if $a=x$ and decrease it otherwise. If some value occurs more than $n/2$ times, it is the final $x$.

:::

::: {.proof}

1. *Pairing.* Each decrement pairs the current element with one earlier copy of $x$ counted in $c$, and the two are different values. Paired elements are never used again.

2. At the end, the unpaired elements are the $c$ copies of the final $x$, and every other element is in a pair of two different values.

3. Let $m$ occur more than $n/2$ times. Each pair contains at most one copy of $m$, so at most $n/2$ copies of $m$ are paired. Hence some copy of $m$ is unpaired, and the unpaired elements are copies of $x$, so $x=m$.

:::

If a majority is not guaranteed, a second pass counts $x$ to check.

## Permutations and rotations in place

::: {#prp-next-permutation .proposition name="Next permutation"}

To turn $A[1..n]$ into the next arrangement in lexicographic order: find the largest $i$ with $A[i]<A[i+1]$; if there is none, $A$ is the last arrangement, so reverse it to get the first. Otherwise find the largest $j>i$ with $A[j]>A[i]$, swap $A[i]$ and $A[j]$, and reverse $A[i+1..n]$. This takes $O(n)$ time.

:::

::: {.proof}

1. *The suffix is maximal.* By the choice of $i$, $A[i+1..n]$ is nonincreasing, so it is already the largest arrangement of its elements. The next arrangement must therefore change position $i$, and keep $A[1..i-1]$.

2. *Smallest increase at $i$.* Position $i$ must get the smallest value in the suffix that exceeds $A[i]$. Since the suffix is nonincreasing, that is $A[j]$ for the largest $j$ with $A[j]>A[i]$.

3. *Smallest suffix.* After the swap the suffix is still nonincreasing ($A[j-1]\ge A[j]>A[i]\ge A[j+1]$), so reversing it gives its smallest arrangement.

:::

::: {#fig-array-techniques-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.6cm]
\foreach \v [count=\i] in {1,3,5,4,2} { \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\v$}; }
\draw[hl cell] (1,0) rectangle (2,1); \node[lab] at (1.5,0.5) {$3$};
\draw[hl cell] (3,0) rectangle (4,1); \node[lab] at (3.5,0.5) {$4$};
\node[lab,tick] at (1.5,-0.4) {$i$}; \node[lab,tick] at (3.5,-0.4) {$j$};
\draw[->] (5.4,0.5) -- (6.6,0.5);
\begin{scope}[xshift=4.2cm]
\foreach \v [count=\i] in {1,4,5,3,2} { \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\v$}; }
\end{scope}
\draw[->] (12.4,0.5) -- (13.6,0.5);
\begin{scope}[xshift=8.4cm]
\foreach \v [count=\i] in {1,4,2,3,5} { \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\v$}; }
\draw[hl] (2,-0.1) rectangle (5,1.1);
\end{scope}
\end{tikzpicture}
\end{center}
```

Next permutation of $13542$: the suffix $542$ is nonincreasing, so $i=2$; the smallest larger value in it is $4$; swap to get $14532$, then reverse the suffix to get $14235$.

:::

::: {#rmk-array-techniques-rotate .remark name="Rotation by reversals"}

Rotating $A[1..n]$ right by $k$ (with $k$ taken mod $n$) sends $A=XY$, with $|Y|=k$, to $YX$. Since $(X^RY^R)^R=YX$, where $^R$ is reversal, it suffices to reverse the whole array, then its first $k$ entries, then the remaining $n-k$: $O(n)$ time, $O(1)$ space.

:::

::: {#prp-array-techniques-missing .proposition name="Smallest missing positive"}

The smallest positive integer not in $A[1..n]$ can be found in $O(n)$ time and $O(1)$ extra space.

:::

::: {.proof}

1. The answer lies in $\{1,\dots,n+1\}$, since $n$ entries cannot cover all of $1,\dots,n+1$.

2. *Cyclic placement.* For $i=1,\dots,n$: while $1\le A[i]\le n$ and $A[A[i]]\ne A[i]$, swap $A[i]$ with $A[A[i]]$. Each swap puts one value $v$ at position $v$ for good, so there are at most $n$ swaps in total.

3. Afterwards, every $v\in\{1,\dots,n\}$ present in $A$ is at position $v$. So the answer is the first $i$ with $A[i]\ne i$, or $n+1$ if there is none.

:::

## Matrices

::: {#rmk-array-techniques-matrix .remark name="Matrix tricks"}

- *Rotate a square matrix $90^\circ$ clockwise* in place: transpose it, then reverse each row. Entry $(r,c)$ goes to $(c,r)$ and then to $(c,n+1-r)$, which is where a clockwise turn sends it.
- *Spiral order*: keep the bounds top, bottom, left, right; read the top row, the right column, the bottom row reversed and the left column upwards, shrinking each bound after its side is read, until the bounds cross.
- *Zero the rows and columns of every $0$* in $O(1)$ extra space: record in two flags whether row $1$ and column $1$ contain a $0$, then use row $1$ and column $1$ as the marks for the other columns and rows, and zero row $1$ and column $1$ last.

:::

::: {#prp-staircase-search .proposition name="Search in a sorted matrix"}

If every row and every column of an $m\times n$ matrix $M$ is sorted increasingly, then a value $t$ can be found in $O(m+n)$ time: start at the top-right entry; if it equals $t$, stop; if it is greater, move left; if it is smaller, move down.

:::

::: {.proof}

1. *Invariant.* If $t$ occurs, it occurs in the submatrix of rows $r..m$ and columns $1..c$, where $(r,c)$ is the current position. This holds at the start.

2. If $M[r,c]>t$, every entry of column $c$ below it is larger still, so column $c$ can be dropped. If $M[r,c]<t$, every entry of row $r$ to its left is smaller, so row $r$ can be dropped.

3. Each move drops a row or a column, so there are at most $m+n$ moves.

:::

::: {#fig-array-techniques-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.6cm,y=0.6cm]
\foreach \row [count=\r] in {{1,4,7,11},{2,5,8,12},{3,6,9,16},{10,13,14,17}} {
  \foreach \v [count=\c] in \row { \draw[cell frame] (\c-1,4-\r) rectangle (\c,5-\r); \node[lab,tick] at (\c-0.5,4.5-\r) {$\v$}; }
}
\draw[->,hl] (3.5,3.5) -- (1.5,3.5) -- (1.5,1.5);
\end{tikzpicture}
\end{center}
```

Searching for $6$ from the top-right corner: $11>6$ and $7>6$ move left, $4<6$ and $5<6$ move down, and then $6$ is found.

:::
