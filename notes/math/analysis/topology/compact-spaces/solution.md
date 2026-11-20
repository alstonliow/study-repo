<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-3-q14" status="draft"}
$(X,\tau)$ is compact exactly when $X$ is finite; $(X,\rho)$ is always compact.

1. If $X$ is finite, every topology on it is compact.

2. If $X$ is infinite, choose distinct $s_1, s_2, \ldots \in X$ and let $S = \{s_n\}$. The sets $U_n = (X \setminus S) \cup \{s_n\}$ are open in $\tau$ (their complements $S \setminus \{s_n\}$ are countable) and cover $X$. A finite subfamily misses some $s_m$. So $(X,\tau)$ is not compact.

3. Cofinite: let $\mathcal U$ be an open cover of a non-empty $X$. Pick a non-empty $U_0 \in \mathcal U$; then $X \setminus U_0$ is finite, and each of its points lies in some member of $\mathcal U$. These finitely many members together with $U_0$ cover $X$.
:::

::: {.solution for="prob-camib-ats-3-q15" status="draft"}
Closed subsets of a compact space are compact.

1. *Point and closed set.* Let $x \notin F$ with $F$ closed. For each $y \in F$ choose disjoint open $U_y \ni x$ and $V_y \ni y$ (Hausdorff). The $V_y$ cover the compact set $F$, so $F \subset V_{y_1} \cup \cdots \cup V_{y_m}$. Then $U = \bigcap_iU_{y_i}$ and $V = \bigcup_iV_{y_i}$ are disjoint open sets with $x \in U$ and $F \subset V$.

2. *Two closed sets.* For each $x \in F_1$, step 1 gives disjoint open $U_x \ni x$ and $V_x \supset F_2$. The $U_x$ cover the compact set $F_1$, so $F_1 \subset U_{x_1} \cup \cdots \cup U_{x_k}$.

3. Let $G_1 = \bigcup_jU_{x_j}$ and $G_2 = \bigcap_jV_{x_j}$. They are open, $F_1 \subset G_1$, $F_2 \subset G_2$, and disjoint because each $U_{x_j}$ is disjoint from $V_{x_j} \supset G_2$.
:::

::: {.solution for="prob-camib-ats-4-q17" status="draft"}
This is the Tietze extension theorem for compact Hausdorff spaces.

(a)

1. Let $A = f^{-1}([-1,-\frac13])$ and $B = f^{-1}([\frac13,1])$. They are closed in $K$, hence in $X$, and disjoint.

2. Take $g_1 = \chi$ with $\chi : X \to [-\frac13,\frac13]$, $\chi = -\frac13$ on $A$ and $\chi = \frac13$ on $B$. Then $\sup_X|g_1| \le \frac13$.

3. On $A$: $f \in [-1,-\frac13]$ and $g_1 = -\frac13$, so $|f - g_1| \le \frac23$. On $B$ likewise. On $K \setminus (A \cup B)$: $|f| < \frac13$ and $|g_1| \le \frac13$, so $|f - g_1| < \frac23$.

(b) Induction on $n$; $n = 1$ is (a). Suppose $g_1, \dots, g_n$ are constructed and let $r = f - \sum_{j\le n}g_j$ on $K$, continuous with $|r| \le (2/3)^n$. Apply (a) to $(3/2)^nr : K \to [-1,1]$ to get $h$ with $\sup_X|h| \le \frac13$ and $\sup_K|(3/2)^nr - h| \le \frac23$. Put $g_{n+1} = (2/3)^nh$. Then $\sup_X|g_{n+1}| \le \frac13(\frac23)^n$ and $\sup_K|f - \sum_{j\le n+1}g_j| = \sup_K|r - g_{n+1}| \le (\frac23)^{n+1}$.

(c) (The sum starts at $j = 1$.) $\sum_n\frac13(\frac23)^{n-1}$ converges, so by the Weierstrass M-test $\sum g_n$ converges uniformly on $X$ and its sum $g$ is continuous. On $K$, $|f - \sum_{j\le n}g_j| \le (2/3)^n \to 0$, so $g|_K = f$. Moreover $|g| \le \sum_n\frac13(\frac23)^{n-1} = 1$.
:::
