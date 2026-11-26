---
title: "Sliding Window"
sources: []
requires: [cs/algorithm-patterns/two-pointers, cs/data-structures/hashing]
status: draft
---

<!-- Added 2026-11-26 in our own words (owner decision 2026-11-26: new notes for the LeetCode Hot 100 problems without a fitting note). No single source; TODO: add a source if one is integrated later. The examples and figures are our own. -->

A *sliding window* is a two-pointer scan in which both pointers move right and the elements between them, the window $A[\ell..r]$, are summarised by a small state (a count, a sum, a table of character counts) that is updated in $O(1)$ when an element enters or leaves.

## Variable-width windows

The method applies when the property we test is *monotone* in the window.

::: {#def-sliding-window-monotone .definition name="Monotone window property"}

A property $\mathcal P$ of contiguous windows is *closed under shrinking* if whenever $A[\ell..r]$ has $\mathcal P$, so does every window $A[\ell'..r']$ with $\ell\le\ell'$ and $r'\le r$.

:::

::: {#thm-sliding-window .theorem name="Longest good window"}

Let $\mathcal P$ be closed under shrinking and suppose the state supports adding $A[r]$, removing $A[\ell]$ and testing $\mathcal P$ in $O(1)$ time. For $r=1,\dots,n$: add $A[r]$, then remove $A[\ell]$ and increase $\ell$ while the window fails $\mathcal P$, and record the length $r-\ell+1$. The largest recorded length is the length of the longest window with $\mathcal P$, and the scan takes $O(n)$ time.

:::

::: {.proof}

1. *Each $\ell$ is the best start for its $r$.* By induction on $r$: after step $r$, $\ell$ is the smallest index such that $A[\ell..r]$ has $\mathcal P$ (or $r+1$ if none). Suppose this holds for $r-1$ with value $\ell_0$. Any $\ell'<\ell_0$ fails at $r-1$, so by closure it fails at $r$ too. Hence the smallest good start for $r$ is at least $\ell_0$, and the `while` loop increases $\ell$ from $\ell_0$ exactly until the window is good.

2. So for each $r$ the recorded window is the longest good window ending at $r$, and the maximum over $r$ is the overall answer.

3. *Time.* $\ell$ and $r$ each increase at most $n$ times, and every step costs $O(1)$.

:::

::: {#exm-sliding-window-distinct .example name="Longest substring without repeated characters"}

"All characters distinct" is closed under shrinking. Keep a table $c$ of counts of the characters in the window: adding $a$ increments $c[a]$, and the window fails exactly when the character just added has $c[a]=2$. For $s=abcabcbb$ the longest such window is $abc$, of length $3$.

:::

::: {#fig-sliding-window-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.65cm,y=0.65cm]
\foreach \c [count=\i] in {a,b,c,a,b,c,b,b} { \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$}; }
\draw[hl] (1,-0.1) rectangle (4,1.1);
\node[lab,tick] at (1.5,-0.5) {$\ell$}; \node[lab,tick] at (3.5,-0.5) {$r$};
\node[lab,note,anchor=west] at (8.4,0.5) {window $bca$ after removing the first $a$};
\end{tikzpicture}
\end{center}
```

At $r=4$ the character $a$ enters a second time, so $\ell$ moves past the first $a$. The window never moves left, so each character enters and leaves once.

:::

The same scan finds the *shortest* window that has a property closed under *growing* (if $A[\ell..r]$ has it, so does every window containing it): for each $r$, while the window still has the property, record it and shrink from the left.

::: {#exm-sliding-window-cover .example name="Minimum window containing a multiset"}

To find the shortest substring of $s$ that contains every character of $t$ with multiplicity, keep a table $\mathit{need}[a]$ (count in $t$ minus count in the window) and the number $m$ of characters $a$ with $\mathit{need}[a]>0$. Adding or removing a character changes one entry of $\mathit{need}$ and possibly $m$, in $O(1)$. The window covers $t$ exactly when $m=0$, a property closed under growing. The total time is $O(|s|+|t|)$.

:::

## Fixed-width windows

When the window width $k$ is fixed, both pointers move together: add $A[r]$ and remove $A[r-k]$ at each step.

::: {#exm-sliding-window-anagram .example name="All anagram positions"}

To find every start of a substring of $s$ that is a permutation of $p$, slide a window of width $|p|$ and compare its character counts with those of $p$. Keeping the number of characters whose two counts differ makes each comparison $O(1)$, so the scan takes $O(|s|+|p|)$ time. For $s=cbaebabacd$ and $p=abc$, the starts are $1$ ($cba$) and $7$ ($bac$).

:::

::: {#fig-sliding-window-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.65cm,y=0.65cm]
\foreach \c [count=\i] in {c,b,a,e,b,a,b,a,c,d} { \draw[cell frame] (\i-1,0) rectangle (\i,1); \node[lab] at (\i-0.5,0.5) {$\c$}; }
\draw[hl] (0,-0.1) rectangle (3,1.1);
\draw[hl] (6,-0.1) rectangle (9,1.1);
\node[lab,tick] at (0.5,-0.5) {1}; \node[lab,tick] at (6.5,-0.5) {7};
\end{tikzpicture}
\end{center}
```

The windows of width $3$ in $cbaebabacd$ whose character counts equal those of $abc$.

:::

The maximum of every fixed-width window is not a counting state; it needs the monotonic queue (@prp-monotonic-queue).
