::: {.problem #prob-ee364ahw-3-q3 origin="external" source="ee364ahw-3-q3"}
*Relaxation of Boolean LP.* In a *Boolean linear program*, the variable $x$ is constrained to have components equal to zero or one:
$$\begin{array}{ll}\text{minimize}&c^Tx\\ \text{subject to}&Ax\preceq b\\ &x_i\in\{0,1\},\quad i=1,\ldots,n.\end{array}\qquad(1)$$
In general, such problems are very difficult to solve, even though the feasible set is finite (containing at most $2^n$ points).

In a general method called *relaxation*, the constraint that $x_i$ be zero or one is replaced with the linear inequalities $0\le x_i\le1$:
$$\begin{array}{ll}\text{minimize}&c^Tx\\ \text{subject to}&Ax\preceq b\\ &0\le x_i\le1,\quad i=1,\ldots,n.\end{array}\qquad(2)$$
We refer to this problem as the *LP relaxation* of the Boolean LP (1). The LP relaxation is far easier to solve than the original Boolean LP.

(a) Show that the optimal value of the LP relaxation (2) is a lower bound on the optimal value of the Boolean LP (1). What can you say about the Boolean LP if the LP relaxation is infeasible?

(b) It sometimes happens that the LP relaxation has a solution with $x_i\in\{0,1\}$. What can you say in this case?
:::
