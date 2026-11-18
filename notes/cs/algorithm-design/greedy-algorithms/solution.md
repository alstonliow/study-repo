<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046r-6-q2" status="draft"}
*Algorithm.* Sort the events by start time. Keep a min-heap of the clones keyed by the finish time of the last event each one attends. For each event $[s_i,f_i)$ in order: if the heap minimum is at most $s_i$, give the event to that clone and update its key to $f_i$; otherwise create a new clone with key $f_i$. Time $O(n\log n)$.

*Optimality.*

1. *Valid.* A clone receives an event only if its previous event finished by $s_i$, so each clone's events do not overlap.

2. *Lower bound.* Let the depth $d$ be the largest number of events that all contain a common time. Any solution needs at least $d$ clones, since those $d$ events must go to different clones.

3. *Greedy uses $d$.* Suppose the greedy opens clone number $k$ when handling event $i$. Then all $k-1$ existing clones end after $s_i$, and their current events started at or before $s_i$ (events are processed in start order). So those $k-1$ events and event $i$ all contain the time $s_i$: $k\le d$.

So the greedy uses exactly $d$ clones, which is optimal.
:::
