<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046-1-q1" status="draft"}
1. *Sort.* Sort the requests by start time, $s(1)\le\dots\le s(n)$, in $O(n\log n)$. Every $R^x$ is then a suffix $\{k,k+1,\dots,n\}$; write $\mathrm{opt}(k)$ for its value, with $\mathrm{opt}(n+1)=0$.

2. *Find the next request.* For each $i$, let $\mathrm{next}(i)$ be the first index $j$ with $s(j)\ge f(i)$, so that $R^{f(i)}$ is the suffix starting at $\mathrm{next}(i)$. Binary search finds it in $O(\log n)$: $O(n\log n)$ for all $i$.

3. *A constant-work relation.* In the suffix starting at $k$, either request $k$ is not chosen, and the best is $\mathrm{opt}(k+1)$; or it is chosen, and it is then the first request, so the best is $w(k)+\mathrm{opt}(\mathrm{next}(k))$. Hence $\mathrm{opt}(k)=\max\{\mathrm{opt}(k+1),\ w(k)+\mathrm{opt}(\mathrm{next}(k))\}$. This takes the same maximum as the lecture's relation over all possible first requests $i\ge k$, written recursively.

4. *Time.* $n$ subproblems in decreasing $k$ with $O(1)$ work each, after $O(n\log n)$ preprocessing: $O(n\log n)$ in total.
:::
