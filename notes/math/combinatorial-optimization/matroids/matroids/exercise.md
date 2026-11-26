::: {.problem #prob-mit18433-5-q1 origin="external" source="mit18433-5-q1"}
Show that any partition matroid is also a linear matroid over $\mathbb F=\mathbb R$. (No need to give a precise matrix $A$ representing it; just argue its existence.)
:::

::: {.problem #prob-mit18433-5-q2 origin="external" source="mit18433-5-q2"}
Prove that a matching matroid is indeed a matroid.
:::

::: {.problem #prob-mit18433-5-q3 origin="external" source="mit18433-5-q3"}
Show that $U_{2,4}$ is representable over $\mathbb F_3$.
:::

::: {.problem #prob-mit18433-5-q4 origin="external" source="mit18433-5-q4"}
Consider the linear matroid (over the reals) defined by the $3\times5$ matrix:
$$A=\begin{pmatrix}1&2&1&0&1\\1&2&0&1&-1\\1&2&0&1&-1\end{pmatrix}.$$
The ground set $E=\{1,2,3,4,5\}$ has cardinality 5, corresponds to the columns of $A$, and the independent sets are the set of columns which are linearly independent (over the reals).

1. Give all bases of this matroid.
2. Give all circuits of this matroid.
3. Choose a base $B$ and an element $e$ not in $B$, and verify the unique circuit property for $B+e$.
:::

::: {.problem #prob-mit18433-5-q5 origin="external" source="mit18433-5-q5"}
Given a family $A_1,A_2,\cdots,A_n$ of sets (they are not necessarily disjoint), a transversal is a set $T$ such that $T=\{a_1,a_2,\cdots,a_n\}$, the $a_i$'s are distinct, and $a_i\in A_i$ for all $i$. A partial transversal is a transversal for $A_{i_1},A_{i_2},\cdots,A_{i_k}$ for some subfamily of the $A_i$'s. Show that the family of all partial transversals forms a matroid (on the ground set $E=\cup A_i$). (Hint: Think of bipartite matchings.)
:::

::: {.problem #prob-mit18433-5-q6 origin="external" source="mit18433-5-q6"}
Let $M=(E,\mathcal I)$ be a matroid. Let $k\in\mathbb N$ and define
$$\mathcal I_k=\{X\in\mathcal I:|X|\le k\}.$$
Show that $M_k=(E,\mathcal I_k)$ is also a matroid. This is known as a truncated matroid.
:::

::: {.problem #prob-mit18433-5-q7 origin="external" source="mit18433-5-q7"}
A family $\mathcal F$ of sets is said to be laminar if, for any two sets $A,B\in\mathcal F$, we have that either (i) $A\subseteq B$, or (ii) $B\subseteq A$ or (iii) $A\cap B=\emptyset$. Suppose that we have a laminar family $\mathcal F$ of subsets of $E$ and an integer $k(A)$ for every set $A\in\mathcal F$. Show that $(E,\mathcal I)$ defines a matroid (a laminar matroid) where:
$$\mathcal I=\{X\subseteq E:|X\cap A|\le k(A)\text{ for all }A\in\mathcal F\}.$$
:::
