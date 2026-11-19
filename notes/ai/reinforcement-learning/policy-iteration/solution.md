<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs188d-4-q1" status="draft"}
Numbers were computed exactly in Python.

(a) $T(s,\text{Stop},\text{Done})=1$ with $R(s,\text{Stop},\text{Done})=s$. $T(s,\text{Draw},s+c)=\frac13$ for each card $c\in\{2,3,4\}$ with $s+c\le5$, and the remaining probability goes to Done (a total of $6$ or more): $T(s,\text{Draw},\text{Done})=\frac13\cdot\#\{c: s+c\ge6\}$. Every Draw has reward $0$. So from $0$: to $2,3,4$; from $2$: to $4$ or $5$ ($\frac13$ each) or Done ($\frac13$); from $3$: to $5$ ($\frac13$) or Done; from $4$ and $5$: Done.

(b) With $V_k(s)=\max\bigl(s,\ \frac13\sum_{c}V_{k-1}(s+c)\bigr)$ (taking $V=0$ beyond $5$):

| | 0 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $V_0$ | 0 | 0 | 0 | 0 | 0 |
| $V_1$ | 0 | 2 | 3 | 4 | 5 |
| $V_2$ | 3 | 3 | 3 | 4 | 5 |
| $V_3$ | $\frac{10}{3}$ | 3 | 3 | 4 | 5 |
| $V_4$ | $\frac{10}{3}$ | 3 | 3 | 4 | 5 |

For instance $V_2(0)=\frac13(2+3+4)=3$, $V_2(2)=\max(2,\frac13(4+5))=3$ and $V_3(0)=\frac13(3+3+4)=\frac{10}{3}$.

(c) **Draw at $0$ and $2$, Stop at $3$, $4$, $5$.** At $2$, Draw is worth $\frac13(4+5+0)=3>2$; at $3$, Draw is worth $\frac13\cdot5=\frac53<3$; at $4$ and $5$ every draw busts.

(d) Evaluating $\pi_i$ (@thm-bellman-policy): $V(5)=0$ (Draw always busts), $V(4)=4$, $V(3)=\frac13V(5)=0$, $V(2)=2$, $V(0)=\frac13\bigl(V(2)+V(3)+V(4)\bigr)=\frac13(2+0+4)=2$. So $V^{\pi_i}=(2,2,0,4,0)$. Improvement (@def-policy-iteration): Draw is worth $\frac13\sum_cV^{\pi_i}(s+c)$, Stop is worth $s$: at $0$ Draw ($2>0$); at $2$ Draw gives $\frac13(4+0)=\frac43<2$, so Stop; at $3$, $4$, $5$ Stop. So $\pi_{i+1}=(\text{Draw},\text{Stop},\text{Stop},\text{Stop},\text{Stop})$; one more round would switch $2$ to Draw.
:::
