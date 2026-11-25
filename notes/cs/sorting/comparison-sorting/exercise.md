::: {.problem #prob-mit6006s20-2-q2 origin="external" source="mit6006s20-2-q2"}
**Sorting Sorts**

For each of the following scenarios, choose a sorting algorithm (from either selection sort, insertion sort, or merge sort) that best applies, and justify your choice. **Don't forget this! Your justification will be worth more points than your choice.** Each sort may be used more than once. If you find that multiple sorts could be appropriate for a scenario, identify their pros and cons, and choose the one that best suits the application. State and justify any assumptions you make. "Best" should be evaluated by asymptotic running time.

(a) Suppose you are given a data structure `D` maintaining an extrinsic order on $n$ items, supporting two standard sequence operations: `D.get_at(i)` in worst-case $\Theta(1)$ time and `D.set_at(i, x)` in worst-case $\Theta(n\log n)$ time. Choose an algorithm to best sort the items in `D` **in-place**.

(b) Suppose you have a static array $A$ containing pointers to $n$ comparable objects, pairs of which take $\Theta(\log n)$ time to compare. Choose an algorithm to best sort the pointers in $A$ so that the pointed-to objects appear in non-decreasing order.

(c) Suppose you have a **sorted array** $A$ containing $n$ integers, each of which fits into a single machine word. Now suppose someone performs some $\log\log n$ swaps between pairs of adjacent items in $A$ so that $A$ is no longer sorted. Choose an algorithm to best re-sort the integers in $A$.
:::
