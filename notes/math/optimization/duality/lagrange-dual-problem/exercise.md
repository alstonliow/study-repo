::: {.problem #prob-ee364ahw-4-q2 origin="external" source="ee364ahw-4-q2"}
*A simple example.* Consider the optimization problem
$$\begin{array}{ll}\text{minimize}&x^2+1\\ \text{subject to}&(x-2)(x-4)\le0,\end{array}$$
with variable $x\in\mathbf{R}$.

(a) *Analysis of primal problem.* Give the feasible set, the optimal value, and the optimal solution.

(b) *Lagrangian and dual function.* Plot the objective $x^2+1$ versus $x$. On the same plot, show the feasible set, optimal point and value, and plot the Lagrangian $L(x,\lambda)$ versus $x$ for a few positive values of $\lambda$. Verify the lower bound property ($p^\star\ge\inf_xL(x,\lambda)$ for $\lambda\ge0$). Derive and sketch the Lagrange dual function $g$.

(c) *Lagrange dual problem.* State the dual problem, and verify that it is a concave maximization problem. Find the dual optimal value and dual optimal solution $\lambda^\star$. Does strong duality hold?

(d) *Sensitivity analysis.* Let $p^\star(u)$ denote the optimal value of the problem
$$\begin{array}{ll}\text{minimize}&x^2+1\\ \text{subject to}&(x-2)(x-4)\le u,\end{array}$$
as a function of the parameter $u$. Plot $p^\star(u)$. Verify that $dp^\star(0)/du=-\lambda^\star$.
:::
