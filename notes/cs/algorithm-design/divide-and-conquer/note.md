---
title: "Divide and Conquer: Convex Hull, Median, Matrix Multiplication"
sources: [mit6046-2, mit6046r-1]
requires: [cs/algorithm-design/greedy-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 2 and Recitation 1, in our own wording; proofs written out in steps. -->

*Divide and conquer*: split a problem of size $n$ into $a$ subproblems of size $n/b$, solve them recursively, and combine the answers. The running time satisfies $T(n)=aT(n/b)+(\text{divide and combine time})$, solved by the master theorem (@thm-master-theorem).

## Convex hull

::: {#def-convex-hull .definition name="Convex hull"}

The *convex hull* $\mathrm{CH}(S)$ of a finite set $S$ of points in the plane is the smallest convex polygon containing $S$. We represent it by its corner points in clockwise order. (We assume no two points share an $x$-coordinate and no three are collinear.)

:::

Brute force tests every segment between two points: it is a hull edge exactly when all other points lie on one side of it, $O(n^3)$ time.

::: {#def-hull-divide-conquer .definition name="Divide-and-conquer hull"}

Sort the points by $x$-coordinate once. To find the hull of a set, split it at the median $x$-coordinate into a left half $A$ and a right half $B$, compute $\mathrm{CH}(A)$ and $\mathrm{CH}(B)$ recursively, and merge: find the *upper tangent* $(a_i,b_j)$ and the *lower tangent* $(a_k,b_m)$, the two segments joining the hulls that have all points below, respectively above, them. The merged hull follows $\mathrm{CH}(A)$ from $a_i$ round to $a_k$, then $\mathrm{CH}(B)$ from $b_m$ round to $b_j$.

:::

```{=latex}
\begin{algorithm}
\caption{Divide-and-conquer convex hull}
\begin{algorithmic}
\INPUT Points $S$ sorted by $x$-coordinate
\OUTPUT $\mathrm{CH}(S)$, corners in clockwise order
\IF{$|S|\le3$}
    \RETURN the hull, by brute force
\ENDIF
\STATE split $S$ at the median $x$-coordinate into $A$ (left) and $B$ (right)
\STATE $\mathrm{CH}(A)\gets$ hull of $A$; $\mathrm{CH}(B)\gets$ hull of $B$ \COMMENT{recursively}
\STATE $(a_i,b_j)\gets$ upper tangent; $(a_k,b_m)\gets$ lower tangent
\RETURN $\mathrm{CH}(A)$ from $a_i$ round to $a_k$, then $\mathrm{CH}(B)$ from $b_m$ round to $b_j$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-divide-and-conquer-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (1.6,0.6) -- (2.2,2.4) -- (0.5,3) -- cycle;
\draw[faint] (3.2,1.2) -- (3.4,0.2) -- (5.4,1.0) -- (4.6,3.2) -- (3.8,2.6) -- cycle;
\draw[emph] (0,0) -- (3.4,0.2) -- (5.4,1.0) -- (4.6,3.2) -- (0.5,3) -- cycle;
\draw[hl] (0,0) -- (3.4,0.2);
\draw[hl] (4.6,3.2) -- (0.5,3);
\fill (0,0) circle[pt];
\fill (1,2) circle[pt];
\fill (0.5,3) circle[pt];
\fill (1.6,0.6) circle[pt];
\fill (2.2,2.4) circle[pt];
\fill (1.4,1.4) circle[pt];
\fill (3.4,0.2) circle[pt];
\fill (4.6,3.2) circle[pt];
\fill (5.4,1.0) circle[pt];
\fill (3.8,2.6) circle[pt];
\fill (4.4,1.6) circle[pt];
\fill (3.2,1.2) circle[pt];
\draw[faint, dashed] (2.7,-0.4) -- (2.7,3.6);
\node[lab] at (1,-0.6) {$A$}; \node[lab] at (4.4,-0.6) {$B$};
\end{tikzpicture}
\end{center}
```

Merging two convex hulls (thin) across the dividing line. The upper and lower tangents (highlighted) join them; the merged hull (bold) follows the left hull from one tangent to the other, then the right hull back.

:::

::: {#prp-two-finger-tangent .proposition name="Finding the upper tangent in linear time"}

Let $L$ be the vertical line between $A$ and $B$, and for a segment from $a\in A$ to $b\in B$ let $y(a,b)$ be the height at which it crosses $L$. Start with $a$ the rightmost point of $A$ and $b$ the leftmost point of $B$. Repeat: move $b$ clockwise while that increases $y(a,b)$, then move $a$ counter-clockwise while that increases $y(a,b)$, until neither move helps. The final $(a,b)$ is the upper tangent, found in $O(|A|+|B|)$ time.

:::

::: {.proof}

1. The upper tangent is the segment between the two hulls that crosses $L$ highest: any segment from $A$ to $B$ crossing $L$ higher would have hull points of both sides below it, so it would be a common supporting line, and conversely.

2. Each move strictly increases $y(a,b)$, and each finger moves monotonically along its hull, so there are at most $|A|+|B|$ moves.

3. When neither move increases $y(a,b)$, the segment is locally supporting for both convex polygons, and for a convex polygon locally supporting means supporting. So $(a,b)$ is the upper tangent.

:::

```{=latex}
\begin{algorithm}
\caption{Upper tangent by two fingers}
\begin{algorithmic}
\INPUT Hulls $\mathrm{CH}(A)$ and $\mathrm{CH}(B)$ on either side of a vertical line $L$
\OUTPUT The upper tangent $(a,b)$
\STATE $a\gets$ rightmost point of $A$; $b\gets$ leftmost point of $B$
\STATE $\mathit{moved}\gets$ true
\WHILE{$\mathit{moved}$}
    \STATE $\mathit{moved}\gets$ false
    \WHILE{$y(a,\text{clockwise neighbour of }b)>y(a,b)$}
        \STATE $b\gets$ clockwise neighbour of $b$; $\mathit{moved}\gets$ true
    \ENDWHILE
    \WHILE{$y(\text{counter-clockwise neighbour of }a,b)>y(a,b)$}
        \STATE $a\gets$ counter-clockwise neighbour of $a$; $\mathit{moved}\gets$ true
    \ENDWHILE
\ENDWHILE
\RETURN $(a,b)$
\end{algorithmic}
\end{algorithm}
```

So $T(n)=2T(n/2)+O(n)=O(n\log n)$, which is optimal: sorting reduces to the convex hull (put the numbers on a parabola).

## Median finding in linear time

::: {#def-select .definition name="Selection"}

`select(S, i)` returns the element of rank $i$ in a set $S$ of $n$ distinct numbers (the median is rank $\lceil n/2\rceil$). Sorting gives $O(n\log n)$; we want $O(n)$.

:::

::: {#def-median-of-medians .definition name="Median of medians"}

`select(S, i)`:

1. split $S$ into groups of $5$ and find the median of each group;
2. recursively find the median $x$ of these $\lceil n/5\rceil$ medians;
3. partition $S$ into $B=\{y<x\}$ and $C=\{y>x\}$, and let $k=|B|+1$ be the rank of $x$;
4. if $i=k$ return $x$; if $i<k$ return `select(B, i)`; otherwise return `select(C, i-k)`.

:::

```{=latex}
\begin{algorithm}
\caption{Median of medians: select$(S,i)$}
\begin{algorithmic}
\INPUT A set $S$ of $n$ distinct numbers, a rank $1\le i\le n$
\OUTPUT The element of rank $i$ in $S$
\IF{$n\le5$}
    \RETURN the element of rank $i$, by sorting
\ENDIF
\STATE split $S$ into groups of $5$; $M\gets$ the medians of the groups
\STATE $x\gets$ select$(M,\lceil|M|/2\rceil)$ \COMMENT{the median of the medians}
\STATE $B\gets\{y\in S:y<x\}$; $C\gets\{y\in S:y>x\}$; $k\gets|B|+1$
\IF{$i=k$}
    \RETURN $x$
\ELSIF{$i<k$}
    \RETURN select$(B,i)$
\ENDIF
\RETURN select$(C,i-k)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-divide-and-conquer-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.0,0.0) rectangle (0.6,0.5);
\node[lab, lbl bold] at (0.3,0.25) {5};
\draw[cell frame] (0.0,-0.62) rectangle (0.6,-0.12);
\node[lab, lbl bold] at (0.3,-0.37) {8};
\draw[cell frame] (0.0,-1.24) rectangle (0.6,-0.74);
\node[lab, lbl bold] at (0.3,-0.99) {12};
\draw[cell frame] (0.0,-1.86) rectangle (0.6,-1.36);
\node[lab] at (0.3,-1.61) {28};
\draw[cell frame] (0.0,-2.48) rectangle (0.6,-1.98);
\node[lab] at (0.3,-2.23) {65};
\draw[cell frame] (0.75,0.0) rectangle (1.35,0.5);
\node[lab, lbl bold] at (1.05,0.25) {7};
\draw[cell frame] (0.75,-0.62) rectangle (1.35,-0.12);
\node[lab, lbl bold] at (1.05,-0.37) {20};
\draw[cell frame] (0.75,-1.24) rectangle (1.35,-0.74);
\node[lab, lbl bold] at (1.05,-0.99) {42};
\draw[cell frame] (0.75,-1.86) rectangle (1.35,-1.36);
\node[lab] at (1.05,-1.61) {51};
\draw[cell frame] (0.75,-2.48) rectangle (1.35,-1.98);
\node[lab] at (1.05,-2.23) {84};
\draw[cell frame] (1.5,0.0) rectangle (2.1,0.5);
\node[lab, lbl bold] at (1.8,0.25) {10};
\draw[cell frame] (1.5,-0.62) rectangle (2.1,-0.12);
\node[lab, lbl bold] at (1.8,-0.37) {13};
\draw[hl cell] (1.5,-1.24) rectangle (2.1,-0.74);
\node[lab] at (1.8,-0.99) {47};
\draw[cell frame] (1.5,-1.86) rectangle (2.1,-1.36);
\node[lab, lbl bold] at (1.8,-1.61) {69};
\draw[cell frame] (1.5,-2.48) rectangle (2.1,-1.98);
\node[lab, lbl bold] at (1.8,-2.23) {75};
\draw[cell frame] (2.25,0.0) rectangle (2.85,0.5);
\node[lab] at (2.55,0.25) {9};
\draw[cell frame] (2.25,-0.62) rectangle (2.85,-0.12);
\node[lab] at (2.55,-0.37) {31};
\draw[cell frame] (2.25,-1.24) rectangle (2.85,-0.74);
\node[lab, lbl bold] at (2.55,-0.99) {54};
\draw[cell frame] (2.25,-1.86) rectangle (2.85,-1.36);
\node[lab, lbl bold] at (2.55,-1.61) {56};
\draw[cell frame] (2.25,-2.48) rectangle (2.85,-1.98);
\node[lab, lbl bold] at (2.55,-2.23) {85};
\draw[cell frame] (3.0,0.0) rectangle (3.6,0.5);
\node[lab] at (3.3,0.25) {16};
\draw[cell frame] (3.0,-0.62) rectangle (3.6,-0.12);
\node[lab] at (3.3,-0.37) {55};
\draw[cell frame] (3.0,-1.24) rectangle (3.6,-0.74);
\node[lab, lbl bold] at (3.3,-0.99) {71};
\draw[cell frame] (3.0,-1.86) rectangle (3.6,-1.36);
\node[lab, lbl bold] at (3.3,-1.61) {73};
\draw[cell frame] (3.0,-2.48) rectangle (3.6,-1.98);
\node[lab, lbl bold] at (3.3,-2.23) {89};
\node[lab,tick, anchor=west] at (3.9,0.25) {groups of $5$, each sorted;};
\node[lab,tick, anchor=west] at (3.9,-0.25) {columns sorted by median;};
\node[lab,tick, anchor=west] at (3.9,-0.75) {$x=47$ is the median of medians:};
\node[lab,tick, anchor=west] at (3.9,-1.25) {bold items are $\le x$ (top left)};
\node[lab,tick, anchor=west] at (3.9,-1.75) {or $\ge x$ (bottom right)};
\end{tikzpicture}
\end{center}
```

Median of medians on $25$ numbers. Each column is a group of $5$ in increasing order, and the columns are ordered by their medians. Everything above and to the left of $x$ is at most $x$, and everything below and to the right is at least $x$: about $\frac3{10}$ of the items on each side, so the recursion discards at least that many.

:::

::: {#thm-median-of-medians .theorem name="Selection in linear time"}

The median-of-medians algorithm runs in $O(n)$ time.

:::

::: {.proof}

1. Half of the $\lceil n/5\rceil$ groups have a median at least $x$, and in each such group (except possibly $x$'s own and a last incomplete one) at least $3$ elements are at least $x$. So at least $3\bigl(\frac12\lceil n/5\rceil-2\bigr)\ge\frac{3n}{10}-6$ elements are at least $x$, and symmetrically at least $\frac{3n}{10}-6$ are at most $x$.

2. Hence each of $B$ and $C$ has at most $\frac{7n}{10}+6$ elements, and $T(n)\le T(\lceil n/5\rceil)+T(\frac{7n}{10}+6)+O(n)$.

3. Guess $T(n)\le cn$. The right side is at most $c(\frac n5+1)+c(\frac{7n}{10}+6)+an=cn-\bigl(\frac{cn}{10}-7c-an\bigr)$, which is at most $cn$ for $c\ge20a$ and $n\ge140$; smaller $n$ are handled by a large enough $c$. So $T(n)=O(n)$. The key fact is $\frac15+\frac7{10}<1$.

:::

## Strassen's matrix multiplication

Multiplying two $n\times n$ matrices from the definition takes $\Theta(n^3)$ operations. Splitting each into four $\frac n2\times\frac n2$ blocks and multiplying blocks naively uses $8$ block products, $T(n)=8T(n/2)+O(n^2)=\Theta(n^3)$: no gain.

::: {#thm-strassen .theorem name="Strassen"}

Seven block products suffice, so two $n\times n$ matrices can be multiplied in $O(n^{\log_27})=O(n^{2.81})$ time.

:::

::: {.proof}

1. With $A=\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{pmatrix}$ and $B$ likewise, form
   $M_1=(A_{11}+A_{22})(B_{11}+B_{22})$, $M_2=(A_{21}+A_{22})B_{11}$, $M_3=A_{11}(B_{12}-B_{22})$, $M_4=A_{22}(B_{21}-B_{11})$, $M_5=(A_{11}+A_{12})B_{22}$, $M_6=(A_{21}-A_{11})(B_{11}+B_{12})$, $M_7=(A_{12}-A_{22})(B_{21}+B_{22})$.

2. Expanding shows $C_{11}=M_1+M_4-M_5+M_7$, $C_{12}=M_3+M_5$, $C_{21}=M_2+M_4$ and $C_{22}=M_1-M_2+M_3+M_6$.

3. That is $7$ products of half-size matrices and $O(n^2)$ additions: $T(n)=7T(n/2)+O(n^2)=O(n^{\log_27})$ by case 1 of the master theorem.

:::

```{=latex}
\begin{algorithm}
\caption{Strassen's algorithm}
\begin{algorithmic}
\INPUT $n\times n$ matrices $A$ and $B$, $n$ a power of $2$
\OUTPUT $C=AB$
\IF{$n=1$}
    \RETURN $(a_{11}b_{11})$
\ENDIF
\STATE split $A$ and $B$ into four $\frac n2\times\frac n2$ blocks each
\STATE compute $M_1,\dots,M_7$ as in the proof, each by a recursive call on half-size matrices
\STATE $C_{11}\gets M_1+M_4-M_5+M_7$; $C_{12}\gets M_3+M_5$
\STATE $C_{21}\gets M_2+M_4$; $C_{22}\gets M_1-M_2+M_3+M_6$
\RETURN $C$ assembled from its four blocks
\end{algorithmic}
\end{algorithm}
```

::: {#fig-divide-and-conquer-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$3$};
\draw[cell frame] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$4$};
\node[lab,tick] at (0.55,0.85) {$A$};
\draw[cell frame] (1.600,0.000) rectangle (2.150,0.550);
\node[lab] at (1.875,0.275) {$5$};
\draw[cell frame] (2.150,0.000) rectangle (2.700,0.550);
\node[lab] at (2.425,0.275) {$6$};
\draw[cell frame] (1.600,-0.550) rectangle (2.150,0.000);
\node[lab] at (1.875,-0.275) {$7$};
\draw[cell frame] (2.150,-0.550) rectangle (2.700,0.000);
\node[lab] at (2.425,-0.275) {$8$};
\node[lab,tick] at (2.15,0.85) {$B$};
\node[lab,anchor=west] at (3.60,0.55) {$M_1=(1+4)(5+8)=65$};
\node[lab,anchor=west] at (3.60,0.13) {$M_2=(3+4)\cdot5=35$};
\node[lab,anchor=west] at (3.60,-0.29) {$M_3=1\cdot(6-8)=-2$};
\node[lab,anchor=west] at (3.60,-0.71) {$M_4=4\cdot(7-5)=8$};
\node[lab,anchor=west] at (3.60,-1.13) {$M_5=(1+2)\cdot8=24$};
\node[lab,anchor=west] at (3.60,-1.55) {$M_6=(3-1)(5+6)=22$};
\node[lab,anchor=west] at (3.60,-1.97) {$M_7=(2-4)(7+8)=-30$};
\draw[hl cell] (8.600,0.000) rectangle (9.300,0.700);
\node[lab] at (8.950,0.350) {$19$};
\draw[hl cell] (9.300,0.000) rectangle (10.000,0.700);
\node[lab] at (9.650,0.350) {$22$};
\draw[hl cell] (8.600,-0.700) rectangle (9.300,0.000);
\node[lab] at (8.950,-0.350) {$43$};
\draw[hl cell] (9.300,-0.700) rectangle (10.000,0.000);
\node[lab] at (9.650,-0.350) {$50$};
\node[lab,tick] at (9.30,0.95) {$C=AB$};
\node[lab,tick,anchor=west] at (8.00,-1.40) {$C_{11}=M_1+M_4-M_5+M_7$, $C_{12}=M_3+M_5$};
\node[lab,tick,anchor=west] at (8.00,-1.80) {$C_{21}=M_2+M_4$, $C_{22}=M_1-M_2+M_3+M_6$};
\end{tikzpicture}
\end{center}
```

Strassen's seven products on $2\times2$ matrices, where every block is a number. The products $M_1,\dots,M_7$ combine to $C=19,22;43,50$, the same as the definition gives ($1\cdot5+2\cdot7=19$, and so on), with $7$ multiplications instead of $8$. For larger $n$ the same formulas apply to $\frac n2\times\frac n2$ blocks.

:::
