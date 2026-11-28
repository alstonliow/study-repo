::: {.problem #prob-mit6851ps-4-q1 origin="external" source="mit6851ps-4-q1"}
**Cache-oblivious median finding.** Given an unordered array of $N$ elements, develop and analyze a cache-oblivious algorithm to find the median of the array in $O(\lceil N/B\rceil)$ memory transfers. In your solution, you may assume knowledge of the standard median-of-medians deterministic selection algorithm.
:::

::: {.problem #prob-mit6851ps-4-q2 origin="external" source="mit6851ps-4-q2"}
**Cache-oblivious queue.** Develop and analyze a cache-oblivious FIFO queue. Both the enqueue and the dequeue operation should take $O(1/B)$ amortized memory transfers. Your data structure should only use external memory indices in $\{0,1,\cdots,O(N)\}$, where $N$ is the maximum number of elements stored in the queue at once.
:::

::: {.problem #prob-mit6851ps-5-q1 origin="external" source="mit6851ps-5-q1"}
**Orthogonal line segment intersection.** Given a set of $N$ horizontal and vertical line segments, develop and analyze a cache-oblivious algorithm to find the number of vertical segments intersecting each horizontal segment in $O\bigl(\frac NB\log_{M/B}\frac NB\bigr)$ memory transfers. You may assume that the endpoints of any two different line segments do not have the same $x$ or $y$ value.
:::

::: {.problem #prob-mit6851ps-5-q2 origin="external" source="mit6851ps-5-q2"}
**Line segment visibility from a point.** Given a set of $N$ line segments and a point $p$, we would like to find the clockwise list of partial line segments visible from $p$. A (partial) line segment is visible from $p$ if, for any point along the segment, a line can be drawn from that point to $p$ without intersecting any other line segment. If a line segment is only partially visible from $p$, then only the segment that is visible should appear in the output list. A single line segment may contain many partial segments in the output list. Develop and analyze a cache-oblivious algorithm to accomplish this in $O\bigl(\frac NB\log_{M/B}\frac NB+\frac KB\bigr)$ memory transfers, where $K$ is the size of the output. You may assume that no two points in the input lie along the same line to $p$, and that no two line segments intersect.
:::
