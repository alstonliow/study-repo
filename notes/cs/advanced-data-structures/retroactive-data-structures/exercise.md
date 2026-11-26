::: {.problem #prob-mit6851ps-1-q1 origin="external" source="mit6851ps-1-q1"}
**Creationist successor.** Given an ordered universe $U$ of keys, develop and analyze a fully retroactive data structure that maintains $S\subseteq U$ and supports the following operations:

* $\mathrm{insert}(k)$: Insert $k\in U$ into $S$
* $\mathrm{delete}(k)$: Remove $k\in U$ from $S$
* $\mathrm{successor}(k)$: Return $\min\{k'\in S\mid k'\ge k\}$

under the constraint that all insert operations must occur at time $-\infty$. All operations should run in time $O(\log m)$, where $m$ is the total number of updates performed in the structure (retroactive or not). Observe that such a structure is sufficient to answer the "rightward ray shot" queries needed for the nonoblivious retroactive priority queue.

A simple reference to the logarithmic time data structure for general retroactive successor is not a valid solution to this problem. This is a special case of that problem, and a much simpler solution is desired.
:::
