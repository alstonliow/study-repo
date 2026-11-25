<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6006-17-q1" status="draft"}
Let times be $0,\dots,n-1$, let $t_i$ be the set of arrows that must be down at time $i$ (newly pressed or held), and let $d(t,p,t',p')$ be the difficulty of a move from foot positions $p$ to $p'$.

1. *State.* A position is $p=(p_L,p_R)$ with $p_L,p_R\in\{\text{up},\text{down},\text{left},\text{right},\text{middle}\}$ and $p_L\ne p_R$ unless both are in the middle. There are at most $25$ positions.

2. *Subproblems.* $x(i,p)$ is the least total difficulty for times $i,\dots,n-1$, given that the feet are at $p$ at time $i$. Here $p$ is *valid* at time $i$ if every arrow of $t_i$ is under a foot.

3. *Relation.* A move from $p$ at time $i$ to $p'$ at time $i+1$ is *allowed* if $p'$ is valid at time $i+1$, and every foot that is on an arrow held across $i\to i+1$ stays on it. Then $x(i,p)=\min\{d(t_i,p,t_{i+1},p')+x(i+1,p'):p'\text{ allowed}\}$. The positions say where each foot is, so a hold can be checked locally. Without that state, a suffix subproblem would not know which foot is still busy.

4. *Order and base.* Decreasing $i$. $x(n-1,p)=0$ for valid $p$, and $\infty$ for invalid $p$.

5. *Original problem.* $\min\{x(0,p):p\text{ valid at time }0\}$, with parent pointers to read off the steps.

6. *Time.* $25n$ subproblems with at most $25$ candidates each: $\Theta(n)$.
:::
