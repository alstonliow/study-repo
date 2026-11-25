<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046-10-q1" status="draft"}
1. *Fill the table.* Compute all $L(i,j)$ bottom-up in increasing $j-i$ (or memoize the recursion), with $L(i,i)=1$ and $L(i,i-1)=0$: $O(n^2)$ time and space.

2. *Walk back.* Start with $i=1$, $j=n$ and an empty list `left`. While $i\le j$:
   - if $i=j$: record the middle letter $X[i]$ and stop;
   - if $X[i]=X[j]$: append $X[i]$ to `left`, and set $i\leftarrow i+1$, $j\leftarrow j-1$;
   - otherwise move to the larger of $L(i+1,j)$ and $L(i,j-1)$ (either one if they are equal).

3. *Output.* `left`, then the middle letter if any, then `left` reversed.

4. *Correctness.* At each step the walk moves to a subproblem that attains $L(i,j)$ in the relation. Each matched pair adds $2$, and the middle letter adds $1$. So the output is a palindrome, it is a subsequence of $X$ (the indices used increase on the left and decrease on the right), and its length is $L(1,n)$.

5. *Time.* The walk takes $O(n)$ steps after the $O(n^2)$ table.
:::
