<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-3-q3" status="draft"}
(a) Every point feasible for (1) is feasible for (2), since $\{0,1\}\subseteq[0,1]$. Minimizing the same objective over a larger set gives a value no larger, so $p^\star_{(2)}\le p^\star_{(1)}$. If (2) is infeasible, its feasible set is empty, and so is the smaller feasible set of (1): the Boolean LP is infeasible too.

(b) Let $x^\star$ solve (2) with all $x_i^\star\in\{0,1\}$. Then $x^\star$ is feasible for (1), so $p^\star_{(1)}\le c^Tx^\star=p^\star_{(2)}\le p^\star_{(1)}$ by (a). Hence $x^\star$ is optimal for the Boolean LP and the two optimal values are equal.
:::
