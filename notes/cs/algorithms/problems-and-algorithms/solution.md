<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006s20-0-q6" status="draft"}
Scan once, keeping the length of the increasing run that ends at the current position, the best length seen so far, and how many runs have that length. A run ending at $i$ extends the run ending at $i-1$ exactly when $a_{i-1}<a_i$. Every longest increasing subarray is a maximal run, and a maximal run of the longest length is counted exactly once (when its length reaches the maximum at its last position; shorter prefixes of it have smaller length). Time $O(n)$, extra space $O(1)$.

```python
def count_long_subarrays(A):
    best, count, run = 0, 0, 0
    for i in range(len(A)):
        run = run + 1 if i > 0 and A[i - 1] < A[i] else 1
        if run > best:
            best, count = run, 1
        elif run == best:
            count += 1
    return count
```

On the example the runs have lengths $1,2,3,1,2,1,2,3,1$, so the maximum $3$ occurs twice.
:::
