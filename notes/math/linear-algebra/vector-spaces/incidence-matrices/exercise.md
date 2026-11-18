::: {.problem #prob-mit1806s10-3-q4 origin="external" source="mit1806s10-3-q4"}
Kirchoff's Law says that current in = current out at every node. This network has six currents $y_1,\dots,y_6$ (the arrows show the positive direction, each $y_i$ could be positive or negative). Find the four equations $A\mathbf{y}=\mathbf{0}$ for Kirchoff's Law at the four nodes. Find three special solutions in the nullspace of $A$.

*Note (these notes):* The figure is not reproduced. The network joins every pair of its four nodes: edge 1 goes from node 1 to node 2, edge 2 from 2 to 3, edge 3 from 3 to 1, edge 4 from 1 to 4, edge 5 from 2 to 4, edge 6 from 3 to 4.
:::

::: {.problem #prob-mit1806s10-5-q12 origin="external" source="mit1806s10-5-q12"}
With conductances $c_1=c_2=2$ and $c_3=c_4=c_5=3$, multiply the matrices $A^{\mathsf T}CA$. Find a solution to $A^{\mathsf T}CA\mathbf{x}=\mathbf{f}=(1,0,0,-1)$. Where these potentials $\mathbf{x}$ and currents $\mathbf{y}=-CA\mathbf{x}$ on the nodes and edges of the square graph.

*Note (these notes):* The square graph of the book has four nodes and five edges: edge 1 from node 1 to 2, edge 2 from 1 to 3, edge 3 from 2 to 3, edge 4 from 2 to 4, edge 5 from 3 to 4. $A$ is its $5\times4$ incidence matrix (@def-oriented-incidence-matrix).
:::

::: {.problem #prob-mit1806s10-5-q13 origin="external" source="mit1806s10-5-q13"}
Suppose $A$ is a $12\times9$ incidence matrix from a connected (but unknown) graph.

a. How many columns of $A$ are independent?

b. What condition on $\mathbf{f}$ makes it possible to solve $A^{\mathsf T}\mathbf{y}=\mathbf{f}$?

c. The diagonal entries of $A^{\mathsf T}A$ give the number of edges into each node. What is the sum of those diagonal entries?
:::
