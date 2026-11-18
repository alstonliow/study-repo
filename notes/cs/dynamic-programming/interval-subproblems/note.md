---
title: "Dynamic Programming on Intervals"
sources: [mit6046-10, mit6046-1, mit6046r-1, mit6046r-5]
requires: [cs/dynamic-programming/pseudopolynomial-time]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lectures 1 and 10 and Recitations 1 and 5, in our own wording; examples our own (checked by computation); proofs written out in steps. The alternating coin game of Lecture 10 is @exm-coin-game. -->

Many problems on sequences use *substring* subproblems $x(i,j)$, one for each contiguous piece, and guess where the piece splits. There are $O(n^2)$ of them, so the running time is $O(n^2)$ times the work per subproblem.

::: {#exm-weighted-interval-scheduling .example name="Weighted interval scheduling"}

Requests $[s(i),f(i))$ have weights $w(i)$; choose compatible requests of largest total weight (the unweighted version is @def-interval-scheduling). Sort the requests by starting time, $s(1)\le\dots\le s(n)$, and let $\mathrm{next}(i)$ be the first request $j>i$ with $s(j)\ge f(i)$, found by binary search.

1. *Subproblems:* $x(i)$, the best total weight using only requests $i,\dots,n$ (a suffix).
2. *Relation:* request $i$ is not used, or it is used and then the next usable request is $\mathrm{next}(i)$: $x(i)=\max\{x(i+1),\ w(i)+x(\mathrm{next}(i))\}$.
3. *Order:* decreasing $i$. 4. *Base:* $x(n+1)=0$. 5. *Original:* $x(1)$.
6. *Time:* sorting and the binary searches take $O(n\log n)$, and the $n$ subproblems $O(1)$ each.

:::

```{=latex}
\begin{algorithm}
\caption{Weighted interval scheduling}
\begin{algorithmic}
\INPUT Requests $[s(i),f(i))$ with weights $w(i)$, $i=1,\dots,n$
\OUTPUT The largest total weight of compatible requests
\STATE sort the requests so that $s(1)\le\dots\le s(n)$
\FOR{$i=1$ to $n$}
    \STATE $\mathrm{next}(i)\gets$ the least $j>i$ with $s(j)\ge f(i)$, or $n+1$ \COMMENT{binary search}
\ENDFOR
\STATE $x(n+1)\gets0$
\FOR{$i=n$ down to $1$}
    \STATE $x(i)\gets\max\{x(i+1),\ w(i)+x(\mathrm{next}(i))\}$
\ENDFOR
\RETURN $x(1)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-interval-subproblems-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\begin{scope}[x=0.55cm,y=0.42cm]
\draw[hl box] (0,0) rectangle (6,-0.7);
\node[lab,tick] at (3.0,-0.35) {$5$};
\node[lab,tick] at (13.5,-0.35) {$1$};
\node[lab,tick] at (15,-0.35) {$7$};
\node[lab,tick] at (16.5,-0.35) {$8$};
\draw[box] (1,-1) rectangle (4,-1.7);
\node[lab,tick] at (2.5,-1.35) {$2$};
\node[lab,tick] at (13.5,-1.35) {$2$};
\node[lab,tick] at (15,-1.35) {$5$};
\node[lab,tick] at (16.5,-1.35) {$7$};
\draw[box] (3,-2) rectangle (5,-2.7);
\node[lab,tick] at (4.0,-2.35) {$3$};
\node[lab,tick] at (13.5,-2.35) {$3$};
\node[lab,tick] at (15,-2.35) {$6$};
\node[lab,tick] at (16.5,-2.35) {$7$};
\draw[box] (3,-3) rectangle (8,-3.7);
\node[lab,tick] at (5.5,-3.35) {$5$};
\node[lab,tick] at (13.5,-3.35) {$4$};
\node[lab,tick] at (15,-3.35) {$8$};
\node[lab,tick] at (16.5,-3.35) {$7$};
\draw[box] (4,-4) rectangle (7,-4.7);
\node[lab,tick] at (5.5,-4.35) {$3$};
\node[lab,tick] at (13.5,-4.35) {$5$};
\node[lab,tick] at (15,-4.35) {$8$};
\node[lab,tick] at (16.5,-4.35) {$5$};
\draw[box] (5,-5) rectangle (9,-5.7);
\node[lab,tick] at (7.0,-5.35) {$4$};
\node[lab,tick] at (13.5,-5.35) {$6$};
\node[lab,tick] at (15,-5.35) {$9$};
\node[lab,tick] at (16.5,-5.35) {$4$};
\draw[hl box] (6,-6) rectangle (10,-6.7);
\node[lab,tick] at (8.0,-6.35) {$3$};
\node[lab,tick] at (13.5,-6.35) {$7$};
\node[lab,tick] at (15,-6.35) {$9$};
\node[lab,tick] at (16.5,-6.35) {$3$};
\draw[box] (8,-7) rectangle (11,-7.7);
\node[lab,tick] at (9.5,-7.35) {$2$};
\node[lab,tick] at (13.5,-7.35) {$8$};
\node[lab,tick] at (15,-7.35) {$9$};
\node[lab,tick] at (16.5,-7.35) {$2$};
\node[lab,tick] at (13.5,1) {$i$};
\node[lab,tick] at (15,1) {$\mathrm{next}(i)$};
\node[lab,tick] at (16.5,1) {$x(i)$};
\draw[faint] (0,-8.3) -- (12,-8.3);
\foreach \t in {0,2,...,12} \node[lab,tick] at (\t,-8.8) {\t};
\end{scope}
\end{tikzpicture}
\end{center}
```

The eight requests of @fig-greedy-algorithms-1, sorted by start, now with weights (inside the bars). The table gives $\mathrm{next}(i)$ ($9$ means none) and $x(i)$, computed from the bottom up. The best total weight is $x(1)=8$, from the highlighted requests $[0,6), [6,10)$; the most requests, three, would weigh less.

:::

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

::: {#exm-optimal-bst .example name="Optimal binary search tree"}

Keys $k_1<\dots<k_n$ are searched with known weights (frequencies) $w_1,\dots,w_n$. A search for $k_r$ costs the number of nodes on the path to it, that is $\mathrm{depth}(k_r)+1$. Find a binary search tree minimising $\sum_rw_r(\mathrm{depth}(k_r)+1)$.

1. *Subproblems:* $e(i,j)$, the least cost of a search tree on $k_i,\dots,k_j$, for $1\le i\le j+1\le n+1$; let $W(i,j)=w_i+\dots+w_j$.
2. *Relation:* guess the root $k_r$. Every key of the subtree then lies one level deeper than in its own subtree, which adds $W(i,j)$:
   $$e(i,j)=W(i,j)+\min_{i\le r\le j}\bigl\{e(i,r-1)+e(r+1,j)\bigr\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $e(i,i-1)=0$ (an empty tree).
5. *Original:* $e(1,n)$, with the chosen roots recorded to build the tree.
6. *Time:* $O(n^2)$ subproblems, $O(n)$ work each with prefix sums for $W$: $O(n^3)$.

Greedily putting the most frequent key at the root is not optimal: with weights $10,8,9$ for keys $1,2,3$, that tree costs $10+2\cdot9+3\cdot8=52$, while the balanced tree with root $2$ costs $8+2\cdot(10+9)=46$.

:::

```{=latex}
\begin{algorithm}
\caption{Optimal binary search tree}
\begin{algorithmic}
\INPUT Weights $w_1,\dots,w_n$ of keys $k_1<\dots<k_n$
\OUTPUT The least cost $e(1,n)$ and the roots $R$ of an optimal tree
\FOR{$i=1$ to $n+1$}
    \STATE $e(i,i-1)\gets0$
\ENDFOR
\FOR{$\ell=0$ to $n-1$}
    \FOR{$i=1$ to $n-\ell$}
        \STATE $j\gets i+\ell$; $e(i,j)\gets\infty$
        \FOR{$r=i$ to $j$}
            \IF{$e(i,r-1)+e(r+1,j)<e(i,j)$}
                \STATE $e(i,j)\gets e(i,r-1)+e(r+1,j)$; $R(i,j)\gets r$
            \ENDIF
        \ENDFOR
        \STATE $e(i,j)\gets e(i,j)+W(i,j)$ \COMMENT{$W(i,j)=w_i+\dots+w_j$, from prefix sums}
    \ENDFOR
\ENDFOR
\RETURN $e(1,n)$, $R$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-interval-subproblems-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.950,0.950);
\node[lab] at (0.475,0.475) {$0$};
\draw[cell frame] (0.950,0.000) rectangle (1.900,0.950);
\node[lab] at (1.425,0.475) {$10\,/\,1$};
\draw[cell frame] (1.900,0.000) rectangle (2.850,0.950);
\node[lab] at (2.375,0.475) {$26\,/\,1$};
\draw[hl cell] (2.850,0.000) rectangle (3.800,0.950);
\node[lab] at (3.325,0.475) {$46\,/\,2$};
\node[lab,tick,anchor=east] at (-0.050,0.475) {$i=1$};
\draw[cell frame] (0.950,-0.950) rectangle (1.900,0.000);
\node[lab] at (1.425,-0.475) {$0$};
\draw[cell frame] (1.900,-0.950) rectangle (2.850,0.000);
\node[lab] at (2.375,-0.475) {$8\,/\,2$};
\draw[cell frame] (2.850,-0.950) rectangle (3.800,0.000);
\node[lab] at (3.325,-0.475) {$25\,/\,3$};
\node[lab,tick,anchor=east] at (-0.050,-0.475) {$i=2$};
\draw[cell frame] (1.900,-1.900) rectangle (2.850,-0.950);
\node[lab] at (2.375,-1.425) {$0$};
\draw[cell frame] (2.850,-1.900) rectangle (3.800,-0.950);
\node[lab] at (3.325,-1.425) {$9\,/\,3$};
\node[lab,tick,anchor=east] at (-0.050,-1.425) {$i=3$};
\draw[cell frame] (2.850,-2.850) rectangle (3.800,-1.900);
\node[lab] at (3.325,-2.375) {$0$};
\node[lab,tick,anchor=east] at (-0.050,-2.375) {$i=4$};
\node[lab,tick] at (0.475,1.130) {$j=0$};
\node[lab,tick] at (1.425,1.130) {$j=1$};
\node[lab,tick] at (2.375,1.130) {$j=2$};
\node[lab,tick] at (3.325,1.130) {$j=3$};
\end{tikzpicture}
\end{center}
```

The table for keys $1,2,3$ with weights $10,8,9$: each cell shows $e(i,j)$ and the best root $R(i,j)$; the cells $e(i,i-1)=0$ are empty trees. The answer $e(1,3)=46$ has root $2$, which gives the balanced tree of @fig-interval-subproblems-1.

:::

::: {#fig-interval-subproblems-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (a) at (0,0) {$1$}; \node[small vertex] (b) at (0.8,-0.9) {$3$}; \node[small vertex] (c) at (0.3,-1.8) {$2$};
\draw (a)--(b) (b)--(c);
\node[lab,tick] at (0.4,-2.5) {cost $10+2\cdot9+3\cdot8=52$};
\node[small vertex] (d) at (5,0) {$2$}; \node[small vertex] (e) at (4.3,-0.9) {$1$}; \node[small vertex] (f) at (5.7,-0.9) {$3$};
\draw (d)--(e) (d)--(f);
\node[lab,tick] at (5,-2.5) {cost $8+2\cdot(10+9)=46$};
\node[lab,tick] at (0.4,0.6) {greedy: heaviest key at the root};
\node[lab,tick] at (5,0.6) {optimal};
\end{tikzpicture}
\end{center}
```

Search trees for keys $1,2,3$ with weights $10,8,9$. Putting the heaviest key at the root (left) costs $52$; the balanced tree found by the dynamic program (right) costs $46$.

:::

::: {#exm-stacking-blocks .example name="Stacking blocks"}

Given boxes with dimensions $(\ell_i,w_i,h_i)$, each usable in any rotation and any number of times, build the tallest tower in which every box sits on one whose base is strictly larger in both directions. List each box in its three rotations (taking $\ell\ge w$), sort the $3n$ oriented boxes by base area, and let $x(i)$ be the tallest tower with oriented box $i$ on top: $x(i)=h_i+\max\{x(j):\ell_j>\ell_i,\ w_j>w_i\}$ (or $h_i$ alone). This is a longest path in a DAG, $O(n^2)$ time, like the longest increasing subsequence (@exm-lis).

:::

```{=latex}
\begin{algorithm}
\caption{Stacking blocks}
\begin{algorithmic}
\INPUT Boxes $(\ell_i,w_i,h_i)$, $i=1,\dots,n$
\OUTPUT The height of a tallest tower
\STATE list the $3n$ oriented boxes (each dimension once as the height, base $\ell\ge w$)
\STATE sort them by decreasing base area $\ell w$, as $b_1,\dots,b_{3n}$
\FOR{$i=1$ to $3n$}
    \STATE $x(i)\gets h_i$
    \FOR{$j=1$ to $i-1$}
        \IF{$\ell_j>\ell_i$ and $w_j>w_i$}
            \STATE $x(i)\gets\max\{x(i),\ h_i+x(j)\}$
        \ENDIF
    \ENDFOR
\ENDFOR
\RETURN $\max_ix(i)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-interval-subproblems-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,tick] at (0.00,0.00) {$(4,3,2)$};
\node[lab,tick] at (1.30,0.00) {$12$};
\node[lab,tick] at (2.40,0.00) {$2$};
\node[lab,tick] at (0.00,-0.60) {$(4,2,3)$};
\node[lab,tick] at (1.30,-0.60) {$8$};
\node[lab,tick] at (2.40,-0.60) {$3$};
\node[lab,tick] at (0.00,-1.20) {$(3,2,4)$};
\node[lab,tick] at (1.30,-1.20) {$6$};
\node[lab,tick] at (2.40,-1.20) {$6$};
\node[lab,tick] at (0.00,0.55) {$(\ell,w,h)$};
\node[lab,tick] at (1.30,0.55) {$\ell w$};
\node[lab,tick] at (2.40,0.55) {$x(i)$};
\draw[faint] (-0.7,0.33) -- (2.8,0.33);
\draw[hl box] (3.80,-1.00) rectangle (5.20,-0.30);
\node[lab,tick,anchor=west] at (5.30,-0.65) {base $4\times3$, height $2$};
\draw[hl box] (3.98,-0.30) rectangle (5.03,1.10);
\node[lab,tick,anchor=west] at (5.12,0.40) {base $3\times2$, height $4$};
\draw[faint] (3.50,-1.0) -- (5.50,-1.0);
\end{tikzpicture}
\end{center}
```

Stacking copies of one $4\times3\times2$ box. Its three orientations, sorted by base area, with $x(i)$, the tallest tower having that orientation on top. Only the base $4\times3$ is strictly larger in both directions than the base $3\times2$, so the best tower (right) puts the box lying flat at the bottom and standing on its $3\times2$ face on top: height $2+4=6$.

:::
