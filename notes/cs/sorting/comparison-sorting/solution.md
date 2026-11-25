<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-2-q2" status="draft"}
(a) *Selection sort.* Writes are expensive and reads cheap. Selection sort makes $\Theta(n^2)$ reads but only $O(n)$ swaps, that is $O(n)$ calls of `set_at`, costing $O(n\cdot n\log n)$; total $\Theta(n^2\log n)$. Insertion sort may do $\Theta(n^2)$ swaps, costing $\Theta(n^3\log n)$, and merge sort is not in place (and writes $\Theta(n\log n)$ times anyway, $\Theta(n^2\log^2n)$).

(b) *Merge sort.* Now comparisons are expensive and moving a pointer is cheap. Merge sort makes $O(n\log n)$ comparisons, $O(n\log^2n)$ time in total; selection and insertion sort make $\Theta(n^2)$ comparisons in the worst case, $\Theta(n^2\log n)$.

(c) *Insertion sort.* Each adjacent swap creates at most one inversion, so $A$ has at most $\log\log n$ inversions. Insertion sort does $O(n)$ comparisons plus one swap per inversion (@sec-cs-sorting-comparison-sorting), so it runs in $O(n+\log\log n)=O(n)$ time, while merge sort takes $\Theta(n\log n)$ and selection sort $\Theta(n^2)$ regardless of the input.
:::
