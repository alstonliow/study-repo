<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cama1s-2-q6" status="draft"}
1. $f$ is continuous and $2\pi$-periodic, and $f \ge 0$.

2. $f(x) > 0$ for every $x$. If $f(x) = 0$ then $\sin x = 0$, so $x = m\pi$ and $\cos x = \pm1$, so $\cos^7 x = \pm 1$. Then $x + \cos^7 x = m\pi \pm 1$ and $\sin^2(m\pi \pm 1) = \sin^2 1 > 0$, a contradiction.

3. On the closed bounded interval $[0, 2\pi]$ the continuous function $f$ attains its minimum $k$ at some point, so $k > 0$ by step 2.

4. By periodicity, $f(x) \ge k$ for all $x \in \mathbb{R}$. (Numerically $k \approx 0.177$.)
:::

::: {.solution for="prob-cama1s-2-q7" status="draft"}
1. $f$ attains its maximum $M$ on $[0,1]$. Suppose $M > 0$. The set $S = \{x : f(x) = M\}$ is non-empty and closed (preimage of a point under a continuous map), so $c = \inf S$ lies in $S$. Since $f(0) = f(1) = 0 < M$, $c \in (0,1)$.

2. Take $\delta$ as in the hypothesis for $x = c$. Then $c - \delta \in (0, c)$, so $c - \delta \notin S$ and $f(c - \delta) < M$, while $f(c + \delta) \le M$. Hence $2M = f(c - \delta) + f(c + \delta) < 2M$, a contradiction. So $M \le 0$, that is, $f \le 0$.

3. $-f$ satisfies the same hypotheses, so $-f \le 0$. Therefore $f = 0$.
:::

::: {.solution for="prob-cama1s-2-q8" status="draft"}
1. Let $g(x) = f(x) - x$, continuous on $[0,1]$. Then $g(0) = f(0) \ge 0$ and $g(1) = f(1) - 1 \le 0$, so by the intermediate value theorem $g(c) = 0$ for some $c \in [0,1]$.

2. A bijection with no fixed point (necessarily discontinuous): $f(0) = 1$, $f(\frac12) = 0$, $f(1) = \frac12$, and $f(x) = 1 - x$ for all other $x$. It permutes $\{0, \frac12, 1\}$ without fixed points, maps the rest of $[0,1]$ bijectively to itself, and $1 - x = x$ only for $x = \frac12$.

3. No: $h(x) = x^2$ is a continuous bijection of $(0,1)$ onto itself, and $x^2 = x$ only for $x \in \{0, 1\}$, which are not in $(0,1)$. (A decreasing continuous bijection of $(0,1)$ does have a fixed point: $h(x) - x$ tends to $1$ as $x \to 0$ and to $-1$ as $x \to 1$.)
:::

::: {.solution for="prob-cama1s-2-q9" status="draft"}
1. For $x \in \mathbb{R}$ write $x - \lfloor x\rfloor = 0.d_1d_2d_3\ldots$ in decimal, using the expansion that does not end in recurring $9$s. Let $A_n(x) = (d_1 + \cdots + d_n)/n$. If $A_n(x)$ converges to a limit $L \in (0, 9)$, put $f(x) = \tan\left(\pi\left(\frac{L}{9} - \frac12\right)\right)$; otherwise put $f(x) = 0$.

2. Changing finitely many digits changes $d_1 + \cdots + d_n$ by a bounded amount, so it does not change whether $A_n$ converges or its limit.

3. The map $L \mapsto \tan(\pi(L/9 - 1/2))$ is a bijection from $(0,9)$ onto $\mathbb{R}$. So given $c$, there is $L \in (0,9)$ with this map sending $L$ to $c$.

4. Let $d_n = 9$ if $\lfloor nL/9\rfloor > \lfloor (n-1)L/9\rfloor$ and $d_n = 0$ otherwise. Then $d_1 + \cdots + d_n = 9\lfloor nL/9\rfloor$, so $A_n \to L$. Since $0 < L < 9$, the digits are neither eventually all $0$ nor eventually all $9$.

5. Given $a < b$, choose $k$ and an integer $m$ with $[m/10^k, (m+1)/10^k] \subset (a,b)$. Let $x$ be the number in this interval whose first $k$ decimal digits (after the integer part) are those of $m/10^k$ and whose later digits are the $d_n$ of step 4 (shifted by $k$ places). It lies strictly inside the interval, because the tail is neither all $0$s nor all $9$s. By steps 2 and 4, $A_n(x) \to L$, so $f(x) = c$.
:::
