::: {.problem #prob-mit6851ps-3-q1 origin="external" source="mit6851ps-3-q1"}
**Geometric basics.** Recall that in class we introduced the geometric view for binary search tree execution. Using only this view, prove that for any set of $m$ queries on $n$ items, there is a BST that will answer the queries in total time $O(m\lg n)$. You should reason only about point sets, not about BSTs.
:::

::: {.problem #prob-mit6851ps-3-q2 origin="external" source="mit6851ps-3-q2"}
**Working-set is harder.** In class we introduced the entropy bound and the working-set property for BSTs. The entropy bound holds if all searches in the BST have amortized time $O\bigl(\sum_{k=1}^n p_k\lg\frac1{p_k}\bigr)$, where $p_k$ is the fraction of the time that key $k$ is queried. The working-set property holds if the time to search for an element $x_i$ is $O(\lg t_i)$, where $t_i$ is the number of elements queried since the last access to $x_i$. Prove that any BST with the working-set property also has the entropy bound.
:::
