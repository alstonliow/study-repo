---
title: "Longest Palindromic Subsequence"
sources: [mit6046-10]
requires: [cs/algorithm-design/interval-subproblems, cs/algorithm-design/lcs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 10, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/interval-subproblems on 2026-11-25 (one problem per note, SPEC §8.6). -->

Substring subproblems that shrink from both ends.

::: {#exm-longest-palindromic-subsequence .example name="Longest palindromic subsequence"}

A *palindrome* reads the same forwards and backwards. Given a string $X=x_1\cdots x_n$, find a longest subsequence of $X$ that is a palindrome. For `CHARACTER` the answer has length $5$, for example `CARAC`.

1. *Subproblems:* $L(i,j)$, the length of a longest palindromic subsequence of $x_i\cdots x_j$, for $1\le i\le j\le n$.
2. *Relation:* if $x_i=x_j$ (and $i<j$), use both ends: $L(i,j)=2+L(i+1,j-1)$; otherwise one end is unused: $L(i,j)=\max\{L(i+1,j),L(i,j-1)\}$.
3. *Order:* increasing $j-i$.
4. *Base:* $L(i,i)=1$, and $L(i,i-1)=0$ for the empty string.
5. *Original:* $L(1,n)$; parent pointers give the palindrome.
6. *Time:* $O(n^2)$ subproblems with $O(1)$ work: $O(n^2)$.

The relation is right by the same exchange argument as for LCS (@lem-lcs-relation): if the two ends are equal, some longest palindrome uses them as its outer letters.

:::

```{=latex}
\begin{algorithm}
\caption{Longest palindromic subsequence}
\begin{algorithmic}
\INPUT A string $X=x_1\cdots x_n$
\OUTPUT The length $L(1,n)$ of a longest palindromic subsequence
\FOR{$i=1$ to $n$}
    \STATE $L(i,i)\gets1$; $L(i,i-1)\gets0$
\ENDFOR
\FOR{$\ell=1$ to $n-1$}
    \FOR{$i=1$ to $n-\ell$}
        \STATE $j\gets i+\ell$
        \IF{$x_i=x_j$}
            \STATE $L(i,j)\gets2+L(i+1,j-1)$
        \ELSE
            \STATE $L(i,j)\gets\max\{L(i+1,j),\,L(i,j-1)\}$
        \ENDIF
    \ENDFOR
\ENDFOR
\RETURN $L(1,n)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-interval-subproblems-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$1$};
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\node[lab] at (1.375,0.275) {$1$};
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\node[lab] at (1.925,0.275) {$1$};
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$3$};
\draw[hl cell] (2.750,0.000) rectangle (3.300,0.550);
\node[lab] at (3.025,0.275) {$5$};
\draw[hl cell] (3.300,0.000) rectangle (3.850,0.550);
\node[lab] at (3.575,0.275) {$5$};
\draw[hl cell] (3.850,0.000) rectangle (4.400,0.550);
\node[lab] at (4.125,0.275) {$5$};
\draw[hl cell] (4.400,0.000) rectangle (4.950,0.550);
\node[lab] at (4.675,0.275) {$5$};
\node[lab,tick,anchor=east] at (-0.050,0.275) {\texttt{C}};
\draw[cell frame] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$1$};
\draw[cell frame] (1.100,-0.550) rectangle (1.650,0.000);
\node[lab] at (1.375,-0.275) {$1$};
\draw[cell frame] (1.650,-0.550) rectangle (2.200,0.000);
\node[lab] at (1.925,-0.275) {$1$};
\draw[hl cell] (2.200,-0.550) rectangle (2.750,0.000);
\node[lab] at (2.475,-0.275) {$3$};
\draw[cell frame] (2.750,-0.550) rectangle (3.300,0.000);
\node[lab] at (3.025,-0.275) {$3$};
\draw[cell frame] (3.300,-0.550) rectangle (3.850,0.000);
\node[lab] at (3.575,-0.275) {$3$};
\draw[cell frame] (3.850,-0.550) rectangle (4.400,0.000);
\node[lab] at (4.125,-0.275) {$3$};
\draw[cell frame] (4.400,-0.550) rectangle (4.950,0.000);
\node[lab] at (4.675,-0.275) {$3$};
\node[lab,tick,anchor=east] at (-0.050,-0.275) {\texttt{H}};
\draw[cell frame] (1.100,-1.100) rectangle (1.650,-0.550);
\node[lab] at (1.375,-0.825) {$1$};
\draw[cell frame] (1.650,-1.100) rectangle (2.200,-0.550);
\node[lab] at (1.925,-0.825) {$1$};
\draw[hl cell] (2.200,-1.100) rectangle (2.750,-0.550);
\node[lab] at (2.475,-0.825) {$3$};
\draw[cell frame] (2.750,-1.100) rectangle (3.300,-0.550);
\node[lab] at (3.025,-0.825) {$3$};
\draw[cell frame] (3.300,-1.100) rectangle (3.850,-0.550);
\node[lab] at (3.575,-0.825) {$3$};
\draw[cell frame] (3.850,-1.100) rectangle (4.400,-0.550);
\node[lab] at (4.125,-0.825) {$3$};
\draw[cell frame] (4.400,-1.100) rectangle (4.950,-0.550);
\node[lab] at (4.675,-0.825) {$3$};
\node[lab,tick,anchor=east] at (-0.050,-0.825) {\texttt{A}};
\draw[hl cell] (1.650,-1.650) rectangle (2.200,-1.100);
\node[lab] at (1.925,-1.375) {$1$};
\draw[cell frame] (2.200,-1.650) rectangle (2.750,-1.100);
\node[lab] at (2.475,-1.375) {$1$};
\draw[cell frame] (2.750,-1.650) rectangle (3.300,-1.100);
\node[lab] at (3.025,-1.375) {$1$};
\draw[cell frame] (3.300,-1.650) rectangle (3.850,-1.100);
\node[lab] at (3.575,-1.375) {$1$};
\draw[cell frame] (3.850,-1.650) rectangle (4.400,-1.100);
\node[lab] at (4.125,-1.375) {$1$};
\draw[cell frame] (4.400,-1.650) rectangle (4.950,-1.100);
\node[lab] at (4.675,-1.375) {$3$};
\node[lab,tick,anchor=east] at (-0.050,-1.375) {\texttt{R}};
\draw[cell frame] (2.200,-2.200) rectangle (2.750,-1.650);
\node[lab] at (2.475,-1.925) {$1$};
\draw[cell frame] (2.750,-2.200) rectangle (3.300,-1.650);
\node[lab] at (3.025,-1.925) {$1$};
\draw[cell frame] (3.300,-2.200) rectangle (3.850,-1.650);
\node[lab] at (3.575,-1.925) {$1$};
\draw[cell frame] (3.850,-2.200) rectangle (4.400,-1.650);
\node[lab] at (4.125,-1.925) {$1$};
\draw[cell frame] (4.400,-2.200) rectangle (4.950,-1.650);
\node[lab] at (4.675,-1.925) {$1$};
\node[lab,tick,anchor=east] at (-0.050,-1.925) {\texttt{A}};
\draw[cell frame] (2.750,-2.750) rectangle (3.300,-2.200);
\node[lab] at (3.025,-2.475) {$1$};
\draw[cell frame] (3.300,-2.750) rectangle (3.850,-2.200);
\node[lab] at (3.575,-2.475) {$1$};
\draw[cell frame] (3.850,-2.750) rectangle (4.400,-2.200);
\node[lab] at (4.125,-2.475) {$1$};
\draw[cell frame] (4.400,-2.750) rectangle (4.950,-2.200);
\node[lab] at (4.675,-2.475) {$1$};
\node[lab,tick,anchor=east] at (-0.050,-2.475) {\texttt{C}};
\draw[cell frame] (3.300,-3.300) rectangle (3.850,-2.750);
\node[lab] at (3.575,-3.025) {$1$};
\draw[cell frame] (3.850,-3.300) rectangle (4.400,-2.750);
\node[lab] at (4.125,-3.025) {$1$};
\draw[cell frame] (4.400,-3.300) rectangle (4.950,-2.750);
\node[lab] at (4.675,-3.025) {$1$};
\node[lab,tick,anchor=east] at (-0.050,-3.025) {\texttt{T}};
\draw[cell frame] (3.850,-3.850) rectangle (4.400,-3.300);
\node[lab] at (4.125,-3.575) {$1$};
\draw[cell frame] (4.400,-3.850) rectangle (4.950,-3.300);
\node[lab] at (4.675,-3.575) {$1$};
\node[lab,tick,anchor=east] at (-0.050,-3.575) {\texttt{E}};
\draw[cell frame] (4.400,-4.400) rectangle (4.950,-3.850);
\node[lab] at (4.675,-4.125) {$1$};
\node[lab,tick,anchor=east] at (-0.050,-4.125) {\texttt{R}};
\node[lab,tick] at (0.275,0.730) {\texttt{C}};
\node[lab,tick] at (0.825,0.730) {\texttt{H}};
\node[lab,tick] at (1.375,0.730) {\texttt{A}};
\node[lab,tick] at (1.925,0.730) {\texttt{R}};
\node[lab,tick] at (2.475,0.730) {\texttt{A}};
\node[lab,tick] at (3.025,0.730) {\texttt{C}};
\node[lab,tick] at (3.575,0.730) {\texttt{T}};
\node[lab,tick] at (4.125,0.730) {\texttt{E}};
\node[lab,tick] at (4.675,0.730) {\texttt{R}};
\end{tikzpicture}
\end{center}
```

The table $L(i,j)$ for \texttt{CHARACTER} (row $i$, column $j$, $i\le j$), filled by increasing $j-i$ from the diagonal of $1$s. The answer is $L(1,9)=5$. The highlighted cells trace one palindrome from the top right corner: equal end letters (C and C, then A and A) become its outer letters, otherwise the step goes to a larger neighbour. This gives \texttt{CARAC}.

:::
