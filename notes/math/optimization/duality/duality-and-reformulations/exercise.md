::: {.problem #prob-ee364ahw-4-q3 origin="external" source="ee364ahw-4-q3"}
*Lagrangian relaxation of Boolean LP.* A *Boolean linear program* is an optimization problem of the form
$$\begin{array}{ll}\text{minimize}&c^Tx\\ \text{subject to}&Ax\preceq b\\ &x_i\in\{0,1\},\quad i=1,\ldots,n,\end{array}$$
and is, in general, very difficult to solve. In exercise 4.15 we studied the LP relaxation of this problem,
$$\begin{array}{ll}\text{minimize}&c^Tx\\ \text{subject to}&Ax\preceq b\\ &0\le x_i\le1,\quad i=1,\ldots,n,\end{array}\qquad(1)$$
which is far easier to solve, and gives a lower bound on the optimal value of the Boolean LP. In this problem we derive another lower bound for the Boolean LP, and work out the relation between the two lower bounds.

(a) *Lagrangian relaxation.* The Boolean LP can be reformulated as the problem
$$\begin{array}{ll}\text{minimize}&c^Tx\\ \text{subject to}&Ax\preceq b\\ &x_i(1-x_i)=0,\quad i=1,\ldots,n,\end{array}$$
which has quadratic equality constraints. Find the Lagrange dual of this problem. The optimal value of the dual problem (which is convex) gives a lower bound on the optimal value of the Boolean LP. This method of finding a lower bound on the optimal value is called *Lagrangian relaxation*.

(b) Show that the lower bound obtained via Lagrangian relaxation, and via the LP relaxation (1), are the same. *Hint.* Derive the dual of the LP relaxation (1).
:::
