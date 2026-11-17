<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-3-q3" status="draft"}
(a) *Radix sort, $O(n)$.* An identifier has $L=16\lceil\frac14\log_2n\rceil\le4\log_2n+16$ bytes, that is $O(\log n)$ bits, stored contiguously. Read as one integer (big-endian, so that numeric order is the lexicographic order of the strings), it occupies $O(1)$ words because $w\ge\log_2n$, and it is less than $2^{8L}\le2^{128}n^{32}$. So the keys are polynomially bounded and radix sort (@thm-radix-sort) takes $O(n)$ time.

(b) *Counting sort, $O(n)$.* Ages are integers in $\{0,\dots,800\,000\}$, a range of constant size, so counting sort (@prp-counting-sort) takes $O(n+800\,001)=O(n)$ time.

(c) *Radix sort, $O(n)$.* Sorting by $m/n^3$ is sorting by the integer $m\in\{0,\dots,4n^3\}$, which is polynomially bounded; radix sort takes $O(n)$ time.

(d) *Merge sort, $O(n\log n)$.* We can only compare slices, so the comparison lower bound $\Omega(n\log n)$ (@thm-comparison-sort-lower-bound) applies, and merge sort meets it.
:::

::: {.solution for="prob-mit6006s20-3-q4" status="draft"}
Since the $b_i$ are distinct, each box $i$ has at most one possible partner: the box with $b_j=r-b_i$.

(a) Insert the pairs $b_i\mapsto i$ into a hash table, in expected $O(n)$ time. Then for each $i$ look up $r-b_i$; if it is present at index $j\ne i$ with $|i-j|<n/10$, answer yes. Otherwise answer no. That is $n$ lookups of $O(1)$ expected time each.

(b) Boxes with $b_i\ge r$ cannot be in a fulfilling pair (all counts are positive), so discard them; the rest have $b_i<r<n^2$. Radix sort the pairs $(b_i,i)$ by $b_i$ in worst-case $O(n)$ time (@thm-radix-sort). Then find all pairs with sum $r$ by two fingers: a finger $x$ at the smallest value and $y$ at the largest; while $x<y$, if $b_x+b_y=r$ check $|i_x-i_y|<n/10$ and move both fingers inwards, if the sum is smaller move $x$ right, and if larger move $y$ left. Each step discards a value that has no partner among the values between the fingers, so every fulfilling pair is examined, in $O(n)$ steps.
:::
