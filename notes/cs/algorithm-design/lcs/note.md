---
title: "Longest Common Subsequence"
sources: [mit6006-16, mit6006r-16]
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 16 and Recitation 16, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/subproblem-design on 2026-11-25 (one problem per note, SPEC §8.6). -->

Two sequences give subproblems that are pairs of suffixes, one of each.

A *subsequence* of a string keeps some of its characters in order, not necessarily next to each other.

::: {#exm-lcs .example name="Longest common subsequence"}

Given strings $A$ and $B$, find a longest string that is a subsequence of both. For example, ALGORITHM and LOGARITHM have the common subsequence LORITHM of length $7$, and none longer.

1. *Subproblems:* $x(i,j)$, the length of a longest common subsequence of the suffixes $A[i:]$ and $B[j:]$, for $0\le i\le|A|$, $0\le j\le|B|$.
2. *Relation:*
   $$x(i,j)=\begin{cases}1+x(i+1,j+1)&\text{if }A[i]=B[j],\\\max\{x(i+1,j),\,x(i,j+1)\}&\text{otherwise.}\end{cases}$$
3. *Order:* decreasing $i+j$ (or: decreasing $i$, and for each $i$ decreasing $j$).
4. *Base:* $x(|A|,j)=x(i,|B|)=0$.
5. *Original:* $x(0,0)$; storing which case gave each value (parent pointers) recovers the subsequence.
6. *Time:* $(|A|+1)(|B|+1)$ subproblems with $O(1)$ work: $O(|A|\cdot|B|)$.

:::

```{=latex}
\begin{algorithm}
\caption{Longest common subsequence}
\begin{algorithmic}
\INPUT Strings $A$ and $B$
\OUTPUT A longest common subsequence $S$
\STATE $x(|A|,j)\gets0$ for all $j$; $x(i,|B|)\gets0$ for all $i$
\FOR{$i=|A|-1$ down to $0$}
    \FOR{$j=|B|-1$ down to $0$}
        \IF{$A[i]=B[j]$}
            \STATE $x(i,j)\gets1+x(i+1,j+1)$
        \ELSE
            \STATE $x(i,j)\gets\max\{x(i+1,j),\,x(i,j+1)\}$
        \ENDIF
    \ENDFOR
\ENDFOR
\STATE $S\gets$ empty; $i\gets0$; $j\gets0$
\WHILE{$i<|A|$ and $j<|B|$}
    \IF{$A[i]=B[j]$}
        \STATE append $A[i]$ to $S$; $i\gets i+1$; $j\gets j+1$
    \ELSIF{$x(i+1,j)\ge x(i,j+1)$}
        \STATE $i\gets i+1$
    \ELSE
        \STATE $j\gets j+1$
    \ENDIF
\ENDWHILE
\RETURN $S$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-subproblem-design-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab] at (0.30,0.35) {\texttt{S}};
\node[lab] at (0.90,0.35) {\texttt{U}};
\node[lab] at (1.50,0.35) {\texttt{N}};
\node[lab] at (2.10,0.35) {\texttt{N}};
\node[lab] at (2.70,0.35) {\texttt{Y}};
\node[lab] at (3.30,0.35) {\texttt{}};
\node[lab] at (-0.30,-0.30) {\texttt{S}};
\draw[hl cell] (0.00,0.00) rectangle (0.60,-0.60);
\node[lab] at (0.30,-0.30) {\textbf{3}};
\draw[cell frame] (0.60,0.00) rectangle (1.20,-0.60);
\node[lab] at (0.90,-0.30) {2};
\draw[cell frame] (1.20,0.00) rectangle (1.80,-0.60);
\node[lab] at (1.50,-0.30) {2};
\draw[cell frame] (1.80,0.00) rectangle (2.40,-0.60);
\node[lab] at (2.10,-0.30) {2};
\draw[cell frame] (2.40,0.00) rectangle (3.00,-0.60);
\node[lab] at (2.70,-0.30) {1};
\draw[cell frame] (3.00,0.00) rectangle (3.60,-0.60);
\node[lab] at (3.30,-0.30) {0};
\node[lab] at (-0.30,-0.90) {\texttt{N}};
\draw[cell frame] (0.00,-0.60) rectangle (0.60,-1.20);
\node[lab] at (0.30,-0.90) {2};
\draw[hl cell] (0.60,-0.60) rectangle (1.20,-1.20);
\node[lab] at (0.90,-0.90) {2};
\draw[hl cell] (1.20,-0.60) rectangle (1.80,-1.20);
\node[lab] at (1.50,-0.90) {\textbf{2}};
\draw[cell frame] (1.80,-0.60) rectangle (2.40,-1.20);
\node[lab] at (2.10,-0.90) {2};
\draw[cell frame] (2.40,-0.60) rectangle (3.00,-1.20);
\node[lab] at (2.70,-0.90) {1};
\draw[cell frame] (3.00,-0.60) rectangle (3.60,-1.20);
\node[lab] at (3.30,-0.90) {0};
\node[lab] at (-0.30,-1.50) {\texttt{O}};
\draw[cell frame] (0.00,-1.20) rectangle (0.60,-1.80);
\node[lab] at (0.30,-1.50) {1};
\draw[cell frame] (0.60,-1.20) rectangle (1.20,-1.80);
\node[lab] at (0.90,-1.50) {1};
\draw[cell frame] (1.20,-1.20) rectangle (1.80,-1.80);
\node[lab] at (1.50,-1.50) {1};
\draw[hl cell] (1.80,-1.20) rectangle (2.40,-1.80);
\node[lab] at (2.10,-1.50) {1};
\draw[cell frame] (2.40,-1.20) rectangle (3.00,-1.80);
\node[lab] at (2.70,-1.50) {1};
\draw[cell frame] (3.00,-1.20) rectangle (3.60,-1.80);
\node[lab] at (3.30,-1.50) {0};
\node[lab] at (-0.30,-2.10) {\texttt{W}};
\draw[cell frame] (0.00,-1.80) rectangle (0.60,-2.40);
\node[lab] at (0.30,-2.10) {1};
\draw[cell frame] (0.60,-1.80) rectangle (1.20,-2.40);
\node[lab] at (0.90,-2.10) {1};
\draw[cell frame] (1.20,-1.80) rectangle (1.80,-2.40);
\node[lab] at (1.50,-2.10) {1};
\draw[hl cell] (1.80,-1.80) rectangle (2.40,-2.40);
\node[lab] at (2.10,-2.10) {1};
\draw[cell frame] (2.40,-1.80) rectangle (3.00,-2.40);
\node[lab] at (2.70,-2.10) {1};
\draw[cell frame] (3.00,-1.80) rectangle (3.60,-2.40);
\node[lab] at (3.30,-2.10) {0};
\node[lab] at (-0.30,-2.70) {\texttt{Y}};
\draw[cell frame] (0.00,-2.40) rectangle (0.60,-3.00);
\node[lab] at (0.30,-2.70) {1};
\draw[cell frame] (0.60,-2.40) rectangle (1.20,-3.00);
\node[lab] at (0.90,-2.70) {1};
\draw[cell frame] (1.20,-2.40) rectangle (1.80,-3.00);
\node[lab] at (1.50,-2.70) {1};
\draw[hl cell] (1.80,-2.40) rectangle (2.40,-3.00);
\node[lab] at (2.10,-2.70) {1};
\draw[hl cell] (2.40,-2.40) rectangle (3.00,-3.00);
\node[lab] at (2.70,-2.70) {\textbf{1}};
\draw[cell frame] (3.00,-2.40) rectangle (3.60,-3.00);
\node[lab] at (3.30,-2.70) {0};
\node[lab] at (-0.30,-3.30) {\texttt{}};
\draw[cell frame] (0.00,-3.00) rectangle (0.60,-3.60);
\node[lab] at (0.30,-3.30) {0};
\draw[cell frame] (0.60,-3.00) rectangle (1.20,-3.60);
\node[lab] at (0.90,-3.30) {0};
\draw[cell frame] (1.20,-3.00) rectangle (1.80,-3.60);
\node[lab] at (1.50,-3.30) {0};
\draw[cell frame] (1.80,-3.00) rectangle (2.40,-3.60);
\node[lab] at (2.10,-3.30) {0};
\draw[cell frame] (2.40,-3.00) rectangle (3.00,-3.60);
\node[lab] at (2.70,-3.30) {0};
\draw[hl cell] (3.00,-3.00) rectangle (3.60,-3.60);
\node[lab] at (3.30,-3.30) {0};
\end{tikzpicture}
\end{center}
```

The table $x(i,j)$ for $A=\texttt{SNOWY}$ (rows) and $B=\texttt{SUNNY}$ (columns); the last row and column are the base cases $0$. It is filled from the bottom right. The highlighted cells trace a path from $x(0,0)=3$: a diagonal step at each bold match, otherwise a step towards the larger neighbour. The matches spell the common subsequence \texttt{SNY}.

:::

::: {#lem-lcs-relation .lemma name="Why the LCS relation is right"}

Let $a=A[i]$ and $b=B[j]$ be the first characters of the two suffixes.

1. If $a=b$, some longest common subsequence of $A[i:]$ and $B[j:]$ starts with this pair matched to each other.
2. If $a\ne b$, every common subsequence either does not use $a$ or does not use $b$.

:::

::: {.proof}

1. Take a longest common subsequence $S$. If it uses neither $a$ nor $b$, putting the common character $a=b$ in front gives a longer one, a contradiction. If its first character comes from $a$ but is matched with a later $b'=a$ in $B[j:]$ (or symmetrically), matching it with $b$ instead still works, since $b$ comes before $b'$. So we can assume $S$ starts with $a$ matched to $b$, and the rest of $S$ is a common subsequence of $A[i+1:]$ and $B[j+1:]$; so $x(i,j)=1+x(i+1,j+1)$.

2. If both $a$ and $b$ were used, each would be the first character of the subsequence (nothing comes before them in their strings), so they would be matched to each other, which needs $a=b$. Hence the best is found in $A[i+1:],B[j:]$ or in $A[i:],B[j+1:]$.

:::
