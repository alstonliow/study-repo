::: {.problem #prob-cs70hw-12-q1 origin="external" source="cs70hw-12-q1"}
**Graph.** Consider a random graph (undirected, no multi-edges, no self-loops) on $n$ nodes, where each possible edge exists independently with probability $p$. Let $X$ be the number of isolated nodes (nodes with degree 0).

(a) What is $\mathrm{Var}(X)$?
:::

::: {.problem #prob-cs70hw-12-q2 origin="external" source="cs70hw-12-q2"}
**Whitening.** Let $X$ and $Y$ be two random variables, with $\mathrm{Var}(X) > 0$, $\mathrm{Var}(Y) > 0$. Show that it is possible to construct $\tilde{X} = aX + bY$ and $\tilde{Y} = cX + dY$, where $a, b, c, d$ are scalars to be chosen subject to the constraint $ad - bc \ne 0$, such that $\mathrm{cov}(\tilde{X}, \tilde{Y}) = 0$.

You may find it unnecessary to transform $Y$, that is, you only need to solve for $a, b$ to get $\mathrm{cov}(\tilde{X}, Y) = 0$.
:::
