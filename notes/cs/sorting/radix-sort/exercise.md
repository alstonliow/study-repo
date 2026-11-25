::: {.problem #prob-mit6006s20-3-q3 origin="external" source="mit6006s20-3-q3"}
**The Cold is Not Bothersome Anyway**

Ice cores are long cylindrical plugs drilled out of deep glaciers, which are accumulations of snow piled on top of each other and compressed into ice. Scientists can divide an ice core into distinct slices, each representing one year of deposits. For each of the following scenerios, describe an **efficient** algorithm to sort $n$ slices collected from multiple ice cores. Justify your answers.

(a) Every ice core is given a unique *core identifier* for bookkeeping, which is a string of exactly $16\lceil\log_4(\sqrt n)\rceil$ ASCII characters. Sort the slices by core identifier.

(b) The deepest ice cores in the database are up to 800,000 years old. Sort the slices by their *age*: the integer number of years since the slice was formed.

(c) Variation in the amount of snowfall each year will cause a glacier to accumulate at different rates over time. Sort the slices by *thickness*, a rational number of centimeters of the form $m/n^3$ between 0 and 4, where $m$ is an integer.

(d) Elna of Northendelle has discovered that water has *memory*, but is unable to quantify the memory of a given slice. Luckily, given two slices, she can distinguish which has more memory in $O(1)$ time using her "two-finger algorithm" (touching the slices with her two index fingers). Sort the slices by memory.

(Footnotes: By "efficient", we mean that asymptotically faster correct algorithms will receive more points than slower ones. You may assume a string of $k$ ASCII characters is a pointer to a contiguous sequence of $k$ bytes in memory, where each byte stores an integer from 0 to 127 inclusive representing an ASCII character.)
:::

::: {.problem #prob-mit6006s20-3-q4 origin="external" source="mit6006s20-3-q4"}
**Pushing Paper**

Farryl Dilbin is a forklift operator at Munder Difflin paper company's central warehouse. She needs to ship exactly $r$ reams of paper to a customer. In the warehouse are $n$ boxes of paper, each one foot in width, lined up side-by-side covering an $n$-foot wall. Each box contains a known positive integer number of reams, where **no two boxes contain the same number of reams**. Let $B=(b_0,\dots,b_{n-1})$ be the number of reams per box, where box $i$ located $i$ feet from the left end of the wall contains $b_i$ reams of paper, where $b_i\ne b_j$ for all $i\ne j$. To minimize her effort, Pharryl wants to know whether there is a ***close*** pair $(b_i,b_j)$ of boxes, meaning that $|i-j|<n/10$, that will ***fulfill*** order $r$, meaning that $b_i+b_j=r$.

(a) Given $B$ and $r$, describe an expected $O(n)$-time algorithm to determine whether $B$ contains a close pair that fulfills order $r$.

(b) Now suppose that $r<n^2$. Describe a worst-case $O(n)$-time algorithm to determine whether $B$ contains a close pair that fulfills order $r$.
:::
