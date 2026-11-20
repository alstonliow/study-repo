::: {.problem #prob-cama1s-1-q8 origin="external" source="cama1s-1-q8"}
Let $z \in \mathbb{C}$ such that $z^{2^j} \neq 1$ for any positive integer $j$. Show that the series
$$\frac{z}{1-z^2} + \frac{z^2}{1-z^4} + \frac{z^4}{1-z^8} + \frac{z^8}{1-z^{16}} + \cdots$$
converges to $z/(1-z)$ if $|z| < 1$, converges to $1/(1-z)$ if $|z| > 1$, and diverges if $|z| = 1$.
:::

::: {.problem #prob-cama1s-1-q9 origin="external" source="cama1s-1-q9"}
Investigate the convergence of the following series. For those expressions containing the complex number $z$, find those $z$ for which convergence occurs.
$$\sum_n \frac{\sin n}{n^2} \qquad \sum_n \frac{n^2z^n}{5^n} \qquad \sum_n \frac{(-1)^n}{4+\sqrt{n}} \qquad \sum_n \frac{z^n(1-z)}{n}$$
:::

::: {.problem #prob-cama1s-1-q11 origin="external" source="cama1s-1-q11"}
For $n \geqslant 1$, let
$$a_n = \frac{1}{\sqrt n} + \frac{(-1)^{n-1}}{n}.$$
Show that each $a_n$ is positive and that $\lim a_n = 0$. Show also that $\sum_{n=1}^\infty (-1)^{n-1}a_n$ diverges.
:::

::: {.problem #prob-cama1s-1-q12 origin="external" source="cama1s-1-q12"}
Let $a_n$ and $b_n$ be two sequences and let $S_n = \sum_{j=1}^n a_j$ with the convention $S_0 = 0$.

(a) Show that for any $1 \leqslant m \leqslant n$ we have:
$$\sum_{j=m}^n a_jb_j = S_nb_n - S_{m-1}b_m + \sum_{j=m}^{n-1} S_j(b_j - b_{j+1}).$$

(b) Suppose now that $b_n$ is a decreasing sequence of positive terms tending to zero and that $S_n$ is a bounded sequence. Prove that $\sum_{j=1}^\infty a_jb_j$ converges.

(c) Does the series $\sum_{n=1}^\infty \frac{\cos(n)}{n}$ converge or diverge?

(d) Deduce the alternating series test from the assertion in part (b).
:::
