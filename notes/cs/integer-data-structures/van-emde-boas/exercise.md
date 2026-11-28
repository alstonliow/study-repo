::: {.problem #prob-mit6046s15-3-q1 origin="external" source="mit6046s15-3-q1"}
**Variants on van Emde Boas**

For each of the following variants on the van Emde Boas data structures (presented in Lecture 4 and CLRS, Section 20.3), carefully describe what changes are needed to the pseudocode (from either lecture or the textbook), and analyze the costs of the vEB operations INSERT, DELETE, and SUCCESSOR, comparing them with the costs of the same operations for the original vEB structure.

(a) Instead of dividing the structure into $u^{1/2}$ groups of $u^{1/2}$ numbers each, use $u^{1/3}$ groups of $u^{2/3}$ numbers each.

(b) In addition to excluding the minimum element from lower-level vEB structures, also exclude the maximum element from lower-level vEB structures (and store it in the already existing max attribute). (Use the original division into $u^{1/2}$ groups of $u^{1/2}$ numbers here.)
:::

::: {.problem #prob-mit6851ps-6-q1 origin="external" source="mit6851ps-6-q1"}
**Concise van Emde Boas.** Develop and analyze a data structure that supports insert, delete, successor and predecessor in the word-RAM model in $O(\lg\lg u)$ worst-case time. Your data structure should use $O(u)$ bits of space. Note that the van Emde Boas data structure from lecture used $\Theta(u)$ words of space, and thus $\Theta(u\lg u)$ bits of space.
:::

::: {.problem #prob-mit6851ps-6-q2 origin="external" source="mit6851ps-6-q2"}
**Union-Split-Find.** Develop and analyze a word-RAM data structure to maintain a set of disjoint intervals of the form $[a,b)$ such that $a,b\in U$. Your data structure should support the following operations in $O(\lg\lg u)$ time:

* $\mathrm{make}(a,b)$: Create the interval $[a,b)$ (must not overlap existing intervals).
* $\mathrm{union}(a,b,c)$: Merge the adjacent intervals $[a,b)$ and $[b,c)$ into $[a,c)$.
* $\mathrm{split}(a,b,k)$: For $k\in[a,b)$, split the interval $[a,b)$ into $[a,k)$ and $[k,b)$.
* $\mathrm{find}(k)$: Return the interval $[a,b)$ that contains $k$, or report that no interval contains $k$.
:::

::: {.problem #prob-mit6851ps-7-q1 origin="external" source="mit6851ps-7-q1"}
**Speeding up static van Emde Boas.** In this problem we will develop a static data structure matching the $O\bigl(\lg\frac{w-\lg n}{a}\bigr)$ predecessor time bound mentioned in class.

1. Develop and analyze a data structure that supports successor and predecessor queries in the word-RAM model in $O(\lg(w-\lg n))$ worst-case time using $O(n)$ space.
2. Develop and analyze a data structure that supports successor and predecessor queries in the word-RAM model in $O\bigl(\lg\frac{w}{\lg\lg n}\bigr)$ worst-case time using $O(n\log n)$ space.

Neither of your data structures needs to support insertions or deletions.
:::
