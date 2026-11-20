<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-1-q2" status="draft"}
Let $g(x) = (x^4+1)/3$, so $a_{n+1} = g(a_n)$. The graphs meet where $x^4 - 3x + 1 = 0$. For $x \ge 0$ this has exactly two roots $\alpha \approx 0.3377$ and $\beta \approx 1.3075$ (the function $x^4-3x+1$ is $1$ at $0$, $-1$ at $1$, $11$ at $2$, and is convex). Moreover $g(x) > x$ on $[0,\alpha)$, $g(x) < x$ on $(\alpha,\beta)$ and $g(x) > x$ on $(\beta,\infty)$; and $g$ is increasing on $[0,\infty)$. The sequence converges for $a_1 = 0$ and $a_1 = 1$ (to $\alpha$) and diverges for $a_1 = 2$.

1. Since $g$ is increasing on $[0,\infty)$, $a_1 \le a_2$ implies $a_n \le a_{n+1}$ for all $n$ by induction, and similarly with $\ge$. Also $x < \alpha \Rightarrow g(x) < g(\alpha) = \alpha$ and $\alpha < x < \beta \Rightarrow \alpha < g(x) < \beta$.

2. $a_1 = 0$: $a_2 = 1/3 > a_1$, so $(a_n)$ is increasing, and $a_n < \alpha$ for all $n$ by step 1. A bounded monotone sequence converges; its limit $L$ satisfies $L = g(L)$ by continuity of $g$, and $L \in [0,\alpha]$, so $L = \alpha$.

3. $a_1 = 1 \in (\alpha,\beta)$: $a_2 = 2/3 < a_1$, so $(a_n)$ is decreasing, and $a_n > \alpha$ for all $n$. Hence $a_n \to L$ with $g(L) = L$ and $L \in [\alpha, 1]$, so $L = \alpha$.

4. $a_1 = 2$: $a_2 = 17/3 > a_1$, so $(a_n)$ is increasing. If it were bounded, it would converge to some $L \ge 2$ with $g(L) = L$; but there is no fixed point above $\beta < 2$. So $a_n \to \infty$.
:::

::: {.solution for="prob-cama1s-1-q3" status="draft"}
The common limit is $\sqrt{a_1b_1}$.

1. Suppose $a_n > b_n > 0$. Then $a_{n+1} = (a_n+b_n)/2 < a_n$, and $b_{n+1} - b_n = b_n(a_n - b_n)/(a_n+b_n) > 0$.

2. $a_{n+1} - b_{n+1} = \dfrac{(a_n+b_n)^2 - 4a_nb_n}{2(a_n+b_n)} = \dfrac{(a_n-b_n)^2}{2(a_n+b_n)} > 0$. So $a_n > a_{n+1} > b_{n+1} > b_n > 0$, and by induction this holds for all $n$.

3. $(a_n)$ is decreasing and bounded below by $b_1$, $(b_n)$ is increasing and bounded above by $a_1$, so both converge, say to $a$ and $b$. Letting $n \to \infty$ in $a_{n+1} = (a_n+b_n)/2$ gives $a = (a+b)/2$, so $a = b$.

4. $a_{n+1}b_{n+1} = \frac{a_n+b_n}{2}\cdot\frac{2a_nb_n}{a_n+b_n} = a_nb_n$, so $a_nb_n = a_1b_1$ for all $n$. In the limit $a^2 = a_1b_1$, and $a > 0$, so $a = b = \sqrt{a_1b_1}$.
:::

::: {.solution for="prob-cama1s-1-q5" status="draft"}
1. Call $m$ a *peak* of $(x_n)$ if $x_m \ge x_n$ for all $n > m$.

2. If there are infinitely many peaks $m_1 < m_2 < \cdots$, then $x_{m_1} \ge x_{m_2} \ge \cdots$, a decreasing subsequence.

3. Otherwise there is $N$ beyond which no index is a peak. Put $n_1 = N+1$. Since $n_1$ is not a peak, there is $n_2 > n_1$ with $x_{n_2} > x_{n_1}$; since $n_2$ is not a peak, there is $n_3 > n_2$ with $x_{n_3} > x_{n_2}$; and so on. This gives an increasing subsequence.

4. Bolzano–Weierstrass: if $(x_n)$ is bounded, a monotone subsequence is bounded and monotone, so it converges by the monotone convergence theorem.
:::

::: {.solution for="prob-cama1s-1-q6" status="draft"}
1. By Bolzano–Weierstrass some subsequence converges, say to $a$.

2. Since $x_n \not\to a$, there is $\varepsilon > 0$ with $|x_n - a| \ge \varepsilon$ for infinitely many $n$. These terms form a bounded subsequence, which by Bolzano–Weierstrass has a further subsequence converging to some $b$.

3. Every term of that subsequence satisfies $|x_n - a| \ge \varepsilon$, so $|b - a| \ge \varepsilon$ and $b \ne a$.
:::
