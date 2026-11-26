::: {.problem #prob-ee364ahw-6-q4 origin="external" source="ee364ahw-6-q4"}
*Maximum volume rectangle inside a polyhedron.* Formulate the following problem as a convex optimization problem. Find the rectangle
$$\mathcal R=\{x\in\mathbf{R}^n\mid l\preceq x\preceq u\}$$
of maximum volume, enclosed in a polyhedron $\mathcal P=\{x\mid Ax\preceq b\}$. The variables are $l,u\in\mathbf{R}^n$. Your formulation should not involve an exponential number of constraints.
:::

::: {.problem #prob-mit6854ps-4-q4 origin="external" source="mit6854ps-4-q4"}
Let $K$ be a bounded convex set in $\mathbb R^n$. In this problem, you'll prove that there exists an ellipsoid $E$ contained within $K$ such that if you blow it up by a factor of $n$ (the dimension) then the corresponding ellipoid contains $K$; in short, $E\subseteq K$ and $K\subseteq nE$.

1. Suppose that we have an ellipsoid $E(a,A)=\{x\in\mathbb R^n:(x-a)^TA^{-1}(x-a)\le1\}$ and we have a point $b\notin nE(a,A)$. Argue that the convex hull of $b$ and $E(a,A)$, $\operatorname{conv}(\{b\},E(a,A))$, contains an ellipsoid $E'$ of larger volume than $E(a,A)$.

   (You do not need to explicitly give $a'$ and $A'$ corresponding to $E'=E(a',A')$, if that helps. It might be easier to deal with a particular case for $a$, $A$ and $b$, and argue why you can.)
2. Argue that the maximum volume ellipsoid $E$ contained in $K$ (it is actually unique, although you do not need this) is such that $nE\supseteq K$.
3. (Optional. Assume that $K=\{x\in\mathbb R^n:Cx\le d\}$ is bounded, where $C$ is $m\times n$ and $d\in\mathbb R^m$. Formulate the problem of finding the largest volume ellipsoid contained within $K$ as a convex program (minimizing a convex function over a convex set, or maximizing a concave function over a convex set. One could therefore use the ellipsoid algorithm to find (a close approximation to) this maximum volume ellipsoid.)
:::
