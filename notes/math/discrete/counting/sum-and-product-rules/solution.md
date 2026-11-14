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
