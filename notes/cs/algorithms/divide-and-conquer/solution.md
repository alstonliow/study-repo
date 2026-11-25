<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-1-q2" status="draft"}
(a) Two points in (or on) a $\frac12\times\frac12$ square are at most its diagonal apart, $\frac{\sqrt2}2<1$.

(b) *Divide:* split the requests at the median of $L_x$ into a left half and a right half, splitting both sorted lists in $O(n)$ by a scan (each request knows its side). *Conquer:* recurse on each half; if either finds a close pair, return it. *Combine:* now no two requests on the same side are within $1$. A close pair across the dividing line $x=x_0$ has both points in the strip $|x-x_0|<1$. Scan $L_y$ restricted to the strip; for each point, compare it with the following points whose $y$ is less than $1$ larger. Those points lie in the part of the strip of height $1$ above it, a $2\times1$ rectangle made of $8$ squares of side $\frac12$; by (a) each square holds at most one point *of each side*, so at most $16$ points lie there and at most $15$ others are compared. *Time:* $T(n)=2T(n/2)+O(n)=O(n\lg n)$. *Correctness:* a close pair is either on one side (found by induction) or crosses the line, and then the lower point compares the upper one.

(c) The same recursion, now looking for a triple. A triple that is not on one side has points on both sides, and since all three are within $1$ of each other, all three lie in the strip $|x-x_0|<1$ and within a $y$-window of height $1$. After the recursion returns "no", no three points of one side are pairwise within $1$, so each $\frac12\times\frac12$ square holds at most $2$ points of each side, and a $2\times1$ window holds at most $32$ points. For each strip point in $y$-order, test all pairs among the next constant number of points in its window: $O(1)$ per point, $O(n)$ per level, $O(n\lg n)$ in total.
:::
