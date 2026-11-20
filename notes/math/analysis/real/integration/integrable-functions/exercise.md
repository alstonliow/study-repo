::: {.problem #prob-cama1s-3-q9 origin="external" source="cama1s-3-q9"}
Let $f(x) = \sin(1/x)$ for $x \neq 0$ and $f(0) = 0$. Does $\int_0^1 f$ exist?
:::

::: {.problem #prob-cama1s-3-q11 origin="external" source="cama1s-3-q11"}
Let $f_1, f_2 : [a,b] \to \mathbb{R}$ be increasing and $g = f_1 - f_2$.

(a) Show that there exists $K$ such that, for any partition $P = x_0 < \cdots < x_n$ of $[-1,1]$, $\sum_{j=1}^n |g(x_j) - g(x_{j-1})| \leq K$.

(b) Deduce that $g$ is integrable.

(c) Now let $h(x) = x\sin(1/x)$ for $x \neq 0$ and $h(0) = 0$. Show that $h$ is integrable. Show that $h$ is not the difference of two increasing functions.

*Note (these notes):* The printed statement of (a) says a partition of $[-1,1]$; the function is defined on $[a,b]$, so the solution reads it as $[a,b]$.
:::

::: {.problem #prob-cama1s-3-q12 origin="external" source="cama1s-3-q12"}
This question exemplifies how badly behaved integrable functions can be.

(a) Let $f : \mathbb{R} \to \mathbb{R}$ be monotonic. Show that $\{x \in \mathbb{R} : f \text{ is discontinuous at } x\}$ is countable.

(b) Let $x_n$, $n \geq 1$ be a sequence of distinct points in $(0,1]$. Let
$$f(x) = \sum_{n=1}^\infty 2^{-n}f_n(x), \qquad f_n(x) = \begin{cases} 0, & 0 \leq x < x_n \\ 1, & x_n \leq x \leq 1 \end{cases}.$$
Show that this series converges for every $x \in [0,1]$. Show that $f$ is increasing (and so is integrable). Show that $f$ is discontinuous at every $x_n$.
:::
