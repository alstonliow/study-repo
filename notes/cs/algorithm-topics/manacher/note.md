---
title: "Manacher's Algorithm"
sources: []
requires: [cs/algorithm-design/amortized-analysis]
status: draft
---

<!-- Added 2026-11-26 for the CSES string problems, in our own wording. TODO: add a source. -->

A string has up to $\Theta(n^2)$ palindromic substrings, but all of them can be described by $2n-1$ numbers computed in $O(n)$ time.

::: {#def-palindromic-radius .definition name="Palindromic radii"}

For a string $s_0\dots s_{n-1}$ let $d_1(i)$ be the largest $r\ge1$ such that $s_{i-r+1..i+r-1}$ is a palindrome (odd length $2r-1$, centre $i$), and $d_2(i)$ the largest $r\ge0$ such that $s_{i-r..i+r-1}$ is a palindrome (even length $2r$, centre between $i-1$ and $i$).

:::

::: {#thm-manacher .theorem name="Manacher's algorithm"}

All $d_1(i)$ and $d_2(i)$ can be computed in $O(n)$ time. The procedure for $d_1$ keeps the palindrome $[l,r]$ found so far that has the rightmost right end. For $i\le r$ it starts with $d_1(i)=\min(d_1(l+r-i),\,r-i+1)$, then extends $d_1(i)$ by comparing characters, and updates $[l,r]$ if the new palindrome ends further right. For $i>r$ it starts with $1$. ($d_2$ is computed in the same way.)

:::

::: {.proof}

1. *The starting value is valid.* If $i\le r$, the mirror $j=l+r-i$ of $i$ in $[l,r]$ has a palindrome of radius $d_1(j)$ around it. Inside $[l,r]$ reflection preserves characters, so the same radius works around $i$ as long as it stays inside $[l,r]$, which gives $\min(d_1(j),r-i+1)$ as a lower bound.

2. *Extending finds the true value.* The loop compares the next pair of characters outside the known radius and stops at the first mismatch, so the final value is exactly $d_1(i)$.

3. *Time.* Each successful comparison reaches a position beyond the current $r$ (if the start was $r-i+1$) or no comparison is successful and the loop stops at once (if the start was $d_1(j)<r-i+1$, the palindrome at $j$ is maximal, hence also at $i$). Thus every successful comparison pushes $r$ to the right, and $r\le n$, so the total number of comparisons is $O(n)$.

:::

::: {#exm-manacher-1 .example name="abacaba"}

For $s=\text{abacaba}$ the odd radii are $d_1=(1,2,1,4,1,2,1)$, so the longest palindrome is the whole string, centred at index $3$ with length $2\cdot4-1=7$. The number of palindromic substrings is $\sum d_1(i)+\sum d_2(i)=12+0=12$.

:::

::: {#fig-manacher-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \c [count=\i from 0] in {a,b,a,c,a,b,a} {
  \draw[cell frame] (0.7*\i,0) rectangle +(0.7,0.7); \node[lab] at (0.7*\i+0.35,0.35) {\c};
  \node[lab,tick] at (0.7*\i+0.35,-0.4) {\i};
}
\draw[hl cell] (2.1,0) rectangle +(0.7,0.7);
\draw[<->,hl] (0,1.0) -- (4.9,1.0);
\node[lab,tick] at (2.45,1.4) {radius $d_1(3)=4$};
\end{tikzpicture}
\end{center}
```

@exm-manacher-1: the centre $3$ of abacaba and the palindrome of radius $4$ around it.

:::

::: {#rmk-manacher-1 .remark name="Uses"}

The longest palindromic substring is the maximum of $2d_1(i)-1$ and $2d_2(i)$. For "all palindromes" tasks, the longest palindrome starting at each position is obtained from the radii by a sweep: each centre $i$ with radius $r$ covers the start positions $i-r+1..i$. The radii also answer "is $s[l..r]$ a palindrome?" in $O(1)$ time by checking the radius at the midpoint.

:::
