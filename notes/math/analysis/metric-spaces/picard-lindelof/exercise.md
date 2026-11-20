::: {.problem #prob-camib-ats-2-q10 origin="external" source="camib-ats-2-q10"}
Take $0 < a, b < \infty$. Let $f : [-a,a] \times [-b,b] \to \mathbb{R}$ be a continuous function. Consider the initial value problem
$$\begin{cases} y'(x) = f(x,y(x)), \\ y(0) = y_0 \end{cases}.$$

(a) Is the solution necessarily unique? Give a proof or counterexample.

(b) Show that for every $k \in \mathbb{N}$, there is sequence of intervals $I_k$, which are neighborhood of zero, and functions $y_k \in C(I_k)$ solving the initial value problem
$$\begin{cases} y_k'(x) = f_k(x,y_k(x)), \\ y_k(0) = y_0 \end{cases}.$$
where $(f_k)$ are Lipschitz functions satisfying $f_k \rightrightarrows f$ on $[-a,a] \times [b,b]$. Hint: you may assume, without proof, the statement of problem 12 below. What happens as $k \to \infty$?

(c) ($\star$) Show that there is a solution $y(x)$ for $x \in (-\epsilon, \epsilon)$, where $0 < \epsilon \leq a$. Hint: you may assume, without proof, the statements in problems 12 and 13(d) below. Compare with your answer in part (b).

*Note (these notes):* The printed rectangle $[-a,a]\times[b,b]$ in (b) is read as $[-a,a]\times[-b,b]$, and the solution assumes $|y_0| < b$.
:::
