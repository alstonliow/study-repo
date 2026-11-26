::: {.problem #prob-mit6854ps-5-q3 origin="external" source="mit6854ps-5-q3"}
In MAX 2SAT, we are given a collection $C_1,\dots,C_k$ of boolean clauses with at most two literals per clause. Each clause is thus either a literal or the disjunction of two literals drawn from a set of variables $\{x_1,x_2,\dots,x_n\}$. A literal is either a variable $x$ or its negation $\bar x$. The goal is to find an assignment of truth values to the variables $x_1,\dots,x_n$ that maximizes the number of satisfied clauses.

(a) Show that the algorithm which independently sets every $x_i$ to true with probability 0.5 is a randomized 0.5-approximation algorithm. (As usual, compute the expected number of satisfied clauses.)

(b) Consider the following linear program:
$$(LP)\qquad\begin{aligned}\text{Max}\ &\sum_{j=1}^kz_j\\\text{subject to:}\ &\sum_{i\in I_j^+}y_i+\sum_{i\in I_j^-}(1-y_i)\ge z_j&&j=1,\dots,k\\&0\le y_i\le1&&1\le i\le n\\&0\le z_j\le1&&j=1,\dots,k,\end{aligned}$$
where $I_j^+$ (resp. $I_j^-$) denotes the set of variables appearing unnegated (resp. negated) in $C_j$. For example, the clause $x_3\vee\bar x_5$ would give rise to the constraint $y_3+1-y_5\ge z_j$.

i. Show that the optimum value of this linear program is an upper bound on the optimum value of MAX 2SAT.

ii. Let $y^*,z^*$ denote the optimum solution of this linear program. Show that the algorithm which independently sets every $x_i$ to true with probability $y_i^*$ is a randomized 0.75-approximation algorithm.

(c) Consider now an approach similar to the one described in class for MAX CUT. Define a unit vector $v_0$ corresponding to "true" and also a unit vector $v_i$ for each variable $x_i$. Define the "value" of the clause or literal $x_i$ as $v(x_i)=\frac{1+v_0\cdot v_i}2$ and the value of $\bar x_i$ as $v(\bar x_i)=\frac{1-v_0\cdot v_i}2$. Observe that $v(x_i)$ is 1 if $v_0=v_i$, 0 if $v_0=-v_i$, and between 0 and 1 otherwise. For a clause with two literals, say $C=x_1\vee x_2$, define $v(C)$ as $(3+v_0\cdot v_1+v_0\cdot v_2-v_1\cdot v_2)/4$. The value of other clauses with two literals are similarly defined. Consider now the nonlinear program:
$$(NLP)\qquad\text{Maximize}\ \sum_{j=1}^kv(C_j)\quad\text{subject to: }v_i\in S_n\quad i=0,1\dots,n.$$

i. Show that the optimum value of this nonlinear program is an upper bound on the optimum value of MAX 2SAT.

ii. Consider the algorithm which first solves this nonlinear program optimally, then generates a uniformly selected point $r$ on the unit sphere $S_n$, and sets $x_i$ to be true if $(v_0\cdot r)(v_i\cdot r)\ge0$. Using the analysis of the MAX CUT algorithm seen in class, show that this algorithm is a randomized 0.878-approximation algorithm for MAX 2SAT.

(d) Can you do better than 0.878?
:::
