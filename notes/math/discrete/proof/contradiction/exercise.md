<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-proofs-14 origin="external" source="fit1058-cn-3.15-q14"}
Identify the errors in the following “theorem” and “proof”.

**“Theorem.”** Every rational number is an integer.

**“Proof.”**

1.  We need to show that the sets $\mathbb{Z}$ and $\mathbb{Q}$ are equal.

2.  To prove two sets equal, we can prove the appropriate subset and
    superset relations.

3.  We first prove $\mathbb{Z}\subseteq\mathbb{Q}$.

4.  Let $x\in\mathbb{Z}$.

5.  Since $x$ is an integer, $x=\frac x1$.

6.  So $x$ is a quotient of integers.

7.  Therefore $x\in\mathbb{Q}$.

8.  So $\mathbb{Z}\subseteq\mathbb{Q}$.

9.  Now we need to prove the superset relation, the reverse of subset.

10. So we will prove that $\mathbb{Q}\supseteq\mathbb{Z}$.

11. Let $x\notin\mathbb{Q}$.

12. Then $x$ cannot be written as $\frac pq$ with $p,q$ integers.

13. So it certainly cannot be written in this form with $q=1$.

14. Therefore $x\notin\mathbb{Z}$.

15. So $\mathbb{Q}\supseteq\mathbb{Z}$.

16. Hence $\mathbb{Z}=\mathbb{Q}$. “$\square$”
:::

::: {.problem #prob-cs70-2-q2 origin="external" source="cs70-2.9-q2"}
Prove Lemma 2.2. (Hint: First try a direct proof. Then, try contraposition. Which proof approach is better suited to proving this lemma?)

*Note (these notes):* Lemma 2.2 of CS70 Note 2: if $a^2$ is even, then $a$ is even. It is used in @exm-contradiction-1.
:::

::: {.problem #prob-mit6042f10-2-q1 origin="external" source="mit6042f10-2-q1"}
Define a *3-chain* to be a (not necessarily contiguous) subsequence of three integers, which is either monotonically increasing or monotonically decreasing. We will show here that any sequence of five distinct integers will contain a 3-chain. Write the sequence as $a_1, a_2, a_3, a_4, a_5$. Note that a monotonically increasing sequences is one in which each term is greater than or equal to the previous term. Similarly, a monotonically decreasing sequence is one in which each term is less than or equal to the previous term. Lastly, a subsequence is a sequence derived from the original sequence by deleting some elements without changing the location of the remaining elements.

(a) Assume that $a_1 < a_2$. Show that if there is no 3-chain in our sequence, then $a_3$ must be less than $a_1$. (Hint: consider $a_4$!)

(b) Using the previous part, show that if $a_1 < a_2$ and there is no 3-chain in our sequence, then $a_3 < a_4 < a_2$.

(c) Assuming that $a_1 < a_2$ and $a_3 < a_4 < a_2$, show that any value of $a_5$ must result in a 3-chain.

(d) Using the previous parts, prove by contradiction that any sequence of five distinct integers must contain a 3-chain.
:::
