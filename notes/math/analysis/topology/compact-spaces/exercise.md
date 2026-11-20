::: {.problem #prob-camib-ats-3-q14 origin="external" source="camib-ats-3-q14"}
Recall that, on a set $X$, we say that $\tau = \emptyset \cup \{A \subset X : X\setminus A \text{ countable}\}$ is the cocountable topology and $\rho = \emptyset \cup \{A \subset X : X\setminus A \text{ finite}\}$ is the cofinite topology. Can $(X,\tau)$ be compact? What about $(X,\rho)$?
:::

::: {.problem #prob-camib-ats-3-q15 origin="external" source="camib-ats-3-q15"}
($\star$) Let $X$ be a compact Hausdorff space. Show that disjoint closed subsets of $X$ can be separated: if $F_1, F_2 \subset X$ are closed and disjoint, then there are disjoint open subsets $G_1$, $G_2 \subset X$ with $F_1 \subset G_1$ and $F_2 \subset G_2$. Thus, we say that a compact Hausdorff topology not only separates points, but also separates sets.
:::

::: {.problem #prob-camib-ats-4-q17 origin="external" source="camib-ats-4-q17"}
Let $(X,\tau)$ be a compact Hausdorff space. Let $K \subset X$ be closed and $f : K \to [-1,1]$ be a continuous function (with respect to subspace topology on $K$).

(a) Show that there exists a continuous $g_1 : X \to \mathbb{R}$ such that $\sup_X|g_1| \leq \frac13$ and $\sup_K|f - g_1| \leq \frac23$. *You may assume the following statement: for any closed disjoint sets $A, B \subset X$ and $-\infty < a < b < \infty$, one can find a continuous bump function $\chi : X \to [a,b]$ such that $\chi(x) = a$ for $x \in A$ and $\chi(x) = b$ for $x \in B$.*

(b) For $n \geq 1$, construct continuous functions $g_n : X \to \mathbb{R}$ such that
$$\sup_X|g_n| \leq \frac13\left(\frac23\right)^{n-1} \qquad\text{and}\qquad \sup_K\Big|f - \sum_{j=1}^n g_j\Big| \leq \left(\frac23\right)^n.$$

(c) Deduce that the series $g(x) = \sum_{j=0}^\infty g_n(x)$ is a well-defined continuous real-valued function on $X$ such that $g|_K = f$.
:::
