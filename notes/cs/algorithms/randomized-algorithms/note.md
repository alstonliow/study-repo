---
title: "Randomized Algorithms: Verification, Quicksort and Selection"
sources: [mit6046-6, mit6046r-4]
requires: [cs/algorithms/divide-and-conquer]
aliases: [cs/algorithm-design/randomized-algorithms]   # old ids (moved)
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

```{=latex}
\begin{algorithm}
\caption{Freivalds' check}
\begin{algorithmic}
\INPUT $n\times n$ matrices $A,B,C$; a number $k$ of trials
\OUTPUT "yes" if probably $AB=C$, "no" if certainly $AB\ne C$
\FOR{$j=1$ to $k$}
    \STATE choose $r\in\{0,1\}^n$ uniformly at random
    \IF{$A(Br)\ne Cr$}
        \RETURN "no"
    \ENDIF
\ENDFOR
\RETURN "yes"
\end{algorithmic}
\end{algorithm}
```

::: {#fig-randomized-algorithms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$19$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$22$};
\draw[cell frame] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$43$};
\draw[hl cell] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$51$};
\node[lab,tick] at (0.55,0.85) {$C$ ($AB$ has $50$ here)};
\node[lab,tick] at (2.60,0.75) {$r$};
\node[lab,tick] at (3.90,0.75) {$A(Br)$};
\node[lab,tick] at (5.20,0.75) {$Cr$};
\node[lab,tick] at (6.50,0.75) {answer};
\draw[faint] (2.1,0.55) -- (7.1,0.55);
\node[lab,tick] at (2.60,0.30) {$(0,0)$};
\node[lab,tick] at (3.90,0.30) {$(0,0)$};
\node[lab,tick] at (5.20,0.30) {$(0,0)$};
\node[lab,tick] at (6.50,0.30) {yes};
\node[lab,tick] at (2.60,-0.12) {$(0,1)$};
\node[lab,tick] at (3.90,-0.12) {$(22,50)$};
\node[lab,tick] at (5.20,-0.12) {$(22,51)$};
\node[lab,tick] at (6.50,-0.12) {\textbf{no}};
\node[lab,tick] at (2.60,-0.54) {$(1,0)$};
\node[lab,tick] at (3.90,-0.54) {$(19,43)$};
\node[lab,tick] at (5.20,-0.54) {$(19,43)$};
\node[lab,tick] at (6.50,-0.54) {yes};
\node[lab,tick] at (2.60,-0.96) {$(1,1)$};
\node[lab,tick] at (3.90,-0.96) {$(41,93)$};
\node[lab,tick] at (5.20,-0.96) {$(41,94)$};
\node[lab,tick] at (6.50,-0.96) {\textbf{no}};
\end{tikzpicture}
\end{center}
```

Freivalds' check with the $A$ and $B$ of @fig-divide-and-conquer-3 and a wrong $C$ (one entry off by $1$). Of the four vectors $r\in\{0,1\}^2$, exactly the two with $r_2=1$ expose the error, so one trial answers ``no'' with probability $\frac12$, and $k$ trials miss the error with probability $2^{-k}$.

:::

Repeating with $k$ independent vectors makes the error probability at most $2^{-k}$, still in $O(kn^2)$ time, much faster than multiplying $A$ and $B$.

## Randomized quicksort

::: {#def-quicksort .definition name="Quicksort"}

*Quicksort* of an array of distinct items: if it has at most one item, stop. Otherwise choose a *pivot* $x$, partition the other items into $L=\{y<x\}$ and $G=\{y>x\}$ in $O(n)$ time, and sort $L$ and $G$ recursively. In *randomized quicksort* the pivot is chosen uniformly at random among the current items.

:::

```{=latex}
\begin{algorithm}
\caption{Randomized quicksort}
\begin{algorithmic}
\INPUT An array $S$ of distinct items
\OUTPUT $S$ sorted
\IF{$|S|\le1$}
    \RETURN $S$
\ENDIF
\STATE $x\gets$ an item of $S$ chosen uniformly at random
\STATE $L\gets\{y\in S:y<x\}$; $G\gets\{y\in S:y>x\}$
\RETURN quicksort$(L)$, then $x$, then quicksort$(G)$
\end{algorithmic}
\end{algorithm}
```

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

```{=latex}
\begin{algorithm}
\caption{rselect$(S,i)$}
\begin{algorithmic}
\INPUT A set $S$ of distinct numbers, a rank $1\le i\le|S|$
\OUTPUT The element of rank $i$ in $S$
\STATE $x\gets$ an element of $S$ chosen uniformly at random
\STATE $L\gets\{y\in S:y<x\}$; $G\gets\{y\in S:y>x\}$; $k\gets|L|+1$
\IF{$i=k$}
    \RETURN $x$
\ELSIF{$i<k$}
    \RETURN rselect$(L,i)$
\ENDIF
\RETURN rselect$(G,i-k)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-randomized-algorithms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$6$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$9$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$4$};
\draw[hl cell] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$7$};
\draw[cell frame] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$1$};
\draw[cell frame] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$8$};
\draw[cell frame] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$3$};
\draw[cell frame] (4.400,0.000) rectangle (4.950,0.550);
\node[lab] at (4.675,0.275) {$5$};
\node[lab,tick,anchor=west] at (5.25,0.28) {$i=5$, pivot $7$, $k=7$: recurse on $L$};
\draw[cell frame] (0.000,-0.900) rectangle (0.550,-0.350);
\node[lab] at (0.275,-0.625) {$6$};
\draw[hl cell] (0.550,-0.900) rectangle (1.100,-0.350);
\node[lab] at (0.825,-0.625) {$2$};
\draw[cell frame] (1.100,-0.900) rectangle (1.650,-0.350);
\node[lab] at (1.375,-0.625) {$4$};
\draw[cell frame] (1.650,-0.900) rectangle (2.200,-0.350);
\node[lab] at (1.925,-0.625) {$1$};
\draw[cell frame] (2.200,-0.900) rectangle (2.750,-0.350);
\node[lab] at (2.475,-0.625) {$3$};
\draw[cell frame] (2.750,-0.900) rectangle (3.300,-0.350);
\node[lab] at (3.025,-0.625) {$5$};
\node[lab,tick,anchor=west] at (5.25,-0.62) {$i=5$, pivot $2$, $k=2$: recurse on $G$ with $i=3$};
\draw[cell frame] (0.000,-1.800) rectangle (0.550,-1.250);
\node[lab] at (0.275,-1.525) {$6$};
\draw[cell frame] (0.550,-1.800) rectangle (1.100,-1.250);
\node[lab] at (0.825,-1.525) {$4$};
\draw[cell frame] (1.100,-1.800) rectangle (1.650,-1.250);
\node[lab] at (1.375,-1.525) {$3$};
\draw[hl cell] (1.650,-1.800) rectangle (2.200,-1.250);
\node[lab] at (1.925,-1.525) {$5$};
\node[lab,tick,anchor=west] at (5.25,-1.52) {$i=3$, pivot $5$, $k=3$: return $x$};
\end{tikzpicture}
\end{center}
```

One run of `rselect` for the median (rank $5$) of the items of @fig-randomized-algorithms-1, with random pivots $7$, $2$ and $5$ (highlighted). Each call partitions around the pivot and recurses into one side only; the third pivot has rank $k=i$ in its call, so the answer is $5$. Unlike quicksort, only one side is ever processed.

:::

::: {#thm-randomized-select .theorem name="Randomized select is linear in expectation"}

`rselect` runs in $O(n)$ expected time.

:::

::: {.proof}

1. Call the pivot *good* if both $L$ and $G$ have at most $\frac34$ of the items; at least half of the items are good pivots (all ranks in the middle half), so a pivot is good with probability at least $\frac12$.

2. Group the recursive calls into *phases*: phase $j$ consists of the calls made while the current size is in $\bigl((\frac34)^{j+1}n,(\frac34)^jn\bigr]$. A phase ends at the latest after its first good pivot, so the expected number of calls in a phase is at most $2$ (a geometric random variable), each costing $O((\frac34)^jn)$.

3. The expected total is $O\bigl(\sum_j2(\frac34)^jn\bigr)=O(n)$.

:::
