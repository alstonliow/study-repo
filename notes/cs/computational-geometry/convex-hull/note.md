---
title: "Convex Hull by Divide and Conquer"
sources: [mit6046-2, mit6046r-1]
requires: [cs/algorithms/divide-and-conquer]
aliases: [cs/algorithm-topics/convex-hull]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 2 and Recitation 1, in our own wording; proofs written out in steps. Split from cs/algorithms/divide-and-conquer on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

A divide-and-conquer algorithm (@sec-cs-algorithms-divide-and-conquer) from computational geometry.

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
