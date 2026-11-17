---
title: "Randomized Algorithms: Verification, Quicksort and Selection"
sources: [mit6046-6, mit6046r-4]
requires: [cs/algorithm-design/divide-and-conquer]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 6 and Recitation 4, in our own wording; proofs written out in steps. -->

A *randomized algorithm* uses random numbers to make decisions, so on the same input different runs may behave differently. A *Monte Carlo* algorithm always runs fast and is *probably* correct; a *Las Vegas* algorithm is always correct and *probably* fast (its running time is a random variable whose expectation we bound). The probabilities are over the algorithm's own coins, for every input; no assumption about the inputs is made.

## Checking a matrix product

::: {#thm-freivalds .theorem name="Freivalds' check"}

Given $n\times n$ matrices $A,B,C$ (over the integers, or any field), choose a vector $r\in\{0,1\}^n$ uniformly at random and answer "yes" if $A(Br)=Cr$. This takes $O(n^2)$ time. If $AB=C$ the answer is always "yes"; if $AB\ne C$ it is "yes" with probability at most $\frac12$.

:::

::: {.proof}

1. Computing $Br$, then $A(Br)$, then $Cr$ takes three matrix–vector products, $O(n^2)$.

2. If $AB=C$ then $A(Br)=(AB)r=Cr$.

3. Otherwise $D=AB-C\ne0$; pick an entry $d_{ij}\ne0$. The answer is "yes" only if $(Dr)_i=\sum_kd_{ik}r_k=0$, that is $r_j=-\frac1{d_{ij}}\sum_{k\ne j}d_{ik}r_k$.

4. Fix the other coordinates of $r$. At most one of the two values of $r_j$ satisfies this, so the probability of "yes" is at most $\frac12$.

:::

Repeating with $k$ independent vectors makes the error probability at most $2^{-k}$, still in $O(kn^2)$ time, much faster than multiplying $A$ and $B$.

## Randomized quicksort

::: {#def-quicksort .definition name="Quicksort"}

*Quicksort* of an array of distinct items: if it has at most one item, stop. Otherwise choose a *pivot* $x$, partition the other items into $L=\{y<x\}$ and $G=\{y>x\}$ in $O(n)$ time, and sort $L$ and $G$ recursively. In *randomized quicksort* the pivot is chosen uniformly at random among the current items.

:::

::: {#fig-randomized-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (q0) at (5.50,0.00) {6 2 9 \textbf{4} 7 1 8 3 5};
\node[box] (q1) at (2.75,-0.95) {\textbf{2} 1 3};
\node[box] (q2) at (1.38,-1.90) {1};
\draw (q1) -- (q2);
\node[box] (q3) at (4.12,-1.90) {3};
\draw (q1) -- (q3);
\draw (q0) -- (q1);
\node[box] (q4) at (8.25,-0.95) {6 9 \textbf{7} 8 5};
\node[box] (q5) at (6.88,-1.90) {\textbf{6} 5};
\node[box] (q6) at (6.19,-2.85) {5};
\draw (q5) -- (q6);
\draw (q4) -- (q5);
\node[box] (q7) at (9.62,-1.90) {9 \textbf{8}};
\node[box] (q8) at (10.31,-2.85) {9};
\draw (q7) -- (q8);
\draw (q4) -- (q7);
\draw (q0) -- (q4);
\end{tikzpicture}
\end{center}
```

One run of randomized quicksort on $6,2,9,4,7,1,8,3,5$; the pivot of each call is in bold. Two items are compared only if one of them is a pivot while both are in the same call: $1$ and $9$ are never compared, because the pivot $4$ separates them first.

:::

With a fixed pivot rule (such as the first item), a sorted input gives $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$. Choosing the median as pivot (@thm-median-of-medians) gives $\Theta(n\log n)$ in the worst case but with large constants. A random pivot is simple and fast in expectation, for every input.

::: {#thm-randomized-quicksort .theorem name="Randomized quicksort"}

Randomized quicksort makes at most $2n\ln n$ comparisons in expectation on any input of $n$ distinct items. So it runs in $O(n\log n)$ expected time.

:::

::: {.proof}

1. Let $z_1<\dots<z_n$ be the items in sorted order and $X_{ij}$ the indicator that $z_i$ and $z_j$ are ever compared ($i<j$). Two items are compared only when one of them is the pivot, and never again afterwards, so the number of comparisons is $X=\sum_{i<j}X_{ij}$.

2. Consider the items $Z_{ij}=\{z_i,\dots,z_j\}$. They stay together in one subarray until the first time a pivot is chosen from $Z_{ij}$. If that pivot is $z_i$ or $z_j$, they are compared; if it is strictly between, they are separated and never compared.

3. Each item of $Z_{ij}$ is equally likely to be that first pivot, so $\Pr(X_{ij}=1)=\frac2{j-i+1}$.

4. By linearity (@thm-linearity-of-expectation),
   $$E[X]=\sum_{i<j}\frac2{j-i+1}\le\sum_{i=1}^n\sum_{k=2}^{n}\frac2k<2nH_n\le2n(1+\ln n),$$
   using @cor-harmonic-bounds. (A slightly more careful count gives at most $2n\ln n$.)

:::

## Randomized selection

::: {#def-randomized-select .definition name="Randomized select"}

`rselect(S, i)`: choose a random pivot $x$, partition into $L$ and $G$, let $k=|L|+1$; return $x$ if $i=k$, `rselect(L, i)` if $i<k$, and `rselect(G, i-k)` otherwise.

:::

::: {#thm-randomized-select .theorem name="Randomized select is linear in expectation"}

`rselect` runs in $O(n)$ expected time.

:::

::: {.proof}

1. Call the pivot *good* if both $L$ and $G$ have at most $\frac34$ of the items; at least half of the items are good pivots (all ranks in the middle half), so a pivot is good with probability at least $\frac12$.

2. Group the recursive calls into *phases*: phase $j$ consists of the calls made while the current size is in $\bigl((\frac34)^{j+1}n,(\frac34)^jn\bigr]$. A phase ends at the latest after its first good pivot, so the expected number of calls in a phase is at most $2$ (a geometric random variable), each costing $O((\frac34)^jn)$.

3. The expected total is $O\bigl(\sum_j2(\frac34)^jn\bigr)=O(n)$.

:::
