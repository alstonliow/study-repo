<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-2-q13" status="draft"}
$C(X)$ carries the uniform metric $d_\infty(f,g) = \sup_X|f - g|$, finite since $X$ is compact.

(a) $C(X)$ is complete: a uniformly Cauchy sequence of continuous functions converges uniformly, and the limit is continuous. A subset of a complete space is complete iff it is closed, and a metric space is compact iff it is complete and totally bounded. So $\mathcal F$ is compact iff it is closed and totally bounded, and it remains to show: totally bounded $\iff$ bounded and equicontinuous.

(b)

1. Bounded: a finite union of balls of radius $1$ is bounded.

2. Equicontinuous: fix $x$ and $\varepsilon > 0$. Take a finite $\varepsilon/3$-net $f_1, \dots, f_m \in \mathcal F$. Each $f_i$ is continuous, so there is a neighbourhood $U_i$ of $x$ with $|f_i(y) - f_i(x)| < \varepsilon/3$ for $y \in U_i$. Let $U_x = \bigcap_iU_i$.

3. For $f \in \mathcal F$ choose $i$ with $d_\infty(f,f_i) < \varepsilon/3$. For $y \in U_x$,
$$|f(y) - f(x)| \le |f(y) - f_i(y)| + |f_i(y) - f_i(x)| + |f_i(x) - f(x)| < \varepsilon.$$

(c)

1. Let $|f| \le M$ for all $f \in \mathcal F$, and fix $\varepsilon > 0$. For each $x$ take an open neighbourhood $U_x$ as in the definition of equicontinuity. By compactness, $X = U_{x_1} \cup \cdots \cup U_{x_m}$.

2. Map $f \mapsto v(f) = (f(x_1), \dots, f(x_m)) \in [-M,M]^m$. Cover $[-M,M]^m$ by finitely many cubes $Q$ of side $\varepsilon$. For each cube that contains some $v(f)$, choose one such $f_Q \in \mathcal F$. This is a finite subfamily.

3. Given $f \in \mathcal F$, let $Q$ contain $v(f)$; then $|f(x_i) - f_Q(x_i)| \le \varepsilon$ for all $i$. For $y \in X$ pick $i$ with $y \in U_{x_i}$:
$$|f(y) - f_Q(y)| \le |f(y) - f(x_i)| + |f(x_i) - f_Q(x_i)| + |f_Q(x_i) - f_Q(y)| < 3\varepsilon.$$
So the $f_Q$ form a finite $3\varepsilon$-net, and $\mathcal F$ is totally bounded.

(d)

1. Let $\mathcal F = \{f_n\}$, bounded by $M$ and equicontinuous. Its closure $\overline{\mathcal F}$ in $C([a,b])$ is closed and bounded by $M$. It is equicontinuous: given $x$ and $\varepsilon$, use the neighbourhood $U_x$ for $\varepsilon/2$; a uniform limit $f$ of members of $\mathcal F$ then satisfies $|f(y) - f(x)| \le \varepsilon/2 < \varepsilon$ on $U_x$.

2. By (a)–(c), $\overline{\mathcal F}$ is compact, hence sequentially compact, so $(f_n)$ has a subsequence converging in $d_\infty$, that is, uniformly.

3. Comparison with sheet 1, question 13: pointwise boundedness alone does not even give a pointwise convergent subsequence on $\mathbb{R}$; adding equicontinuity (on a compact interval) gives a uniformly convergent one.
:::
