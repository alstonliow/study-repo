::: {.problem #prob-mit6854ps-2-q3 origin="external" source="mit6854ps-2-q3"}
Consider a directed graph $G=(V,E)$ with a length function $l:E\to\mathbb Z$ and a specified source vertex $s\in V$. The Bellman-Ford shortest path algorithm computes the shortest path lengths $d(v)$ between $s$ and every vertex $v\in V$, assuming that $G$ has no directed cycle of negative length (otherwise the problem is NP-hard). Here is a description of this algorithm:

> The Bellman-Ford algorithm computes $d(v)$ by computing $d_k(v)$ = the shortest walk (a walk is like a path except that vertices might be repeated) between $s$ and $v$ using exactly $k$ edges. $d_k(v)$ can be computed by the recurrence
> $$d_k(v)=\min_{(w,v)\in E}\left[d_{k-1}(w)+l(w,v)\right].$$
> Let $h_l(v)=\min_{k=1,\dots,l}d_k(v)$. It can be shown that if the graph has no negative cycle then $h_{n-1}(v)=d(v)$ for all $v\in V$. Moreover, the graph has no negative cycle iff, for all $v$, $d_n(v)\ge h_{n-1}(v)$.

(You are not required to prove any of the above facts.)

(a) Let $\mu^*$ be the minimum average length of a directed cycle $C$ of $G$, i.e.,
$$\mu^*(G)=\min_{\text{directed cycles }C}\mu(C)=\min_C\frac{\sum_{(u,v)\in C}l(u,v)}{|C|}.$$
Using the Bellman-Ford algorithm, show how to compute $\mu^*$ in $O(nm)$ time.

(Hint: Use the fact that if we decrease the length of each edge by $\mu$ the average length of any cycle decreases by $\mu$.)

(b) Can you find the cycle $C$ with $\mu(C)=\mu^*$ using only $O(n^2)$ additional time? (In other words, suppose you are given all the values that the Bellman-Ford algorithm computes. Can you find a minimum mean cost cycle using this information in $O(n^2)$?)
:::

::: {.problem #prob-mit6854ps-2-q4 origin="external" source="mit6854ps-2-q4"}
In this problem, we will propose another way to solve the minimum mean cost cycle problem. The resulting algorithm will be quite slow, but the technique is widely applicable (and for other problems, this will give the fastest known approach). The problem of finding $\mu^*$ is equivalent to the problem of finding the largest value of $\mu$ such that the graph with lengths $l_\mu(u,v)=l(u,v)-\mu$ has no negative cycles.

(a) Argue that for a given value of $\mu$, we can decide whether $\mu^*\ge\mu$ or $\mu^*<\mu$ by performing at most $O(A(m,n))$ additions of 2 numbers and $O(C(m,n))$ comparisons involving 2 numbers (and no other operations except control statements). Please state the values you can obtain for $A(m,n)$ and $C(m,n)$. Observe that, as we are performing only additions and comparisons, all the numbers involved are linear functions of the input lengths and $\mu$.

(b) Now suppose we run the above algorithm with $\mu$ equal to the unknown value $\mu^*$. We can easily perform the additions provided that we store all the numbers (including the inputs) as linear functions of $\mu^*$ (i.e. of the form $a+b\mu^*$). Explain how we can resolve the comparisons (even though we do not know $\mu^*$). (It is normal if the solution requires a fair amount of time to resolve each comparison.) As a function of $A(m,n)$ and $C(m,n)$, what is the total running time of your algorithm to compute $\mu^*$?
:::
