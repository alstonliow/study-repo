::: {.problem #prob-mit6046s15-5-q1 origin="external" source="mit6046s15-5-q1"}
**New Operations for Skip Lists**

This problem will demonstrate that skip lists, and some augmentations of skip lists, can answer some queries about "nearby" elements efficiently. In a dynamic-set data structure, the query FINGER-SEARCH$(x,k)$ is given a node $x$ in the data structure and a key $k$, and it must return a node $y$ in the data structure that contains key $k$. (You may assume that such a node $y$ in fact appears in the data structure.) The goal is for FINGER-SEARCH to run faster when nodes $x$ and $y$ are nearby in the data structure.

(a) Write pseudocode for FINGER-SEARCH$(x,k)$ for skip lists. Assume all keys in the skip list are distinct. Assume that the given node $x$ is in the level-0 list, and the operation should return a node $y$ that stores $k$ in the level-0 list.

Your algorithm should run in $O(\lg m)$ steps with high probability, where $m=1+|\mathrm{rank}(x.key)-\mathrm{rank}(k)|$. Here, $\mathrm{rank}(k)$ refers to the rank (index) of a key $k$ in the sorted order of the dynamic set (when the procedure is invoked). "High probability" here is with respect to $m$; more precisely, for any positive integer $\alpha$, your algorithm should run in $O(\lg m)$ time with probability at least $1-\frac1{m^\alpha}$. (The constant implicit in this $O$ may depend on $\alpha$.) Analyze your algorithm carefully.

In writing your code, you may assume that the implementation of skip lists stores both a $-\infty$ at the front of each level as well as a $+\infty$ as the last element on each level.

Another query on a dynamic set is RANK-SEARCH$(x,r)$: given a node $x$ in the data structure and positive integer $r$, return a node $y$ in the data structure that contains the key whose rank is $\mathrm{rank}(x)+r$. You may assume that such a node appears in the data structure. Rank search can be implemented efficiently in skip lists, but this requires augmenting the nodes of the skip list with new information.

(b) Define a way of augmenting skip lists that will support efficient rank search, and show that your augmentation does not increase the usual high-probability order-of-magnitude time bounds for the SEARCH, INSERT, and DELETE operations.

(c) Now write pseudocode for RANK-SEARCH$(x,r)$ for skip lists. Again assume that all keys in the skip list are distinct. Assume that the given node $x$ is in the level-0 list, and the operation should return a node $y$ in the level-0 list.

Your algorithm should run in $O(\lg m)$ steps with high probability with respect to $m=r+1$. More precisely, for any positive integer $\alpha$, your algorithm should run in $O(\lg m)$ time with probability at least $1-\frac1{m^\alpha}$. Analyze your algorithm carefully.
:::
