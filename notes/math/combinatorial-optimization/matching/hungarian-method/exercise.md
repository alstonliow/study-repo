::: {.problem #prob-mit18433-1-q9 origin="external" source="mit18433-1-q9"}
Prove this last claim.

*Note (these notes):* the claim is that if an optimum solution to a linear programming relaxation (of a minimisation integer program) is integral, then it is also an optimum solution to the integer program.
:::

::: {.problem #prob-mit18433-1-q10 origin="external" source="mit18433-1-q10"}
Give an example of an integer program where $Z_{IP}\ne Z_{LP}$.
:::

::: {.problem #prob-mit18433-1-q11 origin="external" source="mit18433-1-q11"}
Check that the running time of the algorithm is indeed $O(n^3)$.
:::

::: {.problem #prob-mit18433-1-q15 origin="external" source="mit18433-1-q15"}
We have shown that there always exists a solution $x$ to the linear program (P) with all components integral. Reprove this result in the following way.

Take a (possibly non-integral) optimum solution $x^*$. If there are many optimum solutions, take one with as few non-integral values $x^*_{ij}$ as possible. Show that, if $x^*$ is not integral, there exists a cycle $C$ with all edges $e=(i,j)\in C$ having a non-integral value $x^*_{ij}$. Now show how to derive another optimum solution with fewer non-integral values, leading to a contradiction.
:::

::: {.problem #prob-mit18433-1-q16 origin="external" source="mit18433-1-q16"}
In this exercise, you will do a little experiment with the (minimum cost) assignment problem. Take a complete bipartite graph with $n$ vertices on each side of the bipartition, and let us assume that all $c_{ij}$ (for $i,j\in\{1,\cdots,n\}$) are all independent uniform random variables between 0 and 1. Take 5 different values for $n$ (the largest being a few hundreds) and for each compute the minimum cost assignment value for 5 instances. Any guess on how this value increases as $n$ goes to infinity. Does it seem to converge? To what value? Surprised? (Yes, you should be, and it is normal that you do not understand why.)

*Note (these notes):* the original exercise suggests MATLAB and a Hungarian-method m-file; any assignment solver will do.
:::

::: {.problem #prob-mit18433-1-q17 origin="external" source="mit18433-1-q17"}
For the assignment problem, the greedy algorithm (which repeatedly finds the minimum cost edge disjoint from all the previously selected edges) can lead to a solution whose cost divided by the optimum cost can be arbitrarily large (even for graphs with 2 vertices on each side of the bipartition).

Suppose now that the cost comes from a metric, even just a line metric. More precisely, suppose that the bipartition is $A\cup B$ with $|A|=|B|=n$ and the $i$th vertex of $A$ (resp. the $j$th vertex of $B$) is associated with $a_i\in\mathbb R$ (resp. $b_j\in B$). Suppose that the cost between these vertices is given by $c_{ij}=|a_i-b_j|$.

Consider the greedy algorithm: select the closest pair of vertices, one from A and from B, match them together, delete them, and repeat until all vertices are matched. For these line metric instances, is the cost of the greedy solution always upper bounded by a constant (independent of $n$) times the optimum cost of the assignment? If so, prove it; if not, give a family of examples (parametrized by $n$) such that the corresponding ratio becomes arbitrarily large.
:::
