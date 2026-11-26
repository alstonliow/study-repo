<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit18433-1-q9" status="draft"}
Let $x^*$ be an optimal solution of the relaxation that is integral. It satisfies all constraints of the integer program, so $Z_{IP}\le c^{\mathsf T}x^*=Z_{LP}$. The integer program has more constraints, so $Z_{LP}\le Z_{IP}$. Hence $c^{\mathsf T}x^*=Z_{IP}$ and $x^*$ is optimal for the integer program.
:::

::: {.solution for="prob-mit18433-1-q10" status="draft"}
Minimise $x_1+x_2+x_3$ subject to $x_1+x_2\ge1$, $x_2+x_3\ge1$, $x_1+x_3\ge1$, $x\ge0$, $x$ integral: the minimum vertex cover of a triangle. An integral solution needs two variables equal to $1$, so $Z_{IP}=2$. The relaxation has the feasible point $(\frac12,\frac12,\frac12)$ of value $\frac32$, and adding the three constraints shows $2(x_1+x_2+x_3)\ge3$, so $Z_{LP}=\frac32<Z_{IP}$.
:::

::: {.solution for="prob-mit18433-1-q11" status="draft"}
Implement one *phase* (from one augmentation to the next) as follows.

1. At the start of a phase compute $L$ by a search from the exposed vertices of $A$, and for each $j\in B\setminus L$ the slack $s_j=\min\{w_{ij}:i\in A\cap L\}$. This takes $O(n^2)$ time.

2. A dual update with $\delta=\min_js_j$ costs $O(n)$: change $u_i$ for $i\in A\cap L$ and $v_j$ for $j\in B\cap L$, and subtract $\delta$ from every $s_j$ ($j\in B\setminus L$), because $w_{ij}$ fell by $\delta$ for all $i\in A\cap L$. By the proof of @thm-hungarian-method, no vertex leaves $L$ and the matching stays tight, so $L$ need not be recomputed.

3. A vertex $j$ with $s_j=0$ now joins $L$. If it is exposed, we have found an augmenting path and the phase ends. Otherwise its partner $i$ joins $L$, and we update $s_{j'}\gets\min(s_{j'},w_{ij'})$ for all $j'\in B\setminus L$ in $O(n)$ time; we also follow any further tight edges from $i$, each new vertex of $B$ handled in the same way.

4. Each vertex of $B$ joins $L$ at most once per phase, so a phase has $O(n)$ dual updates and $O(n)$ insertions, each $O(n)$: $O(n^2)$ per phase. There are at most $n/2$ phases, so the total is $O(n^3)$.
:::

::: {.solution for="prob-mit18433-1-q15" status="draft"}
1. Let $F=\{ij:0<x^*_{ij}<1\}\ne\varnothing$. If a vertex has one edge in $F$, the other values at that vertex are $0$ or $1$ while the total is $1$, so it has a second edge in $F$. Thus every vertex touched by $F$ has degree at least $2$ in $F$, and $F$ contains a cycle $C$. It is even, as the graph is bipartite.

2. Let $d=+1$ on alternate edges of $C$ and $-1$ on the others. At each vertex of $C$ one edge gets $+1$ and one $-1$, so $x^*+\varepsilon d$ satisfies the equality constraints for every $\varepsilon$, and it is nonnegative for $|\varepsilon|\le\min_{e\in C}\min(x^*_e,1-x^*_e)$.

3. Since $x^*$ is optimal, $c^{\mathsf T}(x^*+\varepsilon d)\ge c^{\mathsf T}x^*$ for small $\varepsilon$ of both signs, so $c^{\mathsf T}d=0$ and every such $x^*+\varepsilon d$ is optimal.

4. Increase $|\varepsilon|$ (in either direction) until some edge of $C$ reaches $0$ or $1$. The new optimal solution has that edge integral, and only edges of $C$ changed, all of which were already non-integral. So it has fewer non-integral values, contradicting the choice of $x^*$. Hence $x^*$ is integral.
:::

::: {.solution for="prob-mit18433-1-q16" status="draft"}
We solved $5$ random instances for each $n\in\{10,50,100,200,400\}$ with an assignment solver (`scipy.optimize.linear_sum_assignment`, seed 2026). The mean optimal costs were about $1.47$, $1.73$, $1.51$, $1.66$, $1.65$; the spread shrinks as $n$ grows (for $n=400$ the values lay between $1.56$ and $1.72$).

So the optimal cost does *not* grow with $n$, although it is a sum of $n$ costs: each chosen cost is of order $1/n$. It seems to converge to about $1.64$–$1.65$. Indeed the limit of the expected value is $\zeta(2)=\pi^2/6\approx1.645$; this was conjectured by Mézard and Parisi and proved by Aldous (2001). For finite $n$ the expected value is exactly $\sum_{k=1}^n1/k^2$ (Parisi's conjecture, proved by Linusson–Wästlund and by Nair–Prabhakar–Sharma).
:::

::: {.solution for="prob-mit18433-1-q17" status="draft"}
No. Fix a small $\varepsilon>0$ and build point sets $F_k$ with $2^k$ points of $A$ and $2^k$ of $B$ on an interval of length $L_k$.

1. $F_0$: a point of $B$ at $0$ and a point of $A$ at $1$; $L_0=1$. $F_{k+1}$: a copy of $F_k$, then, at distance $g_k=(1-\varepsilon)L_k$ to its right, the mirror image of $F_k$ with the two colours exchanged. So $L_{k+1}=2L_k+g_k$. In $F_k$ the leftmost point is in $B$ and the rightmost in $A$; the mirrored copy therefore starts with a point of $B$.

2. *Claim:* greedy on $F_k$ matches the leftmost and rightmost points last, and all its earlier pairs have length less than $(1-\varepsilon)L_k$. True for $k=0$. For $F_{k+1}$: any pair across the two copies has length at least $g_k$, with equality only for the two inner end points; pairs inside a copy that greedy uses before its last step have length less than $g_k$ by induction. So greedy first performs all non-final steps inside both copies. Then four points remain: the outer ends of both copies (left end $B$, right end $A$) and the inner ends (an $A$ and a $B$ at distance $g_k$). The pair of inner ends, of length $g_k<L_k$, is the shortest admissible pair; the outer ends are matched last, at distance $L_{k+1}$. All pairs before that have length at most $g_k<(1-\varepsilon)L_{k+1}$.

3. *Costs.* Let $G_k$ be the greedy cost. Then $G_{k+1}=2(G_k-L_k)+g_k+L_{k+1}$. Letting $\varepsilon\to0$ (for fixed $k$ the costs are continuous in $\varepsilon$), $L_k\to3^k$ and $G_k\to2\cdot3^k-2^k$; for example $G_1\to4$, $G_2\to14$, $G_3\to46$, which we confirmed by simulation.

4. The optimum is at most $2^k$: the $2^k$ original pairs of $F_0$-copies have length $1$ and each consists of one point of $A$ and one of $B$.

5. So with $n=2^k$ the ratio is at least about $2(3/2)^k-1=2n^{\log_2(3/2)}-1\to\infty$. For a fixed small $\varepsilon$ the same recursion still gives a ratio growing like $\big(\frac{3-\varepsilon}2\big)^k$.
:::
