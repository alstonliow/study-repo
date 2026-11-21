<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-ee364ahw-6-q4" status="draft"}
1. Write $a_i^T$ for the rows of $A$, and split each into positive and negative parts, $a_i=a_i^+-a_i^-$ with $(a_i^+)_j=\max\{a_{ij},0\}$ and $(a_i^-)_j=\max\{-a_{ij},0\}$.

2. $\mathcal R\subseteq\mathcal P$ iff $\max_{x\in\mathcal R}a_i^Tx\le b_i$ for every $i$. The maximum of a linear function over a box is taken coordinate by coordinate: $x_j=u_j$ where $a_{ij}>0$ and $x_j=l_j$ where $a_{ij}<0$. So
$$\max_{l\preceq x\preceq u}a_i^Tx=(a_i^+)^Tu-(a_i^-)^Tl,$$
and the containment is the $m$ linear inequalities $A^+u-A^-l\preceq b$, with $A^\pm$ the matrices of rows $(a_i^\pm)^T$. This avoids the $2^n$ vertex constraints.

3. The volume is $\prod_j(u_j-l_j)$; maximizing its logarithm gives the convex problem
$$\begin{array}{ll}\text{maximize}&\sum_{j=1}^n\log(u_j-l_j)\\ \text{subject to}&A^+u-A^-l\preceq b,\end{array}$$
with implicit constraint $l\prec u$. The objective is concave (a sum of $\log$ of affine functions) and the constraints are linear, in the same spirit as the inscribed ellipsoid of @def-max-inscribed-ellipsoid.
:::
