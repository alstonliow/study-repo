<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-3-q4" status="draft"}
*1. A schedule of time $55$.* Person 1 rides from $0$ to $54$ (time $9$), leaves the scooter and walks the remaining $46$: arrives at $55$. Person 3 walks to $54$ (time $27$), rides the scooter *back* to $46$ (time $1$, now $28$), leaves it and walks the $54$ to $B$ (time $27$): arrives at $55$. Person 2 walks to $46$ (time $46\ge28$), rides the $54$ to $B$ (time $9$): arrives at $55$.

*2. A lower bound.* First, positions can be clipped at $d$: replacing every trajectory $p(t)$ (people and scooter) by $\min(p(t),d)$ gives a valid schedule (speeds only drop, which waiting can emulate) with the same arrival times. So assume nothing goes beyond $B$. For person $i$ let $x_i,y_i$ be the total times riding forward and backward and $z_i$ the time walking forward; let $T$ be the finishing time. Then
$$\min T\ \text{ s.t. }\ w_iz_i+s_ix_i-s_iy_i\ge d,\quad x_i+y_i+z_i\le T\ \ (\forall i),\quad\sum_is_i(x_i-y_i)\le d,\quad x,y,z\ge0.$$
Each person must cover a net distance $d$ (walking backwards only hurts this inequality, so it may be ignored), within time $T$; and the scooter's net displacement, its final position, is at most $d$. Every schedule gives a feasible point, so the value is a lower bound. It has $3n+1$ variables and $2n+1$ constraints.

*3. The bound is $55$.* The schedule of 1 gives the feasible point $T=55$, $x_1=x_2=9$, $z_1=z_2=46$, $y_3=1$, $z_3=54$ (others $0$). To prove optimality, add the constraints with multipliers $0.3$ (distance and time of persons 1 and 2), $0.2$ and $0.4$ (distance and time of person 3) and $0.25$ (scooter): every variable's coefficient in $\sum\lambda_i(\text{distance}_i)-0.25\,(\text{scooter})$ is at most its coefficient in $\sum\mu_i(\text{time}_i)$ (e.g. $x_1$: $(0.3-0.25)\cdot6=0.3\le0.3$; $y_3$: $(0.25-0.2)\cdot8=0.4\le0.4$; $z_3$: $0.2\cdot2\le0.4$), and $\sum\mu_i=1$. This yields
$$T\ge(0.3+0.3+0.2)\,d-0.25\,d=55.$$
So $55$ is optimal, both for the LP and for the team.
:::
