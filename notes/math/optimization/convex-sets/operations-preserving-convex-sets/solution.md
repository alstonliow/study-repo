<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-1-q3" status="draft"}
(a) Convex: it is the intersection of the halfspaces $a^Tx\le\beta$ and $-a^Tx\le-\alpha$ (@prp-intersection-convex).

(b) Convex: it is the intersection of the $2n$ halfspaces $x_i\le\beta_i$, $-x_i\le-\alpha_i$; in fact a polyhedron.

(c) Convex: an intersection of two halfspaces.

(d) Convex. For each fixed $y\in S$, the set $\{x\mid\lVert x-x_0\rVert_2\le\lVert x-y\rVert_2\}$ is a halfspace (previous exercise; it is all of $\mathbf{R}^n$ if $y=x_0$). The set in question is the intersection of these halfspaces over $y\in S$.

(e) Not convex in general. Take $n=1$, $S=\{-1,1\}$, $T=\{0\}$. Then $\mathbf{dist}(x,S)\le\mathbf{dist}(x,T)$ means $\min\{\lvert x+1\rvert,\lvert x-1\rvert\}\le\lvert x\rvert$, which holds exactly for $\lvert x\rvert\ge\frac12$. The points $\pm1$ belong to the set, but their midpoint $0$ does not.

(f) Convex. $x+S_2\subseteq S_1$ means $x+y\in S_1$ for every $y\in S_2$, so the set is $\bigcap_{y\in S_2}(S_1-y)$, an intersection of translates of the convex set $S_1$.

(g) Convex. Squaring (both sides are nonnegative), the condition is
$$(1-\theta^2)\,x^Tx-2(a-\theta^2b)^Tx+\big(a^Ta-\theta^2b^Tb\big)\le0.$$
If $\theta=1$ this is a halfspace (part (d) with $S=\{b\}$). If $0\le\theta<1$, divide by $1-\theta^2>0$: the left side becomes $\lVert x\rVert_2^2-2c^Tx+\text{const}$ with $c=(a-\theta^2b)/(1-\theta^2)$, so the set is a Euclidean ball centred at $c$ (possibly a single point or empty, both convex).
:::

::: {.solution for="prob-ee364ahw-1-q4" status="draft"}
Throughout, a condition that is a linear inequality in $p$ defines a halfspace, and its intersection with $P$ is convex.

(a) Convex: $\alpha\le\sum_ip_if(a_i)\le\beta$ is a pair of linear inequalities in $p$ (a slab).

(b) Convex: $\mathbf{prob}(x>\alpha)=\sum_{i:\,a_i>\alpha}p_i$ is linear in $p$.

(c) Convex: the condition is $\sum_ip_i\big(\lvert a_i\rvert^3-\alpha\lvert a_i\rvert\big)\le0$, linear in $p$.

(d) Convex: $\sum_ip_ia_i^2\le\alpha$ is linear.

(e) Convex: $\sum_ip_ia_i^2\ge\alpha$ is linear.

(f) Not convex in general. $\mathbf{var}(x)=\sum_ip_ia_i^2-\big(\sum_ip_ia_i\big)^2$ is a linear function minus the square of a linear function, a concave function of $p$, and its sublevel sets need not be convex. Example: $n=2$, $a=(0,1)$, $\alpha=0$. Both $p=(1,0)$ and $p=(0,1)$ give variance $0$, but their midpoint gives variance $\frac14>0$.

(g) Convex: $\mathbf{var}(x)$ is concave in $p$, so its superlevel set $\{p\mid\mathbf{var}(x)\ge\alpha\}$ is convex.

(h) Convex. $\mathbf{quartile}(x)\ge\alpha$ holds iff $\mathbf{prob}(x\le\beta)<0.25$ for every $\beta<\alpha$. Since $x$ takes finitely many values, $\sup_{\beta<\alpha}\mathbf{prob}(x\le\beta)=\sum_{i:\,a_i<\alpha}p_i$ and the supremum is attained (take $\beta$ between the largest $a_i$ below $\alpha$ and $\alpha$). So the condition is $\sum_{i:\,a_i<\alpha}p_i<0.25$, an open halfspace.

(i) Convex. As $\beta\mapsto\mathbf{prob}(x\le\beta)$ is right-continuous, the infimum defining the quartile is attained, so $\mathbf{quartile}(x)\le\alpha$ iff $\mathbf{prob}(x\le\alpha)\ge0.25$, that is, $\sum_{i:\,a_i\le\alpha}p_i\ge0.25$, a halfspace.
:::
