<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-sets-19" status="draft"}
Not in general. Take complements in a universal set $U$, so that
$\overline{A\times B}$ is the complement within $U\times U$.

1. Write out both sets:
   $$\overline A\times\overline B = \{(a,b) : a\notin A \text{ and } b\notin B\},$$
   $$\overline{A\times B} = \{(a,b) : a\notin A \text{ or } b\notin B\}.$$

2. "and" implies "or", so in general
   $$\overline A\times\overline B\subseteq\overline{A\times B}.$$

3. The difference consists of the pairs with exactly one coordinate outside
   its set:
   $$\overline{A\times B}\setminus(\overline A\times\overline B)
     = (A\times\overline B)\cup(\overline A\times B).$$

4. *Example.* Let $U=\{1,2\}$ and $A=B=\{1\}$. Then $(1,2)\in\overline{A\times B}$,
   but $(1,2)\notin\overline A\times\overline B$ because $1\in A$.

5. *When equality holds.* By step 3 we need $A\times\overline B = \emptyset$
   and $\overline A\times B=\emptyset$. A product is empty exactly when one
   factor is empty, so we need
   ($A=\emptyset$ or $B=U$) and ($A=U$ or $B=\emptyset$).

6. For nonempty $U$, the sets $\emptyset$ and $U$ are different, so this
   leaves exactly two cases:
   $$A = B = \emptyset \qquad\text{or}\qquad A = B = U.$$
   (The mixed cases fail. For example, $A=\emptyset$ and $B=U$ give
   $\overline{A\times B} = U\times U$ but $\overline A\times\overline B = U\times\emptyset = \emptyset$.)
:::
