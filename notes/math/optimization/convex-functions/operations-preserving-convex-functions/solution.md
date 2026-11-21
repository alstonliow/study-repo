<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-2-q4" status="draft"}
1. Fix $x,y$ and $0\le\theta\le1$, put $z=\theta x+(1-\theta)y$, $u=g(z)=(g_1(z),\ldots,g_k(z))$ and $w=\theta g(x)+(1-\theta)g(y)$.

2. Compare $u$ and $w$ coordinate by coordinate: $u_i\le w_i$ if $g_i$ is convex, $u_i\ge w_i$ if $g_i$ is concave, and $u_i=w_i$ if $g_i$ is affine.

3. Change the arguments of $h$ from $u$ to $w$ one coordinate at a time. In a coordinate where $g_i$ is convex, $h$ is nondecreasing and the argument increases from $u_i$ to $w_i$, so $h$ does not decrease; where $g_i$ is concave, $h$ is nonincreasing and the argument decreases, so again $h$ does not decrease; affine coordinates do not change. Hence $h(u)\le h(w)$.

4. Convexity of $h$ gives $h(w)\le\theta h(g(x))+(1-\theta)h(g(y))$.

5. Combining, $f(z)=h(u)\le h(w)\le\theta f(x)+(1-\theta)f(y)$, so $f$ is convex.
:::
