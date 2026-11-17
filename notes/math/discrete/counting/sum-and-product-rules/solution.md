<!-- Draft solutions (status="draft") written by Claude with the FIT1058 sample
     solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-counting-01" status="draft"}
(a) Each pass of the outer loop does $bcd$ beeps in the $j$-$k$-$l$ nest and
    $e(f+g+h)$ in the $m$ loop. So the total is
    $$a\bigl(bcd + e(f+g+h)\bigr).$$

(b) $abcd$ is a product of four $O(n)$ quantities, and $ae(f+g+h)$ is
    $O(n^3)$. So the number of beeps is $O(n^4)$.
:::

::: {.solution for="prob-counting-03" status="draft"}
(a) $6\cdot6 = 36$.

(b) The outcomes with both numbers equal are $6$. The remaining $30$ split
    evenly between "first less" and "first greater", so $15$.

(c) $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$: $6$.

(d) $3\cdot3 = 9$.

(e) $5\cdot5 = 25$.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-6-q6" status="draft"}
Maru's points are $\sum_{i\in W}i$ for the set $W\subseteq\{1,\dots,10\}$ of games he wins; all $10$ games give $55$.

(a) He needs at least $28$ points, so the games he loses (one GG each) may total at most $55-28=27$ points. To lose as many games as possible, lose the cheapest: $1+2+\dots+6=21\le27$ but $1+\dots+7=28>27$. So at most $6$ GGs (lose games $1$–$6$, win $7$–$10$: $34$ points).

(b) The map $W\mapsto\{1,\dots,10\}\setminus W$ is a bijection on the $2^{10}$ subsets that sends a total $S$ to $55-S$. Since $55$ is odd, exactly one of $S$ and $55-S$ is at least $28$. So exactly half the subsets work: $2^9=512$ ways.
:::

::: {.solution for="prob-cs70hw-7-q2" status="draft"}
A $5$-digit palindrome $d_1d_2d_3d_2d_1$ is determined by its first three digits: $d_1\ne0$ gives $9$ choices, $d_2$ and $d_3$ give $10$ each. By the product rule there are $9\cdot10\cdot10=900$.
:::
