::: {.problem #prob-mit6046-1-q1 origin="external" source="mit6046-1-q1"}
Total running time is $O(n^2)$ since we need $O(n)$ time to solve each sub-problem. Turns out that we can actually reduce the overall complexity to $O(n\log n)$. We leave this as an exercise.

*Note (these notes):* This refers to weighted interval scheduling (@exm-weighted-interval-scheduling) solved with the subproblems $R^x=\{j\in R: s(j)\ge x\}$ (requests starting at or after $x$) and the relation $\mathrm{opt}(R)=\max_{1\le i\le n}\bigl(w(i)+\mathrm{opt}(R^{f(i)})\bigr)$, where request $i$ is tried as the first request chosen.
:::
