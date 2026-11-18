---
title: "Designing Subproblems"
sources: [mit6006-16, mit6006r-16]
requires: [cs/dynamic-programming/recursive-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 16 and Recitation 16, in our own wording; examples our own (checked by computation); proofs written out in steps. -->

The hard part of dynamic programming is choosing subproblems. Natural choices are prefixes, suffixes or substrings of a sequence, and pairs of these for several sequences. When the natural subproblems do not carry enough information, *constrain* or *expand* them.

## Two sequences: longest common subsequence

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

## Constraining: longest increasing subsequence

::: {#exm-lis .example name="Longest increasing subsequence"}

Given a sequence $A$, find a longest strictly increasing subsequence. For $5,2,8,6,3,6,9,7$ one answer is $2,3,6,9$, of length $4$.

The natural subproblem "a longest increasing subsequence of $A[i:]$" does not combine well: knowing such a subsequence of $A[i+1:]$ does not tell us whether $A[i]$ can be put in front. So we *constrain* the subproblem to start at $A[i]$.

1. *Subproblems:* $x(i)$, the length of a longest increasing subsequence of $A[i:]$ that *starts with* $A[i]$, for $0\le i<|A|$.
2. *Relation:* guess the second element:
   $$x(i)=\max\bigl(\{1+x(j):i<j<|A|,\ A[j]>A[i]\}\cup\{1\}\bigr),$$
   where $1$ is the case that $A[i]$ is the last element.
3. *Order:* decreasing $i$. 4. *Base:* none needed (the option $1$ covers the end).
5. *Original:* $\max_ix(i)$ (guess the first element), with parent pointers to recover a subsequence.
6. *Time:* $|A|$ subproblems with $O(|A|)$ work each: $O(|A|^2)$. (With an augmented balanced search tree the work per subproblem drops to $O(\log|A|)$.)

:::

```{=latex}
\begin{algorithm}
\caption{Longest increasing subsequence}
\begin{algorithmic}
\INPUT A sequence $A$ of length $n\ge1$
\OUTPUT The length of a longest increasing subsequence
\FOR{$i=n-1$ down to $0$}
    \STATE $x(i)\gets1$
    \FOR{$j=i+1$ to $n-1$}
        \IF{$A[j]>A[i]$ and $1+x(j)>x(i)$}
            \STATE $x(i)\gets1+x(j)$; $\mathrm{next}(i)\gets j$ \COMMENT{parent pointer}
        \ENDIF
    \ENDFOR
\ENDFOR
\RETURN $\max_ix(i)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-subproblem-design-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.700,0.700);
\node[lab] at (0.350,0.350) {$5$};
\draw[hl cell] (0.700,0.000) rectangle (1.400,0.700);
\node[lab] at (1.050,0.350) {$2$};
\draw[cell frame] (1.400,0.000) rectangle (2.100,0.700);
\node[lab] at (1.750,0.350) {$8$};
\draw[cell frame] (2.100,0.000) rectangle (2.800,0.700);
\node[lab] at (2.450,0.350) {$6$};
\draw[hl cell] (2.800,0.000) rectangle (3.500,0.700);
\node[lab] at (3.150,0.350) {$3$};
\draw[hl cell] (3.500,0.000) rectangle (4.200,0.700);
\node[lab] at (3.850,0.350) {$6$};
\draw[hl cell] (4.200,0.000) rectangle (4.900,0.700);
\node[lab] at (4.550,0.350) {$9$};
\draw[cell frame] (4.900,0.000) rectangle (5.600,0.700);
\node[lab] at (5.250,0.350) {$7$};
\node[lab, anchor=east] at (-0.100,0.350) {$A$};
\node[lab,tick] at (0.35,-0.3) {3};
\node[lab,tick] at (1.05,-0.3) {4};
\node[lab,tick] at (1.75,-0.3) {2};
\node[lab,tick] at (2.45,-0.3) {2};
\node[lab,tick] at (3.15,-0.3) {3};
\node[lab,tick] at (3.85,-0.3) {2};
\node[lab,tick] at (4.55,-0.3) {1};
\node[lab,tick] at (5.25,-0.3) {1};
\draw[->] (1.05,0.75) to[bend left=35] (3.15,0.75);
\draw[->] (3.15,0.75) to[bend left=35] (3.85,0.75);
\draw[->] (3.85,0.75) to[bend left=35] (4.55,0.75);
\node[lab,tick, anchor=east] at (-0.1,-0.3) {$x(i)$};
\end{tikzpicture}
\end{center}
```

Longest increasing subsequence of $5,2,8,6,3,6,9,7$. Under each item is $x(i)$, the length of a longest increasing subsequence starting there, computed from right to left. The maximum, $4$, is at $2$, and following the choices (arrows) gives $2,3,6,9$.

:::

## Expanding: a two-player game

::: {#exm-coin-game .example name="Alternating coin game"}

Coins with values $v_0,\dots,v_{n-1}$ lie in a row. Two players alternately take the first or the last remaining coin; I move first. How much can I guarantee, if my opponent also plays as well as possible? For $5,10,100,25$ I can guarantee $105$ of the $140$: I take $5$, and whatever the opponent takes, I then get $100$.

*First solution*, using that the game is zero-sum (I get exactly what the opponent does not).

1. *Subproblems:* $x(i,j)$, the most that the player to move can guarantee from coins $i,\dots,j$, for $0\le i\le j<n$.
2. *Relation:* the player takes coin $i$ or coin $j$; the opponent then guarantees $x(i+1,j)$ or $x(i,j-1)$ of the rest:
   $$x(i,j)=\max\Bigl\{\sum_{k=i}^jv_k-x(i+1,j),\ \sum_{k=i}^jv_k-x(i,j-1)\Bigr\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i)=v_i$. 5. *Original:* $x(0,n-1)$.
6. *Time:* $\Theta(n^2)$ subproblems; with all sums $\sum_{k=i}^jv_k$ precomputed from prefix sums, $O(1)$ work each, $\Theta(n^2)$ in total.

*Second solution*, by *expanding* the subproblems with whose turn it is.

1. *Subproblems:* $x(i,j,p)$, the most that *I* can guarantee from coins $i,\dots,j$ when player $p\in\{\text{me},\text{you}\}$ moves next.
2. *Relation:*
   $$x(i,j,\text{me})=\max\{v_i+x(i+1,j,\text{you}),\ v_j+x(i,j-1,\text{you})\},$$
   $$x(i,j,\text{you})=\min\{x(i+1,j,\text{me}),\ x(i,j-1,\text{me})\}.$$
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i,\text{me})=v_i$, $x(i,i,\text{you})=0$.
5. *Original:* $x(0,n-1,\text{me})$. 6. *Time:* $\Theta(n^2)$.

:::

```{=latex}
\begin{algorithm}
\caption{Alternating coin game}
\begin{algorithmic}
\INPUT Coin values $v_0,\dots,v_{n-1}$
\OUTPUT The most the first player can guarantee, $x(0,n-1)$
\STATE $P(0)\gets0$; $P(k+1)\gets P(k)+v_k$ for $k=0,\dots,n-1$ \COMMENT{prefix sums}
\FOR{$i=0$ to $n-1$}
    \STATE $x(i,i)\gets v_i$
\ENDFOR
\FOR{$\ell=1$ to $n-1$}
    \FOR{$i=0$ to $n-1-\ell$}
        \STATE $j\gets i+\ell$; $S\gets P(j+1)-P(i)$
        \STATE $x(i,j)\gets\max\{S-x(i+1,j),\ S-x(i,j-1)\}$
    \ENDFOR
\ENDFOR
\RETURN $x(0,n-1)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-subproblem-design-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.750,0.750);
\node[lab] at (0.375,0.375) {$5$};
\draw[cell frame] (0.750,0.000) rectangle (1.500,0.750);
\node[lab] at (1.125,0.375) {$10$};
\draw[cell frame] (1.500,0.000) rectangle (2.250,0.750);
\node[lab] at (1.875,0.375) {$105$};
\draw[hl cell] (2.250,0.000) rectangle (3.000,0.750);
\node[lab] at (2.625,0.375) {$105$};
\node[lab,tick,anchor=east] at (-0.050,0.375) {$i=0$};
\draw[cell frame] (0.750,-0.750) rectangle (1.500,0.000);
\node[lab] at (1.125,-0.375) {$10$};
\draw[cell frame] (1.500,-0.750) rectangle (2.250,0.000);
\node[lab] at (1.875,-0.375) {$100$};
\draw[hl cell] (2.250,-0.750) rectangle (3.000,0.000);
\node[lab] at (2.625,-0.375) {$35$};
\node[lab,tick,anchor=east] at (-0.050,-0.375) {$i=1$};
\draw[cell frame] (1.500,-1.500) rectangle (2.250,-0.750);
\node[lab] at (1.875,-1.125) {$100$};
\draw[hl cell] (2.250,-1.500) rectangle (3.000,-0.750);
\node[lab] at (2.625,-1.125) {$100$};
\node[lab,tick,anchor=east] at (-0.050,-1.125) {$i=2$};
\draw[hl cell] (2.250,-2.250) rectangle (3.000,-1.500);
\node[lab] at (2.625,-1.875) {$25$};
\node[lab,tick,anchor=east] at (-0.050,-1.875) {$i=3$};
\node[lab,tick] at (0.375,0.930) {$j=0$};
\node[lab,tick] at (1.125,0.930) {$j=1$};
\node[lab,tick] at (1.875,0.930) {$j=2$};
\node[lab,tick] at (2.625,0.930) {$j=3$};
\draw[cell frame] (0.000,-3.300) rectangle (0.750,-2.550);
\node[lab] at (0.375,-2.925) {$5$};
\draw[cell frame] (0.750,-3.300) rectangle (1.500,-2.550);
\node[lab] at (1.125,-2.925) {$10$};
\draw[cell frame] (1.500,-3.300) rectangle (2.250,-2.550);
\node[lab] at (1.875,-2.925) {$100$};
\draw[cell frame] (2.250,-3.300) rectangle (3.000,-2.550);
\node[lab] at (2.625,-2.925) {$25$};
\node[lab, anchor=east] at (-0.100,-2.925) {coins};
\end{tikzpicture}
\end{center}
```

The table $x(i,j)$ of the first solution for the coins $5,10,100,25$, filled by increasing $j-i$ from the diagonal $x(i,i)=v_i$. The answer is $x(0,3)=105$. Highlighted cells follow optimal play: from $(0,3)$ the player to move takes coin $0$ (value $5$), leaving $x(1,3)=35$ to the opponent, and so on.

:::

::: {#rmk-subproblem-design-expansion .remark name="Constraint and expansion"}

If the relation lacks information to check a condition of the problem, or there is no natural smaller subproblem to recurse on, add a constraint (LIS: the subsequence starts here) or extra parameters (the coin game: whose turn). More subproblems give the relation more to work with; the usual trade-off is between the number of subproblems and the work per subproblem.

:::
