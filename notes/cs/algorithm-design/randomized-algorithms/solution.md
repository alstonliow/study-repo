<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-4-q2" status="draft"}
(a) The pivot is uniform among the $m$ elements. If its rank is between $\frac m4$ and $\frac{3m}4$ (at least half of the ranks), both sides of the partition have at most $\frac34m$ elements, so either the pivot is $x_i$ or $x_i$'s next subarray has at most $\frac34m$ elements.

(b) Call a recursive call containing $x_i$ *good* if it has the property in (a); each call is good with probability at least $\frac12$, whatever happened before. After $c\lg n$ good calls with $c=\frac1{\lg(4/3)}\approx2.41$, the size is at most $(\frac34)^{c\lg n}n=1$, so $x_i$ is in at most $c\lg n$ good calls (or is a pivot sooner). Every call compares $x_i$ with one pivot. By the Claim with $\alpha=2$, among $3(2+c)\lg n$ calls at least $c\lg n$ are good with probability at least $1-\frac1{n^2}$ (good calls dominate independent fair coin tosses). So with that probability $x_i$ is compared at most $d\lg n$ times, $d=3(2+c)\approx13.2$.

(c) Every comparison is between some element and a pivot, so the total is $\sum_i(\text{comparisons of }x_i)$. By the union bound over the $n$ elements, all of them satisfy (b) with probability at least $1-n\cdot\frac1{n^2}=1-\frac1n$, and then the total is at most $dn\lg n$: $d'=d\approx13.2$.

(d) Use the Claim with $\alpha+1$ in (b): each $x_i$ has at most $3(\alpha+1+c)\lg n$ comparisons with probability $1-\frac1{n^{\alpha+1}}$, and the union bound gives at most $3(\alpha+1+c)\,n\lg n$ comparisons in total with probability at least $1-\frac1{n^\alpha}$.
:::
