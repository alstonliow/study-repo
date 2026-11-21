::: {.problem #prob-ee364ahw-1-q3 origin="external" source="ee364ahw-1-q3"}
Which of the following sets are convex?

(a) A *slab*, i.e., a set of the form $\{x\in\mathbf{R}^n\mid\alpha\le a^Tx\le\beta\}$.

(b) A *rectangle*, i.e., a set of the form $\{x\in\mathbf{R}^n\mid\alpha_i\le x_i\le\beta_i,\ i=1,\ldots,n\}$. A rectangle is sometimes called a *hyperrectangle* when $n>2$.

(c) A *wedge*, i.e., $\{x\in\mathbf{R}^n\mid a_1^Tx\le b_1,\ a_2^Tx\le b_2\}$.

(d) The set of points closer to a given point than a given set, i.e.,
$$\{x\mid\lVert x-x_0\rVert_2\le\lVert x-y\rVert_2\ \text{for all}\ y\in S\}$$
where $S\subseteq\mathbf{R}^n$.

(e) The set of points closer to one set than another, i.e.,
$$\{x\mid\mathbf{dist}(x,S)\le\mathbf{dist}(x,T)\},$$
where $S,T\subseteq\mathbf{R}^n$, and
$$\mathbf{dist}(x,S)=\inf\{\lVert x-z\rVert_2\mid z\in S\}.$$

(f) [HUL93, volume 1, page 93] The set $\{x\mid x+S_2\subseteq S_1\}$, where $S_1,S_2\subseteq\mathbf{R}^n$ with $S_1$ convex.

(g) The set of points whose distance to $a$ does not exceed a fixed fraction $\theta$ of the distance to $b$, i.e., the set $\{x\mid\lVert x-a\rVert_2\le\theta\lVert x-b\rVert_2\}$. You can assume $a\ne b$ and $0\le\theta\le1$.
:::

::: {.problem #prob-ee364ahw-1-q4 origin="external" source="ee364ahw-1-q4"}
*Some sets of probability distributions.* Let $x$ be a real-valued random variable with $\mathbf{prob}(x=a_i)=p_i$, $i=1,\ldots,n$, where $a_1<a_2<\cdots<a_n$. Of course $p\in\mathbf{R}^n$ lies in the standard probability simplex $P=\{p\mid\mathbf 1^Tp=1,\ p\succeq0\}$. Which of the following conditions are convex in $p$? (That is, for which of the following conditions is the set of $p\in P$ that satisfy the condition convex?)

(a) $\alpha\le\mathbf{E}f(x)\le\beta$, where $\mathbf{E}f(x)$ is the expected value of $f(x)$, i.e., $\mathbf{E}f(x)=\sum_{i=1}^np_if(a_i)$. (The function $f:\mathbf{R}\to\mathbf{R}$ is given.)

(b) $\mathbf{prob}(x>\alpha)\le\beta$.

(c) $\mathbf{E}\lvert x^3\rvert\le\alpha\,\mathbf{E}\lvert x\rvert$.

(d) $\mathbf{E}x^2\le\alpha$.

(e) $\mathbf{E}x^2\ge\alpha$.

(f) $\mathbf{var}(x)\le\alpha$, where $\mathbf{var}(x)=\mathbf{E}(x-\mathbf{E}x)^2$ is the variance of $x$.

(g) $\mathbf{var}(x)\ge\alpha$.

(h) $\mathbf{quartile}(x)\ge\alpha$, where $\mathbf{quartile}(x)=\inf\{\beta\mid\mathbf{prob}(x\le\beta)\ge0.25\}$.

(i) $\mathbf{quartile}(x)\le\alpha$.
:::
