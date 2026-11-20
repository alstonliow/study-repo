<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-ats-1-q14" status="draft"}
1. $n = 1$ is the Bolzano–Weierstrass theorem.

2. Suppose the result holds in $\mathbb{R}^{n-1}$, and let $(v_m)$ be bounded in $\mathbb{R}^n$; write $v_m = (w_m, t_m)$ with $w_m \in \mathbb{R}^{n-1}$ and $t_m \in \mathbb{R}$. Both $(w_m)$ and $(t_m)$ are bounded, since each coordinate is at most the Euclidean norm.

3. By the induction hypothesis, some subsequence $(w_{m_k})$ converges to $w$. The real sequence $(t_{m_k})$ is bounded, so a further subsequence $(t_{m_{k_j}})$ converges to $t$; along it, still $w_{m_{k_j}} \to w$.

4. Then $\|v_{m_{k_j}} - (w,t)\| \le \|w_{m_{k_j}} - w\| + |t_{m_{k_j}} - t| \to 0$.
:::

::: {.solution for="prob-camib-ats-2-q11" status="draft"}
1. Choose a basis $e_1, \dots, e_n$ and identify the space with $\mathbb{R}^n$. It suffices to show that any norm $\|\cdot\|$ is equivalent to the Euclidean norm $\|\cdot\|_2$, since equivalence is transitive.

2. Upper bound: by the triangle inequality and Cauchy–Schwarz, $\|x\| \le \sum|x_i|\,\|e_i\| \le C\|x\|_2$ with $C = (\sum\|e_i\|^2)^{1/2}$.

3. So $|\|x\| - \|y\|| \le \|x - y\| \le C\|x - y\|_2$, and $\|\cdot\|$ is continuous for the Euclidean metric.

4. Lower bound: the unit sphere $S = \{\|x\|_2 = 1\}$ is closed and bounded, hence compact, so $\|\cdot\|$ attains a minimum $m$ on $S$, and $m > 0$ because a norm vanishes only at $0$. For $x \ne 0$, $\|x\| = \|x\|_2\,\|x/\|x\|_2\| \ge m\|x\|_2$.

5. So $m\|x\|_2 \le \|x\| \le C\|x\|_2$.

6. In infinite dimensions this fails. On $C([0,1])$ take $\|f\|_\infty = \sup|f|$ and $\|f\|_1 = \int_0^1|f|$. For $f_n(x) = x^n$, $\|f_n\|_\infty = 1$ but $\|f_n\|_1 = 1/(n+1) \to 0$, so there is no $c > 0$ with $\|f\|_1 \ge c\|f\|_\infty$.
:::
