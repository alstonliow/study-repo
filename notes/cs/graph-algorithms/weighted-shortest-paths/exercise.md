::: {.problem #prob-mit6006s20-6-q3 origin="external" source="mit6006s20-6-q3"}
**Dynamite Detonation**

Superspy Bames Jond is fleeing the alpine mountain lair of Silvertoe, the evil tycoon. Bames has stolen a pair of skis and a trail map listing the mountain's clearings and slopes ($n$ in total), and she wants to ski from the clearing $L$ by the lair to a clearing $S$ where a snowmobile awaits.

- Each **clearing** $c_i\in C$ has an integer **elevation** $e_i$ above sea level.
- Each **slope** $(c_i,c_j,\ell_{ij})$ connects a pair of clearings $c_i$ and $c_j$ with a **monotonic** trail (strictly decreasing or increasing in elevation) with positive integer length $\ell_{ij}$. Bames doesn't have time to ski uphill, so she will only traverse slopes so as to decrease her elevation.
- On her way up the mountain, Bames laced the mountain with **dynamite** at known locations $C_D\subset C$. Detonating the dynamite will immediately change the elevation of clearings $c_i\in C_D$ by a known amount, from $e_i$ to a lower elevation $e'_i<e_i$. The **detonator** exists at clearing $D\in C$ (where there is no dynamite). If she reaches clearing $D$, she can choose to detonate the dynamite before continuing on.

Given Bames' map and dynamite data, describe an $O(n)$-time algorithm to find the minimum distance she must ski to reach the snowmobile (possibly detonating the dynamite along the way).
:::
