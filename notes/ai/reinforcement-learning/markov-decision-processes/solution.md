<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-4-q2" status="draft"}
Assume $0<\gamma<1$. Make $o$ an end state and, for $s\in\text{States}$ and $a\in\text{Actions}(s)$:
$$T'(s,a,s')=\gamma\,T(s,a,s')\quad(s'\in\text{States}),\qquad T'(s,a,o)=1-\gamma,$$
$$\text{Reward}'(s,a,s')=\frac{\text{Reward}(s,a,s')}{\gamma}\quad(s'\in\text{States}),\qquad \text{Reward}'(s,a,o)=0.$$
End states of the original MDP stay end states.

1. $T'(s,a,\cdot)$ is a distribution: $\gamma\sum_{s'}T(s,a,s')+(1-\gamma)=1$.
2. The new optimal values satisfy, with $\gamma'=1$ and $V'(o)=0$,
$$V'(s)=\max_a\Big[\sum_{s'\in\text{States}}\gamma T(s,a,s')\Big(\frac{\text{Reward}(s,a,s')}{\gamma}+V'(s')\Big)+(1-\gamma)(0+0)\Big].$$
3. Simplifying the bracket gives $\sum_{s'}T(s,a,s')\big(\text{Reward}(s,a,s')+\gamma V'(s')\big)$, which is the original recurrence for $V^*$.
4. Both recurrences have the same unique solution (the original one is a $\gamma$-contraction), so $V'(s)=V^*(s)$ for all $s\in\text{States}$.

Interpretation: discounting is the same as continuing with probability $\gamma$ and stopping (in $o$, with no further reward) with probability $1-\gamma$.
:::
