<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-6-q3" status="draft"}
Assume general position: the player $p$ is not on a wall line and no two endpoints are collinear with $p$ (perturb otherwise).

1. *Events.* The angles of all $2n$ endpoints as seen from $p$, sorted: $O(n\log n)$. A wall is *active* at angle $\phi$ if the ray from $p$ in direction $\phi$ meets it.

2. *Status.* The active walls ordered by the distance from $p$ at which the current ray meets them, in a balanced search tree. Since walls do not cross, this order does not change between events, so comparisons can be made by intersecting both walls with the current ray. Initialise with the walls met by the ray at angle $0$ ($O(n\log n)$).

3. *Sweep.* At each event angle insert the walls starting there and delete those ending there ($O(\log n)$ each). After processing the events at an angle, mark the nearest active wall (the minimum of the tree) as visible.

4. *Correctness.* A wall is visible exactly when it is the nearest wall along some ray from $p$ (a point of it is visible iff no wall crosses the segment to it). Between two consecutive event angles the set and order of active walls are fixed, so the nearest wall is constant and equals the minimum recorded after the earlier event. Walls seen only along a single event direction are tangent cases excluded by general position.

5. *Time.* $O(n)$ events of $O(\log n)$ each plus sorting: $O(n\log n)$.
:::
