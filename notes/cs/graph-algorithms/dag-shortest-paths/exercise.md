::: {.problem #prob-mit6006s20-6-q3 origin="external" source="mit6006s20-6-q3"}
**Dynamite Detonation**

Superspy Bames Jond is fleeing the alpine mountain lair of Silvertoe, the evil tycoon. Bames has stolen a pair of skis and a trail map listing the mountain's clearings and slopes ($n$ in total), and she wants to ski from the clearing $L$ by the lair to a clearing $S$ where a snowmobile awaits.

- Each **clearing** $c_i\in C$ has an integer **elevation** $e_i$ above sea level.
- Each **slope** $(c_i,c_j,\ell_{ij})$ connects a pair of clearings $c_i$ and $c_j$ with a **monotonic** trail (strictly decreasing or increasing in elevation) with positive integer length $\ell_{ij}$. Bames doesn't have time to ski uphill, so she will only traverse slopes so as to decrease her elevation.
- On her way up the mountain, Bames laced the mountain with **dynamite** at known locations $C_D\subset C$. Detonating the dynamite will immediately change the elevation of clearings $c_i\in C_D$ by a known amount, from $e_i$ to a lower elevation $e'_i<e_i$. The **detonator** exists at clearing $D\in C$ (where there is no dynamite). If she reaches clearing $D$, she can choose to detonate the dynamite before continuing on.

Given Bames' map and dynamite data, describe an $O(n)$-time algorithm to find the minimum distance she must ski to reach the snowmobile (possibly detonating the dynamite along the way).
:::

::: {.problem #prob-mit6006r-11-q2 origin="external" source="mit6006r-11-q2"}
You have been recruited by MIT to take part in a new part time student initiative where you will take only one class per term. You don't care about graduating; all you really want to do is to take 19.854, Advanced Quantum Machine Learning on the Blockchain: Neural Interfaces, but are concerned because of its formidable set of prerequisites. MIT professors will allow you take any class as long as you have taken at least one of the class's prerequisites prior to taking the class. But passing a class without all the prerequsites is difficult. From a survey of your peers, you know for each class and prerequisite pair, how many hours of stress the class will demand. Given a list of classes, prerequisites, and surveyed stress values, describe a linear time algorithm to find a sequence of classes that minimizes the amount of stress required to take 19.854, never taking more than one prerequisite for any class. You may assume that every class is offered every semester.
:::
