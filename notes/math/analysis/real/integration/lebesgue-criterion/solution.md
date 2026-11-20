<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-3-q13" status="draft"}
(a) For $I' \subset I$, $\sup_{I'}f \le \sup_I f$ and $\inf_{I'}f \ge \inf_I f$; subtract. And
$$U(f,\mathcal P) - L(f,\mathcal P) = \sum_j |I_j|\sup_{I_j}f - \sum_j |I_j|\inf_{I_j}f = \sum_j |I_j|\operatorname{osc}_{I_j}(f).$$

(b)

1. Let $|f| \le M$ and $\varepsilon > 0$. Choose $\eta > 0$ so small that the intervals $[d_i - \eta, d_i + \eta]$ are disjoint and lie in $(a,b)$.

2. The rest of $[a,b]$ is a finite union of closed intervals on which $f$ is continuous, hence uniformly continuous. Partition each into pieces on which $\operatorname{osc}f < \varepsilon$.

3. Together with the points $d_i \pm \eta$ this gives a dissection $\mathcal P$ with, by (a),
$$U - L \le \sum_{i=1}^k 2\eta\cdot 2M + \varepsilon(b - a) = 4Mk\eta + \varepsilon(b-a),$$
which is small when $\eta$ and $\varepsilon$ are. By Riemann's criterion $f$ is integrable.

(c)

1. *Lemma.* If $f$ is integrable on a closed interval $J$ of positive length and $r > 0$, then $J$ contains a closed interval $J'$ of positive length with $\operatorname{osc}_{J'}f < r$, lying in the interior of $J$, with $|J'| \le |J|/2$. Proof: take a dissection of $J$ with $U - L < r|J|$. Since $\sum|I_j| = |J|$, by (a) some $I_j$ has $\operatorname{osc}_{I_j}f < r$. Let $J'$ be a closed subinterval in the interior of $I_j$ of length at most $|J|/2$; by (a), $\operatorname{osc}_{J'}f < r$.

2. Apply the lemma repeatedly, starting from $J_0 = [a,b]$, with $r = 1/n$ at step $n$ (integrable on $[a,b]$ implies integrable on each subinterval). This gives nested closed intervals $J_n$ with $J_{n+1}$ in the interior of $J_n$ and $\operatorname{osc}_{J_n}f < 1/n$.

3. The $J_n$ have a common point $x$, and $x$ is interior to every $J_n$. So for each $n$ there is $\delta > 0$ with $(x - \delta, x + \delta) \cap [a,b] \subset J_n$, and there $|f(y) - f(x)| < 1/n$. Hence $f$ is continuous at $x$.

4. Applying this to the restriction of $f$ to each of the disjoint intervals $[a + (b-a)2^{-m}, a + (b-a)2^{-m+1}]$, $m \ge 1$, gives a continuity point in the interior of each (continuity of the restriction at an interior point is continuity of $f$ there). So $f$ has infinitely many points of continuity.
:::
