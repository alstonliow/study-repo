::: {.problem #prob-mit6854ps-4-q2 origin="external" source="mit6854ps-4-q2"}
Consider the linear program
$$\min\sum_jx_j$$
subject to
$$\sum_ja_{ij}x_j\ge1\quad\forall i,\qquad x_j\ge0\quad\forall j$$
and its dual
$$\max\sum_iy_i$$
subject to
$$\sum_ia_{ij}y_i\le1,\qquad x_i\ge0.$$
Assume that $A=[a_{ij}]$ is $m\times n$ and has only *nonnegative* entries.

In this problem, you'll have to show that a continuous algorithm solves (almost miraculously) the above pair of dual linear programs. We shall define a series of functions whose argument is the "time" and you'll show that some of these functions tend to the optimal solution as time goes to infinity. (For simplicity of notation, we drop the dependence on the time.)

- Initially, we let $s_j=0$ for $j=1,\dots,n$ and $LB=0$. The vector $s$ will (sort of) play the role of primal solution, and $LB$ the role of a lower bound on the objective function.
- At any time, let
$$t_i=e^{-\sum_ja_{ij}s_j}$$
for $i=1,\dots,m$. Also, let $d_j=\sum_ia_{ij}t_i$ for $j=1,\dots,n$, $D=\max_jd_j$ and $k$ be an index $j$ attaining the maximum in the definition of $D$. The algorithm continuously increases $s_k$.

Observe that when $s_k$ is increased, the vectors $t$ and $d$ as well as $D$ change also, implying that the index $k$ changes over time.

1. Let $\alpha=\min_i(\sum_ja_{ij}s_j)$. Let $x_j=s_j/\alpha$ for $j=1,\dots,n$, $y_i=t_i/D$ for $i=1,\dots,m$ and $LB=\max(LB,\frac{\sum_it_i}D)$. Show that $x$ is primal feasible, $y$ is dual feasible and $LB$ is a lower bound on the optimal value of both primal and dual.
2. Prove that
$$\sum_{i=1}^mt_i\le me^{-\sum_{j=1}^ns_j/LB}.$$
Hint: Show that initially the inequality holds and that it is also maintained whenever we have equality.
3. Deduce from (b) that $\sum_it_i$ tends to 0 as time goes to infinity.
4. Using (b), give an upper bound on the value of the primal solution $x$, and using (c), show that this upper bound tends to $LB$ as time goes to infinity. This shows that as time goes to infinity, both $x$ and $y$ tend to primal and dual optimal solutions!
:::

::: {.problem #prob-mit6854ps-4-q3 origin="external" source="mit6854ps-4-q3"}
We would like to find a function $f(n)$ such that, given any set of $n$ (possibly negative) numbers, $c_1,\cdots,c_n$, one cannot find more than $f(n)$ subsums of these numbers which decrease in absolute value by a factor of at least 2. More formally:

**Lemma 1** Let $c\in\mathbb R^n$ and $y_k\in\{0,1\}^n$ for $k=1,\dots,q$ such that $2|y_{k+1}^Tc|\le|y_k^Tc|$ for $k=1,\dots,q-1$. Assume that $y_q^Tc=1$. Then $q\le f(n)$.

Using linear programming, you are asked to prove that $f(n)=O(n\log n)$.

1. Given a vector $c$ and a set of $q$ subsums satisfying the hypothesis of the Lemma, write a set of inequalities in the variables $x_i\ge0$, $i=1\dots n$, such that $x_i=|c_i|$ is a feasible vector, and for any feasible vector $x'$ there is a corresponding vector $c'$ satisfying the hypothesis of the Lemma for the same set of subsums.
2. Prove that there must exist a vector $c'$ satisfying the hypothesis of the Lemma, with $c'$ of the form $(d_1/d,d_2/d,\dots,d_n/d)$ for some integers $|d|,|d_1|,\dots,|d_n|=2^{O(n\log n)}$.
3. Deduce that $f(n)=O(n\log n)$.
4. (Not part of the problem set; only for those who find the problem sets too easy...) Show that $f(n)=\Omega(n\log n)$ (as a tiny step, can you find a set of numbers such that $f(n)>n$?).
:::
