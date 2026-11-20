<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-4-q6" status="draft"}
Path-connected sets are connected.

(a) Path-connected, hence connected. The closed disc $D_1$ about $(-1,0)$ is convex and contains $0 = (0,0)$. For $p$ in the open disc $D_2$ about $c = (1,0)$ and $t \in (0,1]$, $|tp - c| = |t(p - c) - (1-t)c| \le t|p - c| + (1-t) < 1$, so the segment from $p$ to $0$ lies in $D_2 \cup \{0\}$. So every point is joined to $0$ by a segment in the set.

(b) Path-connected, hence connected: it is a union of lines through $0$, and every point is joined to $0$ by a segment along its line.

(c) Neither. No point of the set lies on the line $y = \sqrt2x$: points with $x \ne 0$ have rational slope $y/x$, and the origin is removed. So the open half-planes $\{y > \sqrt2x\}$ and $\{y < \sqrt2x\}$ meet the set in two disjoint, relatively open, non-empty sets covering it (for example $(0,1)$ and $(0,-1)$). So it is disconnected, hence not path-connected.

(d) Path-connected (every point is joined to $x_0$ by a segment in $S$), hence connected.
:::

::: {.solution for="prob-camib-ats-4-q7" status="draft"}
Compact subsets of a Hausdorff space are closed.

(a) Suppose $K = \emptyset$. Then the open sets $X \setminus K_n$ cover $X$, hence cover the compact set $K_1$, so finitely many do. As they increase with $n$, $K_1 \subset X \setminus K_N$ for some $N$, so $K_N = K_N \cap K_1 = \emptyset$, a contradiction.

(b)

1. $K$ is closed, so it is a closed subset of the compact Hausdorff space $K_1$.

2. Suppose $K = P \cup Q$ with $P, Q$ disjoint, non-empty and closed in $K$, hence closed in $K_1$. A compact Hausdorff space separates disjoint closed sets (sheet 3, question 15), so there are disjoint sets $U \supset P$, $V \supset Q$, open in $K_1$.

3. The sets $K_n \setminus (U \cup V)$ are closed in $K_1$, hence compact, decreasing, and their intersection is $K \setminus (U \cup V) = \emptyset$. By (a), some $K_N \setminus (U \cup V)$ is empty, that is, $K_N \subset U \cup V$.

4. Then $K_N \cap U \supset P$ and $K_N \cap V \supset Q$ are disjoint, non-empty, relatively open, and cover $K_N$, contradicting connectedness of $K_N$.

(c) Let $K_n = (\{0,1\} \times \mathbb{R}) \cup ([0,1] \times [n,\infty))$: two vertical lines joined by a half-strip. Each $K_n$ is closed, non-empty and path-connected, and they decrease. But $\bigcap_nK_n = \{0,1\} \times \mathbb{R}$, two disjoint lines, is not connected.
:::

::: {.solution for="prob-camib-ats-4-q8" status="draft"}
1. Let $g(x) = f(x) - f(-x)$, continuous on $S^1$, with $g(-x) = -g(x)$.

2. Take any $x_0$. If $g(x_0) = 0$ we are done. Otherwise $g(x_0)$ and $g(-x_0)$ have opposite signs.

3. $S^1$ is path-connected, hence connected, so $g(S^1)$ is a connected subset of $\mathbb{R}$, an interval. It contains a positive and a negative number, hence $0$. So $g(x) = 0$, that is, $f(x) = f(-x)$, for some $x$.

4. The equator is a circle, and temperature is (modelled as) a continuous function on it.
:::

::: {.solution for="prob-camib-ats-4-q9" status="draft"}
1. Suppose not. Then there are $x_k \to x$ and $\varepsilon > 0$ with $|f(x_k) - f(x)| \ge \varepsilon$ for all $k$.

2. Let $C_k$ be the union of $\{x\}$ and the segments $[x_j, x_{j+1}]$ for $j \ge k$. It is path-connected: run through the $j$-th segment during $[1 - 2^{k-j}, 1 - 2^{k-j-1}]$ and send $1$ to $x$; this is continuous at $1$ since every point of the $j$-th segment is within $\max(|x_j - x|, |x_{j+1} - x|)$ of $x$.

3. So $f(C_k)$ is path-connected, hence connected, and contains $f(x)$ and $f(x_k)$. The continuous function $z \mapsto |z - f(x)|$ on $f(C_k)$ therefore takes every value in $[0,\varepsilon]$. Let $r_k = \frac\varepsilon2 + \frac{\varepsilon}{4k}$ and choose $z_k \in C_k$ with $|f(z_k) - f(x)| = r_k$. Then $z_k \ne x$, so $z_k$ lies on a segment with index $\ge k$, and $|z_k - x| \le \sup_{j\ge k}|x_j - x| \to 0$.

4. $L = \{x\} \cup \{z_k : k \ge 1\}$ is compact (a convergent sequence with its limit), so $f(L)$ is compact, hence closed and bounded.

5. The points $f(z_k)$ lie in a bounded set, so a subsequence converges to some $w$, with $|w - f(x)| = \lim r_k = \varepsilon/2$. As $f(L)$ is closed, $w \in f(L)$. But $w \ne f(x)$, and $w \ne f(z_k)$ for every $k$ since $|f(z_k) - f(x)| = r_k > \varepsilon/2$. This contradiction shows $f$ is continuous.
:::
