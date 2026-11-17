<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-2-q4" status="draft"}
Call $C$ *acceptable* to $J$ if $J$ prefers $C$ to being unmatched, and similarly for candidates. The five conditions say: everyone's partner is acceptable, and there is no pair $(J,C)$, not matched together, in which each prefers the other to its current status (partner or being unmatched). We call such a pair *blocking*.

(a) We give a direct proof with a modified propose-and-reject algorithm instead of the hint's virtual entities.

1. Each job proposes, in order, only to candidates acceptable to it; a candidate keeps the best offer she finds acceptable and rejects all others, including unacceptable ones. A job that has been rejected by all its acceptable candidates stops and stays unmatched.

2. Every day without the end, some job crosses a candidate off its list, so the algorithm stops (@lem-propose-and-reject-halts). Offers only go to acceptable candidates and are only held when acceptable, so every final partner is acceptable to both sides.

3. The improvement lemma still holds: once $C$ holds an offer, she holds one at least as good ever after, by the same proof (@lem-improvement).

4. Suppose $(J,C)$ were blocking. Then $C$ is acceptable to $J$ and $J$ prefers $C$ to its final status. $J$ proposes in order of preference and only stops when its list is used up, so it proposed to $C$ before ending with its final status, and $C$ rejected it.

5. $C$ rejected $J$ either because $J$ is unacceptable to her (then $(J,C)$ is not blocking) or for a better offer, after which by step 3 she always holds something better than $J$ (then she does not prefer $J$). Either way $(J,C)$ is not blocking, so the output is stable.

(b)

1. Suppose $S$ and $T$ are stable and some entity $x_0$ is matched in $T$ but unmatched in $S$. Let $y_0$ be its partner in $T$.

2. $x_0$ finds $y_0$ acceptable ($T$ is stable), so $x_0$ prefers $y_0$ to being unmatched, its status in $S$. Since $S$ is stable, $(x_0,y_0)$ is not blocking in $S$: $y_0$ is matched in $S$, to some $x_1$, and prefers $x_1$ to $x_0$ (if $y_0$ were unmatched in $S$, it would prefer the acceptable $x_0$).

3. Now look at $x_1$. It is on the same side as $x_0$, and $y_0$ prefers $x_1$ to its $T$-partner $x_0$. Since $T$ is stable, $(x_1,y_0)$ is not blocking in $T$: $x_1$ is matched in $T$, to some $y_1$, and prefers $y_1$ to $y_0$ (being unmatched would be worse than the acceptable $y_0$).

4. Repeating steps 2–3 with $(x_1,y_1)$ in place of $(x_0,y_0)$ gives $x_2,y_2,\dots$ without end: each $y_k$ is matched in $S$ to $x_{k+1}$, and each $x_{k+1}$ is matched in $T$ to $y_{k+1}$.

5. These entities are all different. Consider the graph whose edges are the pairs of $S$ and of $T$. Every entity has at most one edge of each matching, and $x_0$ has only its $T$-edge, so the component of $x_0$ is a path starting at $x_0$, and the walk $x_0,y_0,x_1,y_1,\dots$ follows it, alternating $T$- and $S$-edges, never stopping and never turning back ($y_k\ne y_{k+1}$ because $x_{k+1}$ strictly prefers $y_{k+1}$). A path in a finite graph cannot go on forever, a contradiction.

So an entity unmatched in one stable matching is unmatched in all of them.
:::

::: {.solution for="prob-cs70hw-2-q5" status="draft"}
Here the $n$ applicants propose and the $n$ jobs reject.

(a) True; the value is $n$. Let $D_j=\sum_MP_j(M)-\sum_WR_j(W)$; we show $D_j=n$ by induction on $j$.

1. *Day 1:* every applicant proposes to her first choice, so $\sum_MP_1(M)=n$, and nobody has been rejected yet, so $\sum_WR_1(W)=0$.

2. *Step:* let $r_j$ be the number of rejections on day $j$. Then $\sum_WR_{j+1}(W)=\sum_WR_j(W)+r_j$. Each rejected applicant proposes on day $j+1$ to the next job on her list, rank one higher, and every other applicant proposes to the same job again; so $\sum_MP_{j+1}(M)=\sum_MP_j(M)+r_j$. Hence $D_{j+1}=D_j=n$.

(b) True.

1. Suppose, for contradiction, that every applicant and every job ends with a partner in the bottom half of its list. Let $m$ be the last day.

2. Each applicant's final job has rank $P_m(M)\ge\frac n2+1$, so $\sum_MP_m(M)\ge n\bigl(\frac n2+1\bigr)$, and by (a), $\sum_WR_m(W)\ge\frac{n^2}2$.

3. If some job $W$ has rejected at least $\frac n2$ applicants, then by the improvement lemma (@lem-improvement, with the roles of the two sides exchanged) it ends with an applicant it prefers to all of them, who is therefore among its top $\frac n2$. So every job has rejected fewer than $\frac n2$ applicants, and $\sum_WR_m(W)<n\cdot\frac n2$.

4. Steps 2 and 3 contradict each other.
:::
