::: {.problem #prob-camib-ats-1-q6 origin="external" source="camib-ats-1-q6"}
For each of the following sets $X$, determine whether or not the given function $d$ defines a metric on $X$.

(a) $X = \mathbb{R}^n$; $d(x,y) = \min\{|x_1 - y_1|, |x_2 - y_2|, \dots, |x_n - y_n|\}$.

(b) $X = \mathbb{C}$;
$$d(z,w) = \begin{cases} |z - w|, & \text{if } z \text{ and } w \text{ lie on the same line through the origin,} \\ |z| + |w|, & \text{otherwise.} \end{cases}$$

(c) $X$ is the set of functions from $\mathbb{N}$ to $\mathbb{N}$, i.e. sequences with values in $\mathbb{N}$; for $N$ the smallest natural number such that $x_n \neq y_n$,
$$d(x_n, y_n) = \begin{cases} 0, & \text{if } x_n = y_n \ \forall n \in \mathbb{N}, \\ 2^{-N}, & \text{otherwise.} \end{cases}$$

(d) $X$ is the set of closed, non-empty, bounded subsets of a metric space $(M, d_0)$;
$$d(A,B) = \max\Big\{\sup_{a\in A}\inf_{b\in B}d_0(a,b),\ \sup_{b\in B}\inf_{a\in A}d_0(a,b)\Big\}, \qquad A, B \in X.$$
Note: we say a subset $U$ of a metric space $(M, d_0)$ is bounded if there exists $r > 0$ such that $d_0(x,y) < r$ for all $x, y \in U$.
:::

::: {.problem #prob-camib-ats-1-q7 origin="external" source="camib-ats-1-q7"}
For an alphabetic string $s$ of length $L \in \mathbb{N}$, let $s[i]$ be the character at position $i$, for $i = 1, \dots, L$. Let $X_L$ be the set of strings of length $L$. In computer science, one sometimes considers the functions on $X_L$ given by

(a) $d_1(s,s') = \#\{i : s[i] \neq s'[i]\}$;

(b) $d_2(s,s')$ is the minimum number of single-character insertions, deletions or substitutions required to change $s$ into $s'$.

Show that both are metrics on $X_L$. For which $L \in \mathbb{N}$ are they equivalent metrics?
:::
