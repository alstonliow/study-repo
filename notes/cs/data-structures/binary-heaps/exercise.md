::: {.problem #prob-mit6006s20-4-q2 origin="external" source="mit6006s20-4-q2"}
**Heap Practice**

For each array below, draw it as a complete binary tree and state whether the tree is a max-heap, a min-heap, or neither. If the tree is neither, turn the tree into a min-heap by repeatedly swapping items that are adjacent in the tree. Communicate your swaps by drawing a sequence of trees, marking on each tree the pair that was swapped.

(a) `[4, 12, 8, 21, 14, 9, 17]`

(b) `[701, 253, 24, 229, 17, 22]`

(c) `[2, 9, 13, 8, 0, 2]`

(d) `[1, 3, 6, 5, 4, 9, 7]`

(Footnote: Recall from Lecture 8 that a binary tree is complete if it has exactly $2^i$ nodes of depth $i$ for all $i$ except possibly the largest, and at the largest depth, all nodes are as far left as possible.)
:::

::: {.problem #prob-mit6006s20-4-q3 origin="external" source="mit6006s20-4-q3"}
**Gardening Contest**

Gardening company Wonder-Grow sponsors a nation-wide gardening contest each year where they rate gardens around the country with a positive integer score. A garden is designated by a garden pair $(s_i,r_i)$, where $s_i$ is the garden's assigned score and $r_i$ is the garden's unique positive integer registration number.

(a) To support inclusion and reduce competition, Wonder-Grow wants to award identical trophies to the top $k$ gardens. Given an unsorted array $A$ of garden pairs and a positive integer $k\le|A|$, describe an $O(|A|+k\log|A|)$-time algorithm to return the registration numbers of $k$ gardens in $A$ with highest scores, breaking ties arbitrarily.

(b) Wonder-Grow decides to be more objective and award a trophy to every garden receiving a score strictly greater than a reference score $x$. Given a max-heap $A$ of garden pairs, describe an $O(n_x)$-time algorithm to return the registration numbers of all gardens with score larger than $x$, where $n_x$ is the number of gardens returned.

(Footnote: In this class, when an integer or string appears in an input, without listing an explicit bound on its size, you should assume that it is provided inside a constant number of machine words in the input.)
:::

::: {.problem #prob-mit6006s20-4-q4 origin="external" source="mit6006s20-4-q4"}
**Solar Supply**

Entrepreneur Bonty Murns owns a set $S$ of $n$ solar farms in the town of Fallmeadow. Each solar farm $(s_i,c_i)\in S$ is designated by a unique positive integer address $s_i$ and a farm capacity $c_i$: a positive integer corresponding to the maximum energy production rate the farm can support. Many buildings in Fallmeadow want power. A building $(b_j,d_j)$ is designated by a unique name string $b_j$ and a demand $d_j$: a positive integer corresponding to the building's energy consumption rate.

To receive power, a building in Fallmeadow must be connected to a single solar farm under the restriction that, for any solar farm $s_i$, the sum of demand from all the buildings connected to $s_i$ may not exceed the farm's capacity $c_i$. Describe a database supporting the following operations, and for each operation, specify whether your running time is worst-case, expected, and/or amortized.

| operation | specification |
|---|---|
| `initialize(S)` | Initialize database with a list $S=((s_0,c_0),\dots,(s_{n-1},c_{n-1}))$ corresponding to $n$ solar farms in $O(n)$ time. |
| `power_on(b_j, d_j)` | Connect a building with name $b_j$ and demand $d_j$ to any solar farm having available capacity at least $d_j$ in $O(\log n)$ time (or return that no such solar farm exists). |
| `power_off(b_j)` | Remove power from the building with name $b_j$ in $O(\log n)$ time. |
| `customers(s_i)` | Return the names of all buildings supplied by the farm at address $s_i$ in $O(k)$ time, where $k$ is the number of building names returned. |
:::
