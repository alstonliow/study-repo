<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-sequences-13 origin="external" source="fit1058-cn-6.16-q13"}
(a) How can the number $\underbrace{99\cdots99}_{n\text{ digits}}$ be
    interpreted as the sum of a finite geometric series? What are $a$,
    $r$ and $n$? What does the formula for $S_n$ give? Does this make
    sense?

(b) What about the number $0.999999\ldots$?
:::

::: {.problem #prob-sequences-14 origin="external" source="fit1058-cn-6.16-q14"}
(a) Using (6.47) $\bigl(H_n\le\log_e n+\gamma+\frac1{2n}\bigr)$, show
    that $H_n=O(\log n)$.

(b) Hence prove that
    $$\frac n1+\frac n2+\frac n3+\cdots+\frac n{n-1}+\frac nn
                      = O(n\log n).$$
:::

::: {.problem #prob-sequences-15 origin="external" source="fit1058-cn-6.16-q15"}
Recall $(g_n)$ from Exercise 5, with closed form
$g_n=\sum_{i=1}^n\log i$.

(a) Use Exercise 5 and (6.47) to show that
    $g_n\le n\log n-n+\log n+c$ for some positive constant $c$.

(b) Hence show that $g_n=O(n\log n)$.

(c) Use (a) to show that $e^{g_n}\le\bigl(\frac ne\bigr)^n n\,e^c$.

(d) Prove that $e^{g_n}=n!$.

(e) Hence show that $n!=O\Bigl(\bigl(\frac ne\bigr)^n n\Bigr)$.
:::
