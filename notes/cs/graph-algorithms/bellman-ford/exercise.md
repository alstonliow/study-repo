::: {.problem #prob-mit6006s20-6-q2 origin="external" source="mit6006s20-6-q2"}
**Short Circuits**

Given a weighted directed graph $G=(V,E,w)$ and vertex $s\in V$, with the property that, for every vertex $v\in V$, some minimum-weight path from $s$ to $v$ traverses at most $k$ edges, describe an algorithm to find the shortest-path weight from $s$ to each $v\in V$ in $O(|V|+k|E|)$ time.
:::

::: {.problem #prob-mit6006s20-6-q4 origin="external" source="mit6006s20-6-q4"}
**Conservative Cycles**

In Wentonian physics, a force field acts on the motion of a particle by requiring a certain positive or negative amount of work to move along any path. A force field is conservative if the total sum of work is zero along every closed loop. Given a discrete force field represented by $n$ possible particle locations $\ell_i$ and $O(n)$ possible particle transitions, where transition $(\ell_i,\ell_j,w_{ij})$ moves a particle along a directed path from location $\ell_i$ to location $\ell_j$ requiring (positive or negative) integer work $w_{ij}$, describe an $O(n^2)$-time algorithm to determine whether the force field is conservative.

(Footnote: Note that a transition from $\ell_i$ to $\ell_j$ does not imply the existence of a transition from $\ell_j$ to $\ell_i$.)
:::

::: {.problem #prob-mit6006r-12-q1 origin="external" source="mit6006r-12-q1"}
Alice, Bob, and Casey are best friends who live in different corners of a rural school district. During the summer, they decide to meet every Saturday at some intersection in the district to play tee-ball. Each child will bike to the meeting location from their home along dirt roads. Each dirt road between road intersections has a level of fun associated with biking along it in a certain direction, depending on the incline and quality of the road, the number of animals passed, etc. Road fun-ness may be positive, but could also be be negative, e.g. when a road is difficult to traverse in a given direction, or passes by a scary dog, etc. The children would like to: choose a road intersection to meet and play tee-ball that maximizes the total fun of all three children in reaching their chosen meeting location; or alternatively, abandon tee-ball altogether in favor of biking, if a loop of roads exists in their district along which they can bike all day with ever increasing fun. Help the children organize their Saturday routine by finding a tee-ball location, or determining that there exists a continuously fun bike loop in their district (for now, you do not have to find such a loop). You may assume that each child can reach any road in the district by bike.
:::
